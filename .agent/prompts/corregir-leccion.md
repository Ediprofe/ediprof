# ✏️ Prompt: Corregir Lección (Evaluar + Reescribir)

> **Un solo prompt que evalúa y corrige de una vez.**

---

## Prompt

```
Corrige esta lección siguiendo el estilo Ediprofe.

**Lección:** [RUTA]

---

## PASO 1: LEE las referencias

1. `.agent/prompts/estilo-ediprofe.md` (estilo completo)
2. `src/content/fisica/02-cinematica/04-MRUA/01-introduccion.md` (modelo)

---

## PASO 2: VERIFICA estas secciones obligatorias

□ Título en negrita (SIN emoji): `# **Título**`
□ Párrafo intro (1-2 oraciones, conecta con vida real)
□ `## 🎯 ¿Qué vas a aprender?` (4-5 puntos)
□ Contenido con ejemplos PASO A PASO
□ **Imágenes**: mínimo 1 por concepto + 1 por ejemplo + 1 de resumen
□ `## 📝 Ejercicios de Práctica` (exactamente 10, con `<details>`)
□ `## 🔑 Resumen` (tabla + conclusión + imagen de resumen)

---

## PASO 3: VERIFICA el estilo pedagógico

□ Razonamiento inductivo: ejemplo → regla (NO fórmula → ejemplo)
□ Conexión cotidiana desde la primera oración
□ Paso a paso detallado (no dar saltos lógicos)
□ Resultados importantes con `\boxed{}`
□ LaTeX en bloques con líneas vacías antes/después

---

## PASO 4: CORRIGE

Si falta algo o está mal → **reescribe la lección completa**.
No hagas sugerencias, **implementa los cambios directamente**.

### Estructura objetivo:

```markdown
# **[Título]**

[1-2 oraciones conectando con vida real o lección anterior]

---

## 🎯 ¿Qué vas a aprender?

- [Concepto 1]
- [Concepto 2]
- [Concepto 3]
- [Concepto 4]

---

## [Sección de contenido 1]

[Explicación clara, ejemplos paso a paso]

<!-- PROPUESTA DE IMAGEN: concepto-nombre
Descripción: [Qué debe mostrar la imagen]
Elementos:
- [Elemento 1]
- [Elemento 2]
Estilo: Diagrama/Ilustración/Gráfica
-->

---

## [Sección de contenido 2]

[Más contenido...]

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: [Título descriptivo]

[Situación contextualizada]

<!-- PROPUESTA DE IMAGEN: ejemplo1-nombre
Descripción: [Qué situación ilustrar]
Elementos:
- [Objeto principal]
- [Datos visibles: valores, flechas, etc.]
-->

**Datos:**
- ...

**Razonamiento:**
[Paso a paso]

**Resultado:** $\boxed{...}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**[Enunciado]**

<details>
<summary>Ver solución</summary>

**Datos:** ...
**Razonamiento:** ...
**Resultado:** $\boxed{...}$

</details>

[Repetir hasta Ejercicio 10]

---

## 🔑 Resumen

<!-- PROPUESTA DE IMAGEN: resumen-tema
Descripción: Diagrama resumen con los conceptos clave
Elementos:
- [Fórmulas principales]
- [Relaciones entre conceptos]
-->

| Concepto | Descripción |
|----------|-------------|
| **X** | ... |
| **Y** | ... |

> [Conclusión de 1-2 oraciones]
```

---

## PASO 5: ENTREGA

1. Muestra la lección corregida completa
2. Lista los cambios realizados

---

## Formato de Propuesta de Imagen

Usar comentarios HTML con este formato:

```html
<!-- PROPUESTA DE IMAGEN: nombre-descriptivo
Descripción: [Qué debe comunicar visualmente]
Elementos:
- [Lista de elementos a incluir]
- [Datos, flechas, etiquetas]
Estilo: Diagrama | Ilustración | Gráfica | Resumen visual
-->
```

---

## Ejemplo de Uso

```
Corrige esta lección siguiendo el estilo Ediprofe.

**Lección:** src/content/matematicas/02-algebra/01-introduccion/01-lenguaje-algebraico.md
```
