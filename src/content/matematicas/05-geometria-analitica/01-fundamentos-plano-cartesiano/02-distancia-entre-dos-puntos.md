# Distancia Entre Dos Puntos

¿Cuánto mide el camino en línea recta entre dos puntos? Esta pregunta parece simple, pero esconde una de las fórmulas más elegantes de la geometría analítica — y está basada en el famoso **Teorema de Pitágoras**.

---

## 🎯 ¿Qué vas a aprender?

- La fórmula de la distancia entre dos puntos
- Cómo deducirla usando el Teorema de Pitágoras
- Aplicaciones prácticas para calcular longitudes

---

## 📖 Lo Esencial de la Distancia

| Fórmula | Descripción |
|---------|-------------|
| $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ | Distancia entre $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$ |
| $d = \|x_2 - x_1\|$ | Distancia horizontal (si $y_1 = y_2$) |
| $d = \|y_2 - y_1\|$ | Distancia vertical (si $x_1 = x_2$) |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/distancia-puntos.svg" alt="Distancia entre dos puntos usando el Teorema de Pitágoras" style="width: 100%; height: auto;" />
</div>

---

## 📖 La Idea Detrás de la Fórmula

Dados dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$, el segmento que los une es la **hipotenusa** de un triángulo rectángulo cuyos catetos son:

- **Cateto horizontal:** La distancia en $x$, es decir $\Delta x = x_2 - x_1$
- **Cateto vertical:** La distancia en $y$, es decir $\Delta y = y_2 - y_1$

Por el **Teorema de Pitágoras**:

$$
d^2 = (\Delta x)^2 + (\Delta y)^2
$$

Despejando:

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

> 💡 **Nota importante:** Como elevamos al cuadrado, no importa el orden de la resta. $(x_2 - x_1)^2$ da lo mismo que $(x_1 - x_2)^2$.

---

## 📖 La Fórmula de la Distancia

> **Fórmula de la distancia:** Dados dos puntos $P_1(x_1, y_1)$ y $P_2(x_2, y_2)$, la distancia entre ellos es:
>
> $$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

### ⚙️ Ejemplo 1: Distancia entre A(1, 2) y B(4, 6)

**Datos:**
- $P_1 = A(1, 2)$ entonces $x_1 = 1$, $y_1 = 2$
- $P_2 = B(4, 6)$ entonces $x_2 = 4$, $y_2 = 6$

**Aplicando la fórmula:**

$$
d = \sqrt{(4 - 1)^2 + (6 - 2)^2}
$$

$$
d = \sqrt{3^2 + 4^2}
$$

$$
d = \sqrt{9 + 16} = \sqrt{25} = 5
$$

**Respuesta:** La distancia entre A y B es $d = 5$ unidades.

> 💡 ¿Reconoces los números 3, 4 y 5? ¡Es una terna pitagórica! Esto confirma que nuestro cálculo es correcto.

### ⚙️ Ejemplo 2: Distancia entre P(-3, 2) y Q(5, -4)

**Datos:**
- $x_1 = -3$, $y_1 = 2$
- $x_2 = 5$, $y_2 = -4$

**Cálculo:**

$$
d = \sqrt{(5 - (-3))^2 + (-4 - 2)^2}
$$

$$
d = \sqrt{(5 + 3)^2 + (-6)^2}
$$

$$
d = \sqrt{8^2 + 36} = \sqrt{64 + 36} = \sqrt{100} = 10
$$

**Respuesta:** La distancia es $d = 10$ unidades.

### ⚙️ Ejemplo 3: Distancia entre M(2, 7) y N(-1, 3)

**Datos:**
- $x_1 = 2$, $y_1 = 7$
- $x_2 = -1$, $y_2 = 3$

**Cálculo:**

$$
d = \sqrt{(-1 - 2)^2 + (3 - 7)^2}
$$

$$
d = \sqrt{(-3)^2 + (-4)^2}
$$

$$
d = \sqrt{9 + 16} = \sqrt{25} = 5
$$

**Respuesta:** La distancia es $d = 5$ unidades.

---

## 📖 Casos Especiales

### Puntos con la misma ordenada (horizontal)

Si dos puntos tienen la misma coordenada $y$, están sobre una **línea horizontal**.

Para $A(x_1, y)$ y $B(x_2, y)$:

$$
d = \sqrt{(x_2 - x_1)^2 + 0^2} = |x_2 - x_1|
$$

### ⚙️ Ejemplo 4: Distancia horizontal

