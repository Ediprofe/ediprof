<?php

namespace Tests\Feature;

use App\Filament\Pages\ImportAiQuestionDraft;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentSubject;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Livewire\Livewire;
use Tests\TestCase;

class ImportAiQuestionDraftPageTest extends TestCase
{
    use RefreshDatabase;

    public function test_admin_can_open_ai_draft_import_page(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        $this->actingAs($admin, 'web')
            ->get(ImportAiQuestionDraft::getUrl(panel: 'admin'))
            ->assertOk()
            ->assertSee('Agregar preguntas al banco');
    }

    public function test_it_converts_a_shared_context_draft_inside_filament_page(): void
    {
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        $this->actingAs($admin, 'web');

        $subject = AssessmentSubject::query()->create([
            'label' => 'Química',
            'is_active' => true,
        ]);

        $origin = AssessmentOriginCollection::query()->create([
            'subject_id' => $subject->id,
            'origin_type' => 'simulacro',
            'label' => 'Simulacro de prueba',
            'is_active' => true,
        ]);

        Livewire::test(ImportAiQuestionDraft::class)
            ->set('data.subject_id', $subject->id)
            ->set('data.origin_collection_id', $origin->id)
            ->set('data.draft_markdown', <<<'MD'
## Contexto compartido: Reacción química
Se comparan tres muestras.

## Pregunta 1
¿Cuál muestra tiene más componentes?

### Opciones
A. M1
B. M2
C. M3
D. Ninguna

### Correcta
C
MD)
            ->call('convertDraft')
            ->assertSet('parserError', null)
            ->assertSet('preview.schema', 'ai_question_draft_v1')
            ->assertSet('preview.contexts.0.external_id', 'shared-context-reaccion-quimica')
            ->assertSet('preview.questions.0.correct_option_id', 'C')
            ->assertSet('preview.question_context_links.0.context_external_id', 'shared-context-reaccion-quimica');
    }
}
