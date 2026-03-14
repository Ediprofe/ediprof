<?php

namespace App\Services\Content;

use App\Models\AssessmentContext;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentQuestionContext;
use App\Models\AssessmentTemplate;
use App\Models\Workshop;
use Illuminate\Support\Arr;
use Illuminate\Support\Carbon;

class AssessmentTemplateManifestSyncService
{
    /**
     * @param  array<string, array<string, mixed>>  $entriesByExternalId
     * @return array{total:int,created:int,updated:int,deleted:int,skipped:int}
     */
    public function sync(array $entriesByExternalId, Carbon $now, bool $dryRun = false, bool $pruneMissing = false): array
    {
        $created = 0;
        $updated = 0;
        $skipped = 0;

        $workshopMap = Workshop::query()
            ->whereIn('external_id', array_keys($entriesByExternalId))
            ->get()
            ->keyBy('external_id');

        foreach ($entriesByExternalId as $externalId => $entry) {
            if (! is_array($entry)) {
                $skipped++;

                continue;
            }

            $questions = Arr::get($entry, 'questions', []);
            if (! is_array($questions) || $questions === []) {
                $skipped++;

                continue;
            }

            $workshop = $workshopMap->get($externalId);
            if (! $workshop instanceof Workshop) {
                $skipped++;

                continue;
            }

            $templateAttributes = [
                'source_workshop_id' => $workshop->id,
                'title' => (string) (Arr::get($entry, 'title') ?? $workshop->title),
                'source_content_type' => (string) (Arr::get($entry, 'content_type') ?? $workshop->content_type ?? 'taller'),
                'default_mode' => $this->resolveDefaultMode((string) (Arr::get($entry, 'content_type') ?? 'taller')),
                'route' => Arr::get($entry, 'route'),
                'area_slug' => Arr::get($entry, 'area_slug'),
                'unidad_slug' => Arr::get($entry, 'unidad_slug'),
                'access_tier' => (string) (Arr::get($entry, 'access_tier') ?? 'premium'),
                'is_published' => (bool) (Arr::get($entry, 'published') ?? true),
                'total_questions' => max((int) (Arr::get($entry, 'stats.total_questions') ?? count($questions)), 0),
                'total_assets' => max((int) (Arr::get($entry, 'stats.total_assets') ?? count((array) Arr::get($entry, 'assets', []))), 0),
                'assets' => $this->normalizeStringList(Arr::get($entry, 'assets', [])),
                'asset_refs' => $this->normalizeAssetRefs(Arr::get($entry, 'asset_refs', [])),
                'metadata' => Arr::except($entry, ['questions', 'contexts', 'question_context_links', 'assets', 'asset_refs']),
                'synced_at' => $now,
            ];

            $existingTemplate = AssessmentTemplate::query()
                ->where('external_id', $externalId)
                ->first();

            if ($dryRun) {
                if ($existingTemplate instanceof AssessmentTemplate) {
                    $updated++;
                } else {
                    $created++;
                }

                continue;
            }

            $template = AssessmentTemplate::query()->updateOrCreate(
                ['external_id' => $externalId],
                $templateAttributes,
            );

            if ($existingTemplate instanceof AssessmentTemplate) {
                $updated++;
            } else {
                $created++;
            }

            $this->syncContexts($template, Arr::get($entry, 'contexts', []));
            $this->syncQuestions($template, $questions, (string) (Arr::get($entry, 'route') ?? ''));
            $this->syncQuestionContextLinks($template, Arr::get($entry, 'question_context_links', []));
        }

        $deleted = 0;

        if (! $dryRun && $pruneMissing) {
            $query = AssessmentTemplate::query()
                ->whereNotIn('external_id', array_keys($entriesByExternalId))
                ->doesntHave('assignments')
                ->doesntHave('attempts');

            $deleted = $query->delete();
        }

        return [
            'total' => count($entriesByExternalId),
            'created' => $created,
            'updated' => $updated,
            'deleted' => $deleted,
            'skipped' => $skipped,
        ];
    }

