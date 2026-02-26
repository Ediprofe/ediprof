<?php

use App\Http\Controllers\Api\V1\AuthController;
use App\Http\Controllers\Api\V1\Admin\StudentAccessController;
use App\Http\Controllers\Api\V1\ContentController;
use App\Http\Controllers\Api\V1\WorkshopController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::prefix('v1')->middleware('resolve.api_token')->group(function (): void {
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

    Route::post('/auth/register', [AuthController::class, 'register'])->middleware('throttle:auth-register');
    Route::post('/auth/login', [AuthController::class, 'login'])->middleware('throttle:auth-login');
    Route::get('/auth/me', [AuthController::class, 'me'])->middleware('require.api_token');
    Route::post('/auth/logout', [AuthController::class, 'logout'])->middleware('require.api_token');

    Route::get('/content', [ContentController::class, 'index']);
    Route::get('/workshops', [WorkshopController::class, 'index']);
    Route::post('/workshops/{workshopId}/questions/{questionId}/evaluate', [WorkshopController::class, 'evaluateAnswer'])
        ->where('workshopId', '.*');
    Route::get('/workshops/{workshopId}', [WorkshopController::class, 'show'])
        ->where('workshopId', '.*');

    Route::prefix('admin')->middleware(['require.api_token', 'require.admin'])->group(function (): void {
        Route::get('/students', [StudentAccessController::class, 'index']);
        Route::post('/students/{studentId}/approve', [StudentAccessController::class, 'approve']);
        Route::post('/students/{studentId}/block', [StudentAccessController::class, 'block']);
        Route::post('/students/{studentId}/revoke-premium', [StudentAccessController::class, 'revokePremium']);
    });
});
