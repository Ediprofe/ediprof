<?php

namespace App\Services\Assessments;

use App\Models\AssessmentAssignment;
use App\Models\AssessmentAttempt;
use App\Models\AssessmentAttemptAnswer;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentTemplate;
use App\Models\User;
use Carbon\CarbonInterface;
use Illuminate\Support\Arr;
use Illuminate\Support\Carbon;
use Illuminate\Support\Collection;
use Illuminate\Validation\ValidationException;

class AssessmentAttemptService
{
    public function startTemplateAttempt(
        User $user,
        AssessmentTemplate $template,
        string $mode,
        bool $reset = false
    ): AssessmentAttempt {
        $normalizedMode = $this->normalizeMode($mode);

        if ($reset) {
            AssessmentAttempt::query()
                ->where('user_id', $user->id)
                ->where('template_id', $template->id)
                ->whereNull('assignment_id')
                ->where('mode', $normalizedMode)
                ->delete();
        }

        $existing = AssessmentAttempt::query()
            ->where('user_id', $user->id)
            ->where('template_id', $template->id)
            ->whereNull('assignment_id')
            ->where('mode', $normalizedMode)
            ->latest('id')
            ->first();

        if ($existing instanceof AssessmentAttempt) {
            return $existing->loadMissing(['template', 'assignment', 'answers']);
        }

        $questions = $this->resolveTemplateQuestions($template);
        $snapshot = $this->buildQuestionsSnapshot($questions);
        $questionOrder = array_map(static fn (array $question): string => (string) $question['id'], $snapshot);

        $attempt = AssessmentAttempt::query()->create([
            'assignment_id' => null,
            'template_id' => $template->id,
            'user_id' => $user->id,
            'mode' => $normalizedMode,
            'status' => 'in_progress',
            'question_order' => $questionOrder,
            'questions_snapshot' => $snapshot,
            'total_questions' => count($snapshot),
            'started_at' => now(),
            'last_activity_at' => now(),
            'settings_snapshot' => $this->buildTemplateSettingsSnapshot($template, $normalizedMode),
            'meta' => [
                'source' => 'template',
                'template_external_id' => $template->external_id,
            ],
        ]);

        return $attempt->loadMissing(['template', 'assignment', 'answers']);
    }

    public function startAssignmentAttempt(
        User $user,
        AssessmentAssignment $assignment,
        bool $reset = false
    ): AssessmentAttempt {
        if ($reset) {
            AssessmentAttempt::query()
                ->where('user_id', $user->id)
                ->where('assignment_id', $assignment->id)
                ->delete();
        }

        $existing = AssessmentAttempt::query()
            ->where('user_id', $user->id)
            ->where('assignment_id', $assignment->id)
            ->latest('id')
            ->first();

        if ($existing instanceof AssessmentAttempt) {
            return $existing->loadMissing(['template', 'assignment', 'answers']);
        }

        $questions = $this->resolveAssignmentQuestions($assignment);
        $snapshot = $this->buildQuestionsSnapshot($questions);
        $questionOrder = array_map(static fn (array $question): string => (string) $question['id'], $snapshot);

        if ($assignment->randomize_questions) {
            $seed = crc32($user->id.'|'.$assignment->external_id.'|'.now()->timestamp);
            $questionOrder = $this->shuffleQuestionOrder($questionOrder, $seed);
            $snapshot = $this->reorderSnapshot($snapshot, $questionOrder);
        }

        $attempt = AssessmentAttempt::query()->create([
            'assignment_id' => $assignment->id,
            'template_id' => $assignment->template_id,
            'user_id' => $user->id,
            'mode' => $this->normalizeMode((string) $assignment->mode),
            'status' => 'in_progress',
            'question_order' => $questionOrder,
            'questions_snapshot' => $snapshot,
            'total_questions' => count($snapshot),
            'started_at' => now(),
            'last_activity_at' => now(),
            'settings_snapshot' => $this->buildAssignmentSettingsSnapshot($assignment),
            'meta' => [
                'source' => 'assignment',
                'assignment_external_id' => $assignment->external_id,
            ],
        ]);

        return $attempt->loadMissing(['template', 'assignment', 'answers']);
    }

