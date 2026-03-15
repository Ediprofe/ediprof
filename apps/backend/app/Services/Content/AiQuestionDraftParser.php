<?php

namespace App\Services\Content;

use Illuminate\Support\Str;
use RuntimeException;

class AiQuestionDraftParser
{
    /**
     * @return array{
     *   schema:string,
     *   contexts:array<int, array<string, mixed>>,
     *   questions:array<int, array<string, mixed>>,
     *   question_context_links:array<int, array<string, mixed>>
     * }
     */
    public function parse(string $markdown): array
    {
        $source = trim(str_replace("\r\n", "\n", $markdown));

        if ($source === '') {
            throw new RuntimeException('El borrador IA está vacío.');
        }

        $lines = explode("\n", $source);
        $contexts = [];
        $questions = [];
        $links = [];

        $activeSharedContext = null;
        $activeSharedContextOrder = 1;
        $currentQuestion = null;
        $questionOrder = 1;

        $outsideHeading = null;
        $outsideBuffer = [];
        $questionSection = null;
        $questionBuffer = [];

        $flushOutside = function () use (&$outsideHeading, &$outsideBuffer, &$contexts, &$activeSharedContext, &$activeSharedContextOrder): void {
            if ($outsideHeading === null) {
                $outsideBuffer = [];
                return;
            }

            $content = trim(implode("\n", $outsideBuffer));
            if ($content === '') {
                $outsideHeading = null;
                $outsideBuffer = [];
                return;
            }

            if (in_array($outsideHeading['kind'], ['shared_context', 'context'], true)) {
                $title = $outsideHeading['title']
                    ?: ($outsideHeading['kind'] === 'shared_context'
                        ? 'Contexto compartido '.$activeSharedContextOrder
                        : 'Contexto '.$activeSharedContextOrder);
                $externalId = $outsideHeading['external_id'] ?: 'shared-context-'.$activeSharedContextOrder;

                $contexts[$externalId] = [
                    'external_id' => $externalId,
                    'title' => $title,
                    'order_base' => $activeSharedContextOrder,
                    'context_mdx' => $content,
                    'metadata' => [
                        'source' => 'ai-draft',
                        'scope' => 'shared',
                        'inferred_from_generic_context_heading' => $outsideHeading['kind'] === 'context',
                    ],
                ];

                $activeSharedContext = $externalId;
                $activeSharedContextOrder++;
            }

            $outsideHeading = null;
            $outsideBuffer = [];
        };

        $flushQuestionSection = function () use (&$currentQuestion, &$questionSection, &$questionBuffer): void {
            if ($currentQuestion === null || $questionSection === null) {
                $questionBuffer = [];
                return;
            }

            $content = trim(implode("\n", $questionBuffer));
            $normalizedSection = $questionSection['kind'];

            if ($normalizedSection === 'stem' && $content !== '') {
                $currentQuestion['stem_mdx'] = $this->appendContent($currentQuestion['stem_mdx'], $content);
            }

            if ($normalizedSection === 'context' && $content !== '') {
                $currentQuestion['context_mdx'] = $this->appendContent($currentQuestion['context_mdx'], $content);
            }

            if ($normalizedSection === 'options' && $content !== '') {
                $currentQuestion['options'] = $this->parseOptions($content);
            }

            if ($normalizedSection === 'correct' && $content !== '') {
                $currentQuestion['correct_option_id'] = $this->parseCorrectOptionId($content);
            }

            if ($normalizedSection === 'feedback' && $content !== '') {
                $currentQuestion['feedback_mdx'] = $this->appendContent($currentQuestion['feedback_mdx'], $content);
            }

            if ($normalizedSection === 'concepts' && $content !== '') {
                $currentQuestion['concepts_mdx'] = $this->appendContent($currentQuestion['concepts_mdx'], $content);
            }

            $questionSection = null;
            $questionBuffer = [];
        };

        $flushQuestion = function () use (
            &$currentQuestion,
            &$questionSection,
            &$questionBuffer,
            &$questions,
            &$contexts,
            &$links,
            &$questionOrder,
            &$flushQuestionSection
        ): void {
            if ($currentQuestion === null) {
                return;
            }

            $flushQuestionSection();

            $stem = trim((string) ($currentQuestion['stem_mdx'] ?? ''));
            $options = is_array($currentQuestion['options'] ?? null) ? $currentQuestion['options'] : [];

            if ($stem === '' || count($options) < 2) {
                throw new RuntimeException(sprintf(
                    'La pregunta "%s" no tiene enunciado válido u opciones suficientes.',
                    (string) ($currentQuestion['id'] ?? 'sin-id')
                ));
            }

            $correctOptionId = $currentQuestion['correct_option_id'] ?? null;
            if (! is_string($correctOptionId) || $correctOptionId === '') {
                throw new RuntimeException(sprintf(
                    'La pregunta "%s" no tiene una opción correcta declarada.',
                    (string) ($currentQuestion['id'] ?? 'sin-id')
                ));
            }

            $localContext = trim((string) ($currentQuestion['context_mdx'] ?? ''));
            $contextRefs = [];

            if ($localContext !== '') {
                $contextExternalId = 'inline-context-'.Str::slug((string) $currentQuestion['id'], '-');

                $contexts[$contextExternalId] = [
                    'external_id' => $contextExternalId,
                    'title' => 'Contexto de '.(string) $currentQuestion['id'],
                    'order_base' => $questionOrder,
                    'context_mdx' => $localContext,
                    'metadata' => [
                        'source' => 'ai-draft',
                        'scope' => 'question',
                        'question_id' => (string) $currentQuestion['id'],
                    ],
                ];

                $contextRefs[] = $contextExternalId;
            }

            foreach ((array) ($currentQuestion['shared_context_refs'] ?? []) as $sharedContextRef) {
                if (is_string($sharedContextRef) && $sharedContextRef !== '') {
                    $contextRefs[] = $sharedContextRef;
                }
            }

            $contextRefs = array_values(array_unique($contextRefs));

            if ($contextRefs === []) {
                throw new RuntimeException(sprintf(
                    'La pregunta "%s" no tiene contexto. Cada ítem del banco debe pertenecer a un bloque contextual.',
                    (string) ($currentQuestion['id'] ?? 'sin-id')
                ));
            }

            foreach ($contextRefs as $index => $contextRef) {
                $links[] = [
                    'question_external_id' => (string) $currentQuestion['id'],
                    'context_external_id' => $contextRef,
                    'order_base' => $index + 1,
                ];
            }

            unset($currentQuestion['context_mdx'], $currentQuestion['shared_context_refs']);
            $currentQuestion['order'] = $questionOrder;
            $currentQuestion['order_base'] = $questionOrder;

            $questions[] = $currentQuestion;
            $questionOrder++;
            $currentQuestion = null;
        };

        foreach ($lines as $line) {
            if (preg_match('/^(#{1,4})\s+(.*)$/', $line, $matches) === 1) {
                $headingText = trim((string) $matches[2]);
                $heading = $this->parseHeading($headingText);

                if ($heading['kind'] === 'question') {
                    $flushOutside();
                    $flushQuestion();

                    $currentQuestion = [
                        'id' => $heading['external_id'] ?: 'Q'.$questionOrder,
                        'title' => $heading['title'] ?: ('Pregunta '.$questionOrder),
                        'stem_mdx' => '',
                        'context_mdx' => '',
                        'options' => [],
                        'correct_option_id' => null,
                        'feedback_mdx' => '',
                        'concepts_mdx' => '',
                        'shared_context_refs' => $activeSharedContext ? [$activeSharedContext] : [],
                        'metadata' => [
                            'source' => 'ai-draft',
                        ],
                    ];
                    $questionSection = [
                        'kind' => 'stem',
                    ];
                    $questionBuffer = [];
                    continue;
                }

                if ($currentQuestion !== null) {
                    $flushQuestionSection();

                    if (in_array($heading['kind'], ['context', 'stem', 'options', 'correct', 'feedback', 'concepts'], true)) {
                        $questionSection = ['kind' => $heading['kind']];
                        $questionBuffer = [];
                        continue;
                    }

                    // Unknown heading inside a question goes back to stem to avoid losing text.
                    $questionSection = ['kind' => 'stem'];
                    $questionBuffer = [$headingText];
                    continue;
                }

                $flushOutside();

                if (in_array($heading['kind'], ['shared_context', 'context'], true)) {
                    $outsideHeading = $heading;
                    $outsideBuffer = [];
                    continue;
                }

                // Unknown heading outside question/context is ignored for MVP.
                continue;
            }

            if ($currentQuestion !== null) {
                $questionBuffer[] = $line;
                continue;
            }

            if ($outsideHeading !== null) {
                $outsideBuffer[] = $line;
            }
        }

        $flushOutside();
        $flushQuestion();

        if ($questions === []) {
            throw new RuntimeException('El borrador IA no contiene ninguna pregunta reconocible.');
        }

        return [
            'schema' => 'ai_question_draft_v1',
            'contexts' => array_values($contexts),
            'questions' => $questions,
            'question_context_links' => $links,
        ];
    }

