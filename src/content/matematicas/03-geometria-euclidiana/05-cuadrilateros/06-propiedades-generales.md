# Propiedades Generales de los Cuadriláteros

En esta lección resumimos las propiedades comunes a todos los cuadriláteros y comparamos las características de cada tipo.

---

## 📖 Propiedades comunes a todos los cuadriláteros

Todo cuadrilátero cumple:

| Propiedad | Valor/Descripción |
|-----------|-------------------|
| Número de lados | 4 |
| Número de vértices | 4 |
| Número de ángulos | 4 |
| Número de diagonales | 2 |
| Suma de ángulos interiores | 360° |
| Suma de ángulos exteriores | 360° |

### Ilustración: Elementos del Cuadrilátero

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-elementos" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initElementos() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-elementos')) {
      setTimeout(initElementos, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-elementos']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-elementos', {
      boundingbox: [-2, 6, 8, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos (Irregular convexo)
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#1e293b', fixed: true});
    var B = board.create('point', [6, 1], {name: 'B', size: 3, color: '#1e293b', fixed: true});
    var C = board.create('point', [5, 5], {name: 'C', size: 3, color: '#1e293b', fixed: true});
    var D = board.create('point', [1, 4], {name: 'D', size: 3, color: '#1e293b', fixed: true});
    
    // Polígono
    board.create('polygon', [A, B, C, D], {
      fillColor: '#dbeafe', 
      fillOpacity: 0.5, 
      borders: {strokeColor: '#3b82f6', strokeWidth: 2}
    });

    // Diagonales (Punteadas)
    board.create('segment', [A, C], {strokeColor: '#ef4444', strokeWidth: 2, dash: 2});
    board.create('segment', [B, D], {strokeColor: '#ef4444', strokeWidth: 2, dash: 2});
    
    // Ángulos Interiores (CCW)
    var angStyle = {orthoType: 'sectordot', radius: 0.5, fillColor: '#22c55e', fillOpacity: 0.3, strokeColor: '#166534'};
    board.create('angle', [B, A, D], { ...angStyle }); // A
    board.create('angle', [C, B, A], { ...angStyle }); // B
    board.create('angle', [D, C, B], { ...angStyle }); // C
    board.create('angle', [A, D, C], { ...angStyle }); // D
    
    // Etiquetas
    board.create('text', [3.5, 5.5, 'Vértices, Lados, Diagonales (rojas), Ángulos (verdes)'], {anchorX:'middle', fontSize:11, color:'#64748b', fixed:true});
  }
  
  initElementos();
})();
</script>

### Ilustración: Suma de Ángulos (360°)

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-suma-angulos" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initSuma() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-suma-angulos')) {
      setTimeout(initSuma, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-suma-angulos']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-suma-angulos', {
      boundingbox: [-2, 6, 8, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos (Irregular)
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#1e293b', fixed: true});
    var B = board.create('point', [7, 0.5], {name: 'B', size: 3, color: '#1e293b', fixed: true});
    var C = board.create('point', [5, 5], {name: 'C', size: 3, color: '#1e293b', fixed: true});
    var D = board.create('point', [1.5, 4], {name: 'D', size: 3, color: '#1e293b', fixed: true});
    
    // Dividir en 2 triángulos por diagonal AC
    // T1: ABC
    board.create('polygon', [A, B, C], {fillColor: '#bfdbfe', fillOpacity: 0.6, borders:{strokeColor: '#3b82f6'}});
    // T2: ADC
    board.create('polygon', [A, D, C], {fillColor: '#bbf7d0', fillOpacity: 0.6, borders:{strokeColor: '#22c55e'}});
    
    // Diagonal AC
    board.create('segment', [A, C], {strokeColor: '#64748b', strokeWidth: 2, dash: 2});

    // Etiquetas
    board.create('text', [4, 1.5, 'Suma = 180°'], {fontSize: 12, color: '#1e3a8a', anchorX:'middle'});
    board.create('text', [2, 3.5, 'Suma = 180°'], {fontSize: 12, color: '#14532d', anchorX:'middle'});
    
    board.create('text', [3.5, 5.5, 'Total = 180° + 180° = 360°'], {fontSize: 14, fontWeight:'bold', color: '#1e293b', anchorX:'middle', fixed:true});
  }
  
  initSuma();
})();
</script>

---

## 📖 Fórmula de diagonales

Para un polígono de $n$ lados, el número de diagonales es:

