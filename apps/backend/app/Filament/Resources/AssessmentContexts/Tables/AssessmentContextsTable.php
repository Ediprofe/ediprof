<?php

namespace App\Filament\Resources\AssessmentContexts\Tables;

use App\Models\AssessmentContext;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;
use Illuminate\Support\Str;

class AssessmentContextsTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn ($query) => $query->with(['template'])->withCount('questions'))
            ->defaultSort('updated_at', 'desc')
            ->columns([
                TextColumn::make('external_id')
                    ->label('ID local')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('source_key')
                    ->label('Clave global')
                    ->state(fn (AssessmentContext $record): string => $record->source_key)
                    ->copyable()
                    ->toggleable(isToggledHiddenByDefault: true),
                TextColumn::make('title')
                    ->label('Título')
                    ->searchable()
                    ->sortable()
                    ->placeholder('Sin título'),
                TextColumn::make('template.title')
                    ->label('Bloque')
                    ->searchable()
                    ->sortable()
                    ->wrap(),
                TextColumn::make('questions_count')
                    ->label('Preguntas')
                    ->sortable(),
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
                TextColumn::make('context_html')
                    ->label('Contexto')
                    ->state(fn (AssessmentContext $record): string => Str::limit(
                        Str::of(strip_tags((string) $record->context_html))->squish()->value(),
                        150
                    ))
                    ->wrap(),
            ])
            ->filters([
                SelectFilter::make('template_id')
                    ->label('Bloque')
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
            ->emptyStateHeading('Todavía no hay contextos sincronizados.')
            ->emptyStateDescription('Aquí revisas o corriges contextos específicos cuando necesitas trabajar al nivel de detalle del banco.');
    }
}
