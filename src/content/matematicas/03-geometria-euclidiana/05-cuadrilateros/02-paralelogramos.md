# Paralelogramos

Un **paralelogramo** es un cuadrilátero con dos pares de lados paralelos. Es la base de muchas figuras importantes como el rectángulo, el rombo y el cuadrado.

---

## 📖 Definición

> **Definición:** Un paralelogramo es un cuadrilátero cuyos lados opuestos son **paralelos**.

$$
AB \parallel CD \quad \text{y} \quad BC \parallel AD
$$

**Ilustración: Propiedades del Paralelogramo:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-paralelogramo" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initParalelogramo() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-paralelogramo')) {
      setTimeout(initParalelogramo, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-paralelogramo']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-paralelogramo', {
      boundingbox: [-2, 5, 10, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos fijos
    // Base 6. Altura 3. Skew 2.
    // A(0,0), B(6,0), D(2,3), C(8,3).
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, -10]}});
    var B = board.create('point', [6, 0], {name: 'B', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, -10]}});
    var C = board.create('point', [8, 3], {name: 'C', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, 10]}});
    var D = board.create('point', [2, 3], {name: 'D', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, 10]}});
    
    // Polígono
    var poly = board.create('polygon', [A, B, C, D], {
      fillColor: '#dbeafe', 
      fillOpacity: 0.5, 
      borders: {strokeColor: '#3b82f6', strokeWidth: 2}
    });

    // Ángulos
    var angleStyle = {radius: 0.5, fillOpacity: 0.3};
    // A y C son agudos. B y D son obtusos.
    // Coloreamos pares iguales.
    board.create('angle', [D, A, B], { ...angleStyle, fillColor: '#22c55e', strokeColor: '#166534', name: 'α' });
    board.create('angle', [B, C, D], { ...angleStyle, fillColor: '#22c55e', strokeColor: '#166534', name: 'α' });
    
    board.create('angle', [A, B, C], { ...angleStyle, fillColor: '#f97316', strokeColor: '#c2410c', name: 'β' });
    board.create('angle', [C, D, A], { ...angleStyle, fillColor: '#f97316', strokeColor: '#c2410c', name: 'β' });
    
    // Etiquetas de lados (mostrando igualdad)
    // Lados paralelos horizontales (a)
    board.create('text', [3, -0.3, 'a'], {color: '#3b82f6', fontSize: 12, fixed: true, anchorX: 'middle'});
    board.create('text', [5, 3.3, 'a'], {color: '#3b82f6', fontSize: 12, fixed: true, anchorX: 'middle'});

    // Lados paralelos inclinados (b)
    board.create('text', [0.8, 1.5, 'b'], {color: '#3b82f6', fontSize: 12, fixed: true, anchorX: 'right'});
    board.create('text', [7.2, 1.5, 'b'], {color: '#3b82f6', fontSize: 12, fixed: true, anchorX: 'left'});

    // Altura (opcional pero instructiva para el área)
    var H = board.create('point', [2, 0], {visible: false});
    board.create('segment', [D, H], {strokeColor: '#64748b', dash: 2});
    board.create('text', [2.2, 1.5, 'h'], {color: '#64748b', fontSize: 11, fixed: true});
    // Ángulo recto de la altura
    board.create('angle', [D, H, B], {orthoType: 'sectordot', radius: 0.3, fillColor: 'none', strokeColor: '#64748b'});

  }
  
  initParalelogramo();
})();
</script>

---

## 📖 Propiedades de los lados

### Propiedad 1: Lados opuestos iguales

Los lados opuestos de un paralelogramo son **congruentes** (tienen la misma longitud).

$$
AB = CD \quad \text{y} \quad BC = AD
$$

### Ejemplo

Si $AB = 8$ cm y $BC = 5$ cm, entonces:
- $CD = 8$ cm
- $AD = 5$ cm
- Perímetro = $2(8) + 2(5) = 26$ cm

---

## 📖 Propiedades de los ángulos

### Propiedad 2: Ángulos opuestos iguales

Los ángulos opuestos de un paralelogramo son **iguales**.

$$
\angle A = \angle C \quad \text{y} \quad \angle B = \angle D
$$

### Propiedad 3: Ángulos consecutivos suplementarios

Dos ángulos consecutivos (adyacentes) suman **180°**.

$$
\angle A + \angle B = 180°
$$

### Ejemplo

Si $\angle A = 70°$, entonces:
- $\angle C = 70°$ (opuesto)
- $\angle B = 180° - 70° = 110°$ (consecutivo)
- $\angle D = 110°$ (opuesto a B)

---

## 📖 Propiedades de las diagonales

### Propiedad 4: Las diagonales se bisecan

Las diagonales de un paralelogramo se **cortan en su punto medio**.

Si $M$ es el punto de intersección:

$$
AM = MC \quad \text{y} \quad BM = MD
$$

### Ejemplo

Si la diagonal $AC = 12$ cm, entonces $AM = MC = 6$ cm.

---

## 📖 Resumen de propiedades

| Propiedad | Descripción |
|-----------|-------------|
| Lados opuestos | Paralelos e iguales |
| Ángulos opuestos | Iguales |
| Ángulos consecutivos | Suplementarios (suman 180°) |
| Diagonales | Se bisecan mutuamente |

---

## 📖 Área del paralelogramo

El área de un paralelogramo se calcula como:

$$
A = b \times h
$$

Donde:
- $b$ = base (cualquier lado)
- $h$ = altura (distancia perpendicular entre las bases)

### Ejemplo

Si $b = 10$ cm y $h = 6$ cm:

$$
A = 10 \times 6 = 60 \text{ cm}^2
$$

---

## 📖 Casos especiales de paralelogramos

| Figura | Característica adicional |
|--------|-------------------------|
| Rectángulo | 4 ángulos rectos |
| Rombo | 4 lados iguales |
| Cuadrado | 4 ángulos rectos Y 4 lados iguales |

> **Nota:** El cuadrado es a la vez rectángulo Y rombo.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular lados

En un paralelogramo $ABCD$, $AB = 12$ cm y $BC = 7$ cm. Calcula:

1. La longitud de $CD$
2. La longitud de $AD$
3. El perímetro

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $CD = AB = 12$ cm (lados opuestos iguales)
2. $AD = BC = 7$ cm (lados opuestos iguales)
3. Perímetro = $2(12) + 2(7) = 24 + 14 = 38$ cm

</details>

---

### Ejercicio 2: Calcular ángulos

En un paralelogramo, $\angle A = 65°$. Calcula los demás ángulos.

<details>
<summary><strong>Ver respuestas</strong></summary>

- $\angle C = 65°$ (opuesto a A)
- $\angle B = 180° - 65° = 115°$ (consecutivo a A)
- $\angle D = 115°$ (opuesto a B)

Verificación: $65° + 115° + 65° + 115° = 360°$ ✓

</details>

---

### Ejercicio 3: Diagonales

Las diagonales de un paralelogramo miden 14 cm y 10 cm. ¿Cuánto mide cada segmento desde un vértice hasta el punto de intersección?

<details>
<summary><strong>Ver respuestas</strong></summary>

Como las diagonales se bisecan:
- Diagonal de 14 cm: cada mitad mide $14 \div 2 = 7$ cm
- Diagonal de 10 cm: cada mitad mide $10 \div 2 = 5$ cm

</details>

---

### Ejercicio 4: Área

Calcula el área de un paralelogramo con:

1. Base = 15 cm, altura = 8 cm
2. Base = 20 cm, altura = 12 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = 15 \times 8 = 120$ cm²
2. $A = 20 \times 12 = 240$ cm²

</details>

---
