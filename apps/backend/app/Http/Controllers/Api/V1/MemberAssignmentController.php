<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Models\AssessmentAssignment;
use App\Models\AssessmentAttempt;
use App\Models\User;
use App\Services\Assessments\AssessmentAssignmentAccessService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class MemberAssignmentController extends Controller
{
    public function index(
        Request $request,
        AssessmentAssignmentAccessService $accessService
    ): JsonResponse {
        /** @var User $user */
        $user = $request->user();
        $mode = trim((string) $request->query('mode', ''));

        $query = $accessService->accessibleAssignmentsQuery($user)
            ->withCount(['questions'])
            ->with([
                'attempts' => fn ($builder) => $builder
                    ->where('user_id', $user->id)
                    ->latest('id'),
            ]);

        if (! $user->isAdmin()) {
            $query->where('status', AssessmentAssignment::STATUS_ACTIVE);
        }

        if ($mode !== '') {
            $query->where('mode', $mode);
        }

        $items = $query->get()
            ->map(fn (AssessmentAssignment $assignment): array => $this->serializeAssignment($assignment, $user, $accessService))
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
        AssessmentAssignmentAccessService $accessService
    ): JsonResponse {
        /** @var User $user */
        $user = $request->user();

        $assignment = $accessService->accessibleAssignmentsQuery($user)
            ->withCount(['questions'])
            ->with([
                'attempts' => fn ($builder) => $builder
                    ->where('user_id', $user->id)
                    ->latest('id'),
            ])
            ->when(! $user->isAdmin(), fn ($query) => $query->where('status', AssessmentAssignment::STATUS_ACTIVE))
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

        $payload = $this->serializeAssignment($assignment, $user, $accessService);
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
        AssessmentAssignmentAccessService $accessService
    ): array {
        $availability = $accessService->availability($user, $assignment);
        /** @var AssessmentAttempt|null $latestAttempt */
        $latestAttempt = $assignment->attempts->first();
        $effectiveQuestionCount = $assignment->questions_count > 0
            ? (int) $assignment->questions_count
            : (int) ($assignment->template?->total_questions ?? 0);

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
            'availability' => $availability,
            'latest_attempt' => $latestAttempt ? [
                'id' => $latestAttempt->external_id,
                'status' => $latestAttempt->status,
                'submitted_at' => $latestAttempt->submitted_at?->toIso8601String(),
                'score_percent' => $latestAttempt->score_percent,
                'score_scale' => $latestAttempt->score_scale !== null ? (float) $latestAttempt->score_scale : null,
                'can_review' => (bool) (($latestAttempt->settings_snapshot['show_feedback_on_submit'] ?? false)
                    || ($latestAttempt->review_released_at && $latestAttempt->review_released_at->isPast())),
            ] : null,
            'updated_at' => $assignment->updated_at?->toIso8601String(),
        ];
    }
}