Encuentra la distancia entre $A(-3, 5)$ y $B(7, 5)$.

Como $y_1 = y_2 = 5$:

$$
d = |7 - (-3)| = |10| = 10
$$

### Puntos con la misma abscisa (vertical)

Si dos puntos tienen la misma coordenada $x$, están sobre una **línea vertical**.

Para $A(x, y_1)$ y $B(x, y_2)$:

$$
d = \sqrt{0^2 + (y_2 - y_1)^2} = |y_2 - y_1|
$$

### ⚙️ Ejemplo 5: Distancia vertical

Encuentra la distancia entre $P(4, -2)$ y $Q(4, 9)$.

Como $x_1 = x_2 = 4$:

$$
d = |9 - (-2)| = |11| = 11
$$

---

## 📖 Distancia al Origen

Para calcular la distancia de un punto $P(x, y)$ al origen $O(0, 0)$:

$$
d = \sqrt{(x - 0)^2 + (y - 0)^2} = \sqrt{x^2 + y^2}
$$

### ⚙️ Ejemplo 6: Distancia al origen

¿A qué distancia está el punto $A(3, 4)$ del origen?

$$
d = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

El punto $A(3, 4)$ está a 5 unidades del origen.

---

## 🔑 Resumen

| Concepto | Fórmula |
|----------|---------|
| Distancia entre $P_1$ y $P_2$ | $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ |
| Distancia horizontal | $d = \|x_2 - x_1\|$ |
| Distancia vertical | $d = \|y_2 - y_1\|$ |
| Distancia al origen | $d = \sqrt{x^2 + y^2}$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la distancia entre los puntos $A(2, 3)$ y $B(6, 6)$.

<details>
<summary>Ver solución</summary>

**Datos:** $x_1 = 2$, $y_1 = 3$, $x_2 = 6$, $y_2 = 6$

$$
d = \sqrt{(6 - 2)^2 + (6 - 3)^2}
$$

$$
d = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5
$$

**Respuesta:** $d = 5$ unidades

</details>

### Ejercicio 2
Calcula la distancia entre $P(-5, 2)$ y $Q(7, -3)$.

<details>
<summary>Ver solución</summary>

**Datos:** $x_1 = -5$, $y_1 = 2$, $x_2 = 7$, $y_2 = -3$

$$
d = \sqrt{(7 - (-5))^2 + (-3 - 2)^2}
$$

$$
d = \sqrt{12^2 + (-5)^2} = \sqrt{144 + 25} = \sqrt{169} = 13
$$

**Respuesta:** $d = 13$ unidades

</details>

### Ejercicio 3
¿A qué distancia del origen está el punto $M(-8, 6)$?

<details>
<summary>Ver solución</summary>

Usando la fórmula de distancia al origen:

$$
d = \sqrt{(-8)^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10
$$

**Respuesta:** $d = 10$ unidades

</details>

### Ejercicio 4
Un triángulo tiene vértices en $A(0, 0)$, $B(5, 0)$ y $C(5, 12)$. Calcula el perímetro del triángulo.

<details>
<summary>Ver solución</summary>

Calculamos cada lado:

**Lado AB:** (distancia horizontal, $y = 0$)
$$
AB = |5 - 0| = 5
$$

**Lado BC:** (distancia vertical, $x = 5$)
$$
BC = |12 - 0| = 12
$$

**Lado CA:**
$$
CA = \sqrt{(0 - 5)^2 + (0 - 12)^2} = \sqrt{25 + 144} = \sqrt{169} = 13
$$

**Perímetro:**
$$
P = AB + BC + CA = 5 + 12 + 13 = 30
$$

**Respuesta:** El perímetro es 30 unidades.

</details>

### Ejercicio 5
Si la distancia entre los puntos $A(2, k)$ y $B(5, 7)$ es 5 unidades, encuentra los posibles valores de $k$.

<details>
<summary>Ver solución</summary>

Usamos la fórmula de distancia e igualamos a 5:

$$
5 = \sqrt{(5 - 2)^2 + (7 - k)^2}
$$

$$
5 = \sqrt{9 + (7 - k)^2}
$$

Elevamos al cuadrado ambos lados:

$$
25 = 9 + (7 - k)^2
$$

$$
(7 - k)^2 = 16
$$

$$
7 - k = \pm 4
$$

**Caso 1:** $7 - k = 4 \Rightarrow k = 3$

**Caso 2:** $7 - k = -4 \Rightarrow k = 11$

**Respuesta:** Los posibles valores son $k = 3$ o $k = 11$

</details>