    /**
     * @return array{kind:string,title:string,external_id:?string}
     */
    private function parseHeading(string $headingText): array
    {
        $normalized = Str::of($headingText)->lower()->ascii()->trim()->value();

        if (preg_match('/^contexto compartido(?:\s*[:\-]\s*(.+))?$/i', $headingText, $matches) === 1) {
            $title = trim((string) ($matches[1] ?? ''));

            return [
                'kind' => 'shared_context',
                'title' => $title,
                'external_id' => $title !== '' ? 'shared-context-'.Str::slug($title, '-') : null,
            ];
        }

        if (preg_match('/^pregunta(?:\s+|[:\-]\s*|\s*#\s*)(.+)?$/i', $headingText, $matches) === 1) {
            $label = trim((string) ($matches[1] ?? ''));
            $externalId = $label !== '' ? Str::upper(str_replace(' ', '-', $label)) : null;

            return [
                'kind' => 'question',
                'title' => $label !== '' ? 'Pregunta '.$label : '',
                'external_id' => $externalId,
            ];
        }

        if (preg_match('/^contexto(?:\s*[:\-]\s*(.+))?$/i', $headingText, $matches) === 1) {
            $title = trim((string) ($matches[1] ?? ''));

            return [
                'kind' => 'context',
                'title' => $title,
                'external_id' => $title !== '' ? 'shared-context-'.Str::slug($title, '-') : null,
            ];
        }

        return match (true) {
            str_starts_with($normalized, 'enunciado') => ['kind' => 'stem', 'title' => '', 'external_id' => null],
            str_starts_with($normalized, 'pregunta') => ['kind' => 'stem', 'title' => '', 'external_id' => null],
            str_starts_with($normalized, 'opciones') => ['kind' => 'options', 'title' => '', 'external_id' => null],
            str_starts_with($normalized, 'correcta') || str_starts_with($normalized, 'respuesta correcta') => ['kind' => 'correct', 'title' => '', 'external_id' => null],
            str_starts_with($normalized, 'retroalimentacion') || str_starts_with($normalized, 'retroalimentación') || str_starts_with($normalized, 'solucion') || str_starts_with($normalized, 'solución') => ['kind' => 'feedback', 'title' => '', 'external_id' => null],
            str_starts_with($normalized, 'conceptos relacionados') || str_starts_with($normalized, 'conceptos') => ['kind' => 'concepts', 'title' => '', 'external_id' => null],
            default => ['kind' => 'unknown', 'title' => '', 'external_id' => null],
        };
    }

