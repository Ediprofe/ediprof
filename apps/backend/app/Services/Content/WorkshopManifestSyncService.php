<?php

namespace App\Services\Content;

use App\Models\Workshop;
use Illuminate\Support\Arr;
use Illuminate\Support\Carbon;
use Illuminate\Support\Facades\File;
use Illuminate\Support\Facades\Schema;
use RuntimeException;

class WorkshopManifestSyncService
{
    public function __construct(
        private readonly AssessmentTemplateManifestSyncService $assessmentTemplateSyncService
    ) {}

    /**
     * Synchronize workshops from a JSON manifest file.
     *
     * @return array{path:string,total:int,created:int,updated:int,deleted:int,skipped:int,duplicates:int,dry_run:bool}
     */
    public function sync(string $path, bool $dryRun = false, bool $pruneMissing = false): array
    {
        $resolvedPath = $this->resolvePath($path);
        $manifest = $this->loadManifest($resolvedPath);
        $entries = Arr::get($manifest, 'workshops', []);

        if (! is_array($entries)) {
            throw new RuntimeException('Invalid workshop manifest format: workshops must be an array.');
        }

        $now = Carbon::now();
        $rowsByExternalId = [];
        $entriesByExternalId = [];
        $skipped = 0;
        $duplicates = 0;

        foreach ($entries as $entry) {
            if (! is_array($entry)) {
                $skipped++;

                continue;
            }

            $normalized = $this->normalizeEntry($entry, $now);

            if ($normalized === null) {
                $skipped++;

                continue;
            }

            if (isset($rowsByExternalId[$normalized['external_id']])) {
                $duplicates++;
            }

            $rowsByExternalId[$normalized['external_id']] = $normalized;
            $entriesByExternalId[$normalized['external_id']] = $entry;
        }

        $rows = array_values($rowsByExternalId);
        $externalIds = array_column($rows, 'external_id');

        $existingIds = Workshop::query()
            ->whereIn('external_id', $externalIds)
            ->pluck('external_id')
            ->all();

        $existingMap = array_fill_keys($existingIds, true);
        $created = 0;
        $updated = 0;

        foreach ($externalIds as $externalId) {
            if (isset($existingMap[$externalId])) {
                $updated++;
            } else {
                $created++;
            }
        }

        $deleted = 0;

        if (! $dryRun) {
            if ($rows !== []) {
                Workshop::query()->upsert(
                    $rows,
                    ['external_id'],
                    [
                        'content_external_id',
                        'content_type',
                        'title',
                        'route',
                        'area_slug',
                        'unidad_slug',
                        'access_tier',
                        'is_published',
                        'total_questions',
                        'total_assets',
                        'assets',
                        'questions',
                        'metadata',
                        'synced_at',
                        'updated_at',
                    ]
                );
            }

            if (Schema::hasTable('assessment_templates')) {
                $this->assessmentTemplateSyncService->sync(
                    $entriesByExternalId,
                    $now,
                    false,
                    $pruneMissing,
                );
            }

            if ($pruneMissing) {
                $query = Workshop::query();
                if ($externalIds !== []) {
                    $query->whereNotIn('external_id', $externalIds);
                }
                $deleted = $query->delete();
            }
        } else {
            if (Schema::hasTable('assessment_templates')) {
                $this->assessmentTemplateSyncService->sync(
                    $entriesByExternalId,
                    $now,
                    true,
                    $pruneMissing,
                );
            }
        }

        return [
            'path' => $resolvedPath,
            'total' => count($rows),
            'created' => $created,
            'updated' => $updated,
            'deleted' => $deleted,
            'skipped' => $skipped,
            'duplicates' => $duplicates,
            'dry_run' => $dryRun,
        ];
    }

    private function resolvePath(string $path): string
    {
        if (File::exists($path)) {
            return $path;
        }

        $candidate = base_path($path);
        if (File::exists($candidate)) {
            return $candidate;
        }

        throw new RuntimeException("Workshop manifest file not found: {$path}");
    }

    /**
     * @return array<string, mixed>
     */
    private function loadManifest(string $path): array
    {
        $decoded = json_decode(File::get($path), true);

        if (! is_array($decoded)) {
            throw new RuntimeException("Invalid JSON workshop manifest: {$path}");
        }

        return $decoded;
    }

