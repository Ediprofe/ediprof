# Trapecio

Un **trapecio** es un cuadrilátero con exactamente un par de lados paralelos. Es muy común en arquitectura y diseño.

---

## 📖 Definición

> **Definición:** Un trapecio es un cuadrilátero que tiene **un solo par de lados paralelos**.

### Elementos del trapecio

| Elemento | Descripción |
|----------|-------------|
| Base mayor ($B$) | El lado paralelo más largo |
| Base menor ($b$) | El lado paralelo más corto |
| Lados no paralelos | Los otros dos lados (laterales) |
| Altura ($h$) | Distancia perpendicular entre las bases |

---

## 📖 Clasificación de trapecios

### Trapecio isósceles

Los **lados no paralelos son iguales**.

Propiedades:
- Ángulos de la base mayor: iguales
- Ángulos de la base menor: iguales
- Diagonales: iguales

### Trapecio rectángulo

Tiene **dos ángulos rectos** (un lado perpendicular a las bases).

### Trapecio escaleno

Los lados no paralelos son **diferentes**.

**Ilustración: Tipos de Trapecio:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-trapecios" style="width: 100%; height: 350px; min-height: 250px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initTrapecios() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-trapecios')) {
      setTimeout(initTrapecios, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-trapecios']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-trapecios', {
      boundingbox: [-1, 5, 12, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // 1. Trapecio Isósceles (Izquierda)
    // Base mayor 4, menor 2, centrado en x=1.5
    var A1 = board.create('point', [0, 0], {visible: false, fixed: true});
    var B1 = board.create('point', [4, 0], {visible: false, fixed: true});
    var C1 = board.create('point', [3, 2], {visible: false, fixed: true});
    var D1 = board.create('point', [1, 2], {visible: false, fixed: true});
    
    board.create('polygon', [A1, B1, C1, D1], {
      fillColor: '#dbeafe', 
      borders: {strokeColor: '#3b82f6', strokeWidth: 2}
    });

    board.create('text', [2, -0.5, 'Isósceles'], {color: '#1e40af', fontSize: 11, fixed: true, anchorX: 'middle'});
    // Lados iguales
    board.create('segment', [A1, D1], {strokeColor: '#ef4444', strokeWidth: 2});
    board.create('segment', [B1, C1], {strokeColor: '#ef4444', strokeWidth: 2});

    // 2. Trapecio Rectángulo (Centro)
    // x range: 5 to 7.5
    var A2 = board.create('point', [5, 0], {visible: false, fixed: true});
    var B2 = board.create('point', [7.5, 0], {visible: false, fixed: true});
    var C2 = board.create('point', [6.5, 2.5], {visible: false, fixed: true});
    var D2 = board.create('point', [5, 2.5], {visible: false, fixed: true});
    
    board.create('polygon', [A2, B2, C2, D2], {
      fillColor: '#dcfce7', 
      borders: {strokeColor: '#166534', strokeWidth: 2}
    });
    
    board.create('angle', [B2, A2, D2], {orthoType: 'sectordot', radius: 0.3, fillColor: 'none', strokeColor: '#166534'});
    board.create('angle', [A2, D2, C2], {orthoType: 'sectordot', radius: 0.3, fillColor: 'none', strokeColor: '#166534'});

    board.create('text', [6.25, -0.5, 'Rectángulo'], {color: '#166534', fontSize: 11, fixed: true, anchorX: 'middle'});

    // 3. Trapecio Escaleno (Derecha)
    // x range: 8.5 to 11.5
    var A3 = board.create('point', [8, 0], {visible: false, fixed: true});
    var B3 = board.create('point', [11, 0], {visible: false, fixed: true});
    var C3 = board.create('point', [11.5, 2], {visible: false, fixed: true}); // Muy inclinado
    var D3 = board.create('point', [9, 2], {visible: false, fixed: true});
    
    board.create('polygon', [A3, B3, C3, D3], {
      fillColor: '#fef3c7', 
      borders: {strokeColor: '#b45309', strokeWidth: 2}
    });

    board.create('text', [9.75, -0.5, 'Escaleno'], {color: '#b45309', fontSize: 11, fixed: true, anchorX: 'middle'});
  }
  
  initTrapecios();
})();
</script>

---

## 📖 Propiedades generales

### Suma de ángulos

Como todo cuadrilátero:

$$
\angle A + \angle B + \angle C + \angle D = 360°
$$

### Ángulos entre las bases

Los ángulos adyacentes a un mismo lado no paralelo son **suplementarios**:

$$
\angle A + \angle D = 180°
$$

$$
\angle B + \angle C = 180°
$$

---

## 📖 Base media del trapecio

La **base media** (o mediana) de un trapecio es el segmento que une los puntos medios de los lados no paralelos.

### Propiedades de la base media

1. Es **paralela** a las bases
2. Su longitud es el **promedio de las bases**:

$$
m = \frac{B + b}{2}
$$

