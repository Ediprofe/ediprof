---
description: Corregir lección al estilo Ediprofe
globs: ["src/content/**/*.md"]
---

# ✏️ Workflow: Corregir Lección

> **Un comando para evaluar y corregir cualquier lección.**

---

## 🚀 Uso

```
/corregir http://localhost:4321/[URL-de-leccion]
```

---

## 📋 Paso 1: Leer Referencia de Estilo

```bash
# El estilo está en:
.agent/prompts/estilo-ediprofe.md
```

**Lección modelo:** `src/content/fisica/02-cinematica/04-MRUA/01-introduccion.md`

---

## ✅ Paso 2: Verificar Estructura

| Sección | Obligatorio |
|---------|-------------|
| `# **Título**` (sin emoji) | ✅ |
| Párrafo intro (1-2 oraciones) | ✅ |
| `## 🎯 ¿Qué vas a aprender?` | ✅ |
| Contenido con ejemplos paso a paso | ✅ |
| `## 📝 Ejercicios de Práctica` (10, con `<details>`) | ✅ |
| `## 🔑 Resumen` (tabla + conclusión) | ✅ |

---

## ✅ Paso 3: Verificar Estilo Pedagógico

- [ ] Razonamiento inductivo: ejemplo → regla (NUNCA al revés)
- [ ] Conexión cotidiana desde la primera oración
- [ ] Paso a paso detallado (sin saltos lógicos)
- [ ] Resultados con `\boxed{}`
- [ ] **TODAS las ecuaciones en bloque** `$$...$$` con líneas vacías

---

## ✅ Paso 4: Corregir Directamente

**No hacer sugerencias. Implementar los cambios.**

Si falta algo → reescribir.
Si está mal formateado → arreglar.
Si faltan ejemplos → agregar.

---

## ⛔ Reglas Críticas

| ❌ NO hacer | ✅ SÍ hacer |
|-------------|------------|
| LaTeX en títulos | Texto plano en títulos |
| `$inline$` para ecuaciones | `$$bloque$$` con líneas vacías |
| Emoji en H1 | Emoji en H2, H3 |
| Eliminar imágenes existentes | Conservar y usar imágenes |
| Menos de 5 ejemplos por concepto | Mínimo 5 ejemplos |

---

## 📁 Referencia

- Estilo: `.agent/prompts/estilo-ediprofe.md`
- CLAUDE.md: Sección "Formato Técnico"
