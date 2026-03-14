<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Http\Requests\Api\V1\StartAssessmentAttemptRequest;
use App\Models\AssessmentAssignment;
use App\Models\User;
use App\Services\Assessments\AssessmentAttemptService;
use Illuminate\Http\JsonResponse;

class AssessmentAssignmentController extends Controller
{
    public function startAttempt(
        StartAssessmentAttemptRequest $request,
        string $assignmentId,
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

        if ($accessError = $this->resolveAccessErrorResponse($user, $assignment)) {
            return $accessError;
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

    private function resolveAccessErrorResponse(User $user, AssessmentAssignment $assignment): ?JsonResponse
    {
        if ($user->isAdmin()) {
            return null;
        }

        if ($assignment->status !== AssessmentAssignment::STATUS_ACTIVE) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'assignment_inactive',
                    'message' => 'Esta asignación todavía no está activa para estudiantes.',
                ],
            ], 403);
        }

        if ($assignment->opens_at && $assignment->opens_at->isFuture()) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'assignment_not_open',
                    'message' => 'La asignación aún no está abierta.',
                ],
            ], 403);
        }

        if ($assignment->closes_at && $assignment->closes_at->isPast()) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'assignment_closed',
                    'message' => 'La asignación ya cerró.',
                ],
            ], 403);
        }

        $course = $assignment->course;
        if (! $course || ! $course->is_active) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'course_inactive',
                    'message' => 'El curso asociado no está disponible.',
                ],
            ], 403);
        }

        $isEnrolled = $course->enrollments()
            ->where('user_id', $user->id)
            ->where('status', 'active')
            ->exists();

        if (! $isEnrolled) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'assignment_access_denied',
                    'message' => 'Tu cuenta no tiene acceso a esta asignación.',
                ],
            ], 403);
        }

        return null;
    }
}
