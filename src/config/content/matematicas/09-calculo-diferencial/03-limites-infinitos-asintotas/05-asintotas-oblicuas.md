---
title: "Asíntotas Oblicuas"
---

# Asíntotas Oblicuas

Cuando una función racional tiene el grado del numerador mayor que el del denominador, puede tener una asíntota inclinada llamada asíntota oblicua o slant asymptote.

---

## 🎯 ¿Qué vas a aprender?

- Cuándo existe una asíntota oblicua
- Cómo calcularla mediante división
- Verificación con límites
- Ejemplos de funciones con asíntotas oblicuas

---

## 📖 Condición de existencia

Para $f(x) = \frac{P(x)}{Q(x)}$:

Una **asíntota oblicua** existe cuando:

$$
\text{grado}(P) = \text{grado}(Q) + 1
$$

Es decir, el numerador tiene exactamente **un grado más** que el denominador.

---

## 📖 Cómo encontrarla

### Método: División de polinomios

Dividimos $P(x) \div Q(x)$ para obtener:

$$
f(x) = mx + b + \frac{R(x)}{Q(x)}
$$

donde:
- $mx + b$ es el **cociente lineal** (la asíntota)
- $\frac{R(x)}{Q(x)}$ es el residuo (tiende a 0 cuando $x \to \pm\infty$)

**Asíntota oblicua:** $y = mx + b$

---

## ⚙️ Ejemplo 1: División larga

$$
f(x) = \frac{x^2 + 2x + 1}{x - 1}
$$

**Dividimos $x^2 + 2x + 1$ entre $x - 1$:**

```
      x + 3
    ─────────
x-1 │ x² + 2x + 1
      x² -  x
    ─────────
          3x + 1
          3x - 3
        ─────────
               4
```

$$
f(x) = x + 3 + \frac{4}{x - 1}
$$

**Asíntota oblicua:** $y = x + 3$

**Verificación:**
$$
\lim_{x \to \pm\infty} \left[f(x) - (x + 3)\right] = \lim_{x \to \pm\infty} \frac{4}{x-1} = 0 \quad ✓
$$

---

## ⚙️ Ejemplo 2: Con términos faltantes

$$
g(x) = \frac{2x^2 - 5}{x + 2}
$$

**Dividimos:**

```
       2x - 4
    ──────────
x+2 │ 2x² + 0x - 5
      2x² + 4x
    ──────────
          -4x - 5
          -4x - 8
        ──────────
                3
```

$$
g(x) = 2x - 4 + \frac{3}{x + 2}
$$

**Asíntota oblicua:** $y = 2x - 4$

---

## 📖 Método alternativo: Límites

La pendiente $m$ y el intercepto $b$ se pueden calcular como:

$$
m = \lim_{x \to \infty} \frac{f(x)}{x}
$$

$$
b = \lim_{x \to \infty} [f(x) - mx]
$$

---

## ⚙️ Ejemplo 3: Usando límites

$$
h(x) = \frac{x^2 - 3x + 2}{x - 1}
$$

**Pendiente:**
$$
m = \lim_{x \to \infty} \frac{x^2 - 3x + 2}{x(x-1)} = \lim_{x \to \infty} \frac{x^2 - 3x + 2}{x^2 - x}
$$

Dividiendo: $= \frac{1}{1} = 1$

**Intercepto:**
$$
b = \lim_{x \to \infty} \left[\frac{x^2 - 3x + 2}{x - 1} - x\right]
$$

$$
= \lim_{x \to \infty} \frac{x^2 - 3x + 2 - x(x-1)}{x - 1}
$$

$$
= \lim_{x \to \infty} \frac{x^2 - 3x + 2 - x^2 + x}{x - 1}
$$

$$
= \lim_{x \to \infty} \frac{-2x + 2}{x - 1} = \lim_{x \to \infty} \frac{-2 + \frac{2}{x}}{1 - \frac{1}{x}} = -2
$$

**Asíntota oblicua:** $y = x - 2$

---

## ⚙️ Ejemplo 4: Sin asíntota oblicua

$$
f(x) = \frac{x^3 + 1}{x - 2}
$$

Grado 3 - Grado 1 = 2 ≠ 1

**No hay asíntota oblicua.** La función crece como una parábola.

$$
f(x) = x^2 + 2x + 4 + \frac{9}{x-2}
$$

Hay una "asíntota parabólica": $y = x^2 + 2x + 4$

---

## 📖 Resumen de asíntotas

| Diferencia de grados | Tipo de asíntota |
|---------------------|------------------|
| grado $P$ < grado $Q$ | Horizontal: $y = 0$ |
| grado $P$ = grado $Q$ | Horizontal: $y = \frac{a_n}{b_m}$ |
| grado $P$ = grado $Q$ + 1 | **Oblicua**: $y = mx + b$ |
| grado $P$ > grado $Q$ + 1 | Ninguna lineal (asíntota curva) |

---

## ⚙️ Ejemplo 5: Análisis completo

$$
f(x) = \frac{x^2 - 4}{x + 1}
$$

**Asíntotas verticales:** $x = -1$

**Asíntota oblicua:** Dividimos
$$
f(x) = x - 1 - \frac{3}{x + 1}
$$

**A.O.:** $y = x - 1$

**Intersección con la asíntota:** ¿Cuándo $f(x) = x - 1$?
$$
\frac{-3}{x+1} = 0
$$

→ Nunca (excepto en $\pm\infty$)

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra la asíntota oblicua:

$$
f(x) = \frac{x^2 + 3x - 2}{x + 1}
$$

<details>
<summary>Ver solución</summary>

Dividiendo: $\frac{x^2 + 3x - 2}{x + 1} = x + 2 - \frac{4}{x+1}$

**Asíntota oblicua:** $y = x + 2$
</details>

---

**Ejercicio 2:** Encuentra todas las asíntotas:

$$
g(x) = \frac{2x^2 - x + 1}{x - 3}
$$

<details>
<summary>Ver solución</summary>

**A.V.:** $x = 3$

Dividiendo para A.O.:
$$
g(x) = 2x + 5 + \frac{16}{x - 3}
$$

**A.O.:** $y = 2x + 5$
</details>

---

**Ejercicio 3:** ¿Tiene asíntota oblicua?

$$
h(x) = \frac{x^3 - 2x}{x^2 + 1}
$$

<details>
<summary>Ver solución</summary>

Grado 3 - Grado 2 = 1 ✓

Dividiendo: $h(x) = x - \frac{3x}{x^2 + 1}$

**A.O.:** $y = x$
</details>
