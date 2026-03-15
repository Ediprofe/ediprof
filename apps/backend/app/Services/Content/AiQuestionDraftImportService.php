<?php

namespace App\Services\Content;

use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentSubject;
use App\Models\AssessmentUnit;
use App\Models\AssessmentContext;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentQuestionOption;
use App\Models\AssessmentTemplate;
use App\Models\ContentAsset;
use App\Models\User;
use Illuminate\Support\Arr;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

class AiQuestionDraftImportService
{
    public function __construct(
        private readonly MarkdownCanonicalContentCompiler $compiler,
    ) {}

    /**
     * @param  array{
     *   schema:string,
     *   contexts:array<int,array<string,mixed>>,
     *   questions:array<int,array<string,mixed>>,
     *   question_context_links:array<int,array<string,mixed>>
     * }  $draft
     * @param  array{
     *   subject_id:int,
     *   unit_id?:int|null,
     *   origin_collection_id:int
     * }  $organization
     */
    public function import(array $draft, array $organization, ?string $title = null, ?User $actor = null): AssessmentTemplate
    {
        return DB::transaction(function () use ($draft, $organization, $title, $actor): AssessmentTemplate {
            $subject = AssessmentSubject::query()->findOrFail((int) ($organization['subject_id'] ?? 0));
            $unit = filled($organization['unit_id'] ?? null)
                ? AssessmentUnit::query()
                    ->whereKey((int) $organization['unit_id'])
                    ->where('subject_id', $subject->id)
                    ->firstOrFail()
                : null;
            $originCollection = AssessmentOriginCollection::query()
                ->whereKey((int) ($organization['origin_collection_id'] ?? 0))
                ->firstOrFail();

            $subjectLabel = $subject->label;
            $unitLabel = $unit?->label;
            $originType = $originCollection->origin_type;
            $originLabel = $originCollection->label;

            $template = AssessmentTemplate::query()->create([
                'external_id' => 'ai-draft-'.now()->format('Ymd-His').'-'.Str::lower(Str::random(6)),
                'source_workshop_id' => null,
                'title' => $this->resolveTitle($draft, $title),
                'subject_id' => $subject->id,
                'subject_label' => $subjectLabel,
                'source_content_type' => $originType,
                'default_mode' => 'study',
                'route' => null,
                'area_slug' => Str::slug($subjectLabel),
                'unidad_slug' => filled($unitLabel) ? Str::slug($unitLabel) : null,
                'unit_id' => $unit?->id,
                'unit_label' => $unitLabel,
                'origin_collection_id' => $originCollection->id,
                'origin_label' => $originLabel,
                'editorial_status' => 'draft',
                'access_tier' => 'private',
                'is_published' => false,
                'total_questions' => count($draft['questions'] ?? []),
                'total_assets' => 0,
                'assets' => [],
                'asset_refs' => [],
                'metadata' => [
                    'source' => 'ai-draft',
                    'ingest_method' => 'ai_markdown',
                    'schema' => (string) ($draft['schema'] ?? 'ai_question_draft_v1'),
                    'created_by_user_id' => $actor?->id,
                    'created_by_email' => $actor?->email,
                ],
                'synced_at' => now(),
            ]);

            $contextIdByExternalId = [];
            $questionIdByExternalId = [];
            $allAssetRefs = [];

            foreach ((array) ($draft['contexts'] ?? []) as $contextIndex => $context) {
                if (! is_array($context)) {
                    continue;
                }

                $compiled = $this->compiler->compile((string) ($context['context_mdx'] ?? ''));
                $record = AssessmentContext::query()->create([
                    'template_id' => $template->id,
                    'external_id' => (string) ($context['external_id'] ?? 'shared-context-'.($contextIndex + 1)),
                    'title' => filled($context['title'] ?? null) ? (string) $context['title'] : null,
                    'subject_id' => $subject->id,
                    'subject_label' => $subjectLabel,
                    'order_base' => max((int) ($context['order_base'] ?? ($contextIndex + 1)), 1),
                    'is_active' => true,
                    'unit_id' => $unit?->id,
                    'unit_label' => $unitLabel,
                    'origin_collection_id' => $originCollection->id,
                    'origin_label' => $originLabel,
                    'editorial_status' => 'draft',
                    'context_mdx' => $compiled['markdown'],
                    'context_html' => $compiled['html_web'],
                    'context_assets' => $compiled['assets'],
                    'context_blocks' => $compiled['blocks'],
                    'metadata' => array_merge(
                        is_array($context['metadata'] ?? null) ? $context['metadata'] : [],
                        ['source' => 'ai-draft']
                    ),
                ]);

                $contextIdByExternalId[$record->external_id] = $record->id;
                $allAssetRefs = array_merge($allAssetRefs, $compiled['asset_refs']);
            }

            foreach ((array) ($draft['questions'] ?? []) as $questionIndex => $question) {
                if (! is_array($question)) {
                    continue;
                }

                $stem = $this->compiler->compile((string) ($question['stem_mdx'] ?? ''));
                $feedback = $this->compiler->compile((string) ($question['feedback_mdx'] ?? ''));
                $concepts = $this->compiler->compile((string) ($question['concepts_mdx'] ?? ''));
                $options = $this->compileOptions((array) ($question['options'] ?? []), (string) ($question['correct_option_id'] ?? ''));

                $record = AssessmentQuestion::query()->create([
                    'template_id' => $template->id,
                    'external_id' => (string) ($question['id'] ?? ('Q'.($questionIndex + 1))),
                    'order_base' => max((int) ($question['order_base'] ?? $question['order'] ?? ($questionIndex + 1)), 1),
                    'source_slug' => null,
                    'subject_id' => $subject->id,
                    'subject_label' => $subjectLabel,
                    'is_active' => true,
                    'unit_id' => $unit?->id,
                    'unit_label' => $unitLabel,
                    'origin_collection_id' => $originCollection->id,
                    'origin_label' => $originLabel,
                    'editorial_status' => 'draft',
                    'meta' => array_merge(
                        is_array($question['metadata'] ?? null) ? $question['metadata'] : [],
                        ['source' => 'ai-draft']
                    ),
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
                    ], $options),
                    'correct_option_id' => filled($question['correct_option_id'] ?? null) ? (string) $question['correct_option_id'] : null,
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

                foreach ($options as $optionIndex => $option) {
                    AssessmentQuestionOption::query()->create([
                        'question_id' => $record->id,
                        'option_id' => $option['option_id'],
                        'order_base' => max((int) ($option['order_base'] ?? ($optionIndex + 1)), 1),
                        'is_correct' => (bool) $option['is_correct'],
                        'plain_text' => $option['plain_text'],
                        'html_web' => $option['html_web'],
                        'nodes_mobile' => $option['nodes_mobile'],
                        'asset_refs' => $option['asset_refs'],
                        'metadata' => ['source' => 'ai-draft'],
                    ]);
                }

                $questionIdByExternalId[$record->external_id] = $record->id;
                $allAssetRefs = array_merge($allAssetRefs, $stem['asset_refs'], $feedback['asset_refs'], $concepts['asset_refs']);
                foreach ($options as $option) {
                    $allAssetRefs = array_merge($allAssetRefs, $option['asset_refs']);
                }
            }

            foreach ((array) ($draft['question_context_links'] ?? []) as $linkIndex => $link) {
                if (! is_array($link)) {
                    continue;
                }

                $questionId = $questionIdByExternalId[(string) ($link['question_external_id'] ?? '')] ?? null;
                $contextId = $contextIdByExternalId[(string) ($link['context_external_id'] ?? '')] ?? null;

                if (! $questionId || ! $contextId) {
                    continue;
                }

                DB::table('assessment_question_contexts')->insert([
                    'question_id' => $questionId,
                    'context_id' => $contextId,
                    'order_base' => max((int) ($link['order_base'] ?? ($linkIndex + 1)), 1),
                    'created_at' => now(),
                    'updated_at' => now(),
                ]);
            }

            $assetRefs = $this->uniqueAssetRefs($allAssetRefs);
            foreach ($assetRefs as $assetRef) {
                ContentAsset::query()->updateOrCreate(
                    ['asset_key' => (string) ($assetRef['asset_id'] ?? sha1((string) ($assetRef['src'] ?? '')))],
                    [
                        'source_ref' => (string) ($assetRef['src'] ?? ''),
                        'canonical_url' => (string) ($assetRef['src'] ?? ''),
                        'asset_kind' => (string) ($assetRef['type'] ?? 'asset'),
                        'mime_type' => null,
                        'fallback_url' => filled($assetRef['fallback_url'] ?? null) ? (string) $assetRef['fallback_url'] : null,
                        'metadata' => ['source' => 'ai-draft'],
                    ],
                );
            }

            $template->forceFill([
                'assets' => array_values(array_filter(array_map(
                    static fn (array $assetRef): string => (string) ($assetRef['src'] ?? ''),
                    $assetRefs
                ))),
                'asset_refs' => $assetRefs,
                'total_assets' => count($assetRefs),
            ])->save();

            return $template->fresh(['contexts', 'questions.questionOptions', 'questions.contexts']);
        });
    }

