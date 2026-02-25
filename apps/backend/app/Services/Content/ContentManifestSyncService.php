<?php

namespace App\Services\Content;

use App\Models\ContentCatalog;
use Illuminate\Support\Arr;
use Illuminate\Support\Carbon;
use Illuminate\Support\Facades\File;
use RuntimeException;

class ContentManifestSyncService
{
    /**
     * Synchronize content catalog from a JSON manifest file.
     *
     * @return array{path:string,total:int,created:int,updated:int,deleted:int,skipped:int,duplicates:int,dry_run:bool}
     */
    public function sync(string $path, bool $dryRun = false, bool $pruneMissing = false): array
    {
        $resolvedPath = $this->resolvePath($path);
        $manifest = $this->loadManifest($resolvedPath);
        $entries = Arr::get($manifest, 'entries', []);

        if (! is_array($entries)) {
            throw new RuntimeException('Invalid manifest format: entries must be an array.');
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

        $existingIds = ContentCatalog::query()
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

        if (! $dryRun && $rows !== []) {
            ContentCatalog::query()->upsert(
                $rows,
                ['external_id'],
                [
                    'collection',
                    'title',
                    'description',
                    'route',
                    'site_url',
                    'content_type',
                    'access_tier',
                    'area_slug',
                    'unidad_slug',
                    'tema_slug',
                    'sort_order',
                    'is_published',
                    'metadata',
                    'updated_at',
                ]
            );

            if ($pruneMissing) {
                $deleted = ContentCatalog::query()
                    ->whereNotIn('external_id', $externalIds)
                    ->delete();
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

        throw new RuntimeException("Manifest file not found: {$path}");
    }

    /**
     * @return array<string, mixed>
     */
    private function loadManifest(string $path): array
    {
        $decoded = json_decode(File::get($path), true);

        if (! is_array($decoded)) {
            throw new RuntimeException("Invalid JSON manifest: {$path}");
        }

        return $decoded;
    }

    /**
     * @param  array<string, mixed>  $entry
     * @return array<string, mixed>|null
     */
    private function normalizeEntry(array $entry, Carbon $now): ?array
    {
        $route = $this->stringOrNull(Arr::get($entry, 'route'));
        if ($route === null) {
            return null;
        }

        $externalId = $this->stringOrNull(Arr::get($entry, 'id'));
        if ($externalId === null) {
            $externalId = 'route:'.ltrim($route, '/');
        }

        $contentType = $this->normalizeContentType(
            $this->stringOrNull(Arr::get($entry, 'contentType'))
            ?? $this->stringOrNull(Arr::get($entry, 'content_type'))
            ?? $this->guessContentTypeByRoute($route)
        );

        $accessTier = $this->normalizeAccessTier(
            $this->stringOrNull(Arr::get($entry, 'accessTier'))
            ?? $this->stringOrNull(Arr::get($entry, 'access_tier'))
            ?? ($contentType === 'workshop' ? 'premium' : 'free')
        );

        $collection = $this->stringOrNull(Arr::get($entry, 'collection'))
            ?? $this->guessCollectionByRoute($route);

        $title = $this->stringOrNull(Arr::get($entry, 'title'))
            ?? $this->stringOrNull(Arr::get($entry, 'card.headline'))
            ?? $route;

        $description = $this->stringOrNull(Arr::get($entry, 'description'))
            ?? $this->stringOrNull(Arr::get($entry, 'card.subtitle'));

        $siteUrl = $this->stringOrNull(Arr::get($entry, 'siteUrl'))
            ?? $this->stringOrNull(Arr::get($entry, 'site_url'));

        $areaSlug = $this->stringOrNull(Arr::get($entry, 'area.slug'))
            ?? $this->stringOrNull(Arr::get($entry, 'taxonomy.area.slug'))
            ?? $this->guessAreaByRoute($route);

        $unidadSlug = $this->stringOrNull(Arr::get($entry, 'unidad.slug'))
            ?? $this->stringOrNull(Arr::get($entry, 'taxonomy.unidad.slug'));

        $temaSlug = $this->stringOrNull(Arr::get($entry, 'tema.slug'))
            ?? $this->stringOrNull(Arr::get($entry, 'taxonomy.tema.slug'));

        $sortOrder = Arr::get($entry, 'order');
        if (! is_int($sortOrder)) {
            $sortOrder = is_numeric($sortOrder) ? (int) $sortOrder : null;
        }

        $isPublished = (bool) (
            Arr::get($entry, 'flags.published')
            ?? Arr::get($entry, 'published')
            ?? true
        );

        return [
            'external_id' => $externalId,
            'collection' => $collection,
            'title' => $title,
            'description' => $description,
            'route' => $route,
            'site_url' => $siteUrl,
            'content_type' => $contentType,
            'access_tier' => $accessTier,
            'area_slug' => $areaSlug,
            'unidad_slug' => $unidadSlug,
            'tema_slug' => $temaSlug,
            'sort_order' => $sortOrder,
            'is_published' => $isPublished,
            'metadata' => json_encode($entry, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES),
            'created_at' => $now,
            'updated_at' => $now,
        ];
    }

    private function stringOrNull(mixed $value): ?string
    {
        if (! is_string($value)) {
            return null;
        }

        $trimmed = trim($value);

        return $trimmed === '' ? null : $trimmed;
    }

    private function guessCollectionByRoute(string $route): string
    {
        $segments = explode('/', trim($route, '/'));

        return $segments[0] ?? 'general';
    }

    private function guessAreaByRoute(string $route): ?string
    {
        $segments = explode('/', trim($route, '/'));

        if (($segments[0] ?? null) === 'saber') {
            return $segments[1] ?? null;
        }

        return $segments[0] ?? null;
    }

    private function guessContentTypeByRoute(string $route): string
    {
        return str_starts_with($route, '/saber/') ? 'workshop' : 'lesson';
    }

    private function normalizeContentType(string $contentType): string
    {
        return in_array($contentType, ['lesson', 'workshop'], true)
            ? $contentType
            : 'lesson';
    }

    private function normalizeAccessTier(string $tier): string
    {
        return in_array($tier, ['free', 'premium'], true)
            ? $tier
            : 'free';
    }
}
