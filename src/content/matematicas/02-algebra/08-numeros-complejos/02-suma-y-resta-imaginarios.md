# ➕ Sumando y Restando Números Imaginarios

En esta lección aprenderemos a sumar y restar números imaginarios puros.

---

## 📖 Regla de suma y resta

Los números imaginarios puros se suman y restan como términos semejantes, operando solo los coeficientes:

$$
ai + bi = (a + b)i
$$

$$
ai - bi = (a - b)i
$$

---

### Ejemplo 1

Calcular $3i + 5i$.

$$
3i + 5i = (3 + 5)i = 8i
$$

$$
\boxed{3i + 5i = 8i}
$$

Visualización en el eje imaginario:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 420px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-suma-imag1" class="jsxgraph-container" style="width: 100%; height: 380px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma-imag1', {
      boundingbox: [-3, 10, 3, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Eje imaginario
    board.create('line', [[0, 0], [0, 1]], {
      strokeColor: '#64748b',
      strokeWidth: 2,
      straightFirst: true,
      straightLast: true,
      fixed: true
    });
    
    // Marcas
    for (var j = 0; j <= 9; j++) {
      board.create('segment', [[-0.2, j], [0.2, j]], { strokeColor: '#94a3b8', strokeWidth: 1, fixed: true });
      if (j > 0) board.create('text', [-0.8, j, j + 'i'], { fontSize: 10, strokeColor: '#64748b', fixed: true });
    }
    
    // Vector 3i (desde 0 hasta 3)
    board.create('arrow', [[0, 0], [0, 3]], {
      strokeColor: '#3b82f6',
      strokeWidth: 4,
      fixed: true
    });
    board.create('text', [0.5, 1.5, '3i'], { fontSize: 14, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true });
    
    // Vector 5i (desde 3 hasta 8)
    board.create('arrow', [[0, 3], [0, 8]], {
      strokeColor: '#22c55e',
      strokeWidth: 4,
      fixed: true
    });
    board.create('text', [0.5, 5.5, '5i'], { fontSize: 14, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true });
    
    // Resultado
    board.create('point', [0, 8], {
      name: '8i',
      size: 5,
      fixed: true,
      color: '#ef4444',
      label: { fontSize: 14, offset: [12, 0], cssStyle: 'font-weight: bold;' }
    });
    
    // Título
    board.create('text', [0, 9.5, '3i + 5i = 8i'], {
      fontSize: 16,
      strokeColor: '#374151',
      cssStyle: 'font-weight: bold;',
      anchorX: 'middle',
      fixed: true
    });
    
    board.unsuspendUpdate();
  }
});
</script>

---

### Ejemplo 2

Calcular $7i - 2i$.

$$
7i - 2i = (7 - 2)i = 5i
$$

$$
\boxed{7i - 2i = 5i}
$$

---

### Ejemplo 3

Calcular $-4i + 9i$.

$$
-4i + 9i = (-4 + 9)i = 5i
$$

$$
\boxed{-4i + 9i = 5i}
$$

---

### Ejemplo 4

Calcular $2i - 8i$.

$$
2i - 8i = (2 - 8)i = -6i
$$

$$
\boxed{2i - 8i = -6i}
$$

Visualización de la resta:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 420px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-resta-imag1" class="jsxgraph-container" style="width: 100%; height: 380px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board2 = JXG.JSXGraph.initBoard('jsxgraph-resta-imag1', {
      boundingbox: [-3, 4, 3, -8],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Eje imaginario
    board2.create('line', [[0, 0], [0, 1]], {
      strokeColor: '#64748b',
      strokeWidth: 2,
      straightFirst: true,
      straightLast: true,
      fixed: true
    });
    
    // Marcas
    for (var k = -7; k <= 3; k++) {
      board2.create('segment', [[-0.2, k], [0.2, k]], { strokeColor: '#94a3b8', strokeWidth: 1, fixed: true });
      if (k !== 0) board2.create('text', [-0.9, k, k + 'i'], { fontSize: 10, strokeColor: '#64748b', fixed: true });
    }
    board2.create('text', [-0.5, 0, '0'], { fontSize: 10, strokeColor: '#64748b', fixed: true });
    
    // Vector 2i (desde 0 hasta 2)
    board2.create('arrow', [[0, 0], [0, 2]], {
      strokeColor: '#3b82f6',
      strokeWidth: 4,
      fixed: true
    });
    board2.create('text', [0.5, 1, '2i'], { fontSize: 14, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true });
    
    // Vector -8i (desde 2 hasta -6)
    board2.create('arrow', [[0, 2], [0, -6]], {
      strokeColor: '#f97316',
      strokeWidth: 4,
      fixed: true
    });
    board2.create('text', [0.6, -2, '-8i'], { fontSize: 14, strokeColor: '#f97316', cssStyle: 'font-weight: bold;', fixed: true });
    
    // Resultado
    board2.create('point', [0, -6], {
      name: '-6i',
      size: 5,
      fixed: true,
      color: '#ef4444',
      label: { fontSize: 14, offset: [12, 0], cssStyle: 'font-weight: bold;' }
    });
    
    // Título
    board2.create('text', [0, 3.3, '2i - 8i = -6i'], {
      fontSize: 16,
      strokeColor: '#374151',
      cssStyle: 'font-weight: bold;',
      anchorX: 'middle',
      fixed: true
    });
    
    board2.unsuspendUpdate();
  }
});
</script>

