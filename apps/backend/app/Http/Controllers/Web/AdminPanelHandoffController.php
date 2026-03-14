<?php

namespace App\Http\Controllers\Web;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Cache;

class AdminPanelHandoffController extends Controller
{
    /**
     * Handle the incoming request.
     */
    public function __invoke(Request $request, string $token): RedirectResponse
    {
        $payload = Cache::pull($this->cacheKey($token));

        if (! is_array($payload) || ! isset($payload['user_id'])) {
            return redirect('/admin/login');
        }

        $user = User::query()->find($payload['user_id']);

        if (! $user || ! $user->isAdmin() || $user->member_status === 'blocked') {
            return redirect('/admin/login');
        }

        Auth::login($user);
        $request->session()->regenerate();

        $redirectTo = trim((string) ($payload['redirect_to'] ?? '/admin'));

        if (! str_starts_with($redirectTo, '/admin')) {
            $redirectTo = '/admin';
        }

        return redirect($redirectTo);
    }

    protected function cacheKey(string $token): string
    {
        return "filament_admin_handoff:{$token}";
    }
}
