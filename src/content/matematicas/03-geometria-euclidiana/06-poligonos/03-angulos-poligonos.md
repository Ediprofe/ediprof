# Ángulos en Polígonos

Los ángulos de un polígono siguen reglas matemáticas precisas. Conociendo el número de lados, podemos calcular la suma de los ángulos interiores y exteriores.

---

## 📖 Suma de ángulos interiores

> **Fórmula:** La suma de los ángulos interiores de un polígono de $n$ lados es:

$$
S = (n - 2) \times 180°
$$

### ¿Por qué funciona esta fórmula?

Desde un vértice podemos trazar diagonales que dividen el polígono en $(n-2)$ triángulos. Como cada triángulo tiene ángulos que suman 180°:

$$
\text{Suma total} = (n-2) \times 180°
$$

**Ilustración: Triangulación (Suma de Ángulos):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-suma-interiores" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initSumaInt() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-suma-interiores')) {
      setTimeout(initSumaInt, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-suma-interiores']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-suma-interiores', {
      boundingbox: [-2, 4, 6, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Hexágono Regular
    var r = 2.5;
    var center = [2, 1];
    var points = [];
    for(var i=0; i<6; i++) {
        var ang = (60 * i) * Math.PI / 180;
        points.push(board.create('point', [center[0] + r*Math.cos(ang), center[1] + r*Math.sin(ang)], {
            name: String.fromCharCode(65+i), 
            fixed:true, 
            label:{offset:[10,10]}
        }));
    }
    
    // Polígono base
    var poly = board.create('polygon', points, {
        fillColor: '#dbeafe', borders: {strokeColor: '#3b82f6', strokeWidth:2}
    });

    // Diagonales desde A (points[0]) a C, D, E (points[2,3,4])
    var A = points[0]; 
    var diag1 = board.create('segment', [A, points[2]], {strokeColor: '#ef4444', dash:2});
    var diag2 = board.create('segment', [A, points[3]], {strokeColor: '#ef4444', dash:2});
    var diag3 = board.create('segment', [A, points[4]], {strokeColor: '#ef4444', dash:2});
    
    // Etiquetas de Triángulos (en el centroide de cada triángulo)
    // Triángulo 1 (ABC): centroide en área derecha-superior
    board.create('text', [2.8, 2.4, '1'], {color:'#ef4444', fontSize:14, fontWeight:'bold'});
    // Triángulo 2 (ACD): centroide en área superior-izquierda
    board.create('text', [1.6, 1.7, '2'], {color:'#ef4444', fontSize:14, fontWeight:'bold'});
    // Triángulo 3 (ADE): centroide en área izquierda
    board.create('text', [1.6, 0.3, '3'], {color:'#ef4444', fontSize:14, fontWeight:'bold'});
    // Triángulo 4 (AEF): centroide en área inferior-derecha
    board.create('text', [2.8, -0.4, '4'], {color:'#ef4444', fontSize:14, fontWeight:'bold'});
    
    board.create('text', [2, -1.5, 'Hexágono (n=6)'], {anchorX:'middle', fontWeight:'bold', color: '#1e3a8a'});
    board.create('text', [2, -1.8, '4 Triángulos × 180° = 720°'], {anchorX:'middle', fontSize:11, color: '#1e3a8a'});
  }
  
  initSumaInt();
})();
</script>

### Ejemplos

| Polígono | n | Suma de ángulos |
|----------|---|-----------------|
| Triángulo | 3 | $(3-2) \times 180° = 180°$ |
| Cuadrilátero | 4 | $(4-2) \times 180° = 360°$ |
| Pentágono | 5 | $(5-2) \times 180° = 540°$ |
| Hexágono | 6 | $(6-2) \times 180° = 720°$ |
| Octágono | 8 | $(8-2) \times 180° = 1080°$ |

---

## 📖 Ángulo interior de un polígono regular

En un polígono **regular**, todos los ángulos son iguales. Cada ángulo mide:

