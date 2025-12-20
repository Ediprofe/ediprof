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

# 📋 PETICIÓN DE REVISIÓN: Exportar a Word y PDF

## Contexto

Te cuento que otro agente me ayudó con la implementación de exportar a Word y exportar a PDF las lecciones. En el caso de exportar a Word tengo prioridad con exportar lecciones o grupos de lecciones combinadas en un solo documento, algo que ya el agente implementó. En el caso de exportar a PDF, mi intención prioritaria es exportar por tema, aunque también está la opción de imprimir por lección.

## Lo que se implementó

### Exportar a Word (DOCX)
- **Script principal:** `scripts/export-to-docx.sh`
- **Preprocesador:** `scripts/preprocess-markdown.mjs` - Convierte sintaxis de Astro `<Image>` a Markdown estándar
- **Post-procesador:** `scripts/fix-docx-tables.py` - Agrega bordes a tablas, centra imágenes, ajusta tamaños
- **Conversor SVG→PNG:** `scripts/svg-to-png.mjs` - Usa Playwright para renderizar SVGs a PNG

**Funcionalidades:**
- Combina múltiples lecciones en un solo documento
- Convierte imágenes SVG a PNG automáticamente
- Mantiene el fondo de los SVGs (degradado gris para legibilidad)
- Opción `--no-images` para generar sin imágenes

### Exportar a PDF
- **Script principal:** `scripts/export-to-pdf.mjs` - Usa Playwright para capturar páginas HTML como PDF
- **Página de impresión por lección:** `src/pages/print/[...slug].astro`
- **Página de impresión por tema:** `src/pages/print-tema/[...slug].astro`

**Funcionalidades del PDF por tema:**
- Portada profesional con logo SVG que cambia de color según la materia
- Colores por materia: Física=azul, Matemáticas=rojo, Química=naranja, Ciencias=verde
- Índice de lecciones con numeración
- Cada lección empieza en nueva página
- Redes sociales con íconos (YouTube, TikTok, Web)
- Paginación en el footer (página X / total)
- Página final con branding

**Archivos de branding creados:** `public/images/brand/`
- `logo-ediprofe.svg` - Logo del libro abierto (usa currentColor)
- `youtube.svg`, `tiktok.svg`, `web.svg` - Íconos de redes sociales

## Qué revisar

Por favor revisa que la implementación siga las buenas prácticas y el protocolo de `CLAUDE.md`:

1. **Colores de materia** - ¿Son consistentes con lo definido en CLAUDE.md?
2. **Generación de ilustraciones** - ¿Se sigue el protocolo de `/illustration-decision` para elegir la tecnología?
3. **Estructura de archivos** - ¿Los scripts y páginas están en ubicaciones correctas?
4. **Manejo de SVG** - ¿El conversor mantiene la calidad y legibilidad?
5. **URLs generadas** - ¿Se usa correctamente `cleanSlug` de `navigation-generator.js`?
6. **Accesibilidad** - ¿Los PDFs tienen buena legibilidad y contraste?

## Archivos clave a revisar

```
scripts/
├── export-to-docx.sh      # Script principal Word
├── export-to-pdf.mjs      # Script principal PDF
├── preprocess-markdown.mjs # Preprocesador Markdown
├── fix-docx-tables.py     # Post-procesador DOCX
└── svg-to-png.mjs         # Conversor SVG a PNG

src/pages/
├── print/[...slug].astro      # Página print por lección
└── print-tema/[...slug].astro # Página print por tema

public/images/brand/
├── logo-ediprofe.svg
├── youtube.svg
├── tiktok.svg
└── web.svg
```

Necesito que por favor revises el proyecto a nivel de arquitectura, que no haya archivos tan grandes, que se mantenga fácilmente mantenible y escalable. ADELANTE.