    /**
     * @param  array<string, mixed>  $entry
     * @return array<string, mixed>|null
     */
    private function normalizeEntry(array $entry, Carbon $now): ?array
    {
        $externalId = $this->stringOrNull(Arr::get($entry, 'id'));
        $route = $this->stringOrNull(Arr::get($entry, 'route'));

        if ($externalId === null || $route === null) {
            return null;
        }

        $questions = $this->normalizeQuestions(Arr::get($entry, 'questions', []));
        if ($questions === []) {
            return null;
        }

        $assets = $this->normalizeStringList(Arr::get($entry, 'assets', []));
        $metadata = Arr::except($entry, ['questions', 'assets']);

        $totalQuestions = Arr::get($entry, 'stats.total_questions');
        if (! is_int($totalQuestions)) {
            $totalQuestions = is_numeric($totalQuestions) ? (int) $totalQuestions : count($questions);
        }

        $totalAssets = Arr::get($entry, 'stats.total_assets');
        if (! is_int($totalAssets)) {
            $totalAssets = is_numeric($totalAssets) ? (int) $totalAssets : count($assets);
        }

        $accessTier = $this->normalizeAccessTier(
            $this->stringOrNull(Arr::get($entry, 'access_tier')) ?? 'premium'
        );

        return [
            'external_id' => $externalId,
            'content_external_id' => $this->stringOrNull(Arr::get($entry, 'content_external_id')),
            'content_type' => $this->normalizeContentType(
                $this->stringOrNull(Arr::get($entry, 'content_type')) ?? 'taller'
            ),
            'title' => $this->stringOrNull(Arr::get($entry, 'title')) ?? $route,
            'route' => $route,
            'area_slug' => $this->stringOrNull(Arr::get($entry, 'area_slug')),
            'unidad_slug' => $this->stringOrNull(Arr::get($entry, 'unidad_slug')),
            'access_tier' => $accessTier,
            'is_published' => (bool) (Arr::get($entry, 'published') ?? true),
            'total_questions' => max($totalQuestions, 0),
            'total_assets' => max($totalAssets, 0),
            'assets' => json_encode($assets, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES),
            'questions' => json_encode($questions, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES),
            'metadata' => json_encode($metadata, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES),
            'synced_at' => $now,
            'created_at' => $now,
            'updated_at' => $now,
        ];
    }

    /**
     * @return array<int, array<string, mixed>>
     */
    private function normalizeQuestions(mixed $questions): array
    {
        if (! is_array($questions)) {
            return [];
        }

        $normalized = [];

        foreach ($questions as $index => $question) {
            if (! is_array($question)) {
                continue;
            }

            $questionId = $this->stringOrNull(Arr::get($question, 'id')) ?? ('Q'.($index + 1));

            $order = Arr::get($question, 'order');
            if (! is_int($order)) {
                $order = is_numeric($order) ? (int) $order : ($index + 1);
            }

            $options = $this->normalizeOptions(Arr::get($question, 'options', []));

            $correctOptionId = $this->stringOrNull(Arr::get($question, 'correct_option_id'));
            if ($correctOptionId === null) {
                foreach ($options as $option) {
                    if (($option['is_correct'] ?? false) === true) {
                        $correctOptionId = (string) $option['id'];
                        break;
                    }
                }
            }

            $normalized[] = [
                'id' => $questionId,
                'order' => max($order, 1),
                'meta' => is_array(Arr::get($question, 'meta')) ? Arr::get($question, 'meta') : [],
                'stem_mdx' => $this->stringOrNull(Arr::get($question, 'stem_mdx')) ?? '',
                'stem_html' => $this->stringOrNull(Arr::get($question, 'stem_html')) ?? '',
                'stem_assets' => $this->normalizeStringList(Arr::get($question, 'stem_assets', [])),
                'stem_blocks' => $this->normalizeBlocks(Arr::get($question, 'stem_blocks', [])),
                'stem_nodes' => $this->normalizeBlocks(Arr::get($question, 'stem_nodes', Arr::get($question, 'stem_blocks', []))),
                'context_mdx' => $this->stringOrNull(Arr::get($question, 'context_mdx')) ?? '',
                'context_html' => $this->stringOrNull(Arr::get($question, 'context_html')) ?? '',
                'context_assets' => $this->normalizeStringList(Arr::get($question, 'context_assets', [])),
                'context_blocks' => $this->normalizeBlocks(Arr::get($question, 'context_blocks', [])),
                'context_nodes' => $this->normalizeBlocks(Arr::get($question, 'context_nodes', Arr::get($question, 'context_blocks', []))),
                'options' => $options,
                'correct_option_id' => $correctOptionId,
                'feedback_mdx' => $this->stringOrNull(Arr::get($question, 'feedback_mdx')) ?? '',
                'feedback_html' => $this->stringOrNull(Arr::get($question, 'feedback_html')) ?? '',
                'feedback_summary' => $this->stringOrNull(Arr::get($question, 'feedback_summary')) ?? null,
                'feedback_assets' => $this->normalizeStringList(Arr::get($question, 'feedback_assets', [])),
                'feedback_blocks' => $this->normalizeBlocks(Arr::get($question, 'feedback_blocks', [])),
                'feedback_nodes' => $this->normalizeBlocks(Arr::get($question, 'feedback_nodes', Arr::get($question, 'feedback_blocks', []))),
                'concepts_mdx' => $this->stringOrNull(Arr::get($question, 'concepts_mdx')) ?? '',
                'concepts_html' => $this->stringOrNull(Arr::get($question, 'concepts_html')) ?? '',
                'concepts_summary' => $this->stringOrNull(Arr::get($question, 'concepts_summary')) ?? null,
                'concepts_assets' => $this->normalizeStringList(Arr::get($question, 'concepts_assets', [])),
                'concepts_blocks' => $this->normalizeBlocks(Arr::get($question, 'concepts_blocks', [])),
                'concepts_nodes' => $this->normalizeBlocks(Arr::get($question, 'concepts_nodes', Arr::get($question, 'concepts_blocks', []))),
                'app_payload_version' => is_numeric(Arr::get($question, 'app_payload_version'))
                    ? (int) Arr::get($question, 'app_payload_version')
                    : null,
            ];
        }

        return $normalized;
    }

