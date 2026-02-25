<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Http\Resources\WorkshopResource;
use App\Models\Workshop;
use App\Services\Access\WorkshopAccessService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class WorkshopController extends Controller
{
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
