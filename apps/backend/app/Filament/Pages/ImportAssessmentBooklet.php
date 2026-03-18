<?php

namespace App\Filament\Pages;

use App\Filament\Resources\AssessmentBooklets\AssessmentBookletResource;
use App\Filament\Resources\AssessmentOriginCollections\AssessmentOriginCollectionResource;
use App\Filament\Resources\AssessmentSubjects\AssessmentSubjectResource;
use App\Filament\Resources\AssessmentUnits\AssessmentUnitResource;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentSubject;
use App\Models\AssessmentUnit;
use App\Services\Content\AiQuestionDraftParser;
use App\Services\Content\AssessmentBookletImportService;
use Filament\Forms\Components\Repeater;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Toggle;
use Filament\Forms\Concerns\InteractsWithForms;
use Filament\Forms\Contracts\HasForms;
use Filament\Notifications\Notification;
use Filament\Pages\Page;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Components\Utilities\Get;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;

class ImportAssessmentBooklet extends Page implements HasForms
{
    use InteractsWithForms;

    protected string $view = 'filament.pages.import-assessment-booklet';

    protected static bool $shouldRegisterNavigation = false;

    protected static ?string $slug = 'assessment-booklets/import';

    protected static ?string $title = 'Traer preguntas desde cuadernillo';

    protected static string|\BackedEnum|null $navigationIcon = Heroicon::OutlinedDocumentDuplicate;

    public ?array $data = [];

    /**
     * @var array<string,mixed>|null
     */
    public ?array $preview = null;

    public ?string $parserError = null;

    public function getSubheading(): ?string
    {
        return 'Usa esta ruta cuando el material viene como simulacro o taller completo y quieres convertirlo en preguntas reutilizables dentro del banco.';
    }

    public function mount(): void
    {
        $this->form->fill([
            'title' => '',
            'booklet_type' => 'simulacro',
            'origin_collection_id' => null,
            'applied_on' => null,
            'school_year' => (string) now()->year,
            'is_active' => true,
            'notes' => '',
            'sections' => [
                [
                    'title' => '',
                    'subject_id' => null,
                    'default_unit_id' => null,
                    'draft_markdown' => '',
                ],
            ],
        ]);
    }

    public function form(Schema $schema): Schema
    {
        return $schema
            ->components([
                Section::make('Paso 1. Datos base del cuadernillo')
                    ->description('Aquí defines una sola vez el origen global del simulacro o taller. Luego cada bloque hereda ese origen sin repetirlo pregunta por pregunta.')
                    ->components([
                        TextInput::make('title')
                            ->label('Título del cuadernillo')
                            ->required()
                            ->maxLength(255)
                            ->placeholder('Simulacro 2 · Saber 11'),
                        Select::make('booklet_type')
                            ->label('Tipo')
                            ->options([
                                'simulacro' => 'Simulacro',
                                'taller' => 'Taller',
                                'cuadernillo' => 'Cuadernillo',
                            ])
                            ->required()
                            ->default('simulacro')
                            ->native(false),
                        Select::make('origin_collection_id')
                            ->label('Origen global')
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
                            ->required()
                            ->native(false),
                        TextInput::make('applied_on')
                            ->label('Fecha de aplicación')
                            ->type('date'),
                        TextInput::make('school_year')
                            ->label('Año escolar')
                            ->maxLength(20)
                            ->default((string) now()->year),
                        Toggle::make('is_active')
                            ->label('Activo')
                            ->default(true),
                        Textarea::make('notes')
                            ->label('Notas')
                            ->rows(3)
                            ->columnSpanFull(),
                    ])
                    ->columns(3),
                Section::make('Paso 2. Bloques del cuadernillo')
                    ->description('Cada bloque hereda el origen global. Aquí defines la materia y pegas un bloque contextual completo. La unidad queda opcional.')
                    ->components([
                        Repeater::make('sections')
                            ->label('Bloques editoriales del cuadernillo')
                            ->defaultItems(1)
                            ->minItems(1)
                            ->schema([
                                TextInput::make('title')
                                    ->label('Nombre visible del bloque')
                                    ->placeholder('Matemáticas · bloque 1')
                                    ->maxLength(255),
                                Select::make('subject_id')
                                    ->label('Materia')
                                    ->options(fn (): array => AssessmentSubject::query()
                                        ->where('is_active', true)
                                        ->orderBy('label')
                                        ->pluck('label', 'id')
                                        ->all())
                                    ->searchable()
                                    ->preload()
                                    ->native(false)
                                    ->required()
                                    ->live()
                                    ->afterStateUpdated(function ($state, callable $set, Get $get): void {
                                        $currentUnitId = $get('default_unit_id');

                                        if (! filled($currentUnitId) || ! filled($state)) {
                                            $set('default_unit_id', null);

                                            return;
                                        }

                                        $unitStillMatches = AssessmentUnit::query()
                                            ->whereKey((int) $currentUnitId)
                                            ->where('subject_id', (int) $state)
                                            ->exists();

                                        if (! $unitStillMatches) {
                                            $set('default_unit_id', null);
                                        }
                                    }),
                                Select::make('default_unit_id')
                                    ->label('Unidad por defecto')
                                    ->options(fn (Get $get): array => AssessmentUnit::query()
                                        ->where('is_active', true)
                                        ->when($get('subject_id'), fn ($query, $subjectId) => $query->where('subject_id', $subjectId))
                                        ->orderBy('label')
                                        ->pluck('label', 'id')
                                        ->all())
                                    ->searchable()
                                    ->preload()
                                    ->native(false)
                                    ->helperText('Opcional. Sirve si este bloque pertenece casi por completo a una sola unidad.')
                                    ->disabled(fn (Get $get): bool => blank($get('subject_id'))),
                                Textarea::make('draft_markdown')
                                    ->label('Borrador del bloque contextual')
                                    ->required()
                                    ->rows(16)
                                    ->columnSpanFull()
                                    ->placeholder(<<<'TEXT'
## Pregunta 1
¿Cuál afirmación es correcta?

### Opciones
A. ...
B. ...
C. ...
D. ...

### Correcta
B
TEXT),
                            ])
                            ->columns(3)
                            ->columnSpanFull(),
                    ]),
            ])
            ->statePath('data');
    }

