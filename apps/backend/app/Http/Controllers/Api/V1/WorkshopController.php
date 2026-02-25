<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
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

        $query = Workshop::query();

        if ($request->boolean('published_only', true)) {
            $query->where('is_published', true);
        }

        $workshop = $query
            ->where(function ($builder) use ($identifier): void {
                $builder
                    ->where('external_id', $identifier)
                    ->orWhere('content_external_id', $identifier)
                    ->orWhere('route', $identifier);
            })
            ->first();

        if ($workshop === null) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'workshop_not_found',
                    'message' => 'Workshop not found for the requested identifier.',
                ],
            ], 404);
        }

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

        return response()->json([
            'ok' => true,
            'data' => new WorkshopResource($workshop),
        ]);
    }
}
