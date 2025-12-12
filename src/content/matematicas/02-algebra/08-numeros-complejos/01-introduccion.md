# 🔮 Introducción a los Números Imaginarios

En esta lección introduciremos el concepto de número imaginario, su origen histórico y su importancia en las matemáticas y la vida real.

---

## 📖 El problema que motivó los imaginarios

Consideremos la ecuación:

$$
x^2 = -1
$$

¿Existe algún número real que multiplicado por sí mismo dé $-1$?

- Si $x$ es positivo: $x^2$ es positivo ✗
- Si $x$ es negativo: $x^2$ también es positivo ✗
- Si $x$ es cero: $x^2 = 0$ ✗

**No existe ningún número real cuyo cuadrado sea negativo.**

Sin embargo, esta ecuación tiene soluciones muy útiles en ingeniería, física y matemáticas avanzadas.

---

## 📖 Definición de la unidad imaginaria

Para resolver el problema anterior, los matemáticos definieron la **unidad imaginaria** $i$:

$$
i = \sqrt{-1}
$$

O equivalentemente:

$$
i^2 = -1
$$

Con esta definición, la ecuación $x^2 = -1$ tiene solución: $x = i$ o $x = -i$.

Observa cómo el eje imaginario **extiende** la recta numérica real hacia una nueva dimensión vertical:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 470px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-eje-imaginario" class="jsxgraph-container" style="width: 100%; height: 380px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board = JXG.JSXGraph.initBoard('jsxgraph-eje-imaginario', {
      boundingbox: [-4, 4, 4, -4],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Eje real (horizontal)
    board.create('line', [[0, 0], [1, 0]], {
      strokeColor: '#3b82f6',
      strokeWidth: 2,
      straightFirst: true,
      straightLast: true,
      fixed: true
    });
    board.create('text', [3.3, -0.4, 'Reales'], {
      fontSize: 12,
      strokeColor: '#3b82f6',
      cssStyle: 'font-weight: bold;',
      fixed: true
    });
    
    // Eje imaginario (vertical)
    board.create('line', [[0, 0], [0, 1]], {
      strokeColor: '#22c55e',
      strokeWidth: 2,
      straightFirst: true,
      straightLast: true,
      fixed: true
    });
    board.create('text', [0.3, 3.5, 'Imaginarios'], {
      fontSize: 12,
      strokeColor: '#22c55e',
      cssStyle: 'font-weight: bold;',
      fixed: true
    });
    
    // Origen
    board.create('point', [0, 0], {
      name: '0',
      size: 3,
      fixed: true,
      color: '#374151',
      label: { fontSize: 12, offset: [-15, -15] }
    });
    
    // Puntos en eje real
    board.create('point', [1, 0], { name: '1', size: 2, fixed: true, color: '#3b82f6', label: { fontSize: 11, offset: [0, -15] } });
    board.create('point', [2, 0], { name: '2', size: 2, fixed: true, color: '#3b82f6', label: { fontSize: 11, offset: [0, -15] } });
    board.create('point', [-1, 0], { name: '-1', size: 2, fixed: true, color: '#3b82f6', label: { fontSize: 11, offset: [0, -15] } });
    board.create('point', [-2, 0], { name: '-2', size: 2, fixed: true, color: '#3b82f6', label: { fontSize: 11, offset: [0, -15] } });
    
    // Puntos en eje imaginario
    board.create('point', [0, 1], { name: 'i', size: 4, fixed: true, color: '#22c55e', label: { fontSize: 13, offset: [10, 0], cssStyle: 'font-weight: bold; font-style: italic;' } });
    board.create('point', [0, 2], { name: '2i', size: 3, fixed: true, color: '#22c55e', label: { fontSize: 12, offset: [10, 0], cssStyle: 'font-style: italic;' } });
    board.create('point', [0, -1], { name: '-i', size: 4, fixed: true, color: '#ef4444', label: { fontSize: 13, offset: [10, 0], cssStyle: 'font-weight: bold; font-style: italic;' } });
    board.create('point', [0, -2], { name: '-2i', size: 3, fixed: true, color: '#ef4444', label: { fontSize: 12, offset: [10, 0], cssStyle: 'font-style: italic;' } });
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **Observa:** La unidad imaginaria $i$ está ubicada en el punto $(0, 1)$ del plano, exactamente una unidad hacia arriba desde el origen.

---

## 📖 Aplicaciones en el mundo real

Aunque se llaman "imaginarios", estos números tienen aplicaciones muy reales:

### Ingeniería eléctrica

Los números imaginarios son esenciales para analizar **circuitos de corriente alterna**. La impedancia de un circuito se expresa con números complejos.

### Procesamiento de señales

Las **ondas de radio, audio y video** se analizan matemáticamente usando números complejos y la transformada de Fourier.

### Mecánica cuántica

El comportamiento de las partículas subatómicas se describe con ecuaciones que requieren números complejos.

### Aerodinámica

El diseño de alas de avión utiliza análisis complejo para estudiar el flujo de aire.

---

## 📖 Definición de número imaginario

Un **número imaginario puro** es un número de la forma:

$$
bi
$$

donde $b$ es un número real y $b \neq 0$.

### Ejemplos

| Número | Clasificación |
|:------:|:--------------|
| $3i$ | Imaginario puro |
| $-5i$ | Imaginario puro |
| $\frac{1}{2}i$ | Imaginario puro |
| $\sqrt{2}i$ | Imaginario puro |

En el eje imaginario, podemos visualizar estos números:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 420px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-imaginarios-puros" class="jsxgraph-container" style="width: 100%; height: 360px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board2 = JXG.JSXGraph.initBoard('jsxgraph-imaginarios-puros', {
      boundingbox: [-3, 6, 3, -6],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Eje imaginario con flechas
    board2.create('line', [[0, 0], [0, 1]], {
      strokeColor: '#64748b',
      strokeWidth: 2,
      straightFirst: true,
      straightLast: true,
      fixed: true
    });
    
    // Título
    board2.create('text', [0, 5.5, 'Eje Imaginario'], {
      fontSize: 14,
      strokeColor: '#374151',
      cssStyle: 'font-weight: bold;',
      anchorX: 'middle',
      fixed: true
    });
    
    // Origen
    board2.create('point', [0, 0], {
      name: '0',
      size: 3,
      fixed: true,
      color: '#374151',
      label: { fontSize: 11, offset: [10, 0] }
    });
    
    // Imaginarios positivos
    board2.create('point', [0, 3], { name: '3i', size: 5, fixed: true, color: '#3b82f6', label: { fontSize: 14, offset: [12, 0], cssStyle: 'font-weight: bold; font-style: italic;' } });
    board2.create('point', [0, 1.41], { name: '√2 i', size: 4, fixed: true, color: '#22c55e', label: { fontSize: 12, offset: [12, 0], cssStyle: 'font-style: italic;' } });
    board2.create('point', [0, 0.5], { name: '½i', size: 4, fixed: true, color: '#f97316', label: { fontSize: 12, offset: [12, 0], cssStyle: 'font-style: italic;' } });
    
    // Imaginarios negativos
    board2.create('point', [0, -5], { name: '-5i', size: 5, fixed: true, color: '#ef4444', label: { fontSize: 14, offset: [12, 0], cssStyle: 'font-weight: bold; font-style: italic;' } });
    
    // Marcas de escala
    for (var j = -5; j <= 5; j++) {
      if (j !== 0) {
        board2.create('segment', [[-0.15, j], [0.15, j]], { strokeColor: '#94a3b8', strokeWidth: 1, fixed: true });
      }
    }
    
    board2.unsuspendUpdate();
  }
});
</script>

---

## 📖 Raíces cuadradas de números negativos

Usando la unidad imaginaria, podemos calcular raíces cuadradas de números negativos:

$$
\sqrt{-a} = \sqrt{a} \cdot \sqrt{-1} = \sqrt{a} \cdot i = i\sqrt{a}
$$

(para $a > 0$)

---

### Ejemplo 1

Simplificar $\sqrt{-4}$.

$$
\sqrt{-4} = \sqrt{4} \cdot \sqrt{-1} = 2i
$$

$$
\boxed{\sqrt{-4} = 2i}
$$

---

### Ejemplo 2

Simplificar $\sqrt{-9}$.

$$
\sqrt{-9} = \sqrt{9} \cdot i = 3i
$$

$$
\boxed{\sqrt{-9} = 3i}
$$

---

### Ejemplo 3

Simplificar $\sqrt{-25}$.

$$
\sqrt{-25} = \sqrt{25} \cdot i = 5i
$$

$$
\boxed{\sqrt{-25} = 5i}
$$

---

### Ejemplo 4

Simplificar $\sqrt{-7}$.

$$
\sqrt{-7} = \sqrt{7} \cdot i = i\sqrt{7}
$$

$$
\boxed{\sqrt{-7} = i\sqrt{7}}
$$

---

### Ejemplo 5

Simplificar $\sqrt{-12}$.

$$
\sqrt{-12} = \sqrt{12} \cdot i = \sqrt{4 \cdot 3} \cdot i = 2\sqrt{3} \cdot i = 2i\sqrt{3}
$$

$$
\boxed{\sqrt{-12} = 2i\sqrt{3}}
$$

---

### Ejemplo 6

Simplificar $\sqrt{-50}$.

$$
\sqrt{-50} = \sqrt{50} \cdot i = 5\sqrt{2} \cdot i = 5i\sqrt{2}
$$

$$
\boxed{\sqrt{-50} = 5i\sqrt{2}}
$$

---

## 📖 Notación

Es convención escribir $i$ **antes** del radical para evitar confusión:

- ✅ $3i\sqrt{5}$ (correcto)
- ⚠️ $3\sqrt{5}i$ (puede confundirse con $3\sqrt{5i}$)

---

## 📋 Resumen

| Concepto | Definición |
|:---------|:-----------|
| Unidad imaginaria | $i = \sqrt{-1}$, por lo tanto $i^2 = -1$ |
| Número imaginario puro | $bi$ donde $b \in \mathbb{R}$, $b \neq 0$ |
| Raíz de número negativo | $\sqrt{-a} = i\sqrt{a}$ para $a > 0$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Simplifica $\sqrt{-16}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{-16} = 4i
$$

</details>

---

**Ejercicio 2:** Simplifica $\sqrt{-49}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{-49} = 7i
$$

</details>

---

**Ejercicio 3:** Simplifica $\sqrt{-3}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{-3} = i\sqrt{3}
$$

</details>

---

**Ejercicio 4:** Simplifica $\sqrt{-18}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{-18} = \sqrt{9 \cdot 2} \cdot i = 3i\sqrt{2}
$$

</details>

---

**Ejercicio 5:** Simplifica $\sqrt{-72}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{-72} = \sqrt{36 \cdot 2} \cdot i = 6i\sqrt{2}
$$

</details>

---

**Ejercicio 6:** Si $i^2 = -1$, ¿cuánto es $(-i)^2$?

<details>
<summary>Ver solución</summary>

$$
(-i)^2 = (-1)^2 \cdot i^2 = 1 \cdot (-1) = -1
$$

</details>

---