**Ilustración: Base Media:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-basemedia" style="width: 100%; height: 300px; min-height: 250px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initBaseMedia() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-basemedia')) {
      setTimeout(initBaseMedia, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-basemedia']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-basemedia', {
      boundingbox: [-1, 5, 8, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos fijos
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, -10]}});
    var B = board.create('point', [7, 0], {name: 'B', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, -10]}});
    var C = board.create('point', [5, 4], {name: 'C', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, 10]}});
    var D = board.create('point', [2, 4], {name: 'D', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, 10]}});
    
    // Polígono
    board.create('polygon', [A, B, C, D], {
      fillColor: '#f1f5f9', 
      borders: {strokeColor: '#334155', strokeWidth: 2}
    });

    // Puntos medios
    var M_AD = board.create('midpoint', [A, D], {name: 'M', size: 3, color: '#ef4444', fixed: true, label: {offset: [-15, 0]}});
    var M_BC = board.create('midpoint', [B, C], {name: 'N', size: 3, color: '#ef4444', fixed: true, label: {offset: [10, 0]}});

    // Segmento Base Media
    board.create('segment', [M_AD, M_BC], {strokeColor: '#ef4444', strokeWidth: 3});

    // Etiquetas
    board.create('text', [3.5, 4.2, 'Base menor (b)'], {color: '#334155', fontSize: 11, fixed: true, anchorX: 'middle'});
    board.create('text', [3.5, -0.4, 'Base mayor (B)'], {color: '#334155', fontSize: 11, fixed: true, anchorX: 'middle'});
    board.create('text', [3.5, 2.2, 'm (media)'], {color: '#ef4444', fontSize: 12, fontWeight: 'bold', fixed: true, anchorX: 'middle'});

  }
  
  initBaseMedia();
})();
</script>

---

## 📖 Propiedades generales

### Suma de ángulos

Como todo cuadrilátero:

$$
\angle A + \angle B + \angle C + \angle D = 360°
$$

### Ángulos entre las bases

Los ángulos adyacentes a un mismo lado no paralelo son **suplementarios**:

$$
\angle A + \angle D = 180°
$$

$$
\angle B + \angle C = 180°
$$

---

## 📖 Base media del trapecio

La **base media** (o mediana) de un trapecio es el segmento que une los puntos medios de los lados no paralelos.

### Propiedades de la base media

1. Es **paralela** a las bases
2. Su longitud es el **promedio de las bases**:

$$
m = \frac{B + b}{2}
$$

### Ejemplo

Si $B = 12$ cm y $b = 8$ cm:

$$
m = \frac{12 + 8}{2} = \frac{20}{2} = 10 \text{ cm}
$$

---

## 📖 Área del trapecio

$$
A = \frac{(B + b) \times h}{2}
$$

O equivalentemente:

$$
A = m \times h
$$

Donde $m$ es la base media.

### Ejemplo

Trapecio con $B = 10$ cm, $b = 6$ cm, $h = 4$ cm:

$$
A = \frac{(10 + 6) \times 4}{2} = \frac{16 \times 4}{2} = \frac{64}{2} = 32 \text{ cm}^2
$$

---

## 📖 Perímetro del trapecio

$$
P = B + b + l_1 + l_2
$$

Donde $l_1$ y $l_2$ son los lados no paralelos.

### Trapecio isósceles

Si $l_1 = l_2 = l$:

$$
P = B + b + 2l
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular base media

Calcula la base media de trapecios con estas bases:

1. $B = 14$ cm, $b = 10$ cm
2. $B = 20$ cm, $b = 8$ cm
3. $B = 15$ cm, $b = 9$ cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $m = \frac{14 + 10}{2} = 12$ cm
2. $m = \frac{20 + 8}{2} = 14$ cm
3. $m = \frac{15 + 9}{2} = 12$ cm

</details>

---

### Ejercicio 2: Calcular área

Calcula el área de cada trapecio:

1. $B = 12$ cm, $b = 8$ cm, $h = 5$ cm
2. $B = 18$ cm, $b = 10$ cm, $h = 6$ cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \frac{(12 + 8) \times 5}{2} = \frac{100}{2} = 50$ cm²
2. $A = \frac{(18 + 10) \times 6}{2} = \frac{168}{2} = 84$ cm²

</details>

---

### Ejercicio 3: Encontrar una base

El área de un trapecio es 60 cm². Si $B = 14$ cm y $h = 6$ cm, ¿cuánto mide $b$?

<details>
<summary><strong>Ver respuestas</strong></summary>

Despejando de la fórmula:

$$
60 = \frac{(14 + b) \times 6}{2}
$$

$$
120 = (14 + b) \times 6
$$

$$
20 = 14 + b
$$

$$
b = 6 \text{ cm}
$$

</details>

---

### Ejercicio 4: Clasificar trapecios

¿Qué tipo de trapecio es cada uno?

1. Un trapecio con lados no paralelos de 5 cm cada uno
2. Un trapecio con un lado perpendicular a las bases
3. Un trapecio con lados no paralelos de 4 cm y 6 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Trapecio isósceles** (lados no paralelos iguales)
2. **Trapecio rectángulo** (tiene ángulos de 90°)
3. **Trapecio escaleno** (lados no paralelos diferentes)

</details>

---

### Ejercicio 5: Perímetro

Calcula el perímetro de un trapecio isósceles con $B = 16$ cm, $b = 10$ cm y lados laterales de 5 cm cada uno.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
P = 16 + 10 + 5 + 5 = 36 \text{ cm}
$$

</details>

---
