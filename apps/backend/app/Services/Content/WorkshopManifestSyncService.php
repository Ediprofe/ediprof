<?php

namespace App\Services\Content;

use App\Models\Workshop;
use Illuminate\Support\Arr;
use Illuminate\Support\Carbon;
use Illuminate\Support\Facades\File;
use RuntimeException;

class WorkshopManifestSyncService
{
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

            if ($pruneMissing) {
                $query = Workshop::query();
                if ($externalIds !== []) {
                    $query->whereNotIn('external_id', $externalIds);
                }
                $deleted = $query->delete();
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
                'stem_assets' => $this->normalizeStringList(Arr::get($question, 'stem_assets', [])),
                'options' => $options,
                'correct_option_id' => $correctOptionId,
                'feedback_mdx' => $this->stringOrNull(Arr::get($question, 'feedback_mdx')) ?? '',
                'feedback_assets' => $this->normalizeStringList(Arr::get($question, 'feedback_assets', [])),
            ];
        }

        usort($normalized, static fn (array $a, array $b): int => $a['order'] <=> $b['order']);

        return $normalized;
    }

    /**
     * @return array<int, array{id:string,text:string,is_correct:bool}>
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

            if ($id === null || $text === null) {
                continue;
            }

            $isCorrect = (bool) (Arr::get($option, 'is_correct') ?? Arr::get($option, 'correct') ?? false);

            $normalized[] = [
                'id' => $id,
                'text' => $text,
                'is_correct' => $isCorrect,
            ];
        }

        if ($normalized === []) {
            $fallbackOptions = ['A', 'B', 'C', 'D'];

            foreach ($fallbackOptions as $optionId) {
                $normalized[] = [
                    'id' => $optionId,
                    'text' => "Opción {$optionId}",
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

    private function normalizeAccessTier(string $accessTier): string
    {
        return in_array($accessTier, ['free', 'premium'], true) ? $accessTier : 'premium';
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
