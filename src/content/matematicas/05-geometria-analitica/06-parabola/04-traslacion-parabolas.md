# **Traslación de Parábolas (Vértice fuera del Origen)**

En el mundo real, las cosas no siempre están centradas en el $(0,0)$. Un puente colgante o un proyectil pueden tener su vértice en cualquier punto $(h, k)$. Aquí aprendemos a mover nuestras ecuaciones usando la técnica del "paréntesis trampa".

---

## 🎯 ¿Qué vas a aprender?

- Cómo transformar $x^2$ en $(x-h)^2$ y $y^2$ en $(y-k)^2$.
- Ecuaciones Ordinarias para vértices desplazados.
- Cómo extraer el Vértice $(h, k)$ sin equivocarte con los signos.

---

## 🚀 La Ecuación Trasladada

Simplemente reemplazamos $x$ por $(x-h)$ y $y$ por $(y-k)$.
*   **Vértice:** $V(h, k)$.

### 1. Vertical (Eje paralelo a Y)
La $X$ sigue siendo la cuadrática.
$$ (x - h)^2 = 4p(y - k) $$

### 2. Horizontal (Eje paralelo a X)
La $Y$ sigue siendo la cuadrática.
$$ (y - k)^2 = 4p(x - h) $$

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Parábola Trasladada</strong>
  </div>
  <img src="/images/geometria/analitica/parabola-trasladada.svg" alt="Parábola trasladada" style="width: 100%; height: auto;" />
</div>

> **¡Alerta de Signo!** Si ves $(x - 5)$, el vértice está en **+5**. Si ves $(y + 3)$, el vértice está en **-3**.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Leyendo la Ecuación Vertical
Dada $(x - 2)^2 = 12(y - 1)$.
1.  **Orientación:** $X$ cuadrada $\to$ Vertical. Positivo $\to$ Arriba.
2.  **Vértice:** $(h, k) = (2, 1)$.
3.  **Parámetro:** $4p = 12 \Rightarrow p = 3$.
4.  **Foco:** Desde el vértice, sube 3 unidades en Y.
    $F = (2, 1+3) = (2, 4)$.

### Ejemplo 2: Leyendo la Ecuación Horizontal
Dada $(y + 2)^2 = -8(x - 4)$.
1.  **Orientación:** $Y$ cuadrada $\to$ Horizontal. Negativo $\to$ Izquierda.
2.  **Vértice:** $(h, k) = (4, -2)$.
3.  **Parámetro:** $4p = -8 \Rightarrow p = -2$.
4.  **Foco:** Desde el vértice, muévete 2 a la izquierda en X.
    $F = (4-2, -2) = (2, -2)$.

### Ejemplo 3: Escribiendo la Ecuación
Parábola horizontal, Vértice en $(-3, 5)$, $p=4$ (derecha).
1.  Forma: $(y - k)^2 = 4p(x - h)$.
2.  Sustituir: $(y - 5)^2 = 16(x - (-3))$.
3.  Resultado: $(y - 5)^2 = 16(x + 3)$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Vértice de $(x-3)^2 = 4(y+5)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cambiar signos: $h=3, k=-5$.

**Respuesta:** $\boxed{(3, -5)}$
</details>

---

### Ejercicio 2
Parámetro $p$ de $(y-1)^2 = -20(x-2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$4p = -20$.

**Respuesta:** $\boxed{-5}$
</details>

---

### Ejercicio 3
Ecuación Vertical, Vértice $(0,0)$ desplazado a $(1,1)$, $p=2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(x-1)^2 = 8(y-1)$.

**Respuesta:** $\boxed{(x-1)^2 = 8(y-1)}$
</details>

---

### Ejercicio 4
Foco de $(x-2)^2 = 8y$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$V(2,0)$, $p=2$ (Arriba). $F(2, 0+2)$.

**Respuesta:** $\boxed{(2, 2)}$
</details>

---

### Ejercicio 5
Directriz de $(y+2)^2 = 12(x-1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Horizontal Derecha. $V(1, -2)$. $p=3$. Directriz a la izquierda: $x = 1-3$.

**Respuesta:** $\boxed{x = -2}$
</details>

---

### Ejercicio 6
Orientación de $(y-3)^2 = -x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Y cuadrada (Horizontal). Negativo (Izquierda).

**Respuesta:** **Horizontal Izquierda**
</details>

---

### Ejercicio 7
Lado Recto de $(x+5)^2 = 10(y-5)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Coeficiente principal.

**Respuesta:** $\boxed{10}$
</details>

---

### Ejercicio 8
Si el vértice es $(-2, -3)$, ¿cómo queda el paréntesis de x?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x - (-2) = x+2$.

**Respuesta:** $\boxed{(x+2)}$
</details>

---

### Ejercicio 9
Eje de simetría de $(y-4)^2 = 8(x+2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es horizontal, eje "y = constante del vértice".

**Respuesta:** $\boxed{y = 4}$
</details>

---

### Ejercicio 10
Distancia focal de $(x-100)^2 = 16(y-200)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Distancia focal es $p$. $4p=16 \Rightarrow p=4$.

**Respuesta:** $\boxed{4}$
</details>

---

## 🔑 Resumen

| Ecuación | Tipo | Desplazamiento |
| :--- | :--- | :--- |
| **$(x-h)^2 = 4p(y-k)$** | Vertical | Foco se mueve en $Y$ |
| **$(y-k)^2 = 4p(x-h)$** | Horizontal | Foco se mueve en $X$ |

> **Conclusión:** No memorices fórmulas nuevas. Es la misma fórmula de siempre, pero el origen $(0,0)$ se "disfraza" como $(h,k)$.
