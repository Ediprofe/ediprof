---
description: Planear lecciones de un TEMA
globs: ["src/content/**/*.md"]
---

# 📝 Workflow: Planear Tema

> **Proponer LECCIONES para un tema específico.**

---

## 🚀 Uso

```
/planear-tema [materia/unidad/tema o nombre]
```

---

## 📋 Proceso

### Paso 1: Proponer lecciones

```
TEMA: [Nombre]
UNIDAD: [Padre]
MATERIA: [Abuelo]

├── _meta.json → {"name": "Nombre del Tema"}
├── 01-[leccion].md → [conceptos que cubre]
├── 02-[leccion].md → [conceptos que cubre]
├── 03-[leccion].md → [conceptos que cubre]
└── 04-[leccion].md → [conceptos que cubre]
```

### Paso 2: ESPERAR APROBACIÓN

---

## 📁 Después de aprobación

Usar `/generar [URL-tema]` para generar las lecciones.
