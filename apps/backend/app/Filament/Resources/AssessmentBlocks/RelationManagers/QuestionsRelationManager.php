<?php

namespace App\Filament\Resources\AssessmentBlocks\RelationManagers;

use App\Filament\Resources\AssessmentQuestions\AssessmentQuestionResource;
use App\Models\AssessmentQuestion;
use Filament\Actions\Action;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Illuminate\Support\Str;

class QuestionsRelationManager extends RelationManager
{
    protected static string $relationship = 'questions';

    protected static ?string $title = 'Preguntas del bloque';

    public function table(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn ($query) => $query->withCount('contexts'))
            ->defaultSort('order_base')
            ->columns([
                TextColumn::make('order_base')
                    ->label('#')
                    ->sortable(),
                TextColumn::make('external_id')
                    ->label('ID')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('contexts_count')
                    ->label('Contextos')
                    ->sortable(),
                TextColumn::make('unit_label')
                    ->label('Unidad')
                    ->placeholder('Diferida'),
                TextColumn::make('correct_option_id')
                    ->label('Correcta')
                    ->badge(),
                TextColumn::make('stem_html')
                    ->label('Enunciado')
                    ->state(fn (AssessmentQuestion $record): string => Str::limit(
                        Str::of(strip_tags((string) $record->stem_html))->squish()->value(),
                        160
                    ))
                    ->wrap(),
            ])
            ->recordActions([
                Action::make('editQuestion')
                    ->label('Editar pregunta')
                    ->icon('heroicon-o-pencil-square')
                    ->url(fn (AssessmentQuestion $record): string => AssessmentQuestionResource::getUrl('edit', ['record' => $record], panel: 'admin')),
            ])
            ->emptyStateHeading('Este bloque todavía no tiene preguntas.');
    }
}
