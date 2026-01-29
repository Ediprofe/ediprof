# **Gráfica de la Función Tangente**

Si el seno y el coseno son las ondas suaves del mar, la **tangente** es un cohete despegando. A diferencia de sus hermanas, la gráfica de la tangente se rompe, tiene muros invisibles llamados asíntotas y dispara sus valores hasta el infinito. ¡Es la rebelde de la trigonometría!

---

## 🎯 ¿Qué vas a aprender?

- Por qué la gráfica de la tangente tiene "huecos" o asíntotas.
- Por qué su período es $\pi$ (la mitad que el seno/coseno).
- Cómo dibujar la gráfica identificando sus puntos clave y muros.
- Cómo leer el comportamiento de "explosión" hacia infinito.

---

## 🚀 La Rebelde Infinita

La tangente se define como:
$$
\tan(x) = \frac{\sin(x)}{\cos(x)}
$$

Aquí está el problema: **no se puede dividir por cero**.
Cada vez que el coseno vale cero (en $90°$, $270°$, etc.), la tangente se rompe. En esos puntos aparecen **asíntotas verticales**: líneas que la gráfica se acerca pero nunca toca.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = tan(x)</strong>
  </div>

![Gráfica de la función tangente](/images/funciones/trigonometria/tangente-principal.svg)

</div>

**Propiedades Clave:**
1.  **Dominio:** Todos los reales excepto $90° + k\cdot180°$.
2.  **Rango:** $(-\infty, \infty)$ ¡Cubre todos los números verticales!
3.  **Periodo:** $\pi$ (o $180°$). Se repite el doble de rápido.
4.  **Asíntotas:** En $x = \pm \pi/2, \pm 3\pi/2, \dots$

---

## 📍 Anatomía de un Ciclo ($-\pi/2$ a $\pi/2$)

La forma básica de la tangente es una curva S alargada que pasa por el origen.

| Punto | Ángulo $x$ | Valor $y$ | Descripción |
| :--- | :--- | :--- | :--- |
| **Asíntota** | $-\pi/2$ ($-90°$) | $-\infty$ | Viene del abismo. |
| **Punto Clave** | $-\pi/4$ ($-45°$) | $-1$ | Referencia útil. |
| **Centro** | $0$ | $0$ | Cruza el origen. |
| **Punto Clave** | $\pi/4$ ($45°$) | $1$ | Referencia útil. |
| **Asíntota** | $\pi/2$ ($90°$) | $\infty$ | Se dispara al cielo. |

> **Patrón:** Muro $\rightarrow$ Sube $\rightarrow$ Cruza $\rightarrow$ Sube $\rightarrow$ Muro.

---

## 🔄 El Periodo Corto

Mientras que el seno necesita $360°$ para completar su ciclo, a la tangente le basta con **$180°$**.
¿Por qué? Porque en el tercer cuadrante, seno y coseno son ambos negativos, y $(-)/(-) = (+)$. Así que la tangente vuelve a ser positiva y repite lo mismo que en el primer cuadrante.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Período de la tangente: π</strong>
  </div>

![Período de la tangente](/images/funciones/trigonometria/tangente-periodo.svg)

</div>

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
¿Cuál es el valor de $\tan(\pi/2)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan(\pi/2) = \sin(\pi/2) / \cos(\pi/2) = 1 / 0$.
División por cero.

**Respuesta:** **Indefinido (Asíntota)**
</details>

---

### Ejercicio 2
¿En qué puntos cruza la tangente el eje X?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan(x) = 0$ cuando $\sin(x) = 0$.
Esto ocurre en los múltiplos enteros de $\pi$.

**Respuesta:** $0, \pi, 2\pi, -\pi, \dots$ ($k\pi$)
</details>

---

### Ejercicio 3
¿Cuál es el rango de la función tangente?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La gráfica va desde lo más bajo ($-\infty$) hasta lo más alto ($\infty$) sin saltarse ningún valor en Y.

**Respuesta:** **Todos los números reales**
</details>

---

### Ejercicio 4
Calcula $\tan(45°)$ y $\tan(-45°)$ usando la gráfica.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
A 45° ($\pi/4$), el seno iguala al coseno, así que la división es 1.
La función es impar, así que en -45° vale -1.

**Respuesta:** $\boxed{1 \text{ y } -1}$
</details>

---

### Ejercicio 5
¿Es la función tangente creciente o decreciente?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si te mueves de izquierda a derecha, la curva **siempre sube**.

**Respuesta:** **Siempre Creciente** (en su dominio)
</details>

---

### Ejercicio 6
Encuentra la primera asíntota vertical positiva.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ocurre cuando $\cos(x) = 0$.
El primer valor positivo es 90°.

**Respuesta:** $\boxed{x = \frac{\pi}{2}}$
</details>

---

### Ejercicio 7
Si $\tan(x) = 1000$, ¿es posible encontrar un valor para $x$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sí, porque el rango es infinito. La tangente "barre" todos los valores posibles.

**Respuesta:** **Sí**
</details>

---

### Ejercicio 8
Determina el período de la función $y = \tan(2x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El periodo normal es $\pi$.
Al multiplicar $x$ por 2, la función se acelera el doble.
Periodo = $\pi / 2$.

**Respuesta:** $\boxed{\frac{\pi}{2}}$
</details>

---

### Ejercicio 9
¿Qué sucede con la gráfica cuando $x$ se acerca a $\pi/2$ por la izquierda?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La curva sube violentamente hacia el cielo.

**Respuesta:** **Tiende a infinito positivo** ($+\infty$)
</details>

---

### Ejercicio 10
Compara el valor de $\tan(0.1)$ con $0.1$ (para ángulos pequeños).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cerca del origen, la tangente se parece mucho a la recta $y=x$.
Son casi iguales.

**Respuesta:** **Aproximadamente iguales**
</details>

---

## 🔑 Resumen

| Función | Dominio | Rango | Periodo |
| :---: | :---: | :---: | :---: |
| **Seno** | Todo $\mathbb{R}$ | $[-1, 1]$ | $2\pi$ |
| **Coseno** | Todo $\mathbb{R}$ | $[-1, 1]$ | $2\pi$ |
| **Tangente** | Huecos en $\pi/2$ | Todo $\mathbb{R}$ | $\pi$ |

> **Conclusión:** La tangente es la función del "todo o nada". Pasa por el cero pero también alcanza el infinito. Recuerda sus muros (asíntotas) y nunca intentarás cruzar donde no existe camino.
