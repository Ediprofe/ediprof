<?php

namespace Tests\Feature;

use App\Models\ContentCatalog;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ContentCatalogApiTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_returns_paginated_content_catalog(): void
    {
        ContentCatalog::query()->create([
            'external_id' => 'content:quimica:la-materia/resumen',
            'collection' => 'quimica',
            'title' => 'Resumen La Materia',
            'description' => 'Resumen tactico',
            'route' => '/quimica/la-materia/resumen-unidad/resumen',
            'site_url' => 'https://ediprofe.com/quimica/la-materia/resumen-unidad/resumen',
            'content_type' => 'lesson',
            'access_tier' => 'free',
            'area_slug' => 'quimica',
            'unidad_slug' => 'la-materia',
            'tema_slug' => 'resumen-unidad',
            'sort_order' => 1,
            'is_published' => true,
            'metadata' => ['example' => true],
        ]);

        $response = $this->getJson('/api/v1/content?published=true&area_slug=quimica');

        $response
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('meta.total', 1)
            ->assertJsonPath('data.0.id', 'content:quimica:la-materia/resumen')
            ->assertJsonPath('data.0.access_tier', 'free');
    }
}
