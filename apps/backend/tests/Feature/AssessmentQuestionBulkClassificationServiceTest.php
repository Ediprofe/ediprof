<?php

namespace Tests\Feature;

use App\Models\AssessmentContext;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentSubject;
use App\Models\AssessmentTemplate;
use App\Models\AssessmentUnit;
use App\Services\Content\AssessmentQuestionBulkClassificationService;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\DB;
use Tests\TestCase;

class AssessmentQuestionBulkClassificationServiceTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_classifies_questions_in_bulk_and_can_sync_linked_contexts(): void
    {
        $service = app(AssessmentQuestionBulkClassificationService::class);

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
            'label' => 'Simulacro 3',
            'is_active' => true,
        ]);
        $template = AssessmentTemplate::query()->create([
            'external_id' => 'template-1',
            'title' => 'Plantilla de prueba',
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
            'title' => 'Contexto',
            'subject_id' => $subject->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'draft',
            'order_base' => 1,
            'is_active' => true,
        ]);

        $question = AssessmentQuestion::query()->create([
            'template_id' => $template->id,
            'external_id' => 'Q1',
            'subject_id' => $subject->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'draft',
            'order_base' => 1,
            'is_active' => true,
            'stem_html' => '<p>Pregunta</p>',
            'options' => [],
        ]);

        DB::table('assessment_question_contexts')->insert([
            'question_id' => $question->id,
            'context_id' => $context->id,
            'order_base' => 1,
            'created_at' => now(),
            'updated_at' => now(),
        ]);

        $summary = $service->classify(
            AssessmentQuestion::query()->whereKey($question->id)->get(),
            [
                'unit_id' => $unit->id,
                'topic' => 'Materia y energía',
                'subtopic' => 'Solubilidad',
                'editorial_status' => 'review',
                'tags' => ['soluciones', 'saber11'],
                'sync_linked_contexts' => true,
            ],
        );

        $this->assertSame(1, $summary['questions_updated']);
        $this->assertSame(1, $summary['contexts_updated']);
        $this->assertSame(0, $summary['questions_skipped_unit_mismatch']);

        $this->assertDatabaseHas('assessment_questions', [
            'id' => $question->id,
            'unit_id' => $unit->id,
            'topic' => 'Materia y energía',
            'subtopic' => 'Solubilidad',
            'editorial_status' => 'review',
        ]);

        $this->assertDatabaseHas('assessment_contexts', [
            'id' => $context->id,
            'unit_id' => $unit->id,
            'topic' => 'Materia y energía',
            'subtopic' => 'Solubilidad',
            'editorial_status' => 'review',
        ]);
    }

    public function test_it_skips_questions_when_the_selected_unit_belongs_to_another_subject(): void
    {
        $service = app(AssessmentQuestionBulkClassificationService::class);

        $chemistry = AssessmentSubject::query()->create([
            'label' => 'Química',
            'is_active' => true,
        ]);
        $math = AssessmentSubject::query()->create([
            'label' => 'Matemáticas',
            'is_active' => true,
        ]);
        $mathUnit = AssessmentUnit::query()->create([
            'subject_id' => $math->id,
            'label' => 'Álgebra',
            'is_active' => true,
        ]);
        $origin = AssessmentOriginCollection::query()->create([
            'origin_type' => 'simulacro',
            'label' => 'Simulacro 4',
            'is_active' => true,
        ]);
        $template = AssessmentTemplate::query()->create([
            'external_id' => 'template-2',
            'title' => 'Plantilla 2',
            'subject_id' => $chemistry->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'draft',
            'access_tier' => 'private',
            'is_published' => false,
            'total_questions' => 1,
            'total_assets' => 0,
        ]);
        $question = AssessmentQuestion::query()->create([
            'template_id' => $template->id,
            'external_id' => 'Q2',
            'subject_id' => $chemistry->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'draft',
            'order_base' => 1,
            'is_active' => true,
            'stem_html' => '<p>Pregunta</p>',
            'options' => [],
        ]);

        $summary = $service->classify(
            AssessmentQuestion::query()->whereKey($question->id)->get(),
            [
                'unit_id' => $mathUnit->id,
                'sync_linked_contexts' => false,
            ],
        );

        $this->assertSame(0, $summary['questions_updated']);
        $this->assertSame(1, $summary['questions_skipped_unit_mismatch']);

        $this->assertDatabaseHas('assessment_questions', [
            'id' => $question->id,
            'unit_id' => null,
        ]);
    }
}