$$
d = \frac{n(n-3)}{2}
$$

Para un cuadrilátero ($n = 4$):

$$
d = \frac{4(4-3)}{2} = \frac{4}{2} = 2
$$

---

## 📖 Jerarquía de cuadriláteros

**Ilustración: Jerarquía de Cuadriláteros:**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="rough-jerarquia-cuad" width="800" height="500" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script src="https://unpkg.com/roughjs@4.6.6/bundled/rough.js"></script>
<script>
  function initJerarquiaCuad() {
     if (typeof rough === 'undefined') {
        setTimeout(initJerarquiaCuad, 100);
        return;
    }
    const canvas = document.getElementById('rough-jerarquia-cuad');
    if (!canvas) {
        setTimeout(initJerarquiaCuad, 100);
        return;
    }
    const rc = rough.canvas(canvas);
    const ctx = canvas.getContext('2d');
    
    // Limpiar
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Conf
    const cardW = 120;
    const cardH = 40;
    const colorFill = '#f1f5f9';
    const colorStroke = '#1e293b';
    
    function drawBox(x, y, label, bg) {
        rc.rectangle(x - cardW/2, y - cardH/2, cardW, cardH, {
            fill: bg || colorFill, fillStyle: 'solid', roughness: 0.5, stroke: colorStroke
        });
        ctx.font = 'bold 13px sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = '#1e293b';
        ctx.fillText(label, x, y);
    }
    
    function connect(x1, y1, x2, y2) {
        rc.line(x1, y1, x2, y2, {stroke: '#64748b', roughness: 0.5});
    }

    // Nivel 0: Cuadrilátero
    const midX = 400;
    drawBox(midX, 30, 'CUADRILÁTERO', '#e2e8f0');
    
    // Nivel 1: Paralelogramo, Trapecio, Trapezoide
    const y1 = 120;
    const xPara = 150;
    const xTrap = 400;
    const xTrapz = 650;
    
    drawBox(xPara, y1, 'Paralelogramo', '#dbeafe');
    drawBox(xTrap, y1, 'Trapecio', '#dbeafe');
    drawBox(xTrapz, y1, 'Trapezoide', '#dbeafe');
    
    connect(midX, 50, xPara, y1 - 20);
    connect(midX, 50, xTrap, y1 - 20);
    connect(midX, 50, xTrapz, y1 - 20);
    
    // Nivel 2 (Bajo Paralelogramo): Rectángulo, Rombo
    const y2 = 220;
    const xRect = 80;
    const xRombo = 220;
    drawBox(xRect, y2, 'Rectángulo', '#bfdbfe');
    drawBox(xRombo, y2, 'Rombo', '#bfdbfe');
    connect(xPara, y1+20, xRect, y2-20);
    connect(xPara, y1+20, xRombo, y2-20);
    
    // Nivel 3 (Bajo Rect/Rombo): Cuadrado
    const y3 = 320;
    const xCuad = 150;
    drawBox(xCuad, y3, 'Cuadrado', '#60a5fa');
    connect(xRect, y2+20, xCuad, y3-20);
    connect(xRombo, y2+20, xCuad, y3-20);
    
    // Nivel 2 (Bajo Trapecio): Isósceles, Rectángulo, Escaleno
    drawBox(xTrap - 80, y2, 'Isósceles', '#e2e8f0');
    drawBox(xTrap, y2, 'Rectángulo', '#e2e8f0');
    drawBox(xTrap + 80, y2, 'Escaleno', '#e2e8f0');
    connect(xTrap, y1+20, xTrap-80, y2-20);
    connect(xTrap, y1+20, xTrap, y2-20);
    connect(xTrap, y1+20, xTrap+80, y2-20);
    
    // Nivel 2 (Bajo Trapezoide): Deltoide
    drawBox(xTrapz, y2, 'Deltoide', '#e2e8f0');
    connect(xTrapz, y1+20, xTrapz, y2-20);
    
  }

  if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initJerarquiaCuad);
  } else {
      initJerarquiaCuad();
  }
</script>

---

## 📖 Tabla comparativa de diagonales

| Cuadrilátero | Se bisecan | Iguales | Perpendiculares |
|--------------|------------|---------|-----------------|
| Paralelogramo | ✓ | ✗ | ✗ |
| Rectángulo | ✓ | ✓ | ✗ |
| Rombo | ✓ | ✗ | ✓ |
| Cuadrado | ✓ | ✓ | ✓ |
| Trapecio isósceles | ✗ | ✓ | ✗ |
| Deltoide | ✗ (una biseca a otra) | ✗ | ✓ |

