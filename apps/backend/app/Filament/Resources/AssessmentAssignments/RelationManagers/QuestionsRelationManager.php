<?php

namespace App\Filament\Resources\AssessmentAssignments\RelationManagers;

use App\Models\AssessmentAssignment;
use App\Models\AssessmentAssignmentQuestion;
use App\Models\AssessmentQuestion;
use Filament\Actions\BulkActionGroup;
use Filament\Actions\CreateAction;
use Filament\Actions\DeleteAction;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Schemas\Schema;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Support\Str;

class QuestionsRelationManager extends RelationManager
{
    protected static string $relationship = 'questions';

    protected static ?string $title = 'Preguntas de la asignación';

    public function form(Schema $schema): Schema
    {
        /** @var AssessmentAssignment $assignment */
        $assignment = $this->getOwnerRecord();

        return $schema->components([
            Select::make('question_id')
                ->label('Pregunta')
                ->relationship(
                    name: 'question',
                    titleAttribute: 'external_id',
                    modifyQueryUsing: fn (Builder $query) => $query
                        ->where('template_id', $assignment->template_id)
                        ->where('is_active', true)
                        ->orderBy('order_base')
                )
                ->searchable(['external_id', 'source_slug'])
                ->preload()
                ->getOptionLabelFromRecordUsing(function (AssessmentQuestion $record): string {
                    $preview = Str::limit(
                        Str::of(strip_tags((string) $record->stem_html))->squish()->value(),
                        110
                    );

                    return "{$record->external_id} • {$preview}";
                })
                ->disabledOn('edit')
                ->required(),
            TextInput::make('order_base')
                ->label('Orden base')
                ->numeric()
                ->minValue(1)
                ->default(fn () => ((int) $assignment->questions()->max('order_base')) + 1)
                ->required(),
        ]);
    }

    public function table(Table $table): Table
    {
        return $table
            ->recordTitleAttribute('question.external_id')
            ->defaultSort('order_base')
            ->columns([
                TextColumn::make('order_base')
                    ->label('Orden')
                    ->sortable(),
                TextColumn::make('question.external_id')
                    ->label('ID pregunta')
                    ->searchable()
                    ->sortable(),
                TextColumn::make('question.source_slug')
                    ->label('Origen')
                    ->wrap()
                    ->toggleable(),
                TextColumn::make('question.stem_html')
                    ->label('Enunciado')
                    ->html()
                    ->state(fn (AssessmentAssignmentQuestion $record): string => e(
                        Str::limit(
                            Str::of(strip_tags((string) $record->question?->stem_html))->squish()->value(),
                            150
                        )
                    ))
                    ->wrap(),
            ])
            ->headerActions([
                CreateAction::make()
                    ->label('Seleccionar subconjunto')
                    ->modalHeading('Añadir pregunta a la asignación')
                    ->successNotificationTitle('Pregunta añadida.')
                    ->using(function (array $data): AssessmentAssignmentQuestion {
                        /** @var AssessmentAssignment $assignment */
                        $assignment = $this->getOwnerRecord();

                        return AssessmentAssignmentQuestion::query()->updateOrCreate(
                            [
                                'assignment_id' => $assignment->id,
                                'question_id' => $data['question_id'],
                            ],
                            [
                                'order_base' => (int) $data['order_base'],
                            ],
                        );
                    }),
            ])
            ->recordActions([
                EditAction::make()
                    ->modalHeading('Actualizar orden de la pregunta')
                    ->successNotificationTitle('Pregunta actualizada.'),
                DeleteAction::make()
                    ->label('Quitar'),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    DeleteBulkAction::make(),
                ]),
            ])
            ->emptyStateHeading('Se usará la plantilla completa si no seleccionas preguntas.')
            ->emptyStateDescription('Añade preguntas solo cuando quieras una evaluación con subconjunto y orden base propio. Si dejas esta tabla vacía, se usarán todas las preguntas de la plantilla base.');
    }
}
