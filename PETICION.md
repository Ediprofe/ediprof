QUIERO UN SISTEMA QUE ME PERMITA CREAR ÍTEMS TIPO PRUEBA SABER, OPCIÓN MÚLTIPLE CON ÚNICA RESPUESTA, Y QUE ESTE PUEDA GENERAR PRESENTACIONES TIPO EN HTML O LO QUE TÚ CONSIDERES MÁS INTERACTIVO, TAMBIEN QUE PERMITA GENERAR TALLER EN PDF O EN WORD, CON LA IDEA DE QUE MIS ESTUDIANTES TENGAN UN PDF DE ESTUDIO Y UN PDF TALLER, TIPO ALGO ASÍ, Y QUE A MÍ ME RESULTA MUY FÁCIL POR EJEMPLO CONSTRUIR TALLERES A PARTIR DE PREGUNTAS QUE VOY ENCONTRANDO DE DIFERENTES FUENTES O DIFERNETES AÑOS....LE COMENTÉ LA SITUACIÓN A CHATGPT Y ÉL ME HA DADO ESTE MENSAJE:


# Proyecto: Sistema de Talleres Educativos Interactivos
## Fuente primaria en MDX → HTML interactivo + PDF estudiable

---

## 1. Objetivo general

Diseñar y desarrollar un sistema web educativo que permita:

- Mantener **una única fuente primaria de contenido** (MDX).
- Generar automáticamente:
  - **Presentaciones HTML interactivas** para uso en clase.
  - **PDFs de alta calidad** para práctica y estudio autónomo.
- Organizar preguntas reales (uso interno) y preguntas propias/liberadas.
- Facilitar aprendizaje activo, discusión guiada y estudio independiente.
- Mantener control, trazabilidad y escalabilidad del banco de ítems.

---

## 2. Principios de diseño (decisiones clave)

1. **La fuente primaria nunca se edita en HTML o PDF**
   - Todo nace del MDX.
2. **El contenido manda; la tecnología se adapta**
3. **Contexto + ítems viven juntos**
   - No se modulariza el contexto si no se reutiliza.
4. **Un archivo = una unidad pedagógica real**
5. **Separación clara entre contenido, organización y salida**
6. **Sistema preparado para migrar a ítems propios/liberados**
7. **Uso interno, circulación controlada**
8. **PDF estable y HTML interactivo desde la misma fuente**

---

## 3. Unidad atómica de contenido: ItemSet

### Definición
Un **ItemSet** es un archivo único que contiene:

- (Opcional) Un **contexto**
- **1 a 4 ítems** asociados a ese contexto
- Cada ítem incluye:
  - Enunciado
  - Opciones
  - Respuesta correcta
  - Explicación breve
  - (Opcional) feedback por distractor

### Formato
- Extensión: `.mdx`
- Contenido semántico + bloques estructurados
- Sin frontmatter para clasificación (área/unidad/año/fuente)

---

## 4. Organización del contenido (detección por estructura)

La **clasificación NO se hace con frontmatter**, sino por:

- Estructura de carpetas
- Archivos `meta.json` por nivel

### Jerarquía

/content
/<area>
meta.json
/<unidad>
meta.json
/collections
/<coleccion>
meta.json
itemset-01.mdx
itemset-02.mdx


### Significado de niveles

- **Área**: ciencias, matemáticas, química, física
- **Unidad**: célula, materia, cinemática, funciones
- **Colección**:
  - Año real de prueba (ej. icfes-2023)
  - Fuente externa (ej. instruimos, ael-mendoza)
  - Propias / liberadas
  - Simulacros, diagnósticos, práctica

---

## 5. Archivos meta.json