    public function recordAnswer(
        AssessmentAttempt $attempt,
        string $questionExternalId,
        string $selectedOptionId
    ): array {
        $attempt = $attempt->loadMissing(['template', 'assignment', 'answers']);
        $this->assertAttemptWritable($attempt);

        $question = $this->findSnapshotQuestion($attempt, $questionExternalId);
        if ($question === null) {
            throw ValidationException::withMessages([
                'question_id' => 'La pregunta seleccionada no existe en este intento.',
            ]);
        }

        $options = is_array($question['options'] ?? null) ? $question['options'] : [];
        $optionIds = array_values(array_filter(array_map(
            static fn (array $option): string => trim((string) ($option['id'] ?? '')),
            $options
        )));

        if (! in_array($selectedOptionId, $optionIds, true)) {
            throw ValidationException::withMessages([
                'option_id' => 'La opción seleccionada no es válida para esta pregunta.',
            ]);
        }

        $position = $this->resolveQuestionPosition($attempt, $questionExternalId);
        $isCorrect = filled($question['correct_option_id'] ?? null)
            ? (string) $question['correct_option_id'] === $selectedOptionId
            : null;

        $answer = AssessmentAttemptAnswer::query()->updateOrCreate(
            [
                'attempt_id' => $attempt->id,
                'question_external_id' => $questionExternalId,
            ],
            [
                'question_id' => $this->resolveQuestionModelId($attempt, $questionExternalId),
                'position' => $position,
                'selected_option_id' => $selectedOptionId,
                'is_correct' => $isCorrect,
                'answered_at' => now(),
                'meta' => [],
            ],
        );

        $attempt->forceFill([
            'last_activity_at' => now(),
        ])->save();

        return $this->serializeAnswerForClient(
            $attempt->fresh(['template', 'assignment', 'answers']),
            $question,
            $answer,
            $this->canRevealQuestionImmediately($attempt),
        );
    }

    public function submit(AssessmentAttempt $attempt): AssessmentAttempt
    {
        $attempt = $attempt->loadMissing(['template', 'assignment', 'answers']);

        if ($attempt->status === 'submitted' || $attempt->status === 'graded' || $attempt->status === 'released') {
            return $attempt;
        }

        $snapshot = $this->snapshotMap($attempt);
        $answers = $attempt->answers->keyBy('question_external_id');
        $scoreRaw = 0;

        foreach ($attempt->question_order ?? [] as $questionExternalId) {
            $question = $snapshot->get($questionExternalId);
            if (! is_array($question)) {
                continue;
            }

            $answer = $answers->get($questionExternalId);
            $selectedOptionId = $answer?->selected_option_id;
            $isCorrect = filled($question['correct_option_id'] ?? null)
                && filled($selectedOptionId)
                && (string) $question['correct_option_id'] === (string) $selectedOptionId;

            if ($answer instanceof AssessmentAttemptAnswer) {
                $answer->forceFill([
                    'is_correct' => $isCorrect,
                ])->save();
            }

            if ($isCorrect) {
                $scoreRaw++;
            }
        }

        $totalQuestions = max((int) $attempt->total_questions, 0);
        $scorePercent = $totalQuestions > 0 ? (int) round(($scoreRaw / $totalQuestions) * 100) : 0;
        $scoreScale = $totalQuestions > 0 ? round(($scoreRaw / $totalQuestions) * 5, 2) : 0;

        $attempt->forceFill([
            'status' => 'submitted',
            'score_raw' => $scoreRaw,
            'score_percent' => $scorePercent,
            'score_scale' => $scoreScale,
            'submitted_at' => now(),
            'graded_at' => now(),
            'review_released_at' => $this->shouldRevealReviewOnSubmit($attempt) ? now() : null,
            'last_activity_at' => now(),
        ])->save();

        return $attempt->fresh(['template', 'assignment', 'answers']);
    }

