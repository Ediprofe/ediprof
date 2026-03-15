<?php

namespace App\Http\Controllers\Web;

use App\Http\Controllers\Controller;
use App\Services\Auth\GoogleMemberAccountService;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Inertia\Inertia;
use Inertia\Response;
use Laravel\Socialite\Facades\Socialite;
use Throwable;

class MemberAuthController extends Controller
{
    public function showLogin(Request $request): Response|RedirectResponse
    {
        if (Auth::guard('web')->check()) {
            return redirect()->route('members.dashboard');
        }

        return Inertia::render('Members/Auth/Login', [
            'pageTitle' => 'Acceso a miembros',
            'subtitle' => 'Ingresa con tu cuenta de Google para continuar con evaluaciones, talleres y simulacros.',
            'google_login_available' => $this->googleWebConfigured(),
        ]);
    }

    public function redirectToGoogle(): RedirectResponse
    {
        if (! $this->googleWebConfigured()) {
            return redirect()
                ->route('members.login')
                ->with('error', 'El acceso web con Google todavía no está configurado en este entorno.');
        }

        return Socialite::driver('google')
            ->redirectUrl($this->callbackUrl(request()))
            ->scopes(['openid', 'profile', 'email'])
            ->redirect();
    }

    public function handleGoogleCallback(
        Request $request,
        GoogleMemberAccountService $googleAccountService,
    ): RedirectResponse {
        if (! $this->googleWebConfigured()) {
            return redirect()
                ->route('members.login')
                ->with('error', 'El acceso web con Google todavía no está configurado en este entorno.');
        }

        try {
            $googleUser = Socialite::driver('google')
                ->redirectUrl($this->callbackUrl($request))
                ->user();
        } catch (Throwable) {
            return redirect()
                ->route('members.login')
                ->with('error', 'No pudimos completar el acceso con Google. Inténtalo de nuevo.');
        }

        $result = $googleAccountService->authenticate([
            'email' => $googleUser->getEmail(),
            'subject' => $googleUser->getId(),
            'name' => $googleUser->getName(),
            'picture' => $googleUser->getAvatar(),
            'hosted_domain' => $googleUser->user['hd'] ?? null,
            'email_verified' => (bool) ($googleUser->user['verified_email'] ?? true),
        ]);

        if (! $result['ok']) {
            return redirect()
                ->route('members.login')
                ->with('error', $result['message'] ?? 'No pudimos habilitar tu cuenta de miembros.');
        }

        Auth::guard('web')->login($result['user'], true);
        $request->session()->regenerate();

        return redirect()->intended(route('members.dashboard'));
    }

    public function logout(Request $request): RedirectResponse
    {
        Auth::guard('web')->logout();
        $request->session()->invalidate();
        $request->session()->regenerateToken();

        return redirect()
            ->route('members.login')
            ->with('success', 'Tu sesión se cerró correctamente.');
    }

    private function googleWebConfigured(): bool
    {
        return filled(config('services.google.client_id'))
            && filled(config('services.google.client_secret'))
            && (filled(config('services.google.redirect')) || app()->environment('local'));
    }

    private function callbackUrl(Request $request): string
    {
        $relativePath = route('members.auth.google.callback', absolute: false);

        if (app()->environment('local')) {
            return rtrim($request->getSchemeAndHttpHost(), '/').$relativePath;
        }

        $configured = trim((string) config('services.google.redirect'));

        return $configured !== '' ? $configured : rtrim($request->getSchemeAndHttpHost(), '/').$relativePath;
    }
}
