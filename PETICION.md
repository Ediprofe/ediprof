# Lo primero

LEE CLAUDE.md y sus documentos citados ahí para que obtengas el contexto general

---

# ⚠️ REGLAS CRÍTICAS ANTES DE ESCRIBIR CÓDIGO

> **LÉEME PRIMERO.** Estas reglas existen porque otro agente cometió errores que requirieron una refactorización masiva. NO las ignores.

## 🎨 COLORES: NUNCA HARDCODEAR

**El error más común:** escribir colores hexadecimales directamente en el código.

```python
# ❌ PROHIBIDO - Esto causó la refactorización de 314+ líneas
color='#3b82f6'
fill='#ffffff'
stroke='#ef4444'

# ✅ OBLIGATORIO - Siempre usar la paleta centralizada
from core.colors import COLORS
color=COLORS['primary']
fill=COLORS['white']
stroke=COLORS['accent']
```

### Paleta centralizada: `scripts/geometry/core/colors.py`

| Clave | Hex | Uso |
|-------|-----|-----|
| `'primary'` | `#3b82f6` | Azul - figuras principales |
| `'secondary'` | `#22c55e` | Verde - elementos secundarios |
| `'accent'` | `#ef4444` | Rojo - puntos notables |
| `'highlight'` | `#f97316` | Naranja - énfasis |
| `'purple'` | `#8b5cf6` | Púrpura - diámetros |
| `'white'` | `#ffffff` | Fondos blancos |
| `'background'` | `#f8fafc` | Fondos claros |
| `'text'` | `#1e293b` | Texto oscuro |
| `'text_light'` | `#64748b` | Texto secundario |
| `'auxiliary'` | `#94a3b8` | Líneas auxiliares |
| `'grid'` | `#e2e8f0` | Cuadrícula |

### ¿Por qué importa?

1. **Consistencia visual** - Todas las ilustraciones usan la misma paleta
2. **Mantenibilidad** - Cambiar un color se hace en UN solo lugar
3. **Escalabilidad** - Nuevos renderers heredan la paleta automáticamente
4. **Evita deuda técnica** - No se acumulan valores mágicos

### Cómo importar en cualquier renderer

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from core.colors import COLORS

# Usar así:
builder.rect(0, 0, 600, 500, fill=COLORS['white'])
coord.draw_point(builder, P, color=COLORS['accent'])
```

## 📐 ILUSTRACIONES: SEGUIR EL PROTOCOLO

Antes de crear cualquier ilustración, consulta:
- `CLAUDE.md` sección "Generación de Ilustraciones"
- Workflow: `.agent/workflows/geometry-exact.md`

**Pregúntate:**
1. ¿Existe ya un spec JSON para esto? → Usa el renderer existente
2. ¿Es geometría exacta? → Usa SymPy + renderer Python
3. ¿Es diagrama conceptual? → Usa Rough.js inline
4. ¿Requiere animación? → Usa SVG + CSS

## ✅ VERIFICACIÓN OBLIGATORIA

Después de modificar cualquier renderer, ejecuta:

```bash
bash scripts/verify-svg-rendering.sh
```

Esto genera SVGs de prueba y verifica que no haya errores.

---

## 🏷️ CONFIGURACIÓN DE MATERIAS: USAR CENTRALIZADA

**Fuente de verdad:** `src/config/materias.ts`

```typescript
// ❌ PROHIBIDO - Definir colores/config de materia en cada archivo
const materiaColor = '#ef4444';
const materiaName = 'Matemáticas';

// ✅ OBLIGATORIO - Importar de la config centralizada
import { getMateriaConfig, getMateriaName, getMateriaColor } from '../config/materias';
const config = getMateriaConfig('matematicas');
const name = getMateriaName('matematicas');
const color = getMateriaColor('matematicas');
```

### Qué contiene materiaConfig:
| Propiedad | Ejemplo | Uso |
|-----------|---------|-----|
| `name` | `'Matemáticas'` | Nombre con tilde para mostrar |
| `icon` | `'🧮'` | Emoji de la materia |
| `color` | `'#ef4444'` | Color principal |
| `gradient` | `'linear-gradient(...)'` | Gradiente para headers |
| `lightBg` | `'rgba(239,68,68,0.1)'` | Fondo claro |
| `lightSolid` | `'#fee2e2'` | Fondo para impresión (sin rgba) |
| `dark` | `'#991b1b'` | Color oscuro para títulos |

### Constantes del sitio:
```typescript
import { SITE_CONFIG } from '../config/materias';
SITE_CONFIG.url        // 'https://ediprofe.com'
SITE_CONFIG.social.youtube.url  // URL de YouTube
```

---

## 🔗 URLs Y SLUGS: USAR HELPERS

**Fuente de verdad:** `src/utils/navigation-generator.js`

```javascript
// ❌ PROHIBIDO - Manipular slugs manualmente
const url = `/matematicas/01-aritmetica/02-tema/03-leccion`;

