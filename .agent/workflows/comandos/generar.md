---
description: Generar lecciones de un tema aprobado (sin ilustraciones)
globs: ["src/content/**/*.md"]
---

# 📝 Workflow: Generar Lecciones

> **Generar contenido de lecciones SIN ilustraciones.**

---

## 🚀 Uso

```
/generar [URL-tema]
```

Ejemplo:
```
/generar matematicas/trigonometria/trigonometria-triangulo-rectangulo
```

---

## ⚠️ Pre-requisito

Debe existir un plan aprobado de `/planear-materia`, `/planear-unidad` o `/planear-tema`.

---

## 📋 Proceso

### Por cada lección del tema:

1. Usar estructura de `estilo-ediprofe.md`
2. **SIN ilustraciones SVG** (se agregan después con `/plan-ilustraciones`)
3. Mínimo 5 ejemplos por concepto
4. 10 ejercicios con `<details>`

### Estructura obligatoria:

```markdown
# **Título**

[1-2 oraciones intro]

---

## 🎯 ¿Qué vas a aprender?
- ...

---

## [Contenido]
[Ejemplos paso a paso]

---

## 📝 Ejercicios de Práctica
[10 ejercicios con <details>]

---

## 🔑 Resumen
[Tabla + conclusión]
```

---

## 📁 Archivos a crear

- `_meta.json` en el tema
- Una `.md` por cada lección

---

## 📁 Después de generar

Usar `/plan-ilustraciones [URL-tema]` para planear las ilustraciones.