    /**
     * @return array<string, mixed>
     */
    public function toClientPayload(AssessmentAttempt $attempt): array
    {
        $attempt = $attempt->loadMissing(['template', 'assignment', 'answers']);
        $template = $attempt->template;

        if (! $template instanceof AssessmentTemplate) {
            throw ValidationException::withMessages([
                'attempt' => 'El intento no tiene plantilla académica asociada.',
            ]);
        }

        $answers = $attempt->answers->keyBy('question_external_id');
        $canRevealAll = $this->canRevealAll($attempt);
        $questionPayloads = [];
        $selectedByQuestion = [];
        $evaluationByQuestion = [];

        foreach ($attempt->questions_snapshot ?? [] as $index => $snapshotQuestion) {
            if (! is_array($snapshotQuestion)) {
                continue;
            }

            $questionId = (string) ($snapshotQuestion['id'] ?? '');
            if ($questionId === '') {
                continue;
            }

            $answer = $answers->get($questionId);
            if ($answer instanceof AssessmentAttemptAnswer && filled($answer->selected_option_id)) {
                $selectedByQuestion[$questionId] = (string) $answer->selected_option_id;
            }

            $questionPayloads[] = $this->serializeQuestionForClient(
                $snapshotQuestion,
                $canRevealAll,
                $index + 1,
            );

            if ($attempt->mode === 'study' && $answer instanceof AssessmentAttemptAnswer) {
                $evaluationByQuestion[$questionId] = $this->serializeAnswerForClient($attempt, $snapshotQuestion, $answer, true);
                continue;
            }

            if ($canRevealAll) {
                $evaluationByQuestion[$questionId] = $this->serializeAnswerForClient($attempt, $snapshotQuestion, $answer, true);
            }
        }

        return [
            'id' => $template->external_id,
            'content_external_id' => $template->external_id,
            'content_type' => $template->source_content_type,
            'title' => $attempt->assignment?->title ?: $template->title,
            'route' => $template->route,
            'area_slug' => $template->area_slug,
            'unidad_slug' => $template->unidad_slug,
            'stats' => [
                'total_questions' => count($questionPayloads),
                'total_assets' => (int) $template->total_assets,
            ],
            'assets' => $template->assets ?? [],
            'attempt' => [
                'id' => $attempt->external_id,
                'mode' => $attempt->mode,
                'status' => $attempt->status,
                'submitted' => in_array($attempt->status, ['submitted', 'graded', 'released'], true),
                'can_review' => $canRevealAll,
                'total_questions' => $attempt->total_questions,
                'score_raw' => $attempt->score_raw,
                'score_percent' => $attempt->score_percent,
                'score_scale' => $attempt->score_scale !== null ? (float) $attempt->score_scale : null,
                'started_at' => $attempt->started_at?->toIso8601String(),
                'submitted_at' => $attempt->submitted_at?->toIso8601String(),
                'graded_at' => $attempt->graded_at?->toIso8601String(),
                'review_released_at' => $attempt->review_released_at?->toIso8601String(),
            ],
            'questions' => $questionPayloads,
            'selected_by_question' => $selectedByQuestion,
            'evaluation_by_question' => $evaluationByQuestion,
            'updated_at' => $attempt->updated_at?->toIso8601String(),
        ];
    }

    public function findAttemptForUser(string $externalId, User $user): ?AssessmentAttempt
    {
        return AssessmentAttempt::query()
            ->where('external_id', $externalId)
            ->where('user_id', $user->id)
            ->first();
    }

    private function resolveTemplateQuestions(AssessmentTemplate $template): Collection
    {
        return $template->questions()
            ->where('is_active', true)
            ->with([
                'contexts' => fn ($query) => $query
                    ->where('assessment_contexts.is_active', true)
                    ->orderBy('assessment_question_contexts.order_base'),
            ])
            ->orderBy('order_base')
            ->get();
    }

