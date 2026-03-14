<?php

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
