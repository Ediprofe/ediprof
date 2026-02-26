<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Http\Requests\Api\V1\LoginRequest;
use App\Http\Requests\Api\V1\RegisterRequest;
use App\Models\ApiToken;
use App\Models\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Carbon;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;

class AuthController extends Controller
{
    public function register(RegisterRequest $request): JsonResponse
    {
        $validated = $request->validated();
        $email = mb_strtolower(trim((string) $validated['email']));

        $alreadyExists = User::query()
            ->whereRaw('LOWER(email) = ?', [$email])
            ->exists();

        if ($alreadyExists) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'email_taken',
                    'message' => 'There is already an account with this email.',
                ],
            ], 422);
        }

        $user = User::query()->create([
            'name' => trim((string) $validated['name']),
            'email' => $email,
            'password' => (string) $validated['password'],
            'role' => 'student',
            'member_status' => 'pending',
        ]);

        return response()->json([
            'ok' => true,
            'data' => [
                'message' => 'Account created. Your access is pending approval.',
                'user' => [
                    'id' => $user->id,
                    'name' => $user->name,
                    'email' => $user->email,
                    'role' => $user->role,
                    'member_status' => $user->member_status,
                ],
            ],
        ], 201);
    }

    public function login(LoginRequest $request): JsonResponse
    {
        $validated = $request->validated();
        $email = mb_strtolower(trim((string) $validated['email']));
        $password = (string) $validated['password'];

        $user = User::query()
            ->whereRaw('LOWER(email) = ?', [$email])
            ->first();

        if ($user === null || ! Hash::check($password, $user->password)) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'invalid_credentials',
                    'message' => 'Invalid email or password.',
                ],
            ], 422);
        }

        if ($user->member_status === 'blocked') {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'account_blocked',
                    'message' => 'Your account has been blocked. Contact support.',
                ],
            ], 403);
        }

        $expiresInDays = (int) ($validated['expires_in_days'] ?? 30);
        $expiresAt = Carbon::now()->addDays($expiresInDays);
        $plainToken = 'ep_'.Str::random(64);

        $apiToken = ApiToken::query()->create([
            'user_id' => $user->id,
            'name' => trim((string) ($validated['device_name'] ?? 'mobile')),
            'token_hash' => hash('sha256', $plainToken),
            'expires_at' => $expiresAt,
            'last_used_at' => null,
            'revoked_at' => null,
            'metadata' => [
                'ip' => $request->ip(),
                'user_agent' => substr((string) $request->userAgent(), 0, 255),
            ],
        ]);

        return response()->json([
            'ok' => true,
            'data' => [
                'token' => $plainToken,
                'token_type' => 'Bearer',
                'expires_at' => $expiresAt->toIso8601String(),
                'user' => [
                    'id' => $user->id,
                    'name' => $user->name,
                    'email' => $user->email,
                    'role' => $user->role,
                    'member_status' => $user->member_status,
                ],
                'session' => [
                    'token_id' => $apiToken->id,
                    'device_name' => $apiToken->name,
                ],
            ],
        ]);
    }

    public function me(Request $request): JsonResponse
    {
        $user = $request->user();
        /** @var ApiToken|null $apiToken */
        $apiToken = $request->attributes->get('api_token');

        if ($user === null || $apiToken === null) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'auth_required',
                    'message' => 'Authentication required.',
                ],
            ], 401);
        }

        return response()->json([
            'ok' => true,
            'data' => [
                'user' => [
                    'id' => $user->id,
                    'name' => $user->name,
                    'email' => $user->email,
                    'role' => $user->role,
                    'member_status' => $user->member_status,
                ],
                'session' => [
                    'token_id' => $apiToken->id,
                    'device_name' => $apiToken->name,
                    'expires_at' => $apiToken->expires_at?->toIso8601String(),
                    'last_used_at' => $apiToken->last_used_at?->toIso8601String(),
                ],
            ],
        ]);
    }

    public function logout(Request $request): JsonResponse
    {
        /** @var ApiToken|null $apiToken */
        $apiToken = $request->attributes->get('api_token');

        if ($apiToken === null) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'auth_required',
                    'message' => 'Authentication required.',
                ],
            ], 401);
        }

        $apiToken->forceFill([
            'revoked_at' => Carbon::now(),
        ])->save();

        return response()->json([
            'ok' => true,
            'data' => [
                'message' => 'Session closed.',
            ],
        ]);
    }
}
