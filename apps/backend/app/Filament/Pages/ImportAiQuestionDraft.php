<?php

namespace App\Filament\Pages;

use App\Filament\Resources\AssessmentOriginCollections\AssessmentOriginCollectionResource;
use App\Filament\Resources\AssessmentSubjects\AssessmentSubjectResource;
use App\Filament\Resources\AssessmentUnits\AssessmentUnitResource;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentSubject;
use App\Models\AssessmentUnit;
use App\Services\Content\AiQuestionDraftImportService;
use App\Services\Content\AiQuestionDraftParser;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\Select;
use Filament\Forms\Concerns\InteractsWithForms;
use Filament\Forms\Contracts\HasForms;
use Filament\Notifications\Notification;
use Filament\Pages\Page;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Components\Utilities\Get;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;

class ImportAiQuestionDraft extends Page implements HasForms
{
    use InteractsWithForms;

    protected string $view = 'filament.pages.import-ai-question-draft';

    protected static ?string $navigationLabel = 'Importar bloque con IA';

    protected static string|\UnitEnum|null $navigationGroup = 'Banco académico';

    protected static ?int $navigationSort = 10;

    protected static string|\BackedEnum|null $navigationIcon = Heroicon::OutlinedSparkles;

    protected static ?string $title = 'Importar bloque contextual';

    public ?array $data = [];

    /**
     * @var array<string, mixed>|null
     */
    public ?array $preview = null;

    public ?string $parserError = null;

    public ?string $savedPreviewUrl = null;

    public function mount(): void
    {
        $this->form->fill([
            'draft_title' => '',
            'subject_id' => null,
            'unit_id' => null,
            'origin_collection_id' => null,
            'draft_markdown' => '',
        ]);
    }

    public function form(Schema $schema): Schema
    {
        return $schema
            ->components([
                Section::make('Paso 1. Pega un bloque contextual')
                    ->description('Aquí trabajamos como en Saber 11: contexto + una o varias preguntas. Laravel debe reconocer el bloque completo, no preguntas aisladas.')
                    ->components([
                        TextInput::make('draft_title')
                            ->label('Nombre corto del borrador')
                            ->helperText('Opcional. Si lo dejas vacío, Laravel armará un nombre útil con lo que detecte del borrador y su organización.')
                            ->maxLength(255),
                        Textarea::make('draft_markdown')
                            ->label('Bloque pegado desde ChatGPT o Gemini')
                            ->rows(24)
                            ->required()
                            ->placeholder(<<<'TEXT'
## Contexto compartido: Separación de mezclas
Una muestra M1, M2 y M3 se analiza en laboratorio.

## Pregunta 95
¿Cuál inferencia es válida?

### Opciones
A. La muestra M1 y M2 tienen igual composición.
B. La muestra M3 tiene más componentes que M1 y M2.
C. La muestra M2 es la de mayor complejidad.
D. No se puede concluir nada.

### Correcta
B

### Retroalimentación
Explica por qué la opción B es válida.

### Conceptos relacionados
- Separación de mezclas
- Cromatografía
TEXT),
                    ]),
                Section::make('Paso 2. Ubícalo en el banco')
                    ->description('Clasificamos el bloque por materia y origen. La unidad queda diferida para no frenar la captura inicial.')
                    ->components([
                        Select::make('subject_id')
                            ->label('Materia')
                            ->options(fn (): array => AssessmentSubject::query()->where('is_active', true)->orderBy('label')->pluck('label', 'id')->all())
                            ->searchable()
                            ->preload()
                            ->native(false)
                            ->live()
                            ->helperText('Obligatoria. Todo bloque debe quedar ubicado por materia desde el inicio.'),
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
                            ->helperText('Opcional en esta etapa. Puedes asignarla después con clasificación masiva.')
                            ->disabled(fn (Get $get): bool => blank($get('subject_id')))
                            ->live(),
                        Select::make('origin_collection_id')
                            ->label('Origen')
                            ->options(fn (): array => AssessmentOriginCollection::query()
                                ->where('is_active', true)
                                ->orderBy('label')
                                ->get()
                                ->mapWithKeys(fn (AssessmentOriginCollection $collection): array => [
                                    $collection->id => sprintf(
                                        '%s · %s',
                                        ucfirst($collection->origin_type),
                                        $collection->label
                                    ),
                                ])
                                ->all())
                            ->searchable()
                            ->preload()
                            ->native(false)
                            ->helperText('Obligatorio. El origen es trazabilidad editorial, no un simple texto decorativo.'),
                    ])
                    ->columns(2),
            ])
            ->statePath('data');
    }

