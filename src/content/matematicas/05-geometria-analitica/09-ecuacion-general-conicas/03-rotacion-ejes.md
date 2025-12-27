# **Rotación de Ejes**

A veces la cónica es rebelde y no se alinea con el piso (eje X) ni con la pared (eje Y). Está inclinada. Para "enderezarla" y poder usar nuestras fórmulas simples, necesitamos rotar los ejes coordenados un ángulo $\theta$.

---

## 🎯 ¿Qué vas a aprender?

- Por qué el término $Bxy$ indica rotación.
- Cómo calcular el ángulo $\theta$ exacto para eliminar ese término.
- Las ecuaciones de transformación para rotar coordenadas.

---

## 📐 Concepto 1: El Ángulo Mágico ($\theta$)

Nuestro objetivo es encontrar un nuevo sistema de coordenadas $(X', Y')$ girado un ángulo $\theta$ tal que, en este nuevo sistema, el término $x'y'$ desaparezca ($B' = 0$).

La fórmula para encontrar el ángulo doble ($2\theta$) es:

$$ \tan(2\theta) = \frac{B}{A - C} $$

*   *Si $A = C$ (división por cero), el ángulo es automáticamente $45^\circ$ ($\pi/4$).*

Veamos **5 ejemplos de cálculo de ángulos**:

### Ejemplo 1.1: Hipérbola Equilátera
Ecuación: $xy = 1$ ($x^2, y^2$ no están, $B=1$).
*   $A=0, C=0, B=1$.
*   $A-C = 0$.
*   $\tan(2\theta) = 1/0 \to \infty$.
*   $2\theta = 90^\circ \Rightarrow \theta = 45^\circ$.

### Ejemplo 1.2: Elipse Inclinada
Ecuación: $7x^2 - 6\sqrt{3}xy + 13y^2 = 16$.
*   $A=7, B=-6\sqrt{3}, C=13$.
*   $A-C = 7 - 13 = -6$.
*   $\tan(2\theta) = \frac{-6\sqrt{3}}{-6} = \sqrt{3}$.
*   $2\theta = 60^\circ \Rightarrow \theta = 30^\circ$.

### Ejemplo 1.3: Parábola Rotada
Ecuación: $x^2 + 2xy + y^2 + \dots = 0$.
*   $A=1, B=2, C=1$.
*   $A-C = 0$.
*   División por cero $\Rightarrow \theta = 45^\circ$.

### Ejemplo 1.4: Valores Negativos
Ecuación: $x^2 - 4xy + 4y^2 = 0$.
*   $A=1, B=-4, C=4$.
*   $A-C = -3$.
*   $\tan(2\theta) = \frac{-4}{-3} = \frac{4}{3}$.
*   $2\theta \approx 53.13^\circ \Rightarrow \theta \approx 26.5^\circ$.

### Ejemplo 1.5: Ejes Ya Alineados
Ecuación: $3x^2 + 5y^2 = 15$.
*   $B=0$.
*   $\tan(2\theta) = 0 / (3-5) = 0$.
*   $2\theta = 0^\circ \Rightarrow \theta = 0^\circ$. (No se necesita rotación).

---

## 🔄 Concepto 2: Ecuaciones de Transformación

Una vez tienes $\theta$, transformas de viejo $(x, y)$ a nuevo $(x', y')$ con:

$$ x = x' \cos\theta - y' \sin\theta $$
$$ y = x' \sin\theta + y' \cos\theta $$

Analicemos **5 aplicaciones conceptuales**:

### Ejemplo 2.1: Rotación de 90 grados
Si $\theta = 90^\circ$:
*   $x = x'(0) - y'(1) = -y'$.
*   $y = x'(1) + y'(0) = x'$.
*   Intercambiamos ejes (lo que era X ahora es Y).

### Ejemplo 2.2: Rotación de 45 grados ($\sqrt{2}/2$)
Si $\theta = 45^\circ$:
*   $x = \frac{\sqrt{2}}{2}(x' - y')$.
*   $y = \frac{\sqrt{2}}{2}(x' + y')$.
    (Muy común para rotar $xy=1$).

### Ejemplo 2.3: La identidad
Si $\theta = 0^\circ$:
*   $x = x'(1) - y'(0) = x'$.
*   $y = x'(0) + y'(1) = y'$.
    (No cambia nada).

### Ejemplo 2.4: El punto $(1,0)$ rotado 30°
¿Dónde queda el punto $(1,0)$ si rotamos los ejes 30°?
*   $x' = x \cos(30) + y \sin(30)$ (Fórmula inversa).
*   En el nuevo sistema, el punto "viejo" cambia de "dirección" relativa.

### Ejemplo 2.5: Eliminación de $xy$
Al sustituir estas ecuaciones en $Ax^2 + Bxy + Cy^2...$ y simplificar, el nuevo coeficiente $B'$ será:
$$ B' = B \cos(2\theta) - (A-C)\sin(2\theta) $$
Si elegimos bien $\theta$ (con la fórmula de arriba), este $B'$ se vuelve CERO.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Ángulo de rotación si $A=C$.

<details>
<summary>Ver solución</summary>
$45^\circ$
</details>

---

### Ejercicio 2
Calcula $\tan(2\theta)$ si $A=2, B=4, C=6$.

<details>
<summary>Ver solución</summary>
$\tan(2\theta) = 4 / (2-6) = 4/-4 = -1$.
$2\theta = 135^\circ \to \theta = 67.5^\circ$.

**Respuesta:** $\boxed{-1}$
</details>

---

### Ejercicio 3
Nuevas coordenadas del origen $(0,0)$ tras rotar.

<details>
<summary>Ver solución</summary>

**Respuesta:** **(0,0) (El origen no se mueve)**
</details>

---

### Ejercicio 4
Ecuación transformada de $xy=2$ con $\theta=45$.

<details>
<summary>Ver solución</summary>
$(x'^2/2) - (y'^2/2) = 2 \Rightarrow x'^2 - y'^2 = 4$.

**Respuesta:** $\boxed{x'^2 - y'^2 = 4}$
</details>

---

### Ejercicio 5
Si $B=0$, ¿cuánto vale $\theta$?

<details>
<summary>Ver solución</summary>

**Respuesta:** **0 grados**
</details>

---

### Ejercicio 6
Valor de sen(45) y cos(45).

<details>
<summary>Ver solución</summary>

**Respuesta:** $\boxed{\frac{\sqrt{2}}{2}}$
</details>

---

### Ejercicio 7
¿Qué curva es $x^2 + xy + y^2 = 3$? (Elipse/Hipérbola).

<details>
<summary>Ver solución</summary>
$\Delta = 1 - 4(1)(1) = -3$. Elipse.

**Respuesta:** **Elipse**
</details>

---

### Ejercicio 8
Fórmula para $x$ en función de $x', y'$.

<details>
<summary>Ver solución</summary>

**Respuesta:** $\boxed{x' \cos\theta - y' \sin\theta}$
</details>

---

### Ejercicio 9
Si rotamos $x^2 + y^2 = r^2$ cualquier ángulo.

<details>
<summary>Ver solución</summary>
Sigue siendo $x'^2 + y'^2 = r^2$. El círculo es invariante.

**Respuesta:** **La misma ecuación**
</details>

---

### Ejercicio 10
Ángulo para $11x^2 + 24xy + 4y^2 = \dots$

<details>
<summary>Ver solución</summary>
$A-C = 7$. $B=24$. $\tan(2\theta) = 24/7$.
$\theta \approx 36.8^\circ$.

**Respuesta:** $\boxed{\approx 36.8^\circ}$
</details>

---

## 🔑 Resumen

| Paso | Fórmula | Meta |
| :--- | :--- | :--- |
| **1. Hallar Ángulo** | $\tan(2\theta) = \frac{B}{A-C}$ | Eliminar $xy$. |
| **2. Rotar** | $x = x'\cos\theta - y'\sin\theta$ | Reescribir todo. |

> **Conclusión:** La rotación es como girar la cabeza para ver bien un cuadro colgado chueco. La imagen (la cónica) es la misma, solo cambiamos nuestra perspectiva (los ejes).
