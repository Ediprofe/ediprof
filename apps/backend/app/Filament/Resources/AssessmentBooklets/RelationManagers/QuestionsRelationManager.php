<?php

namespace App\Filament\Resources\AssessmentBooklets\RelationManagers;

use App\Filament\Resources\AssessmentQuestions\AssessmentQuestionResource;
use Filament\Actions\Action;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Schemas\Schema;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Illuminate\Support\Str;

class QuestionsRelationManager extends RelationManager
{
    protected static string $relationship = 'questions';

    protected static ?string $title = 'Preguntas vinculadas';

    public function form(Schema $schema): Schema
    {
        return $schema->components([]);
    }

    public function table(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn ($query) => $query->with(['template', 'bookletSections']))
            ->defaultSort('assessment_booklet_questions.order_base')
            ->columns([
                TextColumn::make('pivot.order_base')
                    ->label('#')
                    ->sortable(),
                TextColumn::make('external_id')
                    ->label('ID local')
                    ->searchable()
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
                    ->placeholder('Unidad diferida'),
                TextColumn::make('template.title')
                    ->label('Plantilla')
                    ->wrap(),
                TextColumn::make('stem_html')
                    ->label('Enunciado')
                    ->state(fn ($record): string => Str::limit(
                        Str::of(strip_tags((string) $record->stem_html))->squish()->value(),
                        140
                    ))
                    ->wrap(),
            ])
            ->recordActions([
                Action::make('openQuestion')
                    ->label('Editar pregunta')
                    ->icon('heroicon-o-pencil-square')
                    ->url(fn ($record): string => AssessmentQuestionResource::getUrl('edit', ['record' => $record], panel: 'admin')),
            ])
            ->emptyStateHeading('Este cuadernillo todavía no tiene preguntas vinculadas.');
    }
}
