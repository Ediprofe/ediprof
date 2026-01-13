---
description: Proponer plan de ilustraciones para un tema o lección
globs: ["src/content/**/*.md"]
---

# 🎨 Workflow: Plan de Ilustraciones

> **Proponer LISTA de ilustraciones antes de generar.**

---

## 🚀 Uso

```
/plan-ilustraciones [URL-tema o URL-leccion]
```

---

## 📋 Proceso

### Paso 1: Analizar el contenido

Leer las lecciones y identificar:
- Conceptos que necesitan visualización
- Ejemplos que se benefician de diagrama
- Comparaciones o resúmenes visuales

### Paso 2: Proponer lista de ilustraciones

**Formato:**

```markdown
## Plan de Ilustraciones

### Lección: Razones Trigonométricas

| # | Ubicación | Descripción | Renderer |
|---|-----------|-------------|----------|
| 1 | Después de definición | Triángulo con catetos y hipotenusa etiquetados | ¿Existe? |
| 2 | Ejemplo 1 | Triángulo 3-4-5 con ángulo marcado | ¿Existe? |
| 3 | Resumen | Tabla visual de sin, cos, tan | ¿Existe? |

### Lección: Ángulos Notables

| # | Ubicación | Descripción | Renderer |
|---|-----------|-------------|----------|
| 1 | ... | ... | ... |
```

### Paso 3: Verificar renderers existentes

```bash
python scripts/geometry/list_renderers.py --search "[tema]"
```

### Paso 4: ESPERAR APROBACIÓN

> ⛔ **NO generar SVGs hasta que el plan sea APROBADO.**

---

## 📁 Después de aprobación

Usar `/ilustrar [URL]` para ejecutar el plan.
