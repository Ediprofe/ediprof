<?php

namespace App\Services\Content;

use App\Models\ContentAsset;

class RichContentPayloadNormalizer
{
    /**
     * @var array<string, array<string, mixed>>
     */
    private array $assetCache = [];

    /**
     * @return array<string, mixed>
     */
    public function renderContract(): array
    {
        return [
            'strategy' => 'html_first',
            'html_primary_fields' => [
                'context_html',
                'stem_html',
                'feedback_html',
                'concepts_html',
                'options.text_html',
            ],
            'block_fallback_fields' => [
                'context_blocks',
                'stem_blocks',
                'feedback_blocks',
                'concepts_blocks',
            ],
            'mobile_node_fields' => [
                'context_nodes',
                'stem_nodes',
                'feedback_nodes',
                'concepts_nodes',
                'options.nodes_mobile',
            ],
            'asset_url_policy' => 'absolute_or_data_uri',
            'notes' => [
                'Renderiza html cuando exista; usa blocks solo como fallback legado.',
                'Para cliente móvil, usa *_nodes y options.nodes_mobile como contrato explícito.',
                'Los assets relativos del proyecto se normalizan a URLs absolutas desde backend.',
            ],
        ];
    }

    /**
     * @param  array<int, string>  $assets
     * @return array<int, string>
     */
    public function normalizeAssetList(array $assets): array
    {
        return array_values(array_unique(array_filter(array_map(
            fn (mixed $asset): string => $this->resolveAssetUrl((string) $asset),
            $assets,
        ))));
    }

    /**
     * @param  array<int, array<string, mixed>>  $assetRefs
     * @return array<int, array<string, mixed>>
     */
    public function normalizeAssetRefs(array $assetRefs): array
    {
        return array_values(array_filter(array_map(
            fn (mixed $assetRef): ?array => is_array($assetRef)
                ? $this->normalizeAssetRef($assetRef)
                : null,
            $assetRefs,
        )));
    }

    /**
     * @param  array<int, string>  $assets
     * @return array<int, array<string, mixed>>
     */
    public function buildAssetRefsFromStrings(array $assets): array
    {
        $rows = [];

        foreach (array_values(array_unique(array_filter(array_map(
            static fn (mixed $asset): string => trim((string) $asset),
            $assets,
        )))) as $index => $src) {
            $rows[] = $this->normalizeAssetRef([
                'asset_id' => 'asset:'.substr(sha1($src), 0, 24).':'.($index + 1),
                'src' => $src,
                'alt' => null,
                'caption' => null,
                'type' => $this->inferAssetType($src),
            ]);
        }

        return array_values(array_filter($rows));
    }

    public function normalizeHtml(?string $html): string
    {
        $value = trim((string) ($html ?? ''));
        if ($value === '') {
            return '';
        }

        return preg_replace_callback(
            '/\b(src|href)=["\']([^"\']+)["\']/i',
            fn (array $matches): string => sprintf(
                '%s="%s"',
                $matches[1],
                e($this->resolveAssetUrl((string) ($matches[2] ?? '')))
            ),
            $value,
        ) ?? $value;
    }

    /**
     * @param  array<int, array<string, mixed>>  $blocks
     * @return array<int, array<string, mixed>>
     */
    public function normalizeBlocks(array $blocks): array
    {
        return array_values(array_map(
            fn (array $block): array => $this->normalizeBlock($block),
            array_filter($blocks, 'is_array'),
        ));
    }

