<?php

use App\Http\Controllers\Api\V1\AuthController;
use App\Http\Controllers\Api\V1\Admin\AdminPanelController;
use App\Http\Controllers\Api\V1\Admin\CourseController;
use App\Http\Controllers\Api\V1\AssessmentAssignmentController;
use App\Http\Controllers\Api\V1\AssessmentAttemptController;
use App\Http\Controllers\Api\V1\ContentController;
use App\Http\Controllers\Api\V1\MemberAssignmentController;
use App\Http\Controllers\Api\V1\MemberLibraryController;
use App\Http\Controllers\Api\V1\SimulacroController;
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

    Route::post('/auth/login', [AuthController::class, 'login'])->middleware('throttle:auth-login');
    Route::post('/auth/google/login', [AuthController::class, 'googleLogin'])->middleware('throttle:auth-login');
    Route::get('/auth/me', [AuthController::class, 'me'])->middleware('require.api_token');
    Route::post('/auth/logout', [AuthController::class, 'logout'])->middleware('require.api_token');
    Route::get('/me/courses', [MemberLibraryController::class, 'courses'])->middleware('require.api_token');
    Route::get('/me/library', [MemberLibraryController::class, 'library'])->middleware('require.api_token');
    Route::get('/me/assignments', [MemberAssignmentController::class, 'index'])->middleware('require.api_token');
    Route::get('/me/assignments/{assignmentId}', [MemberAssignmentController::class, 'show'])->middleware('require.api_token');

    Route::get('/content', [ContentController::class, 'index']);
    Route::get('/workshops', [WorkshopController::class, 'index']);
    Route::post('/workshops/{workshopId}/attempts', [WorkshopController::class, 'startAttempt'])
        ->where('workshopId', '.*')
        ->middleware('require.api_token');
    Route::post('/workshops/{workshopId}/questions/{questionId}/evaluate', [WorkshopController::class, 'evaluateAnswer'])
        ->where('workshopId', '.*');
    Route::get('/workshops/{workshopId}', [WorkshopController::class, 'show'])
        ->where('workshopId', '.*');
    Route::get('/simulacros', [SimulacroController::class, 'index']);
    Route::post('/simulacros/{workshopId}/attempts', [SimulacroController::class, 'startAttempt'])
        ->where('workshopId', '.*')
        ->middleware('require.api_token');
    Route::post('/simulacros/{workshopId}/questions/{questionId}/evaluate', [SimulacroController::class, 'evaluateAnswer'])
        ->where('workshopId', '.*');
    Route::get('/simulacros/{workshopId}', [SimulacroController::class, 'show'])
        ->where('workshopId', '.*');
    Route::get('/assessment-attempts/{attemptId}', [AssessmentAttemptController::class, 'show'])
        ->middleware('require.api_token');
    Route::patch('/assessment-attempts/{attemptId}/questions/{questionId}', [AssessmentAttemptController::class, 'answer'])
        ->middleware('require.api_token');
    Route::post('/assessment-attempts/{attemptId}/submit', [AssessmentAttemptController::class, 'submit'])
        ->middleware('require.api_token');
    Route::post('/assignments/{assignmentId}/attempts', [AssessmentAssignmentController::class, 'startAttempt'])
        ->middleware('require.api_token');

    Route::prefix('admin')->middleware(['require.api_token', 'require.admin'])->group(function (): void {
        Route::post('/panel-handoff', [AdminPanelController::class, 'handoff']);
        Route::get('/courses', [CourseController::class, 'index']);
        Route::post('/courses', [CourseController::class, 'store']);
        Route::patch('/courses/{courseId}', [CourseController::class, 'update']);
        Route::post('/courses/{courseId}/enrollments/import', [CourseController::class, 'importEnrollments']);
        Route::get('/courses/{courseId}/contents', [CourseController::class, 'contents']);
        Route::post('/courses/{courseId}/contents', [CourseController::class, 'attachContent']);
        Route::delete('/courses/{courseId}/contents/{contentId}', [CourseController::class, 'detachContent'])
            ->where('contentId', '.*');
    });
});
