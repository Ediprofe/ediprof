# **Asíntotas de la Hipérbola**

Las asíntotas son las "rejas invisibles" de la hipérbola. Son dos líneas rectas que se cruzan en el centro y le dicen a la curva: "Puedes acercarte todo lo que quieras, pero jamás me tocarás".

---

## 🎯 ¿Qué vas a aprender?

- Qué es una asíntota y para qué sirve.
- Cómo dibujar el "Rectángulo Guía".
- Las fórmulas para hipérbolas Horizontales y Verticales.

---

## 🚧 El Rectángulo Guía

Antes de dibujar la curva, dibujamos una caja invisible.
1.  Marca los vértices $(\pm a, 0)$.
2.  Marca los puntos conjugados $(0, \pm b)$.
3.  Dibuja un rectángulo que pase por esos 4 puntos.
4.  Traza las **diagonales** extendidas de ese rectángulo. ¡Esas son las asíntotas!

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Asíntotas y Rectángulo</strong>
  </div>
  <img src="/images/geometria/analitica/asintotas-hiperbola.svg" alt="Asíntotas de la hipérbola y rectángulo guía" style="width: 100%; height: auto;" />
</div>

---

## 📐 Fórmulas de las Ecuaciones

La pendiente ($m$) es simplemente "subida sobre avance" ($\Delta y / \Delta x$).

| Tipo | Ecuación | Pendiente | Razón |
| :--- | :--- | :--- | :--- |
| **Horizontal** | $y = \pm \frac{b}{a}x$ | Subo $b$ (eje Y), Avanzo $a$ (eje X). | $y$ asociado a $b$. |
| **Vertical** | $y = \pm \frac{a}{b}x$ | Subo $a$ (eje Y), Avanzo $b$ (eje X). | $y$ asociado a $a$. |

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Horizontal
Para $\frac{x^2}{16} - \frac{y^2}{9} = 1$.
1.  $a = 4$ (Horizontal), $b = 3$.
2.  Formula: $y = \pm \frac{b}{a}x$.
3.  Asíntotas: $y = \frac{3}{4}x$ y $y = -\frac{3}{4}x$.

### Ejemplo 2: Vertical
Para $\frac{y^2}{25} - \frac{x^2}{4} = 1$.
1.  $a = 5$ (Vertical), $b = 2$.
2.  Formula: $y = \pm \frac{a}{b}x$.
3.  Asíntotas: $y = \frac{5}{2}x$ y $y = -\frac{5}{2}x$.

### Ejemplo 3: Equilátera
Para $x^2 - y^2 = 1$.
1.  $a = 1, b = 1$.
2.  $m = 1/1 = 1$.
3.  Asíntotas: $y = x$ y $y = -x$. (Se cruzan a 90 grados).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Pendiente de asíntotas para $x^2/36 - y^2/49 = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a=6, b=7$. Horizontal. $m = b/a$.

**Respuesta:** $\boxed{\pm 7/6}$
</details>

---

### Ejercicio 2
Pendiente de asíntotas para $y^2/36 - x^2/49 = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a=6, b=7$. Vertical. $m=a/b$.

**Respuesta:** $\boxed{\pm 6/7}$
</details>

---

### Ejercicio 3
Ecuación general de asíntotas si $a=b=k$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = k/k = 1$.

**Respuesta:** $\boxed{y = \pm x}$
</details>

---

### Ejercicio 4
¿Pasan las asíntotas por los focos?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No, pasan por el centro.

**Respuesta:** **No, por el centro**
</details>

---

### Ejercicio 5
Calcula las asíntotas de $4x^2 - 9y^2 = 36$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2/9 - y^2/4 = 1$. $a=3, b=2. Horizontal$. $y = \pm 2/3 x$.

**Respuesta:** $\boxed{y = \pm \frac{2}{3}x}$
</details>

---

### Ejercicio 6
Si las asíntotas son $y = \pm 2x$ y $a=1$ (Horizontal). Halla $b$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$b/a = 2 \Rightarrow b/1 = 2 \Rightarrow b=2$.

**Respuesta:** $\boxed{2}$
</details>

---

### Ejercicio 7
Ángulo entre las asíntotas de una hipérbola equilátera.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Son perpendiculares. $m=1$ y $m=-1$.

**Respuesta:** $\boxed{90^\circ}$
</details>

---

### Ejercicio 8
¿Toca la hipérbola a la asíntota en el infinito?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Conceptualmente sí (límite), geométricamente nunca.

**Respuesta:** **Nunca**
</details>

---

### Ejercicio 9
Dibuja el rectángulo guía de $x^2/4 - y^2/4 = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es un cuadrado de lado 4 centrado en origen.

**Respuesta:** **Un Cuadrado**
</details>

---

### Ejercicio 10
Ecuación de asíntotas si el centro es $(h,k)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Usar forma punto-pendiente: $y - k = \pm m(x - h)$.

**Respuesta:** $\boxed{y - k = \pm m(x - h)}$
</details>

---

## 🔑 Resumen

| Tipo | Pendiente | Mnemotecnia |
| :--- | :--- | :--- |
| **Horizontal** | $b/a$ | $y$ va con $b$. |
| **Vertical** | $a/b$ | $y$ va con $a$. |

> **Conclusión:** Las asíntotas son el esqueleto de la hipérbola. Dibújalas primero y la curva saldrá sola.