    /**
     * @return array<int, array{id:string,text:string,text_html?:string,text_assets?:array<int,string>,nodes_mobile?:array<int, array<string,mixed>>,is_correct:bool}>
     */
    private function normalizeOptions(mixed $options): array
    {
        if (! is_array($options)) {
            return [];
        }

        $normalized = [];

        foreach ($options as $option) {
            if (! is_array($option)) {
                continue;
            }

            $id = $this->stringOrNull(Arr::get($option, 'id'));
            $text = $this->stringOrNull(Arr::get($option, 'text'));
            $textHtml = $this->stringOrNull(Arr::get($option, 'text_html'));

            if ($id === null || $text === null) {
                continue;
            }

            $isCorrect = (bool) (Arr::get($option, 'is_correct') ?? Arr::get($option, 'correct') ?? false);

            $normalized[] = [
                'id' => $id,
                'text' => $text,
                'text_html' => $textHtml ?? '',
                'text_assets' => $this->normalizeStringList(Arr::get($option, 'text_assets', [])),
                'nodes_mobile' => $this->normalizeBlocks(Arr::get($option, 'nodes_mobile', [])),
                'is_correct' => $isCorrect,
            ];
        }

        if ($normalized === []) {
            $fallbackOptions = ['A', 'B', 'C', 'D'];

            foreach ($fallbackOptions as $optionId) {
                $normalized[] = [
                    'id' => $optionId,
                    'text' => "Opción {$optionId}",
                    'text_html' => '',
                    'text_assets' => [],
                    'nodes_mobile' => [],
                    'is_correct' => false,
                ];
            }
        }

        return array_values($normalized);
    }

    /**
     * @return array<int, string>
     */
    private function normalizeStringList(mixed $values): array
    {
        if (! is_array($values)) {
            return [];
        }

        $normalized = [];

        foreach ($values as $value) {
            $string = $this->stringOrNull($value);
            if ($string !== null) {
                $normalized[] = $string;
            }
        }

        return array_values(array_unique($normalized));
    }

    /**
     * @return array<int, array<string, mixed>>
     */
    private function normalizeBlocks(mixed $blocks): array
    {
        if (! is_array($blocks)) {
            return [];
        }

        $normalized = [];

        foreach ($blocks as $block) {
            if (! is_array($block)) {
                continue;
            }

            $type = $this->stringOrNull(Arr::get($block, 'type'));
            if ($type === null) {
                continue;
            }

            $normalized[] = $block;
        }

        return array_values($normalized);
    }

    private function normalizeAccessTier(string $accessTier): string
    {
        return in_array($accessTier, ['free', 'premium'], true) ? $accessTier : 'premium';
    }

    private function normalizeContentType(string $contentType): string
    {
        return in_array($contentType, ['taller', 'simulacro'], true) ? $contentType : 'taller';
    }

    private function stringOrNull(mixed $value): ?string
    {
        if (! is_string($value)) {
            return null;
        }

        $trimmed = trim($value);

        return $trimmed === '' ? null : $trimmed;
    }
}
