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

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-rectangulo" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
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
      boundingbox: [-2, 6, 10, -3],
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
    
    // Punto medio
    var M = board.create('point', [4, 2], {visible: false, fixed: true});

    // Ticks en las diagonales (iguales para los 4 segmentos)
    board.create('group', [
        board.create('text', [2, 1.2, '|'], {color: '#ef4444', anchorX:'middle', rotation: 26}), // Sobre AC
        board.create('text', [6, 2.8, '|'], {color: '#ef4444', anchorX:'middle', rotation: 26}),
        board.create('text', [2, 2.8, '|'], {color: '#ef4444', anchorX:'middle', rotation: -26}), // Sobre BD
        board.create('text', [6, 1.2, '|'], {color: '#ef4444', anchorX:'middle', rotation: -26})
    ]);
    
    board.create('text', [4, 5, 'Diagonales iguales y se bisecan'], {color: '#ef4444', fontSize: 12, fontWeight:'bold', fixed: true, anchorX: 'middle'});

    // Ángulos rectos (Interiores: CCW)
    // D->A->B es 270 (Exterior). B->A->D es 90 (Interior).
    var angleProps = {orthoType: 'sectordot', radius: 0.4, fillColor: 'none', strokeColor: '#1e293b'};
    board.create('angle', [B, A, D], angleProps);
    board.create('angle', [C, B, A], angleProps);
    board.create('angle', [D, C, B], angleProps);
    board.create('angle', [A, D, C], angleProps);
    
  }
  
  initRectangulo();
})();
</script>

### Diagonales del rectángulo

Las diagonales de un rectángulo son **iguales** (congruentes):

$$
AC = BD
$$

Además, se bisecan mutuamente (se cortan exactamente a la mitad, como todo paralelogramo).

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

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-rombo" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
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
      boundingbox: [-3, 7, 9, -3],
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
    ], {visible: false, name:'M'});

    // Polígono
    board.create('polygon', [A, B, C, D], {
      fillColor: '#fef3c7', 
      fillOpacity: 0.4, 
      borders: {strokeColor: '#f59e0b', strokeWidth: 2}
    });

    // Diagonales (perpendiculares)
    board.create('segment', [A, C], {strokeColor: '#f97316', strokeWidth: 2, dash: 2});
    board.create('segment', [B, D], {strokeColor: '#f97316', strokeWidth: 2, dash: 2});
    
    // Ángulo recto intersección (Interior)
    board.create('angle', [A, M, B], {orthoType: 'sectordot', radius: 0.3, fillColor: 'none', strokeColor: '#f97316'});
    board.create('text', [3.3, 2.3, '90°'], {color: '#f97316', fontSize: 10});

    // Lados iguales (Ticks: || en cada lado)
    var sideTicks = {color: '#f59e0b', anchorX:'middle', fontSize: 10};
    board.create('text', [1, 0.5, '||'], { ...sideTicks, rotation: -37 }); // DA
    board.create('text', [5, 0.5, '||'], { ...sideTicks, rotation: 37 });  // AB
    board.create('text', [5, 3.5, '||'], { ...sideTicks, rotation: -37 }); // BC
    board.create('text', [1, 3.5, '||'], { ...sideTicks, rotation: 37 });  // CD

    // Diagonales se bisecan pero NO son iguales
    // Vertical (AC): 1 tick (|)
    board.create('text', [3, 0.5, '-'], {color: '#f97316', anchorX:'middle', rotation: 0, fontSize: 14});
    board.create('text', [3, 3.5, '-'], {color: '#f97316', anchorX:'middle', rotation: 0, fontSize: 14});

    // Horizontal (BD): 2 ticks (=) o marca diferente (x)
    board.create('text', [5, 2, '='], {color: '#f97316', anchorX:'middle', rotation: 90, fontSize: 14});
    board.create('text', [1, 2, '='], {color: '#f97316', anchorX:'middle', rotation: 90, fontSize: 14});

    
  }
  
  initRombo();
})();
</script>

### Diagonales del rombo

Las diagonales del rombo tienen propiedades especiales:
1. Son **perpendiculares** entre sí ($d_1 \perp d_2$)
2. Se **bisecan** mutuamente (se cortan en su punto medio)
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

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-cuadrado" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
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
      boundingbox: [-2, 6, 8, -3],
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
    
    // Polígono (Colores estandarizados: Azul/Slate)
    board.create('polygon', [A, B, C, D], {
      fillColor: '#dbeafe', 
      fillOpacity: 0.5, 
      borders: {strokeColor: '#3b82f6', strokeWidth: 2}
    });

    // Diagonales (iguales y perpendiculares)
    board.create('segment', [A, C], {strokeColor: '#ef4444', strokeWidth: 2, dash: 2});
    board.create('segment', [B, D], {strokeColor: '#ef4444', strokeWidth: 2, dash: 2});
    
    // Centro
    var M = board.create('point', [2, 2], {visible: false});
    // Ángulo recto intersección (Interior)
    board.create('angle', [A, M, B], {orthoType: 'sectordot', radius: 0.3, fillColor: 'none', strokeColor: '#ef4444'});

    // Ángulos rectos vértices (Interiores CCW)
    // D->A->B es 270(Ext). B->A->D es 90(Int).
    var angleProps = {orthoType: 'sectordot', radius: 0.4, fillColor: 'none', strokeColor: '#1e293b'};
    board.create('angle', [B, A, D], angleProps);
    board.create('angle', [C, B, A], angleProps);
    board.create('angle', [D, C, B], angleProps);
    board.create('angle', [A, D, C], angleProps);
    
    // Ticks de lados iguales (||) 
    var sideTicks = {color: '#3b82f6', anchorX:'middle', fontSize: 10};
    board.create('text', [2, -0.2, '||'], { ...sideTicks, rotation: 0 });  // AB
    board.create('text', [4.2, 2, '||'], { ...sideTicks, rotation: 90 });  // BC
    board.create('text', [2, 4.2, '||'], { ...sideTicks, rotation: 0 });   // CD
    board.create('text', [-0.2, 2, '||'], { ...sideTicks, rotation: 90 }); // DA

    // Ticks diagonales (iguales en los 4 semi-segmentos: |)
    var diagTicks = {color: '#ef4444', anchorX:'middle', fontSize: 10};
    board.create('text', [1, 1, '|'], { ...diagTicks, rotation: 45 });
    board.create('text', [3, 1, '|'], { ...diagTicks, rotation: -45 });
    board.create('text', [3, 3, '|'], { ...diagTicks, rotation: 45 });
    board.create('text', [1, 3, '|'], { ...diagTicks, rotation: -45 });
    
    board.create('text', [2, 5, 'Unión perfecta: Lados iguales + Ángulos 90°'], {color: '#1e293b', fontSize: 12, fontWeight: 'bold', fixed: true, anchorX: 'middle'});

  }
  
  initCuadrado();
})();
</script>

