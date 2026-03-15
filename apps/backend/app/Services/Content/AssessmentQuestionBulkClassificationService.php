<?php

namespace App\Services\Content;

use App\Models\AssessmentContext;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentUnit;
use Illuminate\Database\Eloquent\Collection;
use Illuminate\Support\Facades\DB;

class AssessmentQuestionBulkClassificationService
{
    /**
     * @param  Collection<int, AssessmentQuestion>  $questions
     * @param  array{
     *   unit_id?:int|string|null,
     *   topic?:string|null,
     *   subtopic?:string|null,
     *   editorial_status?:string|null,
     *   tags?:array<int,string>|null,
     *   sync_linked_contexts?:bool|null
     * }  $classification
     * @return array{
     *   questions_updated:int,
     *   contexts_updated:int,
     *   questions_skipped_unit_mismatch:int,
     *   contexts_skipped_unit_mismatch:int
     * }
     */
    public function classify(Collection $questions, array $classification): array
    {
        /** @var AssessmentUnit|null $unit */
        $unit = filled($classification['unit_id'] ?? null)
            ? AssessmentUnit::query()->findOrFail((int) $classification['unit_id'])
            : null;

        $topic = $this->normalizeString($classification['topic'] ?? null);
        $subtopic = $this->normalizeString($classification['subtopic'] ?? null);
        $editorialStatus = $this->normalizeString($classification['editorial_status'] ?? null);
        $tags = $this->normalizeTags($classification['tags'] ?? []);
        $syncContexts = (bool) ($classification['sync_linked_contexts'] ?? false);

        $summary = [
            'questions_updated' => 0,
            'contexts_updated' => 0,
            'questions_skipped_unit_mismatch' => 0,
            'contexts_skipped_unit_mismatch' => 0,
        ];

        if (! $unit && $topic === null && $subtopic === null && $editorialStatus === null && $tags === []) {
            return $summary;
        }

        DB::transaction(function () use ($questions, $unit, $topic, $subtopic, $editorialStatus, $tags, $syncContexts, &$summary): void {
            $contextsHandled = [];

            /** @var AssessmentQuestion $question */
            foreach ($questions->loadMissing('contexts') as $question) {
                if ($unit && filled($question->subject_id) && (int) $question->subject_id !== (int) $unit->subject_id) {
                    $summary['questions_skipped_unit_mismatch']++;
                    continue;
                }

                $questionPayload = $this->buildPayload(
                    subjectId: $unit?->subject_id,
                    unitId: $unit?->id,
                    topic: $topic,
                    subtopic: $subtopic,
                    editorialStatus: $editorialStatus,
                    tags: $tags,
                    currentTags: $question->tags,
                    canBackfillSubject: ! filled($question->subject_id),
                );

                if ($questionPayload !== []) {
                    $question->forceFill($questionPayload)->save();
                    $summary['questions_updated']++;
                }

                if (! $syncContexts) {
                    continue;
                }

                /** @var AssessmentContext $context */
                foreach ($question->contexts as $context) {
                    if (isset($contextsHandled[$context->id])) {
                        continue;
                    }

                    if ($unit && filled($context->subject_id) && (int) $context->subject_id !== (int) $unit->subject_id) {
                        $summary['contexts_skipped_unit_mismatch']++;
                        $contextsHandled[$context->id] = true;
                        continue;
                    }

                    $contextPayload = $this->buildPayload(
                        subjectId: $unit?->subject_id,
                        unitId: $unit?->id,
                        topic: $topic,
                        subtopic: $subtopic,
                        editorialStatus: $editorialStatus,
                        tags: $tags,
                        currentTags: $context->tags,
                        canBackfillSubject: ! filled($context->subject_id),
                    );

                    if ($contextPayload !== []) {
                        $context->forceFill($contextPayload)->save();
                        $summary['contexts_updated']++;
                    }

                    $contextsHandled[$context->id] = true;
                }
            }
        });

        return $summary;
    }

    /**
     * @param  array<int,string>|null  $currentTags
     * @param  array<int,string>  $tags
     * @return array<string,mixed>
     */
    private function buildPayload(
        ?int $subjectId,
        ?int $unitId,
        ?string $topic,
        ?string $subtopic,
        ?string $editorialStatus,
        array $tags,
        ?array $currentTags,
        bool $canBackfillSubject,
    ): array {
        $payload = [];

        if ($unitId) {
            if ($canBackfillSubject && $subjectId) {
                $payload['subject_id'] = $subjectId;
            }

            $payload['unit_id'] = $unitId;
        }

        if ($topic !== null) {
            $payload['topic'] = $topic;
        }

        if ($subtopic !== null) {
            $payload['subtopic'] = $subtopic;
        }

        if ($editorialStatus !== null) {
            $payload['editorial_status'] = $editorialStatus;
        }

        if ($tags !== []) {
            $payload['tags'] = $this->mergeTags($currentTags ?? [], $tags);
        }

        return $payload;
    }

    private function normalizeString(mixed $value): ?string
    {
        $normalized = trim((string) $value);

        return $normalized !== '' ? $normalized : null;
    }

    /**
     * @param  array<int,string>|mixed  $value
     * @return array<int,string>
     */
    private function normalizeTags(mixed $value): array
    {
        if (! is_array($value)) {
            return [];
        }

        return collect($value)
            ->map(fn ($tag) => trim((string) $tag))
            ->filter()
            ->unique()
            ->values()
            ->all();
    }

    /**
     * @param  array<int,string>  $currentTags
     * @param  array<int,string>  $incomingTags
     * @return array<int,string>
     */
    private function mergeTags(array $currentTags, array $incomingTags): array
    {
        return collect(array_merge($currentTags, $incomingTags))
            ->map(fn ($tag) => trim((string) $tag))
            ->filter()
            ->unique()
            ->values()
            ->all();
    }
}
