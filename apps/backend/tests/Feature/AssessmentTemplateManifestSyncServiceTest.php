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
                            ['id' => 'A', 'text' => 'Correcta', 'is_correct' => true],
                            ['id' => 'B', 'text' => 'Incorrecta', 'is_correct' => false],
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
        $this->assertDatabaseHas('assessment_question_contexts', [
            'question_id' => $question->id,
            'context_id' => $context->id,
            'order_base' => 1,
        ]);
    }
}
