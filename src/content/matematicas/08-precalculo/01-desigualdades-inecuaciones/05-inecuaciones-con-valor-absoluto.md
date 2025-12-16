# Inecuaciones con Valor Absoluto

El valor absoluto mide la distancia de un número al cero. Cuando aparece en una desigualdad, nos permite expresar condiciones de "cercanía" o "lejanía" de manera elegante.

---

## 🎯 ¿Qué vas a aprender?

- Interpretar geométricamente las inecuaciones con valor absoluto
- Los dos casos fundamentales: $|x| < a$ y $|x| > a$
- Resolver inecuaciones con expresiones dentro del valor absoluto
- Casos especiales y errores comunes

---

## 📖 Repaso: ¿Qué es el valor absoluto?

El **valor absoluto** de $x$, escrito $|x|$, es la distancia de $x$ al origen en la recta numérica:

$$
|x| = \begin{cases} x & \text{si } x \geq 0 \\ -x & \text{si } x < 0 \end{cases}
$$

**Ejemplos:**
- $|5| = 5$
- $|-3| = 3$
- $|0| = 0$

---

## 📖 Caso 1: $|x| < a$ (menor que)

### Interpretación geométrica

La desigualdad $|x| < a$ significa: "la distancia de $x$ al 0 es menor que $a$".

Esto ocurre cuando $x$ está **entre** $-a$ y $a$:

$$
|x| < a \quad \Leftrightarrow \quad -a < x < a
$$

```
           ○━━━━━━━━━━━━━━━━○
──────────┼────────────────┼───────────
         -a        0        a
```

### ⚙️ Ejemplo 1

Resolver: $|x| < 5$

**Solución directa:**
$$
-5 < x < 5
$$

**En notación de intervalo:** $x \in (-5, 5)$

---

### ⚙️ Ejemplo 2

Resolver: $|x - 3| \leq 2$

**Interpretación:** La distancia de $x$ a $3$ es como máximo $2$.

**Aplicamos la regla:**
$$
-2 \leq x - 3 \leq 2
$$

**Sumamos 3 a todas las partes:**
$$
-2 + 3 \leq x \leq 2 + 3
$$
$$
1 \leq x \leq 5
$$

**Solución:** $x \in [1, 5]$

---

### ⚙️ Ejemplo 3

Resolver: $|2x + 1| < 7$

**Aplicamos la regla:**
$$
-7 < 2x + 1 < 7
$$

**Restamos 1:**
$$
-8 < 2x < 6
$$

**Dividimos entre 2:**
$$
-4 < x < 3
$$

**Solución:** $x \in (-4, 3)$

---

## 📖 Caso 2: $|x| > a$ (mayor que)

### Interpretación geométrica

La desigualdad $|x| > a$ significa: "la distancia de $x$ al 0 es mayor que $a$".

Esto ocurre cuando $x$ está **fuera** del intervalo $[-a, a]$:

$$
|x| > a \quad \Leftrightarrow \quad x < -a \text{ o } x > a
$$

```
←━━━━━━━━━○                ○━━━━━━━━━→
──────────┼────────────────┼───────────
         -a        0        a
```

### ⚙️ Ejemplo 4

Resolver: $|x| \geq 4$

**Solución:**
$$
x \leq -4 \quad \text{o} \quad x \geq 4
$$

**En notación de intervalo:** $x \in (-\infty, -4] \cup [4, +\infty)$

---

### ⚙️ Ejemplo 5

Resolver: $|x - 2| > 3$

**Interpretación:** La distancia de $x$ a $2$ es mayor que $3$.

**Aplicamos la regla:**
$$
x - 2 < -3 \quad \text{o} \quad x - 2 > 3
$$

**Sumamos 2:**
$$
x < -1 \quad \text{o} \quad x > 5
$$

**Solución:** $x \in (-\infty, -1) \cup (5, +\infty)$

---

### ⚙️ Ejemplo 6

Resolver: $|3x - 5| \geq 7$

**Aplicamos la regla:**
$$
3x - 5 \leq -7 \quad \text{o} \quad 3x - 5 \geq 7
$$

