---
title: "Conjuntos Numéricos"
---

# **Conjuntos Numéricos**

El zoológico de los números es inmenso. Empezamos con los más simples "1, 2, 3...", pero luego descubrimos el cero, los negativos, las fracciones y hasta números extraños que no terminan nunca de escribirse. Todos ellos viven organizados en grupos llamados **Conjuntos Numéricos**.

---

## 🎯 ¿Qué vas a aprender?

- Diferenciar entre Naturales ($\mathbb{N}$), Enteros ($\mathbb{Z}$), Racionales ($\mathbb{Q}$), E Irracionales ($\mathbb{I}$).
- Por qué todo entero es racional, pero no todo racional es entero.
- Entender el gran conjunto de los Reales ($\mathbb{R}$).
- Visualizar cómo encajan unos dentro de otros (como muñecas rusas).

---

## 🏛 Números Naturales ($\mathbb{N}$)

Son los más antiguos, los que sirven para **contar** cosas que puedes ver y tocar.
$$ \mathbb{N} = \{1, 2, 3, 4, 5, \ldots\} $$
*(Algunos matemáticos incluyen el 0, nosotros usaremos la convención de empezar en 1 para contar).*

### ⚙️ Ejemplos

1.  **5 manzanas** (Natural).
2.  **10 dedos** (Natural).
3.  **1 millón** (Natural, aunque grande).
4.  **-2** (No es natural, no hay "-2 manzanas").
5.  **0.5** (No es natural, no contamos con medias manzanas).

---

## 🏭 Números Enteros ($\mathbb{Z}$)

Si a los Naturales les agregamos el **Cero** y los **Negativos** (deudas), obtenemos los Enteros.
$$ \mathbb{Z} = \{ \ldots, -3, -2, -1, 0, 1, 2, 3, \ldots \} $$

### ⚙️ Relación
Todo número Natural **es también** Entero. ($\mathbb{N} \subset \mathbb{Z}$).

### ⚙️ Ejemplos

1.  **-5** (Entero, pero no natural).
2.  **0** (Entero).
3.  **3** (Es Natural y también Entero).
4.  **4.5** (No es entero, está roto).
5.  **-1000** (Entero).

---

## 🍰 Números Racionales ($\mathbb{Q}$)

Son todos los números que pueden escribirse como una **fracción** (división) de dos enteros.
Incluyen a los enteros (porque $5 = \frac{5}{1}$) y a todos los decimales que terminan o son periódicos.
$$ \mathbb{Q} = \{ \frac{a}{b} \mid a,b \in \mathbb{Z}, b \neq 0 \} $$

### ⚙️ Ejemplos

1.  **$\frac{1}{2} = 0.5$** (Racional, decimal exacto).
2.  **$\frac{1}{3} = 0.333...$** (Racional, decimal periódico).
3.  **7** (Racional, porque es $\frac{7}{1}$).
4.  **-0.25** (Racional, porque es $-\frac{1}{4}$).
5.  **$\sqrt{2}$** (¡NO es racional! Sus decimales no siguen patrón).

---

## 🌀 Números Irracionales ($\mathbb{I}$)

Son los rebeldes. Tienen decimales **infinitos y no periódicos**. No se pueden escribir como fracción.

### ⚙️ Ejemplos

1.  **$\pi$ (Pi):** $3.14159265...$ (Nunca termina, nunca se repite).
2.  **$\sqrt{2}$:** $1.4142...$ (La diagonal de un cuadrado de 1x1).
3.  **$\sqrt{3}$:** $1.7320...$
4.  **$e$ (Euler):** $2.7182...$
5.  **$\sqrt{5}$:** Otro irracional común.

---

## 🌍 Números Reales ($\mathbb{R}$)

Es la unión de TODOS los anteriores. Si está en la recta numérica, es Real.
$$ \mathbb{R} = \mathbb{Racionales} \cup \mathbb{Irracionales} $$

