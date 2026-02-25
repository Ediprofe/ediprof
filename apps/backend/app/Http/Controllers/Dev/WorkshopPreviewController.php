<?php

namespace App\Http\Controllers\Dev;

use App\Http\Controllers\Controller;
use App\Http\Resources\WorkshopResource;
use App\Models\Workshop;
use Illuminate\Http\Request;
use Illuminate\View\View;

class WorkshopPreviewController extends Controller
{
    public function index(Request $request): View
    {
        abort_unless(app()->environment(['local', 'testing']), 404);

        $selectedId = trim((string) $request->query('workshop_id', ''));
        $includeAnswers = $request->boolean('include_answers', false);

        $workshops = Workshop::query()
            ->orderBy('area_slug')
            ->orderBy('unidad_slug')
            ->orderBy('title')
            ->get([
                'external_id',
                'content_external_id',
                'title',
                'route',
                'access_tier',
                'is_published',
            ]);

        $selectedWorkshop = null;

        if ($selectedId !== '') {
            $selectedWorkshop = Workshop::query()
                ->where('external_id', $selectedId)
                ->orWhere('content_external_id', $selectedId)
                ->orWhere('route', $selectedId)
                ->first();
        }

        if ($selectedWorkshop === null) {
            $selectedWorkshop = Workshop::query()
                ->orderBy('area_slug')
                ->orderBy('unidad_slug')
                ->orderBy('title')
                ->first();
        }

        $payload = $selectedWorkshop
            ? (new WorkshopResource($selectedWorkshop))->toArray($request)
            : null;

        return view('dev.workshops-preview', [
            'workshops' => $workshops,
            'selectedWorkshop' => $selectedWorkshop,
            'payload' => $payload,
            'selectedId' => $selectedId,
            'includeAnswers' => $includeAnswers,
        ]);
    }
}