    /**
     * @param  mixed  $contexts
     */
    private function syncContexts(AssessmentTemplate $template, mixed $contexts): void
    {
        if (! is_array($contexts)) {
            $contexts = [];
        }

        $rows = [];
        $activeExternalIds = [];

        foreach ($contexts as $context) {
            if (! is_array($context)) {
                continue;
            }

            $externalId = trim((string) ($context['external_id'] ?? ''));
            if ($externalId === '') {
                continue;
            }

            $activeExternalIds[] = $externalId;
            $rows[] = [
                'template_id' => $template->id,
                'external_id' => $externalId,
                'title' => filled($context['title'] ?? null) ? (string) $context['title'] : null,
                'order_base' => max((int) ($context['order_base'] ?? 1), 1),
                'is_active' => true,
                'context_mdx' => (string) ($context['context_mdx'] ?? ''),
                'context_html' => (string) ($context['context_html'] ?? ''),
                'context_assets' => $this->encodeJsonValue($this->normalizeStringList($context['context_assets'] ?? [])),
                'context_blocks' => $this->encodeJsonValue($this->normalizeArrayValue($context['context_blocks'] ?? [])),
                'metadata' => $this->encodeJsonValue($this->normalizeArrayValue($context['metadata'] ?? [])),
                'created_at' => now(),
                'updated_at' => now(),
            ];
        }

        if ($rows !== []) {
            AssessmentContext::query()->upsert(
                $rows,
                ['template_id', 'external_id'],
                [
                    'title',
                    'order_base',
                    'is_active',
                    'context_mdx',
                    'context_html',
                    'context_assets',
                    'context_blocks',
                    'metadata',
                    'updated_at',
                ],
            );
        }

        $template->contexts()
            ->when(
                $activeExternalIds !== [],
                fn ($query) => $query->whereNotIn('external_id', $activeExternalIds)
            )
            ->when(
                $activeExternalIds === [],
                fn ($query) => $query
            )
            ->update(['is_active' => false]);
    }

    /**
     * @param  mixed  $questions
     */
    private function syncQuestions(AssessmentTemplate $template, mixed $questions, string $route): void
    {
        if (! is_array($questions)) {
            $questions = [];
        }

        $rows = [];
        $activeExternalIds = [];

        foreach ($questions as $index => $question) {
            if (! is_array($question)) {
                continue;
            }

            $externalId = trim((string) ($question['id'] ?? ''));
            if ($externalId === '') {
                continue;
            }

            $activeExternalIds[] = $externalId;
            $rows[] = [
                'template_id' => $template->id,
                'external_id' => $externalId,
                'order_base' => max((int) ($question['order_base'] ?? $question['order'] ?? ($index + 1)), 1),
                'source_slug' => filled($question['source_slug'] ?? null)
                    ? (string) $question['source_slug']
                    : ($route !== '' ? "{$route}#pregunta-{$externalId}" : null),
                'is_active' => true,
                'meta' => $this->encodeJsonValue($this->normalizeArrayValue($question['meta'] ?? [])),
                'stem_mdx' => (string) ($question['stem_mdx'] ?? ''),
                'stem_html' => (string) ($question['stem_html'] ?? ''),
                'stem_assets' => $this->encodeJsonValue($this->normalizeStringList($question['stem_assets'] ?? [])),
                'stem_blocks' => $this->encodeJsonValue($this->normalizeArrayValue($question['stem_blocks'] ?? [])),
                'options' => $this->encodeJsonValue($this->normalizeArrayValue($question['options'] ?? [])),
                'correct_option_id' => filled($question['correct_option_id'] ?? null) ? (string) $question['correct_option_id'] : null,
                'feedback_mdx' => (string) ($question['feedback_mdx'] ?? ''),
                'feedback_html' => (string) ($question['feedback_html'] ?? ''),
                'feedback_summary' => filled($question['feedback_summary'] ?? null) ? (string) $question['feedback_summary'] : null,
                'feedback_assets' => $this->encodeJsonValue($this->normalizeStringList($question['feedback_assets'] ?? [])),
                'feedback_blocks' => $this->encodeJsonValue($this->normalizeArrayValue($question['feedback_blocks'] ?? [])),
                'concepts_mdx' => (string) ($question['concepts_mdx'] ?? ''),
                'concepts_html' => (string) ($question['concepts_html'] ?? ''),
                'concepts_summary' => filled($question['concepts_summary'] ?? null) ? (string) $question['concepts_summary'] : null,
                'concepts_assets' => $this->encodeJsonValue($this->normalizeStringList($question['concepts_assets'] ?? [])),
                'concepts_blocks' => $this->encodeJsonValue($this->normalizeArrayValue($question['concepts_blocks'] ?? [])),
                'app_payload_version' => isset($question['app_payload_version']) ? (int) $question['app_payload_version'] : null,
                'created_at' => now(),
                'updated_at' => now(),
            ];
        }

        if ($rows !== []) {
            AssessmentQuestion::query()->upsert(
                $rows,
                ['template_id', 'external_id'],
                [
                    'order_base',
                    'source_slug',
                    'is_active',
                    'meta',
                    'stem_mdx',
                    'stem_html',
                    'stem_assets',
                    'stem_blocks',
                    'options',
                    'correct_option_id',
                    'feedback_mdx',
                    'feedback_html',
                    'feedback_summary',
                    'feedback_assets',
                    'feedback_blocks',
                    'concepts_mdx',
                    'concepts_html',
                    'concepts_summary',
                    'concepts_assets',
                    'concepts_blocks',
                    'app_payload_version',
                    'updated_at',
                ],
            );
        }

        $template->questions()
            ->when(
                $activeExternalIds !== [],
                fn ($query) => $query->whereNotIn('external_id', $activeExternalIds)
            )
            ->when(
                $activeExternalIds === [],
                fn ($query) => $query
            )
            ->update(['is_active' => false]);
    }