$$
\alpha = \frac{(n-2) \times 180°}{n}
$$

### Ejemplos

| Polígono regular | n | Ángulo interior |
|------------------|---|-----------------|
| Triángulo equilátero | 3 | $\frac{180°}{3} = 60°$ |
| Cuadrado | 4 | $\frac{360°}{4} = 90°$ |
| Pentágono | 5 | $\frac{540°}{5} = 108°$ |
| Hexágono | 6 | $\frac{720°}{6} = 120°$ |
| Octágono | 8 | $\frac{1080°}{8} = 135°$ |

---

## 📖 Suma de ángulos exteriores

> **Propiedad:** La suma de los ángulos exteriores de cualquier polígono convexo es siempre **360°**.

$$
\text{Suma de ángulos exteriores} = 360°
$$

Esta propiedad es válida para **todos** los polígonos convexos, sin importar el número de lados.

**Ilustración: Suma Ángulos Exteriores (360°):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-suma-exteriores" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initSumaExt() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-suma-exteriores')) {
      setTimeout(initSumaExt, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-suma-exteriores']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-suma-exteriores', {
      boundingbox: [-3, 5, 7, -3],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Pentágono Regular
    var r = 2;
    var center = [2, 1];
    var points = [];
    for(var i=0; i<5; i++) {
        var ang = (72 * i + 18) * Math.PI / 180;
        points.push(board.create('point', [center[0] + r*Math.cos(ang), center[1] + r*Math.sin(ang)], {visible:false})); 
    }
    
    var poly = board.create('polygon', points, {
        fillColor: '#fef3c7', borders: {strokeColor: '#d97706', strokeWidth:2}
    });

    // Dibujar ángulos exteriores (Molinillo)
    var colors = ['#ef4444', '#f97316', '#eab308', '#22c55e', '#3b82f6'];
    
    for(var i=0; i<5; i++) {
        var pCurr = points[i];
        var pPrev = points[(i-1+5)%5];
        var pNext = points[(i+1)%5];
        
        var pExt = board.create('point', [
            pCurr.X() + 0.6*(pCurr.X() - pPrev.X()), 
            pCurr.Y() + 0.6*(pCurr.Y() - pPrev.Y())
        ], {visible:false});
        
        board.create('segment', [pCurr, pExt], {strokeColor: '#94a3b8', dash:2});
        
        board.create('angle', [pExt, pCurr, pNext], {
            radius: 0.5, fillColor: colors[i], fillOpacity:0.6, name: '' 
        });
    }

    board.create('text', [2, -2, 'Suma de Exteriores = 360°'], {anchorX:'middle', fontWeight:'bold', color: '#d97706'});
  }
  
  initSumaExt();
})();
</script>

---

## 📖 Ángulo exterior de un polígono regular

En un polígono regular, cada ángulo exterior mide:

$$
\beta = \frac{360°}{n}
$$

### Ejemplos

| Polígono regular | n | Ángulo exterior |
|------------------|---|-----------------|
| Triángulo equilátero | 3 | $\frac{360°}{3} = 120°$ |
| Cuadrado | 4 | $\frac{360°}{4} = 90°$ |
| Pentágono | 5 | $\frac{360°}{5} = 72°$ |
| Hexágono | 6 | $\frac{360°}{6} = 60°$ |
| Octágono | 8 | $\frac{360°}{8} = 45°$ |

---

## 📖 Relación ángulo interior - exterior

El ángulo interior y el ángulo exterior en cada vértice son **suplementarios**:

$$
\alpha + \beta = 180°
$$

### Verificación

Para un hexágono regular:
- Ángulo interior: $120°$
- Ángulo exterior: $60°$
- Suma: $120° + 60° = 180°$ ✓