**Primer caso:**
$$
3x \leq -2 \quad \Rightarrow \quad x \leq -\frac{2}{3}
$$

**Segundo caso:**
$$
3x \geq 12 \quad \Rightarrow \quad x \geq 4
$$

**Solución:** $x \in \left(-\infty, -\frac{2}{3}\right] \cup [4, +\infty)$

---

## 📊 Resumen de reglas

| Tipo | Equivalencia | Solución |
|------|--------------|----------|
| $\|x\| < a$ | $-a < x < a$ | Un intervalo abierto |
| $\|x\| \leq a$ | $-a \leq x \leq a$ | Un intervalo cerrado |
| $\|x\| > a$ | $x < -a$ o $x > a$ | Unión de dos intervalos |
| $\|x\| \geq a$ | $x \leq -a$ o $x \geq a$ | Unión de dos intervalos |

### 💡 Regla mnemotécnica

- **"Menor que" → queda ENTRE** (un solo intervalo)
- **"Mayor que" → queda FUERA** (dos intervalos separados)

---

## 📖 Casos especiales

### Caso 1: $|x| < 0$

No tiene solución. El valor absoluto siempre es $\geq 0$.

**Solución:** $\emptyset$

### Caso 2: $|x| \geq 0$

Siempre es verdadero para todo número real.

**Solución:** $\mathbb{R}$

### Caso 3: $|x| > -3$

Siempre es verdadero (todo valor absoluto es $\geq 0 > -3$).

**Solución:** $\mathbb{R}$

### Caso 4: $|x - 5| < -2$

Imposible. Un valor absoluto no puede ser negativo.

**Solución:** $\emptyset$

---

## ⚙️ Ejemplo 7: Inecuación compuesta

Resolver: $1 < |x - 4| \leq 3$

**Interpretación:** La distancia de $x$ a $4$ está entre $1$ y $3$ (incluido $3$).

**Separamos en dos partes:**

**Parte 1:** $|x - 4| > 1$
$$
x - 4 < -1 \quad \text{o} \quad x - 4 > 1
$$
$$
x < 3 \quad \text{o} \quad x > 5
$$

**Parte 2:** $|x - 4| \leq 3$
$$
-3 \leq x - 4 \leq 3
$$
$$
1 \leq x \leq 7
$$

**Intersección:**
- De $x < 3$ y $1 \leq x \leq 7$: obtenemos $[1, 3)$
- De $x > 5$ y $1 \leq x \leq 7$: obtenemos $(5, 7]$

**Solución:** $x \in [1, 3) \cup (5, 7]$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve y expresa en notación de intervalo:

a) $|x| < 6$
b) $|x + 4| \leq 3$
c) $|2x - 1| < 5$

<details>
<summary>Ver soluciones</summary>

a) $-6 < x < 6$
   
   **Solución:** $(-6, 6)$

b) $-3 \leq x + 4 \leq 3 \Rightarrow -7 \leq x \leq -1$
   
   **Solución:** $[-7, -1]$

c) $-5 < 2x - 1 < 5 \Rightarrow -4 < 2x < 6 \Rightarrow -2 < x < 3$
   
   **Solución:** $(-2, 3)$
</details>

---

**Ejercicio 2:** Resuelve:

a) $|x| > 2$
b) $|x - 1| \geq 4$
c) $|5 - 2x| > 3$

<details>
<summary>Ver soluciones</summary>

a) $x < -2$ o $x > 2$
   
   **Solución:** $(-\infty, -2) \cup (2, +\infty)$

b) $x - 1 \leq -4$ o $x - 1 \geq 4 \Rightarrow x \leq -3$ o $x \geq 5$
   
   **Solución:** $(-\infty, -3] \cup [5, +\infty)$

c) $5 - 2x < -3$ o $5 - 2x > 3$
   
   $-2x < -8$ o $-2x > -2$
   
   $x > 4$ o $x < 1$
   
   **Solución:** $(-\infty, 1) \cup (4, +\infty)$
</details>
