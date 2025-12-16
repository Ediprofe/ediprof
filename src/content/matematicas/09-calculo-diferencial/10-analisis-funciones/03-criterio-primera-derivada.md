# Criterio de la Primera Derivada

El criterio de la primera derivada nos permite clasificar los puntos críticos como máximos, mínimos o ninguno, analizando el cambio de signo de la derivada.

---

## 🎯 ¿Qué vas a aprender?

- El criterio de la primera derivada
- Cómo clasificar extremos relativos
- Aplicación sistemática del método
- Casos donde no hay extremo

---

## 📖 El criterio

Sea $c$ un punto crítico de $f$:

| Cambio de signo de $f'$ | Conclusión |
|-------------------------|------------|
| $+ \to -$ (pasa de positivo a negativo) | **Máximo relativo** en $c$ |
| $- \to +$ (pasa de negativo a positivo) | **Mínimo relativo** en $c$ |
| $+ \to +$ o $- \to -$ (no cambia) | **No hay extremo** en $c$ |

---

## 📖 Método completo

1. Encontrar $f'(x)$
2. Hallar puntos críticos: $f'(x) = 0$ o $f'$ no existe
3. Hacer tabla de signos de $f'$
4. Determinar cambios de signo en cada punto crítico
5. Clasificar cada punto crítico

---

## ⚙️ Ejemplo 1: Aplicación completa

$f(x) = x^3 - 3x + 2$

**Paso 1:** $f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 3(x-1)(x+1)$

**Paso 2:** Puntos críticos: $x = -1, 1$

**Paso 3:** Tabla de signos:

| Intervalo | $(x-1)$ | $(x+1)$ | $f'(x)$ |
|-----------|---------|---------|---------|
| $x < -1$ | $-$ | $-$ | $+$ |
| $-1 < x < 1$ | $-$ | $+$ | $-$ |
| $x > 1$ | $+$ | $+$ | $+$ |

**Paso 4-5:**
- En $x = -1$: $f'$ cambia de $+$ a $-$ → **Máximo relativo**
- En $x = 1$: $f'$ cambia de $-$ a $+$ → **Mínimo relativo**

**Valores:**
- $f(-1) = -1 + 3 + 2 = 4$ (máximo)
- $f(1) = 1 - 3 + 2 = 0$ (mínimo)

---

## ⚙️ Ejemplo 2: Sin extremo

$f(x) = x^3$

$$f'(x) = 3x^2$$

**Punto crítico:** $x = 0$

**Signos:** $f'(x) \geq 0$ para todo $x$

En $x = 0$: $f'$ pasa de $+$ a $+$ (no cambia signo)

**No hay extremo** en $x = 0$ (es punto de inflexión).

---

## ⚙️ Ejemplo 3: Función con valor absoluto

$f(x) = |x - 2|$

**Punto crítico:** $x = 2$ (donde $f'$ no existe)

**Signos:**
- Para $x < 2$: $f(x) = -(x-2)$ → $f'(x) = -1$
- Para $x > 2$: $f(x) = x-2$ → $f'(x) = 1$

$f'$ cambia de $-$ a $+$ en $x = 2$

**Mínimo relativo** en $(2, 0)$

---

## ⚙️ Ejemplo 4: Función racional

$f(x) = \frac{x^2}{x - 1}$

De un ejemplo anterior: $f'(x) = \frac{x(x-2)}{(x-1)^2}$

**Puntos críticos:** $x = 0, 2$ (recordando que $x = 1$ no está en el dominio)

**Tabla de signos:**

| Intervalo | $x$ | $x-2$ | $(x-1)^2$ | $f'$ |
|-----------|-----|-------|-----------|------|
| $x < 0$ | $-$ | $-$ | $+$ | $+$ |
| $0 < x < 1$ | $+$ | $-$ | $+$ | $-$ |
| $1 < x < 2$ | $+$ | $-$ | $+$ | $-$ |
| $x > 2$ | $+$ | $+$ | $+$ | $+$ |

**Clasificación:**
- $x = 0$: $+ \to -$ → **Máximo relativo**, $f(0) = 0$
- $x = 2$: $- \to +$ → **Mínimo relativo**, $f(2) = 4$

---

## ⚙️ Ejemplo 5: Función trigonométrica

$f(x) = \sin x + \cos x$ en $[0, 2\pi]$

$$f'(x) = \cos x - \sin x = 0 \Rightarrow x = \frac{\pi}{4}, \frac{5\pi}{4}$$

**Signos:**
- En $(0, \frac{\pi}{4})$: $f'(\frac{\pi}{8}) > 0$
- En $(\frac{\pi}{4}, \frac{5\pi}{4})$: $f'(\pi) < 0$
- En $(\frac{5\pi}{4}, 2\pi)$: $f'(\frac{3\pi}{2}) > 0$

**Clasificación:**
- $x = \frac{\pi}{4}$: $+ \to -$ → Máximo, $f(\frac{\pi}{4}) = \sqrt{2}$
- $x = \frac{5\pi}{4}$: $- \to +$ → Mínimo, $f(\frac{5\pi}{4}) = -\sqrt{2}$

---

## 📊 Resumen visual

```
      f'(x) > 0    f'(x) < 0
          ↗            ↘
           \          /
            • máximo
            
      f'(x) < 0    f'(x) > 0
          ↘            ↗
           \          /
            • mínimo
```

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Clasifica los puntos críticos de $f(x) = x^4 - 4x^3$.

<details>
<summary>Ver solución</summary>

$f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3)$

Puntos críticos: $x = 0, 3$

- En $x = 0$: $f'$ tiene signo $(-)(−) = −$ para $x < 0$ y $(+)(−) = −$ para $0 < x < 3$. No cambia → **No es extremo**

- En $x = 3$: $f'$ cambia de $-$ a $+$ → **Mínimo relativo**, $f(3) = 81 - 108 = -27$
</details>

---

**Ejercicio 2:** Encuentra extremos de $f(x) = xe^{-x}$.

<details>
<summary>Ver solución</summary>

$f'(x) = e^{-x} - xe^{-x} = e^{-x}(1-x)$

Punto crítico: $x = 1$

$e^{-x} > 0$ siempre
$(1-x) > 0$ para $x < 1$
$(1-x) < 0$ para $x > 1$

$f'$ cambia de $+$ a $-$ → **Máximo en $x = 1$**, $f(1) = \frac{1}{e}$
</details>
