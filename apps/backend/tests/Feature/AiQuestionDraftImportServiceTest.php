<?php

namespace Tests\Feature;

use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentSubject;
use App\Models\AssessmentTemplate;
use App\Models\AssessmentUnit;
use App\Models\User;
use App\Services\Content\AiQuestionDraftImportService;
use App\Services\Content\AiQuestionDraftParser;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class AiQuestionDraftImportServiceTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_imports_a_parsed_draft_into_canonical_assessment_tables(): void
    {
        $parser = app(AiQuestionDraftParser::class);
        $importer = app(AiQuestionDraftImportService::class);
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);
        $subject = AssessmentSubject::query()->create([
            'label' => 'Química',
            'is_active' => true,
        ]);
        $unit = AssessmentUnit::query()->create([
            'subject_id' => $subject->id,
            'label' => 'Separación de mezclas',
            'is_active' => true,
        ]);
        $origin = AssessmentOriginCollection::query()->create([
            'subject_id' => $subject->id,
            'origin_type' => 'simulacro',
            'label' => 'Simulacro 1 Química 11',
            'is_active' => true,
        ]);

        $draft = $parser->parse(<<<'MD'
## Contexto
Una muestra M1, M2 y M3 se analiza en laboratorio.

## Pregunta 95
¿Cuál inferencia es válida?

### Opciones
A. La muestra M1 y M2 tienen igual composición.
B. La muestra M3 tiene más componentes que M1 y M2.
C. La muestra M2 es la de mayor complejidad.
D. No se puede concluir nada.

### Correcta
B

### Retroalimentación
Explica por qué la opción B es válida.
MD);

        $template = $importer->import($draft, [
            'subject_id' => $subject->id,
            'unit_id' => $unit->id,
            'origin_collection_id' => $origin->id,
        ], 'Borrador IA de prueba', $admin);

        $this->assertInstanceOf(AssessmentTemplate::class, $template);
        $this->assertSame('Borrador IA de prueba', $template->title);
        $this->assertDatabaseHas('assessment_templates', [
            'id' => $template->id,
            'subject_id' => $subject->id,
            'source_content_type' => 'simulacro',
            'subject_label' => 'Química',
            'unit_id' => $unit->id,
            'unit_label' => 'Separación de mezclas',
            'origin_collection_id' => $origin->id,
            'origin_label' => 'Simulacro 1 Química 11',
            'editorial_status' => 'draft',
            'is_published' => false,
        ]);
        $this->assertDatabaseHas('assessment_contexts', [
            'template_id' => $template->id,
            'title' => 'Contexto 1',
            'subject_id' => $subject->id,
            'subject_label' => 'Química',
            'unit_id' => $unit->id,
            'unit_label' => 'Separación de mezclas',
            'origin_collection_id' => $origin->id,
            'origin_label' => 'Simulacro 1 Química 11',
            'editorial_status' => 'draft',
        ]);
        $this->assertDatabaseHas('assessment_questions', [
            'template_id' => $template->id,
            'external_id' => '95',
            'subject_id' => $subject->id,
            'subject_label' => 'Química',
            'unit_id' => $unit->id,
            'unit_label' => 'Separación de mezclas',
            'origin_collection_id' => $origin->id,
            'origin_label' => 'Simulacro 1 Química 11',
            'correct_option_id' => 'B',
            'editorial_status' => 'draft',
        ]);

        $question = $template->questions()->firstOrFail();

        $this->assertDatabaseHas('assessment_question_options', [
            'question_id' => $question->id,
            'option_id' => 'B',
            'is_correct' => true,
        ]);
        $this->assertDatabaseCount('assessment_question_contexts', 1);
    }

    public function test_it_allows_importing_a_draft_without_initial_unit_assignment(): void
    {
        $parser = app(AiQuestionDraftParser::class);
        $importer = app(AiQuestionDraftImportService::class);
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);
        $subject = AssessmentSubject::query()->create([
            'label' => 'Biología',
            'is_active' => true,
        ]);
        $origin = AssessmentOriginCollection::query()->create([
            'origin_type' => 'simulacro',
            'label' => 'Simulacro 2 multiarea',
            'is_active' => true,
        ]);

        $draft = $parser->parse(<<<'MD'
## Contexto
Se observa una célula procariota al microscopio.

## Pregunta 14
¿Qué característica diferencia a una célula procariota?

### Opciones
A. Tiene núcleo definido.
B. No tiene material genético.
C. No tiene núcleo definido.
D. Tiene cloroplastos.

### Correcta
C
MD);

        $template = $importer->import($draft, [
            'subject_id' => $subject->id,
            'origin_collection_id' => $origin->id,
        ], 'Borrador IA sin unidad', $admin);

        $this->assertDatabaseHas('assessment_templates', [
            'id' => $template->id,
            'subject_id' => $subject->id,
            'unit_id' => null,
            'origin_collection_id' => $origin->id,
        ]);

        $this->assertDatabaseHas('assessment_questions', [
            'template_id' => $template->id,
            'external_id' => '14',
            'subject_id' => $subject->id,
            'unit_id' => null,
            'origin_collection_id' => $origin->id,
        ]);
    }
}
