<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class RequireAdminRole
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        $user = $request->user();

        if ($user === null) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'auth_required',
                    'message' => 'Authentication required.',
                ],
            ], 401);
        }

        if ($user->role !== 'admin') {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'forbidden',
                    'message' => 'Admin privileges are required.',
                ],
            ], 403);
        }

        return $next($request);
    }
}

