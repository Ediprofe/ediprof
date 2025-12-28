# **Distancia Entre Dos Puntos**

Si te pregunto qué tan lejos está tu casa de la escuela, seguramente pensarás en el camino que recorres (calles, vueltas). Pero en matemáticas, la **distancia** es siempre el camino más corto: una línea recta. ¿Cómo calculamos esa línea diagonal sin usar una regla? Usamos el viejo confiable: Pitágoras.

---

## 🎯 ¿Qué vas a aprender?

- Cómo calcular la distancia exacta entre dos puntos cualesquiera.
- Por qué esta fórmula es en realidad el Teorema de Pitágoras disfrazado.
- Cómo calcular distancias horizontales y verticales al instante.
- Cómo usar esto para calcular el perímetro de figuras geométricas.

---

## 📐 El Secreto es un Triángulo

Imagina dos puntos en el plano, $A$ y $B$. Si trazas una línea recta entre ellos, esa línea es la hipotenusa de un triángulo rectángulo invisible.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Distancia = Pitágoras</strong>
  </div>
  <img src="/images/geometria/analitica/distancia-puntos.svg" alt="Distancia entre dos puntos usando el Teorema de Pitágoras" style="width: 100%; height: auto;" />
</div>

*   **El cateto horizontal:** Es la diferencia de las $x$ ($x_2 - x_1$).
*   **El cateto vertical:** Es la diferencia de las $y$ ($y_2 - y_1$).

El Teorema de Pitágoras dice $c^2 = a^2 + b^2$. Aquí $c$ es la distancia $d$.

$$
d^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2
$$

Despejando la $d$, obtenemos la fórmula maestra.

---

## 🧬 La Fórmula de la Distancia

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

> **Nota:** No importa si restas $(x_2 - x_1)$ o $(x_1 - x_2)$. Como luego lo elevas al cuadrado, el resultado siempre será **positivo**. ¡La magia de las matemáticas!

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Distancia Estándar
Calcula la distancia entre $A(1, 2)$ y $B(4, 6)$.

**Paso 1: Identificar coordenadas**
$x_1=1, y_1=2$
$x_2=4, y_2=6$

**Paso 2: Calcular diferencias**
Restamos las $x$: $4 - 1 = 3$.
Restamos las $y$: $6 - 2 = 4$.

**Paso 3: Pitágoras**
$3^2 + 4^2 = 9 + 16 = 25$.
$d = \sqrt{25} = 5$.

**Resultado:** $\boxed{5}$ unidades.

### Ejemplo 2: Con Números Negativos
Calcula la distancia entre $P(-3, 2)$ y $Q(5, -4)$.

**Paso 1: Diferencias (¡Cuidado con los signos!)**
$\Delta x = 5 - (-3) = 5 + 3 = 8$.
$\Delta y = -4 - 2 = -6$.

**Paso 2: Cuadrados**
$8^2 = 64$.
$(-6)^2 = 36$ (¡Positivo!).

**Paso 3: Raíz**
$d = \sqrt{64 + 36} = \sqrt{100} = 10$.

**Resultado:** $\boxed{10}$ unidades.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la distancia entre $A(2, 1)$ y $B(5, 5)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\Delta x = 3, \Delta y = 4$.
$d = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$.

**Respuesta:** $\boxed{5}$
</details>

---

### Ejercicio 2
Calcula la distancia entre el origen $(0,0)$ y el punto $(3, 4)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$d = \sqrt{3^2 + 4^2} = 5$.

**Respuesta:** $\boxed{5}$
</details>

---

### Ejercicio 3
Calcula la distancia entre $C(-2, 3)$ y $D(4, 3)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es una línea horizontal (misma $y$).
$d = |4 - (-2)| = |6| = 6$.

**Respuesta:** $\boxed{6}$
</details>

---

### Ejercicio 4
Encuentra la distancia entre $E(1, 7)$ y $F(1, -2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es una línea vertical (misma $x$).
$d = |7 - (-2)| = |9| = 9$.

**Respuesta:** $\boxed{9}$
</details>

---

### Ejercicio 5
Calcula la distancia entre $G(1, 1)$ y $H(4, 5)$ y verifica si es igual a 5.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{(4-1)^2 + (5-1)^2} = \sqrt{3^2 + 4^2} = 5$.

**Respuesta:** **Sí, es 5**
</details>

---

### Ejercicio 6
Calcula el perímetro de un triángulo con vértices $A(0,0), B(3,0), C(0,4)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Lado $AB = 3$. Lado $AC = 4$. Hipotenusa $BC = \sqrt{3^2+4^2}=5$.
Perímetro $= 3+4+5=12$.

**Respuesta:** $\boxed{12}$
</details>

---

### Ejercicio 7
Si la distancia entre $(x, 0)$ y $(0, 8)$ es 10, halla $x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$10^2 = (x-0)^2 + (0-8)^2$.
$100 = x^2 + 64$.
$x^2 = 36 \Rightarrow x = \pm 6$.

**Respuesta:** $\boxed{x = 6 \text{ o } x = -6}$
</details>

---

### Ejercicio 8
Demuestra que los puntos $A(1,2), B(4,2), C(1,6)$ forman un triángulo rectángulo.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Lado $AB$ es horizontal (longitud 3). Lado $AC$ es vertical (longitud 4).
Vertical y horizontal son perpendiculares ($90°$).

**Respuesta:** **Sí, es rectángulo**
</details>

---

### Ejercicio 9
Calcula la distancia entre $(-5, -5)$ y $(5, 5)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\Delta x = 10, \Delta y = 10$.
$d = \sqrt{100+100} = \sqrt{200} = 10\sqrt{2} \approx 14.14$.

**Respuesta:** $\boxed{10\sqrt{2}}$
</details>

---

### Ejercicio 10
Un pájaro vuela en línea recta desde $(2,3)$ hasta $(-1,-1)$. ¿Qué distancia recorrió?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{(-1-2)^2 + (-1-3)^2}$.
$\sqrt{(-3)^2 + (-4)^2} = \sqrt{9+16} = 5$.

**Respuesta:** $\boxed{5}$
</details>

---

## 🔑 Resumen

| Tipo de Distancia | Fórmula Simplificada |
| :--- | :--- |
| **Inclinada** (Normal) | $\sqrt{(\Delta x)^2 + (\Delta y)^2}$ |
| **Horizontal** (Misma $y$) | Simplemente resta las $x$. |
| **Vertical** (Misma $x$) | Simplemente resta las $y$. |

> **Conclusión:** No memorices la fórmula gigante. Solo recuerda que estás calculando la hipotenusa de un triángulo rectángulo. ¡Es Pitágoras en acción!
