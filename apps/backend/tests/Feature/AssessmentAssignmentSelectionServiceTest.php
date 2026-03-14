<?php

namespace Tests\Feature;

use App\Models\AssessmentAssignment;
use App\Models\AssessmentAssignmentQuestion;
use App\Models\AssessmentContext;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentTemplate;
use App\Models\Course;
use App\Services\Assessments\AssessmentAssignmentSelectionService;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class AssessmentAssignmentSelectionServiceTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_adds_the_full_shared_context_bundle_when_one_question_is_selected(): void
    {
        [$assignment, $questionOne, $questionTwo, $questionThree] = $this->makeAssignmentWithSharedContext();

        $service = app(AssessmentAssignmentSelectionService::class);
        $service->addQuestionSelection($assignment, $questionOne);
        $service->addQuestionSelection($assignment, $questionThree);

        $rows = AssessmentAssignmentQuestion::query()
            ->where('assignment_id', $assignment->id)
            ->with('question')
            ->orderBy('order_base')
            ->get();

        $this->assertCount(3, $rows);
        $this->assertSame(['q-1', 'q-2', 'q-3'], $rows->pluck('question.external_id')->all());
        $this->assertNotNull($rows[0]->selection_group_key);
        $this->assertSame($rows[0]->selection_group_key, $rows[1]->selection_group_key);
        $this->assertNotSame($rows[1]->selection_group_key, $rows[2]->selection_group_key);
    }

    /**
     * @return array{0:AssessmentAssignment,1:AssessmentQuestion,2:AssessmentQuestion,3:AssessmentQuestion}
     */
    private function makeAssignmentWithSharedContext(): array
    {
        $course = Course::query()->create([
            'name' => 'ICFES 11°1',
            'slug' => 'icfes-11-1',
            'school_year' => '2026',
            'is_active' => true,
        ]);

        $template = AssessmentTemplate::query()->create([
            'external_id' => 'content:simulacro:quimica/demo/taller',
            'title' => 'Simulacro demo',
            'source_content_type' => 'simulacro',
            'default_mode' => 'simulacro',
            'route' => '/simulacros/quimica/demo/taller',
            'area_slug' => 'quimica',
            'unidad_slug' => 'demo',
            'access_tier' => 'premium',
            'is_published' => true,
            'total_questions' => 3,
            'total_assets' => 0,
            'assets' => [],
            'asset_refs' => [],
            'metadata' => [],
            'synced_at' => now(),
        ]);

        $context = AssessmentContext::query()->create([
            'template_id' => $template->id,
            'external_id' => 'ctx-1',
            'title' => 'Panaderías',
            'order_base' => 1,
            'is_active' => true,
            'context_mdx' => 'Contexto',
            'context_html' => '<p>Contexto</p>',
            'context_assets' => [],
            'context_blocks' => [],
            'metadata' => [],
        ]);

        $questionOne = $this->makeQuestion($template, 'q-1', 1);
        $questionTwo = $this->makeQuestion($template, 'q-2', 2);
        $questionThree = $this->makeQuestion($template, 'q-3', 3);

        $questionOne->contexts()->attach($context->id, ['order_base' => 1]);
        $questionTwo->contexts()->attach($context->id, ['order_base' => 1]);

        $assignment = AssessmentAssignment::query()->create([
            'course_id' => $course->id,
            'template_id' => $template->id,
            'title' => 'Evaluación demo',
            'mode' => AssessmentAssignment::MODE_EVALUATION,
            'status' => AssessmentAssignment::STATUS_DRAFT,
        ]);

        return [$assignment, $questionOne, $questionTwo, $questionThree];
    }

    private function makeQuestion(AssessmentTemplate $template, string $externalId, int $orderBase): AssessmentQuestion
    {
        return AssessmentQuestion::query()->create([
            'template_id' => $template->id,
            'external_id' => $externalId,
            'order_base' => $orderBase,
            'source_slug' => '/simulacros/quimica/demo/taller#pregunta-'.$externalId,
            'is_active' => true,
            'meta' => [],
            'stem_mdx' => 'Pregunta '.$externalId,
            'stem_html' => '<p>Pregunta '.$externalId.'</p>',
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
        ]);
    }
}
