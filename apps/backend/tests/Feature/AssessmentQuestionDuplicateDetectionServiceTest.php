<?php

namespace Tests\Feature;

use App\Models\AssessmentContext;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentTemplate;
use App\Services\Content\AssessmentQuestionDuplicateDetectionService;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class AssessmentQuestionDuplicateDetectionServiceTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_marks_exact_duplicates_and_skips_them_from_save(): void
    {
        [$template, $question] = $this->createExistingQuestion();

        $service = app(AssessmentQuestionDuplicateDetectionService::class);

        $draft = [
            'schema' => 'ai_question_draft_v1',
            'contexts' => [
                [
                    'external_id' => 'shared-context-1',
                    'title' => 'Contexto 1',
                    'context_mdx' => 'Texto base de prueba.',
                ],
            ],
            'questions' => [
                [
                    'id' => 'Q1',
                    'order_base' => 1,
                    'stem_mdx' => '¿Cuál es la capital de Francia?',
                    'correct_option_id' => 'B',
                    'options' => [
                        ['option_id' => 'A', 'text' => 'Madrid'],
                        ['option_id' => 'B', 'text' => 'París'],
                        ['option_id' => 'C', 'text' => 'Roma'],
                        ['option_id' => 'D', 'text' => 'Lisboa'],
                    ],
                ],
            ],
            'question_context_links' => [
                [
                    'question_external_id' => 'Q1',
                    'context_external_id' => 'shared-context-1',
                    'order_base' => 1,
                ],
            ],
        ];

        $annotated = $service->annotateDraft($draft);

        $this->assertSame('exact_duplicate', $annotated['questions'][0]['duplicate_status']);
        $this->assertSame('skip_duplicate', $annotated['questions'][0]['save_decision']);
        $this->assertSame($question->id, data_get($annotated, 'questions.0.exact_match.question_id'));
        $this->assertSame($template->title, data_get($annotated, 'questions.0.exact_match.block_title'));
        $this->assertSame(1, data_get($annotated, 'duplicate_summary.exact_duplicates'));
        $this->assertSame(0, data_get($annotated, 'duplicate_summary.savable_questions'));

        $savable = $service->extractSavableDraft($annotated);

        $this->assertSame([], $savable['questions']);
        $this->assertSame([], $savable['contexts']);
        $this->assertSame([], $savable['question_context_links']);
    }

    public function test_it_suggests_similar_questions_without_blocking_save(): void
    {
        $this->createExistingQuestion([
            'stem_mdx' => '¿Cuál es la principal causa del efecto invernadero?',
            'options' => [
                ['id' => 'A', 'text' => 'El aumento del oxígeno en la atmósfera'],
                ['id' => 'B', 'text' => 'La acumulación de gases como el dióxido de carbono'],
                ['id' => 'C', 'text' => 'La disminución de la lluvia anual'],
                ['id' => 'D', 'text' => 'La rotación de la Tierra'],
            ],
            'correct_option_id' => 'B',
        ]);

        $service = app(AssessmentQuestionDuplicateDetectionService::class);

        $draft = [
            'schema' => 'ai_question_draft_v1',
            'contexts' => [
                [
                    'external_id' => 'shared-context-1',
                    'title' => 'Contexto 1',
                    'context_mdx' => 'Texto base de prueba.',
                ],
            ],
            'questions' => [
                [
                    'id' => 'Q1',
                    'order_base' => 1,
                    'stem_mdx' => '¿Qué provoca el efecto invernadero en la atmósfera?',
                    'correct_option_id' => 'B',
                    'options' => [
                        ['option_id' => 'A', 'text' => 'El exceso de oxígeno disponible'],
                        ['option_id' => 'B', 'text' => 'La acumulación de gases como el dióxido de carbono'],
                        ['option_id' => 'C', 'text' => 'La ausencia de nubes en la troposfera'],
                        ['option_id' => 'D', 'text' => 'La inclinación del eje terrestre'],
                    ],
                ],
            ],
            'question_context_links' => [
                [
                    'question_external_id' => 'Q1',
                    'context_external_id' => 'shared-context-1',
                    'order_base' => 1,
                ],
            ],
        ];

        $annotated = $service->annotateDraft($draft);

        $this->assertSame('similar_candidates', $annotated['questions'][0]['duplicate_status']);
        $this->assertSame('new', $annotated['questions'][0]['save_decision']);
        $this->assertGreaterThan(0, count($annotated['questions'][0]['similar_candidates']));
        $this->assertSame(1, data_get($annotated, 'duplicate_summary.questions_with_similar_candidates'));
        $this->assertSame(1, data_get($annotated, 'duplicate_summary.savable_questions'));
    }

    /**
     * @param  array<string, mixed>  $overrides
     * @return array{0: AssessmentTemplate, 1: AssessmentQuestion}
     */
    private function createExistingQuestion(array $overrides = []): array
    {
        $origin = AssessmentOriginCollection::query()->create([
            'origin_type' => 'simulacro',
            'label' => 'Simulacro existente',
            'is_active' => true,
        ]);

        $template = AssessmentTemplate::query()->create([
            'external_id' => 'template-001',
            'title' => 'Bloque existente',
            'subject_label' => 'Ciencias',
            'unit_label' => 'Indagación',
            'source_content_type' => 'simulacro',
            'origin_collection_id' => $origin->id,
            'origin_label' => $origin->label,
            'editorial_status' => 'draft',
            'access_tier' => 'private',
            'is_published' => false,
            'total_questions' => 1,
            'total_assets' => 0,
            'assets' => [],
            'asset_refs' => [],
            'metadata' => ['source' => 'test'],
            'synced_at' => now(),
        ]);

        $context = AssessmentContext::query()->create([
            'template_id' => $template->id,
            'external_id' => 'shared-context-1',
            'title' => 'Contexto 1',
            'subject_label' => 'Ciencias',
            'origin_collection_id' => $origin->id,
            'origin_label' => $origin->label,
            'editorial_status' => 'draft',
            'context_mdx' => 'Texto base de prueba.',
            'context_html' => '<p>Texto base de prueba.</p>',
            'context_assets' => [],
            'context_blocks' => [],
            'metadata' => ['source' => 'test'],
            'is_active' => true,
            'order_base' => 1,
        ]);

        $question = AssessmentQuestion::query()->create(array_merge([
            'template_id' => $template->id,
            'external_id' => 'Q1',
            'order_base' => 1,
            'subject_label' => 'Ciencias',
            'unit_label' => 'Indagación',
            'origin_collection_id' => $origin->id,
            'origin_label' => $origin->label,
            'editorial_status' => 'draft',
            'stem_mdx' => '¿Cuál es la capital de Francia?',
            'stem_html' => '<p>¿Cuál es la capital de Francia?</p>',
            'stem_assets' => [],
            'stem_blocks' => [],
            'options' => [
                ['id' => 'A', 'text' => 'Madrid', 'is_correct' => false],
                ['id' => 'B', 'text' => 'París', 'is_correct' => true],
                ['id' => 'C', 'text' => 'Roma', 'is_correct' => false],
                ['id' => 'D', 'text' => 'Lisboa', 'is_correct' => false],
            ],
            'correct_option_id' => 'B',
            'feedback_mdx' => null,
            'feedback_html' => null,
            'feedback_summary' => null,
            'feedback_assets' => [],
            'feedback_blocks' => [],
            'concepts_mdx' => null,
            'concepts_html' => null,
            'concepts_summary' => null,
            'concepts_assets' => [],
            'concepts_blocks' => [],
            'meta' => ['source' => 'test'],
            'app_payload_version' => 2,
            'is_active' => true,
        ], $overrides));

        $question->contexts()->attach($context->id, [
            'order_base' => 1,
        ]);

        return [$template->fresh(), $question->fresh()];
    }
}
