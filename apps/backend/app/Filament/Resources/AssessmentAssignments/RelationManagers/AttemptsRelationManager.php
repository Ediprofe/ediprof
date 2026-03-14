<?php

namespace App\Filament\Resources\AssessmentAssignments\RelationManagers;

use App\Models\AssessmentAssignment;
use App\Models\AssessmentAttempt;
use App\Services\Assessments\AssessmentAttemptService;
use Filament\Actions\Action;
use Filament\Notifications\Notification;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;

class AttemptsRelationManager extends RelationManager
{
    protected static string $relationship = 'attempts';

    protected static ?string $title = 'Resultados e intentos';

    public function table(Table $table): Table
    {
        /** @var AssessmentAssignment $assignment */
        $assignment = $this->getOwnerRecord();

        return $table
            ->modifyQueryUsing(fn ($query) => $query
                ->with(['user'])
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
                    ->label('Correo')
                    ->searchable()
                    ->copyable()
                    ->toggleable(isToggledHiddenByDefault: true),
                TextColumn::make('status')
                    ->label('Estado')
                    ->badge()
                    ->formatStateUsing(fn (string $state): string => match ($state) {
                        'in_progress' => 'En progreso',
                        'submitted' => 'Entregado',
                        'graded' => 'Calificado',
                        'released' => 'Revisión liberada',
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
                TextColumn::make('review_state')
                    ->label('Revisión')
                    ->badge()
                    ->state(function (AssessmentAttempt $record) use ($assignment): string {
                        if ($record->review_released_at) {
                            return 'Disponible';
                        }

                        if ($record->status === 'in_progress') {
                            return 'Sin entregar';
                        }

                        if ($assignment->show_feedback_on_submit) {
                            return 'Disponible';
                        }

                        if (
                            $assignment->show_feedback_after_close &&
                            (
                                in_array($assignment->status, [AssessmentAssignment::STATUS_CLOSED, AssessmentAssignment::STATUS_ARCHIVED], true) ||
                                ($assignment->closes_at && $assignment->closes_at->isPast())
                            )
                        ) {
                            return 'Disponible';
                        }

                        return 'Oculta';
                    })
                    ->color(fn (string $state): string => $state === 'Disponible' ? 'success' : ($state === 'Sin entregar' ? 'gray' : 'warning')),
                TextColumn::make('started_at')
                    ->label('Inicio')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
                TextColumn::make('submitted_at')
                    ->label('Entrega')
                    ->dateTime()
                    ->sortable(),
                TextColumn::make('review_released_at')
                    ->label('Revisión liberada')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(),
            ])
            ->filters([
                SelectFilter::make('status')
                    ->label('Estado')
                    ->options([
                        'in_progress' => 'En progreso',
                        'submitted' => 'Entregado',
                        'graded' => 'Calificado',
                        'released' => 'Revisión liberada',
                    ]),
            ])
            ->headerActions([
                Action::make('exportAssignmentMinimalExcel')
                    ->label('Lista para pegar')
                    ->icon('heroicon-o-clipboard-document-list')
                    ->color('success')
                    ->url(
                        fn (): string => route('admin.exports.assignments.results.excel_minimal', ['assignment' => $assignment]),
                        shouldOpenInNewTab: true,
                    ),
                Action::make('exportAssignmentExcel')
                    ->label('Planilla de notas')
                    ->icon('heroicon-o-document-arrow-down')
                    ->color('warning')
                    ->url(
                        fn (): string => route('admin.exports.assignments.results.excel', ['assignment' => $assignment]),
                        shouldOpenInNewTab: true,
                    ),
                Action::make('exportAssignmentResults')
                    ->label('Exportar CSV detallado')
                    ->icon('heroicon-o-arrow-down-tray')
                    ->color('gray')
                    ->url(
                        fn (): string => route('admin.exports.assignments.results', ['assignment' => $assignment]),
                        shouldOpenInNewTab: true,
                    ),
                Action::make('releaseAllReviews')
                    ->label('Liberar revisión a entregados')
                    ->icon('heroicon-o-eye')
                    ->color('success')
                    ->requiresConfirmation()
                    ->modalDescription('Se habilitará la revisión para todos los intentos ya entregados de esta asignación.')
                    ->action(function () use ($assignment): void {
                        $released = app(AssessmentAttemptService::class)->releaseReviewsForAssignment($assignment);

                        Notification::make()
                            ->title('Revisión liberada')
                            ->body("Intentos actualizados: {$released}")
                            ->success()
                            ->send();
                    }),
            ])
            ->recordActions([
                Action::make('releaseReview')
                    ->label('Liberar revisión')
                    ->icon('heroicon-o-eye')
                    ->color('success')
                    ->requiresConfirmation()
                    ->visible(fn (AssessmentAttempt $record): bool => ! $record->review_released_at && in_array($record->status, ['submitted', 'graded'], true))
                    ->action(function (AssessmentAttempt $record): void {
                        app(AssessmentAttemptService::class)->releaseReview($record);

                        Notification::make()
                            ->title('Revisión liberada para el intento')
                            ->success()
                            ->send();
                    }),
            ])
            ->emptyStateHeading('Todavía no hay intentos de estudiantes.')
            ->emptyStateDescription('Cuando tus estudiantes entren a esta asignación, aquí verás puntaje, estado y revisión.');
    }
}
