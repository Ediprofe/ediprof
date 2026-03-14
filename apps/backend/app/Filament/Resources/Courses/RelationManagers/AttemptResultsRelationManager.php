<?php

namespace App\Filament\Resources\Courses\RelationManagers;

use App\Filament\Resources\AssessmentAssignments\AssessmentAssignmentResource;
use App\Models\AssessmentAttempt;
use Filament\Actions\Action;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;

class AttemptResultsRelationManager extends RelationManager
{
    protected static string $relationship = 'attempts';

    protected static ?string $title = 'Resultados del curso';

    public function table(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn ($query) => $query
                ->with(['user', 'assignment'])
                ->withCount('answers')
                ->orderBy(
                    \App\Models\User::query()
                        ->selectRaw("COALESCE(last_names, '')")
                        ->whereColumn('users.id', 'assessment_attempts.user_id')
                )
                ->orderBy(
                    \App\Models\User::query()
                        ->selectRaw("COALESCE(first_names, '')")
                        ->whereColumn('users.id', 'assessment_attempts.user_id')
                )
                ->orderBy(
                    \App\Models\User::query()
                        ->selectRaw("COALESCE(institutional_code, '')")
                        ->whereColumn('users.id', 'assessment_attempts.user_id')
                )
                ->orderBy('submitted_at'))
            ->columns([
                TextColumn::make('assignment.title')
                    ->label('Asignacion')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('user.last_names')
                    ->label('Apellidos')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('user.first_names')
                    ->label('Nombres')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('user.institutional_code')
                    ->label('Matricula')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('user.document_number')
                    ->label('Documento')
                    ->searchable()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
                TextColumn::make('user.email')
                    ->label('Correo institucional')
                    ->searchable()
                    ->copyable()
                    ->toggleable(),
                TextColumn::make('mode')
                    ->label('Modo')
                    ->badge()
                    ->formatStateUsing(fn (string $state): string => match ($state) {
                        'study' => 'Estudio guiado',
                        'simulacro' => 'Simulacro',
                        'evaluation' => 'Evaluacion',
                        default => ucfirst($state),
                    }),
                TextColumn::make('status')
                    ->label('Estado')
                    ->badge()
                    ->formatStateUsing(fn (string $state): string => match ($state) {
                        'in_progress' => 'En progreso',
                        'submitted' => 'Entregado',
                        'graded' => 'Calificado',
                        'released' => 'Revision liberada',
                        default => ucfirst($state),
                    })
                    ->color(fn (string $state): string => match ($state) {
                        'in_progress' => 'warning',
                        'released' => 'success',
                        'submitted', 'graded' => 'primary',
                        default => 'gray',
                    }),
                TextColumn::make('answers_progress')
                    ->label('Respondidas')
                    ->state(fn (AssessmentAttempt $record): string => sprintf(
                        '%d / %d',
                        (int) ($record->answers_count ?? 0),
                        (int) $record->total_questions
                    )),
                TextColumn::make('score_percent')
                    ->label('Puntaje')
                    ->formatStateUsing(fn ($state): string => $state === null ? 'Pendiente' : "{$state}%")
                    ->sortable(),
                TextColumn::make('score_scale')
                    ->label('Nota / 5')
                    ->formatStateUsing(fn ($state): string => $state === null ? 'Pendiente' : number_format((float) $state, 2).'/5')
                    ->sortable(),
                TextColumn::make('submitted_at')
                    ->label('Entrega')
                    ->dateTime()
                    ->sortable(),
                TextColumn::make('review_released_at')
                    ->label('Revision liberada')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(),
            ])
            ->filters([
                SelectFilter::make('assignment_id')
                    ->label('Asignacion')
                    ->relationship('assignment', 'title'),
                SelectFilter::make('mode')
                    ->label('Modo')
                    ->options([
                        'study' => 'Estudio guiado',
                        'simulacro' => 'Simulacro',
                        'evaluation' => 'Evaluacion',
                    ]),
                SelectFilter::make('status')
                    ->label('Estado')
                    ->options([
                        'in_progress' => 'En progreso',
                        'submitted' => 'Entregado',
                        'graded' => 'Calificado',
                        'released' => 'Revision liberada',
                    ]),
            ])
            ->headerActions([
                Action::make('exportCourseResults')
                    ->label('Exportar CSV')
                    ->icon('heroicon-o-arrow-down-tray')
                    ->color('gray')
                    ->url(
                        fn (): string => route('admin.exports.courses.results', ['course' => $this->getOwnerRecord()]),
                        shouldOpenInNewTab: true,
                    ),
            ])
            ->recordActions([
                Action::make('openAssignment')
                    ->label('Ver asignacion')
                    ->icon('heroicon-o-arrow-top-right-on-square')
                    ->url(
                        fn (AssessmentAttempt $record): string => AssessmentAssignmentResource::getUrl('edit', ['record' => $record->assignment_id]),
                        shouldOpenInNewTab: true,
                    ),
            ])
            ->emptyStateHeading('Todavia no hay resultados en este curso.')
            ->emptyStateDescription('Cuando las estudiantes entreguen sus asignaciones, aqui podras revisar y exportar el consolidado.');
    }
}
