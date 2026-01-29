# Función Raíz

Las funciones raíz son las inversas de las potencias. La raíz cuadrada, en particular, es esencial para medir distancias y trabajar con el teorema de Pitágoras.

---

## 🎯 ¿Qué vas a aprender?

- La función raíz cuadrada y sus propiedades
- Raíces de índice superior
- Dominio y rango de funciones raíz
- Transformaciones de funciones raíz

---

## 📖 La función raíz cuadrada

La **función raíz cuadrada** se define como:

$$
f(x) = \sqrt{x}
$$

### Definición formal

$$\sqrt{x} = y \quad \Leftrightarrow \quad y^2 = x \text{ y } y \geq 0$$

La raíz cuadrada siempre da el valor **no negativo**.

### Propiedades

| Propiedad | Valor |
|-----------|-------|
| **Dominio** | $[0, +\infty)$ |
| **Rango** | $[0, +\infty)$ |
| **Paridad** | Ninguna (dominio no simétrico) |
| **Creciente** | Sí, en todo su dominio |
| **Inyectiva** | Sí |

### Puntos clave de la gráfica

| $x$ | $\sqrt{x}$ |
|-----|------------|
| $0$ | $0$ |
| $1$ | $1$ |
| $4$ | $2$ |
| $9$ | $3$ |

---

## 📖 Raíz cuadrada vs. función cuadrática

La raíz cuadrada es la **inversa parcial** de $x^2$:

$$
(\sqrt{x})^2 = x \quad \text{para } x \geq 0
$$

$$
\sqrt{x^2} = |x| \quad \text{para todo } x \in \mathbb{R}
$$

**¡Cuidado!** $\sqrt{x^2} \neq x$ cuando $x < 0$.

---

## ⚙️ Ejemplo 1: Evaluar raíces

Calcula:

a) $\sqrt{25} = 5$

b) $\sqrt{0.04} = 0.2$

c) $\sqrt{(-3)^2} = \sqrt{9} = 3 = |-3|$

d) $\sqrt{12} = \sqrt{4 \cdot 3} = 2\sqrt{3} \approx 3.46$

---

## 📖 Función raíz cúbica

$$
f(x) = \sqrt[3]{x} = x^{1/3}
$$

### Propiedades

| Propiedad | Valor |
|-----------|-------|
| **Dominio** | $\mathbb{R}$ |
| **Rango** | $\mathbb{R}$ |
| **Paridad** | Impar |
| **Inyectiva** | Sí |
| **Biyectiva** | Sí |

### Diferencia clave

La raíz **cúbica** acepta valores negativos:
$$\sqrt[3]{-8} = -2 \quad \text{porque } (-2)^3 = -8$$

---

## 📖 Raíces de índice $n$

$$
f(x) = \sqrt[n]{x} = x^{1/n}
$$

### Índice par $(n = 2, 4, 6, \ldots)$

- Dominio: $[0, +\infty)$
- Rango: $[0, +\infty)$
- Solo acepta radicandos no negativos

### Índice impar $(n = 3, 5, 7, \ldots)$

- Dominio: $\mathbb{R}$
- Rango: $\mathbb{R}$
- Acepta cualquier radicando

---

## ⚙️ Ejemplo 2: Encontrar el dominio

Determina el dominio de:

**a) $f(x) = \sqrt{x - 3}$**

Necesitamos: $x - 3 \geq 0 \Rightarrow x \geq 3$

**Dominio:** $[3, +\infty)$

**b) $g(x) = \sqrt{5 - 2x}$**

Necesitamos: $5 - 2x \geq 0 \Rightarrow x \leq 2.5$

**Dominio:** $(-\infty, 2.5]$

**c) $h(x) = \sqrt[3]{x + 1}$**

Raíz cúbica → acepta todo

**Dominio:** $\mathbb{R}$

---

## 📖 Transformaciones

Para $f(x) = a\sqrt{x - h} + k$:

| Parámetro | Efecto |
|-----------|--------|
| $h > 0$ | Desplaza $h$ unidades a la derecha |
| $k > 0$ | Desplaza $k$ unidades hacia arriba |
| $a > 1$ | Estira verticalmente |
| $0 < a < 1$ | Comprime verticalmente |
| $a < 0$ | Refleja respecto al eje X |

### Punto inicial

El punto $(0, 0)$ de $\sqrt{x}$ se traslada a $(h, k)$.

---

## ⚙️ Ejemplo 3: Transformaciones

Analiza $f(x) = 2\sqrt{x - 4} + 1$

**Punto inicial:** $(4, 1)$ (el vértice de la curva)

**Dominio:** $x \geq 4$, es decir, $[4, +\infty)$

**Rango:** $y \geq 1$, es decir, $[1, +\infty)$

**Transformaciones aplicadas:**
1. Desplazamiento 4 unidades a la derecha
2. Estiramiento vertical por factor 2
3. Desplazamiento 1 unidad hacia arriba

---

## ⚙️ Ejemplo 4: Encontrar la intersección

¿Dónde intersecta $f(x) = \sqrt{x - 1}$ al eje X?

Resolvemos $\sqrt{x - 1} = 0$:

$$x - 1 = 0 \Rightarrow x = 1$$

**Intersección:** $(1, 0)$

---

## 📊 Comparación de raíces

| Característica | $\sqrt{x}$ | $\sqrt[3]{x}$ | $\sqrt[4]{x}$ |
|----------------|------------|---------------|---------------|
| Dominio | $[0, +\infty)$ | $\mathbb{R}$ | $[0, +\infty)$ |
| Rango | $[0, +\infty)$ | $\mathbb{R}$ | $[0, +\infty)$ |
| Paridad | Ninguna | Impar | Ninguna |
| Pasa por origen | Sí | Sí | Sí |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra el dominio:

a) $f(x) = \sqrt{2x + 6}$
b) $g(x) = \sqrt{9 - x^2}$
c) $h(x) = \sqrt[5]{x - 4}$

<details>
<summary>Ver soluciones</summary>

a) $2x + 6 \geq 0 \Rightarrow x \geq -3$
   
   **Dominio:** $[-3, +\infty)$

b) $9 - x^2 \geq 0 \Rightarrow x^2 \leq 9 \Rightarrow -3 \leq x \leq 3$
   
   **Dominio:** $[-3, 3]$

c) Raíz de índice impar → todo $\mathbb{R}$
   
   **Dominio:** $\mathbb{R}$
</details>

---

**Ejercicio 2:** Para $f(x) = -\sqrt{x + 2} + 3$, encuentra:

a) Punto inicial
b) Dominio
c) Rango

<details>
<summary>Ver soluciones</summary>

a) **Punto inicial:** $(-2, 3)$

b) $x + 2 \geq 0 \Rightarrow x \geq -2$
   
   **Dominio:** $[-2, +\infty)$

c) Como hay un negativo delante de la raíz, la función decrece desde $y = 3$.
   
   **Rango:** $(-\infty, 3]$
</details>
