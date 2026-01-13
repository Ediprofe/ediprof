---
description: Pipeline completo de generación de contenido educativo en 5 etapas globs: ["src/content/**/*.md"]
---

# 📚 Workflow: Generación de Contenido Educativo

Este documento define el proceso completo para generar lecciones educativas de alta calidad.

---

## 📋 Resumen de las 5 Etapas

| Etapa | Nombre | Responsable | Entregable |
|-------|--------|-------------|------------|
| 1 | Planeador Docente | Agente IA | Árbol de carpetas aprobado |
| 2 | Generador de Lecciones | Agente IA | Lecciones con ASCII art para ilustraciones |
| 3 | Generador de Ilustraciones | Agente IA | SVGs a partir del ASCII art |
| 4 | Evaluador Pedagógico | Agente IA | Lecciones corregidas + ilustraciones ajustadas |
| 5 | Evaluación Final | Humano | Aprobación definitiva |

> ⚠️ **IMPORTANTE:** Cada etapa debe completarse antes de pasar a la siguiente. Las ilustraciones NO se generan en la Etapa 2, solo se describen en ASCII art.

---

# ETAPA 1: PLANEADOR DOCENTE 📋

## Objetivo
Estructurar el árbol de carpetas y archivos para un CAPÍTULO completo.

## Proceso

1. **Recibir** el nombre del capítulo y contexto
2. **Proponer** el árbol de carpetas con temas y lecciones
3. **Indicar** brevemente qué conceptos cubrirá cada lección
4. **Presentar** para APROBACIÓN del usuario

## Formato de Entrega

```
CAPÍTULO: [Nombre]
├── 01-tema-nombre/
│   ├── _meta.json
│   ├── 01-leccion-nombre.md → [conceptos que cubre]
│   └── 02-leccion-nombre.md → [conceptos que cubre]
├── 02-tema-nombre/
│   ├── _meta.json
│   ├── 01-leccion-nombre.md → [conceptos que cubre]
│   └── ...
```

## Ejemplo

```
CAPÍTULO: Geometría Plana
├── 01-conceptos-basicos/
│   ├── _meta.json
│   ├── 01-punto-recta-plano.md → Definiciones, notación, representación
│   ├── 02-segmentos-y-rayos.md → Segmento, rayo, longitud, punto medio
│   └── 03-angulos.md → Definición, clasificación, medición
├── 02-triangulos/
│   ├── _meta.json
│   ├── 01-clasificacion.md → Por lados, por ángulos
│   ├── 02-propiedades.md → Suma de ángulos, desigualdad triangular
│   └── 03-puntos-notables.md → Baricentro, ortocentro, circuncentro, incentro
```

> ⚠️ **CRÍTICO:** NO generar contenido hasta que el árbol sea APROBADO por el usuario.

---

# ETAPA 2: GENERADOR DE LECCIONES 📝

## Objetivo
Generar MASIVAMENTE todas las lecciones del árbol aprobado.

## Reglas Generales

- Una lección por archivo .md
- Cada lección = **LIBRETO completo** para el mejor profesor
- **SIN gráficos SVG** (se agregan en Etapa 3)
- **Las ilustraciones se describen en ASCII art** para que el agente de Etapa 3 las convierta
- Tablas y LaTeX SÍ permitidos

### 💡 ¿Por qué ASCII art en lugar de SVG?

El agente de Etapa 2 se enfoca en **contenido pedagógico**, no en código SVG. Las ilustraciones en ASCII art:

1. **Son fáciles de generar** para cualquier modelo de IA
2. **Comunican claramente** qué debe mostrar la ilustración
3. **Permiten revisión rápida** del contenido antes de invertir en SVGs
4. **Separan responsabilidades** entre agentes especializados

### Formato de ASCII Art para Ilustraciones

```markdown
<!-- ILUSTRACIÓN: [descripción de qué debe mostrar] -->

```
[Diagrama en ASCII que muestre visualmente el concepto]
[Incluir etiquetas, flechas, y elementos relevantes]
```

```

**Ejemplo:**
```markdown
<!-- ILUSTRACIÓN: Modelo atómico con niveles de energía -->

```
    Nivel 4 (N) ═════════════  Más lejos, más energía
    Nivel 3 (M) ═════════════
    Nivel 2 (L) ═════════════
    Nivel 1 (K) ═════════════  Más cerca, menos energía
         ⊕ NÚCLEO ⊕
