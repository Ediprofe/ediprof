# Rectángulo, Rombo y Cuadrado

Estos tres cuadriláteros son **casos especiales de paralelogramos**. Cada uno añade propiedades adicionales que los hacen únicos.

---

## 📖 El Rectángulo

> **Definición:** Un rectángulo es un paralelogramo con **cuatro ángulos rectos** (de 90°).

### Propiedades del rectángulo

| Propiedad | Descripción |
|-----------|-------------|
| Ángulos | Los 4 ángulos son de 90° |
| Lados | Lados opuestos iguales y paralelos |
| Diagonales | Iguales y se bisecan |

**Ilustración: El Rectángulo:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-rectangulo" style="width: 100%; height: 300px; min-height: 250px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initRectangulo() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-rectangulo')) {
      setTimeout(initRectangulo, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-rectangulo']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-rectangulo', {
      boundingbox: [-2, 5, 10, -3],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos fijos (lado 6x4)
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, -10]}});
    var B = board.create('point', [8, 0], {name: 'B', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, -10]}});
    var C = board.create('point', [8, 4], {name: 'C', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, 10]}});
    var D = board.create('point', [0, 4], {name: 'D', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, 10]}});
    
    // Polígono
    board.create('polygon', [A, B, C, D], {
      fillColor: '#dbeafe', 
      fillOpacity: 0.5, 
      borders: {strokeColor: '#3b82f6', strokeWidth: 2}
    });

    // Diagonales (iguales)
    board.create('segment', [A, C], {strokeColor: '#ef4444', strokeWidth: 2, dash: 2});
    board.create('segment', [B, D], {strokeColor: '#ef4444', strokeWidth: 2, dash: 2});
    
    board.create('text', [4, 1.5, 'Diagonales iguales'], {color: '#ef4444', fontSize: 11, fixed: true, anchorX: 'middle'});

    // Ángulos rectos
    var angleProps = {orthoType: 'sectordot', radius: 0.4, fillColor: 'none', strokeColor: '#1e293b'};
    board.create('angle', [D, A, B], angleProps);
    board.create('angle', [A, B, C], angleProps);
    board.create('angle', [B, C, D], angleProps);
    board.create('angle', [C, D, A], angleProps);
    
  }
  
  initRectangulo();
})();
</script>

### Diagonales del rectángulo

Las diagonales de un rectángulo son **iguales** (congruentes):

$$
AC = BD
$$

Además, se bisecan mutuamente (como todo paralelogramo).

### Diagonal con Pitágoras

Si los lados miden $a$ y $b$, la diagonal mide:

$$
d = \sqrt{a^2 + b^2}
$$

### Ejemplo

Rectángulo con lados 3 y 4:

$$
d = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

---

## 📖 El Rombo

> **Definición:** Un rombo es un paralelogramo con **cuatro lados iguales**.

### Propiedades del rombo

| Propiedad | Descripción |
|-----------|-------------|
| Lados | Los 4 lados son iguales |
| Ángulos | Opuestos iguales, consecutivos suplementarios |
| Diagonales | Perpendiculares y se bisecan |

**Ilustración: El Rombo:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-rombo" style="width: 100%; height: 350px; min-height: 250px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initRombo() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-rombo')) {
      setTimeout(initRombo, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-rombo']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-rombo', {
      boundingbox: [-3, 6, 9, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos fijos (rombo centrado, diag mayor 8, menor 6)
    // Centro (3, 2). A(3, -1), B(7, 2), C(3, 5), D(-1, 2)
    var A = board.create('point', [3, -1], {name: 'A', size: 3, color: '#1e293b', fixed: true, label: {offset: [0, -10], anchorX: 'middle'}});
    var B = board.create('point', [7, 2], {name: 'B', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, 0]}});
    var C = board.create('point', [3, 5], {name: 'C', size: 3, color: '#1e293b', fixed: true, label: {offset: [0, 10], anchorX: 'middle'}});
    var D = board.create('point', [-1, 2], {name: 'D', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, 0]}});
    
    // Centro intersección
    var M = board.create('intersection', [
      board.create('line', [A, C], {visible: false}),
      board.create('line', [B, D], {visible: false})
    ], {visible: false});

    // Polígono
    board.create('polygon', [A, B, C, D], {
      fillColor: '#fef3c7', 
      fillOpacity: 0.5, 
      borders: {strokeColor: '#f59e0b', strokeWidth: 2}
    });

    // Diagonales (perpendiculares)
    board.create('segment', [A, C], {strokeColor: '#f97316', strokeWidth: 2, dash: 2});
    board.create('segment', [B, D], {strokeColor: '#f97316', strokeWidth: 2, dash: 2});
    
    // Ángulo recto intersección
    board.create('angle', [A, M, B], {orthoType: 'sectordot', radius: 0.3, fillColor: 'none', strokeColor: '#f97316'});
    board.create('text', [3.2, 2.2, '90°'], {color: '#f97316', fontSize: 10});

    // Lados iguales
    board.create('text', [1, 0.5, 'L'], {color: '#f59e0b', fontSize: 12});
    board.create('text', [5, 0.5, 'L'], {color: '#f59e0b', fontSize: 12});
    
  }
  
  initRombo();
})();
</script>

### Diagonales del rombo

Las diagonales del rombo tienen propiedades especiales:
1. Son **perpendiculares** entre sí ($d_1 \perp d_2$)
2. Se **bisecan** mutuamente
3. **No** son iguales (excepto en el cuadrado)

### Área del rombo

El área se calcula con las diagonales:

$$
A = \frac{d_1 \times d_2}{2}
$$

### Ejemplo

Rombo con diagonales de 8 cm y 6 cm:

