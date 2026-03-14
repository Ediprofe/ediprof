<?php

namespace App\Filament\Resources\AssessmentAssignments\RelationManagers;

use App\Models\AssessmentAssignment;
use App\Models\AssessmentAssignmentQuestion;
use App\Models\AssessmentQuestion;
use App\Services\Assessments\AssessmentAssignmentSelectionService;
use App\Services\Assessments\AssessmentQuestionGroupService;
use Filament\Actions\Action;
use Filament\Actions\CreateAction;
use Filament\Forms\Components\Select;
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
                ->helperText('Si la pregunta comparte contexto con otras, la asignación incorporará ese bloque completo y lo mantendrá unido en la evaluación.')
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
                TextColumn::make('selection_group_key')
                    ->label('Unidad')
                    ->state(function (AssessmentAssignmentQuestion $record): string {
                        $question = $record->question;
                        if (! $question instanceof AssessmentQuestion) {
                            return 'Pregunta individual';
                        }

                        return app(AssessmentQuestionGroupService::class)->describeBundle($question);
                    })
                    ->badge()
                    ->color(fn (string $state): string => str_contains($state, 'Contexto compartido') ? 'warning' : 'gray'),
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
                    ->successNotificationTitle('Selección actualizada.')
                    ->using(function (array $data): AssessmentAssignmentQuestion {
                        /** @var AssessmentAssignment $assignment */
                        $assignment = $this->getOwnerRecord();
                        /** @var AssessmentQuestion $question */
                        $question = AssessmentQuestion::query()
                            ->with([
                                'template',
                                'contexts' => fn ($query) => $query
                                    ->where('assessment_contexts.is_active', true)
                                    ->orderBy('assessment_question_contexts.order_base'),
                            ])
                            ->findOrFail($data['question_id']);

                        return app(AssessmentAssignmentSelectionService::class)
                            ->addQuestionSelection($assignment, $question);
                    }),
            ])
            ->recordActions([
                Action::make('removeSelection')
                    ->label('Quitar')
                    ->icon('heroicon-o-trash')
                    ->color('danger')
                    ->modalHeading('Quitar unidad seleccionada')
                    ->successNotificationTitle('Selección actualizada.')
                    ->requiresConfirmation()
                    ->action(function (AssessmentAssignmentQuestion $record): void {
                        /** @var AssessmentAssignment $assignment */
                        $assignment = $this->getOwnerRecord();
                        $question = $record->question;

                        if (! $question instanceof AssessmentQuestion) {
                            $record->delete();

                            return;
                        }

                        app(AssessmentAssignmentSelectionService::class)
                            ->removeQuestionSelection($assignment, $question, $record->selection_group_key);
                    }),
            ])
            ->emptyStateHeading('Se usará la plantilla completa si no seleccionas preguntas.')
            ->emptyStateDescription('Añade preguntas solo cuando quieras un subconjunto propio. Si una pregunta comparte contexto con otras, la asignación añadirá ese bloque completo y lo mantendrá unido.');
    }
}
