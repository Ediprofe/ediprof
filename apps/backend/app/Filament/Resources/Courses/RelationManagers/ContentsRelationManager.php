<?php

namespace App\Filament\Resources\Courses\RelationManagers;

use App\Models\CourseContent;
use App\Models\Workshop;
use Filament\Actions\BulkActionGroup;
use Filament\Actions\CreateAction;
use Filament\Actions\DeleteAction;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\Toggle;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Schemas\Schema;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Builder;

class ContentsRelationManager extends RelationManager
{
    protected static string $relationship = 'contents';

    protected static ?string $title = 'Biblioteca del curso';

    public function form(Schema $schema): Schema
    {
        return $schema->components([
            Select::make('workshop_id')
                ->label('Contenido')
                ->relationship(
                    name: 'workshop',
                    titleAttribute: 'title',
                    modifyQueryUsing: fn (Builder $query) => $query
                        ->where('is_published', true)
                        ->orderBy('title')
                )
                ->searchable(['title', 'route'])
                ->preload()
                ->getOptionLabelFromRecordUsing(
                    fn (Workshop $record): string => "{$record->title} • {$record->content_type}"
                )
                ->disabledOn('edit')
                ->required(),
            Toggle::make('is_active')
                ->label('Disponible para estudiantes')
                ->default(true)
                ->required(),
        ]);
    }

    public function table(Table $table): Table
    {
        return $table
            ->recordTitleAttribute('workshop.title')
            ->columns([
                TextColumn::make('workshop.title')
                    ->label('Contenido')
                    ->searchable()
                    ->wrap(),
                TextColumn::make('workshop.content_type')
                    ->label('Tipo')
                    ->badge()
                    ->formatStateUsing(fn (string $state): string => $state === 'simulacro' ? 'Simulacro' : 'Taller')
                    ->color(fn (string $state): string => $state === 'simulacro' ? 'warning' : 'primary'),
                TextColumn::make('workshop.route')
                    ->label('Ruta pública')
                    ->copyable()
                    ->toggleable(),
                TextColumn::make('is_active')
                    ->label('Estado')
                    ->badge()
                    ->formatStateUsing(fn (bool $state): string => $state ? 'Activo' : 'Inactivo')
                    ->color(fn (bool $state): string => $state ? 'success' : 'gray'),
                TextColumn::make('created_at')
                    ->label('Asignado')
                    ->dateTime()
                    ->sortable(),
            ])
            ->headerActions([
                CreateAction::make()
                    ->label('Asignar contenido')
                    ->modalHeading('Asignar taller o simulacro')
                    ->successNotificationTitle('Biblioteca actualizada.')
                    ->using(function (array $data): CourseContent {
                        /** @var \App\Models\Course $course */
                        $course = $this->getOwnerRecord();

                        return CourseContent::query()->updateOrCreate(
                            [
                                'course_id' => $course->id,
                                'workshop_id' => $data['workshop_id'],
                            ],
                            [
                                'is_active' => (bool) ($data['is_active'] ?? true),
                            ],
                        );
                    }),
            ])
            ->recordActions([
                EditAction::make()
                    ->modalHeading('Actualizar acceso al contenido')
                    ->successNotificationTitle('Contenido actualizado.'),
                DeleteAction::make()
                    ->label('Quitar'),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    DeleteBulkAction::make(),
                ]),
            ])
            ->emptyStateHeading('Este curso todavía no tiene biblioteca asignada.')
            ->emptyStateDescription('Añade talleres o simulacros publicados para habilitar la práctica del grupo.');
    }
}