### Diagonales del cuadrado

Las diagonales del cuadrado combinan las propiedades de rectángulo y rombo:
- Son **iguales** (como en el rectángulo)
- Son **perpendiculares** (como en el rombo)
- Se **bisecan** (se dividen en dos partes iguales)

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

**Ilustración: Jerarquía de Paralelogramos:**
<div style="display: flex; justify-content: center; width: 100%; margin: 2rem 0;">
    <canvas id="rough-jerarquia" width="600" height="400"></canvas>
</div>

<script src="https://unpkg.com/roughjs@4.6.6/bundled/rough.js"></script>
<script>
  function initJerarquia() {
    // Esperar a que rough esté cargado globalmente
    if (typeof rough === 'undefined') {
        // Intentar cargar dinámicamente si el script no funcionó o esperar
        setTimeout(initJerarquia, 100);
        return;
    }

    const canvas = document.getElementById('rough-jerarquia');
    if (!canvas) {
        setTimeout(initJerarquia, 100);
        return;
    }
    const rc = rough.canvas(canvas);
    const ctx = canvas.getContext('2d');
    
    // Limpiar
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Configuración
    const cardW = 140;
    const cardH = 50;
    const colorFill = '#f1f5f9';
    const colorStroke = '#1e293b';
    
    // Coordenadas Centros
    const topX = 300, topY = 50;       // Paralelogramo
    const midLeftX = 150, midY = 180;  // Rectángulo
    const midRightX = 450;             // Rombo
    const botX = 300, botY = 320;      // Cuadrado
    
    // Función para dibujar tarjeta
    // x, y es el CENTRO
    function drawCard(x, y, text, color) {
        const xrec = x - cardW/2;
        const yrec = y - cardH/2;
        rc.rectangle(xrec, yrec, cardW, cardH, {
             fill: color || colorFill, 
             fillStyle: 'solid',
             roughness: 0.5,
             stroke: colorStroke
        });
        
        ctx.font = 'bold 16px sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = '#1e293b';
        ctx.fillText(text, x, y);
    }
    
    // Función para dibujar flecha
    function drawArrow(x1, y1, x2, y2) {
        rc.line(x1, y1, x2, y2, {stroke: '#64748b', strokeWidth: 2, roughness: 0.5});
        // Punta simple (círculo pequeño o linea)
        rc.circle(x2, y2, 5, {fill: '#64748b', stroke: 'none'});
    }

    // --- Dibujo ---
    
    // Nivel 1: Paralelogramo
    drawCard(topX, topY, 'Paralelogramo', '#e2e8f0');
    
    // Nivel 2: Rectángulo y Rombo
    drawCard(midLeftX, midY, 'Rectángulo', '#dbeafe');
    drawCard(midRightX, midY, 'Rombo', '#fef3c7');
    
    // Nivel 3: Cuadrado
    drawCard(botX, botY, 'Cuadrado', '#a7f3d0');
    
    // Flechas
    // Para -> Rect
    drawArrow(topX, topY + cardH/2, midLeftX, midY - cardH/2);
    // Para -> Rombo
    drawArrow(topX, topY + cardH/2, midRightX, midY - cardH/2);
    
    // Rect -> Cuadrado
    drawArrow(midLeftX, midY + cardH/2, botX, botY - cardH/2);
    // Rombo -> Cuadrado
    drawArrow(midRightX, midY + cardH/2, botX, botY - cardH/2);
    
    // Etiquetas de flechas (Opcional)
    ctx.font = '12px sans-serif';
    ctx.fillStyle = '#475569';
    // P->Rect: "+ 90°"
    ctx.fillText('+ Ángulos rectos', (topX+midLeftX)/2 - 40, (topY+midY)/2);
    // P->Rombo: "+ Lados iguales"
    ctx.fillText('+ Lados iguales', (topX+midRightX)/2 + 40, (topY+midY)/2);
  }

  // Ejecutar cuando RoughJS esté cargado o esperar un poco
  if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initJerarquia);
  } else {
      initJerarquia();
  }
</script>

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
