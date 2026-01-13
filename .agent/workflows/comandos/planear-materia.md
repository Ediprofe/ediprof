---
description: Planear estructura completa de una MATERIA
globs: ["src/content/**/*.md"]
---

# 📚 Workflow: Planear Materia

> **Proponer árbol completo de UNIDADES, TEMAS y LECCIONES para una materia.**

---

## 🚀 Uso

```
/planear-materia [nombre de la materia]
```

---

## 📐 Jerarquía Ediprofe

```
MATERIA (ej: Matemáticas)
  └── UNIDAD (ej: Trigonometría)
       └── TEMA (ej: Trigonometría del Triángulo Rectángulo)
            └── LECCIÓN (ej: Razones Trigonométricas)
```

**Ejemplo real:**
```
http://localhost:4321/matematicas/trigonometria/trigonometria-triangulo-rectangulo/razones-trigonometricas

Matemáticas          → MATERIA
Trigonometría        → UNIDAD
Trig. Triángulo Rect.→ TEMA
Razones Trigonom.    → LECCIÓN
```

---

## 📋 Proceso

### Paso 1: Analizar entradas del usuario

El usuario puede proporcionar:
- Documentos de referencia (PDFs, notas)
- Temario o currículo
- Lista de conceptos a cubrir

### Paso 2: Proponer árbol de carpetas

```
MATERIA: [Nombre]

├── 01-[unidad-slug]/
│   ├── _meta.json → {"name": "Nombre de la Unidad"}
│   ├── 01-[tema-slug]/
│   │   ├── _meta.json → {"name": "Nombre del Tema"}
│   │   ├── 01-[leccion].md → [conceptos]
│   │   └── 02-[leccion].md → [conceptos]
│   └── 02-[tema-slug]/
│       └── ...
└── 02-[unidad-slug]/
    └── ...
```

### Paso 3: ESPERAR APROBACIÓN

> ⛔ **NO generar contenido hasta que el árbol sea APROBADO.**

---

## 📁 Después de aprobación

Usar `/generar [URL-tema]` para generar las lecciones.
