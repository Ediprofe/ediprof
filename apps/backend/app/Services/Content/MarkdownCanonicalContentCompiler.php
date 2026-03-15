<?php

namespace App\Services\Content;

use Illuminate\Support\Str;
use League\CommonMark\Environment\Environment;
use League\CommonMark\Extension\CommonMark\CommonMarkCoreExtension;
use League\CommonMark\Extension\Strikethrough\StrikethroughExtension;
use League\CommonMark\Extension\Table\TableExtension;
use League\CommonMark\MarkdownConverter;

class MarkdownCanonicalContentCompiler
{
    private MarkdownConverter $converter;

    public function __construct(
        private readonly RichContentPayloadNormalizer $normalizer,
    ) {
        $environment = new Environment([
            'html_input' => 'strip',
            'allow_unsafe_links' => false,
        ]);

        $environment->addExtension(new CommonMarkCoreExtension());
        $environment->addExtension(new TableExtension());
        $environment->addExtension(new StrikethroughExtension());

        $this->converter = new MarkdownConverter($environment);
    }

    /**
     * @return array{
     *   markdown:string,
     *   plain_text:string,
     *   html_web:string,
     *   assets:array<int,string>,
     *   asset_refs:array<int,array<string,mixed>>,
     *   blocks:array<int,array<string,mixed>>
     * }
     */
    public function compile(?string $markdown): array
    {
        $source = trim((string) $markdown);

        if ($source === '') {
            return [
                'markdown' => '',
                'plain_text' => '',
                'html_web' => '',
                'assets' => [],
                'asset_refs' => [],
                'blocks' => [],
            ];
        }

        $placeholders = [];
        $prepared = $this->replaceHighlightMarkup($source, $placeholders);
        $html = (string) $this->converter->convert($prepared);

        foreach ($placeholders as $placeholder => $replacement) {
            $html = str_replace($placeholder, $replacement, $html);
        }

        $html = $this->normalizer->normalizeHtml($html);
        $assets = $this->extractAssetStrings($source, $html);

        return [
            'markdown' => $source,
            'plain_text' => Str::of(strip_tags($html))->squish()->value(),
            'html_web' => $html,
            'assets' => $assets,
            'asset_refs' => $this->normalizer->buildAssetRefsFromStrings($assets),
            'blocks' => [],
        ];
    }

    /**
     * @param  array<string, string>  $placeholders
     */
    private function replaceHighlightMarkup(string $markdown, array &$placeholders): string
    {
        return (string) preg_replace_callback('/(?<!\\\\)==(.+?)(?<!\\\\)==/', function (array $matches) use (&$placeholders): string {
            $content = trim((string) ($matches[1] ?? ''));
            $token = strtoupper(sprintf('CANONICAL_HIGHLIGHT_%d', count($placeholders) + 1));

            $placeholders[$token] = sprintf('<mark>%s</mark>', e($content));

            return $token;
        }, $markdown);
    }

    /**
     * @return array<int, string>
     */
    private function extractAssetStrings(string $markdown, string $html): array
    {
        $assets = [];

        if (preg_match_all('/!\[[^\]]*]\(([^)]+)\)/', $markdown, $markdownMatches) === 1) {
            foreach (($markdownMatches[1] ?? []) as $src) {
                $assets[] = trim((string) $src);
            }
        }

        if (preg_match_all('/\b(?:src|href)=["\']([^"\']+)["\']/', $html, $htmlMatches) === 1) {
            foreach (($htmlMatches[1] ?? []) as $src) {
                $assets[] = trim((string) $src);
            }
        }

        return array_values(array_unique(array_filter($assets)));
    }
}
