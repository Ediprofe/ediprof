<?php

namespace App\Services\Content;

use App\Models\AssessmentContext;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentQuestionOption;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;
use Illuminate\Validation\ValidationException;

class AssessmentEditorialContentUpdateService
{
    public function __construct(
        private readonly MarkdownCanonicalContentCompiler $compiler,
    ) {}

    /**
     * @param  array<string,mixed>  $data
     */
    public function updateContext(AssessmentContext $context, array $data): AssessmentContext
    {
        $markdown = trim((string) ($data['context_mdx'] ?? ''));

        if ($markdown === '') {
            throw ValidationException::withMessages([
                'context_mdx' => 'El contexto no puede quedar vacío.',
            ]);
        }

        $compiled = $this->compiler->compile($markdown);

        $context->fill([
            'title' => filled($data['title'] ?? null) ? trim((string) $data['title']) : null,
            'subject_id' => filled($data['subject_id'] ?? null) ? (int) $data['subject_id'] : null,
            'unit_id' => filled($data['unit_id'] ?? null) ? (int) $data['unit_id'] : null,
            'origin_collection_id' => filled($data['origin_collection_id'] ?? null) ? (int) $data['origin_collection_id'] : null,
            'editorial_status' => filled($data['editorial_status'] ?? null) ? (string) $data['editorial_status'] : null,
            'tags' => $this->normalizeTags($data['tags'] ?? []),
            'teacher_notes' => filled($data['teacher_notes'] ?? null) ? trim((string) $data['teacher_notes']) : null,
            'context_mdx' => $compiled['markdown'],
            'context_html' => $compiled['html_web'],
            'context_assets' => $compiled['assets'],
            'context_blocks' => $compiled['blocks'],
        ]);

        $context->save();

        return $context->fresh();
    }

    /**
     * @param  array<string,mixed>  $data
     */
    public function updateQuestion(AssessmentQuestion $question, array $data): AssessmentQuestion
    {
        $stemMarkdown = trim((string) ($data['stem_mdx'] ?? ''));
        $optionsDraft = is_array($data['options_editor'] ?? null) ? $data['options_editor'] : [];
        $correctOptionId = trim((string) ($data['correct_option_id'] ?? ''));

        if ($stemMarkdown === '') {
            throw ValidationException::withMessages([
                'stem_mdx' => 'El enunciado no puede quedar vacío.',
            ]);
        }

        $compiledOptions = $this->compileOptions($optionsDraft, $correctOptionId);
        $stem = $this->compiler->compile($stemMarkdown);
        $feedback = $this->compiler->compile((string) ($data['feedback_mdx'] ?? ''));
        $concepts = $this->compiler->compile((string) ($data['concepts_mdx'] ?? ''));

        return DB::transaction(function () use ($question, $data, $compiledOptions, $correctOptionId, $stem, $feedback, $concepts): AssessmentQuestion {
            $question->fill([
                'subject_id' => filled($data['subject_id'] ?? null) ? (int) $data['subject_id'] : null,
                'unit_id' => filled($data['unit_id'] ?? null) ? (int) $data['unit_id'] : null,
                'origin_collection_id' => filled($data['origin_collection_id'] ?? null) ? (int) $data['origin_collection_id'] : null,
                'editorial_status' => filled($data['editorial_status'] ?? null) ? (string) $data['editorial_status'] : null,
                'tags' => $this->normalizeTags($data['tags'] ?? []),
                'teacher_notes' => filled($data['teacher_notes'] ?? null) ? trim((string) $data['teacher_notes']) : null,
                'stem_mdx' => $stem['markdown'],
                'stem_html' => $stem['html_web'],
                'stem_assets' => $stem['assets'],
                'stem_blocks' => $stem['blocks'],
                'options' => array_map(static fn (array $option): array => [
                    'id' => $option['option_id'],
                    'text' => $option['plain_text'],
                    'text_html' => $option['html_web'],
                    'text_assets' => collect($option['asset_refs'])->pluck('src')->filter()->values()->all(),
                    'nodes_mobile' => $option['nodes_mobile'],
                    'is_correct' => $option['is_correct'],
                ], $compiledOptions),
                'correct_option_id' => $correctOptionId,
                'feedback_mdx' => $feedback['markdown'],
                'feedback_html' => $feedback['html_web'],
                'feedback_summary' => $feedback['plain_text'] !== '' ? Str::limit($feedback['plain_text'], 180) : null,
                'feedback_assets' => $feedback['assets'],
                'feedback_blocks' => $feedback['blocks'],
                'concepts_mdx' => $concepts['markdown'],
                'concepts_html' => $concepts['html_web'],
                'concepts_summary' => $concepts['plain_text'] !== '' ? Str::limit($concepts['plain_text'], 180) : null,
                'concepts_assets' => $concepts['assets'],
                'concepts_blocks' => $concepts['blocks'],
                'app_payload_version' => 2,
            ]);

            $question->save();

            $question->questionOptions()->delete();

            foreach ($compiledOptions as $option) {
                AssessmentQuestionOption::query()->create([
                    'question_id' => $question->id,
                    'option_id' => $option['option_id'],
                    'order_base' => $option['order_base'],
                    'is_correct' => $option['is_correct'],
                    'plain_text' => $option['plain_text'],
                    'html_web' => $option['html_web'],
                    'nodes_mobile' => $option['nodes_mobile'],
                    'asset_refs' => $option['asset_refs'],
                    'metadata' => ['source' => 'editorial-edit'],
                ]);
            }

            return $question->fresh(['questionOptions', 'contexts']);
        });
    }

