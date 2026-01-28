---
title: "Recta Tangente a la Hipérbola"
---

# **Recta Tangente a la Hipérbola**

La tangente a la hipérbola tiene una propiedad de reflexión fascinante: es la bisectriz del ángulo formado por los dos focos. Esto se usa en telescopios Cassegrain y en sistemas de navegación de largo alcance.

---

## 🎯 ¿Qué vas a aprender?

- Método de Desdoblamiento para la tangente.
- Tangentes con pendiente conocida.
- La condición de tangencia (Discriminante).

---

## 🎱 Ecuación por Desdoblamiento

Si el punto $P(x_1, y_1)$ **pertenece** a la curva, usamos el truco mágico de siempre:
*   $x^2 \to x_1 x$
*   $y^2 \to y_1 y$

**Fórmula (Horizontal):**
$$ \frac{x_1 x}{a^2} - \frac{y_1 y}{b^2} = 1 $$

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Tangente a la Hipérbola</strong>
  </div>
  <img src="/images/geometria/analitica/tangente-hiperbola.svg" alt="Recta tangente en la hipérbola" style="width: 100%; height: auto;" />
</div>

---

## ⛰️ Tangente con Pendiente $m$

Para encontrar las rectas tangentes con una inclinación fija ($m$):

**Horizontal:**
$$ y = mx \pm \sqrt{a^2 m^2 - b^2} $$
*(Condición: Para que exista, lo de adentro de la raíz debe ser positivo. $|m| > b/a$. Si $m$ es muy pequeña, la recta cruza la hipérbola como secante y no es tangente).*

**Vertical:**
$$ y = mx \pm \sqrt{b^2 - a^2 m^2} $$ (Cuidado con los signos aquí).
O mejor usa la forma general: sustituye $y=mx+k$ en la ecuación y haz que el discriminante sea cero.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: En un Punto
Tangente a $x^2 - y^2 = 16$ en $(5, 3)$.
1.  Verificar: $25 - 9 = 16$. Pertenece.
2.  Desdoblar ($x^2 \to 5x$, $y^2 \to 3y$):
    $$ 5x - 3y = 16 $$

### Ejemplo 2: Con Pendiente
Tangentes a $x^2/9 - y^2/4 = 1$ con $m=1$.
1.  $a^2=9, b^2=4$.
2.  Fórmula:
    $$ y = 1x \pm \sqrt{9(1)^2 - 4} $$
    $$ y = x \pm \sqrt{5} $$
    Dos rectas tangentes paralelas.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Tangente en el vértice $(a, 0)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{ax}{a^2} - 0 = 1 \Rightarrow x = a$. (Recta vertical).

**Respuesta:** $\boxed{x = a}$
</details>

---

### Ejercicio 2
Tangente a $x^2 - 4y^2 = 12$ en $(4, 1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$4x - 4(1)y = 12 \Rightarrow x - y = 3$.

**Respuesta:** $\boxed{x - y = 3}$
</details>

---

### Ejercicio 3
Condición para que exista tangente con pendiente $m$ (Horizontal).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La pendiente debe ser más empinada que la asíntota. $|m| > b/a$.

**Respuesta:** $\boxed{|m| > \frac{b}{a}}$
</details>

---

### Ejercicio 4
Tangentes desde el centro $(0,0)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ninguna tangente pasa por el centro (solo las asíntotas, que no tocan).

**Respuesta:** **Cero**
</details>

---

### Ejercicio 5
Calcula $\sqrt{a^2 m^2 - b^2}$ si $a=2, b=1, m=1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{4(1) - 1} = \sqrt{3}$.

**Respuesta:** $\boxed{\sqrt{3}}$
</details>

---

### Ejercicio 6
Tangente a $x^2/16 - y^2/20 = 1$ en $(6, 4)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$6x/16 - 4y/20 = 1 \Rightarrow 3x/8 - y/5 = 1$.

**Respuesta:** $\boxed{15x - 8y = 40}$
</details>

---

### Ejercicio 7
¿Puede una asíntota ser tangente?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No. Es tangente en el infinito, pero no en el plano real.

**Respuesta:** **No**
</details>

---

### Ejercicio 8
Tangentes horizontales ($m=0$) en hipérbola horizontal.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Raíz de $-b^2$. Imaginario. No tiene picos ni valles suaves.

**Respuesta:** **No existen**
</details>

---

### Ejercicio 9
Tangentes verticales en hipérbola horizontal.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
En los vértices. $x = \pm a$.

**Respuesta:** $\boxed{x = \pm a}$
</details>

---

### Ejercicio 10
Punto de corte de la tangente con el eje focal.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Depende del punto. Intersección con eje X.

**Respuesta:** **Variable**
</details>

---

## 🔑 Resumen

| Método | Fórmula | Requisito |
| :--- | :--- | :--- |
| **Desdoble** | $x_1 x / a^2 - \dots = 1$ | Conocer punto de contacto. |
| **Pendiente** | $\dots \pm \sqrt{a^2 m^2 - b^2}$ | $|m| >$ pendiente asíntota. |

> **Conclusión:** La tangente respeta las asíntotas. Nunca puede tener una pendiente que la haga cruzar las fronteras prohibidas del rectángulo guía.
