<?php

namespace App\Services\Assessments;

use App\Models\AssessmentContext;
use App\Models\AssessmentQuestion;
use Illuminate\Support\Collection;

class AssessmentQuestionGroupService
{
    /**
     * @return Collection<int, AssessmentQuestion>
     */
    public function resolveSelectionBundle(AssessmentQuestion $question): Collection
    {
        $question->loadMissing([
            'template',
            'contexts' => fn ($query) => $query
                ->where('assessment_contexts.is_active', true)
                ->orderBy('assessment_question_contexts.order_base'),
        ]);

        $contextIds = $question->contexts
            ->where('is_active', true)
            ->pluck('id')
            ->filter()
            ->values()
            ->all();

        if ($contextIds === []) {
            return collect([$question]);
        }

        return AssessmentQuestion::query()
            ->where('template_id', $question->template_id)
            ->where('is_active', true)
            ->whereHas('contexts', fn ($query) => $query
                ->where('assessment_contexts.is_active', true)
                ->whereIn('assessment_contexts.id', $contextIds))
            ->with([
                'template',
                'contexts' => fn ($query) => $query
                    ->where('assessment_contexts.is_active', true)
                    ->orderBy('assessment_question_contexts.order_base'),
            ])
            ->orderBy('order_base')
            ->get();
    }

    public function groupKeyForQuestion(AssessmentQuestion $question): string
    {
        $question->loadMissing([
            'template',
            'contexts' => fn ($query) => $query
                ->where('assessment_contexts.is_active', true)
                ->orderBy('assessment_question_contexts.order_base'),
        ]);

        $templateExternalId = $this->templateExternalIdForQuestion($question);
        $contextSourceKeys = $question->contexts
            ->where('is_active', true)
            ->map(fn (AssessmentContext $context): string => $this->sourceKeyForContext($context, $templateExternalId))
            ->filter()
            ->unique()
            ->values()
            ->all();

        if ($contextSourceKeys === []) {
            return 'question:'.$this->sourceKeyForQuestion($question, $templateExternalId);
        }

        return 'context:'.implode('|', $contextSourceKeys);
    }

    public function sourceKeyForQuestion(AssessmentQuestion $question, ?string $templateExternalId = null): string
    {
        $templateExternalId ??= $this->templateExternalIdForQuestion($question);

        return $templateExternalId.'#question:'.trim((string) $question->external_id);
    }

    public function sourceKeyForContext(AssessmentContext $context, ?string $templateExternalId = null): string
    {
        $templateExternalId ??= $context->template?->external_id ?: ('template:'.$context->template_id);

        return $templateExternalId.'#context:'.trim((string) $context->external_id);
    }

    public function describeBundle(AssessmentQuestion $question): string
    {
        $bundle = $this->resolveSelectionBundle($question);
        $count = $bundle->count();

        if ($count <= 1) {
            return 'Pregunta individual';
        }

        return "Contexto compartido ({$count} preguntas)";
    }

    private function templateExternalIdForQuestion(AssessmentQuestion $question): string
    {
        return $question->template?->external_id ?: ('template:'.$question->template_id);
    }
}

