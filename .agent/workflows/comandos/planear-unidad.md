---
description: Planear estructura de una UNIDAD
globs: ["src/content/**/*.md"]
---

# 📖 Workflow: Planear Unidad

> **Proponer TEMAS y LECCIONES para una unidad específica.**

---

## 🚀 Uso

```
/planear-unidad [materia/unidad o nombre]
```

---

## 📋 Proceso

### Paso 1: Proponer estructura

```
UNIDAD: [Nombre]
MATERIA: [Padre]

├── 01-[tema-slug]/
│   ├── _meta.json → {"name": "Nombre del Tema"}
│   ├── 01-[leccion].md → [conceptos]
│   ├── 02-[leccion].md → [conceptos]
│   └── 03-[leccion].md → [conceptos]
├── 02-[tema-slug]/
│   └── ...
```

### Paso 2: ESPERAR APROBACIÓN

---

## 📁 Después de aprobación

Usar `/generar [URL-tema]` para generar las lecciones.
