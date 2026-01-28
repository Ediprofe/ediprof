---
title: "Punto Medio de un Segmento"
---

# **Punto Medio de un Segmento**

Imagina que dos amigos viven en ciudades distintas y quieren encontrarse exactamente a la mitad del camino para almorzar. ¿Cómo calculas esas coordenadas? No necesitas fórmulas complejas; solo necesitas saber sacar un **promedio**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es geométricamente el punto medio.
- La fórmula del punto medio (que es básicamente un promedio).
- Cómo encontrar el punto medio dados dos extremos.
- El problema inverso: Cómo hallar un extremo si te dan el punto medio.

---

## ⚖️ El Concepto de "Promedio"

Si sacaste 10 en un examen y 6 en otro, tu promedio es $\frac{10+6}{2} = 8$. El 8 está justo en medio del 6 y el 10.

El **Punto Medio ($M$)** funciona exactamente igual, pero lo haces dos veces:
1.  Sacas el promedio de las $x$ (coordenadas horizontales).
2.  Sacas el promedio de las $y$ (coordenadas verticales).

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Punto Medio = Promedio</strong>
  </div>
  <img src="/images/geometria/analitica/punto-medio.svg" alt="Punto medio de un segmento" style="width: 100%; height: auto;" />
</div>

---

## 🧬 La Fórmula

Dados dos puntos $A(x_1, y_1)$ y $B(x_2, y_2)$, el punto medio $M$ es:

$$
M = \left( \frac{x_1 + x_2}{2} , \frac{y_1 + y_2}{2} \right)
$$

> **Truco:** Suma las coordenadas y divide entre 2. ¡Así de fácil!

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Calcular el Punto Medio
Encuentra el punto medio entre $A(2, 4)$ y $B(6, 10)$.

**Paso 1: Promedio de las X**
$$ x_m = \frac{2 + 6}{2} = \frac{8}{2} = 4 $$

**Paso 2: Promedio de las Y**
$$ y_m = \frac{4 + 10}{2} = \frac{14}{2} = 7 $$

**Resultado:** El punto medio es $\boxed{M(4, 7)}$.

### Ejemplo 2: El Problema del Extremo Perdido (Inverso)
El punto medio de un segmento es $M(2, 3)$. Uno de los extremos es $A(-1, 1)$. ¿Cuál es el otro extremo $B(x_2, y_2)$?

**Paso 1: Plantear la ecuación para X**
$$ 2 = \frac{-1 + x_2}{2} $$
Multiplicamos por 2:
$$ 4 = -1 + x_2 $$
$$ x_2 = 5 $$

**Paso 2: Plantear la ecuación para Y**
$$ 3 = \frac{1 + y_2}{2} $$
Multiplicamos por 2:
$$ 6 = 1 + y_2 $$
$$ y_2 = 5 $$

**Resultado:** El otro extremo es $\boxed{B(5, 5)}$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el punto medio entre $A(0, 0)$ y $B(10, 10)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Promedios: $10/2 = 5$ y $10/2 = 5$.

**Respuesta:** $\boxed{(5, 5)}$
</details>

---

### Ejercicio 2
Calcula el punto medio de $C(4, -2)$ y $D(-4, 2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x: \frac{4-4}{2} = 0$.
$y: \frac{-2+2}{2} = 0$.

**Respuesta:** $\boxed{(0, 0)}$
</details>

---

### Ejercicio 3
Encuentra el punto medio entre $P(3, 5)$ y $Q(7, 9)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x: (3+7)/2 = 5$.
$y: (5+9)/2 = 7$.

**Respuesta:** $\boxed{(5, 7)}$
</details>

---

### Ejercicio 4
Si el punto medio es $(3, 3)$ y un extremo es $(0, 0)$, halla el otro extremo.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Doble del medio menos el extremo conocido.
$x: 2(3) - 0 = 6$.
$y: 2(3) - 0 = 6$.

**Respuesta:** $\boxed{(6, 6)}$
</details>

---

### Ejercicio 5
Calcula el punto medio de una vara que va de $(-5, 0)$ a $(5, 0)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x: (-5+5)/2 = 0$.
$y: (0+0)/2 = 0$.
Es el origen.

**Respuesta:** $\boxed{(0, 0)}$
</details>

---

### Ejercicio 6
Encuentra el centro de un círculo cuyo diámetro va de $A(1, 2)$ a $B(5, 6)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El centro es el punto medio del diámetro.
$x: (1+5)/2 = 3$.
$y: (2+6)/2 = 4$.

**Respuesta:** $\boxed{(3, 4)}$
</details>

---

### Ejercicio 7
Si tus notas son 2 y 10, ¿cuál es tu nota promedio (punto medio)?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(2+10)/2 = 6$.

**Respuesta:** $\boxed{6}$
</details>

---

### Ejercicio 8
El extremo $A$ está en $(4, 8)$. El punto medio es $(4, 8)$. ¿Dónde está $B$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si el medio es igual al extremo, el segmento tiene longitud 0. $A=B=M$.

**Respuesta:** $\boxed{(4, 8)}$
</details>

---

### Ejercicio 9
Halla el punto medio de $(1.5, 2.5)$ y $(3.5, 4.5)$. (Con decimales).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x: (1.5+3.5)/2 = 5/2 = 2.5$.
$y: (2.5+4.5)/2 = 7/2 = 3.5$.

**Respuesta:** $\boxed{(2.5, 3.5)}$
</details>

---

### Ejercicio 10
Demuestra que el punto medio divide al segmento en razón 1:1.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La distancia de un extremo al centro es igual a la distancia del centro al otro extremo. Por eso la razón es 1.

**Respuesta:** **Es por definición**
</details>

---

## 🔑 Resumen

| ¿Qué buscas? | Fórmula Mental |
| :--- | :--- |
| **Punto Medio** | Promedio de $x$, Promedio de $y$. |
| **Extremo Faltante** | Doble del medio M, menos el extremo conocido. |

> **Conclusión:** El punto medio es el concepto más democrático de la geometría: trata a ambos extremos por igual. Es fundamental para encontrar centros de círculos, rectángulos y para equilibrar balanzas.
