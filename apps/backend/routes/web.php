<?php

use App\Http\Controllers\Dev\WorkshopPreviewController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/dev/workshops/preview', [WorkshopPreviewController::class, 'index'])
    ->name('dev.workshops.preview');
