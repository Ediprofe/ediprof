<?php

namespace Tests\Feature;

use App\Filament\Resources\AssessmentContexts\AssessmentContextResource;
use App\Filament\Resources\AssessmentQuestions\AssessmentQuestionResource;
use App\Models\AssessmentContext;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentSubject;
use App\Models\AssessmentTemplate;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class AssessmentEditorialEditPagesTest extends TestCase
{
    use RefreshDatabase;

    public function test_context_edit_page_shows_real_editor_fields(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);
        [$context] = $this->createEditorialRecords();

        $this->actingAs($admin, 'web')
            ->get(AssessmentContextResource::getUrl('edit', ['record' => $context], panel: 'admin'))
            ->assertOk()
            ->assertSee('Contexto (Markdown)')
            ->assertSee('Título del contexto');
    }

    public function test_question_edit_page_shows_real_editor_fields(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);
        [, $question] = $this->createEditorialRecords();

        $this->actingAs($admin, 'web')
            ->get(AssessmentQuestionResource::getUrl('edit', ['record' => $question], panel: 'admin'))
            ->assertOk()
            ->assertSee('Enunciado (Markdown)')
            ->assertSee('Retroalimentación / solución guiada (Markdown)')
            ->assertSee('Conceptos relacionados (Markdown)');
    }

    /**
     * @return array{0:AssessmentContext,1:AssessmentQuestion}
     */
    private function createEditorialRecords(): array
    {
        $subject = AssessmentSubject::query()->create([
            'label' => 'Naturales',
            'is_active' => true,
        ]);
        $origin = AssessmentOriginCollection::query()->create([
            'origin_type' => 'simulacro',
            'label' => 'Banco de prueba',
            'is_active' => true,
        ]);
        $template = AssessmentTemplate::query()->create([
            'external_id' => 'template-edit-pages',
            'title' => 'Bloque de prueba',
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
            'external_id' => 'ctx-edit',
            'title' => 'Contexto de prueba',
            'subject_id' => $subject->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'draft',
            'order_base' => 1,
            'is_active' => true,
            'context_mdx' => 'Texto de contexto.',
            'context_html' => '<p>Texto de contexto.</p>',
        ]);

        $question = AssessmentQuestion::query()->create([
            'template_id' => $template->id,
            'external_id' => 'Q-edit',
            'subject_id' => $subject->id,
            'origin_collection_id' => $origin->id,
            'editorial_status' => 'draft',
            'order_base' => 1,
            'is_active' => true,
            'stem_mdx' => '¿Pregunta de prueba?',
            'stem_html' => '<p>¿Pregunta de prueba?</p>',
            'options' => [],
            'correct_option_id' => 'A',
        ]);

        return [$context, $question];
    }
}
