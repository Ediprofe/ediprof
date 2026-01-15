---
description: Ejecutar plan de ilustraciones aprobado
globs: ["src/content/**/*.md", "scripts/geometry/**/*.py"]
---

# 🖼️ Workflow: Ilustrar

> **Ejecutar el plan de ilustraciones aprobado.**

---

## 🚀 Uso

```
/ilustrar [URL-tema o URL-leccion]
```

---

## ⚠️ Pre-requisito

Debe existir un plan aprobado de `/plan-ilustraciones`.

---

## 📋 Proceso

### Paso 0: Verificar Estructura de Integración

> ⛔ **ANTES de generar cualquier SVG, confirmar la ubicación en el markdown:**

| Tipo | Ubicación Correcta |
|------|-------------------|
| Ilustración Teórica | **Inmediatamente después** de su explicación |
| Ilustración de Ejemplo | **Después del enunciado**, **ANTES** de los cálculos |

> [!IMPORTANT]  
> **Flujo obligatorio para ejemplos:**
> 1. Enunciado + idea clave (1-2 líneas)
> 2. **Ilustración** (contexto visual)
> 3. Razonamiento con cálculos `$$...$$`
> 4. Resultado `\boxed{}`

❌ **NUNCA** poner cálculos antes de la ilustración que da contexto.
❌ **NUNCA** agrupar ilustraciones al final de una sección.
✅ **SIEMPRE** generar e integrar una por una en orden de aparición.

---

### Paso 0.5: Verificar Correspondencia con el Texto

> 📝 **La ilustración debe ser AUTO-EXPLICATIVA usando la notación del texto.**

**Reglas:**
1. Usar los **mismos símbolos** que el texto (si dice $AC = BD$, la figura debe etiquetar $A$, $B$, $C$, $D$).
2. Incluir **fórmulas clave** dentro de la ilustración si aplica (ej: cálculo de área con valores).
3. Mostrar **propiedades mencionadas** (si dice "diagonales perpendiculares", marcar el ángulo de $90°$).
4. Los **valores numéricos** de los ejemplos deben aparecer como etiquetas en la figura.

> La ilustración debe poder entenderse **sin leer el texto**, porque incluye toda la notación relevante.

---

### Paso 0.6: Verificar Legibilidad Visual

> 👁️ **Validar que las etiquetas no se solapen ni se salgan del canvas.**

Antes de finalizar cada SVG:
1. **Etiquetas verticales** → usar `transform="rotate(-90)"`
2. **Dimensiones** → líneas de cota FUERA de la figura
3. **Vértices** → offset mínimo 20px desde el punto
4. **Verificación visual** → revisar que nada se solapa ni se corta

---

### Paso 1: Verificar renderer existente

```bash
python scripts/geometry/list_renderers.py --search "[nombre-leccion]"
```

### Paso 2A: Si existe renderer

1. Identificar la función
2. Ejecutar para generar SVG
3. Mover a `public/images/[materia]/`
4. Enlazar en la lección

### Paso 2B: Si NO existe renderer

1. Copiar `scripts/geometry/renderer_template.py`
2. **Importar de core/ (OBLIGATORIO):**
   ```python
   from core.colors import COLORS
   from core.canvas import get_canvas_config
   from core.layouts import side_by_side, centered_single
   ```
3. Agregar docstring con "Para: [leccion].md"
4. Generar SVG

---

## ⛔ Reglas (CLAUDE.md sección 6)

| ✅ SIEMPRE | ❌ NUNCA |
|-----------|----------|
| Buscar renderer existente | Crear sin buscar |
| Importar de `core/` | Hardcodear colores |
| `get_canvas_config()` | `width=600` |

---

## 📁 Referencia

- Template: `scripts/geometry/renderer_template.py`
- Building blocks: `scripts/geometry/core/`
