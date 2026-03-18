<?php

namespace Tests\Feature;

use App\Filament\Resources\AssessmentQuestions\AssessmentQuestionResource;
use App\Filament\Resources\AssessmentQuestions\Pages\CreateAssessmentQuestion;
use App\Models\AssessmentContext;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentQuestion;
use App\Models\AssessmentQuestionOption;
use App\Models\AssessmentSubject;
use App\Models\AssessmentTemplate;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Livewire\Livewire;
use Tests\TestCase;

class AssessmentQuestionCreatePageTest extends TestCase
{
    use RefreshDatabase;

    public function test_admin_can_open_manual_question_create_page(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        $this->actingAs($admin, 'web')
            ->get(AssessmentQuestionResource::getUrl('create', panel: 'admin'))
            ->assertOk()
            ->assertSee('Agregar pregunta')
            ->assertSee('Contexto base del bloque')
            ->assertSee('Enunciado (Markdown)');
    }

    public function test_manual_question_create_builds_block_context_and_question(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        $subject = AssessmentSubject::query()->create([
            'label' => 'Química',
            'is_active' => true,
        ]);

        $origin = AssessmentOriginCollection::query()->create([
            'subject_id' => $subject->id,
            'origin_type' => 'simulacro',
            'label' => 'Simulacro docente',
            'is_active' => true,
        ]);

        $this->actingAs($admin, 'web');

        Livewire::test(CreateAssessmentQuestion::class)
            ->set('data.block_title', 'Bloque manual de prueba')
            ->set('data.context_title', 'Contexto de laboratorio')
            ->set('data.context_mdx', 'Una muestra se analiza en laboratorio.')
            ->set('data.stem_mdx', '¿Cuál muestra tiene más componentes?')
            ->set('data.options_editor', [
                ['option_id' => 'A', 'text' => 'M1'],
                ['option_id' => 'B', 'text' => 'M2'],
                ['option_id' => 'C', 'text' => 'M3'],
                ['option_id' => 'D', 'text' => 'M4'],
            ])
            ->set('data.correct_option_id', 'C')
            ->set('data.feedback_mdx', 'La muestra M3 reúne la mayor cantidad de componentes observables.')
            ->set('data.concepts_mdx', '- Separación de mezclas')
            ->set('data.subject_id', $subject->id)
            ->set('data.origin_collection_id', $origin->id)
            ->set('data.editorial_status', 'draft')
            ->call('create')
            ->assertHasNoFormErrors();

        $this->assertDatabaseCount(AssessmentTemplate::class, 1);
        $this->assertDatabaseCount(AssessmentContext::class, 1);
        $this->assertDatabaseCount(AssessmentQuestion::class, 1);
        $this->assertDatabaseCount(AssessmentQuestionOption::class, 4);

        $question = AssessmentQuestion::query()->with(['template', 'contexts', 'questionOptions'])->firstOrFail();

        $this->assertSame('Bloque manual de prueba', $question->template?->title);
        $this->assertSame('¿Cuál muestra tiene más componentes?', $question->stem_mdx);
        $this->assertSame('C', $question->correct_option_id);
        $this->assertCount(1, $question->contexts);
        $this->assertSame('Contexto de laboratorio', $question->contexts->first()?->title);
        $this->assertCount(4, $question->questionOptions);
    }
}
