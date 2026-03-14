<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Http\Requests\Api\V1\StartAssessmentAttemptRequest;
use App\Http\Requests\Api\V1\EvaluateWorkshopAnswerRequest;
use App\Http\Resources\WorkshopResource;
use App\Http\Resources\WorkshopSummaryResource;
use App\Models\AssessmentTemplate;
use App\Models\Workshop;
use App\Services\Access\WorkshopAccessService;
use App\Services\Assessments\AssessmentAttemptService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class WorkshopController extends Controller
{
    protected string $contentType = 'taller';

    /**
     * Display paginated workshop catalog entries.
     */
    public function index(Request $request, WorkshopAccessService $accessService): JsonResponse
    {
        $perPage = max(1, min((int) $request->integer('per_page', 20), 100));
        $query = $this->baseQuery();

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
            return $this->contentNotFoundResponse();
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

    public function startAttempt(
        StartAssessmentAttemptRequest $request,
        string $workshopId,
        WorkshopAccessService $accessService,
        AssessmentAttemptService $attemptService
    ): JsonResponse {
        $user = $request->user();
        if (! $user) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'auth_required',
                    'message' => 'Authentication is required to start an attempt.',
                ],
            ], 401);
        }

        $identifier = trim(rawurldecode($workshopId));
        $workshop = $this->resolveWorkshop($request, $identifier);

        if ($workshop === null) {
            return $this->contentNotFoundResponse();
        }

        $accessError = $this->resolveAccessErrorResponse($request, $workshop, $accessService);
        if ($accessError !== null) {
            return $accessError;
        }

        $template = $this->resolveAssessmentTemplate($workshop);
        if (! $template instanceof AssessmentTemplate) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'assessment_template_not_found',
                    'message' => 'No se encontró una plantilla académica sincronizada para este contenido.',
                ],
            ], 409);
        }

        $defaultMode = $this->contentType === 'simulacro' ? 'simulacro' : 'study';
        $requestedMode = (string) ($request->validated('mode') ?? $defaultMode);
        $reset = (bool) ($request->validated('reset') ?? false);

        $attempt = $attemptService->startTemplateAttempt(
            $user,
            $template,
            $requestedMode,
            $reset,
        );

        return response()->json([
            'ok' => true,
            'data' => $attemptService->toClientPayload($attempt),
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
            return $this->contentNotFoundResponse();
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
                    'message' => 'Question not found in the selected content.',
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
                'feedback_html' => (string) ($question['feedback_html'] ?? ''),
                'feedback_summary' => filled($question['feedback_summary'] ?? null) ? (string) $question['feedback_summary'] : null,
                'feedback_assets' => is_array($question['feedback_assets'] ?? null) ? $question['feedback_assets'] : [],
                'feedback_blocks' => is_array($question['feedback_blocks'] ?? null) ? $question['feedback_blocks'] : [],
                'concepts_mdx' => (string) ($question['concepts_mdx'] ?? ''),
                'concepts_html' => (string) ($question['concepts_html'] ?? ''),
                'concepts_summary' => filled($question['concepts_summary'] ?? null) ? (string) $question['concepts_summary'] : null,
                'concepts_assets' => is_array($question['concepts_assets'] ?? null) ? $question['concepts_assets'] : [],
                'concepts_blocks' => is_array($question['concepts_blocks'] ?? null) ? $question['concepts_blocks'] : [],
                'next_question_id' => $nextQuestionId,
            ],
        ]);
    }

    protected function resolveWorkshop(Request $request, string $identifier): ?Workshop
    {
        $query = $this->baseQuery();

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

    protected function baseQuery()
    {
        return Workshop::query()->where('content_type', $this->contentType);
    }

    protected function resolveAccessErrorResponse(
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
                    'message' => 'Authentication is required to access this premium content.',
                ],
            ], 401);
        }

        if (! $accessService->canAccessWorkshop($user, $workshop)) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'premium_access_required',
                    'message' => 'Your account does not have access to this premium content.',
                ],
            ], 403);
        }

        return null;
    }

    protected function resolveAssessmentTemplate(Workshop $workshop): ?AssessmentTemplate
    {
        return AssessmentTemplate::query()
            ->where('source_workshop_id', $workshop->id)
            ->orWhere('external_id', $workshop->external_id)
            ->first();
    }

    protected function contentNotFoundResponse(): JsonResponse
    {
        return response()->json([
            'ok' => false,
            'error' => [
                'code' => 'content_not_found',
                'message' => 'Requested content was not found for the provided identifier.',
            ],
        ], 404);
    }
}
