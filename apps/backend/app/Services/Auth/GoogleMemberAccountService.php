<?php

namespace App\Services\Auth;

use App\Models\User;
use Illuminate\Support\Carbon;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Str;

class GoogleMemberAccountService
{
    /**
     * @param  array{
     *   email?:string|null,
     *   subject?:string|null,
     *   name?:string|null,
     *   picture?:string|null,
     *   hosted_domain?:string|null,
     *   email_verified?:bool|null
     * }  $profile
     * @return array{
     *   ok:bool,
     *   code?:string,
     *   message?:string,
     *   user?:User
     * }
     */
    public function authenticate(array $profile): array
    {
        $email = mb_strtolower(trim((string) ($profile['email'] ?? '')));
        $subject = trim((string) ($profile['subject'] ?? ''));
        $hostedDomain = mb_strtolower(trim((string) ($profile['hosted_domain'] ?? '')));
        $emailVerified = (bool) ($profile['email_verified'] ?? false);
        $name = trim((string) ($profile['name'] ?? Str::headline(Str::before($email, '@'))));
        $picture = trim((string) ($profile['picture'] ?? ''));

        if ($email === '' || $subject === '' || ! $emailVerified) {
            return [
                'ok' => false,
                'code' => 'invalid_google_claims',
                'message' => 'Google no devolvió una identidad válida para iniciar sesión.',
            ];
        }

        $access = $this->resolveAccess($email, $hostedDomain);

        if (! $access['allowed']) {
            return [
                'ok' => false,
                'code' => 'invalid_google_domain',
                'message' => 'Tu cuenta institucional de Google no tiene acceso a esta zona de miembros.',
            ];
        }

        $user = User::query()
            ->whereRaw('LOWER(email) = ?', [$email])
            ->first();

        if ($user !== null && $user->member_status === 'blocked') {
            return [
                'ok' => false,
                'code' => 'account_blocked',
                'message' => 'Tu cuenta fue bloqueada. Contacta soporte para continuar.',
            ];
        }

        if ($user === null) {
            $user = User::query()->create([
                'name' => $name,
                'first_names' => null,
                'last_names' => null,
                'email' => $email,
                'password' => Hash::make(Str::random(40)),
                'role' => $access['is_admin'] ? 'admin' : 'student',
                'member_status' => 'approved',
                'auth_provider' => 'google',
                'google_subject' => $subject,
                'google_avatar_url' => $picture !== '' ? $picture : null,
                'email_verified_at' => Carbon::now(),
                'last_login_at' => Carbon::now(),
            ]);
        } else {
            $preserveAcademicName = filled($user->first_names)
                || filled($user->last_names)
                || filled($user->institutional_code)
                || filled($user->document_number);

            $user->forceFill([
                'name' => $access['is_admin'] || $user->isAdmin() || $preserveAcademicName ? $user->name : $name,
                'role' => $access['is_admin'] ? 'admin' : $user->role,
                'member_status' => $access['is_admin'] || $user->isAdmin() ? $user->member_status : 'approved',
                'auth_provider' => 'google',
                'google_subject' => $subject,
                'google_avatar_url' => $picture !== '' ? $picture : $user->google_avatar_url,
                'email_verified_at' => $user->email_verified_at ?? Carbon::now(),
                'last_login_at' => Carbon::now(),
            ])->save();
        }

        return [
            'ok' => true,
            'user' => $user,
        ];
    }

    /**
     * @return array{allowed:bool,is_admin:bool}
     */
    private function resolveAccess(string $email, string $hostedDomain): array
    {
        $allowedDomain = mb_strtolower(trim((string) config('services.google.allowed_domain', 'sanjoseitagui.edu.co')));
        $adminEmails = collect(config('services.google.admin_emails', []))
            ->map(static fn ($value): string => mb_strtolower(trim((string) $value)))
            ->filter()
            ->values()
            ->all();

        $emailDomain = (string) Str::of($email)->afterLast('@');
        $isGoogleAdmin = in_array($email, $adminEmails, true);
        $isAllowedInstitutionalUser = $emailDomain === $allowedDomain
            && ($hostedDomain === '' || $hostedDomain === $allowedDomain);

        return [
            'allowed' => $isGoogleAdmin || $isAllowedInstitutionalUser,
            'is_admin' => $isGoogleAdmin,
        ];
    }
}
