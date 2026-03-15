<?php

namespace Tests\Feature;

use App\Models\AssessmentContext;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentTemplate;
use App\Models\Workshop;
use App\Services\Content\AssessmentTemplateManifestSyncService;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Carbon;
use Tests\TestCase;

class AssessmentTemplateManifestSyncServiceTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_syncs_normalized_contexts_questions_and_links_into_assessment_tables(): void
    {
        $workshop = Workshop::query()->create([
            'external_id' => 'content:saber:quimica/la-materia/taller',
            'content_external_id' => 'content:saber:quimica/la-materia/taller',
            'content_type' => 'taller',
            'title' => 'Taller La Materia',
            'route' => '/saber/quimica/la-materia/taller',
            'area_slug' => 'quimica',
            'unidad_slug' => 'la-materia',
            'access_tier' => 'premium',
            'is_published' => true,
            'total_questions' => 1,
            'total_assets' => 1,
            'assets' => ['https://cdn.ediprofe.com/img/saber/quimica/candado-de-hierro.webp'],
            'questions' => [],
            'metadata' => [],
            'synced_at' => now(),
        ]);

        $entries = [
            $workshop->external_id => [
                'id' => $workshop->external_id,
                'content_external_id' => $workshop->content_external_id,
                'content_type' => 'taller',
                'route' => $workshop->route,
                'title' => $workshop->title,
                'area_slug' => $workshop->area_slug,
                'unidad_slug' => $workshop->unidad_slug,
                'access_tier' => 'premium',
                'published' => true,
                'stats' => [
                    'total_questions' => 1,
                    'total_assets' => 1,
                ],
                'assets' => ['https://cdn.ediprofe.com/img/saber/quimica/candado-de-hierro.webp'],
                'asset_refs' => [
                    [
                        'asset_id' => 'candado',
                        'src' => 'https://cdn.ediprofe.com/img/saber/quimica/candado-de-hierro.webp',
                        'type' => 'image',
                    ],
                ],
                'contexts' => [
                    [
                        'external_id' => 'ctx-1',
                        'title' => 'Contexto compartido',
                        'order_base' => 1,
                        'context_mdx' => 'Contexto de prueba',
                        'context_html' => '<p>Contexto de prueba</p>',
                        'context_assets' => [],
                        'context_blocks' => [],
                    ],
                ],
                'question_context_links' => [
                    [
                        'question_external_id' => '1',
                        'context_external_id' => 'ctx-1',
                        'order_base' => 1,
                    ],
                ],
                'questions' => [
                    [
                        'id' => '1',
                        'order' => 1,
                        'order_base' => 1,
                        'source_slug' => '/saber/quimica/la-materia/taller#pregunta-1',
                        'context_ids' => ['ctx-1'],
                        'meta' => ['fuente' => 'ICFES', 'anio' => 2024],
                        'stem_mdx' => 'Pregunta de prueba',
                        'stem_html' => '<p>Pregunta de prueba</p>',
                        'stem_assets' => [],
                        'stem_blocks' => [],
                        'options' => [
                            ['id' => 'A', 'text' => 'Correcta', 'text_html' => '<span><strong>Correcta</strong></span>', 'text_assets' => [], 'is_correct' => true],
                            ['id' => 'B', 'text' => 'Incorrecta', 'text_html' => '<span>Incorrecta</span>', 'text_assets' => [], 'is_correct' => false],
                        ],
                        'correct_option_id' => 'A',
                        'feedback_mdx' => 'Retro',
                        'feedback_html' => '<p>Retro</p>',
                        'feedback_summary' => 'Respuesta',
                        'feedback_assets' => [],
                        'feedback_blocks' => [],
                        'concepts_mdx' => 'Conceptos',
                        'concepts_html' => '<p>Conceptos</p>',
                        'concepts_summary' => 'Conceptos relacionados',
                        'concepts_assets' => [],
                        'concepts_blocks' => [],
                        'app_payload_version' => 1,
                    ],
                ],
            ],
        ];

        $service = app(AssessmentTemplateManifestSyncService::class);
        $result = $service->sync($entries, Carbon::now(), false, false);

        $this->assertSame(1, $result['created']);

        $template = AssessmentTemplate::query()
            ->where('external_id', $workshop->external_id)
            ->first();

        $this->assertNotNull($template);
        $this->assertSame('study', $template->default_mode);
        $this->assertSame('/saber/quimica/la-materia/taller', $template->route);
        $this->assertSame('image', $template->asset_refs[0]['type'] ?? null);

        $context = AssessmentContext::query()
            ->where('template_id', $template->id)
            ->where('external_id', 'ctx-1')
            ->first();

        $question = AssessmentQuestion::query()
            ->where('template_id', $template->id)
            ->where('external_id', '1')
            ->first();

        $this->assertNotNull($context);
        $this->assertNotNull($question);
        $this->assertSame('<p>Contexto de prueba</p>', $context->context_html);
        $this->assertSame('/saber/quimica/la-materia/taller#pregunta-1', $question->source_slug);
        $this->assertSame('<span><strong>Correcta</strong></span>', $question->options[0]['text_html'] ?? null);
        $this->assertDatabaseHas('assessment_question_contexts', [
            'question_id' => $question->id,
            'context_id' => $context->id,
            'order_base' => 1,
        ]);
    }

    public function test_it_allows_same_local_question_id_in_different_templates_without_global_collision(): void
    {
        $workshopA = Workshop::query()->create([
            'external_id' => 'content:simulacro:quimica/a/taller',
            'content_external_id' => 'content:simulacro:quimica/a/taller',
            'content_type' => 'simulacro',
            'title' => 'Simulacro A',
            'route' => '/simulacros/quimica/a/taller',
            'area_slug' => 'quimica',
            'unidad_slug' => 'a',
            'access_tier' => 'premium',
            'is_published' => true,
            'total_questions' => 1,
            'total_assets' => 0,
            'assets' => [],
            'questions' => [],
            'metadata' => [],
            'synced_at' => now(),
        ]);

        $workshopB = Workshop::query()->create([
            'external_id' => 'content:simulacro:quimica/b/taller',
            'content_external_id' => 'content:simulacro:quimica/b/taller',
            'content_type' => 'simulacro',
            'title' => 'Simulacro B',
            'route' => '/simulacros/quimica/b/taller',
            'area_slug' => 'quimica',
            'unidad_slug' => 'b',
            'access_tier' => 'premium',
            'is_published' => true,
            'total_questions' => 1,
            'total_assets' => 0,
            'assets' => [],
            'questions' => [],
            'metadata' => [],
            'synced_at' => now(),
        ]);

        $questionPayload = [
            [
                'id' => 'S1-95',
                'order' => 95,
                'order_base' => 95,
                'source_slug' => '/simulacros/quimica/demo/taller#pregunta-S1-95',
                'meta' => [],
                'stem_mdx' => 'Pregunta repetida localmente',
                'stem_html' => '<p>Pregunta repetida localmente</p>',
                'stem_assets' => [],
                'stem_blocks' => [],
                'options' => [
                    ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                    ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
                ],
                'correct_option_id' => 'A',
                'feedback_mdx' => 'Retro',
                'feedback_html' => '<p>Retro</p>',
                'feedback_summary' => 'Respuesta',
                'feedback_assets' => [],
                'feedback_blocks' => [],
                'concepts_mdx' => '',
                'concepts_html' => '',
                'concepts_summary' => 'Conceptos relacionados',
                'concepts_assets' => [],
                'concepts_blocks' => [],
                'app_payload_version' => 1,
            ],
        ];

        $service = app(AssessmentTemplateManifestSyncService::class);
        $service->sync([
            $workshopA->external_id => [
                'id' => $workshopA->external_id,
                'content_external_id' => $workshopA->content_external_id,
                'content_type' => 'simulacro',
                'route' => $workshopA->route,
                'title' => $workshopA->title,
                'area_slug' => $workshopA->area_slug,
                'unidad_slug' => $workshopA->unidad_slug,
                'access_tier' => 'premium',
                'published' => true,
                'stats' => ['total_questions' => 1, 'total_assets' => 0],
                'assets' => [],
                'asset_refs' => [],
                'contexts' => [],
                'question_context_links' => [],
                'questions' => $questionPayload,
            ],
            $workshopB->external_id => [
                'id' => $workshopB->external_id,
                'content_external_id' => $workshopB->content_external_id,
                'content_type' => 'simulacro',
                'route' => $workshopB->route,
                'title' => $workshopB->title,
                'area_slug' => $workshopB->area_slug,
                'unidad_slug' => $workshopB->unidad_slug,
                'access_tier' => 'premium',
                'published' => true,
                'stats' => ['total_questions' => 1, 'total_assets' => 0],
                'assets' => [],
                'asset_refs' => [],
                'contexts' => [],
                'question_context_links' => [],
                'questions' => $questionPayload,
            ],
        ], Carbon::now(), false, false);

        $questions = AssessmentQuestion::query()
            ->where('external_id', 'S1-95')
            ->with('template')
            ->orderBy('template_id')
            ->get();

        $this->assertCount(2, $questions);
        $this->assertNotSame($questions[0]->source_key, $questions[1]->source_key);
    }

    public function test_it_preserves_backend_taxonomy_when_the_template_is_resynced(): void
    {
        $workshop = Workshop::query()->create([
            'external_id' => 'content:saber:quimica/resync/taller',
            'content_external_id' => 'content:saber:quimica/resync/taller',
            'content_type' => 'taller',
            'title' => 'Taller Resync',
            'route' => '/saber/quimica/resync/taller',
            'area_slug' => 'quimica',
            'unidad_slug' => 'resync',
            'access_tier' => 'premium',
            'is_published' => true,
            'total_questions' => 1,
            'total_assets' => 0,
            'assets' => [],
            'questions' => [],
            'metadata' => [],
            'synced_at' => now(),
        ]);

        $entries = [
            $workshop->external_id => [
                'id' => $workshop->external_id,
                'content_external_id' => $workshop->content_external_id,
                'content_type' => 'taller',
                'route' => $workshop->route,
                'title' => $workshop->title,
                'area_slug' => $workshop->area_slug,
                'unidad_slug' => $workshop->unidad_slug,
                'access_tier' => 'premium',
                'published' => true,
                'stats' => ['total_questions' => 1, 'total_assets' => 0],
                'assets' => [],
                'asset_refs' => [],
                'contexts' => [],
                'question_context_links' => [],
                'questions' => [[
                    'id' => 'Q-1',
                    'order' => 1,
                    'order_base' => 1,
                    'source_slug' => '/saber/quimica/resync/taller#pregunta-Q-1',
                    'meta' => ['fuente' => 'ICFES'],
                    'stem_mdx' => 'Pregunta base',
                    'stem_html' => '<p>Pregunta base</p>',
                    'stem_assets' => [],
                    'stem_blocks' => [],
                    'options' => [
                        ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                        ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
                    ],
                    'correct_option_id' => 'A',
                    'feedback_mdx' => 'Retro',
                    'feedback_html' => '<p>Retro</p>',
                    'feedback_summary' => 'Respuesta',
                    'feedback_assets' => [],
                    'feedback_blocks' => [],
                    'concepts_mdx' => '',
                    'concepts_html' => '',
                    'concepts_summary' => 'Conceptos relacionados',
                    'concepts_assets' => [],
                    'concepts_blocks' => [],
                    'app_payload_version' => 1,
                ]],
            ],
        ];

        $service = app(AssessmentTemplateManifestSyncService::class);
        $service->sync($entries, Carbon::now(), false, false);

        $question = AssessmentQuestion::query()->where('external_id', 'Q-1')->firstOrFail();
        $question->forceFill([
            'topic' => 'Enlaces',
            'unit_label' => 'Química general',
            'subtopic' => 'Enlace iónico',
            'origin_label' => 'Clasificación docente',
            'editorial_status' => 'ready',
            'tags' => ['ionico', 'repaso'],
            'teacher_notes' => 'Usar en evaluación corta.',
        ])->save();

        $service->sync($entries, Carbon::now()->addMinute(), false, false);

        $question->refresh();

        $this->assertSame('Enlaces', $question->topic);
        $this->assertSame('Química general', $question->unit_label);
        $this->assertSame('Enlace iónico', $question->subtopic);
        $this->assertSame('Clasificación docente', $question->origin_label);
        $this->assertSame('ready', $question->editorial_status);
        $this->assertSame(['ionico', 'repaso'], $question->tags);
        $this->assertSame('Usar en evaluación corta.', $question->teacher_notes);
    }
}
