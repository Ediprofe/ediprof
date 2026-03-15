<?php

namespace App\Services\Content;

class RichContentPayloadNormalizer
{
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
            'asset_url_policy' => 'absolute_or_data_uri',
            'notes' => [
                'Renderiza html cuando exista; usa blocks solo como fallback legado.',
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

        foreach (['context_assets', 'stem_assets', 'feedback_assets', 'concepts_assets'] as $assetField) {
            if (isset($question[$assetField]) && is_array($question[$assetField])) {
                $question[$assetField] = $this->normalizeAssetList($question[$assetField]);
            }
        }

        foreach (['context_blocks', 'stem_blocks', 'feedback_blocks', 'concepts_blocks'] as $blockField) {
            if (isset($question[$blockField]) && is_array($question[$blockField])) {
                $question[$blockField] = $this->normalizeBlocks($question[$blockField]);
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

    private function isPublicRelativeAsset(string $value): bool
    {
        return str_starts_with($value, '/images/')
            || str_starts_with($value, '/ilustraciones/')
            || str_starts_with($value, '/illustrations/');
    }
}
