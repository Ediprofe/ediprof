---
title: "Recta Tangente a la Elipse"
---

# **Recta Tangente a la Elipse**

¿Alguna vez has jugado billar en una mesa elíptica? Si golpeas una bola desde un foco, rebotará (en la tangente) directo al otro foco. Esta propiedad acústica y óptica es legendaria y depende totalmente de la recta tangente.

---

## 🎯 ¿Qué vas a aprender?

- Ecuación de la tangente por el método de Desdoblamiento.
- Propiedad de reflexión focal.
- Ecuación si conoces la pendiente ($m$).

---

## 🎱 Ecuación por Desdoblamiento

Si tienes un punto $P(x_1, y_1)$ que **pertenece** a la elipse, hallar la tangente es facilísimo. Solo "desdobla" la ecuación:

**Regla de Oro:**
*   $x^2 \to x_1 x$
*   $y^2 \to y_1 y$

**Fórmula (Centro Origen):**
$$ \frac{x_1 x}{a^2} + \frac{y_1 y}{b^2} = 1 $$

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Tangente a la Elipse</strong>
  </div>
  <img src="/images/geometria/analitica/tangente-elipse.svg" alt="Recta tangente a la elipse" style="width: 100%; height: auto;" />
</div>

---

## ⛰️ Tangente con Pendiente $m$

Si no conoces el punto de contacto, pero buscas una tangente paralela a una dirección dada ($m$):

$$ y = mx \pm \sqrt{a^2 m^2 + b^2} $$

El $\pm$ indica que hay **dos** tangentes paralelas (una arriba y otra abajo).
*(Nota: Esta fórmula específica es para elipses horizontales centradas en el origen. Para verticales, intercambia $a$ y $b$. Para trasladadas, ajusta $(y-k)$ y $(x-h)$)*.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: En un Punto
Tangente a $\frac{x^2}{25} + \frac{y^2}{9} = 1$ en el punto $(0, -3)$.
1.  Verificar punto: $0/25 + 9/9 = 1$. Sí pertenece.
2.  Desdoblar:
    $$ \frac{(0)x}{25} + \frac{(-3)y}{9} = 1 $$
    $$ 0 - \frac{y}{3} = 1 \Rightarrow y = -3 $$
    Es una recta horizontal pegada al vértice inferior.

### Ejemplo 2: Con Pendiente
Tangentes con $m=1$ para la elipse anterior ($a^2=25, b^2=9$).
1.  Fórmula:
    $$ y = 1x \pm \sqrt{25(1)^2 + 9} $$
    $$ y = x \pm \sqrt{34} $$
2.  Las rectas son $y = x + 5.83$ y $y = x - 5.83$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Tangente en el vértice mayor derecho $(a, 0)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{ax}{a^2} + 0 = 1 \Rightarrow \frac{x}{a} = 1 \Rightarrow x = a$.

**Respuesta:** $\boxed{x = a}$
</details>

---

### Ejercicio 2
Tangente a $x^2 + 4y^2 = 4$ en $(\sqrt{2}, \frac{1}{\sqrt{2}})$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{2}x + 4(\frac{1}{\sqrt{2}})y = 4 \Rightarrow \sqrt{2}x + 2\sqrt{2}y = 4$.

**Respuesta:** $\boxed{\sqrt{2}x + 2\sqrt{2}y = 4}$
</details>

---

### Ejercicio 3
¿Cuántas tangentes se pueden trazar desde el centro $(0,0)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ninguna que toque el borde.

**Respuesta:** **Cero**
</details>

---

### Ejercicio 4
Pendiente de la tangente en un vértice menor.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es horizontal.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 5
Calcula $\sqrt{a^2m^2+b^2}$ si $a=3, b=4, m=0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{0 + 16} = 4$. Las tangentes son $y = \pm 4$.

**Respuesta:** $\boxed{4}$
</details>

---

### Ejercicio 6
Propiedad de la normal (perpendicular a tangente) en la elipse.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La normal es la bisectriz del ángulo formado por los radios focales.

**Respuesta:** **Bisectriz de los focos**
</details>

---

### Ejercicio 7
Tangente a $\frac{x^2}{10} + \frac{y^2}{5} = 1$ con $m=1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{10(1) + 5} = \sqrt{15}$.

**Respuesta:** $\boxed{y = x \pm \sqrt{15}}$
</details>

---

### Ejercicio 8
Si el punto no está en la elipse, ¿sirve el desdoblamiento?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No, daría la "recta polar", no la tangente.

**Respuesta:** **No**
</details>

---

### Ejercicio 9
Tangente a $x^2 + 2y^2 = 3$ en $(1, 1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$1x + 2(1)y = 3$.

**Respuesta:** $\boxed{x + 2y = 3}$
</details>

---

### Ejercicio 10
Ángulo entre las tangentes en los extremos de un diámetro.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Son paralelas ($m$ iguales).

**Respuesta:** **0 grados (Paralelas)**
</details>

---

## 🔑 Resumen

| Método | Fórmula | Uso |
| :--- | :--- | :--- |
| **Desdoble** | $\frac{x_1 x}{a^2} + \dots = 1$ | Punto en la curva. |
| **Pendiente** | $y = mx \pm \sqrt{\dots}$ | Dirección conocida. |

> **Conclusión:** La recta tangente es el espejo perfecto. Cualquier luz que salga de un foco, rebotará en la tangente y llegará inevitablemente al otro foco.
