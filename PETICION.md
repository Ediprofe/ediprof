# 📋 PETICIÓN AL AGENTE

> **Este documento es tu punto de entrada.** Lee las instrucciones, las reglas críticas, y luego la petición del usuario al final.

---

## 🚀 INSTRUCCIONES RÁPIDAS

### Paso 1: Obtener contexto
```
LEE: CLAUDE.md (secciones relevantes según el tipo de tarea)
```

### Paso 2: Identificar tipo de tarea

| Si la petición es sobre... | Lee esta sección de CLAUDE.md |
|---------------------------|-------------------------------|
| **Crear lecciones nuevas** | "Flujo de trabajo en 5 etapas" |
| **Generar ilustraciones** | "Sistema de ilustraciones" + Árbol de decisión |
| **Modificar renderers Python** | "Módulo Core" + "Módulo Cartesian" |
| **Exportar a Word/PDF** | "Comandos útiles" |
| **Entender la estructura** | "Estructura del proyecto" |

### Paso 3: Consultar workflows específicos

| Tipo de ilustración | Workflow |
|---------------------|----------|
| Circunferencias | `.agent/workflows/circle-spec.md` |
| Triángulos | `.agent/workflows/geometry-exact.md` |
| Geometría analítica | `.agent/workflows/cartesian-spec.md` |
| Gráficas de funciones | `.agent/workflows/graphspec.md` |
| **Estadística (histogramas, barras)** | `.agent/workflows/mathplotter-spec.md` |
| **Sistemas de ecuaciones** | `.agent/workflows/mathplotter-spec.md` |
| Diagramas conceptuales | PNG de tablet (ver CLAUDE.md) |
| Química (tabla periódica) | `.agent/workflows/chemistry-spec.md` |
| Contenido educativo | `.agent/workflows/content-generation.md` |

---

## ⚠️ REGLAS CRÍTICAS (LEER SIEMPRE)

> **Estas reglas existen porque errores pasados requirieron refactorizaciones masivas. NO las ignores.**

### 🎨 1. COLORES: Nunca hardcodear

```python
# ❌ PROHIBIDO
color='#3b82f6'

# ✅ OBLIGATORIO
from core.colors import COLORS
color=COLORS['primary']
```

**Fuente de verdad:** `scripts/geometry/core/colors.py`

### 🏷️ 2. CONFIGURACIÓN: Usar centralizadas

```typescript
// ❌ PROHIBIDO
const materiaColor = '#ef4444';

// ✅ OBLIGATORIO
import { getMateriaConfig } from '../config/materias';
const config = getMateriaConfig('matematicas');
```

**Fuentes de verdad:**
- Materias: `src/config/materias.ts`
- Tipos: `src/types/content.ts`
- URLs: `src/utils/navigation-generator.js`

### 📐 3. LaTeX: Formato correcto

```markdown
<!-- ❌ PROHIBIDO -->
La fórmula es: $$A = \pi r^2$$ donde...

<!-- ✅ OBLIGATORIO -->
La fórmula es:

$$
A = \pi r^2
$$

Donde...
```

### 🖼️ 4. Contenedores SVG: Responsivos

```html
<!-- ❌ PROHIBIDO -->
<div style="max-width: 500px;">

<!-- ✅ OBLIGATORIO -->
<div style="width: 100%; box-sizing: border-box;">
```

### 📁 5. Metadatos: _meta.json obligatorio

Cada carpeta de tema DEBE tener:
```json
{
  "name": "Nombre con Tildes",
  "description": "Descripción breve"
}
```

### ✅ 6. Verificación: Ejecutar siempre

Después de modificar renderers:
```bash
bash scripts/verify-svg-rendering.sh
```

---

## 📊 TABLA RESUMEN DE FUENTES DE VERDAD

| Qué | Dónde | Importar |
|-----|-------|----------|
| Colores SVG | `scripts/geometry/core/colors.py` | `from core.colors import COLORS` |
| MathPlotter | `scripts/geometry/core/plotter.py` | `from scripts.geometry.core.plotter import MathPlotter` |
| Config materias | `src/config/materias.ts` | `getMateriaConfig()` |
| Tipos TypeScript | `src/types/content.ts` | `MateriaSlug`, `isMateriaSlug` |
| Helpers de URL | `src/utils/navigation-generator.js` | `cleanSlug()`, `cleanSegment()` |
| Tamaños canvas | `scripts/geometry/core/canvas.py` | `SIZE_SIMPLE`, `SIZE_COMPOUND` |
| **Navegación contextual** | `src/utils/navigation-loader.ts` | `loadContextualNavigation()`, `MATERIAS_LIST` |