    public function convertDraft(AiQuestionDraftParser $parser): void
    {
        $state = $this->form->getState();
        $sections = collect((array) ($state['sections'] ?? []));

        if ($sections->isEmpty()) {
            $this->preview = null;
            $this->parserError = 'Agrega al menos una sección antes de convertir el cuadernillo.';

            return;
        }

        try {
            $parsedSections = $sections->values()->map(function (array $section, int $index) use ($parser): array {
                $draft = trim((string) ($section['draft_markdown'] ?? ''));

                if ($draft === '') {
                    throw new \RuntimeException('La sección '.($index + 1).' no tiene contenido para convertir.');
                }

                if (! filled($section['subject_id'] ?? null)) {
                    throw new \RuntimeException('La sección '.($index + 1).' necesita una materia antes de convertir.');
                }

                $subject = AssessmentSubject::query()->find((int) $section['subject_id']);
                $defaultUnit = filled($section['default_unit_id'] ?? null)
                    ? AssessmentUnit::query()->find((int) $section['default_unit_id'])
                    : null;

                $parsed = $parser->parse($draft);

                return [
                    'title' => filled($section['title'] ?? null) ? trim((string) $section['title']) : null,
                    'subject_id' => (int) $section['subject_id'],
                    'subject_label' => $subject?->label,
                    'default_unit_id' => filled($section['default_unit_id'] ?? null) ? (int) $section['default_unit_id'] : null,
                    'default_unit_label' => $defaultUnit?->label,
                    'parsed_draft' => $parsed,
                    'summary' => [
                        'contexts' => count($parsed['contexts'] ?? []),
                        'questions' => count($parsed['questions'] ?? []),
                        'links' => count($parsed['question_context_links'] ?? []),
                    ],
                ];
            })->all();

            $this->preview = [
                'booklet' => [
                    'title' => $state['title'] ?? null,
                    'booklet_type' => $state['booklet_type'] ?? 'simulacro',
                    'origin_label' => filled($state['origin_collection_id'] ?? null)
                        ? AssessmentOriginCollection::query()->find((int) $state['origin_collection_id'])?->label
                        : null,
                ],
                'sections' => $parsedSections,
                'summary' => [
                    'sections' => count($parsedSections),
                    'contexts' => collect($parsedSections)->sum(fn (array $section): int => (int) data_get($section, 'summary.contexts', 0)),
                    'questions' => collect($parsedSections)->sum(fn (array $section): int => (int) data_get($section, 'summary.questions', 0)),
                    'links' => collect($parsedSections)->sum(fn (array $section): int => (int) data_get($section, 'summary.links', 0)),
                ],
            ];
            $this->parserError = null;

            Notification::make()
                ->title('Cuadernillo convertido')
                ->body(sprintf(
                    'Se detectaron %d sección(es) y %d pregunta(s).',
                    (int) data_get($this->preview, 'summary.sections', 0),
                    (int) data_get($this->preview, 'summary.questions', 0),
                ))
                ->success()
                ->send();
        } catch (\Throwable $exception) {
            $this->preview = null;
            $this->parserError = $exception->getMessage();

            Notification::make()
                ->title('No se pudo convertir el cuadernillo')
                ->body($exception->getMessage())
                ->danger()
                ->send();
        }
    }

