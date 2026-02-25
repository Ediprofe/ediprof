<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

/**
 * @mixin \App\Models\ContentCatalog
 */
class ContentCatalogResource extends JsonResource
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
            'title' => $this->title,
            'description' => $this->description,
            'route' => $this->route,
            'site_url' => $this->site_url,
            'collection' => $this->collection,
            'content_type' => $this->content_type,
            'access_tier' => $this->access_tier,
            'area_slug' => $this->area_slug,
            'unidad_slug' => $this->unidad_slug,
            'tema_slug' => $this->tema_slug,
            'sort_order' => $this->sort_order,
            'published' => $this->is_published,
            'metadata' => $this->metadata,
            'updated_at' => $this->updated_at?->toIso8601String(),
        ];
    }
}