    /**
     * @param  array<int, array<string, mixed>>  $options
     * @return array<int, array<string, mixed>>
     */
    public function normalizeOptions(array $options): array
    {
        return array_values(array_map(function (array $option): array {
            if (array_key_exists('text_html', $option)) {
                $option['text_html'] = $this->normalizeHtml((string) ($option['text_html'] ?? ''));
            }

            if (isset($option['text_assets']) && is_array($option['text_assets'])) {
                $option['text_assets'] = $this->normalizeAssetList($option['text_assets']);
            }

            if (isset($option['asset_refs']) && is_array($option['asset_refs'])) {
                $option['asset_refs'] = $this->normalizeAssetRefs($option['asset_refs']);
            } elseif (isset($option['text_assets']) && is_array($option['text_assets'])) {
                $option['asset_refs'] = $this->buildAssetRefsFromStrings($option['text_assets']);
            }

            if (isset($option['nodes_mobile']) && is_array($option['nodes_mobile']) && $option['nodes_mobile'] !== []) {
                $option['nodes_mobile'] = $this->normalizeBlocks($option['nodes_mobile']);
            } elseif (filled($option['text'] ?? null)) {
                $option['nodes_mobile'] = [[
                    'type' => 'paragraph',
                    'inlines' => [[
                        'text' => (string) $option['text'],
                        'variant' => 'plain',
                    ]],
                ]];
            } else {
                $option['nodes_mobile'] = [];
            }

            return $option;
        }, array_filter($options, 'is_array')));
    }

    /**
     * @param  array<string, mixed>  $question
     * @return array<string, mixed>
     */
    public function normalizeQuestion(array $question): array
    {
        foreach (['context_html', 'stem_html', 'feedback_html', 'concepts_html'] as $htmlField) {
            if (array_key_exists($htmlField, $question)) {
                $question[$htmlField] = $this->normalizeHtml((string) ($question[$htmlField] ?? ''));
            }
        }

        foreach ([
            'context_assets' => 'context_asset_refs',
            'stem_assets' => 'stem_asset_refs',
            'feedback_assets' => 'feedback_asset_refs',
            'concepts_assets' => 'concepts_asset_refs',
        ] as $assetField => $assetRefsField) {
            if (isset($question[$assetField]) && is_array($question[$assetField])) {
                $question[$assetField] = $this->normalizeAssetList($question[$assetField]);
            }

            if (isset($question[$assetRefsField]) && is_array($question[$assetRefsField])) {
                $question[$assetRefsField] = $this->normalizeAssetRefs($question[$assetRefsField]);
            } elseif (isset($question[$assetField]) && is_array($question[$assetField])) {
                $question[$assetRefsField] = $this->buildAssetRefsFromStrings($question[$assetField]);
            }
        }

        foreach (['context_blocks', 'stem_blocks', 'feedback_blocks', 'concepts_blocks'] as $blockField) {
            if (isset($question[$blockField]) && is_array($question[$blockField])) {
                $question[$blockField] = $this->normalizeBlocks($question[$blockField]);
            }
        }

        foreach ([
            'context_nodes' => 'context_blocks',
            'stem_nodes' => 'stem_blocks',
            'feedback_nodes' => 'feedback_blocks',
            'concepts_nodes' => 'concepts_blocks',
        ] as $nodeField => $fallbackBlockField) {
            if (isset($question[$nodeField]) && is_array($question[$nodeField])) {
                $question[$nodeField] = $this->normalizeBlocks($question[$nodeField]);
                continue;
            }

            if (isset($question[$fallbackBlockField]) && is_array($question[$fallbackBlockField])) {
                $question[$nodeField] = $this->normalizeBlocks($question[$fallbackBlockField]);
            }
        }

        if (isset($question['options']) && is_array($question['options'])) {
            $question['options'] = $this->normalizeOptions($question['options']);
        }

        return $question;
    }

    private function normalizeBlock(array $block): array
    {
        if (($block['type'] ?? null) === 'image' && isset($block['src'])) {
            $block['src'] = $this->resolveAssetUrl((string) $block['src']);
        }

        if (($block['type'] ?? null) === 'html' && isset($block['html'])) {
            $block['html'] = $this->normalizeHtml((string) $block['html']);
        }

        if (isset($block['items']) && is_array($block['items'])) {
            $block['items'] = array_map(function (mixed $item): mixed {
                if (! is_array($item)) {
                    return $item;
                }

                if (isset($item['src'])) {
                    $item['src'] = $this->resolveAssetUrl((string) $item['src']);
                }

                if (isset($item['html'])) {
                    $item['html'] = $this->normalizeHtml((string) $item['html']);
                }

                return $item;
            }, $block['items']);
        }

        return $block;
    }

