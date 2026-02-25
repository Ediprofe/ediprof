<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

/**
 * @mixin \App\Models\Workshop
 */
class WorkshopSummaryResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @return array<string, mixed>
     */
    public function toArray(Request $request): array
    {
        return [
            'id' => $this->external_id,
            'content_external_id' => $this->content_external_id,
            'title' => $this->title,
            'route' => $this->route,
            'area_slug' => $this->area_slug,
            'unidad_slug' => $this->unidad_slug,
            'access_tier' => $this->access_tier,
            'published' => $this->is_published,
            'stats' => [
                'total_questions' => $this->total_questions,
                'total_assets' => $this->total_assets,
            ],
            'asset_preview' => array_slice((array) ($this->assets ?? []), 0, 1),
            'can_access' => (bool) ($this->can_access ?? false),
            'updated_at' => $this->updated_at?->toIso8601String(),
        ];
    }
}
