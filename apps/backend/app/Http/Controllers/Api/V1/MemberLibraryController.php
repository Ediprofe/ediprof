<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Http\Resources\WorkshopSummaryResource;
use App\Models\Course;
use App\Models\User;
use App\Models\Workshop;
use App\Services\Access\CourseLibraryService;
use App\Services\Access\WorkshopAccessService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Collection;

class MemberLibraryController extends Controller
{
    public function courses(Request $request, CourseLibraryService $courseLibraryService): JsonResponse
    {
        /** @var User $user */
        $user = $request->user();
        $courses = $courseLibraryService->accessibleCourses($user);

        $data = $courses->map(function (Course $course): array {
            $contentCount = $course->contents()
                ->where('is_active', true)
                ->count();

            $tallerCount = $course->contents()
                ->where('is_active', true)
                ->whereHas('workshop', function ($builder): void {
                    $builder->where('content_type', 'taller');
                })
                ->count();

            $simulacroCount = $course->contents()
                ->where('is_active', true)
                ->whereHas('workshop', function ($builder): void {
                    $builder->where('content_type', 'simulacro');
                })
                ->count();

            return [
                'id' => $course->id,
                'name' => $course->name,
                'slug' => $course->slug,
                'school_year' => $course->school_year,
                'is_active' => (bool) $course->is_active,
                'notes' => $course->notes,
                'stats' => [
                    'contents' => $contentCount,
                    'talleres' => $tallerCount,
                    'simulacros' => $simulacroCount,
                ],
            ];
        })->values();

        return response()->json([
            'ok' => true,
            'data' => $data,
        ]);
    }

    public function library(
        Request $request,
        CourseLibraryService $courseLibraryService,
        WorkshopAccessService $accessService
    ): JsonResponse {
        /** @var User $user */
        $user = $request->user();
        $perPage = max(1, min((int) $request->integer('per_page', 60), 100));
        $contentType = trim((string) $request->query('content_type', ''));

        $query = $user->isAdmin()
            ? Workshop::query()
            : $courseLibraryService->accessibleWorkshopsQuery($user, $contentType !== '' ? $contentType : null);

        if ($user->isAdmin() && $contentType !== '') {
            $query->where('content_type', $contentType);
        }

        if ($request->filled('published')) {
            $query->where('is_published', filter_var($request->query('published'), FILTER_VALIDATE_BOOL));
        } else {
            $query->where('is_published', true);
        }

        $search = trim((string) $request->query('search', ''));
        if ($search !== '') {
            $query->where('title', 'like', '%'.$search.'%');
        }

        $catalog = $query
            ->orderBy('area_slug')
            ->orderBy('unidad_slug')
            ->orderBy('title')
            ->paginate($perPage)
            ->withQueryString();

        /** @var Collection<int, Workshop> $items */
        $items = $catalog->getCollection();
        $courseMap = $courseLibraryService->workshopCourseMap($user, $items);

        $items = $items->map(function (Workshop $workshop) use ($accessService, $courseMap, $user): Workshop {
            $workshop->setAttribute('can_access', $accessService->canAccessWorkshop($user, $workshop));
            $workshop->setAttribute('course_names', $courseMap[$workshop->id] ?? []);

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
}
