# Definición de Polígono

Un **polígono** es una figura geométrica plana formada por segmentos de recta que encierran una región. Los triángulos y cuadriláteros que ya estudiamos son casos particulares de polígonos.

---

## 📖 ¿Qué es un polígono?

> **Definición:** Un polígono es una figura plana cerrada formada por **tres o más segmentos de recta** llamados lados, que se unen solo en sus extremos.

### Condiciones para ser polígono

1. Figura **plana** (en 2D)
2. Figura **cerrada** (el último lado conecta con el primero)
3. Lados que son **segmentos de recta** (no curvas)
4. Los lados solo se tocan en los **vértices**

---

## 📖 Elementos de un polígono

| Elemento | Descripción |
|----------|-------------|
| Vértices | Puntos donde se unen dos lados |
| Lados | Segmentos que forman el contorno |
| Ángulos internos | Ángulos formados dentro del polígono |
| Ángulos externos | Suplementarios a los internos |
| Diagonales | Segmentos que unen vértices no consecutivos |

**Ilustración: Elementos del Polígono:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-elementos-poligono" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initElementosPol() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-elementos-poligono')) {
      setTimeout(initElementosPol, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-elementos-poligono']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-elementos-poligono', {
      boundingbox: [-3, 6, 9, -3],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Pentágono Irregular Convexo
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#1e293b', fixed: true, label:{offset:[-10,-10]}});
    var B = board.create('point', [5, -1], {name: 'B', size: 3, color: '#1e293b', fixed: true, label:{offset:[10,-10]}});
    var C = board.create('point', [7, 3], {name: 'C', size: 3, color: '#1e293b', fixed: true, label:{offset:[10,10]}});
    var D = board.create('point', [3, 5], {name: 'D', size: 3, color: '#1e293b', fixed: true, label:{offset:[0,10]}});
    var E = board.create('point', [-2, 3], {name: 'E', size: 3, color: '#1e293b', fixed: true, label:{offset:[-10,10]}});
    
    // Polígono
    board.create('polygon', [A, B, C, D, E], {
      fillColor: '#dbeafe', 
      fillOpacity: 0.5, 
      borders: {strokeColor: '#3b82f6', strokeWidth: 2}
    });

    // 1. Ángulo Interno (en D) - CCW: E -> D -> C (Por abajo, "dentro")
    board.create('angle', [E, D, C], {orthoType: 'sectordot', radius: 0.6, fillColor: '#22c55e', fillOpacity: 0.3});
    board.create('text', [3, 4, 'Ángulo Int.'], {fontSize: 10, color: '#166534', fixed: true, anchorX:'middle'});
    
    // 2. Ángulo Externo (en B)
    // Extender lado AB
    var extLine = board.create('line', [A, B], {visible: false, straightFirst:false, straightLast:true});
    // Punto auxiliar lejano en la recta
    var B_ext = board.create('point', [8, -1.6], {visible: false}); 
    board.create('segment', [B, B_ext], {strokeColor: '#94a3b8', dash: 2}); // Proyección
    
    // Ángulo Externo: A->B->C es interior. C->B->Ext es exterior
    board.create('angle', [B_ext, B, C], {radius: 0.7, fillColor: '#f59e0b', fillOpacity: 0.3});
    board.create('text', [6, -0.5, 'Ángulo Ext.'], {fontSize: 10, color: '#b45309', fixed: true});

    // 3. Diagonal (A -> C)
    board.create('segment', [A, C], {strokeColor: '#ef4444', strokeWidth: 2, dash: 2});
    board.create('text', [3.5, 1.5, 'Diagonal'], {fontSize: 10, color: '#ef4444', fixed: true, rotation: 25});

    // 4. Lado y Vértice etiquetas
    board.create('text', [-1, 1.5, 'Lado'], {fontSize: 11, color: '#3b82f6', fixed: true});
    board.create('text', [-2.2, 3.2, 'Vértice'], {fontSize: 11, color: '#1e293b', fixed: true, anchorX:'right'});
    
  }
  
  initElementosPol();
})();
</script>

---

## 📖 Notación

Un polígono se nombra con las letras de sus vértices en orden:

$$
\text{Polígono } ABCDE...
$$

El número de vértices = número de lados = número de ángulos.

---

## 📖 Nombres según el número de lados