---

### Ejemplo 5

Calcular $\sqrt{-9} + \sqrt{-16}$.

**Paso 1:** Convertimos a imaginarios:

$$
\sqrt{-9} = 3i, \quad \sqrt{-16} = 4i
$$

**Paso 2:** Sumamos:

$$
3i + 4i = 7i
$$

$$
\boxed{\sqrt{-9} + \sqrt{-16} = 7i}
$$

---

### Ejemplo 6

Calcular $\sqrt{-25} - \sqrt{-4}$.

$$
\sqrt{-25} = 5i, \quad \sqrt{-4} = 2i
$$

$$
5i - 2i = 3i
$$

$$
\boxed{\sqrt{-25} - \sqrt{-4} = 3i}
$$

---

### Ejemplo 7

Calcular $\sqrt{-8} + \sqrt{-18}$.

**Paso 1:** Simplificamos:

$$
\sqrt{-8} = \sqrt{8} \cdot i = 2\sqrt{2} \cdot i = 2i\sqrt{2}
$$

$$
\sqrt{-18} = \sqrt{18} \cdot i = 3\sqrt{2} \cdot i = 3i\sqrt{2}
$$

**Paso 2:** Sumamos:

$$
2i\sqrt{2} + 3i\sqrt{2} = 5i\sqrt{2}
$$

$$
\boxed{\sqrt{-8} + \sqrt{-18} = 5i\sqrt{2}}
$$

---

### Ejemplo 8

Calcular $\sqrt{-12} - \sqrt{-27}$.

$$
\sqrt{-12} = 2i\sqrt{3}, \quad \sqrt{-27} = 3i\sqrt{3}
$$

$$
2i\sqrt{3} - 3i\sqrt{3} = -i\sqrt{3}
$$

$$
\boxed{\sqrt{-12} - \sqrt{-27} = -i\sqrt{3}}
$$

---

## 📖 Combinando reales e imaginarios

Cuando tenemos mezcla de números reales e imaginarios, los separamos:

### Ejemplo 9

Simplificar $(5 + 3i) + 2i$.

$$
5 + 3i + 2i = 5 + 5i
$$

$$
\boxed{(5 + 3i) + 2i = 5 + 5i}
$$

---

### Ejemplo 10

Simplificar $4i + 7 - 2i + 3$.

$$
(7 + 3) + (4i - 2i) = 10 + 2i
$$

$$
\boxed{4i + 7 - 2i + 3 = 10 + 2i}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula $6i + 4i$.

<details>
<summary>Ver solución</summary>

$$
6i + 4i = 10i
$$

</details>

---

**Ejercicio 2:** Calcula $9i - 12i$.

<details>
<summary>Ver solución</summary>

$$
9i - 12i = -3i
$$

</details>

---

**Ejercicio 3:** Calcula $\sqrt{-36} + \sqrt{-49}$.

<details>
<summary>Ver solución</summary>

$$
6i + 7i = 13i
$$

</details>

---

**Ejercicio 4:** Calcula $\sqrt{-20} + \sqrt{-45}$.

<details>
<summary>Ver solución</summary>

$$
2i\sqrt{5} + 3i\sqrt{5} = 5i\sqrt{5}
$$

</details>

---

**Ejercicio 5:** Simplifica $3i - 8i + 5i$.

<details>
<summary>Ver solución</summary>

$$
(3 - 8 + 5)i = 0i = 0
$$

</details>

---

**Ejercicio 6:** Simplifica $2 + 5i + 3 - 2i$.

<details>
<summary>Ver solución</summary>

$$
(2 + 3) + (5i - 2i) = 5 + 3i
$$

</details>

---