    private function resolveAssignmentQuestions(AssessmentAssignment $assignment): Collection
    {
        $assignment->loadMissing(['questions.question.contexts', 'template']);

        if ($assignment->questions->isNotEmpty()) {
            return $assignment->questions
                ->sortBy('order_base')
                ->map(static fn ($assignmentQuestion) => $assignmentQuestion->question)
                ->filter()
                ->values();
        }

        if ($assignment->template instanceof AssessmentTemplate) {
            return $this->resolveTemplateQuestions($assignment->template);
        }

        return new Collection();
    }

    /**
     * @param  Collection<int, AssessmentQuestion>  $questions
     * @return array<int, array<string, mixed>>
     */
    private function buildQuestionsSnapshot(Collection $questions): array
    {
        return $questions
            ->values()
            ->map(function (AssessmentQuestion $question): array {
                $contexts = $question->contexts
                    ->sortBy(fn ($context) => (int) ($context->pivot->order_base ?? $context->order_base ?? 1))
                    ->values();

                $contextIds = $contexts
                    ->map(static fn ($context): string => (string) $context->external_id)
                    ->filter()
                    ->values()
                    ->all();

                $contextHtml = $contexts
                    ->map(static fn ($context): string => (string) ($context->context_html ?? ''))
                    ->filter()
                    ->implode("\n");

                $contextMdx = $contexts
                    ->map(static fn ($context): string => (string) ($context->context_mdx ?? ''))
                    ->filter()
                    ->implode("\n\n");

                $contextAssets = $contexts
                    ->flatMap(static fn ($context): array => is_array($context->context_assets) ? $context->context_assets : [])
                    ->unique()
                    ->values()
                    ->all();

                $contextBlocks = $contexts
                    ->flatMap(static fn ($context): array => is_array($context->context_blocks) ? $context->context_blocks : [])
                    ->values()
                    ->all();

                return [
                    'id' => $question->external_id,
                    'order' => $question->order_base,
                    'order_base' => $question->order_base,
                    'source_slug' => $question->source_slug,
                    'meta' => $question->meta ?? [],
                    'context_ids' => $contextIds,
                    'context_mdx' => $contextMdx,
                    'context_html' => $contextHtml,
                    'context_assets' => $contextAssets,
                    'context_blocks' => $contextBlocks,
                    'stem_mdx' => (string) ($question->stem_mdx ?? ''),
                    'stem_html' => (string) ($question->stem_html ?? ''),
                    'stem_assets' => $question->stem_assets ?? [],
                    'stem_blocks' => $question->stem_blocks ?? [],
                    'options' => $question->options ?? [],
                    'correct_option_id' => $question->correct_option_id,
                    'feedback_mdx' => (string) ($question->feedback_mdx ?? ''),
                    'feedback_html' => (string) ($question->feedback_html ?? ''),
                    'feedback_summary' => $question->feedback_summary,
                    'feedback_assets' => $question->feedback_assets ?? [],
                    'feedback_blocks' => $question->feedback_blocks ?? [],
                    'concepts_mdx' => (string) ($question->concepts_mdx ?? ''),
                    'concepts_html' => (string) ($question->concepts_html ?? ''),
                    'concepts_summary' => $question->concepts_summary,
                    'concepts_assets' => $question->concepts_assets ?? [],
                    'concepts_blocks' => $question->concepts_blocks ?? [],
                    'app_payload_version' => $question->app_payload_version,
                ];
            })
            ->all();
    }

    /**
     * @param  array<int, string>  $questionOrder
     * @return array<int, string>
     */
    private function shuffleQuestionOrder(array $questionOrder, int $seed): array
    {
        $scored = array_map(static function (string $questionId) use ($seed): array {
            return [
                'id' => $questionId,
                'score' => crc32($seed.'|'.$questionId),
            ];
        }, $questionOrder);

        usort($scored, static fn (array $a, array $b): int => $a['score'] <=> $b['score']);

        return array_values(array_map(static fn (array $item): string => $item['id'], $scored));
    }