### Visualización
<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-conjuntos" class="jsxgraph-container" style="width: 100%; height: 320px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-conjuntos')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-conjuntos', {
      boundingbox: [-0.5, 6.5, 11, -0.5],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // ℝ - Reales (exterior)
    board.create('polygon', [[0.2, 0.2], [10.8, 0.2], [10.8, 6.2], [0.2, 6.2]], {
      fillColor: '#fef3c7', strokeColor: '#f59e0b', strokeWidth: 2, fixed: true, vertices: {visible: false}
    });
    board.create('text', [0.5, 5.9, 'ℝ Reales'], {fontSize: 13, strokeColor: '#b45309', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [9.5, 1, 'π'], {fontSize: 14, strokeColor: '#b45309', fixed: true});
    board.create('text', [9.5, 2, '√2'], {fontSize: 14, strokeColor: '#b45309', fixed: true});
    board.create('text', [9.5, 3, 'e'], {fontSize: 14, strokeColor: '#b45309', fixed: true});
    
    // ℚ - Racionales
    board.create('polygon', [[0.5, 0.5], [8.5, 0.5], [8.5, 5.8], [0.5, 5.8]], {
      fillColor: '#dbeafe', strokeColor: '#3b82f6', strokeWidth: 2, fixed: true, vertices: {visible: false}
    });
    board.create('text', [0.8, 5.5, 'ℚ Racionales'], {fontSize: 13, strokeColor: '#1d4ed8', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [7, 1.2, '1/2'], {fontSize: 13, strokeColor: '#1d4ed8', fixed: true});
    board.create('text', [7, 2, '0.75'], {fontSize: 13, strokeColor: '#1d4ed8', fixed: true});
    board.create('text', [7, 2.8, '-2/3'], {fontSize: 13, strokeColor: '#1d4ed8', fixed: true});
    
    // ℤ - Enteros
    board.create('polygon', [[0.8, 0.8], [5.8, 0.8], [5.8, 5.5], [0.8, 5.5]], {
      fillColor: '#dcfce7', strokeColor: '#22c55e', strokeWidth: 2, fixed: true, vertices: {visible: false}
    });
    board.create('text', [1.1, 5.2, 'ℤ Enteros'], {fontSize: 13, strokeColor: '#15803d', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [4.5, 1.2, '0'], {fontSize: 14, strokeColor: '#15803d', fixed: true});
    board.create('text', [4.5, 2, '-1'], {fontSize: 14, strokeColor: '#15803d', fixed: true});
    board.create('text', [4.5, 2.8, '-5'], {fontSize: 14, strokeColor: '#15803d', fixed: true});
    
    // ℕ - Naturales (interior)
    board.create('polygon', [[1.1, 1.1], [3.8, 1.1], [3.8, 5.2], [1.1, 5.2]], {
      fillColor: '#fce7f3', strokeColor: '#ec4899', strokeWidth: 2, fixed: true, vertices: {visible: false}
    });
    board.create('text', [1.4, 4.9, 'ℕ Naturales'], {fontSize: 12, strokeColor: '#be185d', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [2.4, 1.5, '1'], {fontSize: 16, strokeColor: '#be185d', fixed: true});
    board.create('text', [2.4, 2.3, '2'], {fontSize: 16, strokeColor: '#be185d', fixed: true});
    board.create('text', [2.4, 3.1, '3'], {fontSize: 16, strokeColor: '#be185d', fixed: true});
    board.create('text', [2.4, 3.9, '...'], {fontSize: 16, strokeColor: '#be185d', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Clasifica el número $-8$.

<details>
<summary>Ver solución</summary>

Es Entero ($\mathbb{Z}$), Racional ($\mathbb{Q}$) y Real ($\mathbb{R}$).
**Resultado:** $\boxed{\mathbb{Z}, \mathbb{Q}, \mathbb{R}}$

</details>

### Ejercicio 2
Clasifica el número $\frac{2}{3}$.

<details>
<summary>Ver solución</summary>

Es fracción (Racional) y Real. No es entero.
**Resultado:** $\boxed{\mathbb{Q}, \mathbb{R}}$

</details>

### Ejercicio 3
Clasifica el número $\pi$.

<details>
<summary>Ver solución</summary>

Es Irracional y Real.
**Resultado:** $\boxed{\mathbb{I}, \mathbb{R}}$

</details>

### Ejercicio 4
Clasifica el número $\sqrt{16}$.

<details>
<summary>Ver solución</summary>

$\sqrt{16} = 4$. Es Natural, Entero, Racional y Real.
**Resultado:** $\boxed{\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}}$

</details>

### Ejercicio 5
Clasifica el número $0$.

<details>
<summary>Ver solución</summary>

Entero, Racional, Real.
**Resultado:** $\boxed{\mathbb{Z}, \mathbb{Q}, \mathbb{R}}$

</details>

### Ejercicio 6
Clasifica el número $3.5$.

<details>
<summary>Ver solución</summary>

Decimal exacto $\to$ Racional, Real.
**Resultado:** $\boxed{\mathbb{Q}, \mathbb{R}}$

</details>

### Ejercicio 7
Clasifica el número $3.333...$

<details>
<summary>Ver solución</summary>

Periódico $\to$ Racional, Real.
**Resultado:** $\boxed{\mathbb{Q}, \mathbb{R}}$

</details>

### Ejercicio 8
¿Es $\frac{10}{2}$ un número natural?

<details>
<summary>Ver solución</summary>

Sí, porque $10/2 = 5$.
**Resultado:** $\boxed{\text{Sí}}$

</details>

### Ejercicio 9
¿Todos los enteros son racionales?

<details>
<summary>Ver solución</summary>

Sí, porque se pueden dividir entre 1.
**Resultado:** $\boxed{\text{Sí}}$

</details>

### Ejercicio 10
Menciona un número que sea Real pero no Racional.

<details>
<summary>Ver solución</summary>

Cualquier irracional.
**Resultado:** $\boxed{\sqrt{2}, \pi, \dots}$

</details>

---

## 🔑 Resumen

| Símbolo | Nombre | Descripción |
| :--- | :--- | :--- |
| **$\mathbb{N}$** | Naturales | Conteo ($1, 2, 3...$). |
| **$\mathbb{Z}$** | Enteros | Naturales + Cero + Negativos. |
| **$\mathbb{Q}$** | Racionales | Fracciones y decimales finitos/periódicos. |
| **$\mathbb{I}$** | Irracionales | Decimales infinitos sin patrón. |
| **$\mathbb{R}$** | Reales | Todos los anteriores. |

> **Conclusión:** Si puedes escribirlo como fracción ($\frac{a}{b}$), es Racional. Si no (como $\pi$), es Irracional. Pero ambos viven juntos en la recta Real.
