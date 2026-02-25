<?php

namespace Tests\Feature;

use App\Models\ContentCatalog;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\File;
use Tests\TestCase;

class ContentSyncManifestCommandTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_syncs_content_manifest_entries_into_catalog(): void
    {
        $manifestPath = storage_path('app/testing-content-manifest.json');

        File::ensureDirectoryExists(dirname($manifestPath));
        File::put($manifestPath, json_encode([
            'entries' => [
                [
                    'id' => 'content:quimica:la-materia/resumen',
                    'collection' => 'quimica',
                    'title' => 'Resumen La Materia',
                    'description' => 'Resumen tactico',
                    'route' => '/quimica/la-materia/resumen-unidad/resumen',
                    'siteUrl' => 'https://ediprofe.com/quimica/la-materia/resumen-unidad/resumen',
                    'contentType' => 'lesson',
                    'accessTier' => 'free',
                    'area' => ['slug' => 'quimica'],
                    'unidad' => ['slug' => 'la-materia'],
                    'tema' => ['slug' => 'resumen-unidad'],
                    'order' => 1,
                    'flags' => ['published' => true],
                ],
            ],
        ], JSON_PRETTY_PRINT));

        $this->artisan('content:sync-manifest', ['path' => $manifestPath])
            ->assertSuccessful();

        $this->assertDatabaseHas('content_catalog', [
            'external_id' => 'content:quimica:la-materia/resumen',
            'collection' => 'quimica',
            'route' => '/quimica/la-materia/resumen-unidad/resumen',
            'content_type' => 'lesson',
            'access_tier' => 'free',
            'is_published' => 1,
        ]);

        File::delete($manifestPath);
    }

    public function test_dry_run_does_not_write_data(): void
    {
        $manifestPath = storage_path('app/testing-content-manifest-dry.json');

        File::ensureDirectoryExists(dirname($manifestPath));
        File::put($manifestPath, json_encode([
            'entries' => [
                [
                    'id' => 'content:test:entry',
                    'route' => '/test/entry',
                    'title' => 'Test Entry',
                ],
            ],
        ], JSON_PRETTY_PRINT));

        $this->artisan('content:sync-manifest', ['path' => $manifestPath, '--dry-run' => true])
            ->assertSuccessful();

        $this->assertSame(0, ContentCatalog::query()->count());

        File::delete($manifestPath);
    }
}
