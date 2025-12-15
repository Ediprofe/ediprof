# Clasificación de Polígonos

Los polígonos se clasifican de diversas maneras: por el número de lados, por la regularidad de sus elementos y por su forma (convexo o cóncavo).

---

## 📖 Clasificación por número de lados

### Polígonos básicos (3-6 lados)

| Lados | Nombre | Ejemplo común |
|-------|--------|---------------|
| 3 | Triángulo | Señales de precaución |
| 4 | Cuadrilátero | Ventanas, puertas |
| 5 | Pentágono | El Pentágono (edificio) |
| 6 | Hexágono | Celdas de panal |

### Polígonos intermedios (7-10 lados)

| Lados | Nombre | Ejemplo común |
|-------|--------|---------------|
| 7 | Heptágono | Algunas monedas |
| 8 | Octágono | Señal de PARE |
| 9 | Nonágono (o eneágono) | Poco común |
| 10 | Decágono | Algunas estrellas |

### Polígonos superiores (11-12 lados)

| Lados | Nombre |
|-------|--------|
| 11 | Endecágono (o undecágono) |
| 12 | Dodecágono |

### Polígonos de muchos lados

Para $n > 12$: "polígono de $n$ lados"

> **Nota:** A medida que $n$ aumenta, el polígono regular se parece más a un círculo.


**Ilustración: Polígonos según lados:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-poligonos-lados" style="width: 100%; height: 250px; min-height: 200px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initPolLados() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-poligonos-lados')) {
      setTimeout(initPolLados, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-poligonos-lados']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-poligonos-lados', {
      boundingbox: [-1, 3, 13, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Función aux para polígonos regulares
    function drawRegPoly(x, y, sides, color, label) {
        var r = 1;
        var points = [];
        for(var i=0; i<sides; i++) {
            var ang = (360/sides * i - 90 + (sides%2==0 ? 180/sides : 0)) * Math.PI / 180;
            points.push(board.create('point', [x + r*Math.cos(ang), y + r*Math.sin(ang)], {visible:false, fixed:true}));
        }
        board.create('polygon', points, {fillColor: color, borders:{strokeColor:'#334155'}});
        board.create('text', [x, -0.8, label], {anchorX:'middle', fontSize:11, color:'#334155'});
    }
    
    drawRegPoly(1.5, 1, 3, '#fca5a5', 'Triángulo (3)');
    drawRegPoly(4.5, 1, 4, '#fdba74', 'Cuadrilátero (4)');
    drawRegPoly(7.5, 1, 5, '#86efac', 'Pentágono (5)');
    drawRegPoly(10.5, 1, 6, '#93c5fd', 'Hexágono (6)');
  }
  
  initPolLados();
})();
</script>

## 📖 Clasificación por regularidad

### Polígono regular

Cumple **ambas** condiciones:
- **Equilátero**: todos los lados iguales
- **Equiángulo**: todos los ángulos iguales

### Polígono irregular

No cumple al menos una de las condiciones anteriores.

### Casos especiales

| Tipo | Lados | Ángulos | Ejemplo |
|------|-------|---------|---------|
| Regular | Iguales | Iguales | Cuadrado |
| Equilátero (no regular) | Iguales | Diferentes | Rombo |
| Equiángulo (no regular) | Diferentes | Iguales | Rectángulo |
| Irregular | Diferentes | Diferentes | Trapezoide |
| Equiángulo (no regular) | Diferentes | Iguales | Rectángulo |
| Irregular | Diferentes | Diferentes | Trapezoide |

