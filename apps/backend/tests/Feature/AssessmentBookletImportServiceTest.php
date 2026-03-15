<?php

namespace Tests\Feature;

use App\Models\AssessmentBooklet;
use App\Models\AssessmentOriginCollection;
use App\Models\AssessmentSubject;
use App\Models\AssessmentUnit;
use App\Models\User;
use App\Services\Content\AiQuestionDraftParser;
use App\Services\Content\AssessmentBookletImportService;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class AssessmentBookletImportServiceTest extends TestCase
{
    use RefreshDatabase;

    public function test_it_imports_a_multisection_booklet_with_global_origin_and_deferred_units(): void
    {
        $parser = app(AiQuestionDraftParser::class);
        $importer = app(AssessmentBookletImportService::class);
        $admin = User::factory()->create([
            'role' => 'admin',
            'member_status' => 'approved',
        ]);

        $math = AssessmentSubject::query()->create([
            'label' => 'Matemáticas',
            'is_active' => true,
        ]);
        $reading = AssessmentSubject::query()->create([
            'label' => 'Lectura crítica',
            'is_active' => true,
        ]);
        $mathUnit = AssessmentUnit::query()->create([
            'subject_id' => $math->id,
            'label' => 'Álgebra básica',
            'is_active' => true,
        ]);
        $origin = AssessmentOriginCollection::query()->create([
            'origin_type' => 'simulacro',
            'label' => 'Simulacro 2 institucional',
            'is_active' => true,
        ]);

        $booklet = $importer->import(
            [
                'title' => 'Simulacro 2',
                'booklet_type' => 'simulacro',
                'origin_collection_id' => $origin->id,
                'school_year' => '2026',
            ],
            [
                [
                    'title' => 'Matemáticas',
                    'subject_id' => $math->id,
                    'default_unit_id' => $mathUnit->id,
                    'parsed_draft' => $parser->parse(<<<'MD'
## Pregunta 1
¿Cuál es el valor de x si 2x = 10?

### Opciones
A. 2
B. 3
C. 5
D. 10

### Correcta
C
MD),
                ],
                [
                    'title' => 'Lectura crítica',
                    'subject_id' => $reading->id,
                    'parsed_draft' => $parser->parse(<<<'MD'
## Contexto compartido: Texto informativo
Se analiza un texto breve.

## Pregunta 2
¿Cuál es la intención principal del autor?

### Opciones
A. Describir un experimento.
B. Convencer al lector.
C. Informar sobre un hecho.
D. Narrar una anécdota.

### Correcta
C
MD),
                ],
            ],
            $admin,
        );

        $this->assertInstanceOf(AssessmentBooklet::class, $booklet);
        $this->assertSame('Simulacro 2', $booklet->title);
        $this->assertSame($origin->id, $booklet->origin_collection_id);
        $this->assertSame(2, $booklet->total_sections);
        $this->assertSame(2, $booklet->total_questions);

        $this->assertDatabaseHas('assessment_booklets', [
            'id' => $booklet->id,
            'origin_collection_id' => $origin->id,
            'total_sections' => 2,
            'total_questions' => 2,
        ]);

        $this->assertDatabaseHas('assessment_booklet_sections', [
            'booklet_id' => $booklet->id,
            'title' => 'Matemáticas',
            'subject_id' => $math->id,
            'default_unit_id' => $mathUnit->id,
            'total_questions' => 1,
        ]);

        $this->assertDatabaseHas('assessment_booklet_sections', [
            'booklet_id' => $booklet->id,
            'title' => 'Lectura crítica',
            'subject_id' => $reading->id,
            'default_unit_id' => null,
            'total_questions' => 1,
        ]);

        $this->assertDatabaseHas('assessment_questions', [
            'external_id' => '1',
            'subject_id' => $math->id,
            'unit_id' => $mathUnit->id,
            'origin_collection_id' => $origin->id,
        ]);

        $this->assertDatabaseHas('assessment_questions', [
            'external_id' => '2',
            'subject_id' => $reading->id,
            'unit_id' => null,
            'origin_collection_id' => $origin->id,
        ]);

        $this->assertDatabaseHas('assessment_booklet_questions', [
            'booklet_id' => $booklet->id,
            'order_base' => 1,
        ]);

        $this->assertDatabaseHas('assessment_booklet_questions', [
            'booklet_id' => $booklet->id,
            'order_base' => 2,
        ]);
    }
}
