---
title: "Familias de Rectas"
---

# **Familias de Rectas**

En la vida real, las cosas cambian. Una tubería puede girar, un rayo de sol cambia de ángulo durante el día. Una **familia de rectas** es una ecuación que representa no una, sino **infinitas** rectas que comparten una característica común (como pasar por el mismo punto o ser paralelas).

---

## 🎯 ¿Qué vas a aprender?

- Qué es un "parámetro" ($k$) y cómo controla a la familia.
- La familia de rectas paralelas (vías de tren).
- La familia de rectas concurrentes (rayos de sol).
- Cómo usar $k$ para encontrar una recta específica.

---

## 👨‍👩‍👧‍👦 ¿Qué es una Familia?

Es un grupo de rectas unidas por un ADN común.
La ecuación tiene una variable extra (usualmente $k$ o $\lambda$) llamada **parámetro**. Al cambiar $k$, generas una recta distinta de la familia.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">El Haz de Rectas</strong>
  </div>
  <img src="/images/geometria/analitica/familias-rectas.svg" alt="Familia de rectas (haz)" style="width: 100%; height: auto;" />
</div>

---

## 🛤️ Tipos Principales

### 1. Familia de Paralelas
Todas tienen la **misma pendiente** $m$, pero diferente altura $k$.
$$ y = mx + k $$
*   Ejemplo: $y = 2x + k$.
    *   Si $k=1 \to y=2x+1$.
    *   Si $k=5 \to y=2x+5$.
    (Todas suben igual, son paralelas).

### 2. Familia de Concurrentes (Punto Común)
Todas pasan por el **mismo punto** $(x_1, y_1)$, pero con diferente pendiente $k$.
$$ y - y_1 = k(x - x_1) $$
*   Ejemplo: $y - 2 = k(x - 3)$.
    *   Todas las rectas pasan por $(3, 2)$, girando como manecillas de reloj.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Encontrar el Miembro Perdido
Encuentra la recta de la familia $y = 3x + k$ que pasa por $(2, 10)$.
1.  Sustituimos el punto en la ecuación:
    $10 = 3(2) + k$.
2.  Despejamos $k$:
    $10 = 6 + k \Rightarrow k = 4$.
3.  Reescribimos la ecuación completa:
    **Resultado:** $\boxed{y = 3x + 4}$.

### Ejemplo 2: Haz de Rectas
Encuentra la recta que pasa por la intersección de $x+y-2=0$ y $x-y=0$, y también por $(4,0)$.
1.  Formamos la familia (Haz):
    $(x+y-2) + k(x-y) = 0$.
2.  Sustituimos el punto extra $(4,0)$:
    $(4+0-2) + k(4-0) = 0$.
    $2 + 4k = 0 \Rightarrow 4k = -2 \Rightarrow k = -0.5$.
3.  Sustituimos $k$ de vuelta:
    $(x+y-2) - 0.5(x-y) = 0$.
    Multiplicamos por 2 para limpiar:
	$2(x+y-2) - (x-y) = 0$.
    $2x + 2y - 4 - x + y = 0$.
    $x + 3y - 4 = 0$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la familia de rectas paralelas a $y = 5x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Misma pendiente $m=5$.

**Respuesta:** $\boxed{y = 5x + k}$
</details>

---

### Ejercicio 2
Escribe la familia de rectas que pasan por el origen.

<details>
<summary>Ver solución</summary>
<br>
**Razonamiento:**
Corte y es 0. La pendiente $m$ (o $k$) es libre.

**Respuesta:** $\boxed{y = kx}$
</details>

---

### Ejercicio 3
Halla $k$ para que la recta $2x + 3y + k = 0$ pase por $(1, 1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2(1) + 3(1) + k = 0 \Rightarrow 5 + k = 0 \Rightarrow k = -5$.

**Respuesta:** $\boxed{-5}$
</details>

---

### Ejercicio 4
Escribe la familia de rectas verticales.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Siempre $x = \text{constante}$.

**Respuesta:** $\boxed{x = k}$
</details>

---

### Ejercicio 5
De la familia $y - 3 = k(x - 2)$, ¿cuál es el punto común?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Comparar con $y-y_1 = m(x-x_1)$.

**Respuesta:** $\boxed{(2, 3)}$
</details>

---

### Ejercicio 6
Halla la recta paralela a $y=x$ que pasa por $(0, -5)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Familia $y = x + k$.
$-5 = 0 + k \Rightarrow k = -5$.

**Respuesta:** $\boxed{y = x - 5}$
</details>

---

### Ejercicio 7
¿Qué característica tienen las rectas $Ax + By + k = 0$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Tienen la misma pendiente $-A/B$.

**Respuesta:** **Son paralelas**
</details>

---

### Ejercicio 8
Encuentra la recta del haz $(x+y) + k(x-y) = 0$ donde $k=1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x+y + x-y = 0 \Rightarrow 2x = 0 \Rightarrow x=0$.

**Respuesta:** $\boxed{x = 0 \text{ (Eje Y)}}$
</details>

---

### Ejercicio 9
Si $k$ puede ser cualquier número, ¿cuántas rectas hay en la familia?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Infinitos valores para $k$.

**Respuesta:** **Infinitas**
</details>

---

### Ejercicio 10
Escribe la familia de rectas horizontales.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La altura $y$ es constante.

**Respuesta:** $\boxed{y = k}$
</details>

---

## 🔑 Resumen

| Ecuación con $k$ | Tipo de Familia | Efecto Visual |
| :--- | :--- | :--- |
| **$y = mx + k$** | Paralelas | La recta sube o baja (ascensor). |
| **$y - y_1 = k(x - x_1)$** | Concurrentes | La recta gira sobre un eje (molino). |

> **Conclusión:** Una familia de rectas es una "plantilla". Define las reglas del juego, y el parámetro $k$ elige al jugador específico que necesitas.
