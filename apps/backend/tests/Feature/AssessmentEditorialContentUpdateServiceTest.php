<?php

namespace Tests\Feature;

use App\Models\AssessmentContext;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentQuestionOption;
use App\Models\AssessmentSubject;
use App\Models\AssessmentTemplate;
use App\Models\AssessmentUnit;
use App\Services\Content\AssessmentEditorialContentUpdateService;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class AssessmentEditorialContentUpdateServiceTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_updates_the_real_content_of_a_context_and_recompiles_it(): void
    {
        $service = app(AssessmentEditorialContentUpdateService::class);

        $subject = AssessmentSubject::query()->create([
            'label' => 'Biología',
            'is_active' => true,
        ]);
        $unit = AssessmentUnit::query()->create([
            'subject_id' => $subject->id,
            'label' => 'Ecosistemas',
            'is_active' => true,
        ]);
        $origin = AssessmentOriginCollection::query()->create([
            'origin_type' => 'simulacro',
            'label' => 'Simulacro ecológico',
            'is_active' => true,
        ]);
        $template = AssessmentTemplate::query()->create([
            'external_id' => 'template-editorial-1',
            'title' => 'Bloque ecológico',
            'subject_id' => $subject->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'draft',
            'access_tier' => 'private',
            'is_published' => false,
            'total_questions' => 1,
            'total_assets' => 0,
        ]);
        $context = AssessmentContext::query()->create([
            'template_id' => $template->id,
            'external_id' => 'ctx-1',
            'title' => 'Contexto inicial',
            'subject_id' => $subject->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'draft',
            'order_base' => 1,
            'is_active' => true,
            'context_mdx' => 'Texto inicial.',
            'context_html' => '<p>Texto inicial.</p>',
        ]);

        $updated = $service->updateContext($context, [
            'title' => 'Bosque húmedo tropical',
            'subject_id' => $subject->id,
            'unit_id' => $unit->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'review',
            'tags' => ['ecosistemas', 'saber11'],
            'teacher_notes' => 'Revisado para once.',
            'context_mdx' => "Se observa una **red trófica** con varias especies.\n\nEl caso ocurre en un bosque húmedo.",
        ]);

        $this->assertSame('Bosque húmedo tropical', $updated->title);
        $this->assertSame($unit->id, $updated->unit_id);
        $this->assertSame('review', $updated->editorial_status);
        $this->assertSame(['ecosistemas', 'saber11'], $updated->tags);
        $this->assertStringContainsString('<strong>red trófica</strong>', (string) $updated->context_html);
        $this->assertSame(
            "Se observa una **red trófica** con varias especies.\n\nEl caso ocurre en un bosque húmedo.",
            $updated->context_mdx
        );
    }

    public function test_it_updates_question_content_options_and_feedback_consistently(): void
    {
        $service = app(AssessmentEditorialContentUpdateService::class);

        $subject = AssessmentSubject::query()->create([
            'label' => 'Química',
            'is_active' => true,
        ]);
        $unit = AssessmentUnit::query()->create([
            'subject_id' => $subject->id,
            'label' => 'Disoluciones',
            'is_active' => true,
        ]);
        $origin = AssessmentOriginCollection::query()->create([
            'origin_type' => 'simulacro',
            'label' => 'Simulacro 2',
            'is_active' => true,
        ]);
        $template = AssessmentTemplate::query()->create([
            'external_id' => 'template-editorial-2',
            'title' => 'Bloque de solubilidad',
            'subject_id' => $subject->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'draft',
            'access_tier' => 'private',
            'is_published' => false,
            'total_questions' => 1,
            'total_assets' => 0,
        ]);
        $question = AssessmentQuestion::query()->create([
            'template_id' => $template->id,
            'external_id' => 'Q1',
            'subject_id' => $subject->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'draft',
            'order_base' => 1,
            'is_active' => true,
            'stem_mdx' => 'Pregunta inicial',
            'stem_html' => '<p>Pregunta inicial</p>',
            'options' => [],
            'correct_option_id' => 'A',
        ]);

        AssessmentQuestionOption::query()->create([
            'question_id' => $question->id,
            'option_id' => 'A',
            'order_base' => 1,
            'is_correct' => true,
            'plain_text' => 'Opción inicial A',
            'html_web' => '<p>Opción inicial A</p>',
        ]);
        AssessmentQuestionOption::query()->create([
            'question_id' => $question->id,
            'option_id' => 'B',
            'order_base' => 2,
            'is_correct' => false,
            'plain_text' => 'Opción inicial B',
            'html_web' => '<p>Opción inicial B</p>',
        ]);

        $updated = $service->updateQuestion($question, [
            'subject_id' => $subject->id,
            'unit_id' => $unit->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'ready',
            'tags' => ['solubilidad', 'curvas'],
            'teacher_notes' => 'Ajustada para simulacro.',
            'stem_mdx' => '¿Qué ocurre con la **solubilidad** del azúcar cuando aumenta la temperatura?',
            'options_editor' => [
                ['option_id' => 'A', 'text' => 'Disminuye.'],
                ['option_id' => 'B', 'text' => 'Aumenta.'],
                ['option_id' => 'C', 'text' => 'Permanece igual.'],
                ['option_id' => 'D', 'text' => 'Desaparece la disolución.'],
            ],
            'correct_option_id' => 'B',
            'feedback_mdx' => "La respuesta correcta es **B**.\n\nA mayor temperatura, la solubilidad del azúcar aumenta.",
            'concepts_mdx' => "## Conceptos relacionados\nCurva de solubilidad y solución saturada.",
        ]);

        $this->assertSame($unit->id, $updated->unit_id);
        $this->assertSame('B', $updated->correct_option_id);
        $this->assertSame('ready', $updated->editorial_status);
        $this->assertSame(['solubilidad', 'curvas'], $updated->tags);
        $this->assertStringContainsString('<strong>solubilidad</strong>', (string) $updated->stem_html);
        $this->assertStringContainsString('<strong>B</strong>', (string) $updated->feedback_html);
        $this->assertStringContainsString('Curva de solubilidad', (string) $updated->concepts_html);
        $this->assertNotNull($updated->feedback_summary);
        $this->assertNotNull($updated->concepts_summary);

        $this->assertCount(4, $updated->questionOptions);
        $this->assertDatabaseHas('assessment_question_options', [
            'question_id' => $question->id,
            'option_id' => 'B',
            'is_correct' => true,
        ]);
        $this->assertDatabaseMissing('assessment_question_options', [
            'question_id' => $question->id,
            'option_id' => 'A',
            'is_correct' => true,
        ]);
        $this->assertSame('B', $updated->options[1]['id']);
        $this->assertTrue((bool) $updated->options[1]['is_correct']);
    }
}
