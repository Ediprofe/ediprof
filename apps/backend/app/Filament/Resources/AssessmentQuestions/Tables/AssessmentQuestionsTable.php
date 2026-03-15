<?php

namespace App\Filament\Resources\AssessmentQuestions\Tables;

use App\Models\AssessmentBooklet;
use App\Models\AssessmentUnit;
use App\Services\Content\AssessmentQuestionBulkClassificationService;
use Filament\Actions\BulkAction;
use Filament\Actions\BulkActionGroup;
use App\Models\AssessmentQuestion;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TagsInput;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Toggle;
use Filament\Notifications\Notification;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Filters\TernaryFilter;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Collection;
use Illuminate\Support\Str;

class AssessmentQuestionsTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn ($query) => $query->with(['template', 'contexts'])->withCount(['contexts', 'booklets']))
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
                    ->label('Bloque')
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
                TextColumn::make('booklets_count')
                    ->label('Cuadernillos')
                    ->sortable()
                    ->toggleable()
                    ->placeholder('0'),
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
                    ->label('Bloque')
                    ->relationship('template', 'title'),
                SelectFilter::make('subject_id')
                    ->label('Materia')
                    ->relationship('subject', 'label'),
                SelectFilter::make('origin_collection_id')
                    ->label('Origen')
                    ->relationship('originCollection', 'label'),
                SelectFilter::make('booklet_id')
                    ->label('Cuadernillo')
                    ->options(fn (): array => AssessmentBooklet::query()->orderBy('title')->pluck('title', 'id')->all())
                    ->query(function (Builder $query, array $data): Builder {
                        $value = $data['value'] ?? null;

                        if (! filled($value)) {
                            return $query;
                        }

                        return $query->whereHas('booklets', fn (Builder $booklets): Builder => $booklets->whereKey((int) $value));
                    }),
                SelectFilter::make('editorial_status')
                    ->label('Estado editorial')
                    ->options([
                        'draft' => 'Borrador',
                        'ready' => 'Lista para usar',
                        'review' => 'Revisar',
                        'archived' => 'Archivada',
                    ]),
                TernaryFilter::make('unit_id')
                    ->label('Unidad asignada')
                    ->placeholder('Todas')
                    ->trueLabel('Con unidad')
                    ->falseLabel('Sin unidad')
                    ->queries(
                        true: fn (Builder $query): Builder => $query->whereNotNull('unit_id'),
                        false: fn (Builder $query): Builder => $query->whereNull('unit_id'),
                        blank: fn (Builder $query): Builder => $query,
                    ),
            ])
            ->recordActions([
                EditAction::make(),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    BulkAction::make('classifySelection')
                        ->label('Clasificar selección')
                        ->icon('heroicon-o-tag')
                        ->schema([
                            Select::make('unit_id')
                                ->label('Asignar unidad')
                                ->helperText('Opcional. Si la dejas vacía, no se cambia la unidad.')
                                ->options(fn (): array => AssessmentUnit::query()
                                    ->where('is_active', true)
                                    ->with('subject')
                                    ->orderBy('label')
                                    ->get()
                                    ->mapWithKeys(fn (AssessmentUnit $unit): array => [
                                        $unit->id => sprintf('%s · %s', $unit->subject?->label ?? 'Sin materia', $unit->label),
                                    ])
                                    ->all())
                                ->searchable()
                                ->preload()
                                ->native(false),
                            TextInput::make('topic')
                                ->label('Tema')
                                ->helperText('Opcional. Solo se aplica si escribes algo.'),
                            TextInput::make('subtopic')
                                ->label('Subtema')
                                ->helperText('Opcional. Solo se aplica si escribes algo.'),
                            Select::make('editorial_status')
                                ->label('Estado editorial')
                                ->options([
                                    'draft' => 'Borrador',
                                    'ready' => 'Lista para usar',
                                    'review' => 'Revisar',
                                    'archived' => 'Archivada',
                                ])
                                ->native(false)
                                ->helperText('Opcional. Solo se aplica si eliges un estado.'),
                            TagsInput::make('tags')
                                ->label('Tags a agregar')
                                ->helperText('Se suman a los tags existentes; no los reemplazan.'),
                            Toggle::make('sync_linked_contexts')
                                ->label('Sincronizar contextos vinculados')
                                ->helperText('Recomendado cuando el cuadernillo viene por bloques de una misma materia.')
                                ->default(true),
                        ])
                        ->action(function (Collection $records, array $data): void {
                            $summary = app(AssessmentQuestionBulkClassificationService::class)->classify($records, $data);

                            Notification::make()
                                ->title('Clasificación aplicada')
                                ->body(
                                    'Preguntas actualizadas: '.$summary['questions_updated'].
                                    ' · Contextos actualizados: '.$summary['contexts_updated'].
                                    ' · Preguntas omitidas por incompatibilidad de unidad: '.$summary['questions_skipped_unit_mismatch'].
                                    ' · Contextos omitidos: '.$summary['contexts_skipped_unit_mismatch']
                                )
                                ->success()
                                ->send();
                        }),
                ]),
            ])
            ->emptyStateHeading('Todavía no hay preguntas sincronizadas.')
            ->emptyStateDescription('Aquí entras cuando necesitas afinar o corregir preguntas puntuales dentro del banco editorial.');
    }
}