    /**
     * @return array<int, array{id:string,text:string,is_correct:bool}>
     */
    private function parseOptions(string $content): array
    {
        $lines = explode("\n", trim($content));
        $options = [];
        $currentId = null;
        $currentBuffer = [];

        $flush = function () use (&$options, &$currentId, &$currentBuffer): void {
            if ($currentId === null) {
                $currentBuffer = [];
                return;
            }

            $text = trim(implode("\n", $currentBuffer));
            $options[] = [
                'id' => $currentId,
                'text' => $text,
                'is_correct' => false,
            ];

            $currentId = null;
            $currentBuffer = [];
        };

        foreach ($lines as $line) {
            if (preg_match('/^\s*([A-Z])[\.\)]\s+(.*)$/', $line, $matches) === 1) {
                $flush();
                $currentId = strtoupper((string) $matches[1]);
                $currentBuffer = [trim((string) $matches[2])];
                continue;
            }

            if ($currentId !== null) {
                $currentBuffer[] = rtrim($line);
            }
        }

        $flush();

        if (count($options) < 2) {
            throw new RuntimeException('Las opciones del borrador deben venir en formato "A. ...", "B. ...".');
        }

        return $options;
    }

    private function parseCorrectOptionId(string $content): string
    {
        if (preg_match('/\b([A-Z])\b/', strtoupper($content), $matches) === 1) {
            return (string) $matches[1];
        }

        throw new RuntimeException('No se pudo identificar la opción correcta en el borrador IA.');
    }

    private function appendContent(string $existing, string $new): string
    {
        $existing = trim($existing);
        $new = trim($new);

        if ($existing === '') {
            return $new;
        }

        if ($new === '') {
            return $existing;
        }

        return $existing."\n\n".$new;
    }
}