```
```

---

## Estructura de Cada Lección

### 1. INTRODUCCIÓN MOTIVADORA

```markdown
# Título de la Lección

¿Alguna vez te has preguntado [pregunta enganchadora]?

En esta lección vas a aprender:
- Concepto 1
- Concepto 2
- Concepto 3

---

## 📋 Resumen Rápido

| Concepto | Fórmula/Definición |
|----------|-------------------|
| ... | ... |

<!-- ILUSTRACIÓN: Diagrama visual que muestre todos los conceptos -->

> 💡 **Tip:** [Regla mnemotécnica o truco para recordar]

---
```

### 2. DESARROLLO DE CONCEPTOS

```markdown
## 📖 Concepto 1: [Nombre]

[Definición simple en 1-2 oraciones]

### Ejemplo 1

[Enunciado]

**Solución:**

Paso 1: ...
Paso 2: ...

$$
\boxed{\text{Resultado}}
$$

### Ejemplo 2

[Otro ejemplo resuelto paso a paso]

<!-- ILUSTRACIÓN: Visual del concepto -->

---

## 📖 Concepto 2: [Nombre]

[Repetir estructura...]
```

### 3. CIERRE

```markdown
---

## 📋 Resumen

| Concepto | Punto clave |
|----------|-------------|
| ... | ... |

---

## 📝 Ejercicios de Práctica

**Ejercicio 1:** [Enunciado]

<details>
<summary>Ver solución</summary>

[Solución paso a paso]

$$
\boxed{\text{Respuesta}}
$$

</details>

**Ejercicio 2:** [Enunciado]

<details>
<summary>Ver solución</summary>

[Solución]

</details>
```

---

## Filosofía Anti-Abrumamiento

> **PRINCIPIO:** El estudiante no debe ver mucho texto antes de entender visualmente qué va a aprender.

### Patrón Correcto

```
1️⃣ Título + 1 línea intro  
2️⃣ Tabla resumen (Cheat Sheet)  
3️⃣ <!-- ILUSTRACIÓN --> JUSTO DESPUÉS  
4️⃣ Tip/regla para recordar  
5️⃣ --- (separador)
6️⃣ Detalles de cada concepto
```

### Ejemplos

❌ **MALO:**
```markdown
# Título
[200 líneas de teoría]
[Tabla resumen al final]
[Ilustración al final]
```

✅ **BUENO:**
```markdown
# Título
[1 línea de intro]

## 📋 Resumen Rápido
[Tabla]

<!-- ILUSTRACIÓN: Vista general -->

> 💡 Tip para recordar

---

## Detalles...
```

---

## Reglas de Redacción

| ✅ HACER | ❌ EVITAR |
|----------|-----------|
| Oraciones cortas y directas | Párrafos densos sin pausas |
| Una idea por párrafo | Múltiples conceptos mezclados |
| Segunda persona ("vas a aprender") | Lenguaje impersonal |
| Ejemplos antes que teoría | Definiciones sin contexto |
| Preguntas retóricas | Entrar directo en fórmulas |
| Transiciones ("Ahora que sabes X, veamos Y") | Saltar entre temas |

---

## Restricciones Técnicas

### LaTeX
```markdown
✅ Bloque: $$x = \frac{-b}{2a}$$
✅ Inline: La fórmula es $a^2 + b^2 = c^2$
❌ En títulos: ## La fórmula $x^2$ (NO)
❌ Sintaxis alternativa: \[...\] o \(...\)
```

### Emojis
```markdown
✅ En subtítulos: ## 📖 Definición
❌ En H1: # 📖 Título Principal (NO)
```

### Moneda
```markdown
❌ El costo es $50 (se confunde con LaTeX)
✅ El costo es 50 USD
✅ El costo es 50 pesos
```

---

## Archivo _meta.json

Crear para cada tema:

```json
{
  "name": "Nombre del Tema con Tildes"
}
```

---

# ETAPA 3: GENERADOR DE ILUSTRACIONES 🎨

## Objetivo
Convertir todo el ASCII art de las lecciones en ilustraciones SVG o Rough.js de alta calidad.

---

## Proceso de Conversión ASCII → SVG

### Paso 1: Identificar ASCII art

Buscar en las lecciones:
- Bloques de código con diagramas ASCII
- Marcadores `<!-- ILUSTRACIÓN: ... -->`
- Cualquier representación visual en texto plano

