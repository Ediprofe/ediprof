<?php

namespace App\Http\Controllers\Api\V1\Admin;

use App\Http\Controllers\Controller;
use App\Http\Resources\WorkshopSummaryResource;
use App\Models\Course;
use App\Models\CourseContent;
use App\Models\Workshop;
use App\Services\Courses\CourseEnrollmentImportService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;
use Illuminate\Support\Str;

class CourseController extends Controller
{
    public function __construct(
        protected CourseEnrollmentImportService $enrollmentImportService,
    ) {}

    public function index(): JsonResponse
    {
        $courses = Course::query()
            ->orderBy('name')
            ->get()
            ->map(fn (Course $course): array => $this->coursePayload($course));

        return response()->json([
            'ok' => true,
            'data' => $courses,
        ]);
    }

    public function store(Request $request): JsonResponse
    {
        $validated = Validator::make($request->all(), [
            'name' => ['required', 'string', 'min:3', 'max:120'],
            'slug' => ['nullable', 'string', 'max:120'],
            'school_year' => ['nullable', 'string', 'max:20'],
            'is_active' => ['nullable', 'boolean'],
            'notes' => ['nullable', 'string', 'max:1000'],
        ])->validate();

        $slug = Course::resolveUniqueSlug(
            trim((string) ($validated['slug'] ?? '')) !== '' ? (string) $validated['slug'] : Str::slug((string) $validated['name'])
        );

        $course = Course::query()->create([
            'name' => trim((string) $validated['name']),
            'slug' => $slug,
            'school_year' => filled($validated['school_year'] ?? null) ? trim((string) $validated['school_year']) : null,
            'is_active' => (bool) ($validated['is_active'] ?? true),
            'notes' => filled($validated['notes'] ?? null) ? trim((string) $validated['notes']) : null,
        ]);

        return response()->json([
            'ok' => true,
            'data' => $this->coursePayload($course),
        ], 201);
    }

    public function update(Request $request, int $courseId): JsonResponse
    {
        $course = Course::query()->findOrFail($courseId);

        $validated = Validator::make($request->all(), [
            'name' => ['required', 'string', 'min:3', 'max:120'],
            'slug' => ['nullable', 'string', 'max:120'],
            'school_year' => ['nullable', 'string', 'max:20'],
            'is_active' => ['nullable', 'boolean'],
            'notes' => ['nullable', 'string', 'max:1000'],
        ])->validate();

        $requestedSlug = trim((string) ($validated['slug'] ?? '')) !== '' ? (string) $validated['slug'] : Str::slug((string) $validated['name']);
        $slug = Course::resolveUniqueSlug($requestedSlug, $course->id);

        $course->forceFill([
            'name' => trim((string) $validated['name']),
            'slug' => $slug,
            'school_year' => filled($validated['school_year'] ?? null) ? trim((string) $validated['school_year']) : null,
            'is_active' => array_key_exists('is_active', $validated) ? (bool) $validated['is_active'] : $course->is_active,
            'notes' => filled($validated['notes'] ?? null) ? trim((string) $validated['notes']) : null,
        ])->save();

        return response()->json([
            'ok' => true,
            'data' => $this->coursePayload($course->refresh()),
        ]);
    }

    public function importEnrollments(Request $request, int $courseId): JsonResponse
    {
        $course = Course::query()->findOrFail($courseId);

        $validated = Validator::make($request->all(), [
            'csv' => ['required', 'file', 'mimetypes:text/plain,text/csv,text/tsv,application/csv,application/vnd.ms-excel'],
        ])->validate();

        $result = $this->enrollmentImportService->importFromUploadedFile($course, $validated['csv']);

        return response()->json([
            'ok' => true,
            'data' => [
                'course' => $this->coursePayload($result['course']),
                'summary' => $result['summary'],
                'errors' => $result['errors'],
            ],
        ]);
    }

    public function contents(int $courseId): JsonResponse
    {
        $course = Course::query()->findOrFail($courseId);
        $items = $course->contents()
            ->where('is_active', true)
            ->with('workshop')
            ->get()
            ->pluck('workshop')
            ->filter()
            ->values();

        $items->each(function (Workshop $workshop): void {
            $workshop->setAttribute('can_access', true);
        });

        return response()->json([
            'ok' => true,
            'data' => [
                'course' => $this->coursePayload($course),
                'items' => WorkshopSummaryResource::collection($items),
            ],
        ]);
    }

    public function attachContent(Request $request, int $courseId): JsonResponse
    {
        $course = Course::query()->findOrFail($courseId);

        $validated = Validator::make($request->all(), [
            'content_id' => ['required', 'string', 'max:255'],
        ])->validate();

        $workshop = $this->resolveWorkshop((string) $validated['content_id']);
        if ($workshop === null) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'content_not_found',
                    'message' => 'No se encontró el taller o simulacro solicitado.',
                ],
            ], 404);
        }

        CourseContent::query()->updateOrCreate(
            [
                'course_id' => $course->id,
                'workshop_id' => $workshop->id,
            ],
            [
                'is_active' => true,
            ]
        );

        return response()->json([
            'ok' => true,
            'data' => [
                'course' => $this->coursePayload($course->refresh()),
            ],
        ]);
    }

    public function detachContent(int $courseId, string $contentId): JsonResponse
    {
        $course = Course::query()->findOrFail($courseId);
        $identifier = trim(rawurldecode($contentId));
        $workshop = $this->resolveWorkshop($identifier);

        if ($workshop === null) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'content_not_found',
                    'message' => 'No se encontró el taller o simulacro solicitado.',
                ],
            ], 404);
        }

        CourseContent::query()
            ->where('course_id', $course->id)
            ->where('workshop_id', $workshop->id)
            ->delete();

        return response()->json([
            'ok' => true,
            'data' => [
                'course' => $this->coursePayload($course->refresh()),
            ],
        ]);
    }

    private function coursePayload(Course $course): array
    {
        return [
            'id' => $course->id,
            'name' => $course->name,
            'slug' => $course->slug,
            'school_year' => $course->school_year,
            'is_active' => (bool) $course->is_active,
            'notes' => $course->notes,
            'stats' => [
                'students' => $course->enrollments()->where('status', 'active')->count(),
                'contents' => $course->contents()->where('is_active', true)->count(),
                'talleres' => $course->contents()->where('is_active', true)->whereHas('workshop', fn ($builder) => $builder->where('content_type', 'taller'))->count(),
                'simulacros' => $course->contents()->where('is_active', true)->whereHas('workshop', fn ($builder) => $builder->where('content_type', 'simulacro'))->count(),
            ],
            'created_at' => $course->created_at?->toIso8601String(),
            'updated_at' => $course->updated_at?->toIso8601String(),
        ];
    }

    private function resolveWorkshop(string $identifier): ?Workshop
    {
        return Workshop::query()
            ->where(function ($builder) use ($identifier): void {
                $builder
                    ->where('external_id', $identifier)
                    ->orWhere('content_external_id', $identifier)
                    ->orWhere('route', $identifier);
            })
            ->first();
    }
}
