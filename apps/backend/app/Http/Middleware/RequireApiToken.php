<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

class RequireApiToken
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        if (! $request->attributes->has('api_token')) {
            return response()->json([
                'ok' => false,
                'error' => [
                    'code' => 'auth_required',
                    'message' => 'Bearer token is required for this endpoint.',
                ],
            ], 401);
        }

        return $next($request);
    }
}
