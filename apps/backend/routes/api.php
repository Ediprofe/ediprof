<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::prefix('v1')->group(function (): void {
    Route::get('/health', function (Request $request) {
        return response()->json([
            'ok' => true,
            'service' => 'ediprofe-backend',
            'version' => 1,
            'environment' => app()->environment(),
            'timestamp' => now()->toIso8601String(),
            'request_id' => $request->headers->get('X-Request-Id'),
        ]);
    });
});