| Lados | Nombre | Lados | Nombre |
|-------|--------|-------|--------|
| 3 | Triángulo | 8 | Octágono |
| 4 | Cuadrilátero | 9 | Nonágono |
| 5 | Pentágono | 10 | Decágono |
| 6 | Hexágono | 11 | Endecágono |
| 7 | Heptágono | 12 | Dodecágono |

Para polígonos con más lados: "polígono de $n$ lados" o "$n$-gono".

---

## 📖 Polígonos convexos y cóncavos

### Polígono convexo

- Todos los ángulos interiores son **menores que 180°**
- Todas las diagonales están **dentro** del polígono
- Un segmento que une dos puntos interiores está completamente dentro

### Polígono cóncavo

- Al menos un ángulo interior es **mayor que 180°**
- Al menos una diagonal está parcialmente **fuera** del polígono

**Ilustración: Convexo vs Cóncavo:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-convexo-concavo" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initConvConc() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-convexo-concavo')) {
      setTimeout(initConvConc, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-convexo-concavo']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-convexo-concavo', {
      boundingbox: [-1, 5, 12, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // --- IZQUIERDA: CONVEXO (Pentágono) ---
    var p1 = board.create('point', [0, 0], {fixed:true, visible:false});
    var p2 = board.create('point', [3, 0], {fixed:true, visible:false});
    var p3 = board.create('point', [4, 2], {fixed:true, visible:false});
    var p4 = board.create('point', [1.5, 4], {fixed:true, visible:false});
    var p5 = board.create('point', [-1, 2], {fixed:true, visible:false});
    
    var polyConvex = board.create('polygon', [p1, p2, p3, p4, p5], {
        fillColor: '#bbf7d0', borders: {strokeColor: '#22c55e'}
    });
    
    // Diagonal interna
    board.create('segment', [p5, p2], {strokeColor: '#166534', dash:2});
    board.create('text', [1.5, -1, 'CONVEXO'], {anchorX:'middle', fontWeight:'bold', color: '#166534'});
    board.create('text', [1.5, 1.5, 'Diagonales dentro'], {anchorX:'middle', fontSize:10, color: '#166534'});


    // --- DERECHA: CÓNCAVO (Flecha) ---
    var dx = 7; 
    var q1 = board.create('point', [dx+0, 0], {fixed:true, visible:false});
    var q2 = board.create('point', [dx+4, 2], {fixed:true, visible:false}); // Punta
    var q3 = board.create('point', [dx+0, 4], {fixed:true, visible:false});
    var q4 = board.create('point', [dx+1.5, 2], {fixed:true, visible:false, name:'V'}); // Vértice entrante
    
    // Polígono: q1 -> q2 -> q3 -> q4 -> q1 ?? No, orden correcto
    // Flecha de izq a derecha: Base en izq es q1-q4-q3? No, q1-q2-q3-q4
    
    var polyConcave = board.create('polygon', [q1, q2, q3, q4], {
        fillColor: '#fecaca', borders: {strokeColor: '#ef4444'}
    });
    
    // Diagonal EXTERNA (q1 a q3 pasa fuera si q4 está "adentro")
    board.create('segment', [q1, q3], {strokeColor: '#b91c1c', strokeWidth:2, dash:2});
    
    // Angulo > 180 (Interior en q4)
    // q3 -> q4 -> q1
    board.create('angle', [q3, q4, q1], {radius:0.4, fillColor:'#ef4444', fillOpacity:0.4});
    
    board.create('text', [dx+2, -1, 'CÓNCAVO'], {anchorX:'middle', fontWeight:'bold', color: '#b91c1c'});
    board.create('text', [dx+0.8, 2, '> 180°'], {anchorX:'right', fontSize:10, color: '#b91c1c'});
    board.create('text', [dx-0.2, 2, 'Diagonal fuera'], {anchorX:'right', fontSize:10, color: '#b91c1c', rotation: 90});

  }
  
  initConvConc();
})();
</script>

---

## 📖 Polígonos regulares e irregulares

### Polígono regular

- Todos los **lados son iguales** (equilátero)
- Todos los **ángulos son iguales** (equiángulo)

### Polígono irregular

- Los lados y/o ángulos **no son todos iguales**

> **Nota:** Un polígono puede ser equilátero sin ser regular (ej: rombo) o equiángulo sin ser regular (ej: rectángulo).

