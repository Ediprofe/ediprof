<?php

use App\Http\Controllers\Api\V1\ContentController;
use App\Http\Controllers\Api\V1\WorkshopController;
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

    Route::get('/content', [ContentController::class, 'index']);
    Route::get('/workshops/{workshopId}', [WorkshopController::class, 'show'])
        ->where('workshopId', '.*');
});
