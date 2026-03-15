<?php

namespace App\Filament\Resources\AssessmentQuestions\Tables;

use App\Models\AssessmentQuestion;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;
use Illuminate\Support\Str;

class AssessmentQuestionsTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn ($query) => $query->with(['template', 'contexts']))
            ->defaultSort('updated_at', 'desc')
            ->columns([
                TextColumn::make('external_id')
                    ->label('ID local')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('source_key')
                    ->label('Clave global')
                    ->state(fn (AssessmentQuestion $record): string => $record->source_key)
                    ->toggleable(isToggledHiddenByDefault: true)
                    ->copyable(),
                TextColumn::make('template.title')
                    ->label('Plantilla')
                    ->searchable()
                    ->sortable()
                    ->wrap(),
                TextColumn::make('subject_label')
                    ->label('Materia')
                    ->searchable()
                    ->sortable()
                    ->placeholder('Sin clasificar'),
                TextColumn::make('unit_label')
                    ->label('Unidad')
                    ->searchable()
                    ->sortable()
                    ->placeholder('Sin clasificar'),
                TextColumn::make('origin_label')
                    ->label('Origen')
                    ->searchable()
                    ->toggleable()
                    ->placeholder('Sin clasificar'),
                TextColumn::make('editorial_status')
                    ->label('Estado editorial')
                    ->badge()
                    ->sortable()
                    ->formatStateUsing(fn (?string $state): string => match ($state) {
                        'ready' => 'Lista para usar',
                        'review' => 'Revisar',
                        'archived' => 'Archivada',
                        'draft' => 'Borrador',
                        default => 'Sin estado',
                    })
                    ->color(fn (?string $state): string => match ($state) {
                        'ready' => 'success',
                        'review' => 'warning',
                        'archived' => 'gray',
                        'draft' => 'danger',
                        default => 'gray',
                    }),
                TextColumn::make('contexts_count')
                    ->label('Contextos')
                    ->state(fn (AssessmentQuestion $record): int => $record->contexts->count())
                    ->toggleable(),
                TextColumn::make('stem_html')
                    ->label('Enunciado')
                    ->state(fn (AssessmentQuestion $record): string => Str::limit(
                        Str::of(strip_tags((string) $record->stem_html))->squish()->value(),
                        150
                    ))
                    ->wrap(),
                TextColumn::make('updated_at')
                    ->label('Actualizada')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
            ])
            ->filters([
                SelectFilter::make('template_id')
                    ->label('Plantilla')
                    ->relationship('template', 'title'),
                SelectFilter::make('editorial_status')
                    ->label('Estado editorial')
                    ->options([
                        'draft' => 'Borrador',
                        'ready' => 'Lista para usar',
                        'review' => 'Revisar',
                        'archived' => 'Archivada',
                    ]),
            ])
            ->recordActions([
                EditAction::make(),
            ])
            ->emptyStateHeading('Todavía no hay preguntas sincronizadas.')
            ->emptyStateDescription('Aquí administras la clasificación mínima del banco canónico y su estado editorial.');
    }
}