    public function convertDraft(AiQuestionDraftParser $parser): void
    {
        $state = $this->form->getState();
        $draft = trim((string) ($state['draft_markdown'] ?? ''));

        try {
            $this->preview = $parser->parse($draft);
            $this->preview['organization'] = $this->selectedOrganizationPreview($state);
            $this->parserError = null;
            $this->savedPreviewUrl = null;

            Notification::make()
                ->title('Borrador convertido')
                ->body(sprintf(
                    'Se detectaron %d contexto(s), %d pregunta(s) y %d enlace(s) de contexto.',
                    count($this->preview['contexts'] ?? []),
                    count($this->preview['questions'] ?? []),
                    count($this->preview['question_context_links'] ?? [])
                ))
                ->success()
                ->send();

        } catch (\Throwable $exception) {
            $this->preview = null;
            $this->parserError = $exception->getMessage();

            Notification::make()
                ->title('No se pudo convertir el borrador')
                ->body($exception->getMessage())
                ->danger()
                ->send();

        }
    }

    /**
     * @return array<string, mixed>|null
     */
    public function previewSummary(): ?array
    {
        if (! is_array($this->preview)) {
            return null;
        }

        return [
            'contexts' => count($this->preview['contexts'] ?? []),
            'questions' => count($this->preview['questions'] ?? []),
            'links' => count($this->preview['question_context_links'] ?? []),
        ];
    }

    /**
     * @return array<int, array{label:string, value:int}>
     */
    public function detectedSignals(): array
    {
        if (! is_array($this->preview)) {
            return [];
        }

        $questions = (array) ($this->preview['questions'] ?? []);
        $feedbackCount = 0;
        $conceptsCount = 0;
        $formulaCount = 0;

        foreach ($questions as $question) {
            if (! is_array($question)) {
                continue;
            }

            if (filled($question['feedback_mdx'] ?? null)) {
                $feedbackCount++;
            }

            if (filled($question['concepts_mdx'] ?? null)) {
                $conceptsCount++;
            }

            $formulaCount += $this->countMathDelimiters((string) ($question['stem_mdx'] ?? ''));
            $formulaCount += $this->countMathDelimiters((string) ($question['feedback_mdx'] ?? ''));
            $formulaCount += $this->countMathDelimiters((string) ($question['concepts_mdx'] ?? ''));

            foreach ((array) ($question['options'] ?? []) as $option) {
                if (is_array($option)) {
                    $formulaCount += $this->countMathDelimiters((string) ($option['text'] ?? ''));
                }
            }
        }

        return [
            ['label' => 'Contextos compartidos detectados', 'value' => count($this->preview['contexts'] ?? [])],
            ['label' => 'Preguntas detectadas', 'value' => count($questions)],
            ['label' => 'Enlaces contexto/pregunta', 'value' => count($this->preview['question_context_links'] ?? [])],
            ['label' => 'Preguntas con retroalimentación', 'value' => $feedbackCount],
            ['label' => 'Preguntas con conceptos', 'value' => $conceptsCount],
            ['label' => 'Fórmulas detectadas', 'value' => $formulaCount],
        ];
    }

    public function saveDraftAndOpenPreview(AiQuestionDraftImportService $importer)
    {
        $template = $this->persistDraft($importer);

        if (! $template || ! filled($this->savedPreviewUrl)) {
            return;
        }

        return $this->redirect($this->savedPreviewUrl, navigate: true);
    }

    private function countMathDelimiters(string $markdown): int
    {
        if ($markdown === '') {
            return 0;
        }

        $blockMatches = preg_match_all('/(?<!\\\\)\$\$(.+?)(?<!\\\\)\$\$/s', $markdown);
        $inlineMatches = preg_match_all('/(?<!\\\\)\$([^\n$]+?)(?<!\\\\)\$(?!\$)/', $markdown);

        return max((int) $blockMatches, 0) + max((int) $inlineMatches, 0);
    }

    /**
     * @param  array<string, mixed>  $state
     * @return array{subject_label:?string,unit_label:?string,origin_type:?string,origin_label:?string}
     */
    private function selectedOrganizationPreview(array $state): array
    {
        $subject = filled($state['subject_id'] ?? null)
            ? AssessmentSubject::query()->find((int) $state['subject_id'])
            : null;
        $unit = filled($state['unit_id'] ?? null)
            ? AssessmentUnit::query()->find((int) $state['unit_id'])
            : null;
        $origin = filled($state['origin_collection_id'] ?? null)
            ? AssessmentOriginCollection::query()->find((int) $state['origin_collection_id'])
            : null;

        return [
            'subject_label' => $subject?->label,
            'unit_label' => $unit?->label,
            'origin_type' => $origin?->origin_type,
            'origin_label' => $origin?->label,
        ];
    }

