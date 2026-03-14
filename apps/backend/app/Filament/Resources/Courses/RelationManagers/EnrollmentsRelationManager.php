<?php

namespace App\Filament\Resources\Courses\RelationManagers;

use App\Models\CourseEnrollment;
use App\Models\User;
use App\Services\Courses\CourseEnrollmentImportService;
use Filament\Actions\Action;
use Filament\Actions\BulkActionGroup;
use Filament\Actions\CreateAction;
use Filament\Actions\DeleteAction;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Forms\Components\FileUpload;
use Filament\Forms\Components\Select;
use Filament\Notifications\Notification;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Schemas\Schema;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Support\Facades\Storage;

class EnrollmentsRelationManager extends RelationManager
{
    protected static string $relationship = 'enrollments';

    protected static ?string $title = 'Estudiantes matriculados';

    public function form(Schema $schema): Schema
    {
        return $schema->components([
            Select::make('user_id')
                ->label('Estudiante')
                ->relationship(
                    name: 'user',
                    titleAttribute: 'email',
                    modifyQueryUsing: fn (Builder $query) => $query
                        ->where('role', 'student')
                        ->orderBy('last_names')
                        ->orderBy('first_names')
                        ->orderBy('name')
                )
                ->searchable(['name', 'first_names', 'last_names', 'email', 'institutional_code', 'document_number'])
                ->preload()
                ->getOptionLabelFromRecordUsing(
                    fn (User $record): string => "{$record->academic_sort_name} • {$record->email}"
                )
                ->disabledOn('edit')
                ->required(),
            Select::make('status')
                ->label('Estado de matrícula')
                ->options([
                    'active' => 'Activa',
                    'inactive' => 'Inactiva',
                ])
                ->default('active')
                ->required(),
        ]);
    }

    public function table(Table $table): Table
    {
        return $table
            ->recordTitleAttribute('user.email')
            ->columns([
                TextColumn::make('user.last_names')
                    ->label('Apellidos')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('user.first_names')
                    ->label('Nombres')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('user.institutional_code')
                    ->label('Matrícula')
                    ->searchable()
                    ->sortable()
                    ->toggleable(),
                TextColumn::make('user.document_number')
                    ->label('Documento')
                    ->searchable()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
                TextColumn::make('user.email')
                    ->label('Correo institucional')
                    ->searchable()
                    ->copyable(),
                TextColumn::make('status')
                    ->label('Estado')
                    ->badge()
                    ->formatStateUsing(fn (string $state): string => $state === 'active' ? 'Activa' : 'Inactiva')
                    ->color(fn (string $state): string => $state === 'active' ? 'success' : 'gray'),
                TextColumn::make('source')
                    ->label('Origen')
                    ->badge()
                    ->formatStateUsing(fn (string $state): string => match ($state) {
                        'csv_import' => 'CSV',
                        default => 'Manual',
                    }),
                TextColumn::make('created_at')
                    ->label('Asignado')
                    ->dateTime()
                    ->sortable(),
            ])
            ->headerActions([
                CreateAction::make()
                    ->label('Matricular estudiante')
                    ->modalHeading('Matricular estudiante')
                    ->successNotificationTitle('Estudiante matriculado.')
                    ->using(function (array $data): CourseEnrollment {
                        /** @var \App\Models\Course $course */
                        $course = $this->getOwnerRecord();

                        return CourseEnrollment::query()->updateOrCreate(
                            [
                                'course_id' => $course->id,
                                'user_id' => $data['user_id'],
                            ],
                            [
                                'status' => $data['status'],
                                'source' => 'manual',
                            ],
                        );
                    }),
                Action::make('importCsv')
                    ->label('Importar CSV')
                    ->icon('heroicon-o-arrow-up-tray')
                    ->color('gray')
                    ->schema([
                        FileUpload::make('csv')
                            ->label('Archivo CSV')
                            ->helperText('Encabezados recomendados: matricula, documento, grupo, apellidos, nombres, correo. También acepta nombre usuario y correo electrónico.')
                            ->acceptedFileTypes([
                                'text/csv',
                                'text/plain',
                                'application/csv',
                                'application/vnd.ms-excel',
                            ])
                            ->disk('local')
                            ->directory('temp/course-enrollments')
                            ->required(),
                    ])
                    ->action(function (array $data, CourseEnrollmentImportService $importService): void {
                        /** @var \App\Models\Course $course */
                        $course = $this->getOwnerRecord();
                        $path = $data['csv'] ?? null;

                        if (! is_string($path) || $path === '') {
                            Notification::make()
                                ->title('No se encontró el archivo CSV.')
                                ->danger()
                                ->send();

                            return;
                        }

                        $result = $importService->importFromStoragePath($course, $path);
                        Storage::disk('local')->delete($path);

                        $summary = $result['summary'];
                        $errors = $result['errors'];

                        Notification::make()
                            ->title('Importación completada')
                            ->body(
                                "Matriculados: {$summary['enrolled_users']} · Nuevos usuarios: {$summary['created_users']} · " .
                                "Actualizados: {$summary['updated_users']} · Errores: {$summary['error_count']}"
                            )
                            ->{$summary['error_count'] > 0 ? 'warning' : 'success'}()
                            ->send();

                        if ($summary['error_count'] > 0) {
                            Notification::make()
                                ->title('Revisa el CSV')
                                ->body('Algunas filas no se importaron. Puedes volver a intentar con el archivo corregido.')
                                ->warning()
                                ->send();
                        }
                    }),
            ])
            ->recordActions([
                EditAction::make()
                    ->modalHeading('Actualizar matrícula')
                    ->successNotificationTitle('Matrícula actualizada.'),
                DeleteAction::make()
                    ->label('Retirar'),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    DeleteBulkAction::make(),
                ]),
            ])
            ->emptyStateHeading('Este curso todavía no tiene estudiantes matriculados.')
            ->emptyStateDescription('Puedes matricularlos manualmente o importar el CSV del grupo.');
    }
}
