# **Concepto de Lugar Geométrico**

Si te digo "todos los puntos que están a 5 metros de este poste", tu cerebro dibuja automáticamente un círculo. Si te digo "todos los puntos que están a la misma distancia de dos paredes", tu cerebro dibuja una línea diagonal. Eso es un **Lugar Geométrico**: una figura creada por una regla simple.

---

## 🎯 ¿Qué vas a aprender?

- Qué significa "Lugar Geométrico" (LG).
- Cómo traducir una frase en español a una ecuación matemática.
- Los LG más famosos: Circunferencia, Mediatriz, Bisectriz y Parábola.
- Cómo encontrar la ecuación de una figura misteriosa paso a paso.

---

## 📍 ¿Qué es un Lugar Geométrico?

Es el conjunto de **todos** los puntos $(x, y)$ que cumplen una condición específica. Ni uno más, ni uno menos.

Imagínalo como un club exclusivo.
*   **La Regla del Club:** "Solo entran los puntos cuya distancia al origen es 5".
*   **Los Miembros:** $(3,4), (5,0), (0,5), (-3,4)...$
*   **La Figura:** Si dibujas todos los miembros, obtienes una **Circunferencia**.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">De la Condición a la Gráfica</strong>
  </div>
  <img src="/images/geometria/analitica/lugar-circunferencia.svg" alt="Circunferencia como lugar geométrico" style="width: 100%; height: auto;" />
</div>

---

## 📝 Traduciendo Español a Matemáticas

Para hallar la ecuación de un LG, seguimos estos pasos:
1.  Tomamos un punto genérico $P(x, y)$.
2.  Escribimos la condición en fórmula matemática.
3.  Simplificamos.

### Ejemplo 1: La Circunferencia
**Condición:** "La distancia de $P(x,y)$ al origen $(0,0)$ es siempre 3".

**Traducción:**
$$ \sqrt{(x-0)^2 + (y-0)^2} = 3 $$
$$ \sqrt{x^2 + y^2} = 3 $$

Elevamos al cuadrado para quitar la raíz fea:
$$ x^2 + y^2 = 9 $$

### Ejemplo 2: La Mediatriz
**Condición:** "Puntos que están a la misma distancia de $A(0,0)$ y $B(4,0)$".

**Traducción:**
$$ d(P, A) = d(P, B) $$
$$ \sqrt{x^2 + y^2} = \sqrt{(x-4)^2 + y^2} $$

Simplificando (elevamos al cuadrado):
$$ x^2 + y^2 = x^2 - 8x + 16 + y^2 $$
Cancelamos $x^2$ y $y^2$:
$$ 0 = -8x + 16 $$
$$ 8x = 16 \Rightarrow x = 2 $$

**Interpretación:** Es una recta vertical que pasa por $x=2$ (justo a la mitad de 0 y 4).

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 3: Bisectriz (Equidistante a los ejes)
**Condición:** La distancia al eje X es igual a la distancia al eje Y.
*   Distancia a eje X: $|y|$
*   Distancia a eje Y: $|x|$

**Ecuación:**
$$ |x| = |y| $$
Esto nos da dos rectas: $y = x$ y $y = -x$.

### Ejemplo 4: Suma de Distancias (Elipse)
**Condición:** La suma de distancias a $(-3,0)$ y $(3,0)$ es 10.
$$ \sqrt{(x+3)^2 + y^2} + \sqrt{(x-3)^2 + y^2} = 10 $$
(Esta ecuación, al simplificarse, da la ecuación de una elipse).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Halla la ecuación de los puntos a distancia 5 del origen.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2 + y^2 = 5^2$.

**Respuesta:** $\boxed{x^2 + y^2 = 25}$
</details>

---

### Ejercicio 2
Halla el LG de los puntos con abscisa 4.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
"Abscisa es 4" significa $x = 4$. Es una recta vertical.

**Respuesta:** $\boxed{x = 4}$
</details>

---

### Ejercicio 3
Halla el LG de los puntos cuya ordenada es el doble de su abscisa.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$y = 2x$. Una recta que pasa por el origen.

**Respuesta:** $\boxed{y = 2x}$
</details>

---

### Ejercicio 4
Halla el LG de puntos equidistantes de $y=2$ y $y=-2$.

<details>
<summary>Ver solución</summary>
<br>
**Razonamiento:**
El punto medio entre 2 y -2 es 0.
Recta horizontal $y=0$ (Eje X).

**Respuesta:** $\boxed{y = 0}$
</details>

---

### Ejercicio 5
Describe el LG dado por $x^2 + y^2 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La única forma de sumar dos cuadrados y que dé 0 es si ambos son 0.
Es un solo punto: el origen $(0,0)$.

**Respuesta:** **El punto (0,0)**
</details>

---

### Ejercicio 6
Halla el LG de puntos a distancia 2 del punto $(1,1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Circunferencia desplazada.
$(x-1)^2 + (y-1)^2 = 2^2$.

**Respuesta:** $\boxed{(x-1)^2 + (y-1)^2 = 4}$
</details>

---

### Ejercicio 7
Halla el LG de puntos donde el producto de coordenadas es 1.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$xy = 1$ o $y = 1/x$.
Es una hipérbola.

**Respuesta:** $\boxed{xy = 1}$
</details>

---

### Ejercicio 8
¿Cuál es la ecuación del Eje Y?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
En el eje vertical, no te mueves horizontalmente. $x$ siempre es 0.

**Respuesta:** $\boxed{x = 0}$
</details>

---

### Ejercicio 9
Halla el LG de los puntos cuya distancia al eje X es 3.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$|y| = 3$. Son dos rectas horizontales: $y=3$ y $y=-3$.

**Respuesta:** $\boxed{y = \pm 3}$
</details>

---

### Ejercicio 10
Halla el LG de los puntos equidistantes de $(0,0)$ y $(10, 10)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es la mediatriz. Pasa por el punto medio $(5, 5)$ y tiene pendiente perpendicular.
$m_{AB} = 1$, así que $m_{\perp} = -1$.
$y - 5 = -1(x - 5) \Rightarrow y = -x + 10$.

**Respuesta:** $\boxed{x + y = 10}$
</details>

---

## 🔑 Resumen

| Figura | Condición Geométrica Típica |
| :--- | :--- |
| **Circunferencia** | Equidista de un punto (centro). |
| **Mediatriz** | Equidista de dos puntos. |
| **Paralela Media** | Equidista de dos rectas paralelas. |
| **Bisectriz** | Equidista de dos rectas que se cruzan. |

> **Conclusión:** Un lugar geométrico es la "huella" que deja un punto al moverse siguiendo una regla estricta. La ecuación es solo la forma de escribir esa regla en idioma álgebra.
