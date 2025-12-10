# 🧩 Conjuntos Numéricos

En este tema aprenderemos los diferentes conjuntos de números y sus características.

---

## 📖 Números Naturales ($\mathbb{N}$)

Son los números que usamos para **contar**.

$$
\mathbb{N} = \{1, 2, 3, 4, 5, \ldots\}
$$

### Ejemplo 1

$15$ es natural porque es un número de conteo.

---

### Ejemplo 2

$0$ no es natural en la definición tradicional (aunque algunos autores lo incluyen).

---

## 📖 Números Enteros ($\mathbb{Z}$)

Incluyen los naturales, sus opuestos y el cero.

$$
\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}
$$

### Ejemplo 1

$-5$ es entero (opuesto de un natural).

---

### Ejemplo 2

$0$ es entero.

---

## 📖 Números Racionales ($\mathbb{Q}$)

Son los que pueden expresarse como **fracción** de enteros.

$$
\mathbb{Q} = \left\{\frac{a}{b} : a, b \in \mathbb{Z}, b \neq 0\right\}
$$

### Ejemplo 1

$\frac{3}{4} = 0.75$ es racional.

---

### Ejemplo 2

$0.\overline{3} = \frac{1}{3}$ es racional (decimal periódico).

---

## 📖 Números Irracionales ($\mathbb{I}$)

Son los que **no pueden** expresarse como fracción. Tienen decimales infinitos no periódicos.

### Ejemplo 1

$\sqrt{2} = 1.41421356...$ es irracional.

---

### Ejemplo 2

$\pi = 3.14159265...$ es irracional.

---

## 📖 Números Reales ($\mathbb{R}$)

Unión de racionales e irracionales.

$$
\mathbb{R} = \mathbb{Q} \cup \mathbb{I}
$$

---

## 📖 Relación de inclusión

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}
$$

Los naturales están contenidos en los enteros, los enteros en los racionales, y los racionales en los reales.

El siguiente diagrama muestra cómo cada conjunto **contiene** al anterior:

<div id="jsxgraph-conjuntos" class="jsxgraph-container" style="width: 100%; max-width: 550px; height: 320px; margin: 1.5rem auto;"></div>

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

> 💡 **Observa:** Los irracionales (π, √2, e) están en ℝ pero **fuera** de ℚ.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Clasifica $-7$ en todos los conjuntos a los que pertenece.

**Ejercicio 2:** ¿A qué conjuntos pertenece $\frac{5}{2}$?

**Ejercicio 3:** ¿Es $\sqrt{9}$ racional o irracional?

**Ejercicio 4:** Da un ejemplo de número irracional diferente a $\pi$ y $\sqrt{2}$.

---
