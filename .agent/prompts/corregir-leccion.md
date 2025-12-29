# ✏️ Prompt: Corregir Lección (Evaluar + Reescribir)

> **Un solo prompt que evalúa y corrige de una vez.**

---

## Prompt

Corrige las siguientes lecciones al estilo Ediprofe.


http://localhost:4321/matematicas/algebra/potenciacion/introduccion

http://localhost:4321/matematicas/algebra/potenciacion/propiedades-potencias-i

http://localhost:4321/matematicas/algebra/potenciacion/propiedades-potencias-ii



Corrige las siguientes lecciones al estilo Ediprofe.

http://localhost:4321/matematicas/aritmetica/potenciacion-radicacion-logaritmos/propiedades-de-los-logaritmos

http://localhost:4321/matematicas/aritmetica/potenciacion-radicacion-logaritmos/operaciones-combinadas-avanzadas



MINIMO 5 EJEMPLOS POR SECCIÓN O CONCEPTO. TEN EN CUENTA QUE DENTRO DE UNA MISMA LECCIÓN PUEDEN HABER VARIOS CONCEPTOS, NORMALMENTE DSEPARADOS POR TÍTULO MARKDOWN, PERO SIN ANOTAR EXPLÍCITAMENTE "CONCEPTO 1: ..." NI NADA DE ESO...SOLO TENIENDOLO EN CUENTA. REPITO: NO ANOTAR ESO EN LOS TÍTULOS ESO DE "CONCEPTO 1:...." MIRA LA LECCIÓN DE REFERENCIA.

LAS IMAGENES GENERADAS EN LAS LECCIONES NO LAS ELIMINES! ÚSALAS COMO PARTE DE LA REESCRITURA.

LAS IMAGENES GENERADAS EN LAS LECCIONES ELIMÍNALAS! ÚSALAS COMO PARTE DE LA REESCRITURA.

Si encuentras un símbolo $ déjalo mejor como "pesos" porque hay un problema para renderizar eso en latex.

Recuerda que en los títulos markdown de sección no puedes agregar expresiones latex.

## PASO 1: LEE las referencias

1. `.agent/prompts/estilo-ediprofe.md` (estilo completo)

2. http://localhost:4321/fisica/cinematica/mcu/introduccion (modelo de lección)


Nota como hay lecciones que por su naturaleza no cabe hablando de más antes del título "¿Qué vas a aprender?". Si hay una conexión muy pertienente, entonces se puede hacer ese párrafo pequeño introductorio.

Ten en cuenta también que los títulos markdown de la lección no pueden tener expresiones latex, ya que se daña como se ve en eo índice de la página y en la barra lateral de navegación.

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
□ **⚠️ TODAS LAS ECUACIONES EN BLOQUE (REGLA CRÍTICA):** 

   > **🚨 NUNCA uses formato inline `$...$` para ecuaciones importantes.** Esta regla se aplica a TODAS las ecuaciones, incluyendo las de los pasos de razonamiento y las soluciones de ejercicios.
   
   - Cada ecuación debe ir en su propio bloque `$$...$$`.
   - SIEMPRE deja una línea vacía ANTES y DESPUÉS del bloque.
   - Esto mejora la legibilidad y evita errores de renderizado.
   
   **Ejemplo correcto (cada paso en su bloque):**
   ```markdown
   **Razonamiento:**
   
   1. Abrimos el centro:
   
   $$
   2x^2 + 6x + x + 3
   $$
   
   2. Agrupamos:
   
   $$
   (2x^2 + 6x) + (x + 3)
   $$
   
   3. Factor común:
   
   $$
   2x(x + 3) + 1(x + 3)
   $$
   ```
   
   **Incorrecto (inline o sin separación):**
   ```markdown
   Abrimos: $2x^2 + 6x + x + 3$, agrupamos $(2x^2+6x)+(x+3)$ y sacamos...
   ```
   
   **También incorrecto (bloque pegado al texto):**
   ```markdown
   **Razonamiento:**
   $$2x^2 + 6x + x + 3$$
   Agrupamos:
   ```

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

