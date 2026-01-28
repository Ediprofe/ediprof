---
title: "Traslación de Hipérbolas (Centro fuera del Origen)"
---

# **Traslación de Hipérbolas (Centro fuera del Origen)**

Igual que con la parábola y la elipse, podemos desplazar la hipérbola a cualquier punto $(h, k)$ del plano. La estructura se mantiene, solo añadimos "paréntesis de viaje".

---

## 🎯 ¿Qué vas a aprender?

- Ecuaciones trasladadas: $(x-h)^2$ y $(y-k)^2$.
- Extraer el centro y determinar la orientación.
- Calcular vértices, focos y asíntotas reales.

---

## 🚀 La Ecuación Trasladada

Reemplazamos $x \to (x-h)$ y $y \to (y-k)$.

**1. Horizontal (Eje paralelo a X):**
El término positivo contiene a $X$.
$$ \frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1 $$

**2. Vertical (Eje paralelo a Y):**
El término positivo contiene a $Y$.
$$ \frac{(y-k)^2}{a^2} - \frac{(x-h)^2}{b^2} = 1 $$

*(Nota: $a^2$ siempre está debajo del positivo).*

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Hipérbola Trasladada</strong>
  </div>
  <img src="/images/geometria/analitica/hiperbola-trasladada.svg" alt="Hipérbola con centro fuera del origen" style="width: 100%; height: auto;" />
</div>

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Lectura de Ecuación
$$ \frac{(y-2)^2}{9} - \frac{(x+1)^2}{16} = 1 $$
1.  **Centro:** $(-1, 2)$. (Cuidado con el orden X, Y).
2.  **Orientación:** El positivo es Y $\to$ **Vertical**.
3.  **Parámetros:**
    *   $a^2 = 9 \Rightarrow a = 3$.
    *   $b^2 = 16 \Rightarrow b = 4$.
    *   $c = \sqrt{9+16} = 5$.
4.  **Focos:** Centro $(-1, 2) \pm 5$ en Y.
    $F_1(-1, 7)$ y $F_2(-1, -3)$.

### Ejemplo 2: Escritura
Centro $(3, 1)$, Horizontal, $a=2, b=1$.
1.  Positivo en X.
2.  $a^2=4, b^2=1$.
3.  Ecuación:
    $$ \frac{(x-3)^2}{4} - \frac{(y-1)^2}{1} = 1 $$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Centro de $\frac{(x+5)^2}{10} - \frac{y^2}{5} = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$h=-5, k=0$.

**Respuesta:** $\boxed{(-5, 0)}$
</details>

---

### Ejercicio 2
Orientación de la anterior.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Positivo en X.

**Respuesta:** **Horizontal**
</details>

---

### Ejercicio 3
Ecuación de asíntotas para Ejemplo 1 ($C(-1,2)$, Vertical $a=3, b=4$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$y-2 = \pm (3/4)(x+1)$.

**Respuesta:** $\boxed{y - 2 = \pm \frac{3}{4}(x + 1)}$
</details>

---

### Ejercicio 4
Si el centro es $(2,2)$ y $a=2$ (Horizontal), ¿cuáles son los vértices?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sumar/restar $a$ a la X. $(2\pm 2, 2)$.

**Respuesta:** $\boxed{(4, 2) \text{ y } (0, 2)}$
</details>

---

### Ejercicio 5
Calcula $c$ para $\frac{(x-1)^2}{1} - \frac{(y-1)^2}{3} = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$c = \sqrt{1+3} = 2$.

**Respuesta:** $\boxed{2}$
</details>

---

### Ejercicio 6
Ecuación si Centro $(0,0)$ se mueve a $(h,k)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Reemplazar $x,y$ por $x-h, y-k$.

**Respuesta:** **Ecuación Ordinaria**
</details>

---

### Ejercicio 7
Distancia entre vértices de una hipérbola vertical con $a=5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es $2a = 10$, sin importar el centro.

**Respuesta:** $\boxed{10}$
</details>

---

### Ejercicio 8
¿Afecta la traslación a la excentricidad?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No, la forma es la misma.

**Respuesta:** **No**
</details>

---

### Ejercicio 9
Escribe la ecuación de una hipérbola vertical, centro $(1,1), a=1, b=1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(y-1)^2 - (x-1)^2 = 1$.

**Respuesta:** $\boxed{(y-1)^2 - (x-1)^2 = 1}$
</details>

---

### Ejercicio 10
Coordenas de los focos de la anterior ($c=\sqrt{2}$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Vertical $\to$ mover Y. $(1, 1 \pm \sqrt{2})$.

**Respuesta:** $\boxed{(1, 1+\sqrt{2}) \text{ y } (1, 1-\sqrt{2})}$
</details>

---

## 🔑 Resumen

| Paso | Acción |
| :--- | :--- |
| **1. Centro** | Ubicar $(h, k)$ cambiando signos. |
| **2. Signo** | Identificar cuál término es positivo para saber la orientación. |
| **3. Calcular** | Sumar $a, c$ a la coordenada correcta ($x$ o $y$). |

> **Conclusión:** El paréntesis es tu amigo. Te dice dónde clavar el compás antes de empezar a dibujar.
