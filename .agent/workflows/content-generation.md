---
description: Pipeline completo de generación de contenido educativo en 3 etapas globs: ["src/content/**/*.md"]
---

# 📚 Workflow: Generación de Contenido Educativo

Este documento define el proceso completo para generar lecciones educativas de alta calidad.

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
- **SIN gráficos complejos** (se agregan en Etapa 3)
- Usar marcadores: `<!-- ILUSTRACIÓN: descripción -->`
- Tablas y LaTeX SÍ permitidos

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

# ETAPA 3: DISEÑADOR Y EVALUADOR PEDAGÓGICO 🎨

## Objetivo
Enriquecer con gráficos y evaluar mejoras pedagógicas.

---

## 3.1 Agregar Ilustraciones

### Regla Obligatoria

> ⚠️ **MÍNIMO UNA ILUSTRACIÓN POR CONCEPTO**
> 
> Concepto = cada sección con título Markdown (##, ###)
> 
> **EXCEPCIÓN:** Sección de "Ejercicios de Práctica"

### Proceso

1. **Identificar** cada marcador `<!-- ILUSTRACIÓN: ... -->`
2. **Consultar** el árbol de decisión en CLAUDE.md
3. **Generar** usando el workflow correspondiente:
   - `.agent/workflows/echarts.md` → Funciones y datos
   - `.agent/workflows/geometry-exact.md` → Geometría exacta
   - `.agent/workflows/roughjs.md` → Diagramas ilustrativos
   - `.agent/workflows/chartjs.md` → Fracciones
   - `.agent/workflows/threejs.md` → 3D
4. **Reemplazar** el marcador por el código/enlace

### Árbol de Decisión Rápido

| Tipo | Tecnología |
|------|------------|
| Función f(x), datos, estadísticas | ECharts |
| Geometría exacta (puntos notables, perpendiculares) | GeometrySpec |
| Diagrama ilustrativo (física, química, procesos) | Rough.js |
| Fracción como pastel | Chart.js |
| Geometría 3D | Three.js |

---

## 3.2 Evaluar Pedagógicamente

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

### Si Detecta Problemas

Proponer mejoras específicas:

```markdown
## 🔧 Mejoras Sugeridas

### Lección: [nombre]

1. **Problema:** [descripción]
   **Solución:** [propuesta]

2. **Problema:** [descripción]
   **Solución:** [propuesta]
```

---

## 3.3 Verificar Estilo Visual

### Modo Claro/Oscuro

Todo elemento debe verse bien en AMBOS modos.

✅ **Seguro:**
- Markdown nativo (tablas, blockquotes, listas)
- Canvas (Rough.js, ECharts, JSXGraph)
- Fondos oscuros: `background: #1e293b`
- Colores saturados con alto contraste

❌ **Evitar:**
- Fondos claros con texto gris
- Colores de texto sin especificar

---

# ✅ CHECKLIST FINAL

## Después de Etapa 2

- [ ] Árbol de carpetas aprobado
- [ ] `_meta.json` en cada tema
- [ ] Intro motivadora en cada lección
- [ ] Cheat Sheet al inicio
- [ ] Marcadores `<!-- ILUSTRACIÓN -->` donde corresponde
- [ ] Mínimo 2 ejemplos por concepto
- [ ] Ejercicios con `<details>`
- [ ] Sin LaTeX en títulos
- [ ] Sin emojis en H1

## Después de Etapa 3

- [ ] Todas las ilustraciones generadas
- [ ] Mínimo 1 por concepto (excepto ejercicios)
- [ ] Tecnología correcta según árbol de decisión
- [ ] IDs únicos en gráficos inline
- [ ] Funciona en modo claro y oscuro
- [ ] Evaluación pedagógica completada

---

# 🔗 Workflows Relacionados

- [ECharts](./echarts.md) - Funciones y datos
- [GeometrySpec](./geometry-exact.md) - Geometría exacta
- [Rough.js](./roughjs.md) - Diagramas ilustrativos
- [Chart.js](./chartjs.md) - Fracciones
- [Three.js](./threejs.md) - Geometría 3D
- [Árbol de Decisión](./illustration-decision.md) - Guía expandida