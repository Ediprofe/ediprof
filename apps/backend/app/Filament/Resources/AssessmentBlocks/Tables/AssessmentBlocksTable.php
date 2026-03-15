<?php

namespace App\Filament\Resources\AssessmentBlocks\Tables;

use App\Filament\Resources\AssessmentBlocks\AssessmentBlockResource;
use App\Models\AssessmentTemplate;
use Filament\Actions\Action;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;
use Illuminate\Support\Str;

class AssessmentBlocksTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn ($query) => $query->withCount(['contexts', 'questions']))
            ->defaultSort('updated_at', 'desc')
            ->columns([
                TextColumn::make('title')
                    ->label('Bloque')
                    ->searchable()
                    ->sortable()
                    ->wrap(),
                TextColumn::make('subject_label')
                    ->label('Materia')
                    ->searchable()
                    ->sortable()
                    ->placeholder('Sin materia'),
                TextColumn::make('unit_label')
                    ->label('Unidad')
                    ->searchable()
                    ->sortable()
                    ->placeholder('Unidad diferida'),
                TextColumn::make('origin_label')
                    ->label('Origen')
                    ->searchable()
                    ->sortable()
                    ->placeholder('Sin origen'),
                TextColumn::make('contexts_count')
                    ->label('Contextos')
                    ->sortable(),
                TextColumn::make('questions_count')
                    ->label('Preguntas')
                    ->sortable(),
                TextColumn::make('editorial_status')
                    ->label('Estado')
                    ->badge()
                    ->formatStateUsing(fn (?string $state): string => match ($state) {
                        'ready' => 'Lista para usar',
                        'review' => 'Revisar',
                        'archived' => 'Archivado',
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
                TextColumn::make('contexts_preview')
                    ->label('Contexto principal')
                    ->state(fn (AssessmentTemplate $record): string => Str::limit(
                        Str::of(strip_tags((string) optional($record->contexts()->orderBy('order_base')->first())->context_html))->squish()->value(),
                        160
                    ))
                    ->wrap()
                    ->placeholder('Sin preview'),
            ])
            ->filters([
                SelectFilter::make('subject_id')
                    ->label('Materia')
                    ->relationship('subject', 'label'),
                SelectFilter::make('origin_collection_id')
                    ->label('Origen')
                    ->relationship('originCollection', 'label'),
                SelectFilter::make('editorial_status')
                    ->label('Estado editorial')
                    ->options([
                        'draft' => 'Borrador',
                        'ready' => 'Lista para usar',
                        'review' => 'Revisar',
                        'archived' => 'Archivado',
                    ]),
            ])
            ->recordActions([
                Action::make('previewWeb')
                    ->label('Preview')
                    ->icon('heroicon-o-globe-alt')
                    ->color('gray')
                    ->url(fn (AssessmentTemplate $record): string => route('admin.assessment_drafts.preview_web', $record), shouldOpenInNewTab: true),
                EditAction::make(),
            ])
            ->emptyStateHeading('Todavía no hay bloques contextuales en el banco.')
            ->emptyStateDescription('Importa bloques con IA o desde un cuadernillo para construir el banco editorial reutilizable.');
    }
}
