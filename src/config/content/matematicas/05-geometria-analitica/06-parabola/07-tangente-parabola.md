---
title: "Recta Tangente a la Parábola"
---

# **Recta Tangente a la Parábola**

Las antenas parabólicas funcionan porque tienen una propiedad mágica de reflexión. Cualquier rayo que golpee la superficie rebota directamente al foco. ¿Quién decide ese rebote? La **Recta Tangente**.

---

## 🎯 ¿Qué vas a aprender?

- Propiedad de reflexión: Ángulo de incidencia = Ángulo de reflexión.
- La ecuación de la tangente en un punto dado $(x_1, y_1)$.
- La ecuación si solo conoces la pendiente $m$.

---

## 🔭 Ecuación de la Tangente (Desdoblamiento)

Si tienes un punto de contacto $(x_1, y_1)$ que PERTENECE a la parábola, usa el truco del **Desdoblamiento**:
*   Cambia $x^2$ por $x_1 x$.
*   Cambia $y^2$ por $y_1 y$.
*   Cambia $x$ por $\frac{x + x_1}{2}$.
*   Cambia $y$ por $\frac{y + y_1}{2}$.

### Fórmulas Resultantes:

| Parábola | Tangente en $(x_1, y_1)$ |
| :--- | :--- |
| **$y^2 = 4px$** | $y_1 y = 2p(x + x_1)$ |
| **$x^2 = 4py$** | $x_1 x = 2p(y + y_1)$ |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Tangente a la Parábola</strong>
  </div>
  <img src="/images/geometria/analitica/tangente-parabola.svg" alt="Recta tangente a la parábola" style="width: 100%; height: auto;" />
</div>

---

## ⛰️ Tangente con Pendiente $m$

Si no sabes dónde toca, pero sabes la inclinación ($m$), la tangente es única (para parábolas).

Para $y^2 = 4px$:
$$ y = mx + \frac{p}{m} $$

*(Nota: $m \neq 0$)*.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Tangente en un Punto
Tangente a $y^2 = 8x$ en el punto $(2, 4)$.
1.  Verificar: $4^2 = 16$. $8(2) = 16$. Pertenece.
2.  $4p=8 \Rightarrow 2p=4$.
3.  Fórmula: $4y = 4(x + 2)$.
4.  Simplificar: $y = x + 2$.

### Ejemplo 2: Tangente con Pendiente
Tangente a $x^2 = 12y$ con pendiente $m=2$.
(Ojo: La fórmula $p/m$ es para horizontales. Para verticales usamos otra o derivamos, pero usemos el método general de discriminante o desdoble).
Mejor truco para Verticales ($x^2=4py$): La tangente es $y = mx - pm^2$.
1.  Verificamos $m=2, p=3$.
2.  $y = 2x - 3(2^2) = 2x - 12$.

### Ejemplo 3: Propiedad Reflectiva
Si lanzas un rayo paralelo al eje X hacia $y^2 = 4x$, rebotará hacia el foco $(1, 0)$. La tangente en el punto de choque funciona como un espejo plano exacto para ese ángulo.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Tangente a $y^2 = 4x$ en $(1, 2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2y = 2(1)(x+1) \Rightarrow 2y = 2x + 2 \Rightarrow y = x+1$.

**Respuesta:** $\boxed{y = x + 1}$
</details>

---

### Ejercicio 2
Tangente a $x^2 = 4y$ en $(2, 1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2x = 2(1)(y+1) \Rightarrow 2x = 2y + 2 \Rightarrow x = y + 1$.

**Respuesta:** $\boxed{y = x - 1}$
</details>

---

### Ejercicio 3
Pendiente de la tangente en el vértice $(0,0)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Para $y^2=4px$, tangente es eje Y (vertical, $\infty$). Para $x^2=4py$, eje X (0).

**Respuesta:** **0 o Indefinida**
</details>

---

### Ejercicio 4
Ecuación con pendiente $m=1$ para $y^2 = 16x$ ($p=4$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$y = 1x + 4/1$.

**Respuesta:** $\boxed{y = x + 4}$
</details>

---

### Ejercicio 5
¿Cuántas tangentes paralelas a una recta dada tiene una parábola?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Solo una. (A diferencia del círculo que tiene dos).

**Respuesta:** **Una**
</details>

---

### Ejercicio 6
Intersección de la tangente en extremo del lado recto con el eje.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Propiedad geométrica: corta al eje en Directriz.

**Respuesta:** **En la intersección Eje-Directriz**
</details>

---

### Ejercicio 7
Tangente a $y^2 = -8x$ en $(-2, 4)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2p = -4$. $4y = -4(x - 2)$. $y = -x + 2$.

**Respuesta:** $\boxed{x + y - 2 = 0}$
</details>

---

### Ejercicio 8
Usa la fórmula $p/m$ para $m=0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
División por cero. La tangente horizontal es el Eje X (para parábola horizontal), que toca en el vértice.

**Respuesta:** **No se puede (es el eje)**
</details>

---

### Ejercicio 9
Tangente a $x^2 = y$ en $(-1, 1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$-1x = 0.5(y+1) \Rightarrow -2x = y + 1$.

**Respuesta:** $\boxed{2x + y + 1 = 0}$
</details>

---

### Ejercicio 10
Ángulo entre las tangentes que se cruzan en la directriz.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Propiedad famosa: siempre son perpendiculares.

**Respuesta:** **90 grados**
</details>

---

## 🔑 Resumen

| Método | Fórmula | Uso |
| :--- | :--- | :--- |
| **Desdoble** | $y_1 y = 2p(x + x_1)$ | Cuando tienes el punto de contacto. |
| **Pendiente** | $y = mx + p/m$ | Cuando buscas una dirección específica. |

> **Conclusión:** La tangente es la "piel" de la parábola. Define su forma y dirección en cada centímetro.
