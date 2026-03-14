<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Models\AssessmentAssignment;
use App\Models\AssessmentAttempt;
use App\Models\User;
use App\Services\Assessments\AssessmentAssignmentAccessService;
use App\Services\Assessments\AssessmentAttemptService;
use Carbon\CarbonInterface;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class MemberAssignmentController extends Controller
{
    public function index(
        Request $request,
        AssessmentAssignmentAccessService $accessService,
        AssessmentAttemptService $attemptService
    ): JsonResponse {
        /** @var User $user */
        $user = $request->user();
        $mode = trim((string) $request->query('mode', ''));

        $query = $accessService->accessibleAssignmentsQuery($user)
            ->withCount([
                'questions',
                'attempts as user_attempts_count' => fn ($builder) => $builder->where('user_id', $user->id),
            ])
            ->with([
                'attempts' => fn ($builder) => $builder
                    ->where('user_id', $user->id)
                    ->latest('id'),
            ]);

        if ($mode !== '') {
            $query->where('mode', $mode);
        }

        $items = $query->get()
            ->map(fn (AssessmentAssignment $assignment): array => $this->serializeAssignment($assignment, $user, $accessService, $attemptService))
            ->filter(fn (array $assignment): bool => (bool) $assignment['availability']['can_view'])
            ->values();

        return response()->json([
            'ok' => true,
            'data' => $items,
        ]);
    }

    public function show(
        Request $request,
        string $assignmentId,
        AssessmentAssignmentAccessService $accessService,
        AssessmentAttemptService $attemptService
    ): JsonResponse {
        /** @var User $user */
        $user = $request->user();

        $assignment = $accessService->accessibleAssignmentsQuery($user)
            ->withCount([
                'questions',
                'attempts as user_attempts_count' => fn ($builder) => $builder->where('user_id', $user->id),
            ])
            ->with([
                'attempts' => fn ($builder) => $builder
                    ->where('user_id', $user->id)
                    ->latest('id'),
            ])
            ->where(function ($query) use ($assignmentId): void {
                $identifier = trim(rawurldecode($assignmentId));
                $query->where('external_id', $identifier);
                if (ctype_digit($identifier)) {
                    $query->orWhere('id', (int) $identifier);
                }
            })
            ->first();

        if (! $assignment instanceof AssessmentAssignment) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'assignment_not_found',
                    'message' => 'No se encontró la asignación solicitada.',
                ],
            ], 404);
        }

        $payload = $this->serializeAssignment($assignment, $user, $accessService, $attemptService);
        if (! $payload['availability']['can_view']) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => $payload['availability']['code'] ?? 'assignment_access_denied',
                    'message' => $payload['availability']['message'] ?? 'Tu cuenta no tiene acceso a esta asignación.',
                ],
            ], 403);
        }

        return response()->json([
            'ok' => true,
            'data' => $payload,
        ]);
    }

    /**
     * @return array<string, mixed>
     */
    private function serializeAssignment(
        AssessmentAssignment $assignment,
        User $user,
        AssessmentAssignmentAccessService $accessService,
        AssessmentAttemptService $attemptService
    ): array {
        $availability = $accessService->availability($user, $assignment);
        /** @var AssessmentAttempt|null $latestAttempt */
        $latestAttempt = $assignment->attempts->first();
        $effectiveQuestionCount = $assignment->questions_count > 0
            ? (int) $assignment->questions_count
            : (int) ($assignment->template?->total_questions ?? 0);
        $attemptsUsed = (int) ($assignment->user_attempts_count ?? 0);
        $maxAttempts = $assignment->max_attempts;
        $remainingAttempts = $maxAttempts === null
            ? null
            : max($maxAttempts - $attemptsUsed, 0);
        $feedback = $this->serializeFeedback($assignment, $latestAttempt, $attemptService);

        return [
            'id' => $assignment->external_id,
            'title' => $assignment->title,
            'mode' => $assignment->mode,
            'status' => $assignment->status,
            'randomize_questions' => (bool) $assignment->randomize_questions,
            'max_attempts' => $assignment->max_attempts,
            'time_limit_minutes' => $assignment->time_limit_minutes,
            'opens_at' => $assignment->opens_at?->toIso8601String(),
            'closes_at' => $assignment->closes_at?->toIso8601String(),
            'review_released_at' => $assignment->review_released_at?->toIso8601String(),
            'course' => $assignment->course ? [
                'id' => $assignment->course->id,
                'name' => $assignment->course->name,
                'slug' => $assignment->course->slug,
                'school_year' => $assignment->course->school_year,
            ] : null,
            'template' => $assignment->template ? [
                'id' => $assignment->template->external_id,
                'title' => $assignment->template->title,
                'content_type' => $assignment->template->source_content_type,
                'route' => $assignment->template->route,
            ] : null,
            'stats' => [
                'selected_questions' => (int) $assignment->questions_count,
                'effective_questions' => $effectiveQuestionCount,
            ],
            'attempts' => [
                'used' => $attemptsUsed,
                'limit' => $maxAttempts,
                'remaining' => $remainingAttempts,
            ],
            'feedback' => $feedback,
            'availability' => $availability,
            'latest_attempt' => $latestAttempt ? [
                'id' => $latestAttempt->external_id,
                'status' => $latestAttempt->status,
                'submitted_at' => $latestAttempt->submitted_at?->toIso8601String(),
                'score_percent' => $latestAttempt->score_percent,
                'score_scale' => $latestAttempt->score_scale !== null ? (float) $latestAttempt->score_scale : null,
                'can_review' => $attemptService->canReview($latestAttempt),
                'feedback_state' => $feedback['state'],
                'feedback_state_label' => $feedback['state_label'],
            ] : null,
            'updated_at' => $assignment->updated_at?->toIso8601String(),
        ];
    }

    /**
     * @return array{
     *   policy:string,
     *   policy_label:string,
     *   state:string,
     *   state_label:string,
     *   message:string,
     *   available:bool,
     *   release_at:string|null
     * }
     */
    private function serializeFeedback(
        AssessmentAssignment $assignment,
        ?AssessmentAttempt $latestAttempt,
        AssessmentAttemptService $attemptService
    ): array {
        $policy = $this->resolveFeedbackPolicy($assignment);
        $policyLabel = $this->feedbackPolicyLabel($policy);
        $releaseAt = $assignment->review_released_at;
        $canReview = $latestAttempt instanceof AssessmentAttempt
            ? $attemptService->canReview($latestAttempt)
            : false;
        $hasSubmittedAttempt = $latestAttempt instanceof AssessmentAttempt
            && in_array($latestAttempt->status, ['submitted', 'graded', 'released'], true);

        if ($canReview) {
            return [
                'policy' => $policy,
                'policy_label' => $policyLabel,
                'state' => 'available',
                'state_label' => 'Disponible',
                'message' => 'Ya puedes revisar la respuesta correcta y los conceptos relacionados de esta asignación.',
                'available' => true,
                'release_at' => $releaseAt?->toIso8601String(),
            ];
        }

        if ($policy === 'scheduled') {
            if ($releaseAt instanceof CarbonInterface && $releaseAt->isPast()) {
                return [
                    'policy' => $policy,
                    'policy_label' => $policyLabel,
                    'state' => $hasSubmittedAttempt ? 'available' : 'available_on_submit',
                    'state_label' => $hasSubmittedAttempt ? 'Disponible' : 'Lista al entregar',
                    'message' => $hasSubmittedAttempt
                        ? 'Ya puedes revisar la respuesta correcta y los conceptos relacionados de esta asignación.'
                        : 'Cuando entregues, la retroalimentación quedará disponible de inmediato.',
                    'available' => $hasSubmittedAttempt,
                    'release_at' => $releaseAt->toIso8601String(),
                ];
            }

            return [
                'policy' => $policy,
                'policy_label' => $policyLabel,
                'state' => 'scheduled',
                'state_label' => 'Programada',
                'message' => $hasSubmittedAttempt
                    ? 'Tu resultado ya quedó guardado. La retroalimentación se habilitará '.$this->formatReleaseMoment($releaseAt).'.'
                    : 'Después de entregar, la retroalimentación se habilitará '.$this->formatReleaseMoment($releaseAt).'.',
                'available' => false,
                'release_at' => $releaseAt?->toIso8601String(),
            ];
        }

        if ($policy === 'on_submit') {
            return [
                'policy' => $policy,
                'policy_label' => $policyLabel,
                'state' => 'available_on_submit',
                'state_label' => 'Se muestra al entregar',
                'message' => 'Cuando entregues, verás la respuesta correcta y los conceptos relacionados de inmediato.',
                'available' => false,
                'release_at' => null,
            ];
        }

        if ($policy === 'after_close') {
            return [
                'policy' => $policy,
                'policy_label' => $policyLabel,
                'state' => 'pending_close',
                'state_label' => $hasSubmittedAttempt ? 'Pendiente por cierre' : 'Se habilita al cerrar',
                'message' => $hasSubmittedAttempt
                    ? 'Tu resultado ya quedó guardado. La retroalimentación se habilitará cuando el docente cierre la asignación.'
                    : 'Después de entregar, la retroalimentación se habilitará cuando el docente cierre la asignación.',
                'available' => false,
                'release_at' => null,
            ];
        }

        return [
            'policy' => $policy,
            'policy_label' => $policyLabel,
            'state' => 'pending_teacher',
            'state_label' => $hasSubmittedAttempt ? 'Pendiente por docente' : 'Liberación manual',
            'message' => $hasSubmittedAttempt
                ? 'Tu resultado ya quedó guardado. La retroalimentación se habilitará cuando el docente la libere desde el panel.'
                : 'Después de entregar, la retroalimentación quedará pendiente hasta que el docente la libere desde el panel.',
            'available' => false,
            'release_at' => null,
        ];
    }

    private function resolveFeedbackPolicy(AssessmentAssignment $assignment): string
    {
        if ($assignment->show_feedback_on_submit) {
            return 'on_submit';
        }

        if ($assignment->review_released_at instanceof CarbonInterface) {
            return 'scheduled';
        }

        if ($assignment->show_feedback_after_close) {
            return 'after_close';
        }

        return 'manual';
    }

    private function feedbackPolicyLabel(string $policy): string
    {
        return match ($policy) {
            'on_submit' => 'Retroalimentación al entregar',
            'scheduled' => 'Retroalimentación programada',
            'after_close' => 'Retroalimentación al cerrar',
            default => 'Retroalimentación manual',
        };
    }

    private function formatReleaseMoment(?CarbonInterface $releaseAt): string
    {
        if (! $releaseAt instanceof CarbonInterface) {
            return 'en una fecha programada';
        }

        return 'a partir del '.$releaseAt->format('d/m/Y H:i');
    }
}
