<?php

namespace Tests\Feature;

use App\Models\Workshop;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class SimulacroApiTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_returns_only_simulacros_in_simulacros_catalog(): void
    {
        $simulacro = $this->createContent('content:simulacros:quimica/2026-s1/taller', '/simulacros/quimica/2026-s1/taller', 'simulacro');
        $this->createContent('content:saber:quimica/la-materia/taller', '/saber/quimica/la-materia/taller', 'taller');

        $response = $this->getJson('/api/v1/simulacros');

        $response
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('meta.total', 1)
            ->assertJsonPath('data.0.id', $simulacro->external_id)
            ->assertJsonPath('data.0.content_type', 'simulacro');
    }

    public function test_it_evaluates_simulacro_questions_through_simulacro_endpoint(): void
    {
        $simulacro = $this->createContent('content:simulacros:quimica/2026-s1/taller', '/simulacros/quimica/2026-s1/taller', 'simulacro');

        $this->postJson("/api/v1/simulacros/{$simulacro->external_id}/questions/1/evaluate?published_only=false&format=app", [
            'option_id' => 'A',
        ])->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.is_correct', true);

        $this->getJson("/api/v1/workshops/{$simulacro->external_id}?published_only=false&include_answers=false&format=app")
            ->assertStatus(404)
            ->assertJsonPath('error.code', 'content_not_found');
    }

    private function createContent(string $externalId, string $route, string $contentType): Workshop
    {
        return Workshop::query()->create([
            'external_id' => $externalId,
            'content_external_id' => $externalId,
            'content_type' => $contentType,
            'title' => 'Contenido '.$contentType,
            'route' => $route,
            'area_slug' => 'quimica',
            'unidad_slug' => 'estructura-atomica',
            'access_tier' => 'free',
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
                    'stem_blocks' => [],
                    'options' => [
                        ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                        ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retro',
                    'feedback_assets' => [],
                    'feedback_blocks' => [],
                ],
            ],
            'metadata' => [],
            'synced_at' => now(),
        ]);
    }
}
