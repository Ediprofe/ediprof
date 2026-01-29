# Inecuaciones Racionales

¿Qué ocurre cuando una fracción contiene la variable en el denominador? Las inecuaciones racionales requieren un cuidado especial: debemos considerar dónde la fracción está indefinida.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una inecuación racional
- El método de puntos críticos para racionales
- Por qué nunca debemos multiplicar por el denominador sin precaución
- Análisis de signos sistemático

---

## 📖 ¿Qué es una inecuación racional?

Una **inecuación racional** es una desigualdad que involucra un cociente de polinomios:

$$
\frac{P(x)}{Q(x)} < 0 \quad \text{(o con } >, \leq, \geq \text{)}
$$

**Ejemplos:**
- $\frac{x - 2}{x + 3} > 0$
- $\frac{2x + 1}{x^2 - 4} \leq 0$
- $\frac{x^2 - 9}{x - 1} \geq 0$

### ⚠️ Cuidado importante

El **denominador nunca puede ser cero**. Esos valores deben excluirse de la solución.

---

## 📖 Método de los puntos críticos

### Pasos:

1. **Pasar todo a un lado** para tener $\frac{P(x)}{Q(x)} \lessgtr 0$
2. **Encontrar los ceros del numerador** (donde la fracción vale 0)
3. **Encontrar los ceros del denominador** (donde la fracción es indefinida)
4. **Ordenar todos los puntos críticos** en la recta numérica
5. **Evaluar el signo** en cada intervalo
6. **Seleccionar intervalos** según la desigualdad

---

## ⚙️ Ejemplo 1: Caso básico

Resolver: $\frac{x - 2}{x + 3} > 0$

**Paso 1:** Ya está en forma $\frac{P(x)}{Q(x)} > 0$

**Paso 2:** Cero del numerador: $x - 2 = 0 \Rightarrow x = 2$

**Paso 3:** Cero del denominador: $x + 3 = 0 \Rightarrow x = -3$ (excluido)

**Paso 4:** Puntos críticos ordenados: $-3$, $2$

```
←━━━━━━━━━┿━━━━━━━━━┿━━━━━━━━━→
         -3         2
    I      II       III
```

**Paso 5:** Evaluamos el signo

| Intervalo | Valor de prueba | $(x-2)$ | $(x+3)$ | Cociente |
|-----------|-----------------|---------|---------|----------|
| $(-\infty, -3)$ | $x = -4$ | $(-)$ | $(-)$ | $(+)$ |
| $(-3, 2)$ | $x = 0$ | $(-)$ | $(+)$ | $(-)$ |
| $(2, +\infty)$ | $x = 3$ | $(+)$ | $(+)$ | $(+)$ |

**Paso 6:** Necesitamos $> 0$

**Solución:** $x \in (-\infty, -3) \cup (2, +\infty)$

Nota: $x = -3$ se excluye porque el denominador es cero.

---

## ⚙️ Ejemplo 2: Con desigualdad no estricta

Resolver: $\frac{x + 1}{x - 4} \leq 0$

**Paso 1:** Cero del numerador: $x = -1$ (puede incluirse)

**Paso 2:** Cero del denominador: $x = 4$ (nunca se incluye)

**Paso 3:** Analizamos signos

| Intervalo | $(x+1)$ | $(x-4)$ | Cociente |
|-----------|---------|---------|----------|
| $(-\infty, -1)$ | $(-)$ | $(-)$ | $(+)$ |
| $(-1, 4)$ | $(+)$ | $(-)$ | $(-)$ |
| $(4, +\infty)$ | $(+)$ | $(+)$ | $(+)$ |

**Paso 4:** Necesitamos $\leq 0$ (negativo o cero)

- En $(-1, 4)$: negativo ✓
- En $x = -1$: el cociente es $0$ ✓
- En $x = 4$: indefinido ✗

**Solución:** $x \in [-1, 4)$

---

## ⚙️ Ejemplo 3: Con factores cuadráticos

Resolver: $\frac{x^2 - 4}{x - 1} \geq 0$

**Paso 1:** Factorizamos el numerador
$$
\frac{(x - 2)(x + 2)}{x - 1} \geq 0
$$

