<?php

namespace Tests\Feature;

use App\Models\Workshop;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\File;
use Tests\TestCase;

class WorkshopSyncManifestCommandTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_syncs_workshop_manifest_entries_into_workshops_table(): void
    {
        $manifestPath = storage_path('app/testing-workshops-manifest.json');

        File::ensureDirectoryExists(dirname($manifestPath));
        File::put($manifestPath, json_encode([
            'workshops' => [
                [
                    'id' => 'content:saber:quimica/la-materia/taller',
                    'content_external_id' => 'content:saber:quimica/la-materia/taller',
                    'route' => '/saber/quimica/la-materia/taller',
                    'title' => 'Taller La Materia',
                    'area_slug' => 'quimica',
                    'unidad_slug' => 'la-materia',
                    'access_tier' => 'premium',
                    'published' => true,
                    'stats' => [
                        'total_questions' => 1,
                        'total_assets' => 1,
                    ],
                    'assets' => ['https://cdn.ediprofe.com/img/saber/quimica/candado-de-hierro.webp'],
                    'questions' => [
                        [
                            'id' => '1',
                            'order' => 1,
                            'meta' => ['fuente' => 'ICFES', 'anio' => 2024],
                            'stem_mdx' => 'Pregunta de prueba',
                            'stem_assets' => [],
                            'options' => [
                                ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                                ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
                            ],
                            'correct_option_id' => 'A',
                            'feedback_mdx' => 'Retro',
                            'feedback_assets' => [],
                        ],
                    ],
                ],
            ],
        ], JSON_PRETTY_PRINT));

        $this->artisan('workshops:sync-manifest', ['path' => $manifestPath])
            ->assertSuccessful();

        $this->assertDatabaseHas('workshops', [
            'external_id' => 'content:saber:quimica/la-materia/taller',
            'route' => '/saber/quimica/la-materia/taller',
            'title' => 'Taller La Materia',
            'access_tier' => 'premium',
            'is_published' => 1,
            'total_questions' => 1,
            'total_assets' => 1,
        ]);

        File::delete($manifestPath);
    }

    public function test_dry_run_does_not_write_workshop_data(): void
    {
        $manifestPath = storage_path('app/testing-workshops-manifest-dry.json');

        File::ensureDirectoryExists(dirname($manifestPath));
        File::put($manifestPath, json_encode([
            'workshops' => [
                [
                    'id' => 'content:saber:test/taller',
                    'route' => '/saber/test/taller',
                    'title' => 'Taller test',
                    'questions' => [
                        [
                            'id' => '1',
                            'order' => 1,
                            'options' => [
                                ['id' => 'A', 'text' => 'ok', 'is_correct' => true],
                            ],
                        ],
                    ],
                ],
            ],
        ], JSON_PRETTY_PRINT));

        $this->artisan('workshops:sync-manifest', ['path' => $manifestPath, '--dry-run' => true])
            ->assertSuccessful();

        $this->assertSame(0, Workshop::query()->count());

        File::delete($manifestPath);
    }
}
