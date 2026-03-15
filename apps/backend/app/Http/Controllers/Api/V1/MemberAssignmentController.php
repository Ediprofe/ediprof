<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Models\AssessmentAssignment;
use App\Models\User;
use App\Services\Assessments\AssessmentAssignmentAccessService;
use App\Services\Members\MemberAssignmentPresenter;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class MemberAssignmentController extends Controller
{
    public function index(
        Request $request,
        AssessmentAssignmentAccessService $accessService,
        MemberAssignmentPresenter $presenter,
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
            ->map(fn (AssessmentAssignment $assignment): array => $presenter->present($assignment, $user))
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
        MemberAssignmentPresenter $presenter,
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

        $payload = $presenter->present($assignment, $user);
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
}
