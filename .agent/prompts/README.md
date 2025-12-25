# 📋 Sistema de Prompts - Simplificado

> **Un solo prompt para corregir lecciones. Un solo estilo para todas.**

---

## 🗂️ Archivos

| Archivo | Propósito |
|---------|-----------|
| `corregir-leccion.md` | **PROMPT PRINCIPAL** - Evalúa y corrige de una vez |
| `estilo-ediprofe.md` | Referencia del estilo (para consulta) |

---

## 🚀 Uso

```
1. Copiar el prompt de corregir-leccion.md
2. Cambiar [RUTA] por la ruta de la lección
3. Pegar al agente
4. El agente evalúa Y corrige automáticamente
```

### Ejemplo:
```
Corrige esta lección siguiendo el estilo Ediprofe.

**Lección:** src/content/matematicas/02-algebra/01-introduccion/01-lenguaje-algebraico.md
```

---

## 📚 Lección Modelo

**Referencia principal:** `src/content/fisica/02-cinematica/04-MRUA/01-introduccion.md`

---

## ✅ Checklist Rápido

Toda lección debe tener:

```
□ # **Título** (SIN emoji en H1)
□ Párrafo intro (1-2 oraciones)
□ ## 🎯 ¿Qué vas a aprender? (4-5 puntos)
□ Contenido con ejemplos paso a paso
□ PROPUESTAS DE IMAGEN (comentarios HTML)
□ ## 📝 Ejercicios de Práctica (10 ejercicios con <details>)
□ ## 🔑 Resumen (tabla + conclusión + imagen resumen)
```

---

## 🖼️ Propuesta de Imágenes

Al corregir, incluir propuestas como comentarios HTML:

```html
<!-- PROPUESTA DE IMAGEN: nombre
Descripción: [Qué mostrar]
Elementos: [Lista]
Estilo: Diagrama | Ilustración | Resumen
-->
```

**Ubicaciones:** 1 por concepto + 1 por ejemplo + 1 de resumen