**Ilustración: Grid de Regularidad:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-regularidad-matrix" style="width: 100%; height: 500px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initRegMatrix() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-regularidad-matrix')) {
      setTimeout(initRegMatrix, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-regularidad-matrix']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-regularidad-matrix', {
      boundingbox: [-1, 7, 7, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    var styleSolid = {fillColor: '#bfdbfe', borders: {strokeColor: '#2563eb', strokeWidth:2}};
    var styleLabel = {anchorX:'middle', fontSize:11};
    
    // 1. REGULAR (Top-Left, [0, 4] a [2, 6]) -> Cuadrado
    // (0,4) (2,4) (2,6) (0,6)
    var sq = board.create('polygon', [[0.5, 4], [2.5, 4], [2.5, 6], [0.5, 6]], styleSolid);
    board.create('text', [1.5, 3.5, 'REGULAR (Cuadrado)'], {...styleLabel, fontWeight:'bold', color: '#1e3a8a'});
    board.create('text', [1.5, 3.2, 'Lados =  |  Ángulos ='], {...styleLabel, fontSize:10, color: '#1e3a8a'});

    // 2. EQUILÁTERO (Top-Right, [3.8, 4] a [6.8, 6]) -> Rombo (Shifted right to avoid line overlap)
    var rhomb = board.create('polygon', [[5.3, 4], [6.8, 5], [5.3, 6], [3.8, 5]], {fillColor: '#fde047', borders: {strokeColor: '#ca8a04'}});
    board.create('text', [5.3, 3.5, 'EQUILÁTERO (Rombo)'], {...styleLabel, fontWeight:'bold', color: '#ca8a04'});
    board.create('text', [5.3, 3.2, 'Lados =  |  Ángulos ≠'], {...styleLabel, fontSize:10, color: '#ca8a04'});

    // 3. EQUIÁNGULO (Bottom-Left, [0, 0] a [2, 2]) -> Rectángulo
    var rect = board.create('polygon', [[0, 0.5], [3, 0.5], [3, 2], [0, 2]], {fillColor: '#bbf7d0', borders: {strokeColor: '#16a34a'}});
    board.create('text', [1.5, -0.5, 'EQUIÁNGULO (Rectángulo)'], {...styleLabel, fontWeight:'bold', color: '#16a34a'});
    board.create('text', [1.5, -0.8, 'Lados ≠  |  Ángulos ='], {...styleLabel, fontSize:10, color: '#16a34a'});

    // 4. IRREGULAR (Bottom-Right, [3, 0] a [6, 2]) -> Trapezoide
    var trapz = board.create('polygon', [[3.5, 0.5], [6, 0.8], [5.5, 2.5], [4, 2]], {fillColor: '#e2e8f0', borders: {strokeColor: '#475569'}});
    board.create('text', [4.75, -0.5, 'IRREGULAR (General)'], {...styleLabel, fontWeight:'bold', color: '#475569'});
    board.create('text', [4.75, -0.8, 'Lados ≠  |  Ángulos ≠'], {...styleLabel, fontSize:10, color: '#475569'});

    // Líneas divisorias
    board.create('segment', [[-1, 3], [7, 3]], {strokeColor: '#cbd5e1', dash:2});
    board.create('segment', [[3.25, -1], [3.25, 7]], {strokeColor: '#cbd5e1', dash:2});
  }
  
  initRegMatrix();
})();
</script>

## 📖 Clasificación por convexidad

### Polígono convexo

- Todos los ángulos interiores son **menores que 180°**
- Todas las diagonales quedan **dentro** del polígono
- Un segmento entre dos puntos internos siempre está dentro

### Polígono cóncavo

- Al menos un ángulo interior es **mayor que 180°** (reflejo)
- Al menos una diagonal pasa por **fuera** del polígono
- Tiene al menos una "entrada" o "hendidura"

---

## 📖 Polígonos regulares convexos

Solo existen polígonos regulares con 3 o más lados:

| n | Polígono regular | Ángulo interior |
|---|------------------|-----------------|
| 3 | Triángulo equilátero | 60° |
| 4 | Cuadrado | 90° |
| 5 | Pentágono regular | 108° |
| 6 | Hexágono regular | 120° |
| 8 | Octágono regular | 135° |
| 10 | Decágono regular | 144° |
| 12 | Dodecágono regular | 150° |

---

## 📖 Polígonos simples y complejos

### Polígono simple

Los lados **no se cruzan** entre sí (excepto en los vértices consecutivos).

### Polígono complejo (o cruzado)

Los lados **se cruzan** en puntos que no son vértices.

**Ejemplo:** Una estrella de 5 puntas trazada de un solo trazo es un polígono cruzado.

