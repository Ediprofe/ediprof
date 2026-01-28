---
title: "Cónicas Degeneradas"
---

# **Cónicas Degeneradas**

A veces, la ecuación cuadrática "falla" en crear una curva suave y bonita. Se rompe en pedazos (rectas) o se encoge hasta desaparecer (punto). Estos son los "cadáveres geométricos" de las cónicas.

---

## 🎯 ¿Qué vas a aprender?

- Qué significa "degenerar" en geometría.
- Los 3 casos principales: Punto, Rectas, Vacío.
- Cómo identificarlas factorizando.

---

## 🥀 Concepto 1: El Punto (Elipse Degenerada)

Ocurre cuando una elipse o círculo reduce su radio a cero. La ecuación suele verse como una suma de cuadrados igualada a cero.

**5 Ejemplos:**

### Ejemplo 1.1
$$ x^2 + y^2 = 0 $$
La única solución real es $x=0$ y $y=0$. Es un punto en el origen.

### Ejemplo 1.2
$$ 4(x-1)^2 + 9(y+2)^2 = 0 $$
Suma de positivos es cero solo si ambos son cero.
Punto: $(1, -2)$.

### Ejemplo 1.3
$$ 2x^2 + 5y^2 + 4x - 10y + 7 = 0 $$
Al completar cuadrados queda: $2(x+1)^2 + 5(y-1)^2 = 0$.
Punto: $(-1, 1)$.

### Ejemplo 1.4
$$ x^2 + 2y^2 = 0 $$
Punto: $(0,0)$.

### Ejemplo 1.5
$$ (x+5)^2 + (y-3)^2 \le 0 $$
Dado que el cuadrado no puede ser menor a cero, solo se admite la igualdad.
Punto: $(-5, 3)$.

---

## ⚔️ Concepto 2: Par de Rectas (Hipérbola Degenerada)

Ocurre cuando una hipérbola "toca" sus asíntotas. La ecuación suele verse como una **resta** de cuadrados igualada a cero (Diferencia de cuadrados factorizable).

**5 Ejemplos:**

### Ejemplo 2.1
$$ x^2 - y^2 = 0 $$
Factorizando: $(x-y)(x+y) = 0$.
Dos rectas: $y=x$ y $y=-x$.

### Ejemplo 2.2
$$ 4x^2 - 9y^2 = 0 $$
Factorizando: $(2x-3y)(2x+3y) = 0$.
Rectas: $y = \frac{2}{3}x$ y $y = -\frac{2}{3}x$.

### Ejemplo 2.3
$$ x^2 - 1 = 0 $$
$(x-1)(x+1) = 0$.
Dos rectas verticales paralelas: $x=1$ y $x=-1$. (Parábola degenerada en cilindro).

### Ejemplo 2.4
$$ xy = 0 $$
Significa $x=0$ O $y=0$.
Son los ejes coordenados (la cruz).

### Ejemplo 2.5
$$ (x-1)^2 - 4(y+2)^2 = 0 $$
Rectas que se cruzan en $(1, -2)$ con pendientes $\pm 1/2$.

---

## 🚫 Concepto 3: Conjunto Vacío (Caso Imaginario)

Ocurre cuando la ecuación exige algo imposible en los números reales, como que una suma de cuadrados sea negativa.

**5 Ejemplos:**

### Ejemplo 3.1
$$ x^2 + y^2 = -1 $$
Imposible. No hay gráfica.

### Ejemplo 3.2
$$ x^2 + y^2 + 1 = 0 $$
Equivale a $x^2 + y^2 = -1$. Vacío.

### Ejemplo 3.3
$$ 2x^2 + 3y^2 = -10 $$
Vacío.

### Ejemplo 3.4
$$ (x+2)^2 + y^2 = -0.1 $$
Por pequeño que sea el negativo, es imposible.

### Ejemplo 3.5
$$ x^2 + 4 = 0 $$
$x^2 = -4$. Vacío en los reales (rectas imaginarias).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Clasifica $x^2 + y^2 = 0$.

<details>
<summary>Ver solución</summary>
Punto (Circulo radio 0).
</details>

---

### Ejercicio 2
Clasifica $x^2 - 4 = 0$.

<details>
<summary>Ver solución</summary>
Dos rectas paralelas verticales ($x=2, x=-2$).
</details>

---

### Ejercicio 3
Clasifica $x^2 + y^2 + 4 = 0$.

<details>
<summary>Ver solución</summary>
$x^2+y^2=-4$. Vacío (Imaginaria).
</details>

---

### Ejercicio 4
Factoriza $y^2 - x^2 = 0$.

<details>
<summary>Ver solución</summary>
$(y-x)(y+x)=0$. Rectas $y=x, y=-x$.
</details>

---

### Ejercicio 5
¿Qué es geométricamente $(x-1)(y-2) = 0$?

<details>
<summary>Ver solución</summary>
Dos rectas perpendiculares: $x=1$ y $y=2$.
</details>

---

### Ejercicio 6
Degeneración de $y = x^2$ si colapsa.

<details>
<summary>Ver solución</summary>
$x^2=0$. Recta doble (Eje Y, $x=0$).
</details>

---

### Ejercicio 7
Discriminante de $x^2 - y^2 = 0$.

<details>
<summary>Ver solución</summary>
$\Delta = 0 - 4(1)(-1) = 4 > 0$. Hipérbola (degenerada).
</details>

---

### Ejercicio 8
¿Un punto tiene área?

<details>
<summary>Ver solución</summary>
No.
</details>

---

### Ejercicio 9
Identifica $3x^2 + 3y^2 = -3$.

<details>
<summary>Ver solución</summary>
Vacío.
</details>

---

### Ejercicio 10
Identifica $x^2 = 0$.

<details>
<summary>Ver solución</summary>
Recta "doble" $x=0$ (dos rectas coincidentes).
</details>

---

## 🔑 Resumen

| Ecuación Tipo | Forma | Figura |
| :--- | :--- | :--- |
| **Suma $= 0$** | $A^2 + B^2 = 0$ | Punto |
| **Suma $< 0$** | $A^2 + B^2 = -K$ | Nada (Vacío) |
| **Resta $= 0$** | $A^2 - B^2 = 0$ | Rectas cruzadas (X) |
| **Cuadrado $= 0$**| $A^2 = 0$ | Recta doble (I) |

> **Conclusión:** Si el lado derecho es CERO, sospecha inmediatamente de una degeneración. La cónica ha perdido su "volumen".
