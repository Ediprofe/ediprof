<?php

namespace App\Filament\Resources\AssessmentBooklets\Tables;

use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\IconColumn;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;

class AssessmentBookletsTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->defaultSort('updated_at', 'desc')
            ->columns([
                TextColumn::make('title')
                    ->label('Cuadernillo')
                    ->searchable()
                    ->sortable()
                    ->wrap(),
                TextColumn::make('booklet_type')
                    ->label('Tipo')
                    ->badge()
                    ->formatStateUsing(fn (string $state): string => match ($state) {
                        'simulacro' => 'Simulacro',
                        'taller' => 'Taller',
                        'cuadernillo' => 'Cuadernillo',
                        default => ucfirst($state),
                    })
                    ->sortable(),
                TextColumn::make('origin_label')
                    ->label('Origen')
                    ->searchable()
                    ->sortable()
                    ->placeholder('Sin origen'),
                TextColumn::make('total_sections')
                    ->label('Secciones')
                    ->sortable(),
                TextColumn::make('total_questions')
                    ->label('Preguntas')
                    ->sortable(),
                TextColumn::make('school_year')
                    ->label('Año')
                    ->sortable()
                    ->placeholder('Sin año'),
                TextColumn::make('editorial_status')
                    ->label('Estado editorial')
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
                IconColumn::make('is_active')
                    ->label('Activo')
                    ->boolean(),
                TextColumn::make('updated_at')
                    ->label('Actualizado')
                    ->dateTime()
                    ->sortable()
                    ->toggleable(isToggledHiddenByDefault: true),
            ])
            ->filters([
                SelectFilter::make('booklet_type')
                    ->label('Tipo')
                    ->options([
                        'simulacro' => 'Simulacro',
                        'taller' => 'Taller',
                        'cuadernillo' => 'Cuadernillo',
                    ]),
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
                EditAction::make(),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    DeleteBulkAction::make(),
                ]),
            ])
            ->emptyStateHeading('Todavía no hay cuadernillos importados.')
            ->emptyStateDescription('Importa un simulacro o taller completo por bloques de materia para poblar el banco sin repetir origen ni unidad.');
    }
}
