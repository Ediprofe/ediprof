<?php

namespace App\Http\Middleware;

use App\Models\ApiToken;
use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Carbon;
use Symfony\Component\HttpFoundation\Response;

class ResolveApiTokenUser
{
    /**
     * Handle an incoming request.
     *
     * @param  \Closure(\Illuminate\Http\Request): (\Symfony\Component\HttpFoundation\Response)  $next
     */
    public function handle(Request $request, Closure $next): Response
    {
        $bearerToken = $request->bearerToken();

        if ($bearerToken === null || trim($bearerToken) === '') {
            return $next($request);
        }

        $tokenHash = hash('sha256', $bearerToken);
        $now = Carbon::now();

        $apiToken = ApiToken::query()
            ->with('user')
            ->where('token_hash', $tokenHash)
            ->whereNull('revoked_at')
            ->where(function ($query) use ($now): void {
                $query
                    ->whereNull('expires_at')
                    ->orWhere('expires_at', '>', $now);
            })
            ->first();

        if ($apiToken === null || $apiToken->user === null) {
            return $next($request);
        }

        $apiToken->forceFill([
            'last_used_at' => $now,
        ])->save();

        $request->attributes->set('api_token', $apiToken);

        $existingResolver = $request->getUserResolver();

        $request->setUserResolver(static function () use ($apiToken, $existingResolver) {
            return $apiToken->user ?? ($existingResolver ? $existingResolver() : null);
        });

        return $next($request);
    }
}
