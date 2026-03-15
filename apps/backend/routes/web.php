<?php

use App\Http\Controllers\Dev\WorkshopPreviewController;
use App\Http\Controllers\Api\V1\AssessmentAssignmentController;
use App\Http\Controllers\Api\V1\AssessmentAttemptController;
use App\Http\Controllers\Web\Admin\AssessmentResultsExportController;
use App\Http\Controllers\Web\Admin\AssessmentDraftPreviewController;
use App\Http\Controllers\Web\AdminPanelHandoffController;
use App\Http\Controllers\Web\MemberAuthController;
use App\Http\Controllers\Web\MembersController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/dev/workshops/preview', [WorkshopPreviewController::class, 'index'])
    ->name('dev.workshops.preview');

Route::prefix('miembros-v2')->group(function (): void {
    Route::get('/login', [MemberAuthController::class, 'showLogin'])->name('members.login');
    Route::get('/auth/google/redirect', [MemberAuthController::class, 'redirectToGoogle'])->name('members.auth.google.redirect');
    Route::get('/auth/google/callback', [MemberAuthController::class, 'handleGoogleCallback'])->name('members.auth.google.callback');

    Route::middleware('ensure.member_session')->group(function (): void {
        Route::get('/', [MembersController::class, 'dashboard'])->name('members.dashboard');
        Route::get('/evaluaciones', [MembersController::class, 'evaluations'])->name('members.evaluations');
        Route::get('/evaluaciones/{evaluation}', [MembersController::class, 'showEvaluation'])->name('members.evaluations.show');
        Route::get('/talleres', [MembersController::class, 'workshops'])->name('members.workshops');
        Route::get('/talleres/{workshop}', [MembersController::class, 'showWorkshop'])->name('members.workshops.show');
        Route::get('/simulacros', [MembersController::class, 'simulacros'])->name('members.simulacros');
        Route::get('/simulacros/{simulacro}', [MembersController::class, 'showSimulacro'])->name('members.simulacros.show');
        Route::post('/asignaciones/{assignment}/intento', [AssessmentAssignmentController::class, 'startAttempt'])->name('members.assignments.attempts.start');
        Route::post('/evaluaciones/{assignment}/intento', [AssessmentAssignmentController::class, 'startAttempt'])->name('members.evaluations.attempts.start');
        Route::get('/intentos/{attempt}', [AssessmentAttemptController::class, 'show'])->name('members.attempts.show');
        Route::patch('/intentos/{attempt}/preguntas/{question}', [AssessmentAttemptController::class, 'answer'])->name('members.attempts.answer');
        Route::post('/intentos/{attempt}/entregar', [AssessmentAttemptController::class, 'submit'])->name('members.attempts.submit');
        Route::post('/logout', [MemberAuthController::class, 'logout'])->name('members.logout');
    });
});

Route::get('/admin/handoff/{token}', AdminPanelHandoffController::class)
    ->name('admin.handoff');

Route::middleware('auth')->prefix('admin/exports')->name('admin.exports.')->group(function (): void {
    Route::get('/assignments/{assignment}/results.csv', [AssessmentResultsExportController::class, 'assignment'])
        ->name('assignments.results');
    Route::get('/assignments/{assignment}/results.xls', [AssessmentResultsExportController::class, 'assignmentExcel'])
        ->name('assignments.results.excel');
    Route::get('/assignments/{assignment}/results-min.xls', [AssessmentResultsExportController::class, 'assignmentMinimalExcel'])
        ->name('assignments.results.excel_minimal');
    Route::get('/courses/{course}/results.csv', [AssessmentResultsExportController::class, 'course'])
        ->name('courses.results');
});

Route::middleware('auth')->get('/admin/assessment-drafts/{template}/preview-web', AssessmentDraftPreviewController::class)
    ->name('admin.assessment_drafts.preview_web');