    /**
     * @param  mixed  $links
     */
    private function syncQuestionContextLinks(AssessmentTemplate $template, mixed $links): void
    {
        $questionMap = $template->questions()
            ->where('is_active', true)
            ->get()
            ->keyBy('external_id');
        $contextMap = $template->contexts()
            ->where('is_active', true)
            ->get()
            ->keyBy('external_id');

        $questionIds = $questionMap->pluck('id')->filter()->all();
        if ($questionIds !== []) {
            AssessmentQuestionContext::query()
                ->whereIn('question_id', $questionIds)
                ->delete();
        }

        if (! is_array($links) || $links === []) {
            return;
        }

        $rows = [];

        foreach ($links as $link) {
            if (! is_array($link)) {
                continue;
            }

            $question = $questionMap->get((string) ($link['question_external_id'] ?? ''));
            $context = $contextMap->get((string) ($link['context_external_id'] ?? ''));

            if (! $question instanceof AssessmentQuestion || ! $context instanceof AssessmentContext) {
                continue;
            }

            $rows[] = [
                'question_id' => $question->id,
                'context_id' => $context->id,
                'order_base' => max((int) ($link['order_base'] ?? 1), 1),
                'created_at' => now(),
                'updated_at' => now(),
            ];
        }

        if ($rows !== []) {
            AssessmentQuestionContext::query()->upsert(
                $rows,
                ['question_id', 'context_id'],
                ['order_base', 'updated_at'],
            );
        }
    }

    /**
     * @param  mixed  $value
     * @return array<int, mixed>
     */
    private function normalizeArrayValue(mixed $value): array
    {
        return is_array($value) ? array_values($value) : [];
    }

    /**
     * @param  mixed  $value
     * @return array<int, string>
     */
    private function normalizeStringList(mixed $value): array
    {
        if (! is_array($value)) {
            return [];
        }

        return array_values(
            array_unique(
                array_values(
                    array_filter(
                        array_map(
                            static fn ($item): string => trim((string) $item),
                            $value
                        ),
                        static fn (string $item): bool => $item !== '',
                    )
                )
            )
        );
    }

    /**
     * @param  mixed  $value
     * @return array<int, array<string, mixed>>
     */
    private function normalizeAssetRefs(mixed $value): array
    {
        if (! is_array($value)) {
            return [];
        }

        return array_values(array_filter($value, static fn ($item): bool => is_array($item) && filled($item['src'] ?? null)));
    }

    private function resolveDefaultMode(string $contentType): string
    {
        return $contentType === 'simulacro' ? 'simulacro' : 'study';
    }

    private function encodeJsonValue(array $value): string
    {
        return json_encode($value, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) ?: '[]';
    }
}