    /**
     * @param  array<int,mixed>  $tags
     * @return array<int,string>
     */
    private function normalizeTags(array $tags): array
    {
        return array_values(array_unique(array_filter(array_map(
            static fn ($tag): string => trim((string) $tag),
            $tags
        ))));
    }

    /**
     * @param  array<int,mixed>  $optionsDraft
     * @return array<int,array<string,mixed>>
     */
    private function compileOptions(array $optionsDraft, string $correctOptionId): array
    {
        $rows = [];
        $ids = [];

        foreach (array_values($optionsDraft) as $index => $option) {
            if (! is_array($option)) {
                continue;
            }

            $optionId = Str::upper(trim((string) ($option['option_id'] ?? '')));
            $optionText = trim((string) ($option['text'] ?? ''));

            if ($optionId === '') {
                throw ValidationException::withMessages([
                    'options_editor' => 'Cada opción debe tener un identificador como A, B, C o D.',
                ]);
            }

            if ($optionText === '') {
                throw ValidationException::withMessages([
                    'options_editor' => 'Cada opción debe tener contenido.',
                ]);
            }

            if (in_array($optionId, $ids, true)) {
                throw ValidationException::withMessages([
                    'options_editor' => 'No puede haber dos opciones con la misma letra.',
                ]);
            }

            $ids[] = $optionId;

            $compiled = $this->compiler->compile($optionText);

            $rows[] = [
                'option_id' => $optionId,
                'order_base' => $index + 1,
                'is_correct' => $optionId === $correctOptionId,
                'plain_text' => $compiled['plain_text'],
                'html_web' => $compiled['html_web'],
                'nodes_mobile' => $compiled['plain_text'] !== ''
                    ? [[
                        'type' => 'paragraph',
                        'inlines' => [[
                            'text' => $compiled['plain_text'],
                            'variant' => 'plain',
                        ]],
                    ]]
                    : [],
                'asset_refs' => $compiled['asset_refs'],
            ];
        }

        if (count($rows) < 2) {
            throw ValidationException::withMessages([
                'options_editor' => 'La pregunta necesita al menos dos opciones.',
            ]);
        }

        if ($correctOptionId === '' || ! in_array($correctOptionId, $ids, true)) {
            throw ValidationException::withMessages([
                'correct_option_id' => 'Selecciona una respuesta correcta válida.',
            ]);
        }

        return $rows;
    }
}
