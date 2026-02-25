<?php

namespace Tests\Feature;

use App\Models\Workshop;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class DevWorkshopPreviewTest extends TestCase
{
    use RefreshDatabase;

    public function test_preview_shows_question_context_and_assets_with_empty_workshop_id(): void
    {
        Workshop::query()->create([
            'external_id' => 'content:saber:quimica/la-materia/taller-preview',
            'content_external_id' => 'content:saber:quimica/la-materia/taller-preview',
            'title' => 'Taller Preview',
            'route' => '/saber/quimica/la-materia/taller-preview',
            'area_slug' => 'quimica',
            'unidad_slug' => 'la-materia',
            'access_tier' => 'free',
            'is_published' => true,
            'total_questions' => 1,
            'total_assets' => 1,
            'assets' => ['https://cdn.ediprofe.com/img/saber/quimica/candado-de-hierro.webp'],
            'questions' => [
                [
                    'id' => '1',
                    'order' => 1,
                    'meta' => ['fuente' => 'ICFES', 'anio' => 2024],
                    'stem_mdx' => 'Contexto visible de prueba',
                    'stem_assets' => ['https://cdn.ediprofe.com/img/saber/quimica/candado-de-hierro.webp'],
                    'options' => [
                        ['id' => 'A', 'text' => 'Opcion A', 'is_correct' => true],
                        ['id' => 'B', 'text' => 'Opcion B', 'is_correct' => false],
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retroalimentacion',
                    'feedback_assets' => [],
                ],
            ],
            'metadata' => ['contractVersion' => 1],
        ]);

        $response = $this->get('/dev/workshops/preview?workshop_id=');

        $response
            ->assertOk()
            ->assertSee('Taller Preview')
            ->assertSee('Contexto visible de prueba')
            ->assertSee('https://cdn.ediprofe.com/img/saber/quimica/candado-de-hierro.webp');
    }
}
