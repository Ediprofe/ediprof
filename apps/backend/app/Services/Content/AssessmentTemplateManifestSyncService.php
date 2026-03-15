<?php

namespace App\Services\Content;

use App\Models\AssessmentContext;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentQuestionOption;
use App\Models\AssessmentQuestionContext;
use App\Models\AssessmentTemplate;
use App\Models\ContentAsset;
use App\Models\Workshop;
use Illuminate\Support\Arr;
use Illuminate\Support\Carbon;

class AssessmentTemplateManifestSyncService
{
    public function __construct(
        private readonly RichContentPayloadNormalizer $contentNormalizer,
    ) {}

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
            $this->syncQuestionOptions($template, $questions);
            $this->syncQuestionContextLinks($template, Arr::get($entry, 'question_context_links', []));
            $this->syncContentAssets($template, $entry);
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

    private function syncQuestionOptions(AssessmentTemplate $template, mixed $questions): void
    {
        if (! is_array($questions)) {
            $questions = [];
        }

        $questionMap = $template->questions()
            ->where('is_active', true)
            ->get()
            ->keyBy('external_id');

        $questionIds = $questionMap->pluck('id')->filter()->values()->all();
        if ($questionIds !== []) {
            AssessmentQuestionOption::query()
                ->whereIn('question_id', $questionIds)
                ->delete();
        }

        $rows = [];

        foreach ($questions as $questionIndex => $question) {
            if (! is_array($question)) {
                continue;
            }

            $externalId = trim((string) ($question['id'] ?? ''));
            if ($externalId === '') {
                continue;
            }

            $questionModel = $questionMap->get($externalId);
            if (! $questionModel instanceof AssessmentQuestion) {
                continue;
            }

            $correctOptionId = trim((string) ($question['correct_option_id'] ?? ''));
            $options = is_array($question['options'] ?? null) ? $question['options'] : [];

            foreach ($options as $optionIndex => $option) {
                if (! is_array($option)) {
                    continue;
                }

                $optionId = trim((string) ($option['id'] ?? ''));
                if ($optionId === '') {
                    continue;
                }

                $textAssets = $this->normalizeStringList($option['text_assets'] ?? []);
                $rows[] = [
                    'question_id' => $questionModel->id,
                    'option_id' => $optionId,
                    'order_base' => max((int) ($option['order_base'] ?? ($optionIndex + 1)), 1),
                    'is_correct' => array_key_exists('is_correct', $option)
                        ? (bool) $option['is_correct']
                        : ($correctOptionId !== '' && $correctOptionId === $optionId),
                    'plain_text' => (string) ($option['text'] ?? ''),
                    'html_web' => filled($option['text_html'] ?? null) ? (string) $option['text_html'] : null,
                    'nodes_mobile' => $this->encodeJsonValue($this->normalizeArrayValue($option['nodes_mobile'] ?? [])),
                    'asset_refs' => $this->encodeJsonValue($this->buildAssetRefsFromStrings($textAssets)),
                    'metadata' => $this->encodeJsonValue([
                        'legacy_text_assets' => $textAssets,
                        'question_external_id' => $externalId,
                        'question_order' => max((int) ($question['order_base'] ?? $question['order'] ?? ($questionIndex + 1)), 1),
                    ]),
                    'created_at' => now(),
                    'updated_at' => now(),
                ];
            }
        }

        if ($rows !== []) {
            AssessmentQuestionOption::query()->insert($rows);
        }
    }