    /**
     * @param  array<int, array<string, mixed>>  $snapshot
     * @param  array<int, string>  $questionOrder
     * @return array<int, array<string, mixed>>
     */
    private function reorderSnapshot(array $snapshot, array $questionOrder): array
    {
        $snapshotMap = [];
        foreach ($snapshot as $question) {
            if (! is_array($question)) {
                continue;
            }

            $questionId = (string) ($question['id'] ?? '');
            if ($questionId === '') {
                continue;
            }

            $snapshotMap[$questionId] = $question;
        }

        $ordered = [];
        foreach ($questionOrder as $position => $questionId) {
            $question = $snapshotMap[$questionId] ?? null;
            if (! is_array($question)) {
                continue;
            }

            $question['order'] = $position + 1;
            $ordered[] = $question;
        }

        return $ordered;
    }

    private function assertAttemptWritable(AssessmentAttempt $attempt): void
    {
        if (in_array($attempt->status, ['submitted', 'graded', 'released', 'expired'], true)) {
            throw ValidationException::withMessages([
                'attempt' => 'Este intento ya no admite nuevas respuestas.',
            ]);
        }
    }

    /**
     * @return array<string, mixed>|null
     */
    private function findSnapshotQuestion(AssessmentAttempt $attempt, string $questionExternalId): ?array
    {
        foreach ($attempt->questions_snapshot ?? [] as $question) {
            if (! is_array($question)) {
                continue;
            }

            if ((string) ($question['id'] ?? '') === $questionExternalId) {
                return $question;
            }
        }

        return null;
    }

    private function resolveQuestionModelId(AssessmentAttempt $attempt, string $questionExternalId): ?int
    {
        return AssessmentQuestion::query()
            ->where('template_id', $attempt->template_id)
            ->where('external_id', $questionExternalId)
            ->value('id');
    }

    private function resolveQuestionPosition(AssessmentAttempt $attempt, string $questionExternalId): int
    {
        $order = $attempt->question_order ?? [];
        $index = array_search($questionExternalId, $order, true);

        return $index === false ? 1 : ($index + 1);
    }

    private function snapshotMap(AssessmentAttempt $attempt): \Illuminate\Support\Collection
    {
        return collect($attempt->questions_snapshot ?? [])
            ->filter(static fn ($question): bool => is_array($question) && filled($question['id'] ?? null))
            ->keyBy(static fn (array $question): string => (string) $question['id']);
    }

    private function canRevealQuestionImmediately(AssessmentAttempt $attempt): bool
    {
        return $attempt->mode === 'study';
    }

    private function canRevealAll(AssessmentAttempt $attempt): bool
    {
        if ($attempt->mode === 'study') {
            return false;
        }

        if (! in_array($attempt->status, ['submitted', 'graded', 'released'], true)) {
            return false;
        }

        if ($this->shouldRevealReviewOnSubmit($attempt)) {
            return true;
        }

        $reviewReleasedAt = $attempt->review_released_at;
        if ($reviewReleasedAt instanceof CarbonInterface) {
            return $reviewReleasedAt->lessThanOrEqualTo(now());
        }

        return false;
    }

    private function shouldRevealReviewOnSubmit(AssessmentAttempt $attempt): bool
    {
        $settings = is_array($attempt->settings_snapshot) ? $attempt->settings_snapshot : [];

        return (bool) ($settings['show_feedback_on_submit'] ?? false);
    }

    /**
     * @param  array<string, mixed>  $snapshotQuestion
     * @return array<string, mixed>
     */
    private function serializeQuestionForClient(array $snapshotQuestion, bool $includeReviewFields, int $position): array
    {
        $payload = $snapshotQuestion;
        $payload['order'] = $position;

        if (! $includeReviewFields) {
            $payload['correct_option_id'] = null;
            $payload['feedback_mdx'] = '';
            $payload['feedback_html'] = '';
            $payload['feedback_summary'] = null;
            $payload['feedback_assets'] = [];
            $payload['feedback_blocks'] = [];
            $payload['concepts_mdx'] = '';
            $payload['concepts_html'] = '';
            $payload['concepts_summary'] = null;
            $payload['concepts_assets'] = [];
            $payload['concepts_blocks'] = [];
            $payload['options'] = array_map(static function (array $option): array {
                unset($option['is_correct']);

                return $option;
            }, is_array($payload['options'] ?? null) ? $payload['options'] : []);
        }

        unset($payload['meta']);

        return $payload;
    }

