<?php

namespace App\Filament\Resources\AssessmentBlocks\RelationManagers;

use App\Filament\Resources\AssessmentContexts\AssessmentContextResource;
use App\Models\AssessmentContext;
use Filament\Actions\Action;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Illuminate\Support\Str;

class ContextsRelationManager extends RelationManager
{
    protected static string $relationship = 'contexts';

    protected static ?string $title = 'Contextos del bloque';

    public function table(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn ($query) => $query->withCount('questions'))
            ->defaultSort('order_base')
            ->columns([
                TextColumn::make('order_base')
                    ->label('#')
                    ->sortable(),
                TextColumn::make('title')
                    ->label('Contexto')
                    ->searchable()
                    ->wrap()
                    ->placeholder('Sin título'),
                TextColumn::make('questions_count')
                    ->label('Preguntas vinculadas')
                    ->sortable(),
                TextColumn::make('unit_label')
                    ->label('Unidad')
                    ->placeholder('Diferida'),
                TextColumn::make('context_html')
                    ->label('Preview')
                    ->state(fn (AssessmentContext $record): string => Str::limit(
                        Str::of(strip_tags((string) $record->context_html))->squish()->value(),
                        150
                    ))
                    ->wrap(),
            ])
            ->recordActions([
                Action::make('editContext')
                    ->label('Editar contexto')
                    ->icon('heroicon-o-pencil-square')
                    ->url(fn (AssessmentContext $record): string => AssessmentContextResource::getUrl('edit', ['record' => $record], panel: 'admin')),
            ])
            ->emptyStateHeading('Este bloque todavía no tiene contextos.');
    }
}