    private function syncContentAssets(AssessmentTemplate $template, mixed $entry): void
    {
        if (! is_array($entry)) {
            return;
        }

        $assetMap = [];

        foreach ($this->normalizeAssetRefs(Arr::get($entry, 'asset_refs', [])) as $assetRef) {
            $src = trim((string) ($assetRef['src'] ?? ''));
            if ($src === '') {
                continue;
            }

            $assetMap[$src] = [
                'src' => $src,
                'type' => (string) ($assetRef['type'] ?? $this->inferAssetKind($src)),
                'metadata' => $assetRef,
            ];
        }

        foreach ($this->collectStringAssetRefsFromEntry($entry) as $src) {
            if (! isset($assetMap[$src])) {
                $assetMap[$src] = [
                    'src' => $src,
                    'type' => $this->inferAssetKind($src),
                    'metadata' => [],
                ];
            }
        }

        if ($assetMap === []) {
            return;
        }

        $rows = [];
        foreach ($assetMap as $src => $asset) {
            $canonicalUrl = $this->resolveCanonicalAssetUrl($src);
            $rows[] = [
                'asset_key' => sha1($src),
                'source_ref' => $src,
                'canonical_url' => $canonicalUrl,
                'asset_kind' => (string) ($asset['type'] ?? $this->inferAssetKind($src)),
                'mime_type' => $this->inferMimeType($src),
                'fallback_url' => null,
                'width' => null,
                'height' => null,
                'metadata' => $this->encodeJsonValue([
                    'template_external_id' => $template->external_id,
                    'source_content_type' => $template->source_content_type,
                    'asset_ref' => $asset['metadata'] ?? [],
                ]),
                'created_at' => now(),
                'updated_at' => now(),
            ];
        }

        ContentAsset::query()->upsert(
            $rows,
            ['asset_key'],
            [
                'source_ref',
                'canonical_url',
                'asset_kind',
                'mime_type',
                'fallback_url',
                'width',
                'height',
                'metadata',
                'updated_at',
            ],
        );
    }

    /**
     * @return array<int, mixed>
     */
    private function normalizeArrayValue(mixed $value): array
    {
        return is_array($value) ? array_values($value) : [];
    }

    /**
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
     * @return array<int, array<string, mixed>>
     */
    private function normalizeAssetRefs(mixed $value): array
    {
        if (! is_array($value)) {
            return [];
        }

        return array_values(array_filter($value, static fn ($item): bool => is_array($item) && filled($item['src'] ?? null)));
    }

    /**
     * @return array<int, string>
     */
    private function collectStringAssetRefsFromEntry(array $entry): array
    {
        $assetRefs = $this->normalizeStringList(Arr::get($entry, 'assets', []));

        foreach (Arr::get($entry, 'contexts', []) as $context) {
            if (! is_array($context)) {
                continue;
            }

            $assetRefs = [
                ...$assetRefs,
                ...$this->normalizeStringList($context['context_assets'] ?? []),
            ];
        }

        foreach (Arr::get($entry, 'questions', []) as $question) {
            if (! is_array($question)) {
                continue;
            }

            $assetRefs = [
                ...$assetRefs,
                ...$this->normalizeStringList($question['context_assets'] ?? []),
                ...$this->normalizeStringList($question['stem_assets'] ?? []),
                ...$this->normalizeStringList($question['feedback_assets'] ?? []),
                ...$this->normalizeStringList($question['concepts_assets'] ?? []),
            ];

            foreach ($question['options'] ?? [] as $option) {
                if (! is_array($option)) {
                    continue;
                }

                $assetRefs = [
                    ...$assetRefs,
                    ...$this->normalizeStringList($option['text_assets'] ?? []),
                ];
            }
        }

        return array_values(array_unique(array_filter($assetRefs)));
    }

    /**
     * @param  array<int, string>  $assets
     * @return array<int, array<string, mixed>>
     */
    private function buildAssetRefsFromStrings(array $assets): array
    {
        $rows = [];

        foreach (array_values(array_unique(array_filter($assets))) as $index => $src) {
            $rows[] = [
                'asset_id' => 'asset:'.substr(sha1($src), 0, 24).':'.($index + 1),
                'src' => $src,
                'alt' => null,
                'caption' => null,
                'type' => $this->inferAssetKind($src),
            ];
        }

        return $rows;
    }

    private function resolveCanonicalAssetUrl(string $src): string
    {
        $assets = $this->contentNormalizer->normalizeAssetList([$src]);

        return $assets[0] ?? trim($src);
    }

    private function inferAssetKind(string $src): string
    {
        return match (true) {
            preg_match('/\.svg$/i', $src) === 1 => 'svg',
            preg_match('/\.(png|jpg|jpeg|webp|gif|avif)$/i', $src) === 1 => 'image',
            preg_match('/\.pdf$/i', $src) === 1 => 'document',
            default => 'asset',
        };
    }

    private function inferMimeType(string $src): ?string
    {
        return match (strtolower((string) pathinfo(parse_url($src, PHP_URL_PATH) ?: $src, PATHINFO_EXTENSION))) {
            'svg' => 'image/svg+xml',
            'png' => 'image/png',
            'jpg', 'jpeg' => 'image/jpeg',
            'webp' => 'image/webp',
            'gif' => 'image/gif',
            'avif' => 'image/avif',
            'pdf' => 'application/pdf',
            default => null,
        };
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
