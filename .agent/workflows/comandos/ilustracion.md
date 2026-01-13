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