**Ilustración: Relación Interior-Exterior:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-relacion-int-ext" style="width: 100%; height: 250px; min-height: 200px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initRelIntExt() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-relacion-int-ext')) {
      setTimeout(initRelIntExt, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-relacion-int-ext']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-relacion-int-ext', {
      boundingbox: [-2, 3, 8, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Zoom en un vértice de un hexágono
    var A = board.create('point', [0, 0], {visible:false});
    var B = board.create('point', [4, 0], {name:'Vértice', size:4, color:'#1e293b', fixed:true, label:{offset:[0,-15]}});
    var C = board.create('point', [6, 3.46], {visible:false});
    
    // Lados (parciales)
    board.create('segment', [A, B], {strokeColor: '#3b82f6', strokeWidth:3});
    board.create('segment', [B, C], {strokeColor: '#3b82f6', strokeWidth:3});
    
    // Extensión
    var B_ext = board.create('point', [7, 0], {visible:false});
    board.create('segment', [B, B_ext], {strokeColor: '#94a3b8', dash:2});
    
    // Ángulo Interior (120 para hex)
    board.create('angle', [C, B, A], {
        radius: 1, fillColor: '#22c55e', fillOpacity: 0.3,
        name: 'Interior (α)'
    });
    
    // Ángulo Exterior (60)
    board.create('angle', [B_ext, B, C], {
        radius: 0.8, fillColor: '#f97316', fillOpacity: 0.3,
        name: 'Exterior (β)'
    });
    
    board.create('text', [3, -1.2, 'Interior (α) + Exterior (β) = 180°'], {fontSize:12, fontWeight:'bold', color: '#1e293b'});
  }
  
  initRelIntExt();
})();
</script>

---

## 📖 Encontrar el número de lados

Si conocemos un ángulo, podemos encontrar $n$:

### Conociendo el ángulo interior

$$
n = \frac{360°}{180° - \alpha}
$$

### Conociendo el ángulo exterior

$$
n = \frac{360°}{\beta}
$$

### Ejemplo

Si el ángulo exterior de un polígono regular es $30°$:

$$
n = \frac{360°}{30°} = 12 \text{ lados (dodecágono)}
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Suma de ángulos interiores

Calcula la suma de los ángulos interiores:

1. Pentágono (5 lados)
2. Heptágono (7 lados)
3. Decágono (10 lados)

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $(5-2) \times 180° = 3 \times 180° = 540°$
2. $(7-2) \times 180° = 5 \times 180° = 900°$
3. $(10-2) \times 180° = 8 \times 180° = 1440°$

</details>

---

### Ejercicio 2: Ángulo interior de polígono regular

Calcula el ángulo interior de:

1. Pentágono regular
2. Nonágono regular (9 lados)
3. Dodecágono regular (12 lados)

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\frac{540°}{5} = 108°$
2. $\frac{(9-2) \times 180°}{9} = \frac{1260°}{9} = 140°$
3. $\frac{(12-2) \times 180°}{12} = \frac{1800°}{12} = 150°$

</details>

---

### Ejercicio 3: Ángulo exterior

Calcula el ángulo exterior de cada polígono regular:

1. Hexágono (6 lados)
2. Decágono (10 lados)

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\frac{360°}{6} = 60°$
2. $\frac{360°}{10} = 36°$

</details>

---

### Ejercicio 4: Encontrar el número de lados

¿Cuántos lados tiene un polígono regular si...?

1. Su ángulo exterior es $40°$
2. Su ángulo interior es $156°$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $n = \frac{360°}{40°} = 9$ lados (nonágono)
2. Ángulo exterior = $180° - 156° = 24°$, entonces $n = \frac{360°}{24°} = 15$ lados

</details>

---

### Ejercicio 5: Problema

Un polígono regular tiene ángulos interiores de $144°$. ¿Cuántos lados tiene y cuál es la suma de sus ángulos interiores?

<details>
<summary><strong>Ver respuesta</strong></summary>

Ángulo exterior = $180° - 144° = 36°$

$$
n = \frac{360°}{36°} = 10 \text{ lados (decágono)}
$$

Suma de ángulos = $(10-2) \times 180° = 1440°$

</details>

---
