<?php

namespace App\Http\Controllers\Api\V1\Admin;

use App\Http\Controllers\Controller;
use App\Models\AccessGrant;
use App\Models\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Carbon;
use Illuminate\Support\Facades\Log;

class StudentAccessController extends Controller
{
    public function index(Request $request): JsonResponse
    {
        $perPage = max(1, min((int) $request->integer('per_page', 25), 100));
        $query = User::query()
            ->where('role', 'student');

        $status = trim((string) $request->query('status', ''));
        if (in_array($status, ['pending', 'approved', 'blocked'], true)) {
            $query->where('member_status', $status);
        }

        $search = trim((string) $request->query('search', ''));
        if ($search !== '') {
            $query->where(function ($builder) use ($search): void {
                $builder
                    ->where('name', 'like', "%{$search}%")
                    ->orWhere('email', 'like', "%{$search}%");
            });
        }

        $students = $query
            ->orderBy('created_at', 'desc')
            ->paginate($perPage)
            ->withQueryString();

        $items = $students->getCollection()->map(function (User $student): array {
            $hasPremiumGrant = $student->accessGrants()
                ->where('reason', 'school_whitelist')
                ->where('is_active', true)
                ->where('scope', 'global')
                ->exists();

            return $this->studentPayload($student, $hasPremiumGrant);
        });

        return response()->json([
            'ok' => true,
            'data' => $items,
            'meta' => [
                'current_page' => $students->currentPage(),
                'per_page' => $students->perPage(),
                'total' => $students->total(),
                'last_page' => $students->lastPage(),
                'from' => $students->firstItem(),
                'to' => $students->lastItem(),
            ],
            'links' => [
                'first' => $students->url(1),
                'last' => $students->url($students->lastPage()),
                'prev' => $students->previousPageUrl(),
                'next' => $students->nextPageUrl(),
            ],
        ]);
    }

    public function approve(Request $request, int $studentId): JsonResponse
    {
        $admin = $request->user();
        $student = User::query()
            ->where('role', 'student')
            ->findOrFail($studentId);

        $student->forceFill([
            'member_status' => 'approved',
        ])->save();

        $this->activateSchoolGrant($student, $admin?->id);

        Log::info('student_access.approved', [
            'admin_user_id' => $admin?->id,
            'student_user_id' => $student->id,
            'student_email' => $student->email,
        ]);

        return response()->json([
            'ok' => true,
            'data' => $this->studentPayload($student->refresh(), true),
        ]);
    }

    public function block(Request $request, int $studentId): JsonResponse
    {
        $admin = $request->user();
        $student = User::query()
            ->where('role', 'student')
            ->findOrFail($studentId);
        $now = Carbon::now();

        $student->forceFill([
            'member_status' => 'blocked',
        ])->save();

        $student->accessGrants()
            ->where('reason', 'school_whitelist')
            ->where('is_active', true)
            ->update([
                'is_active' => false,
                'ends_at' => $now,
            ]);

        $student->apiTokens()
            ->whereNull('revoked_at')
            ->update([
                'revoked_at' => $now,
            ]);

        Log::info('student_access.blocked', [
            'admin_user_id' => $admin?->id,
            'student_user_id' => $student->id,
            'student_email' => $student->email,
        ]);

        return response()->json([
            'ok' => true,
            'data' => $this->studentPayload($student->refresh(), false),
        ]);
    }

    public function revokePremium(Request $request, int $studentId): JsonResponse
    {
        $admin = $request->user();
        $student = User::query()
            ->where('role', 'student')
            ->findOrFail($studentId);
        $now = Carbon::now();

        $student->accessGrants()
            ->where('reason', 'school_whitelist')
            ->where('is_active', true)
            ->update([
                'is_active' => false,
                'ends_at' => $now,
            ]);

        Log::info('student_access.premium_revoked', [
            'admin_user_id' => $admin?->id,
            'student_user_id' => $student->id,
            'student_email' => $student->email,
        ]);

        return response()->json([
            'ok' => true,
            'data' => $this->studentPayload($student->refresh(), false),
        ]);
    }

    private function activateSchoolGrant(User $student, ?int $adminId): void
    {
        $now = Carbon::now();

        $grant = $student->accessGrants()
            ->where('reason', 'school_whitelist')
            ->where('scope', 'global')
            ->orderByDesc('id')
            ->first();

        $metadata = [
            'granted_by_user_id' => $adminId,
            'granted_at' => $now->toIso8601String(),
        ];

        if ($grant === null) {
            AccessGrant::query()->create([
                'user_id' => $student->id,
                'scope' => 'global',
                'scope_ref' => '*',
                'reason' => 'school_whitelist',
                'starts_at' => $now,
                'ends_at' => null,
                'is_active' => true,
                'metadata' => $metadata,
            ]);

            return;
        }

        $grant->forceFill([
            'scope_ref' => '*',
            'starts_at' => $now,
            'ends_at' => null,
            'is_active' => true,
            'metadata' => array_merge((array) ($grant->metadata ?? []), $metadata),
        ])->save();
    }

    private function studentPayload(User $student, bool $hasPremiumGrant): array
    {
        return [
            'id' => $student->id,
            'name' => $student->name,
            'email' => $student->email,
            'role' => $student->role,
            'member_status' => $student->member_status,
            'has_school_premium_grant' => $hasPremiumGrant,
            'created_at' => $student->created_at?->toIso8601String(),
            'updated_at' => $student->updated_at?->toIso8601String(),
        ];
    }
}

