<?php

use App\Http\Controllers\Web\Admin\AssessmentResultsExportController;
use App\Http\Controllers\Web\AdminPanelHandoffController;
use App\Http\Controllers\Dev\WorkshopPreviewController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/dev/workshops/preview', [WorkshopPreviewController::class, 'index'])
    ->name('dev.workshops.preview');

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
