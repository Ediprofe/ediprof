# ✏️ Prompt: Corregir Lección (Evaluar + Reescribir)

> **Un solo prompt que evalúa y corrige de una vez.**

---

## Prompt

Corrige las siguientes lecciones al estilo Ediprofe.


http://localhost:4321/matematicas/algebra/potenciacion/introduccion

http://localhost:4321/matematicas/algebra/potenciacion/propiedades-potencias-i

http://localhost:4321/matematicas/algebra/potenciacion/propiedades-potencias-ii





---

## PASO 1: LEE las referencias

1. `.agent/prompts/estilo-ediprofe.md` (estilo completo)

2. http://localhost:4321/fisica/cinematica/mcu/introduccion

3. http://localhost:4321/matematicas/algebra/productos-notables/introduccion-cuadrado-binomio (de desarrollo)

Nota como hay lecciones que por su naturaleza no cabe hablando de más antes del título "¿Qué vas a aprender?". Si hay una conexión muy pertienente, entonces se puede hacer ese párrafo pequeño introductorio.

---

## PASO 2: VERIFICA estas secciones obligatorias

□ Título en negrita (SIN emoji): `# **Título**`
□ Párrafo intro (1-2 oraciones, conecta con vida real)
□ `## 🎯 ¿Qué vas a aprender?` (4-5 puntos)
□ Contenido con ejemplos PASO A PASO
□ `## 📝 Ejercicios de Práctica` (exactamente 10, con `<details>`)
□ `## 🔑 Resumen` (tabla + conclusión)

---

## PASO 3: VERIFICA el estilo pedagógico

□ Razonamiento inductivo: ejemplo → regla (NO fórmula → ejemplo)
□ Conexión cotidiana desde la primera oración
□ Paso a paso detallado (no dar saltos lógicos)
□ Resultados importantes con `\boxed{}`
□ LaTeX en bloques con líneas vacías antes/después
□ Usar nombres propios para una enseñanza en latinoamerica, sin spanglish ni nombres de métodos rebuscados o cosas así, a menos que sea algo ya conocido de verdad así.
□ **⚠️ TODAS LAS ECUACIONES EN BLOQUE:** 
   - Propiedades, fórmulas Y pasos de razonamiento deben estar en LaTeX de bloque.
   - Cada ecuación en su propio bloque `$$..$$` separado por líneas vacías.
   - Esto mejora la legibilidad y evita errores de renderizado.
   
   **Ejemplo correcto:**
   ```markdown
   **Razonamiento:**
   
   $$
   a^{-5 + 2}
   $$
   
   Debo 5 y pago 2, quedo debiendo 3.
   
   $$
   a^{-3}
   $$
   ```
   
   **Incorrecto:** `$$a^{-5+2}$$ Debo $5...` (inline y sin separación).

---

## PASO 4: CORRIGE

Si falta algo o está mal → **reescribe la lección completa**.
No hagas sugerencias, **implementa los cambios directamente**.

### Estructura objetivo:

```markdown
# [Título]

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


---

## [Sección de contenido 2]

[Más contenido...]

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: [Título descriptivo]

[Situación contextualizada]

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
