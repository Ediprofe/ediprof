<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Http\Requests\Api\V1\StartAssessmentAttemptRequest;
use App\Models\AssessmentAssignment;
use App\Models\AssessmentAttempt;
use App\Models\User;
use App\Services\Assessments\AssessmentAssignmentAccessService;
use App\Services\Assessments\AssessmentAttemptService;
use Illuminate\Http\JsonResponse;

class AssessmentAssignmentController extends Controller
{
    public function startAttempt(
        StartAssessmentAttemptRequest $request,
        string $assignmentId,
        AssessmentAssignmentAccessService $accessService,
        AssessmentAttemptService $attemptService
    ): JsonResponse {
        /** @var User|null $user */
        $user = $request->user();
        if (! $user) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'auth_required',
                    'message' => 'Authentication is required to start an assignment.',
                ],
            ], 401);
        }

        $assignment = $this->resolveAssignment(trim(rawurldecode($assignmentId)));
        if (! $assignment instanceof AssessmentAssignment) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'assignment_not_found',
                    'message' => 'No se encontró la asignación solicitada.',
                ],
            ], 404);
        }

        $latestAttempt = AssessmentAttempt::query()
            ->where('user_id', $user->id)
            ->where('assignment_id', $assignment->id)
            ->latest('id')
            ->first();

        if ($accessError = $this->resolveAccessErrorResponse($user, $assignment, $accessService, $latestAttempt)) {
            return $accessError;
        }

        if ($latestAttempt instanceof AssessmentAttempt && ! $accessService->availability($user, $assignment)['can_start']) {
            return response()->json([
                'ok' => true,
                'data' => $attemptService->toClientPayload($latestAttempt),
            ]);
        }

        $reset = (bool) ($request->validated('reset') ?? false);
        $attempt = $attemptService->startAssignmentAttempt($user, $assignment, $reset);

        return response()->json([
            'ok' => true,
            'data' => $attemptService->toClientPayload($attempt),
        ]);
    }

    private function resolveAssignment(string $identifier): ?AssessmentAssignment
    {
        return AssessmentAssignment::query()
            ->with(['course', 'template'])
            ->where('external_id', $identifier)
            ->orWhere(function ($query) use ($identifier): void {
                if (ctype_digit($identifier)) {
                    $query->where('id', (int) $identifier);
                }
            })
            ->first();
    }

    private function resolveAccessErrorResponse(
        User $user,
        AssessmentAssignment $assignment,
        AssessmentAssignmentAccessService $accessService,
        ?AssessmentAttempt $latestAttempt = null
    ): ?JsonResponse {
        $availability = $accessService->availability($user, $assignment);
        if ($availability['can_start'] || $latestAttempt instanceof AssessmentAttempt) {
            return null;
        }

        return response()->json([
            'ok' => false,
            'error' => [
                'code' => $availability['code'] ?? 'assignment_access_denied',
                'message' => $availability['message'] ?? 'Tu cuenta no tiene acceso a esta asignación.',
            ],
        ], 403);
    }
}