    /**
     * @param  array<string, mixed>  $snapshotQuestion
     * @return array<string, mixed>
     */
    private function serializeAnswerForClient(
        AssessmentAttempt $attempt,
        array $snapshotQuestion,
        ?AssessmentAttemptAnswer $answer,
        bool $includeReviewFields
    ): array {
        $selectedOptionId = $answer?->selected_option_id;
        $correctOptionId = filled($snapshotQuestion['correct_option_id'] ?? null)
            ? (string) $snapshotQuestion['correct_option_id']
            : null;
        $isCorrect = $selectedOptionId !== null && $correctOptionId !== null
            ? $selectedOptionId === $correctOptionId
            : false;

        return [
            'attempt_id' => $attempt->external_id,
            'question_id' => (string) ($snapshotQuestion['id'] ?? ''),
            'selected_option_id' => $selectedOptionId,
            'correct_option_id' => $includeReviewFields ? $correctOptionId : null,
            'is_correct' => $includeReviewFields ? $isCorrect : null,
            'feedback_mdx' => $includeReviewFields ? (string) ($snapshotQuestion['feedback_mdx'] ?? '') : '',
            'feedback_html' => $includeReviewFields ? (string) ($snapshotQuestion['feedback_html'] ?? '') : '',
            'feedback_summary' => $includeReviewFields
                ? (filled($snapshotQuestion['feedback_summary'] ?? null) ? (string) $snapshotQuestion['feedback_summary'] : null)
                : null,
            'feedback_blocks' => $includeReviewFields ? (is_array($snapshotQuestion['feedback_blocks'] ?? null) ? $snapshotQuestion['feedback_blocks'] : []) : [],
            'concepts_mdx' => $includeReviewFields ? (string) ($snapshotQuestion['concepts_mdx'] ?? '') : '',
            'concepts_html' => $includeReviewFields ? (string) ($snapshotQuestion['concepts_html'] ?? '') : '',
            'concepts_summary' => $includeReviewFields
                ? (filled($snapshotQuestion['concepts_summary'] ?? null) ? (string) $snapshotQuestion['concepts_summary'] : null)
                : null,
            'concepts_blocks' => $includeReviewFields ? (is_array($snapshotQuestion['concepts_blocks'] ?? null) ? $snapshotQuestion['concepts_blocks'] : []) : [],
        ];
    }

    /**
     * @return array<string, mixed>
     */
    private function buildTemplateSettingsSnapshot(AssessmentTemplate $template, string $mode): array
    {
        return [
            'source' => 'template',
            'template_external_id' => $template->external_id,
            'content_type' => $template->source_content_type,
            'randomize_questions' => false,
            'show_feedback_on_submit' => $mode === 'simulacro',
            'show_feedback_after_close' => false,
            'review_release_policy' => $mode === 'study' ? 'immediate' : 'on_submit',
        ];
    }

    /**
     * @return array<string, mixed>
     */
    private function buildAssignmentSettingsSnapshot(AssessmentAssignment $assignment): array
    {
        return [
            'source' => 'assignment',
            'assignment_external_id' => $assignment->external_id,
            'randomize_questions' => (bool) $assignment->randomize_questions,
            'show_feedback_on_submit' => (bool) $assignment->show_feedback_on_submit,
            'show_feedback_after_close' => (bool) $assignment->show_feedback_after_close,
            'opens_at' => $assignment->opens_at?->toIso8601String(),
            'closes_at' => $assignment->closes_at?->toIso8601String(),
            'review_released_at' => $assignment->review_released_at?->toIso8601String(),
        ];
    }

    private function normalizeMode(string $mode): string
    {
        $normalized = strtolower(trim($mode));

        return match ($normalized) {
            'exam' => 'simulacro',
            'study' => 'study',
            'evaluation' => 'evaluation',
            default => 'simulacro',
        };
    }
}
