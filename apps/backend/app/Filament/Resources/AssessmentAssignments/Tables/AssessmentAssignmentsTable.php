<?php

namespace App\Filament\Resources\AssessmentAssignments\Tables;

use App\Filament\Resources\AssessmentAssignments\AssessmentAssignmentResource;
use App\Models\AssessmentAssignment;
use Filament\Actions\Action;
use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\IconColumn;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;

class AssessmentAssignmentsTable
{
    public static function configure(Table $table, bool $includeCourse = true): Table
    {
        return $table
            ->modifyQueryUsing(fn ($query) => $query->withCount(['questions', 'attempts']))
            ->defaultSort('updated_at', 'desc')
            ->columns(array_values(array_filter([
                TextColumn::make('title')
                    ->label('Asignación')
                    ->searchable()
                    ->sortable()
                    ->wrap(),
                $includeCourse
                    ? TextColumn::make('course.name')
                        ->label('Curso')
                        ->searchable()
                        ->sortable()
                    : null,
                TextColumn::make('template.title')
                    ->label('Plantilla')
                    ->searchable()
                    ->sortable()
                    ->wrap(),
                TextColumn::make('mode')
                    ->label('Modo')
                    ->badge()
                    ->formatStateUsing(fn (string $state): string => AssessmentAssignment::modeOptions()[$state] ?? ucfirst($state))
                    ->color(fn (string $state): string => match ($state) {
                        AssessmentAssignment::MODE_STUDY => 'primary',
                        AssessmentAssignment::MODE_EVALUATION => 'danger',
                        default => 'warning',
                    }),
                TextColumn::make('status')
                    ->label('Estado')
                    ->badge()
                    ->formatStateUsing(fn (string $state): string => AssessmentAssignment::statusOptions()[$state] ?? ucfirst($state))
                    ->color(fn (string $state): string => match ($state) {
                        AssessmentAssignment::STATUS_ACTIVE => 'success',
                        AssessmentAssignment::STATUS_CLOSED, AssessmentAssignment::STATUS_ARCHIVED => 'gray',
                        default => 'warning',
                    }),
                TextColumn::make('questions_count')
                    ->label('Preguntas')
                    ->state(fn (AssessmentAssignment $record): string => $record->questions_count > 0
                        ? (string) $record->questions_count
                        : 'Toda la plantilla ('.($record->template?->total_questions ?? 0).')')
                    ->tooltip(fn (AssessmentAssignment $record): ?string => $record->questions_count > 0
                        ? 'Esta asignación usa un subconjunto configurado manualmente.'
                        : 'Todavía no tiene preguntas seleccionadas manualmente, así que usará toda la plantilla base.')
                    ->toggleable(),
                TextColumn::make('attempts_count')
                    ->label('Intentos')
                    ->sortable(),
                IconColumn::make('randomize_questions')
                    ->label('Aleatoria')
                    ->boolean(),
                TextColumn::make('opens_at')
                    ->label('Apertura')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
                TextColumn::make('closes_at')
                    ->label('Cierre')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
                TextColumn::make('updated_at')
                    ->label('Actualizada')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
            ])))
            ->filters(array_values(array_filter([
                $includeCourse
                    ? SelectFilter::make('course_id')
                        ->label('Curso')
                        ->relationship('course', 'name')
                    : null,
                SelectFilter::make('mode')
                    ->label('Modo')
                    ->options(AssessmentAssignment::modeOptions()),
                SelectFilter::make('status')
                    ->label('Estado')
                    ->options(AssessmentAssignment::statusOptions()),
            ])))
            ->recordActions([
                Action::make('configureQuestions')
                    ->label('Configurar preguntas')
                    ->icon('heroicon-o-list-bullet')
                    ->url(fn (AssessmentAssignment $record): string => AssessmentAssignmentResource::getUrl('edit', ['record' => $record])),
                EditAction::make(),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    DeleteBulkAction::make(),
                ]),
            ])
            ->emptyStateHeading('Todavía no hay asignaciones académicas.')
            ->emptyStateDescription('Crea una asignación para transformar una plantilla en un estudio guiado, simulacro o evaluación real.');
    }
}