    /**
     * @param  array<string, mixed>  $assetRef
     * @return array<string, mixed>|null
     */
    private function normalizeAssetRef(array $assetRef): ?array
    {
        $src = trim((string) ($assetRef['src'] ?? ''));
        if ($src === '') {
            return null;
        }

        $record = $this->lookupAssetRecord($src);
        $normalizedSrc = $this->resolveAssetUrl($src);
        $canonicalUrl = $record['canonical_url'] ?? $normalizedSrc;

        return [
            'asset_id' => filled($assetRef['asset_id'] ?? null)
                ? (string) $assetRef['asset_id']
                : ($record['asset_key'] ?? 'asset:'.substr(sha1($src), 0, 24)),
            'src' => $canonicalUrl,
            'alt' => $assetRef['alt'] ?? null,
            'caption' => $assetRef['caption'] ?? null,
            'type' => (string) ($assetRef['type'] ?? $record['asset_kind'] ?? $this->inferAssetType($src)),
            'mime_type' => $record['mime_type'] ?? null,
            'fallback_url' => $record['fallback_url'] ?? null,
            'width' => $record['width'] ?? null,
            'height' => $record['height'] ?? null,
        ];
    }

    private function resolveAssetUrl(string $value): string
    {
        $normalized = trim($value);
        if ($normalized === '') {
            return '';
        }

        if (
            preg_match('/^https?:\/\//i', $normalized) === 1 ||
            str_starts_with($normalized, 'data:') ||
            str_starts_with($normalized, 'blob:')
        ) {
            return $normalized;
        }

        if (! $this->isPublicRelativeAsset($normalized)) {
            return $normalized;
        }

        $baseUrl = rtrim((string) config('app.content_asset_base_url', ''), '/');

        if ($baseUrl === '') {
            return $normalized;
        }

        return $baseUrl.$normalized;
    }

    /**
     * @return array<string, mixed>|null
     */
    private function lookupAssetRecord(string $src): ?array
    {
        if (array_key_exists($src, $this->assetCache)) {
            return $this->assetCache[$src] !== [] ? $this->assetCache[$src] : null;
        }

        $normalizedSrc = $this->resolveAssetUrl($src);

        $record = ContentAsset::query()
            ->where('source_ref', $src)
            ->orWhere('source_ref', $normalizedSrc)
            ->orWhere('canonical_url', $normalizedSrc)
            ->first();

        $this->assetCache[$src] = $record instanceof ContentAsset
            ? [
                'asset_key' => $record->asset_key,
                'canonical_url' => $record->canonical_url,
                'asset_kind' => $record->asset_kind,
                'mime_type' => $record->mime_type,
                'fallback_url' => $record->fallback_url,
                'width' => $record->width,
                'height' => $record->height,
            ]
            : [];

        return $this->assetCache[$src] !== [] ? $this->assetCache[$src] : null;
    }

    private function inferAssetType(string $src): string
    {
        return match (true) {
            preg_match('/\.svg$/i', $src) === 1 => 'svg',
            preg_match('/\.(png|jpg|jpeg|webp|gif|avif)$/i', $src) === 1 => 'image',
            preg_match('/\.pdf$/i', $src) === 1 => 'document',
            default => 'asset',
        };
    }

    private function isPublicRelativeAsset(string $value): bool
    {
        return str_starts_with($value, '/images/')
            || str_starts_with($value, '/ilustraciones/')
            || str_starts_with($value, '/illustrations/');
    }
}