---

## 📖 Tabla comparativa de propiedades

| Cuadrilátero | Lados paralelos | Lados iguales | Ángulos rectos |
|--------------|-----------------|---------------|----------------|
| Cuadrado | 2 pares | Todos (4) | Todos (4) |
| Rectángulo | 2 pares | Opuestos | Todos (4) |
| Rombo | 2 pares | Todos (4) | Ninguno* |
| Paralelogramo | 2 pares | Opuestos | Ninguno* |
| Trapecio | 1 par | Depende | Depende |
| Trapezoide | Ninguno | Depende | Depende |

*Excepto casos especiales

---

## 📖 Áreas de cuadriláteros

| Cuadrilátero | Fórmula del área |
|--------------|------------------|
| Cuadrado | $A = l^2$ |
| Rectángulo | $A = b \times h$ |
| Rombo | $A = \frac{d_1 \times d_2}{2}$ |
| Paralelogramo | $A = b \times h$ |
| Trapecio | $A = \frac{(B + b) \times h}{2}$ |
| Deltoide | $A = \frac{d_1 \times d_2}{2}$ |

---

## 📖 Perímetros

| Cuadrilátero | Fórmula del perímetro |
|--------------|----------------------|
| Cuadrado | $P = 4l$ |
| Rectángulo | $P = 2(a + b)$ |
| Rombo | $P = 4l$ |
| Paralelogramo | $P = 2(a + b)$ |
| Trapecio | $P = B + b + l_1 + l_2$ |
| General | $P = $ suma de los 4 lados |

---

## 📖 Criterios de clasificación

### Por lados paralelos

1. **2 pares paralelos** → Paralelogramo
2. **1 par paralelo** → Trapecio
3. **0 pares paralelos** → Trapezoide

### Por lados iguales

1. **4 lados iguales** → Rombo (o cuadrado)
2. **2 pares de lados iguales (opuestos)** → Paralelogramo
3. **2 pares de lados iguales (consecutivos)** → Deltoide

### Por ángulos

1. **4 ángulos rectos** → Rectángulo (o cuadrado)
2. **2 ángulos rectos** → Trapecio rectángulo
3. **Ningún ángulo recto** → Otros

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificar por propiedades

Identifica el cuadrilátero:

1. 4 lados iguales y 4 ángulos rectos
2. 2 pares de lados paralelos, lados opuestos iguales, sin ángulos rectos
3. 1 par de lados paralelos, lados no paralelos iguales
4. 4 lados iguales, sin ángulos rectos

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Cuadrado**
2. **Paralelogramo** (general)
3. **Trapecio isósceles**
4. **Rombo**

</details>

---

### Ejercicio 2: Propiedades de diagonales

¿En cuáles cuadriláteros las diagonales son perpendiculares?

<details>
<summary><strong>Ver respuesta</strong></summary>

- **Rombo**
- **Cuadrado**
- **Deltoide**

</details>

---

### Ejercicio 3: Verdadero o Falso

1. Todo cuadrado es un paralelogramo.
2. Todo paralelogramo es un cuadrado.
3. Las diagonales de todo cuadrilátero suman 360°.
4. Un trapecio puede tener dos ángulos rectos.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero** - El cuadrado tiene 2 pares de lados paralelos
2. **Falso** - Se necesitan 4 lados iguales y 4 ángulos rectos
3. **Falso** - Esta propiedad es de los ángulos, no de las diagonales
4. **Verdadero** - Es el trapecio rectángulo

</details>

---

### Ejercicio 4: Completar la tabla

| Cuadrilátero | Lados | Ángulos | Diagonales |
|--------------|-------|---------|------------|
| Cuadrado | 4 iguales | 4 de 90° | ? |
| Rombo | 4 iguales | ? | Perpendiculares |
| Rectángulo | ? | 4 de 90° | Iguales |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Cuadrilátero | Lados | Ángulos | Diagonales |
|--------------|-------|---------|------------|
| Cuadrado | 4 iguales | 4 de 90° | **Iguales y perpendiculares** |
| Rombo | 4 iguales | **Opuestos iguales** | Perpendiculares |
| Rectángulo | **Opuestos iguales** | 4 de 90° | Iguales |

</details>

---
