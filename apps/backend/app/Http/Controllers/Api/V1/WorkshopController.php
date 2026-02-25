<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Http\Requests\Api\V1\EvaluateWorkshopAnswerRequest;
use App\Http\Resources\WorkshopResource;
use App\Http\Resources\WorkshopSummaryResource;
use App\Models\Workshop;
use App\Services\Access\WorkshopAccessService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class WorkshopController extends Controller
{
    /**
     * Display paginated workshop catalog entries.
     */
    public function index(Request $request, WorkshopAccessService $accessService): JsonResponse
    {
        $perPage = max(1, min((int) $request->integer('per_page', 20), 100));
        $query = Workshop::query();

        if ($request->filled('published')) {
            $query->where('is_published', filter_var($request->query('published'), FILTER_VALIDATE_BOOL));
        } else {
            $query->where('is_published', true);
        }

        $query->when(
            $request->filled('access_tier'),
            fn ($builder) => $builder->where('access_tier', (string) $request->query('access_tier'))
        );

        $query->when(
            $request->filled('area_slug'),
            fn ($builder) => $builder->where('area_slug', (string) $request->query('area_slug'))
        );

        $query->when(
            $request->filled('search'),
            fn ($builder) => $builder->where('title', 'like', '%'.$request->query('search').'%')
        );

        $catalog = $query
            ->orderBy('area_slug')
            ->orderBy('unidad_slug')
            ->orderBy('title')
            ->paginate($perPage)
            ->withQueryString();

        $user = $request->user();

        $items = $catalog->getCollection()->map(function (Workshop $workshop) use ($accessService, $user): Workshop {
            $workshop->setAttribute('can_access', $accessService->canAccessWorkshop($user, $workshop));

            return $workshop;
        });

        return response()->json([
            'ok' => true,
            'data' => WorkshopSummaryResource::collection($items),
            'meta' => [
                'current_page' => $catalog->currentPage(),
                'per_page' => $catalog->perPage(),
                'total' => $catalog->total(),
                'last_page' => $catalog->lastPage(),
                'from' => $catalog->firstItem(),
                'to' => $catalog->lastItem(),
            ],
            'links' => [
                'first' => $catalog->url(1),
                'last' => $catalog->url($catalog->lastPage()),
                'prev' => $catalog->previousPageUrl(),
                'next' => $catalog->nextPageUrl(),
            ],
        ]);
    }

    /**
     * Display a workshop by its external id, related content id, or route.
     */
    public function show(Request $request, string $workshopId, WorkshopAccessService $accessService): JsonResponse
    {
        $identifier = trim(rawurldecode($workshopId));
        $workshop = $this->resolveWorkshop($request, $identifier);

        if ($workshop === null) {
            return $this->workshopNotFoundResponse();
        }

        $accessError = $this->resolveAccessErrorResponse($request, $workshop, $accessService);
        if ($accessError !== null) {
            return $accessError;
        }

        return response()->json([
            'ok' => true,
            'data' => new WorkshopResource($workshop),
        ]);
    }

    /**
     * Evaluate a selected option for a specific workshop question.
     */
    public function evaluateAnswer(
        EvaluateWorkshopAnswerRequest $request,
        string $workshopId,
        string $questionId,
        WorkshopAccessService $accessService
    ): JsonResponse {
        $identifier = trim(rawurldecode($workshopId));
        $normalizedQuestionId = trim(rawurldecode($questionId));

        $workshop = $this->resolveWorkshop($request, $identifier);
        if ($workshop === null) {
            return $this->workshopNotFoundResponse();
        }

        $accessError = $this->resolveAccessErrorResponse($request, $workshop, $accessService);
        if ($accessError !== null) {
            return $accessError;
        }

        $questions = is_array($workshop->questions) ? $workshop->questions : [];
        $questionIndex = null;
        $question = null;

        foreach ($questions as $index => $candidate) {
            if (! is_array($candidate)) {
                continue;
            }

            if ((string) ($candidate['id'] ?? '') !== $normalizedQuestionId) {
                continue;
            }

            $questionIndex = $index;
            $question = $candidate;
            break;
        }

        if (! is_array($question)) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'question_not_found',
                    'message' => 'Question not found in the selected workshop.',
                ],
            ], 404);
        }

        $selectedOptionId = (string) $request->validated('option_id');
        $options = is_array($question['options'] ?? null) ? $question['options'] : [];
        $selectedOption = null;
        $correctOption = null;

        foreach ($options as $option) {
            if (! is_array($option)) {
                continue;
            }

            $optionId = (string) ($option['id'] ?? '');

            if ($optionId === $selectedOptionId) {
                $selectedOption = $option;
            }

            if (($option['is_correct'] ?? false) === true) {
                $correctOption = $option;
            }
        }

        if (! is_array($selectedOption)) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'invalid_option',
                    'message' => 'Selected option is not valid for this question.',
                ],
            ], 422);
        }

        $correctOptionId = (string) ($question['correct_option_id'] ?? '');
        if ($correctOptionId === '' && is_array($correctOption)) {
            $correctOptionId = (string) ($correctOption['id'] ?? '');
        }

        $isCorrect = $correctOptionId !== '' && $selectedOptionId === $correctOptionId;
        $nextQuestionId = null;

        if ($questionIndex !== null && isset($questions[$questionIndex + 1]) && is_array($questions[$questionIndex + 1])) {
            $nextQuestionId = (string) ($questions[$questionIndex + 1]['id'] ?? '');
            if ($nextQuestionId === '') {
                $nextQuestionId = null;
            }
        }

        return response()->json([
            'ok' => true,
            'data' => [
                'workshop_id' => $workshop->external_id,
                'question_id' => $normalizedQuestionId,
                'selected_option_id' => $selectedOptionId,
                'correct_option_id' => $correctOptionId !== '' ? $correctOptionId : null,
                'is_correct' => $isCorrect,
                'feedback_mdx' => (string) ($question['feedback_mdx'] ?? ''),
                'feedback_assets' => is_array($question['feedback_assets'] ?? null) ? $question['feedback_assets'] : [],
                'next_question_id' => $nextQuestionId,
            ],
        ]);
    }

    private function resolveWorkshop(Request $request, string $identifier): ?Workshop
    {
        $query = Workshop::query();

        if ($request->boolean('published_only', true)) {
            $query->where('is_published', true);
        }

        return $query
            ->where(function ($builder) use ($identifier): void {
                $builder
                    ->where('external_id', $identifier)
                    ->orWhere('content_external_id', $identifier)
                    ->orWhere('route', $identifier);
            })
            ->first();
    }

    private function resolveAccessErrorResponse(
        Request $request,
        Workshop $workshop,
        WorkshopAccessService $accessService
    ): ?JsonResponse {
        $user = $request->user();
        if ($workshop->access_tier === 'premium' && $user === null) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'auth_required',
                    'message' => 'Authentication is required to access premium workshops.',
                ],
            ], 401);
        }

        if (! $accessService->canAccessWorkshop($user, $workshop)) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'premium_access_required',
                    'message' => 'Your account does not have access to this premium workshop.',
                ],
            ], 403);
        }

        return null;
    }

    private function workshopNotFoundResponse(): JsonResponse
    {
        return response()->json([
            'ok' => false,
            'error' => [
                'code' => 'workshop_not_found',
                'message' => 'Workshop not found for the requested identifier.',
            ],
        ], 404);
    }
}
