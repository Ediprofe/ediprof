<?php

namespace App\Services\Assessments;

use App\Models\AssessmentAssignment;
use App\Models\AssessmentAssignmentQuestion;
use App\Models\AssessmentQuestion;

class AssessmentAssignmentSelectionService
{
    public function __construct(
        private readonly AssessmentQuestionGroupService $questionGroups,
    ) {
    }

    public function addQuestionSelection(AssessmentAssignment $assignment, AssessmentQuestion $question): AssessmentAssignmentQuestion
    {
        $bundle = $this->questionGroups->resolveSelectionBundle($question);
        $groupKey = $this->questionGroups->groupKeyForQuestion($question);
        $questionIds = $bundle->pluck('id')->filter()->values()->all();

        if ($questionIds !== []) {
            $assignment->questions()
                ->whereIn('question_id', $questionIds)
                ->delete();
        }

        $nextOrder = (int) ($assignment->questions()->max('order_base') ?? 0);
        $firstRecord = null;

        foreach ($bundle as $bundleQuestion) {
            $nextOrder++;

            $record = AssessmentAssignmentQuestion::query()->create([
                'assignment_id' => $assignment->id,
                'question_id' => $bundleQuestion->id,
                'selection_group_key' => $groupKey,
                'order_base' => $nextOrder,
            ]);

            $firstRecord ??= $record;
        }

        $this->resequence($assignment);

        return $firstRecord ?? AssessmentAssignmentQuestion::query()->firstOrFail();
    }

    public function removeQuestionSelection(AssessmentAssignment $assignment, AssessmentQuestion $question, ?string $selectionGroupKey = null): int
    {
        $selectionGroupKey = filled($selectionGroupKey)
            ? trim((string) $selectionGroupKey)
            : $this->questionGroups->groupKeyForQuestion($question);

        $query = $assignment->questions();
        $deleted = 0;

        if ($selectionGroupKey !== '' && $assignment->questions()->where('selection_group_key', $selectionGroupKey)->exists()) {
            $deleted = $assignment->questions()
                ->where('selection_group_key', $selectionGroupKey)
                ->delete();
        } else {
            $questionIds = $this->questionGroups->resolveSelectionBundle($question)
                ->pluck('id')
                ->filter()
                ->values()
                ->all();

            if ($questionIds !== []) {
                $deleted = $query->whereIn('question_id', $questionIds)->delete();
            }
        }

        if ($deleted > 0) {
            $this->resequence($assignment);
        }

        return $deleted;
    }

    private function resequence(AssessmentAssignment $assignment): void
    {
        $assignment->questions()
            ->orderBy('order_base')
            ->get()
            ->values()
            ->each(function (AssessmentAssignmentQuestion $row, int $index): void {
                $expected = $index + 1;

                if ((int) $row->order_base === $expected) {
                    return;
                }

                $row->forceFill([
                    'order_base' => $expected,
                ])->save();
            });
    }
}