    /**
     * @param  array<int, array<string, mixed>>  $options
     * @return array<int, array<string, mixed>>
     */
    private function compileOptions(array $options, string $correctOptionId): array
    {
        $rows = [];

        foreach ($options as $index => $option) {
            if (! is_array($option)) {
                continue;
            }

            $compiled = $this->compiler->compile((string) ($option['text'] ?? ''));
            $rows[] = [
                'option_id' => (string) ($option['id'] ?? chr(65 + $index)),
                'order_base' => $index + 1,
                'is_correct' => (string) ($option['id'] ?? '') === $correctOptionId,
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

        return $rows;
    }

    private function resolveTitle(array $draft, ?string $title = null): string
    {
        $explicit = trim((string) $title);
        if ($explicit !== '') {
            return $explicit;
        }

        $firstContextTitle = trim((string) Arr::get($draft, 'contexts.0.title', ''));
        if ($firstContextTitle !== '') {
            return 'Borrador IA · '.$firstContextTitle;
        }

        $firstQuestionId = trim((string) Arr::get($draft, 'questions.0.id', ''));

        return $firstQuestionId !== ''
            ? 'Borrador IA · Pregunta '.$firstQuestionId
            : 'Borrador IA · '.now()->format('Y-m-d H:i');
    }

    /**
     * @param  array<int, array<string, mixed>>  $assetRefs
     * @return array<int, array<string, mixed>>
     */
    private function uniqueAssetRefs(array $assetRefs): array
    {
        $unique = [];

        foreach ($assetRefs as $assetRef) {
            if (! is_array($assetRef)) {
                continue;
            }

            $src = trim((string) ($assetRef['src'] ?? ''));
            if ($src === '') {
                continue;
            }

            $key = trim((string) ($assetRef['asset_id'] ?? ''));
            if ($key === '') {
                $key = sha1($src);
            }

            $unique[$key] = $assetRef;
        }

        return array_values($unique);
    }
}
