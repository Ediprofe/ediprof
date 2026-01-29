# **Definición de la Circunferencia**

Todos sabemos qué es un círculo ("una redonda"), pero en matemáticas necesitamos ser más precisos. ¿Cómo le explicas a una computadora qué es un círculo sin dibujarlo? Usando una "regla sagrada" sobre la distancia.

---

## 🎯 ¿Qué vas a aprender?

- La diferencia entre Círculo (relleno) y Circunferencia (borde).
- La definición oficial: "Equidistancia a un centro".
- Cómo traducir esa definición a la fórmula matemática $\sqrt{(x-h)^2 + (y-k)^2} = r$.
- Los elementos clave: Radio, Diámetro, Cuerda y Arco.

---

## ⭕ El Club Exclusivo

Una circunferencia es un club muy estricto.
*   **El Portero (Centro):** El punto fijo $C(h, k)$.
*   **La Regla de Entrada (Radio):** "Solo entras si estás exactamente a $r$ metros de mí".
*   **Los Miembros:** El conjunto de puntos $P(x, y)$ que cumplen la regla.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Elementos de la Circunferencia</strong>
  </div>
  <img src="/images/geometria/analitica/elementos-circunferencia.svg" alt="Elementos de la circunferencia" style="width: 100%; height: auto;" />
</div>

> **Ojo:** La circunferencia es la línea (el anillo). El círculo es la línea MÁS lo de adentro (la moneda).

---

## 📐 De la Definición a la Ecuación

Si la distancia entre $P(x,y)$ y el Centro $C(h,k)$ debe ser $r$:
$$ d(P, C) = r $$

Usando la fórmula de distancia entre dos puntos:
$$ \sqrt{(x - h)^2 + (y - k)^2} = r $$

Para quitar la raíz fea, elevamos al cuadrado:
$$ (x - h)^2 + (y - k)^2 = r^2 $$

¡Y esa es la ecuación de la circunferencia!

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Escribir la Ecuación
Centro en $(2, 3)$ y radio 5.
$$ (x - 2)^2 + (y - 3)^2 = 5^2 $$
$$ (x - 2)^2 + (y - 3)^2 = 25 $$

### Ejemplo 2: Centro en el Origen
Centro $(0, 0)$ y radio 4.
$$ (x - 0)^2 + (y - 0)^2 = 4^2 $$
$$ x^2 + y^2 = 16 $$

### Ejemplo 3: Identificar Elementos
Dada $(x + 1)^2 + (y - 4)^2 = 9$.
*   El centro es $(-1, 4)$. (Cambia los signos de lo que ves).
*   El radio es $\sqrt{9} = 3$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Ecuación con centro $(0,0)$ y radio 1.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2 + y^2 = 1^1$.

**Respuesta:** $\boxed{x^2 + y^2 = 1}$
</details>

---

### Ejercicio 2
Radio de $x^2 + y^2 = 100$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$r^2 = 100 \Rightarrow r = 10$.

**Respuesta:** $\boxed{10}$
</details>

---

### Ejercicio 3
Centro de $(x-5)^2 + (y+2)^2 = 4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cambia signos: $h=5, k=-2$.

**Respuesta:** $\boxed{(5, -2)}$
</details>

---

### Ejercicio 4
Si el diámetro es 10, ¿cuál es el radio?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$r = D/2 = 5$.

**Respuesta:** $\boxed{5}$
</details>

---

### Ejercicio 5
Distancia máxima entre dos puntos de una circunferencia de radio 3.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es el diámetro. $2 \times 3 = 6$.

**Respuesta:** $\boxed{6}$
</details>

---

### Ejercicio 6
Ecuación si el centro es $(3,0)$ y radio 2.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(x-3)^2 + y^2 = 4$.

**Respuesta:** $\boxed{(x-3)^2 + y^2 = 4}$
</details>

---

### Ejercicio 7
¿El punto $(3,4)$ está en $x^2+y^2=25$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$3^2 + 4^2 = 9 + 16 = 25$. Sí cumple.

**Respuesta:** **Sí**
</details>

---

### Ejercicio 8
¿Cuántos puntos tiene una circunferencia?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es una línea continua cerrada.

**Respuesta:** **Infinitos**
</details>

---

### Ejercicio 9
Diferencia entre $(x-1)^2$ y $x^2-1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(x-1)^2$ es un binomio (circunferencia desplazada). $x^2-1$ es una resta. No confundir.

**Respuesta:** **Son distintos**
</details>

---

### Ejercicio 10
Ecuación de la circunferencia unitaria.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Centro $(0,0)$, radio 1.

**Respuesta:** $\boxed{x^2 + y^2 = 1}$
</details>

---

## 🔑 Resumen

| Elemento | En la Ecuación | Función |
| :--- | :--- | :--- |
| **Centro $(h,k)$** | Aparece restando: $(x-h), (y-k)$. | Ubica el círculo en el mapa. |
| **Radio $r$** | Aparece al cuadrado $r^2$. | Define el tamaño. |
| **Fórmula** | $(x-h)^2 + (y-k)^2 = r^2$ | El ADN de la circunferencia. |

> **Conclusión:** La circunferencia no es más que una aplicación directa del Teorema de Pitágoras. Cada punto forma un triángulo rectángulo con el radio como hipotenusa.