**Paso 2:** Puntos críticos:
- Numerador: $x = -2$, $x = 2$ (pueden incluirse)
- Denominador: $x = 1$ (excluido)

**Paso 3:** Ordenamos: $-2$, $1$, $2$

| Intervalo | $(x-2)$ | $(x+2)$ | $(x-1)$ | Producto |
|-----------|---------|---------|---------|----------|
| $(-\infty, -2)$ | $(-)$ | $(-)$ | $(-)$ | $(-)$ |
| $(-2, 1)$ | $(-)$ | $(+)$ | $(-)$ | $(+)$ |
| $(1, 2)$ | $(-)$ | $(+)$ | $(+)$ | $(-)$ |
| $(2, +\infty)$ | $(+)$ | $(+)$ | $(+)$ | $(+)$ |

**Paso 4:** Necesitamos $\geq 0$

**Solución:** $x \in [-2, 1) \cup [2, +\infty)$

---

## ⚙️ Ejemplo 4: Restar fracciones primero

Resolver: $\frac{3}{x - 2} > \frac{2}{x + 1}$

**Paso 1:** Pasamos todo a un lado
$$
\frac{3}{x - 2} - \frac{2}{x + 1} > 0
$$

**Paso 2:** Operamos con un denominador común
$$
\frac{3(x + 1) - 2(x - 2)}{(x - 2)(x + 1)} > 0
$$
$$
\frac{3x + 3 - 2x + 4}{(x - 2)(x + 1)} > 0
$$
$$
\frac{x + 7}{(x - 2)(x + 1)} > 0
$$

**Paso 3:** Puntos críticos: $x = -7$, $x = -1$, $x = 2$

| Intervalo | $(x+7)$ | $(x+1)$ | $(x-2)$ | Total |
|-----------|---------|---------|---------|-------|
| $(-\infty, -7)$ | $(-)$ | $(-)$ | $(-)$ | $(-)$ |
| $(-7, -1)$ | $(+)$ | $(-)$ | $(-)$ | $(+)$ |
| $(-1, 2)$ | $(+)$ | $(+)$ | $(-)$ | $(-)$ |
| $(2, +\infty)$ | $(+)$ | $(+)$ | $(+)$ | $(+)$ |

**Solución:** $x \in (-7, -1) \cup (2, +\infty)$

---

## 📊 Resumen de reglas

| Tipo de punto | ¿Se puede incluir? |
|---------------|-------------------|
| Cero del numerador con $\leq$ o $\geq$ | ✅ Sí |
| Cero del numerador con $<$ o $>$ | ❌ No |
| Cero del denominador | ❌ **Nunca** |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve las siguientes inecuaciones:

a) $\frac{x - 5}{x + 2} \geq 0$
b) $\frac{2x + 3}{x - 1} < 0$
c) $\frac{x^2 - 1}{x + 4} > 0$

<details>
<summary>Ver soluciones</summary>

a) Puntos críticos: $5$ (num), $-2$ (den)
   
   Signos: $(+)$ en $(-\infty, -2)$, $(-)$ en $(-2, 5)$, $(+)$ en $(5, +\infty)$
   
   **Solución:** $(-\infty, -2) \cup [5, +\infty)$

b) Puntos críticos: $-\frac{3}{2}$ (num), $1$ (den)
   
   **Solución:** $\left(-\frac{3}{2}, 1\right)$

c) $\frac{(x-1)(x+1)}{x+4} > 0$. Puntos críticos: $-4$, $-1$, $1$
   
   **Solución:** $(-4, -1) \cup (1, +\infty)$
</details>

---

**Ejercicio 2:** Resuelve:

$$\frac{x - 3}{x + 2} \leq 1$$

<details>
<summary>Ver solución</summary>

Restamos 1: $\frac{x - 3}{x + 2} - 1 \leq 0$

$\frac{x - 3 - (x + 2)}{x + 2} \leq 0$

$\frac{-5}{x + 2} \leq 0$

El numerador es $-5 < 0$ (siempre negativo).

Necesitamos que el cociente sea $\leq 0$, lo que ocurre cuando el denominador es positivo.

$x + 2 > 0 \Rightarrow x > -2$

**Solución:** $(-2, +\infty)$
</details>