### Área (`/ciencias/meta.json`)
```json
{
  "type": "area",
  "id": "ciencias",
  "title": "Ciencias Naturales"
}
Unidad (/ciencias/celula/meta.json)
{
  "type": "unit",
  "id": "celula",
  "title": "La célula"
}
Colección (/collections/icfes-2023/meta.json)
{
  "type": "collection",
  "id": "icfes-2023",
  "origin": "externa",
  "visibility": "private",
  "notes": "Uso interno. No distribuir."
}
6. Estructura interna de un ItemSet (MDX)
Ejemplo conceptual:

## Contexto
Texto, imagen, gráfico o tabla que sirve de base.

---

:::item{key="q1" answer="B"}
### Enunciado
Pregunta basada en el contexto.

- A. ...
- B. ...
- C. ...
- D. ...

:::
Explicación breve de la respuesta correcta.
:::

:::
A: Error típico A.
B: Correcto.
C: Error típico C.
D: Error típico D.
:::
:::
Reglas
El contexto pertenece SOLO a ese ItemSet.

Los ítems no se reutilizan fuera del ItemSet.

La numeración global NO se escribe en el contenido.

7. Taller (Quiz)
Definición
Un taller es una selección de ItemSets, no de ítems sueltos.

Formato
Archivo .yml

Define:

Qué ItemSets incluir

Cuántos ítems totales

Qué salidas generar

Ejemplo
id: ciencias-celula-taller-10
title: "Taller Célula – 10 ítems"
source:
  area: ciencias
  unit: celula
  collection: icfes-2023

pick:
  - itemset-01
  - itemset-02
  - itemset-03

constraints:
  target_items: 10

outputs:
  html_present:
    mode: teacher

  pdf_practice:
    include_answers: false

  pdf_study:
    include_answers: true
    answers_at_end: true
8. Numeración de ítems
Cada ítem tiene un identificador local (q1, q2, etc.).

El sistema asigna numeración global según:

Orden del taller

Cantidad de ítems por ItemSet

El build falla si no se cumple target_items.

9. Productos finales (outputs)
9.1 HTML interactivo (presentación)
Uso en clase (proyector)

Una “slide” por:

Contexto

Ítem

Funciones:

Siguiente / anterior

Revelar respuesta

Mostrar explicación

(Opcional) feedback por distractor

No público

Idealmente local o en red interna

9.2 PDF de práctica (sin respuestas)
Para imprimir o compartir

Una pregunta por página

Sin clave

9.3 PDF de estudio (con respuestas)
Misma estructura

Al final:

Clave de respuestas

Explicación breve por ítem

Ideal para estudio autónomo

Compatible con NotebookLM y tutores IA

10. Pipeline técnico resumido
ItemSet (.mdx)
   ↓
Taller (.yml)
   ↓
Assembler (numera, valida)
   ↓
Render HTML (presentación)
   ↓
Render HTML (print)
   ↓
Export PDF (Playwright)
11. Consideraciones legales y éticas
Material real de pruebas:

Uso interno únicamente

No publicación

No distribución masiva

Recomendaciones:

Marcas de agua en PDF

HTML solo en clase

Migrar progresivamente a ítems propios o liberados

El sistema debe permitir coexistencia de:

Colecciones reales (privadas)

Colecciones propias (públicas)

12. Objetivo pedagógico
Fomentar:

Aprendizaje activo

Discusión guiada

Metacognición

Superar la lógica “tipo Kahoot” superficial:

Feedback por distractor

Explicaciones breves

Uso en cuaderno abierto

Un mismo taller sirve para:

Clase

Práctica

Estudio autónomo

13. Estado actual del diseño
Modelo conceptual: ✅ definido

Estructura de contenido: ✅ definida

Contrato de archivos: ✅ definido

Siguiente pasos:

Parser de ItemSet MDX

Assembler de Taller

Renderer HTML (presentación)

Renderer PDF (print)


---


QUIERO QUE EVALÚES ESO QUE PROPONE CHAT GPT, CON BASE EN LA ESRUCTURA DE ESTE PROYECTO, EL CUÁL TIENE PUNTO DE ENTRADA EN CLAUDE.md, pero tambien puedes leer la carpeta .agents para contexto en profundidad.

QUIERO QUE EVALÚES ESA PROPUESTA DE CHAT GPT ASÍ COMO STACK Y REALICES TU PROPIA PROPUESTA. TEN EN CUENTA TOMAR COSAS BUENAS QUE HACE ESTE PROYECTO, TIPO LO DE INFERIR A PARTIR DE LA ORGANIZACIÓN DE CARPETAS, Y DEMÁS QUE CONSIDERES. CREA EL PLAN Y YO MIRO SI LO APRUEBO O NO. EN PRIMERA MEDIDA PIENSO CREARLO COMO UN RPOYECTO INDEPENDEINTE A ESTE, PERO BUENO TÚ CON TU CRITERIO EVALÚAS. 

ADELANTE.