    /**
     * @return array<int, string>
     */
    public function reviewNotes(): array
    {
        if (! is_array($this->preview)) {
            return [];
        }

        $notes = [];
        $contexts = count($this->preview['contexts'] ?? []);
        $questions = count($this->preview['questions'] ?? []);
        $links = count($this->preview['question_context_links'] ?? []);
        $signals = collect($this->detectedSignals())->keyBy('label');

        if ($questions > 0) {
            $notes[] = sprintf('Laravel entendió %d pregunta(s) dentro del bloque. Ya podemos pasar a guardar y revisar la vista real.', $questions);
        }

        if ($contexts > 0) {
            $notes[] = sprintf('Se detectó %d contexto(s). Eso deja el bloque listo para reutilizarse sin duplicarlo.', $contexts);
        }

        if ($contexts > 0 && $links === 0) {
            $notes[] = 'Hay contexto, pero no quedó enlazado a ninguna pregunta. Aquí sí conviene revisar el formato del bloque.';
        }

        $formulaCount = (int) ($signals->get('Fórmulas detectadas')['value'] ?? 0);
        if ($formulaCount > 0) {
            $notes[] = sprintf('Se detectaron %d fórmula(s). El siguiente chequeo importante es abrir la vista web real.', $formulaCount);
        }

        return $notes;
    }

    /**
     * @return array<int, array{id:string, order:int, correct:string, options:int, contexts:array<int, string>}>
     */
    public function questionReviewRows(): array
    {
        if (! is_array($this->preview)) {
            return [];
        }

        $links = collect($this->preview['question_context_links'] ?? []);

        return collect($this->preview['questions'] ?? [])
            ->filter(fn ($question) => is_array($question))
            ->map(function (array $question) use ($links): array {
                return [
                    'id' => (string) ($question['id'] ?? 'sin-id'),
                    'order' => (int) ($question['order'] ?? $question['order_base'] ?? 0),
                    'correct' => (string) ($question['correct_option_id'] ?? 'sin definir'),
                    'options' => count($question['options'] ?? []),
                    'contexts' => $links
                        ->where('question_external_id', $question['id'] ?? null)
                        ->pluck('context_external_id')
                        ->filter()
                        ->values()
                        ->all(),
                ];
            })
            ->values()
            ->all();
    }

    private function persistDraft(AiQuestionDraftImportService $importer): ?\App\Models\AssessmentTemplate
    {
        if (! is_array($this->preview)) {
            Notification::make()
                ->title('Convierte el borrador primero')
                ->body('Primero necesitamos confirmar que Laravel entendió bien la estructura.')
                ->warning()
                ->send();

            return null;
        }

        $state = $this->form->getState();
        $organization = [
            'subject_id' => (int) ($state['subject_id'] ?? 0),
            'unit_id' => filled($state['unit_id'] ?? null) ? (int) $state['unit_id'] : null,
            'origin_collection_id' => (int) ($state['origin_collection_id'] ?? 0),
        ];

        foreach ([
            'subject_id' => 'la materia',
            'origin_collection_id' => 'el origen',
        ] as $field => $label) {
            if (($organization[$field] ?? 0) < 1) {
                Notification::make()
                    ->title('Falta organización mínima del banco')
                    ->body("Antes de guardar, completa {$label}.")
                    ->warning()
                    ->send();

                return null;
            }
        }

        $title = trim((string) ($state['draft_title'] ?? ''));
        $user = auth()->user();
        $template = $importer->import(
            $this->preview,
            $organization,
            $title !== '' ? $title : null,
            $user,
        );

        $this->savedPreviewUrl = route('admin.assessment_drafts.preview_web', $template);

        return $template;
    }

    public function subjectAdminUrl(): string
    {
        return AssessmentSubjectResource::getUrl(panel: 'admin');
    }

    public function unitAdminUrl(): string
    {
        return AssessmentUnitResource::getUrl(panel: 'admin');
    }

    public function originAdminUrl(): string
    {
        return AssessmentOriginCollectionResource::getUrl(panel: 'admin');
    }
}
