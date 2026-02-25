<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Http\Resources\ContentCatalogResource;
use App\Models\ContentCatalog;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class ContentController extends Controller
{
    /**
     * Display paginated content catalog entries.
     */
    public function index(Request $request): JsonResponse
    {
        $perPage = max(1, min((int) $request->integer('per_page', 20), 100));

        $query = ContentCatalog::query();

        $query->when(
            $request->filled('published'),
            fn ($builder) => $builder->where('is_published', filter_var($request->query('published'), FILTER_VALIDATE_BOOL))
        );

        $query->when(
            $request->filled('access_tier'),
            fn ($builder) => $builder->where('access_tier', (string) $request->query('access_tier'))
        );

        $query->when(
            $request->filled('content_type'),
            fn ($builder) => $builder->where('content_type', (string) $request->query('content_type'))
        );

        $query->when(
            $request->filled('area_slug'),
            fn ($builder) => $builder->where('area_slug', (string) $request->query('area_slug'))
        );

        $query->when(
            $request->filled('collection'),
            fn ($builder) => $builder->where('collection', (string) $request->query('collection'))
        );

        $query->when(
            $request->filled('search'),
            fn ($builder) => $builder->where(fn ($inner) => $inner
                ->where('title', 'like', '%'.$request->query('search').'%')
                ->orWhere('description', 'like', '%'.$request->query('search').'%')
            )
        );

        $catalog = $query
            ->orderBy('area_slug')
            ->orderBy('unidad_slug')
            ->orderBy('tema_slug')
            ->orderByRaw('sort_order IS NULL')
            ->orderBy('sort_order')
            ->orderBy('title')
            ->paginate($perPage)
            ->withQueryString();

        return response()->json([
            'ok' => true,
            'data' => ContentCatalogResource::collection($catalog->getCollection()),
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
}
