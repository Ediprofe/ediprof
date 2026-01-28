---
title: "Tangente a la Cónica General"
---

# **Tangente a la Cónica General**

Hay una fórmula maestra, un "anillo único", que permite hallar la tangente de *cualquier* cónica (círculo, elipse, parábola, hipérbola) en un punto dado sin tener que averiguar primero qué tipo de curva es. Se llama **Método del Desdoblamiento**.

---

## 🎯 ¿Qué vas a aprender?

- La regla de sustitución mágica ($x^2 \to x_1x$, etc.).
- Cómo aplicar la fórmula general.
- Ejemplos prácticos en todas las cónicas.

---

## 🎩 Concepto 1: La Regla del Desdoblamiento

Si tienes la ecuación general y un punto de contacto $P(x_1, y_1)$, reemplaza los términos así:

| Término Original | Sustitución en la Tangente |
| :--- | :--- |
| **$x^2$** | $x_1 x$ |
| **$y^2$** | $y_1 y$ |
| **$x$** (lineal) | $\frac{x + x_1}{2}$ |
| **$y$** (lineal) | $\frac{y + y_1}{2}$ |
| **$xy$** (producto) | $\frac{x_1 y + y_1 x}{2}$ |
| **Constante $F$** | Se queda igual ($F$) |

---

## ⚙️ Concepto 2: Aplicación en Casos Reales

Veamos **5 ejemplos** aplicando la fórmula directamente:

### Ejemplo 2.1: Circunferencia
Ecuación: $x^2 + y^2 = 25$.
Punto: $(3, 4)$.
1.  Sustituimos $x^2 \to 3x$ y $y^2 \to 4y$.
2.  Ecuación Tangente:
    $$ 3x + 4y = 25 $$

### Ejemplo 2.2: Parábola
Ecuación: $y^2 = 8x$.
Punto: $(2, 4)$.
1.  Sustituimos $y^2 \to 4y$ y $x \to \frac{x+2}{2}$.
2.  $4y = 8(\frac{x+2}{2})$.
3.  $4y = 4(x+2) \Rightarrow y = x+2$.

### Ejemplo 2.3: Elipse
Ecuación: $x^2 + 4y^2 = 8$.
Punto: $(2, 1)$.
1.  Sustituimos $x^2 \to 2x$ y $y^2 \to 1y$.
2.  $2x + 4(1y) = 8$.
3.  $2x + 4y = 8 \Rightarrow x + 2y = 4$.

### Ejemplo 2.4: Hipérbola General
Ecuación: $x^2 - y^2 - 4x + 6y - 9 = 0$.
Punto: $(4, 1)$. (Verificamos: $16 - 1 - 16 + 6 - 9 = 22-26 \neq 0$... ¡Ojo! El punto debe pertenecer. Usemos otro punto real).
Usemos Punto $(5, 2)$:
$25 - 4 - 20 + 12 - 9 = 37-33 \neq 0$.
Usemos Punto $(6, 3)$:
$36 - 9 - 24 + 18 - 9 = 12 \neq 0$.
*(Nota: Inventar puntos es difícil. Usemos un ejemplo teórico).*
Ecuación: $x^2 - y^2 = 16$. Punto $(5, 3)$.
1.  $5x - 3y = 16$.

### Ejemplo 2.5: Con Término XY (Avanzado)
Ecuación: $xy = 4$.
Punto: $(2, 2)$.
1.  Sustituimos $xy \to \frac{2y + 2x}{2} = x + y$.
2.  Ecuación Tangente:
    $$ x + y = 4 $$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Tangente a $x^2 + y^2 = 100$ en $(6, -8)$.

<details>
<summary>Ver solución</summary>
$6x - 8y = 100 \Rightarrow 3x - 4y = 50$.
</details>

---

### Ejercicio 2
Tangente a $y^2 - 4x = 0$ en $(1, 2)$.

<details>
<summary>Ver solución</summary>
$2y - 4(\frac{x+1}{2}) = 0 \Rightarrow 2y - 2(x+1) = 0 \Rightarrow y = x+1$.
</details>

---

### Ejercicio 3
Sustitución para el término $4x$.

<details>
<summary>Ver solución</summary>
$4(\frac{x+x_1}{2}) = 2(x+x_1)$.
</details>

---

### Ejercicio 4
Si el punto NO pertenece a la curva, ¿qué hallas?

<details>
<summary>Ver solución</summary>
La Recta Polar (no la tangente).
</details>

---

### Ejercicio 5
Tangente a $2x^2 + 3y^2 = 5$ en $(1, 1)$.

<details>
<summary>Ver solución</summary>
$2(1)x + 3(1)y = 5 \Rightarrow 2x + 3y = 5$.
</details>

---

### Ejercicio 6
Tangente de $x^2 = y$ en eje origen $(0,0)$.

<details>
<summary>Ver solución</summary>
$0x = \frac{y+0}{2} \Rightarrow 0 = y/2 \Rightarrow y = 0$. (Eje X).
</details>

---

### Ejercicio 7
Tangente a circunferencia con centro $(0,0)$ en cualquier punto $(x_1, y_1)$.

<details>
<summary>Ver solución</summary>
$x_1x + y_1y = r^2$.
</details>

---

### Ejercicio 8
¿Funciona para rectas (cónicas degeneradas)?

<details>
<summary>Ver solución</summary>
Sí, te devuelve la misma recta.
</details>

---

### Ejercicio 9
Sustitución para constante 10.

<details>
<summary>Ver solución</summary>
Sigue siendo 10.
</details>

---

### Ejercicio 10
Tangente a $x^2 + y^2 - 2x = 0$ en $(2, 0)$.

<details>
<summary>Ver solución</summary>
$2x + 0y - 2(\frac{x+2}{2}) = 0 \Rightarrow 2x - (x+2) = 0 \Rightarrow x = 2$. (Recta vertical).
</details>

---

## 🔑 Resumen

| Término | Transformación |
| :--- | :--- |
| **Cuadrático** | Producto $x_1 x$ |
| **Lineal** | Promedio $\frac{x+x_1}{2}$ |
| **Producto** | Promedio Cruzado $\frac{x_1y + y_1x}{2}$ |

> **Conclusión:** No memorices fórmulas distintas para cada curva. La regla del desdoblamiento funciona universalmente si conoces el punto de tangencia.
