# 🔢 Números Complejos

En esta lección introduciremos formalmente los números complejos, que combinan números reales e imaginarios.

---

## 📖 Definición de número complejo

Un **número complejo** es un número de la forma:

$$
z = a + bi
$$

donde:
- $a$ es la **parte real** (Re)
- $b$ es la **parte imaginaria** (Im)
- $i$ es la unidad imaginaria ($i^2 = -1$)

---

## 📖 Partes de un número complejo

| Número complejo | Parte real ($a$) | Parte imaginaria ($b$) |
|:---------------:|:----------------:|:----------------------:|
| $3 + 4i$ | $3$ | $4$ |
| $-2 + 5i$ | $-2$ | $5$ |
| $7 - 3i$ | $7$ | $-3$ |
| $-1 - 6i$ | $-1$ | $-6$ |
| $4$ | $4$ | $0$ |
| $2i$ | $0$ | $2$ |

Visualización en el plano complejo:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-complejos-intro" class="jsxgraph-container" style="width: 100%; height: 400px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board = JXG.JSXGraph.initBoard('jsxgraph-complejos-intro', {
      boundingbox: [-8, 8, 9, -8],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Puntos de los números complejos
    board.create('point', [3, 4], { name: '3 + 4i', size: 4, fixed: true, color: '#3b82f6', label: { fontSize: 12, offset: [8, 8] } });
    board.create('point', [-2, 5], { name: '-2 + 5i', size: 4, fixed: true, color: '#22c55e', label: { fontSize: 12, offset: [8, 8] } });
    board.create('point', [7, -3], { name: '7 - 3i', size: 4, fixed: true, color: '#f97316', label: { fontSize: 12, offset: [8, -12] } });
    board.create('point', [-1, -6], { name: '-1 - 6i', size: 4, fixed: true, color: '#a855f7', label: { fontSize: 12, offset: [8, -12] } });
    board.create('point', [4, 0], { name: '4', size: 4, fixed: true, color: '#ef4444', label: { fontSize: 12, offset: [0, -15] } });
    board.create('point', [0, 2], { name: '2i', size: 4, fixed: true, color: '#14b8a6', label: { fontSize: 12, offset: [10, 0] } });
    
    // Etiquetas de ejes
    board.create('text', [8.3, -0.5, 'Parte Real'], { fontSize: 11, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [0.3, 7.5, 'Parte Imaginaria'], { fontSize: 11, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Notación

$$
z = a + bi
$$

$$
\text{Re}(z) = a \quad \text{(parte real)}
$$

$$
\text{Im}(z) = b \quad \text{(parte imaginaria)}
$$

---

## 📖 Casos especiales

### Número real

Si $b = 0$, el número es **real puro**:

$$
z = a + 0i = a
$$

Los números reales son un subconjunto de los complejos.

---

### Número imaginario puro

Si $a = 0$ y $b \neq 0$, el número es **imaginario puro**:

$$
z = 0 + bi = bi
$$

---

## 📖 Igualdad de números complejos

Dos números complejos son **iguales** si y solo si sus partes reales son iguales y sus partes imaginarias son iguales:

$$
a + bi = c + di \quad \Leftrightarrow \quad a = c \text{ y } b = d
$$

---

### Ejemplo 1

Si $3 + xi = y + 4i$, encuentra $x$ e $y$.

Por igualdad de complejos:
- Parte real: $3 = y$ → $y = 3$
- Parte imaginaria: $x = 4$ → $x = 4$

$$
\boxed{x = 4, \quad y = 3}
$$

---

### Ejemplo 2

Si $(2a - 1) + (b + 3)i = 5 + 7i$, encuentra $a$ y $b$.

- Parte real: $2a - 1 = 5$ → $2a = 6$ → $a = 3$
- Parte imaginaria: $b + 3 = 7$ → $b = 4$

$$
\boxed{a = 3, \quad b = 4}
$$

---

## 📖 Identificando partes

### Ejemplo 3

Para $z = 5 - 2i$, identificar las partes.

$$
\text{Re}(z) = 5, \quad \text{Im}(z) = -2
$$

$$
\boxed{\text{Re}(z) = 5, \quad \text{Im}(z) = -2}
$$

---

### Ejemplo 4

Para $z = -3 + \sqrt{2}i$, identificar las partes.

$$
\text{Re}(z) = -3, \quad \text{Im}(z) = \sqrt{2}
$$

$$
\boxed{\text{Re}(z) = -3, \quad \text{Im}(z) = \sqrt{2}}
$$

---

### Ejemplo 5

Para $z = 7$, identificar las partes.

$z = 7 + 0i$

$$
\text{Re}(z) = 7, \quad \text{Im}(z) = 0
$$

$$
\boxed{\text{Re}(z) = 7, \quad \text{Im}(z) = 0}
$$

---

### Ejemplo 6

Para $z = -4i$, identificar las partes.

$z = 0 + (-4)i$

$$
\text{Re}(z) = 0, \quad \text{Im}(z) = -4
$$

$$
\boxed{\text{Re}(z) = 0, \quad \text{Im}(z) = -4}
$$

---

## 📖 El conjunto de los números complejos

El conjunto de los números complejos se denota con $\mathbb{C}$:

$$
\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}
$$

### Relación con otros conjuntos

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}
$$

---

## 📋 Resumen

| Concepto | Definición |
|:---------|:-----------|
| Número complejo | $z = a + bi$ |
| Parte real | $\text{Re}(z) = a$ |
| Parte imaginaria | $\text{Im}(z) = b$ |
| Igualdad | $a + bi = c + di \Leftrightarrow a = c, b = d$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Identifica la parte real e imaginaria de $z = 8 - 5i$.

<details>
<summary>Ver solución</summary>

Re$(z) = 8$, Im$(z) = -5$

</details>

---

**Ejercicio 2:** Identifica la parte real e imaginaria de $z = -\frac{1}{2} + \frac{3}{4}i$.

<details>
<summary>Ver solución</summary>

Re$(z) = -\frac{1}{2}$, Im$(z) = \frac{3}{4}$

</details>

---

**Ejercicio 3:** Si $x + 2i = 5 + yi$, encuentra $x$ e $y$.

<details>
<summary>Ver solución</summary>

$x = 5$, $y = 2$

</details>

---

**Ejercicio 4:** Si $(a + 2) + (b - 1)i = 4 + 3i$, encuentra $a$ y $b$.

<details>
<summary>Ver solución</summary>

$a + 2 = 4$ → $a = 2$

$b - 1 = 3$ → $b = 4$

</details>

---

**Ejercicio 5:** ¿Cuál es la parte imaginaria de $z = 10$?

<details>
<summary>Ver solución</summary>

Im$(z) = 0$ (es un número real)

</details>

---

**Ejercicio 6:** ¿Cuál es la parte real de $z = 6i$?

<details>
<summary>Ver solución</summary>

Re$(z) = 0$ (es un imaginario puro)

</details>

---
