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

---

## 📐 Regla de Ubicación Obligatoria

> ⛔ **CADA ilustración debe ir INMEDIATAMENTE después de su contenido.**

| Tipo de Contenido | Ubicación de la Ilustración |
|-------------------|----------------------------|
| Definición/Concepto | **Inmediatamente después** del texto explicativo |
| Fórmula | **Inmediatamente después** del bloque `$$...$$` |
| Ejemplo N | **Después del enunciado**, **ANTES** de los cálculos |

> [!IMPORTANT]
> **Flujo Visual en Ejemplos:**
> La ilustración da CONTEXTO (muestra elementos, dimensiones, notación).
> Los cálculos DESARROLLAN la solución.
> El estudiante primero VE, luego CALCULA.

**Patrón obligatorio para ejemplos con ilustración:**
```markdown
#### Ejemplo N: Título

[Enunciado del problema]
[Idea clave: qué vamos a hacer (1 línea)]

<div class="illustration">
  <img src="..." alt="..." />
</div>

**Razonamiento:**
[Desarrollo paso a paso con ecuaciones $$...$$]

**Resultado:**
$$
\boxed{...}
$$
```

> ❌ **NUNCA** poner cálculos antes de la ilustración.
> ❌ **NUNCA** agrupar ilustraciones al final de una sección.


---

## 📝 Regla de Correspondencia

> **La ilustración debe incluir la NOTACIÓN del texto para ser auto-explicativa.**

| Elemento del Texto | Debe Aparecer en la Ilustración |
|--------------------|--------------------------------|
| Vértices $A$, $B$, $C$, $D$ | Etiquetas visibles en cada punto |
| Fórmula $AC = BD$ | Líneas marcadas con igualdad |
| Valores numéricos | Etiquetas con los números |
| Propiedades (ej: perpendicular) | Símbolos de ángulo recto |

> 🎯 La ilustración debe poder entenderse **sin leer el texto**, porque lleva la notación completa.

---

## 🔍 Regla de Legibilidad Visual

> **Las etiquetas NO deben solaparse entre sí ni salirse del canvas.**

| Situación | Solución |
|-----------|----------|
| Etiquetas verticales (alturas, diagonales) | Texto rotado 90° (`transform="rotate(-90)"`) |
| Medidas externas (dimensiones) | Líneas de cota FUERA de la figura |
| Vértices cercanos | Offset mínimo 20px desde el punto |
| Texto largo | Abreviatura o dividir en líneas |

**Checklist de validación:**
- [ ] Ninguna etiqueta tapa otra
- [ ] Ningún texto se sale del borde del SVG
- [ ] Las líneas de cota no cruzan la figura

---

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
