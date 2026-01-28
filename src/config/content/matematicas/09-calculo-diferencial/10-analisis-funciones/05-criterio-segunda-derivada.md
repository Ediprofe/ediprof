---
title: "Criterio de la Segunda Derivada"
---

# Criterio de la Segunda Derivada

El criterio de la segunda derivada ofrece una forma alternativa y a menudo más rápida de clasificar puntos críticos como máximos o mínimos.

---

## 🎯 ¿Qué vas a aprender?

- El criterio de la segunda derivada
- Cuándo usarlo
- Sus limitaciones
- Comparación con el criterio de la primera derivada

---

## 📖 El criterio

Sea $c$ un punto crítico donde $f'(c) = 0$:

| Valor de $f''(c)$ | Conclusión |
|-------------------|------------|
| $f''(c) > 0$ | **Mínimo relativo** en $c$ |
| $f''(c) < 0$ | **Máximo relativo** en $c$ |
| $f''(c) = 0$ | **Inconcluso** (usar otro criterio) |

---

## 📖 Interpretación

- $f''(c) > 0$: curva cóncava arriba → "valle" → mínimo
- $f''(c) < 0$: curva cóncava abajo → "colina" → máximo

---

## ⚙️ Ejemplo 1: Aplicación directa

$f(x) = x^3 - 6x^2 + 9x + 1$

**Paso 1:** $f'(x) = 3x^2 - 12x + 9 = 3(x^2 - 4x + 3) = 3(x-1)(x-3)$

**Paso 2:** Puntos críticos: $x = 1, 3$

**Paso 3:** $f''(x) = 6x - 12$

**Paso 4:** Evaluar:
- $f''(1) = 6 - 12 = -6 < 0$ → **Máximo en $x = 1$**
- $f''(3) = 18 - 12 = 6 > 0$ → **Mínimo en $x = 3$**

**Valores:**
- Máximo: $f(1) = 1 - 6 + 9 + 1 = 5$
- Mínimo: $f(3) = 27 - 54 + 27 + 1 = 1$

---

## ⚙️ Ejemplo 2: Función exponencial

$f(x) = xe^{-x}$

$$f'(x) = e^{-x} - xe^{-x} = e^{-x}(1 - x) = 0$$

**Punto crítico:** $x = 1$

$$f''(x) = -e^{-x}(1-x) + e^{-x}(-1) = e^{-x}(x - 2)$$

$$f''(1) = e^{-1}(1 - 2) = -\frac{1}{e} < 0$$

**Máximo relativo** en $x = 1$, valor $f(1) = \frac{1}{e}$

---

## ⚙️ Ejemplo 3: Caso inconcluso

$f(x) = x^4$

$$f'(x) = 4x^3 = 0 \Rightarrow x = 0$$

$$f''(x) = 12x^2$$

$$f''(0) = 0$$ → **Inconcluso**

Debemos usar el criterio de la primera derivada:
- $f'(x) < 0$ para $x < 0$
- $f'(x) > 0$ para $x > 0$

Cambia de $-$ a $+$ → **Mínimo** en $x = 0$

---

## ⚙️ Ejemplo 4: Otro caso inconcluso

$f(x) = x^3$

$$f'(x) = 3x^2 = 0 \Rightarrow x = 0$$

$$f''(0) = 0$$ → Inconcluso

Primera derivada: $f'(x) > 0$ para todo $x \neq 0$

No cambia de signo → **No hay extremo** (es punto de inflexión)

---

## 📖 Comparación de criterios

| Aspecto | Primera derivada | Segunda derivada |
|---------|-----------------|------------------|
| Información requerida | Signo de $f'$ a ambos lados | Valor de $f''$ en el punto |
| Siempre funciona | Sí | No (puede ser inconcluso) |
| Velocidad | Requiere analizar intervalos | Solo evaluar un valor |
| Cuando $f'(c)$ no existe | Funciona | No aplica |

---

## ⚙️ Ejemplo 5: Función racional

$f(x) = \frac{x}{x^2 + 4}$

$$f'(x) = \frac{x^2 + 4 - 2x^2}{(x^2+4)^2} = \frac{4 - x^2}{(x^2+4)^2}$$

**Puntos críticos:** $x = \pm 2$

$$f''(x) = \frac{d}{dx}\left[\frac{4-x^2}{(x^2+4)^2}\right]$$

Tras cálculos: $f''(x) = \frac{2x(x^2 - 12)}{(x^2+4)^3}$

$$f''(2) = \frac{4(4-12)}{(8)^3} = \frac{-32}{512} = -\frac{1}{16} < 0$$ → Máximo

$$f''(-2) = \frac{-4(4-12)}{(8)^3} = \frac{32}{512} = \frac{1}{16} > 0$$ → Mínimo

---

## 📖 Cuándo preferir cada criterio

**Usa segunda derivada cuando:**
- $f''$ es fácil de calcular
- $f''(c) \neq 0$
- Quieres clasificar rápidamente

**Usa primera derivada cuando:**
- El criterio de segunda es inconcluso
- $f'$ no existe en el punto crítico
- Ya tienes la tabla de signos de $f'$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Usa el criterio de segunda derivada:

$$f(x) = x^2 e^x$$

<details>
<summary>Ver solución</summary>

$f'(x) = 2xe^x + x^2e^x = e^x \cdot x(x+2) = 0$

Puntos críticos: $x = 0, -2$

$f''(x) = e^x(x^2 + 4x + 2)$

$f''(0) = 2 > 0$ → **Mínimo**

$f''(-2) = e^{-2}(4 - 8 + 2) = -2e^{-2} < 0$ → **Máximo**
</details>

---

**Ejercicio 2:** Clasifica los extremos de $f(x) = x - \ln x$.

<details>
<summary>Ver solución</summary>

$f'(x) = 1 - \frac{1}{x} = 0 \Rightarrow x = 1$

$f''(x) = \frac{1}{x^2}$

$f''(1) = 1 > 0$ → **Mínimo** en $x = 1$, $f(1) = 1$
</details>
