<?php

namespace Tests\Feature;

use App\Models\Workshop;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class WorkshopApiTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_returns_workshop_detail_by_external_id_with_slashes(): void
    {
        Workshop::query()->create([
            'external_id' => 'content:saber:quimica/la-materia/taller',
            'content_external_id' => 'content:saber:quimica/la-materia/taller',
            'title' => 'Taller de La Materia',
            'route' => '/saber/quimica/la-materia/taller',
            'area_slug' => 'quimica',
            'unidad_slug' => 'la-materia',
            'access_tier' => 'premium',
            'is_published' => true,
            'total_questions' => 1,
            'total_assets' => 1,
            'assets' => ['https://cdn.ediprofe.com/img/saber/quimica/candado-de-hierro.webp'],
            'questions' => [
                [
                    'id' => '1',
                    'order' => 1,
                    'meta' => ['fuente' => 'ICFES'],
                    'stem_mdx' => 'Pregunta de prueba',
                    'stem_assets' => [],
                    'options' => [
                        ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                        ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retroalimentacion',
                    'feedback_assets' => [],
                ],
            ],
            'metadata' => ['contractVersion' => 1],
        ]);

        $response = $this->getJson('/api/v1/workshops/content:saber:quimica/la-materia/taller');

        $response
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.id', 'content:saber:quimica/la-materia/taller')
            ->assertJsonPath('data.stats.total_questions', 1)
            ->assertJsonPath('data.questions.0.correct_option_id', 'A');
    }

    public function test_it_can_hide_answers_when_include_answers_is_false(): void
    {
        Workshop::query()->create([
            'external_id' => 'workshop:saber:quimica:la-materia:taller',
            'content_external_id' => 'content:saber:quimica/la-materia/taller',
            'title' => 'Taller de La Materia',
            'route' => '/saber/quimica/la-materia/taller',
            'area_slug' => 'quimica',
            'unidad_slug' => 'la-materia',
            'access_tier' => 'premium',
            'is_published' => true,
            'total_questions' => 1,
            'total_assets' => 0,
            'assets' => [],
            'questions' => [
                [
                    'id' => '1',
                    'order' => 1,
                    'meta' => [],
                    'stem_mdx' => 'Pregunta',
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
            'metadata' => ['contractVersion' => 1],
        ]);

        $response = $this->getJson('/api/v1/workshops/workshop:saber:quimica:la-materia:taller?include_answers=false');

        $response
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.questions.0.correct_option_id', null)
            ->assertJsonPath('data.questions.0.feedback_mdx', '')
            ->assertJsonPath('data.questions.0.feedback_assets', []);

        $firstOption = $response->json('data.questions.0.options.0');
        $this->assertIsArray($firstOption);
        $this->assertArrayNotHasKey('is_correct', $firstOption);
    }
}
