<?php

namespace Tests\Feature;

use App\Services\Content\AiQuestionDraftParser;
use RuntimeException;
use Tests\TestCase;

class AiQuestionDraftParserTest extends TestCase
{
    public function test_it_parses_a_single_question_draft_into_structured_sections(): void
    {
        $parser = app(AiQuestionDraftParser::class);

        $result = $parser->parse(<<<'MD'
## Contexto
Observa la siguiente relación entre partículas subatómicas.

## Pregunta 1
¿Cuál es la relación correcta?

### Opciones
A. **Opción A**
B. Opción B con $A = p^+ + n$
C. ~~Opción incorrecta~~
D. ==Opción destacada==

### Correcta
B

### Retroalimentación
La masa atómica se calcula como $A = p^+ + n$.

### Conceptos relacionados
- Masa atómica
- Protones
- Neutrones
MD);

        $this->assertSame('ai_question_draft_v1', $result['schema']);
        $this->assertCount(1, $result['contexts']);
        $this->assertCount(1, $result['questions']);
        $this->assertCount(1, $result['question_context_links']);

        $question = $result['questions'][0];
        $this->assertSame('1', $question['id']);
        $this->assertSame('¿Cuál es la relación correcta?', $question['stem_mdx']);
        $this->assertSame('B', $question['correct_option_id']);
        $this->assertCount(4, $question['options']);
        $this->assertSame('**Opción A**', $question['options'][0]['text']);
        $this->assertStringContainsString('Masa atómica', $question['concepts_mdx']);
    }

    public function test_it_rejects_a_question_without_context(): void
    {
        $parser = app(AiQuestionDraftParser::class);

        $this->expectException(RuntimeException::class);
        $this->expectExceptionMessage('no tiene contexto');

        $parser->parse(<<<'MD'
## Pregunta 1
¿Cuál es la relación correcta?

### Opciones
A. **Opción A**
B. Opción B
C. Opción C
D. Opción D

### Correcta
B
MD);
    }

    public function test_it_parses_shared_context_and_links_it_to_multiple_questions(): void
    {
        $parser = app(AiQuestionDraftParser::class);

        $result = $parser->parse(<<<'MD'
## Contexto compartido: Separación de mezclas
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

## Pregunta 96
¿Qué variable cambió durante el procedimiento?

### Opciones
A. La altura del papel
B. El solvente
C. La posición de las manchas
D. El número atómico

### Correcta
C
MD);

        $this->assertCount(1, $result['contexts']);
        $this->assertCount(2, $result['questions']);
        $this->assertCount(2, $result['question_context_links']);

        $context = $result['contexts'][0];
        $this->assertSame('shared-context-separacion-de-mezclas', $context['external_id']);
        $this->assertStringContainsString('Una muestra M1, M2 y M3', $context['context_mdx']);

        $this->assertSame('95', $result['questions'][0]['id']);
        $this->assertSame('96', $result['questions'][1]['id']);
        $this->assertSame('95', $result['question_context_links'][0]['question_external_id']);
        $this->assertSame('96', $result['question_context_links'][1]['question_external_id']);
        $this->assertSame('shared-context-separacion-de-mezclas', $result['question_context_links'][0]['context_external_id']);
    }

    public function test_it_treats_a_top_level_context_heading_as_shared_context_for_following_questions(): void
    {
        $parser = app(AiQuestionDraftParser::class);

        $result = $parser->parse(<<<'MD'
## Contexto
Una muestra M1, M2 y M3 se analiza en laboratorio.

## Pregunta 95
¿Cuál inferencia es válida?

### Opciones
A. M1
B. M2
C. M3
D. Ninguna

### Correcta
C
MD);

        $this->assertCount(1, $result['contexts']);
        $this->assertSame('Contexto 1', $result['contexts'][0]['title']);
        $this->assertTrue($result['contexts'][0]['metadata']['inferred_from_generic_context_heading']);
        $this->assertCount(1, $result['question_context_links']);
        $this->assertSame('shared-context-1', $result['question_context_links'][0]['context_external_id']);
        $this->assertSame('95', $result['questions'][0]['id']);
    }

    public function test_it_rejects_a_question_without_valid_options(): void
    {
        $parser = app(AiQuestionDraftParser::class);

        $this->expectException(RuntimeException::class);
        $this->expectExceptionMessage('Las opciones del borrador deben venir en formato');

        $parser->parse(<<<'MD'
## Pregunta 1
Texto de prueba

### Opciones
Solo una línea sin opciones válidas

### Correcta
A
MD);
    }
}