---

## 🚫 ANTI-PATRONES (NO REPETIR)

| ❌ Error | ✅ Solución |
|---------|------------|
| Hardcodear colores hex | Usar `COLORS` de core |
| `max-width` fijo en SVG | Usar `width: 100%` |
| LaTeX en títulos | Usar texto plano |
| Usar tags HTML/JSX para imágenes | Usar Markdown `![alt](path)` |
| Crear `_meta.json` sin `name` | Siempre incluir `name` |
| Definir tipos localmente | Importar de `types/content` |

---

## 📋 CHECKLIST ANTES DE ENTREGAR

- [ ] ¿Usé las fuentes de verdad para colores/config?
- [ ] ¿Los contenedores SVG son responsivos?
- [ ] ¿El LaTeX está en bloques con líneas vacías?
- [ ] ¿Ejecuté la verificación de renderers?
- [ ] ¿Los `_meta.json` tienen `name`?

---

## 🔄 PROTOCOLO DE CLARIFICACIÓN

**Si NO tienes certeza de algo → PREGUNTA ANTES de ejecutar.**

Situaciones que requieren confirmación:
- Diagramas técnicos/visuales
- Primera vez haciendo algo de ese tipo
- Solicitud ambigua o con múltiples interpretaciones

---

# 📝 PETICIÓN DEL USUARIO


Corrige las siguientes lecciones al estilo Ediprofe.


http://localhost:4321/matematicas/algebra/fracciones-algebraicas/multiplicacion-de-fracciones

http://localhost:4321/matematicas/algebra/fracciones-algebraicas/division-de-fracciones

http://localhost:4321/matematicas/algebra/fracciones-algebraicas/combinacion-de-operaciones

http://localhost:4321/matematicas/algebra/fracciones-algebraicas/fracciones-complejas



---

## PASO 1: LEE las referencias

1. `.agent/prompts/estilo-ediprofe.md` (estilo completo)

2. http://localhost:4321/fisica/cinematica/mcu/introduccion

3. http://localhost:4321/matematicas/algebra/productos-notables/introduccion-cuadrado-binomio (de desarrollo)

Nota como hay lecciones que por su naturaleza no cabe hablando de más antes del título "¿Qué vas a aprender?". Si hay una conexión muy pertienente, entonces se puede hacer ese párrafo pequeño introductorio.

---

## PASO 2: VERIFICA estas secciones obligatorias

□ Título en negrita (SIN emoji): `# **Título**`
□ Párrafo intro (1-2 oraciones, conecta con vida real)
□ `## 🎯 ¿Qué vas a aprender?` (4-5 puntos)
□ Contenido con ejemplos PASO A PASO
□ `## 📝 Ejercicios de Práctica` (exactamente 10, con `<details>`)
□ `## 🔑 Resumen` (tabla + conclusión)

---

## PASO 3: VERIFICA el estilo pedagógico

□ Razonamiento inductivo: ejemplo → regla (NO fórmula → ejemplo)
□ Conexión cotidiana desde la primera oración
□ Paso a paso detallado (no dar saltos lógicos)
□ Resultados importantes con `\boxed{}`
□ LaTeX en bloques con líneas vacías antes/después
□ Usar nombres propios para una enseñanza en latinoamerica, sin spanglish ni nombres de métodos rebuscados o cosas así, a menos que sea algo ya conocido de verdad así.

---

## PASO 4: CORRIGE

Si falta algo o está mal → **reescribe la lección completa**.
No hagas sugerencias, **implementa los cambios directamente**.

### Estructura objetivo:

```markdown
# [Título]

[1-2 oraciones conectando con vida real o lección anterior]

---

## 🎯 ¿Qué vas a aprender?

- [Concepto 1]
- [Concepto 2]
- [Concepto 3]
- [Concepto 4]

---

## [Sección de contenido 1]

[Explicación clara, ejemplos paso a paso]


---

## [Sección de contenido 2]

[Más contenido...]

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: [Título descriptivo]

[Situación contextualizada]

**Datos:**
- ...

**Razonamiento:**
[Paso a paso]

**Resultado:** $\boxed{...}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**[Enunciado]**

<details>
<summary>Ver solución</summary>

**Datos:** ...
**Razonamiento:** ...
**Resultado:** $\boxed{...}$

</details>

[Repetir hasta Ejercicio 10]

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **X** | ... |
| **Y** | ... |

> [Conclusión de 1-2 oraciones]
```

---

## PASO 5: ENTREGA

1. Muestra la lección corregida completa
2. Lista los cambios realizados

---
