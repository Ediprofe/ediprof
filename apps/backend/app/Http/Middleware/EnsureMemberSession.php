<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Symfony\Component\HttpFoundation\Response;

class EnsureMemberSession
{
    /**
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        $user = Auth::guard('web')->user();

        if ($user === null) {
            if ($request->expectsJson()) {
                return response()->json([
                    'ok' => false,
                    'error' => [
                        'code' => 'auth_required',
                        'message' => 'Necesitas iniciar sesión para continuar en la zona de miembros.',
                    ],
                ], 401);
            }

            return redirect()->guest(route('members.login'));
        }

        if ($user->member_status === 'blocked') {
            Auth::guard('web')->logout();
            $request->session()->invalidate();
            $request->session()->regenerateToken();

            if ($request->expectsJson()) {
                return response()->json([
                    'ok' => false,
                    'error' => [
                        'code' => 'account_blocked',
                        'message' => 'Tu cuenta fue bloqueada. Contacta al administrador si necesitas ayuda.',
                    ],
                ], 403);
            }

            return redirect()
                ->route('members.login')
                ->with('error', 'Tu cuenta fue bloqueada. Contacta al administrador si necesitas ayuda.');
        }

        return $next($request);
    }
}