**Ilustración: Regular vs Irregular:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-reg-irreg" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initRegIrreg() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-reg-irreg')) {
      setTimeout(initRegIrreg, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-reg-irreg']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-reg-irreg', {
      boundingbox: [-2, 5, 12, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // --- IZQUIERDA: REGULAR (Hexágono) ---
    // Centro (1.5, 1.5), Radio 2
    var cx = 1.5, cy = 1.5, r = 2;
    var hexPoints = [];
    for(var i=0; i<6; i++) {
        var ang = (60 * i + 30) * Math.PI / 180;
        hexPoints.push(board.create('point', [cx + r*Math.cos(ang), cy + r*Math.sin(ang)], {visible:false, fixed:true}));
    }
    
    var polyReg = board.create('polygon', hexPoints, {
        fillColor: '#bfdbfe', borders: {strokeColor: '#3b82f6'}
    });
    
    // Ticks en todos los lados
    for(var i=0; i<6; i++) {
        board.create('ticks', [polyReg.borders[i]], {strokeColor: '#1e3a8a'});
    }
    
    board.create('text', [cx, -1, 'REGULAR'], {anchorX:'middle', fontWeight:'bold', color: '#1e3a8a'});
    board.create('text', [cx, cy, 'Simetría Total'], {anchorX:'middle', fontSize:10, color: '#1e3a8a'});


    // --- DERECHA: IRREGULAR (Hexágono deforme) ---
    var dx = 8, dy = 1.5;
    // Puntos aleatorios pero formando hexágono
    var irrPoints = [
        board.create('point', [dx+0, dy+2], {visible:false, fixed:true}),
        board.create('point', [dx-2, dy+0.5], {visible:false, fixed:true}),
        board.create('point', [dx-1, dy-2], {visible:false, fixed:true}),
        board.create('point', [dx+1, dy-1.5], {visible:false, fixed:true}),
        board.create('point', [dx+2.5, dy-1], {visible:false, fixed:true}),
        board.create('point', [dx+2, dy+1.5], {visible:false, fixed:true})
    ];
    
    var polyIrr = board.create('polygon', irrPoints, {
        fillColor: '#e2e8f0', borders: {strokeColor: '#64748b'}
    });
    
    board.create('text', [dx, -1, 'IRREGULAR'], {anchorX:'middle', fontWeight:'bold', color: '#475569'});
    board.create('text', [dx, dy, 'Sin Patrón'], {anchorX:'middle', fontSize:10, color: '#475569'});

  }
  
  initRegIrreg();
})();
</script>

---

## 📖 Ejemplos de polígonos regulares

| Polígono | Ángulo interior |
|----------|-----------------|
| Triángulo equilátero | 60° |
| Cuadrado | 90° |
| Pentágono regular | 108° |
| Hexágono regular | 120° |
| Octágono regular | 135° |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar y nombrar

¿Cuántos lados tienen estos polígonos y cómo se llaman?

1. Una señal de PARE
2. Un triángulo
3. Una figura con 5 lados
4. Una figura con 10 lados

<details>
<summary><strong>Ver respuestas</strong></summary>

1. 8 lados → **Octágono**
2. 3 lados → **Triángulo**
3. 5 lados → **Pentágono**
4. 10 lados → **Decágono**

</details>

---

### Ejercicio 2: Clasificar

Clasifica cada polígono como convexo o cóncavo:

1. Un cuadrado
2. Una estrella de 5 puntas
3. Un hexágono donde "entra" un vértice

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Convexo** (todos los ángulos < 180°)
2. **Cóncavo** (tiene ángulos > 180°)
3. **Cóncavo** (al menos un ángulo > 180°)

</details>

---

### Ejercicio 3: Regular o irregular

Indica si cada polígono es regular o irregular:

1. Un triángulo con lados 3, 3, 3 y ángulos 60°, 60°, 60°
2. Un rectángulo de 4 × 6
3. Un rombo con ángulos de 60° y 120°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Regular** (equilátero y equiángulo)
2. **Irregular** (equiángulo pero no equilátero)
3. **Irregular** (equilátero pero no equiángulo)

</details>

---

### Ejercicio 4: Verdadero o Falso

1. Todo polígono tiene el mismo número de lados que de vértices.
2. Un círculo es un polígono.
3. Un cuadrado es un polígono regular.
4. Todo polígono convexo tiene ángulos menores que 180°.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero**
2. **Falso** - El círculo no tiene lados rectos
3. **Verdadero** - Tiene lados y ángulos iguales
4. **Verdadero** - Por definición de convexo

</details>

---