**Ilustración: Simple vs Complejo:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-simple-complejo" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initSimpleComp() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-simple-complejo')) {
      setTimeout(initSimpleComp, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-simple-complejo']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-simple-complejo', {
      boundingbox: [-2, 5, 12, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Función estrella (no usada ahora pero guardada por si acaso)
    function createStarPoints(cx, cy, r) {
        var points = [];
        var order = [0, 2, 4, 1, 3];
        for(var i=0; i<5; i++) {
            var idx = order[i];
            var ang = (72 * idx - 90) * Math.PI / 180;
            points.push([cx + r*Math.cos(ang), cy + r*Math.sin(ang)]);
        }
        return points;
    }

    // --- LEFT: SIMPLE (Heptágono Convexo) ---
    // Centrado en x=2
    var pSimple = [];
    var sx = 2, sy = 1, sr = 2;
    for(var i=0; i<7; i++) {
        var ang = (360/7 * i - 90) * Math.PI / 180;
        pSimple.push(board.create('point', [sx + sr*Math.cos(ang), sy + sr*Math.sin(ang)], {visible:false}));
    }
    board.create('polygon', pSimple, {fillColor: '#bbf7d0', borders: {strokeColor:'#22c55e'}});
    board.create('text', [sx, -1.5, 'SIMPLE'], {anchorX:'middle', fontWeight:'bold', color: '#166534'});
    board.create('text', [sx, -1.9, 'Lados no se cruzan'], {anchorX:'middle', fontSize:10, color: '#166534'});


    // --- RIGHT: COMPLEJO (Cuadrilátero Cruzado / Mariposa) ---
    // Centrado en x=9. Ancho total 4 (7 a 11). Fits in 12.
    // Vértices: A(7, 0), B(11, 0), C(7, 4), D(11, 4) -- NO, coordenadas relativas a cx
    
    var cx = 9, cy = 1.5;
    var w = 1.5; // Half width
    var h = 2;   // Half height
    var qA = board.create('point', [cx-w, cy-h], {visible:false}); // 7.5, -0.5
    var qB = board.create('point', [cx-w, cy+h], {visible:false}); // 7.5, 3.5
    var qC = board.create('point', [cx+w, cy-h], {visible:false}); // 10.5, -0.5
    var qD = board.create('point', [cx+w, cy+h], {visible:false}); // 10.5, 3.5
    
    // Polígono cruzado: Arriba-Izq -> Abajo-Der -> Arriba-Der -> Abajo-Izq
    // qB -> qC -> qD -> qA
    var polyComplex = board.create('polygon', [qB, qC, qD, qA], {
        fillColor: 'none', borders: {strokeColor:'#ef4444', strokeWidth:2}
    });
    
    board.create('text', [cx, -1.5, 'COMPLEJO (Cruzado)'], {anchorX:'middle', fontWeight:'bold', color: '#b91c1c'});
    
    // Marcar el cruce explícitamente
    // Intersección de AC y BD (según orden polígono) -> Lados qB-qC y qD-qA se cruzan? 
    // qB(7,3.5)->qC(11,-0.5) y qD(11,3.5)->qA(7,-0.5)
    // Se cruzan en el centro (9, 1.5)
    
    var intersection = board.create('point', [cx, 1.5], {name:'', size:4, color:'#b91c1c', fixed:true});
    board.create('text', [cx, 1.9, 'Cruce de lados'], {anchorX:'middle', color:'#b91c1c', fontSize:11, fontWeight:'bold'});
    board.create('text', [cx, 1.1, '(No es vértice)'], {anchorX:'middle', color:'#b91c1c', fontSize:10});

  }
  
  initSimpleComp();
})();
</script>

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Nombrar polígonos

¿Cómo se llama un polígono de...?

1. 5 lados
2. 7 lados
3. 8 lados
4. 12 lados

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Pentágono**
2. **Heptágono**
3. **Octágono**
4. **Dodecágono**

</details>

---

### Ejercicio 2: Clasificar por regularidad

¿Es regular, equilátero, equiángulo o irregular?

1. Un cuadrado
2. Un rombo con ángulos de 60° y 120°
3. Un rectángulo de 3 × 5
4. Un triángulo con lados 4, 5, 6

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Regular** (lados iguales y ángulos iguales)
2. **Equilátero** (lados iguales, ángulos diferentes)
3. **Equiángulo** (ángulos iguales, lados diferentes)
4. **Irregular** (lados y ángulos diferentes)

</details>

---

### Ejercicio 3: Convexo o cóncavo

1. Un hexágono regular
2. Una estrella de 6 puntas
3. Un pentágono con un ángulo de 200°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Convexo** (todos los ángulos < 180°)
2. **Cóncavo** (tiene ángulos > 180°)
3. **Cóncavo** (tiene un ángulo > 180°)

</details>

---

### Ejercicio 4: Completar la tabla

| Polígono | Lados | Regular | Convexo |
|----------|-------|---------|---------|
| Cuadrado | ? | ? | ? |
| Triángulo escaleno | 3 | ? | ? |
| Octágono regular | ? | ? | ? |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Polígono | Lados | Regular | Convexo |
|----------|-------|---------|---------|
| Cuadrado | **4** | **Sí** | **Sí** |
| Triángulo escaleno | 3 | **No** | **Sí** |
| Octágono regular | **8** | **Sí** | **Sí** |

</details>

---
