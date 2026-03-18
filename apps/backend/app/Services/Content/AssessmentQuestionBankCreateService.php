<?php

namespace App\Services\Content;

use App\Models\AssessmentContext;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentTemplate;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;
use Illuminate\Validation\ValidationException;

class AssessmentQuestionBankCreateService
{
    public function __construct(
        private readonly MarkdownCanonicalContentCompiler $compiler,
        private readonly AssessmentEditorialContentUpdateService $editorialUpdateService,
        private readonly AssessmentQuestionFingerprintService $fingerprintService,
    ) {}

    /**
     * @param  array<string, mixed>  $data
     */
    public function create(array $data): AssessmentQuestion
    {
        $this->guardAgainstExactDuplicate($data);

        return DB::transaction(function () use ($data): AssessmentQuestion {
            $template = AssessmentTemplate::query()->create([
                'external_id' => 'manual-bank-'.now()->format('Ymd-His').'-'.Str::lower(Str::random(6)),
                'title' => $this->resolveBlockTitle($data),
                'subject_id' => (int) $data['subject_id'],
                'unit_id' => null,
                'origin_collection_id' => (int) $data['origin_collection_id'],
                'editorial_status' => (string) ($data['editorial_status'] ?? 'draft'),
                'access_tier' => 'private',
                'is_published' => false,
                'total_questions' => 1,
                'total_assets' => 0,
                'assets' => [],
                'asset_refs' => [],
                'metadata' => [
                    'source' => 'manual-question-create',
                    'context_strategy' => 'single-context-single-question',
                ],
                'synced_at' => now(),
            ]);

            $context = $this->createContext($template, $data);

            $question = AssessmentQuestion::query()->create([
                'template_id' => $template->id,
                'external_id' => 'Q1',
                'order_base' => 1,
                'subject_id' => (int) $data['subject_id'],
                'unit_id' => filled($data['unit_id'] ?? null) ? (int) $data['unit_id'] : null,
                'origin_collection_id' => (int) $data['origin_collection_id'],
                'editorial_status' => (string) ($data['editorial_status'] ?? 'draft'),
                'is_active' => true,
                'stem_mdx' => '',
                'stem_html' => '',
                'options' => [],
                'correct_option_id' => null,
                'meta' => [
                    'source' => 'manual-question-create',
                ],
            ]);

            $question = $this->editorialUpdateService->updateQuestion($question, $data);
            $question->contexts()->sync([$context->id => ['order_base' => 1]]);

            return $question->fresh(['template', 'contexts', 'questionOptions']);
        });
    }

    /**
     * @param  array<string, mixed>  $data
     */
    private function createContext(AssessmentTemplate $template, array $data): AssessmentContext
    {
        $markdown = trim((string) ($data['context_mdx'] ?? ''));

        if ($markdown === '') {
            throw ValidationException::withMessages([
                'context_mdx' => 'El contexto base no puede quedar vacío.',
            ]);
        }

        $compiled = $this->compiler->compile($markdown);

        return AssessmentContext::query()->create([
            'template_id' => $template->id,
            'external_id' => 'CTX1',
            'title' => filled($data['context_title'] ?? null) ? trim((string) $data['context_title']) : null,
            'subject_id' => (int) $data['subject_id'],
            'origin_collection_id' => (int) $data['origin_collection_id'],
            'editorial_status' => (string) ($data['editorial_status'] ?? 'draft'),
            'order_base' => 1,
            'is_active' => true,
            'context_mdx' => $compiled['markdown'],
            'context_html' => $compiled['html_web'],
            'context_assets' => $compiled['assets'],
            'context_blocks' => $compiled['blocks'],
            'teacher_notes' => filled($data['teacher_notes'] ?? null) ? trim((string) $data['teacher_notes']) : null,
            'metadata' => [
                'source' => 'manual-question-create',
            ],
        ]);
    }

    /**
     * @param  array<string, mixed>  $data
     */
    private function guardAgainstExactDuplicate(array $data): void
    {
        $fingerprint = $this->fingerprintService->exactFingerprintFromDraftQuestion([
            'stem_mdx' => (string) ($data['stem_mdx'] ?? ''),
            'options' => collect((array) ($data['options_editor'] ?? []))
                ->map(fn (mixed $option): array => [
                    'id' => is_array($option) ? (string) ($option['option_id'] ?? '') : '',
                    'text' => is_array($option) ? (string) ($option['text'] ?? '') : '',
                ])
                ->all(),
            'correct_option_id' => (string) ($data['correct_option_id'] ?? ''),
        ]);

        if ($fingerprint === '') {
            return;
        }

        $existing = AssessmentQuestion::query()
            ->with('template')
            ->where('exact_fingerprint', $fingerprint)
            ->first();

        if (! $existing instanceof AssessmentQuestion) {
            return;
        }

        $blockTitle = $existing->template?->title ?: 'otro bloque del banco';

        throw ValidationException::withMessages([
            'stem_mdx' => sprintf(
                'Esta pregunta ya existe en el banco dentro de "%s". Abre esa versión y reutilízala en lugar de duplicarla.',
                $blockTitle
            ),
        ]);
    }

    /**
     * @param  array<string, mixed>  $data
     */
    private function resolveBlockTitle(array $data): string
    {
        $explicitBlockTitle = trim((string) ($data['block_title'] ?? ''));
        if ($explicitBlockTitle !== '') {
            return $explicitBlockTitle;
        }

        $contextTitle = trim((string) ($data['context_title'] ?? ''));
        if ($contextTitle !== '') {
            return $contextTitle;
        }

        $stem = Str::of((string) ($data['stem_mdx'] ?? ''))
            ->replaceMatches('/[#*_`>\\-]+/u', ' ')
            ->squish()
            ->limit(80, '')
            ->value();

        return $stem !== '' ? 'Bloque · '.$stem : 'Bloque manual · '.now()->format('Y-m-d H:i');
    }
}
