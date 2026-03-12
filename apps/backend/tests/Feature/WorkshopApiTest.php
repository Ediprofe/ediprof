<?php

namespace Tests\Feature;

use App\Models\Course;
use App\Models\CourseContent;
use App\Models\CourseEnrollment;
use App\Models\User;
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
            'access_tier' => 'free',
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
                    'stem_blocks' => [
                        [
                            'type' => 'paragraph',
                            'inlines' => [
                                ['text' => 'Pregunta', 'variant' => 'plain'],
                            ],
                        ],
                    ],
                    'options' => [
                        ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                        ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retro',
                    'feedback_assets' => [],
                    'feedback_blocks' => [
                        [
                            'type' => 'paragraph',
                            'inlines' => [
                                ['text' => 'Retro', 'variant' => 'plain'],
                            ],
                        ],
                    ],
                    'app_payload_version' => 1,
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
            ->assertJsonPath('data.questions.0.feedback_assets', [])
            ->assertJsonPath('data.questions.0.feedback_blocks', []);

        $question = $response->json('data.questions.0');
        $this->assertIsArray($question);
        $this->assertArrayNotHasKey('meta', $question);

        $data = $response->json('data');
        $this->assertIsArray($data);
        $this->assertArrayNotHasKey('metadata', $data);

        $firstOption = $response->json('data.questions.0.options.0');
        $this->assertIsArray($firstOption);
        $this->assertArrayNotHasKey('is_correct', $firstOption);
    }

    public function test_it_returns_app_optimized_payload_without_mdx_fields(): void
    {
        Workshop::query()->create([
            'external_id' => 'workshop:saber:quimica:la-materia:app-format',
            'content_external_id' => 'content:saber:quimica/la-materia/app-format',
            'title' => 'Taller App Payload',
            'route' => '/saber/quimica/la-materia/app-format',
            'area_slug' => 'quimica',
            'unidad_slug' => 'la-materia',
            'access_tier' => 'free',
            'is_published' => true,
            'total_questions' => 1,
            'total_assets' => 0,
            'assets' => [],
            'questions' => [
                [
                    'id' => '1',
                    'order' => 1,
                    'meta' => ['fuente' => 'ICFES'],
                    'stem_mdx' => 'Pregunta en MDX',
                    'stem_assets' => [],
                    'stem_blocks' => [
                        [
                            'type' => 'paragraph',
                            'inlines' => [
                                ['text' => 'Pregunta app', 'variant' => 'plain'],
                            ],
                        ],
                    ],
                    'options' => [
                        ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                        ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retro en MDX',
                    'feedback_assets' => [],
                    'feedback_blocks' => [
                        [
                            'type' => 'paragraph',
                            'inlines' => [
                                ['text' => 'Retro app', 'variant' => 'plain'],
                            ],
                        ],
                    ],
                    'app_payload_version' => 1,
                ],
            ],
            'metadata' => [],
        ]);

        $response = $this->getJson(
            '/api/v1/workshops/workshop:saber:quimica:la-materia:app-format?include_answers=false&format=app'
        );

        $response
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.questions.0.stem_blocks.0.type', 'paragraph')
            ->assertJsonPath('data.questions.0.feedback_blocks', [])
            ->assertJsonPath('data.questions.0.correct_option_id', null);

        $question = $response->json('data.questions.0');
        $this->assertIsArray($question);
        $this->assertArrayNotHasKey('meta', $question);
        $this->assertArrayNotHasKey('stem_mdx', $question);
        $this->assertArrayNotHasKey('feedback_mdx', $question);
    }

    public function test_it_evaluates_answer_and_returns_feedback(): void
    {
        Workshop::query()->create([
            'external_id' => 'content:saber:quimica/la-materia/taller-evaluate',
            'content_external_id' => 'content:saber:quimica/la-materia/taller-evaluate',
            'title' => 'Taller Evaluacion',
            'route' => '/saber/quimica/la-materia/taller-evaluate',
            'area_slug' => 'quimica',
            'unidad_slug' => 'la-materia',
            'access_tier' => 'free',
            'is_published' => true,
            'total_questions' => 1,
            'total_assets' => 0,
            'assets' => [],
            'questions' => [
                [
                    'id' => '1',
                    'order' => 1,
                    'meta' => ['fuente' => 'ICFES'],
                    'stem_mdx' => 'Pregunta',
                    'stem_assets' => [],
                    'options' => [
                        ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                        ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retro para estudiante',
                    'feedback_assets' => [],
                    'feedback_blocks' => [
                        [
                            'type' => 'paragraph',
                            'inlines' => [
                                ['text' => 'Retro para estudiante', 'variant' => 'plain'],
                            ],
                        ],
                    ],
                    'app_payload_version' => 1,
                ],
            ],
            'metadata' => ['contractVersion' => 1],
        ]);

        $response = $this->postJson(
            '/api/v1/workshops/content:saber:quimica/la-materia/taller-evaluate/questions/1/evaluate',
            ['option_id' => 'A']
        );

        $response
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.question_id', '1')
            ->assertJsonPath('data.selected_option_id', 'A')
            ->assertJsonPath('data.correct_option_id', 'A')
            ->assertJsonPath('data.is_correct', true)
            ->assertJsonPath('data.feedback_mdx', 'Retro para estudiante')
            ->assertJsonPath('data.feedback_blocks.0.type', 'paragraph');
    }

    public function test_it_rejects_invalid_option_during_evaluation(): void
    {
        Workshop::query()->create([
            'external_id' => 'content:saber:quimica/la-materia/taller-invalid-option',
            'content_external_id' => 'content:saber:quimica/la-materia/taller-invalid-option',
            'title' => 'Taller Evaluacion',
            'route' => '/saber/quimica/la-materia/taller-invalid-option',
            'area_slug' => 'quimica',
            'unidad_slug' => 'la-materia',
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
                    'options' => [
                        ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retro',
                    'feedback_assets' => [],
                ],
            ],
            'metadata' => [],
        ]);

        $response = $this->postJson(
            '/api/v1/workshops/content:saber:quimica/la-materia/taller-invalid-option/questions/1/evaluate',
            ['option_id' => 'Z']
        );

        $response
            ->assertStatus(422)
            ->assertJsonPath('ok', false)
            ->assertJsonPath('error.code', 'invalid_option');
    }

    public function test_it_requires_authentication_for_premium_workshop(): void
    {
        Workshop::query()->create([
            'external_id' => 'content:saber:quimica/la-materia/taller-premium',
            'content_external_id' => 'content:saber:quimica/la-materia/taller-premium',
            'title' => 'Taller Premium',
            'route' => '/saber/quimica/la-materia/taller-premium',
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
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retro',
                    'feedback_assets' => [],
                ],
            ],
            'metadata' => [],
        ]);

        $response = $this->getJson('/api/v1/workshops/content:saber:quimica/la-materia/taller-premium');

        $response
            ->assertStatus(401)
            ->assertJsonPath('ok', false)
            ->assertJsonPath('error.code', 'auth_required');
    }

    public function test_it_allows_premium_workshop_for_student_enrolled_in_course_with_attached_content(): void
    {
        $user = User::factory()->create([
            'member_status' => 'approved',
        ]);

        $course = Course::query()->create([
            'name' => 'ICFES 11°1',
            'slug' => 'icfes-11-1',
            'school_year' => '2026',
            'is_active' => true,
        ]);

        CourseEnrollment::query()->create([
            'course_id' => $course->id,
            'user_id' => $user->id,
            'status' => 'active',
            'source' => 'manual',
        ]);

        $workshop = Workshop::query()->create([
            'external_id' => 'content:saber:quimica/la-materia/taller-premium-sub',
            'content_external_id' => 'content:saber:quimica/la-materia/taller-premium-sub',
            'title' => 'Taller Premium Sub',
            'route' => '/saber/quimica/la-materia/taller-premium-sub',
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
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retro',
                    'feedback_assets' => [],
                ],
            ],
            'metadata' => [],
        ]);

        CourseContent::query()->create([
            'course_id' => $course->id,
            'workshop_id' => $workshop->id,
            'is_active' => true,
        ]);

        $response = $this
            ->actingAs($user)
            ->getJson('/api/v1/workshops/content:saber:quimica/la-materia/taller-premium-sub');

        $response
            ->assertOk()
            ->assertJsonPath('ok', true)
            ->assertJsonPath('data.id', 'content:saber:quimica/la-materia/taller-premium-sub');
    }

    public function test_it_denies_premium_workshop_when_student_is_not_enrolled_in_any_course_with_that_content(): void
    {
        $user = User::factory()->create([
            'member_status' => 'approved',
        ]);

        Workshop::query()->create([
            'external_id' => 'content:saber:quimica/la-materia/taller-premium-grant',
            'content_external_id' => 'content:saber:quimica/la-materia/taller-premium-grant',
            'title' => 'Taller Premium Grant',
            'route' => '/saber/quimica/la-materia/taller-premium-grant',
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
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retro',
                    'feedback_assets' => [],
                ],
            ],
            'metadata' => [],
        ]);

        $response = $this
            ->actingAs($user)
            ->getJson('/api/v1/workshops/content:saber:quimica/la-materia/taller-premium-grant');

        $response
            ->assertForbidden()
            ->assertJsonPath('ok', false)
            ->assertJsonPath('error.code', 'premium_access_required');
    }

    public function test_it_returns_403_for_authenticated_user_without_premium_access(): void
    {
        $user = User::factory()->create();

        Workshop::query()->create([
            'external_id' => 'content:saber:quimica/la-materia/taller-premium-no-access',
            'content_external_id' => 'content:saber:quimica/la-materia/taller-premium-no-access',
            'title' => 'Taller Premium Sin Acceso',
            'route' => '/saber/quimica/la-materia/taller-premium-no-access',
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
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retro',
                    'feedback_assets' => [],
                ],
            ],
            'metadata' => [],
        ]);

        $response = $this
            ->actingAs($user)
            ->getJson('/api/v1/workshops/content:saber:quimica/la-materia/taller-premium-no-access');

        $response
            ->assertStatus(403)
            ->assertJsonPath('ok', false)
            ->assertJsonPath('error.code', 'premium_access_required');
    }
}
