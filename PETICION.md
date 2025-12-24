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

QUIERO QUE LEAS EL CONTEXTO DE ESTE PROYECTO, Y CON BASE EN ÉL, ME AYUDES A TOMAR UNA DECISIÓN CON RESPECTO A LA ISSUE PRESENTADA EN EL ARCHIVO ISSUES.md. EN ELLA TE DOY CONTEXTO ESPECÍFICO DE LA ISSUE, Y TAMBIÉN LA POSICIÓN DE ALGUNAS IA. TOMA LA MEJOR DECISIÓN, PIENSA, Y COMUNÍCAME, PARA ANTES DE AJUSTAR LA ISSUE, YO APROBAR CUÁL ES EL PASO A SEGUIR CON BASE EN TU CONCEPTO Y MIS NECESIDADES.