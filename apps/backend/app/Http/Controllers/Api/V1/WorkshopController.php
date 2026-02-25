<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Http\Resources\WorkshopResource;
use App\Models\Workshop;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class WorkshopController extends Controller
{
    /**
     * Display a workshop by its external id, related content id, or route.
     */
    public function show(Request $request, string $workshopId): JsonResponse
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

        return response()->json([
            'ok' => true,
            'data' => new WorkshopResource($workshop),
        ]);
    }
}
