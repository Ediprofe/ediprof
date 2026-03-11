<?php

namespace App\Http\Controllers\Api\V1\Admin;

use App\Http\Controllers\Controller;
use App\Http\Resources\WorkshopSummaryResource;
use App\Models\Course;
use App\Models\CourseContent;
use App\Models\CourseEnrollment;
use App\Models\User;
use App\Models\Workshop;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Validator;
use Illuminate\Support\Str;

class CourseController extends Controller
{
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

        $slug = $this->resolveUniqueSlug(
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
        $slug = $this->resolveUniqueSlug($requestedSlug, $course->id);

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

        /** @var UploadedFile $csv */
        $csv = $validated['csv'];
        $rows = $this->parseCsv($csv);
        $allowedDomain = mb_strtolower((string) config('services.google.allowed_domain', 'sanjoseitagui.edu.co'));

        $createdUsers = 0;
        $updatedUsers = 0;
        $enrolledUsers = 0;
        $errors = [];

        foreach ($rows as $index => $row) {
            $line = $index + 1;
            $email = mb_strtolower(trim((string) ($row['email'] ?? '')));
            $name = trim((string) ($row['name'] ?? ''));

            if ($email === '') {
                $errors[] = ['line' => $line, 'message' => 'Falta el correo institucional.'];
                continue;
            }

            if (! filter_var($email, FILTER_VALIDATE_EMAIL)) {
                $errors[] = ['line' => $line, 'message' => 'Correo inválido.'];
                continue;
            }

            $domain = (string) Str::of($email)->afterLast('@');
            if ($domain !== $allowedDomain) {
                $errors[] = ['line' => $line, 'message' => 'El correo no pertenece al dominio institucional permitido.'];
                continue;
            }

            $user = User::query()->whereRaw('LOWER(email) = ?', [$email])->first();
            $wasRecentlyCreated = false;

            if ($user === null) {
                $user = User::query()->create([
                    'name' => $name !== '' ? $name : Str::headline(Str::before($email, '@')),
                    'email' => $email,
                    'password' => Hash::make(Str::random(40)),
                    'role' => 'student',
                    'member_status' => 'approved',
                    'auth_provider' => 'google',
                ]);
                $createdUsers += 1;
                $wasRecentlyCreated = true;
            } else {
                $user->forceFill([
                    'name' => $name !== '' ? $name : $user->name,
                    'role' => $user->isAdmin() ? 'admin' : 'student',
                    'member_status' => $user->member_status === 'blocked' ? 'blocked' : 'approved',
                    'auth_provider' => $user->auth_provider ?: 'google',
                ])->save();
                if (! $wasRecentlyCreated) {
                    $updatedUsers += 1;
                }
            }

            CourseEnrollment::query()->updateOrCreate(
                [
                    'course_id' => $course->id,
                    'user_id' => $user->id,
                ],
                [
                    'status' => 'active',
                    'source' => 'csv_import',
                ]
            );

            $enrolledUsers += 1;
        }

        return response()->json([
            'ok' => true,
            'data' => [
                'course' => $this->coursePayload($course->refresh()),
                'summary' => [
                    'created_users' => $createdUsers,
                    'updated_users' => $updatedUsers,
                    'enrolled_users' => $enrolledUsers,
                    'error_count' => count($errors),
                ],
                'errors' => $errors,
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

    /**
     * @return array<int, array{email:string,name:string}>
     */
    private function parseCsv(UploadedFile $csv): array
    {
        $contents = trim((string) file_get_contents($csv->getRealPath()));
        if ($contents === '') {
            return [];
        }

        $lines = preg_split('/\r\n|\n|\r/', preg_replace('/^\xEF\xBB\xBF/', '', $contents) ?: '');
        if (! is_array($lines) || $lines === []) {
            return [];
        }

        $rows = [];
        $header = array_map(fn ($value) => mb_strtolower(trim((string) $value)), str_getcsv((string) $lines[0]));
        $hasHeader = in_array('email', $header, true) || in_array('correo', $header, true);

        $emailIndex = 0;
        $nameIndex = 1;
        $startIndex = 0;

        if ($hasHeader) {
            $startIndex = 1;
            $emailIndex = array_search('email', $header, true);
            if ($emailIndex === false) {
                $emailIndex = array_search('correo', $header, true);
            }

            $nameIndex = array_search('name', $header, true);
            if ($nameIndex === false) {
                $nameIndex = array_search('nombre', $header, true);
            }
            if ($nameIndex === false) {
                $nameIndex = 1;
            }
        }

        for ($i = $startIndex; $i < count($lines); $i += 1) {
            $line = trim((string) $lines[$i]);
            if ($line === '') {
                continue;
            }

            $columns = str_getcsv($line);
            if (! is_array($columns)) {
                continue;
            }

            $rows[] = [
                'email' => trim((string) ($columns[$emailIndex] ?? '')),
                'name' => trim((string) ($columns[$nameIndex] ?? '')),
            ];
        }

        return $rows;
    }

    private function resolveUniqueSlug(string $baseSlug, ?int $ignoreId = null): string
    {
        $slug = Str::slug($baseSlug);
        if ($slug === '') {
            $slug = 'curso';
        }

        $candidate = $slug;
        $suffix = 2;

        while ($this->slugExists($candidate, $ignoreId)) {
            $candidate = "{$slug}-{$suffix}";
            $suffix += 1;
        }

        return $candidate;
    }

    private function slugExists(string $slug, ?int $ignoreId = null): bool
    {
        return Course::query()
            ->when($ignoreId !== null, fn ($builder) => $builder->where('id', '!=', $ignoreId))
            ->where('slug', $slug)
            ->exists();
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
