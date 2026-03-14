<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Http\Requests\Api\V1\RecordAssessmentAttemptAnswerRequest;
use App\Models\AssessmentAttempt;
use App\Services\Assessments\AssessmentAttemptService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class AssessmentAttemptController extends Controller
{
    public function show(
        Request $request,
        string $attemptId,
        AssessmentAttemptService $attemptService
    ): JsonResponse {
        $attempt = $this->resolveAttempt($request, $attemptId, $attemptService);
        if (! $attempt instanceof AssessmentAttempt) {
            return $this->notFoundResponse();
        }

        return response()->json([
            'ok' => true,
            'data' => $attemptService->toClientPayload($attempt),
        ]);
    }

    public function answer(
        RecordAssessmentAttemptAnswerRequest $request,
        string $attemptId,
        string $questionId,
        AssessmentAttemptService $attemptService
    ): JsonResponse {
        $attempt = $this->resolveAttempt($request, $attemptId, $attemptService);
        if (! $attempt instanceof AssessmentAttempt) {
            return $this->notFoundResponse();
        }

        $result = $attemptService->recordAnswer(
            $attempt,
            trim(rawurldecode($questionId)),
            (string) $request->validated('option_id'),
        );

        return response()->json([
            'ok' => true,
            'data' => $result,
        ]);
    }

    public function submit(
        Request $request,
        string $attemptId,
        AssessmentAttemptService $attemptService
    ): JsonResponse {
        $attempt = $this->resolveAttempt($request, $attemptId, $attemptService);
        if (! $attempt instanceof AssessmentAttempt) {
            return $this->notFoundResponse();
        }

        $submittedAttempt = $attemptService->submit($attempt);

        return response()->json([
            'ok' => true,
            'data' => $attemptService->toClientPayload($submittedAttempt),
        ]);
    }

    private function resolveAttempt(
        Request $request,
        string $attemptId,
        AssessmentAttemptService $attemptService
    ): ?AssessmentAttempt {
        $user = $request->user();
        if (! $user) {
            return null;
        }

        return $attemptService->findAttemptForUser(trim(rawurldecode($attemptId)), $user);
    }

    private function notFoundResponse(): JsonResponse
    {
        return response()->json([
            'ok' => false,
            'error' => [
                'code' => 'attempt_not_found',
                'message' => 'No se encontró el intento solicitado para este usuario.',
            ],
        ], 404);
    }
}
