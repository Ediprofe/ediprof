<?php

namespace App\Http\Controllers\Api\V1;

use App\Http\Controllers\Controller;
use App\Http\Requests\Api\V1\LoginRequest;
use App\Http\Requests\Api\V1\GoogleLoginRequest;
use App\Models\ApiToken;
use App\Models\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Carbon;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;

class AuthController extends Controller
{
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

        return $this->issueTokenResponse($request, $user, $validated);
    }

    public function googleLogin(GoogleLoginRequest $request): JsonResponse
    {
        $validated = $request->validated();
        $clientId = trim((string) config('services.google.client_id'));
        $allowedDomain = mb_strtolower(trim((string) config('services.google.allowed_domain', 'sanjoseitagui.edu.co')));
        $adminEmails = collect(config('services.google.admin_emails', []))
            ->map(static fn ($value): string => mb_strtolower(trim((string) $value)))
            ->filter()
            ->values()
            ->all();

        if ($clientId === '') {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'google_not_configured',
                    'message' => 'Google login is not configured yet.',
                ],
            ], 503);
        }

        $googleResponse = Http::asForm()
            ->timeout(10)
            ->get('https://oauth2.googleapis.com/tokeninfo', [
                'id_token' => (string) $validated['credential'],
            ]);

        if (! $googleResponse->ok()) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'invalid_google_token',
                    'message' => 'Google could not validate the credential.',
                ],
            ], 422);
        }

        $claims = $googleResponse->json();
        $audience = trim((string) ($claims['aud'] ?? ''));
        $email = mb_strtolower(trim((string) ($claims['email'] ?? '')));
        $subject = trim((string) ($claims['sub'] ?? ''));
        $emailVerified = filter_var($claims['email_verified'] ?? false, FILTER_VALIDATE_BOOL);
        $hostedDomain = mb_strtolower(trim((string) ($claims['hd'] ?? '')));

        if ($audience !== $clientId || $subject === '' || $email === '' || ! $emailVerified) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'invalid_google_claims',
                    'message' => 'Google credential is missing required claims.',
                ],
            ], 422);
        }

        $emailDomain = (string) Str::of($email)->afterLast('@');
        $isGoogleAdmin = in_array($email, $adminEmails, true);
        $isAllowedInstitutionalUser = $emailDomain === $allowedDomain
            && ($hostedDomain === '' || $hostedDomain === $allowedDomain);

        if (! $isGoogleAdmin && ! $isAllowedInstitutionalUser) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'invalid_google_domain',
                    'message' => 'Your institutional Google account is not allowed for this members area.',
                ],
            ], 403);
        }

        $name = trim((string) ($claims['name'] ?? Str::headline(Str::before($email, '@'))));
        $picture = trim((string) ($claims['picture'] ?? ''));

        $user = User::query()
            ->whereRaw('LOWER(email) = ?', [$email])
            ->first();

        if ($user === null) {
            $user = User::query()->create([
                'name' => $name,
                'first_names' => null,
                'last_names' => null,
                'email' => $email,
                'password' => Hash::make(Str::random(40)),
                'role' => $isGoogleAdmin ? 'admin' : 'student',
                'member_status' => 'approved',
                'auth_provider' => 'google',
                'google_subject' => $subject,
                'google_avatar_url' => $picture !== '' ? $picture : null,
                'email_verified_at' => Carbon::now(),
                'last_login_at' => Carbon::now(),
            ]);
        } else {
            if ($user->member_status === 'blocked') {
                return response()->json([
                    'ok' => false,
                    'error' => [
                        'code' => 'account_blocked',
                        'message' => 'Your account has been blocked. Contact support.',
                    ],
                ], 403);
            }

            $preserveAcademicName = filled($user->first_names)
                || filled($user->last_names)
                || filled($user->institutional_code)
                || filled($user->document_number);

            $user->forceFill([
                'name' => $isGoogleAdmin || $user->isAdmin() || $preserveAcademicName ? $user->name : $name,
                'role' => $isGoogleAdmin ? 'admin' : $user->role,
                'member_status' => $isGoogleAdmin || $user->isAdmin() ? $user->member_status : 'approved',
                'auth_provider' => 'google',
                'google_subject' => $subject,
                'google_avatar_url' => $picture !== '' ? $picture : $user->google_avatar_url,
                'email_verified_at' => $user->email_verified_at ?? Carbon::now(),
                'last_login_at' => Carbon::now(),
            ])->save();
        }

        return $this->issueTokenResponse($request, $user, $validated);
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
                    'first_names' => $user->first_names,
                    'last_names' => $user->last_names,
                    'email' => $user->email,
                    'institutional_code' => $user->institutional_code,
                    'document_number' => $user->document_number,
                    'grade_group' => $user->grade_group,
                    'role' => $user->role,
                    'member_status' => $user->member_status,
                    'auth_provider' => $user->auth_provider,
                    'google_avatar_url' => $user->google_avatar_url,
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

    /**
     * @param array<string, mixed> $validated
     */
    private function issueTokenResponse(Request $request, User $user, array $validated): JsonResponse
    {
        $expiresInDays = (int) ($validated['expires_in_days'] ?? 30);
        $expiresAt = Carbon::now()->addDays($expiresInDays);
        $plainToken = 'ep_'.Str::random(64);

        $apiToken = ApiToken::query()->create([
            'user_id' => $user->id,
            'name' => trim((string) ($validated['device_name'] ?? 'web-miembros')),
            'token_hash' => hash('sha256', $plainToken),
            'expires_at' => $expiresAt,
            'last_used_at' => null,
            'revoked_at' => null,
            'metadata' => [
                'ip' => $request->ip(),
                'user_agent' => substr((string) $request->userAgent(), 0, 255),
            ],
        ]);

        $user->forceFill([
            'last_login_at' => Carbon::now(),
        ])->save();

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
                    'auth_provider' => $user->auth_provider,
                    'google_avatar_url' => $user->google_avatar_url,
                ],
                'session' => [
                    'token_id' => $apiToken->id,
                    'device_name' => $apiToken->name,
                ],
            ],
        ]);
    }
}