// ✅ OBLIGATORIO - Usar cleanSlug para URLs limpias
import { cleanSlug, cleanSegment } from '../utils/navigation-generator.js';
const url = `/${materia}/${cleanSlug(lesson.slug)}`;
// Resultado: /matematicas/aritmetica/tema/leccion
```

### Funciones disponibles:
| Función | Input | Output |
|---------|-------|--------|
| `cleanSlug(slug)` | `'01-intro/02-tema/03-leccion'` | `'intro/tema/leccion'` |
| `cleanSegment(seg)` | `'01-introduccion'` | `'introduccion'` |
| `formatName(slug)` | `'numeros-naturales'` | `'Numeros Naturales'` |
| `extractOrder(file)` | `'03-leccion.md'` | `3` |

---

## 📝 TIPOS: USAR TIPOS EXISTENTES

**Fuente de verdad:** `src/types/content.ts`

```typescript
// ❌ PROHIBIDO - Definir tipos ad-hoc
type Materia = 'matematicas' | 'fisica';

// ✅ OBLIGATORIO - Importar tipos existentes
import { MateriaSlug, MATERIA_SLUGS, isMateriaSlug } from '../types/content';

// Validar si un string es materia válida
if (isMateriaSlug(slug)) {
  // TypeScript sabe que slug es MateriaSlug
}
```

---

## 🖼️ CONTENEDORES DE SVG: RESPONSIVOS

```html
<!-- ❌ PROHIBIDO - max-width fijo que no coincide con el SVG -->
<div style="max-width: 500px;">
  <img src="/images/grafico.svg" />
</div>

<!-- ✅ OBLIGATORIO - width 100% + box-sizing -->
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/grafico.svg" alt="Descripción" style="width: 100%; height: auto;" />
</div>
```

### Reglas:
1. **Siempre** `width: 100%` en el contenedor
2. **Siempre** `style="width: 100%; height: auto;"` en el `<img>`
3. **Dentro de HTML**, usar `<img>` NO `![]()`  (markdown no funciona dentro de `<div>`)
4. **Siempre** incluir `alt` descriptivo

---

## 📁 METADATOS: _meta.json OBLIGATORIO

Cada carpeta de tema DEBE tener un `_meta.json`:

```json
{
  "name": "Números Naturales",
  "description": "Conceptos básicos de números naturales"
}
```

### ¿Por qué?
- Sin `_meta.json` → la carpeta NO aparece en navegación
- El `name` se usa para mostrar títulos con tildes
- Las lecciones sin capítulo/tema válido son filtradas

---

## 📐 LaTeX: FORMATO CORRECTO

```markdown
<!-- ❌ PROHIBIDO - Fórmula comprimida en una línea -->
La fórmula es: $$A = \pi r^2$$ donde $r$ es el radio.

<!-- ✅ OBLIGATORIO - Bloque con líneas vacías -->
La fórmula es:

$$
A = \pi r^2
$$

Donde $r$ es el radio.
```

### Reglas:
| Situación | Usar | Ejemplo |
|-----------|------|---------|
| Fórmula principal | Bloque `$$` con líneas vacías | Teoremas, definiciones |
| Resultado final | `$$\boxed{x = 5}$$` | Respuestas destacadas |
| Variable en texto | Inline `$x$` | "donde $x$ es..." |
| **NUNCA** en títulos | Texto plano | `## Área del círculo` no `## $A = \pi r^2$` |

---

## 🎨 ESTILOS CSS: SINCRONIZACIÓN

Si cambias colores en `src/config/materias.ts`, **DEBES** actualizar estos archivos CSS:

```
src/styles/layouts/lesson.css      # Comentario: SINCRONIZAR con materias.ts
src/styles/pages/materia.css       # Comentario: SINCRONIZAR con materias.ts
src/styles/pages/capitulo.css      # Comentario: SINCRONIZAR con materias.ts
src/styles/pages/tema.css          # Comentario: SINCRONIZAR con materias.ts
```

Busca el comentario `SINCRONIZAR` en estos archivos para saber qué actualizar.

---

## 🚫 ANTI-PATRONES DETECTADOS (NO REPETIR)

| Anti-patrón | Consecuencia | Solución |
|-------------|--------------|----------|
| Hardcodear colores hex | Refactorización masiva | Usar `COLORS` de core |
| Hardcodear URLs de redes sociales | Inconsistencia | Usar `SITE_CONFIG` |
| `max-width` fijo en SVG | SVG cortado o espacio en blanco | Usar `width: 100%` |
| Definir `MateriaSlug` localmente | Duplicación, errores de tipo | Importar de `types/content` |
| Crear `_meta.json` sin `name` | Carpeta no aparece en nav | Siempre incluir `name` |
| LaTeX en títulos de sección | Error de renderizado | Usar texto plano |
| `![](img)` dentro de `<div>` | Imagen no renderiza | Usar `<img src="">` |

---

## 📋 CHECKLIST ANTES DE HACER PR

- [ ] ¿Usé `COLORS` de `core/colors.py` en renderers Python?
- [ ] ¿Usé `getMateriaConfig()` para colores de materia en Astro/TS?
- [ ] ¿Usé `cleanSlug()` para URLs?
- [ ] ¿Los contenedores de SVG tienen `width: 100%`?
- [ ] ¿Los `_meta.json` tienen el campo `name`?
- [ ] ¿El LaTeX está en bloques separados con líneas vacías?
- [ ] ¿Ejecuté `bash scripts/verify-svg-rendering.sh`?

---

