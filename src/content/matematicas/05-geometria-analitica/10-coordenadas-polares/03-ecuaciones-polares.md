# **Ecuaciones Polares**

En cartesianas, $y = f(x)$. En el mundo polar, $r = f(\theta)$. Es decir, la distancia al centro depende de hacia dónde estés mirando. Esto permite dibujar flores, espirales y corazones con ecuaciones sorprendentemente simples.

---

## 🎯 ¿Qué vas a aprender?

- Cómo leer una ecuación polar.
- Convertir ecuaciones enteras de $x,y$ a $r,\theta$.
- Círculos, Rectas y las bellas Rosas Polares.

---

## 🌹 Concepto 1: Ecuaciones Básicas y Conversión

Usamos las mismas llaves de traducción: $x = r \cos \theta$, $y = r \sin \theta$ y $x^2 + y^2 = r^2$.

**5 Ejemplos de Conversión (Cartesiana $\leftrightarrow$ Polar):**

### Ejemplo 1.1: Círculo Centrado
Cartesiana: $x^2 + y^2 = 25$.
Conversión:
$$ r^2 = 25 \Rightarrow r = 5 $$
*(Significado: "La distancia al centro es siempre 5, sin importar el ángulo").*

### Ejemplo 1.2: Recta por el Origen
Cartesiana: $y = x$.
Conversión: $r \sin \theta = r \cos \theta$.
Dividiendo por $r \cos \theta$: $\tan \theta = 1$.
$$ \theta = 45^\circ $$
*(Significado: "Mantén el ángulo de 45 grados y camina lo que quieras").*

### Ejemplo 1.3: Círculo Desplazado
Cartesiana: $x^2 + y^2 = 4x$.
Conversión: $r^2 = 4(r \cos \theta)$.
Dividiendo por $r$:
$$ r = 4 \cos \theta $$

### Ejemplo 1.4: Recta Vertical
Cartesiana: $x = 3$.
Conversión: $r \cos \theta = 3$.
$$ r = 3 \sec \theta $$

### Ejemplo 1.5: Hipérbola
Cartesiana: $x^2 - y^2 = 1$.
Conversión: $r^2 \cos^2 \theta - r^2 \sin^2 \theta = 1$.
$r^2 (\cos^2 \theta - \sin^2 \theta) = 1$.
$$ r^2 \cos(2\theta) = 1 $$

---

## 🎨 Concepto 2: La Galería Polar

Algunas curvas son nativas de este sistema y tienen nombres poéticos.

**5 Curvas Famosas:**

### 1. El Círculo ($r = a$)
La más simple. $r = 2$. Un anillo perfecto.

### 2. La Recta ($r \cos \theta = a$)
Líneas que no pasan por el origen.
*   $r \cos \theta = 2$ (Vertical $x=2$).
*   $r \sin \theta = 3$ (Horizontal $y=3$).

### 3. El Caracol y Cardioide ($r = a \pm b \cos \theta$)
Formas de corazón o frijol.
*   Si $a=b$ (ej. $r = 2 + 2\cos\theta$), es un **Cardioide** (Corazón).
*   Si $a < b$, tiene un lazo interior.

### 4. La Rosa ($r = a \cos(n\theta)$)
*   Si $n$ es par, tiene $2n$ pétalos (ej. $\cos(2\theta) \to 4$ pétalos).
*   Si $n$ es impar, tiene $n$ pétalos (ej. $\cos(3\theta) \to 3$ pétalos).

### 5. La Espiral de Arquímedes ($r = a\theta$)
El radio crece a medida que giras. Como un rollo de cinta o un mosquito volando hacia afuera.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Pasa a polar $y = 5$.

<details>
<summary>Ver solución</summary>
$r \sin \theta = 5 \Rightarrow r = 5 \csc \theta$.
</details>

---

### Ejercicio 2
Identifica la curva $r = 4$.

<details>
<summary>Ver solución</summary>
Circunferencia radio 4 centro origen.
</details>

---

### Ejercicio 3
Nro. de pétalos de $r = \sin(5\theta)$.

<details>
<summary>Ver solución</summary>
Impar $\to$ 5 pétalos.
</details>

---

### Ejercicio 4
Nro. de pétalos de $r = \cos(4\theta)$.

<details>
<summary>Ver solución</summary>
Par $\to$ 8 pétalos.
</details>

---

### Ejercicio 5
Pasa a cartesiana $r \cos \theta = -2$.

<details>
<summary>Ver solución</summary>
$x = -2$ (Recta vertical).
</details>

---

### Ejercicio 6
Identifica $r = \theta$.

<details>
<summary>Ver solución</summary>
Espiral.
</details>

---

### Ejercicio 7
Convierte $r = 2 \sin \theta$.

<details>
<summary>Ver solución</summary>
Multiplica por $r$: $r^2 = 2 r \sin \theta \Rightarrow x^2 + y^2 = 2y$. (Círculo desplazado).
</details>

---

### Ejercicio 8
¿El cardioide pasa por el origen?

<details>
<summary>Ver solución</summary>
Sí. Cuando $\cos \theta = -1$, $r = a(1-1) = 0$.
</details>

---

### Ejercicio 9
Ecuación de recta a $45^\circ$.

<details>
<summary>Ver solución</summary>
$\theta = \pi/4$.
</details>

---

### Ejercicio 10
Valor máximo de $r$ en $r = 2 + 2\cos\theta$.

<details>
<summary>Ver solución</summary>
Cuando $\cos=1$, $r = 4$.
</details>

---

## 🔑 Resumen

| Ecuación | Forma |
| :--- | :--- |
| **$r = c$** | Círculo |
| **$\theta = c$** | Recta (Radio) |
| **$r = a \cos n\theta$** | Rosa |
| **$r = 1 + \cos \theta$** | Corazón (Cardioide) |

> **Conclusión:** Las coordenadas polares hacen que lo circular sea simple y lo lineal sea complejo. Usa el sistema adecuado para el problema adecuado.
