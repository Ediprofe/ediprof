---
title: "Elipse Horizontal con Centro en el Origen"
---

# **Elipse Horizontal con Centro en el Origen**

La elipse más "clásica", acostada sobre el eje X. Es como un ojo mirando de frente. Su ecuación es simple, limpia y la base para entender todas las demás elipses.

---

## 🎯 ¿Qué vas a aprender?

- Reconocer la ecuación $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$.
- Por qué $a^2$ debajo de la $x$ significa "horizontal".
- Cómo extraer el centro, focos y vértices en segundos.

---

## 🚀 La Ecuación Canónica

La ecuación de una elipse centrada en $(0,0)$ y estirada horizontalmente es:

$$ \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 $$

**Condición Vital:**
Para que sea horizontal, el número debajo de la $x$ ($a^2$) debe ser **MAYOR** que el número debajo de la $y$ ($b^2$).
$$ a > b $$

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Elipse Horizontal</strong>
  </div>
  <img src="/images/geometria/analitica/elipse-horizontal.svg" alt="Elipse horizontal con centro en el origen" style="width: 100%; height: auto;" />
</div>

---

## 🔍 Anatomía de la Elipse Horizontal

Desde la ecuación:
1.  **Centro:** $(0, 0)$.
2.  **Vértices Mayores (Puntas):** $(\pm a, 0)$. (Sobre el eje X).
3.  **Vértices Menores (Altura):** $(0, \pm b)$. (Sobre el eje Y).
4.  **Focos:** $(\pm c, 0)$. (Sobre el eje X, adentro).
    *   Recuerda: $c = \sqrt{a^2 - b^2}$.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Elipse Canónica
Analiza $\frac{x^2}{25} + \frac{y^2}{16} = 1$.
1.  **Identificar:** El número mayor (25) está bajo $x$. $\to$ **Horizontal**.
2.  **Parámetros:**
    *   $a^2 = 25 \Rightarrow a = 5$.
    *   $b^2 = 16 \Rightarrow b = 4$.
3.  **Foco ($c$):**
    $$ c = \sqrt{25 - 16} = \sqrt{9} = 3 $$
4.  **Coordenadas:**
    *   Vértices: $(\pm 5, 0)$.
    *   Focos: $(\pm 3, 0)$.
    *   Centro: $(0, 0)$.

### Ejemplo 2: Ecuación desde Datos
Vértices en $(\pm 10, 0)$ y Focos en $(\pm 6, 0)$.
1.  **Eje:** Están en X $\to$ Horizontal.
2.  **Datos:** $a = 10, c = 6$.
3.  **Hallar $b$:**
    $$ b = \sqrt{100 - 36} = \sqrt{64} = 8 $$
4.  **Ecuación:**
    $$ \frac{x^2}{100} + \frac{y^2}{64} = 1 $$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Halla $a$ y $b$ de $\frac{x^2}{49} + \frac{y^2}{4} = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a = \sqrt{49} = 7$. $b = \sqrt{4} = 2$.

**Respuesta:** $\boxed{a=7, b=2}$
</details>

---

### Ejercicio 2
Calcula la distancia focal ($2c$) del ejercicio anterior.

<details>
<summary>Ver solución</summary>
**Razonamiento:**
$c = \sqrt{49-4} = \sqrt{45} \approx 6.7$.
$2c = 2\sqrt{45}$.

**Respuesta:** $\boxed{2\sqrt{45}}$
</details>

---

### Ejercicio 3
Escribe la ecuación si $a=5$ y $b=1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2/25 + y^2/1 = 1$.

**Respuesta:** $\boxed{\frac{x^2}{25} + y^2 = 1}$
</details>

---

### Ejercicio 4
Vértices $(\pm 8, 0)$, Eje menor 10 ($2b=10$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a=8 \Rightarrow a^2=64$. $b=5 \Rightarrow b^2=25$.

**Respuesta:** $\boxed{\frac{x^2}{64} + \frac{y^2}{25} = 1}$
</details>

---

### Ejercicio 5
¿Pasa la elipse $\frac{x^2}{100} + \frac{y^2}{36} = 1$ por $(0, 6)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$0/100 + 36/36 = 0 + 1 = 1$.

**Respuesta:** **Sí**
</details>

---

### Ejercicio 6
Longitud del lado recto si $a=5, b=4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$LR = 2b^2/a = 2(16)/5 = 32/5 = 6.4$.

**Respuesta:** $\boxed{6.4}$
</details>

---

### Ejercicio 7
Excentricidad de $\frac{x^2}{16} + \frac{y^2}{12} = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$c = \sqrt{16-12} = 2$. $a=4$. $e = 2/4 = 0.5$.

**Respuesta:** $\boxed{0.5}$
</details>

---

### Ejercicio 8
Si $a^2$ estuviera bajo $y$, ¿sería horizontal?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No, sería vertical. El mayor manda.

**Respuesta:** **No**
</details>

---

### Ejercicio 9
Halla la ecuación si Focos $(\pm 4, 0)$ y $a=5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$c=4, a=5 \Rightarrow b=3$.
$x^2/25 + y^2/9 = 1$.

**Respuesta:** $\boxed{\frac{x^2}{25} + \frac{y^2}{9} = 1}$
</details>

---

### Ejercicio 10
¿Dónde corta al eje Y la elipse $\frac{x^2}{25} + \frac{y^2}{1} = 1$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
En los vértices menores $\pm b$. $b=1$.

**Respuesta:** $\boxed{(0, 1) \text{ y } (0, -1)}$
</details>

---

## 🔑 Resumen

| Ecuación | Identificador | Vértices |
| :--- | :--- | :--- |
| **$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$** | $x^2$ tiene el denominador grande. | $(\pm a, 0)$ |

> **Conclusión:** Busca siempre el número más grande abajo. Si está bajo la $X$, la elipse es **Horizontal**. El número grande siempre es $a^2$.
