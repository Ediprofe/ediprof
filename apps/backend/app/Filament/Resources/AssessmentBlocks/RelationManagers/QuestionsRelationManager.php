<?php

namespace App\Filament\Resources\AssessmentBlocks\RelationManagers;

use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentSubject;
use App\Models\AssessmentUnit;
use App\Services\Content\AssessmentEditorialContentUpdateService;
use Filament\Actions\Action;
use Filament\Forms\Components\Repeater;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\TextInput;
use Filament\Notifications\Notification;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Components\Utilities\Get;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Illuminate\Support\Str;

class QuestionsRelationManager extends RelationManager
{
    protected static string $relationship = 'questions';

    protected static ?string $title = 'Preguntas que nacen del contexto';

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
                Action::make('quickEditQuestion')
                    ->label('Editar pregunta')
                    ->icon('heroicon-o-pencil-square')
                    ->color('primary')
                    ->slideOver()
                    ->modalWidth('7xl')
                    ->modalHeading('Editar pregunta del bloque')
                    ->modalDescription('Aquí trabajas lo específico: enunciado, opciones, correcta y apoyo pedagógico.')
                    ->modalSubmitActionLabel('Guardar pregunta')
                    ->fillForm(function (AssessmentQuestion $record): array {
                        $options = $record->questionOptions()
                            ->orderBy('order_base')
                            ->get()
                            ->map(fn ($option): array => [
                                'option_id' => (string) $option->option_id,
                                'text' => (string) ($option->plain_text ?? ''),
                            ])
                            ->all();

                        if ($options === []) {
                            $options = collect((array) ($record->options ?? []))
                                ->map(fn ($option): array => [
                                    'option_id' => trim((string) ($option['id'] ?? '')),
                                    'text' => (string) ($option['text'] ?? ''),
                                ])
                                ->filter(fn (array $option): bool => $option['option_id'] !== '' && trim($option['text']) !== '')
                                ->values()
                                ->all();
                        }

                        if ($options === []) {
                            $options = [
                                ['option_id' => 'A', 'text' => ''],
                                ['option_id' => 'B', 'text' => ''],
                                ['option_id' => 'C', 'text' => ''],
                                ['option_id' => 'D', 'text' => ''],
                            ];
                        }

                        return [
                            'stem_mdx' => $record->stem_mdx,
                            'options_editor' => $options,
                            'correct_option_id' => $record->correct_option_id,
                            'feedback_mdx' => $record->feedback_mdx,
                            'concepts_mdx' => $record->concepts_mdx,
                            'subject_id' => $record->subject_id,
                            'unit_id' => $record->unit_id,
                            'origin_collection_id' => $record->origin_collection_id,
                            'editorial_status' => $record->editorial_status,
                            'teacher_notes' => $record->teacher_notes,
                        ];
                    })
                    ->schema([
                        Section::make('Contenido de la pregunta')
                            ->description('Aquí editas lo que verá y responderá el estudiante.')
                            ->components([
                                Textarea::make('stem_mdx')
                                    ->label('Enunciado (Markdown)')
                                    ->rows(8)
                                    ->required()
                                    ->helperText('Corrige aquí la pregunta específica que sale del contexto base.')
                                    ->columnSpanFull(),
                                Repeater::make('options_editor')
                                    ->label('Opciones')
                                    ->addActionLabel('Agregar opción')
                                    ->minItems(2)
                                    ->defaultItems(4)
                                    ->reorderable(false)
                                    ->live()
                                    ->helperText('Edita el contenido de las opciones. La letra es una referencia simple para identificar cada respuesta.')
                                    ->schema([
                                        TextInput::make('option_id')
                                            ->label('Letra')
                                            ->required()
                                            ->maxLength(5)
                                            ->placeholder('A'),
                                        Textarea::make('text')
                                            ->label('Texto de la opción')
                                            ->required()
                                            ->rows(3)
                                            ->columnSpanFull(),
                                    ])
                                    ->columns(2)
                                    ->columnSpanFull(),
                                Select::make('correct_option_id')
                                    ->label('Respuesta correcta')
                                    ->options(fn (Get $get): array => collect((array) $get('options_editor'))
                                        ->mapWithKeys(function ($option): array {
                                            if (! is_array($option)) {
                                                return [];
                                            }

                                            $optionId = trim((string) ($option['option_id'] ?? ''));
                                            if ($optionId === '') {
                                                return [];
                                            }

                                            $text = Str::limit(
                                                Str::of((string) ($option['text'] ?? ''))->squish()->value(),
                                                80
                                            );

                                            return [$optionId => $optionId.($text !== '' ? ' · '.$text : '')];
                                        })
                                    ->all())
                                    ->required()
                                    ->helperText('Marca cuál opción es la correcta después de revisar el contenido.')
                                    ->native(false)
                                    ->searchable(false),
                            ]),
                        Section::make('Apoyo pedagógico de esta pregunta')
                            ->description('Cada pregunta puede necesitar una explicación y profundización distinta, aunque comparta contexto.')
                            ->components([
                                Textarea::make('feedback_mdx')
                                    ->label('Retroalimentación / solución guiada (Markdown)')
                                    ->rows(8)
                                    ->helperText('Explica por qué la respuesta correcta lo es y por qué las demás no.')
                                    ->columnSpanFull(),
                                Textarea::make('concepts_mdx')
                                    ->label('Conceptos relacionados (Markdown)')
                                    ->rows(8)
                                    ->helperText('Añade solo lo necesario para profundizar después de responder.')
                                    ->columnSpanFull(),
                            ]),
                        Section::make('Clasificación editorial de la pregunta')
                            ->description('Aquí sí ubicamos la pregunta dentro del banco. Es la parte específica y reusable del ítem.')
                            ->components([
                                Select::make('subject_id')
                                    ->label('Materia')
                                    ->options(fn (): array => AssessmentSubject::query()->where('is_active', true)->orderBy('label')->pluck('label', 'id')->all())
                                    ->searchable()
                                    ->preload()
                                    ->native(false)
                                    ->nullable()
                                    ->live(),
                                Select::make('unit_id')
                                    ->label('Unidad')
                                    ->options(fn (Get $get): array => AssessmentUnit::query()
                                        ->where('is_active', true)
                                        ->when($get('subject_id'), fn ($query, $subjectId) => $query->where('subject_id', $subjectId))
                                        ->orderBy('label')
                                        ->pluck('label', 'id')
                                        ->all())
                                    ->searchable()
                                    ->preload()
                                    ->native(false)
                                    ->nullable(),
                                Select::make('origin_collection_id')
                                    ->label('Origen')
                                    ->options(fn (): array => AssessmentOriginCollection::query()
                                        ->where('is_active', true)
                                        ->orderBy('label')
                                        ->get()
                                        ->mapWithKeys(fn (AssessmentOriginCollection $collection): array => [
                                            $collection->id => sprintf('%s · %s', ucfirst($collection->origin_type), $collection->label),
                                        ])
                                        ->all())
                                    ->searchable()
                                    ->preload()
                                    ->native(false)
                                    ->nullable(),
                                Select::make('editorial_status')
                                    ->label('Estado editorial')
                                    ->options([
                                        'draft' => 'Borrador',
                                        'ready' => 'Lista para usar',
                                        'review' => 'Revisar',
                                        'archived' => 'Archivada',
                                    ])
                                    ->native(false)
                                    ->nullable(),
                                Textarea::make('teacher_notes')
                                    ->label('Notas docentes')
                                    ->rows(4)
                                    ->helperText('Observaciones internas para revisión o colaboración docente.')
                                    ->columnSpanFull(),
                            ])
                            ->columns(2)
                            ->collapsible()
                            ->collapsed(),
                    ])
                    ->action(function (AssessmentQuestion $record, array $data): void {
                        app(AssessmentEditorialContentUpdateService::class)->updateQuestion($record, $data);

                        Notification::make()
                            ->title('Pregunta actualizada')
                            ->body('Los cambios de contenido quedaron guardados sin salir del bloque.')
                            ->success()
                            ->send();
                    }),
            ])
            ->emptyStateHeading('Este bloque todavía no tiene preguntas.');
    }
}