    public function saveBookletAndOpenEdit(AssessmentBookletImportService $importService)
    {
        $booklet = $this->persistBooklet($importService);

        if (! $booklet) {
            return null;
        }

        return $this->redirect(
            AssessmentBookletResource::getUrl('edit', ['record' => $booklet], panel: 'admin'),
            navigate: true,
        );
    }

    public function previewSummary(): ?array
    {
        return is_array($this->preview) ? ($this->preview['summary'] ?? null) : null;
    }

    public function reviewNotes(): array
    {
        if (! is_array($this->preview)) {
            return [];
        }

        $notes = [];
        $questions = (int) data_get($this->preview, 'summary.questions', 0);
        $contexts = (int) data_get($this->preview, 'summary.contexts', 0);
        $sections = (int) data_get($this->preview, 'summary.sections', 0);

        if ($sections > 0) {
            $notes[] = "Laravel entendió {$sections} bloque(s) de materia y los dejó listos para guardarse como un solo cuadernillo.";
        }

        if ($questions > 0) {
            $notes[] = "En total se detectaron {$questions} pregunta(s). Eso ya permite reutilizarlas luego como banco canónico.";
        }

        if ($contexts > 0) {
            $notes[] = "También se detectaron {$contexts} contexto(s), así que el importador conservará el material compartido sin duplicarlo.";
        }

        $notes[] = 'Recuerda: la unidad es opcional aquí. Lo fino se puede clasificar después desde el banco.';

        return $notes;
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

    private function persistBooklet(AssessmentBookletImportService $importService): ?\App\Models\AssessmentBooklet
    {
        if (! is_array($this->preview)) {
            Notification::make()
                ->title('Convierte el cuadernillo primero')
                ->body('Primero necesitamos confirmar que Laravel entendió bien los bloques por materia.')
                ->warning()
                ->send();

            return null;
        }

        $state = $this->form->getState();

        if (! filled($state['title'] ?? null) || ! filled($state['origin_collection_id'] ?? null)) {
            Notification::make()
                ->title('Faltan datos base')
                ->body('Completa el título y el origen global antes de guardar.')
                ->warning()
                ->send();

            return null;
        }

        return $importService->import(
            [
                'title' => trim((string) $state['title']),
                'booklet_type' => $state['booklet_type'] ?? 'simulacro',
                'origin_collection_id' => (int) $state['origin_collection_id'],
                'applied_on' => filled($state['applied_on'] ?? null) ? (string) $state['applied_on'] : null,
                'school_year' => filled($state['school_year'] ?? null) ? (string) $state['school_year'] : null,
                'notes' => filled($state['notes'] ?? null) ? (string) $state['notes'] : null,
                'is_active' => (bool) ($state['is_active'] ?? true),
                'editorial_status' => 'draft',
            ],
            collect((array) ($this->preview['sections'] ?? []))
                ->map(fn (array $section): array => [
                    'title' => $section['title'] ?? null,
                    'subject_id' => (int) $section['subject_id'],
                    'default_unit_id' => $section['default_unit_id'] ?? null,
                    'parsed_draft' => $section['parsed_draft'],
                    'metadata' => [
                        'source' => 'filament-booklet-import-preview',
                    ],
                ])
                ->all(),
            auth()->user(),
        );
    }
}