$$
A = \frac{8 \times 6}{2} = \frac{48}{2} = 24 \text{ cm}^2
$$

---

## 📖 El Cuadrado

> **Definición:** Un cuadrado es un paralelogramo con **4 ángulos rectos** y **4 lados iguales**.

El cuadrado es simultáneamente un **rectángulo** y un **rombo**.

### Propiedades del cuadrado

| Propiedad | Descripción |
|-----------|-------------|
| Lados | Los 4 lados son iguales |
| Ángulos | Los 4 ángulos son de 90° |
| Diagonales | Iguales, perpendiculares, se bisecan |

**Ilustración: El Cuadrado:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-cuadrado" style="width: 100%; height: 350px; min-height: 250px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initCuadrado() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-cuadrado')) {
      setTimeout(initCuadrado, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-cuadrado']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-cuadrado', {
      boundingbox: [-2, 6, 8, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos fijos (cuadrado 4x4)
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, -10]}});
    var B = board.create('point', [4, 0], {name: 'B', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, -10]}});
    var C = board.create('point', [4, 4], {name: 'C', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, 10]}});
    var D = board.create('point', [0, 4], {name: 'D', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, 10]}});
    
    // Polígono
    board.create('polygon', [A, B, C, D], {
      fillColor: '#a7f3d0', 
      fillOpacity: 0.5, 
      borders: {strokeColor: '#059669', strokeWidth: 2}
    });

    // Diagonales (iguales y perpendiculares)
    board.create('segment', [A, C], {strokeColor: '#059669', strokeWidth: 2, dash: 2});
    board.create('segment', [B, D], {strokeColor: '#059669', strokeWidth: 2, dash: 2});
    
    // Centro
    var M = board.create('point', [2, 2], {visible: false});
    // Ángulo recto intersección
    board.create('angle', [A, M, B], {orthoType: 'sectordot', radius: 0.3, fillColor: 'none', strokeColor: '#059669'});

    // Ángulos rectos vértices
    var angleProps = {orthoType: 'sectordot', radius: 0.4, fillColor: 'none', strokeColor: '#1e293b'};
    board.create('angle', [D, A, B], angleProps);
    board.create('angle', [A, B, C], angleProps);
    board.create('angle', [B, C, D], angleProps);
    board.create('angle', [C, D, A], angleProps);
    
    // Texto
    board.create('text', [2, -0.5, 'Todos los lados iguales'], {color: '#059669', fontSize: 11, fixed: true, anchorX: 'middle'});
    board.create('text', [2, 4.5, '90° vértices & diagonales'], {color: '#059669', fontSize: 11, fixed: true, anchorX: 'middle'});

  }
  
  initCuadrado();
})();
</script>

### Diagonales del cuadrado

Las diagonales del cuadrado combinan las propiedades de rectángulo y rombo:
- Son **iguales** (como en el rectángulo)
- Son **perpendiculares** (como en el rombo)
- Se **bisecan** (como todo paralelogramo)

### Diagonal del cuadrado

Si el lado mide $a$:

$$
d = a\sqrt{2}
$$

### Ejemplo

Cuadrado de lado 5:

$$
d = 5\sqrt{2} \approx 7.07
$$

---

## 📖 Jerarquía de paralelogramos

```
Paralelogramo (general)
├── Rectángulo (4 ángulos rectos)
│   └── Cuadrado
├── Rombo (4 lados iguales)
│   └── Cuadrado
└── Cuadrado (4 ángulos rectos Y 4 lados iguales)
```

> **Importante:** Todo cuadrado es rectángulo. Todo cuadrado es rombo. Pero no todo rectángulo ni todo rombo es cuadrado.

---

## 📖 Tabla comparativa

| Propiedad | Rectángulo | Rombo | Cuadrado |
|-----------|------------|-------|----------|
| 4 ángulos de 90° | ✓ | ✗ | ✓ |
| 4 lados iguales | ✗ | ✓ | ✓ |
| Diagonales iguales | ✓ | ✗ | ✓ |
| Diagonales perpendiculares | ✗ | ✓ | ✓ |
| Diagonales se bisecan | ✓ | ✓ | ✓ |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Diagonal del rectángulo

Calcula la diagonal de rectángulos con estos lados:

1. $a = 6$ cm, $b = 8$ cm
2. $a = 5$ cm, $b = 12$ cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $d = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$ cm
2. $d = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13$ cm

</details>

---

### Ejercicio 2: Área del rombo

Calcula el área de rombos con estas diagonales:

1. $d_1 = 10$ cm, $d_2 = 8$ cm
2. $d_1 = 14$ cm, $d_2 = 10$ cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \frac{10 \times 8}{2} = 40$ cm²
2. $A = \frac{14 \times 10}{2} = 70$ cm²

</details>

---

### Ejercicio 3: Cuadrado

Un cuadrado tiene lado de 10 cm. Calcula:

1. El perímetro
2. El área
3. La diagonal

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Perímetro = $4 \times 10 = 40$ cm
2. Área = $10^2 = 100$ cm²
3. Diagonal = $10\sqrt{2} \approx 14.14$ cm

</details>

---

### Ejercicio 4: Clasificar

Indica si cada afirmación es verdadera o falsa:

1. Todo cuadrado es un rectángulo.
2. Todo rectángulo es un cuadrado.
3. Las diagonales de un rombo son iguales.
4. Las diagonales de un rectángulo son perpendiculares.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero** - El cuadrado tiene 4 ángulos rectos
2. **Falso** - Solo si además tiene 4 lados iguales
3. **Falso** - Son perpendiculares pero no iguales
4. **Falso** - Son iguales pero no perpendiculares

</details>

---
