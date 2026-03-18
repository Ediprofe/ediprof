<?php

namespace App\Services\Content;

use App\Models\AssessmentQuestion;
use Illuminate\Support\Str;

class AssessmentQuestionFingerprintService
{
    /**
     * @param  array<string, mixed>  $question
     */
    public function exactFingerprintFromDraftQuestion(array $question): string
    {
        return $this->buildExactFingerprint(
            (string) ($question['stem_mdx'] ?? ''),
            (array) ($question['options'] ?? []),
            (string) ($question['correct_option_id'] ?? '')
        );
    }

    /**
     * @param  array<string, mixed>  $question
     */
    public function searchDocumentFromDraftQuestion(array $question): string
    {
        return $this->buildSearchDocument(
            (string) ($question['stem_mdx'] ?? ''),
            (array) ($question['options'] ?? [])
        );
    }

    public function exactFingerprintForQuestion(AssessmentQuestion $question): string
    {
        return $this->buildExactFingerprint(
            (string) ($question->stem_mdx ?? ''),
            (array) ($question->options ?? []),
            (string) ($question->correct_option_id ?? '')
        );
    }

    public function searchDocumentForQuestion(AssessmentQuestion $question): string
    {
        return $this->buildSearchDocument(
            (string) ($question->stem_mdx ?? ''),
            (array) ($question->options ?? [])
        );
    }

    /**
     * @param  array<int, mixed>  $options
     */
    private function buildExactFingerprint(string $stem, array $options, string $correctOptionId): string
    {
        $normalizedStem = $this->normalizeText($stem);
        $normalizedOptions = $this->normalizeOptions($options);
        $correctText = $this->resolveCorrectOptionText($options, $correctOptionId);

        sort($normalizedOptions);

        return hash('sha256', json_encode([
            'stem' => $normalizedStem,
            'options' => $normalizedOptions,
            'correct' => $correctText,
        ], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
    }

    /**
     * @param  array<int, mixed>  $options
     */
    private function buildSearchDocument(string $stem, array $options): string
    {
        $parts = [$this->normalizeText($stem)];

        foreach ($options as $option) {
            $text = $this->extractOptionText($option);

            if ($text !== '') {
                $parts[] = $text;
            }
        }

        return trim(implode(' ', array_filter($parts)));
    }

    /**
     * @param  array<int, mixed>  $options
     * @return array<int, string>
     */
    private function normalizeOptions(array $options): array
    {
        return array_values(array_filter(array_map(
            fn ($option): string => $this->extractOptionText($option),
            $options
        )));
    }

    /**
     * @param  array<int, mixed>  $options
     */
    private function resolveCorrectOptionText(array $options, string $correctOptionId): string
    {
        $normalizedCorrectId = Str::upper(trim($correctOptionId));

        foreach ($options as $option) {
            if (! is_array($option)) {
                continue;
            }

            $optionId = Str::upper(trim((string) ($option['id'] ?? $option['option_id'] ?? '')));

            if ($optionId !== '' && $optionId === $normalizedCorrectId) {
                return $this->extractOptionText($option);
            }

            if (($option['is_correct'] ?? false) === true) {
                return $this->extractOptionText($option);
            }
        }

        return $this->normalizeText($correctOptionId);
    }

    /**
     * @param  mixed  $option
     */
    private function extractOptionText($option): string
    {
        if (! is_array($option)) {
            return '';
        }

        return $this->normalizeText((string) ($option['text'] ?? $option['plain_text'] ?? $option['text_html'] ?? ''));
    }

    private function normalizeText(string $text): string
    {
        $normalized = html_entity_decode(strip_tags($text), ENT_QUOTES | ENT_HTML5, 'UTF-8');

        return Str::of($normalized)
            ->ascii()
            ->lower()
            ->replaceMatches('/[^a-z0-9]+/u', ' ')
            ->squish()
            ->value();
    }
}
