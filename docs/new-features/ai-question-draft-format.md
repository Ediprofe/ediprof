# AI Question Draft Format v1

## Objetivo
Permitir una entrada rápida desde ChatGPT, Gemini u otra IA general sin obligar al docente a escribir `MDX`, HTML o JSON.

La idea del MVP es:
- pegar un borrador estructurado en markdown
- separar ese borrador en contexto, pregunta, opciones, correcta, retroalimentación y conceptos
- transformar luego ese borrador al modelo canónico de Laravel

## Regla de producto
La entrada rápida puede ser markdown.

La fuente de verdad final no es ese markdown, sino Laravel.

## Formato recomendado: pregunta simple

```md
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
```

## Formato recomendado: contexto compartido

```md
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
```

## Qué hace el parser v1
- reconoce `Contexto compartido`
- reconoce `Pregunta`
- reconoce `Opciones`
- reconoce `Correcta`
- reconoce `Retroalimentación`
- reconoce `Conceptos relacionados`
- crea `question_context_links` cuando un contexto compartido aplica a varias preguntas

Esto mantiene la misma idea importante del sistema viejo:
- el contexto compartido no depende de posición implícita
- queda como entidad explícita con referencias claras

## Atajo aceptado en el MVP
También aceptamos un `## Contexto` al inicio del borrador.

Si aparece fuera de una pregunta, Laravel lo interpreta como contexto compartido para las preguntas que sigan después.

## Limitaciones deliberadas del MVP
- las opciones deben venir como `A. ...`, `B. ...`
- la correcta debe venir como una letra clara
- no soporta todavía edición libre tipo WYSIWYG
- no soporta todavía imágenes embebidas dentro de este borrador IA v1

## Evolución prevista
1. pegar borrador IA
2. parser Laravel separa secciones
3. pantalla de revisión rápida
4. guardar en modelo canónico
5. luego añadir upload de assets y bloques de imagen/ecuación con preview