### Paso 2: Elegir tecnología

Consultar el árbol de decisión en CLAUDE.md:

| Tipo de ASCII art | Tecnología | Workflow |
|-------------------|------------|----------|
| Diagramas conceptuales | **PNG de tablet** | Ver CLAUDE.md |
| Niveles de energía, orbitales | **SVG estático** | Spec + Renderer |
| Geometría exacta | **GeometrySpec** | `.agent/workflows/geometry-exact.md` |
| Gráficas de funciones | **CartesianSpec** | `.agent/workflows/cartesian-spec.md` |
| Tabla periódica, tendencias | **SVG estático** | Spec + Renderer |

### Paso 3: Generar la ilustración

1. **Crear spec JSON** (si aplica) en `specs/[materia]/[tema]/`
2. **Ejecutar renderer** o escribir Rough.js inline
3. **Guardar SVG** en `public/images/[materia]/`

### Paso 4: Reemplazar en el markdown

**Reemplazar el ASCII art con:**
```markdown
![Descripción](/images/materia/archivo.svg)
```

**O con wrapper para contexto:**
```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <img src="/images/materia/archivo.svg" alt="Descripción" style="width: 100%; height: auto;" />
</div>
```

---

## Reglas de Calidad

> ⚠️ **MÍNIMO UNA ILUSTRACIÓN POR CONCEPTO**
> 
> Concepto = cada sección con título Markdown (##, ###)
> 
> **EXCEPCIÓN:** Sección de "Ejercicios de Práctica"

### Criterios de Ilustración Correcta

| Criterio | Descripción |
|----------|-------------|
| **Auto-explicativa** | Se entiende SIN leer el texto alrededor |
| **Etiquetas claras** | Todo elemento tiene nombre visible |
| **Colores distintivos** | Usar paleta de CLAUDE.md |
| **Consistente** | Mismo estilo visual en todo el tema |

---

## Verificar Estilo Visual

### Modo Claro/Oscuro

Todo elemento debe verse bien en AMBOS modos.

✅ **Seguro:**
- Markdown nativo (tablas, blockquotes, listas)
- Canvas (Rough.js)
- Fondos oscuros: `background: #1e293b`
- Colores saturados con alto contraste

❌ **Evitar:**
- Fondos claros con texto gris
- Colores de texto sin especificar

---

# ETAPA 4: EVALUADOR PEDAGÓGICO 🎓

## Objetivo
Revisar TODO el contenido con mentalidad del **mejor profesor del colegio** y corregir lo necesario.

---

## 4.1 Evaluar con Criterios Pedagógicos

### Características del Mejor Profesor

| Característica | Pregunta de Evaluación |
|---------------|------------------------|
| **SIMPLICIDAD** | ¿Explica conceptos complejos de forma brutalmente simple? |
| **CLARIDAD** | ¿Cada oración tiene un solo propósito, sin ambigüedades? |
| **ORDEN** | ¿La secuencia de ideas es lógica y natural? |
| **MOTIVADOR** | ¿Engancha al estudiante con preguntas y contexto real? |
| **INDUCTIVO** | ¿Va de lo particular a lo general, de ejemplos a teoría? |
| **PROGRESIVO** | ¿Una idea a la vez, sin saltos? |

### Checklist de Evaluación

| Aspecto | Pregunta | ✅/❌ |
|---------|----------|------|
| **Motivación** | ¿Hay pregunta enganchadora al inicio? | |
| **Anti-abrumamiento** | ¿Cheat Sheet + Ilustración juntos al inicio? | |
| **Claridad** | ¿Se entiende a la primera lectura? | |
| **Progresión** | ¿Va de simple a complejo? | |
| **Ejemplos** | ¿Mínimo 2 por concepto, paso a paso? | |
| **Visuales** | ¿1 ilustración por concepto? | |
| **Transiciones** | ¿Conexiones claras entre secciones? | |
| **Práctica** | ¿Ejercicios con soluciones en `<details>`? | |
| **Contenido correcto** | ¿La información es precisa y sin errores? | |

---

## 4.2 Acciones Correctivas

### Si detecta problemas, el agente DEBE:

1. **Reorganizar lecciones** si el orden no es lógico
2. **Reescribir secciones** si no son claras
3. **Agregar ejemplos** si faltan
4. **Corregir errores** de contenido
5. **Ajustar ilustraciones** si no son auto-explicativas
6. **Generar ilustraciones faltantes** para conceptos sin visual
7. **Reacomodar ilustraciones existentes** si están mal ubicadas

### Formato de Reporte

```markdown
## 🔧 Correcciones Realizadas

### Lección: [nombre]

1. **Problema:** [descripción]
   **Acción:** [qué se corrigió]

2. **Problema:** [descripción]
   **Acción:** [qué se corrigió]

### Ilustraciones Ajustadas:
- [lista de SVGs modificados/agregados]
```

---

## 4.3 Revisión de Ilustraciones

El evaluador también revisa las ilustraciones generadas en Etapa 3:

| Verificar | Acción si falla |
|-----------|----------------|
| ¿Ilustración es auto-explicativa? | Agregar etiquetas, leyendas |
| ¿Está en el lugar correcto? | Mover antes/después |
| ¿Falta ilustración para un concepto? | Generar nueva |
| ¿Hay ilustraciones redundantes? | Eliminar o consolidar |
| ¿El estilo es consistente? | Regenerar con estilo correcto |

---

# ETAPA 5: EVALUACIÓN FINAL DEL HUMANO ✅

## Objetivo
Aprobación definitiva por parte del usuario antes de publicar.

---

## Qué Revisa el Humano

1. **Precisión del contenido** - ¿La información es correcta?
2. **Calidad pedagógica** - ¿La lección enseña bien?
3. **Claridad visual** - ¿Las ilustraciones ayudan a entender?
4. **Experiencia de usuario** - ¿Se ve bien en la web?
5. **Aprobación para publicar** - ¿Listo para producción?

## Entregable del Agente al Humano

```markdown
## 📋 Resumen para Revisión Humana

### Lecciones Generadas:
- [ ] Lección 1: [nombre] - [URL local]
- [ ] Lección 2: [nombre] - [URL local]
- ...

### Ilustraciones Generadas:
- [cantidad] SVGs en `public/images/[materia]/`
- [cantidad] Rough.js inline

### Correcciones Realizadas en Etapa 4:
- [resumen de cambios importantes]

### Puntos a Validar:
1. [aspecto específico que requiere atención]
2. [otro aspecto]
```

---

# ✅ CHECKLISTS POR ETAPA

## Después de Etapa 1 (Planeación)

- [ ] Árbol de carpetas propuesto
- [ ] Conceptos por lección identificados
- [ ] **APROBACIÓN del usuario obtenida**

## Después de Etapa 2 (Generación de Lecciones)

- [ ] `_meta.json` en cada tema
- [ ] Intro motivadora en cada lección
- [ ] Cheat Sheet al inicio
- [ ] **ASCII art** para cada ilustración (NO SVG aún)
- [ ] Mínimo 2 ejemplos por concepto
- [ ] Ejercicios con `<details>`
- [ ] Sin LaTeX en títulos
- [ ] Sin emojis en H1

## Después de Etapa 3 (Generación de Ilustraciones)

- [ ] Todo ASCII art convertido a SVG/Rough.js
- [ ] Mínimo 1 ilustración por concepto (excepto ejercicios)
- [ ] Tecnología correcta según árbol de decisión
- [ ] IDs únicos en gráficos inline
- [ ] Funciona en modo claro y oscuro
- [ ] Specs guardados en `specs/`
- [ ] SVGs guardados en `public/images/`

## Después de Etapa 4 (Evaluación Pedagógica)

- [ ] Evaluación con criterios del "mejor profesor" completada
- [ ] Problemas detectados corregidos
- [ ] Orden de lecciones revisado
- [ ] Ilustraciones ajustadas/completadas
- [ ] Reporte de correcciones generado

## Después de Etapa 5 (Evaluación Humana)

- [ ] Contenido validado por humano
- [ ] Ilustraciones aprobadas
- [ ] **LISTO PARA PUBLICAR**

---

# 🔗 Workflows Relacionados

- [Ilustración](./ilustracion.md) - Crear/usar renderers
- [Corregir](./corregir.md) - Corregir lecciones
- [Nuevo Tema](./nuevo-tema.md) - Crear temas desde cero
- [GeometrySpec](./geometry-exact.md) - Geometría exacta
- [CartesianSpec](./cartesian-spec.md) - Geometría analítica
- [Árbol de Decisión](./illustration-decision.md) - Guía expandida