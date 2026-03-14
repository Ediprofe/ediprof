<?php

namespace App\Http\Controllers\Api\V1\Admin;

use App\Http\Controllers\Controller;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\Validator;
use Illuminate\Support\Str;

class AdminPanelController extends Controller
{
    public function handoff(Request $request): JsonResponse
    {
        $user = $request->user();

        abort_unless($user?->isAdmin(), 403);

        $validated = Validator::make($request->all(), [
            'redirect_to' => ['nullable', 'string', 'max:255'],
        ])->validate();

        $redirectTo = trim((string) ($validated['redirect_to'] ?? ''));

        if (($redirectTo !== '') && (! str_starts_with($redirectTo, '/admin'))) {
            $redirectTo = '';
        }

        $token = (string) Str::uuid();

        Cache::put(
            $this->cacheKey($token),
            [
                'user_id' => $user->id,
                'redirect_to' => $redirectTo !== '' ? $redirectTo : '/admin',
            ],
            now()->addMinutes(5),
        );

        return response()->json([
            'ok' => true,
            'data' => [
                'url' => "{$request->getSchemeAndHttpHost()}/admin/handoff/{$token}",
            ],
        ]);
    }

    protected function cacheKey(string $token): string
    {
        return "filament_admin_handoff:{$token}";
    }
}
