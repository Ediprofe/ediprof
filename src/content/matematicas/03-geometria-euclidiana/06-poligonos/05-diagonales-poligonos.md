# Diagonales de Polígonos

Una **diagonal** es un segmento que une dos vértices no consecutivos de un polígono. El número de diagonales depende del número de lados.

---

## 📖 ¿Qué es una diagonal?

> **Definición:** Una diagonal es un segmento que une dos vértices de un polígono que **no son adyacentes** (no son consecutivos).

### Ejemplo

En un cuadrilátero $ABCD$:
- $\overline{AC}$ es diagonal (une vértices no consecutivos)
- $\overline{BD}$ es diagonal (une vértices no consecutivos)
- $\overline{AB}$ **no** es diagonal (es un lado)

**Ilustración: ¿Qué es una Diagonal?**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-def-diagonal" style="width: 100%; height: 300px; min-height: 250px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initDefDiag() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-def-diagonal')) {
      setTimeout(initDefDiag, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-def-diagonal']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-def-diagonal', {
      boundingbox: [-1, 4, 5, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Cuadrilátero ABCD
    var A = board.create('point', [0, 0], {name:'A', size:3, color:'#1e293b', fixed:true});
    var B = board.create('point', [4, 0], {name:'B', size:3, color:'#1e293b', fixed:true});
    var C = board.create('point', [4, 3], {name:'C', size:3, color:'#1e293b', fixed:true});
    var D = board.create('point', [0, 3], {name:'D', size:3, color:'#1e293b', fixed:true});
    
    // Lados (azul, sólido)
    board.create('polygon', [A, B, C, D], {
        fillColor: '#dbeafe', fillOpacity:0.2,
        borders: {strokeColor: '#3b82f6', strokeWidth:2}
    });
    
    // Diagonales (rojo, punteadas)
    board.create('segment', [A, C], {strokeColor: '#ef4444', strokeWidth:2, dash:2});
    board.create('segment', [B, D], {strokeColor: '#ef4444', strokeWidth:2, dash:2});
    
    // Etiquetas
    board.create('text', [2, 1.5, 'Diagonales'], {fontSize:12, color:'#ef4444', fontWeight:'bold'});
    board.create('text', [2, -0.5, 'Lados = Azul (sólido)'], {fontSize:10, color:'#3b82f6', anchorX:'middle'});
  }
  
  initDefDiag();
})();
</script>

---

## 📖 Fórmula del número de diagonales

El número de diagonales de un polígono de $n$ lados es:

$$
d = \frac{n(n-3)}{2}
$$

### ¿De dónde viene esta fórmula?

- Desde cada vértice se pueden trazar $(n-3)$ diagonales
- Hay $n$ vértices
- Cada diagonal se cuenta dos veces (una desde cada extremo)
- Por lo tanto: $d = \frac{n(n-3)}{2}$

---

## 📖 Tabla de diagonales

| Polígono | n | Diagonales |
|----------|---|------------|
| Triángulo | 3 | $\frac{3(0)}{2} = 0$ |
| Cuadrilátero | 4 | $\frac{4(1)}{2} = 2$ |
| Pentágono | 5 | $\frac{5(2)}{2} = 5$ |
| Hexágono | 6 | $\frac{6(3)}{2} = 9$ |
| Heptágono | 7 | $\frac{7(4)}{2} = 14$ |
| Octágono | 8 | $\frac{8(5)}{2} = 20$ |
| Decágono | 10 | $\frac{10(7)}{2} = 35$ |
| Dodecágono | 12 | $\frac{12(9)}{2} = 54$ |

**Ilustración: Comparativa de Diagonales:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <canvas id="rough-comp-diagonales" width="800" height="600" style="width: 100%; height: auto; border-radius: 8px;"></canvas>
</div>

<script>
(function() {
  function initCompDiagRough() {
    if (typeof rough === 'undefined') {
      setTimeout(initCompDiagRough, 100);
      return;
    }
    
    const canvas = document.getElementById('rough-comp-diagonales');
    if (!canvas) {
      setTimeout(initCompDiagRough, 100);
      return;
    }
    
    const rc = rough.canvas(canvas);
    const ctx = canvas.getContext('2d');
    
    // Función para dibujar polígono con diagonales
    function drawPolygonWithDiagonals(cx, cy, n, label, diagCount) {
      const r = 80;
      const points = [];
      const startAngle = (n === 3) ? -Math.PI/2 : ((n === 4) ? -Math.PI/4 : Math.PI/10);
      
      // Calcular vértices
      for(let i=0; i<n; i++) {
        const ang = (2*Math.PI/n) * i + startAngle;
        points.push([cx + r*Math.cos(ang), cy + r*Math.sin(ang)]);
      }
      
      // Dibujar polígono
      rc.polygon(points, { 
        stroke: '#3b82f6', 
        strokeWidth: 2,
        fill: '#dbeafe',
        fillStyle: 'solid'
      });
      
      // Dibujar diagonales
      for(let i=0; i<n; i++) {
        for(let j=i+1; j<n; j++) {
          // Saltar lados
          if (j === i+1) continue;
          if (i === 0 && j === n-1) continue;
          
          // Dibujar diagonal
          rc.line(points[i][0], points[i][1], points[j][0], points[j][1], {
            stroke: '#ef4444',
            strokeWidth: 1.5,
            roughness: 1.5
          });
        }
      }
      
      // Etiquetas
      ctx.font = 'bold 16px Inter, sans-serif';
      ctx.fillStyle = '#1e3a8a';
      ctx.textAlign = 'center';
      ctx.fillText(label, cx, cy + r + 30);
      
      ctx.font = 'bold 14px Inter, sans-serif';
      ctx.fillStyle = '#ef4444';
      ctx.fillText('d = ' + diagCount, cx, cy + r + 55);
    }
    
    // Grid 2x2
    // Ajustamos coordenadas para que quepan las etiquetas
    // Canvas height aumentado a 600
    drawPolygonWithDiagonals(200, 130, 3, 'Triángulo (n=3)', 0);
    drawPolygonWithDiagonals(600, 130, 4, 'Cuadrilátero (n=4)', 2);
    drawPolygonWithDiagonals(200, 410, 5, 'Pentágono (n=5)', 5);
    drawPolygonWithDiagonals(600, 410, 6, 'Hexágono (n=6)', 9);
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCompDiagRough);
  } else {
    initCompDiagRough();
  }
})();
</script>

---

## 📖 Propiedad: Diagonales desde un vértice

Desde un vértice cualquiera se pueden trazar exactamente $(n-3)$ diagonales.

### ¿Por qué $(n-3)$?

De los $n$ vértices:
- No se puede unir consigo mismo (1 vértice)
- No se puede unir con los vértices adyacentes (2 vértices)
- Quedan $n - 3$ vértices disponibles

### Ejemplos

| Polígono | n | Diagonales desde un vértice |
|----------|---|----------------------------|
| Cuadrilátero | 4 | $4 - 3 = 1$ |
| Pentágono | 5 | $5 - 3 = 2$ |
| Hexágono | 6 | $6 - 3 = 3$ |
| Octágono | 8 | $8 - 3 = 5$ |

---

## 📖 División en triángulos

Las diagonales trazadas desde **un solo vértice** dividen al polígono en $(n-2)$ triángulos.

### Ejemplo

Un hexágono (6 lados):
- Diagonales desde un vértice: 3
- Triángulos formados: $6 - 2 = 4$

Esta propiedad es la base de la fórmula para la suma de ángulos interiores.

**Ilustración: Diagonales desde un Vértice:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-diag-vertice" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initDiagVert() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-diag-vertice')) {
      setTimeout(initDiagVert, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-diag-vertice']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-diag-vertice', {
      boundingbox: [-3, 4, 5, -3],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Pentágono
    var r = 2.5;
    var cx = 1, cy = 0.5;
    var points = [];
    for(var i=0; i<5; i++) {
        var ang = (72 * i + 18) * Math.PI / 180;
        points.push(board.create('point', [cx + r*Math.cos(ang), cy + r*Math.sin(ang)], {
            name: String.fromCharCode(65+i),
            size:3, color:'#1e293b', fixed:true
        }));
    }
    
    // Polígono
    var poly = board.create('polygon', points, {
        fillColor: 'none',
        borders: {strokeColor: '#3b82f6', strokeWidth:2}
    });
    
    // Diagonales desde A (points[0]) a C y D (points[2] y points[3])
    // n=5, n-3=2 diagonales
    board.create('segment', [points[0], points[2]], {strokeColor: '#ef4444', strokeWidth:2, dash:2});
    board.create('segment', [points[0], points[3]], {strokeColor: '#ef4444', strokeWidth:2, dash:2});
    
    // Colorear los 3 triángulos: ABC, ACD, ADE
    var colors = ['#bfdbfe', '#fef3c7', '#bbf7d0'];
    board.create('polygon', [points[0], points[1], points[2]], {
        fillColor: colors[0], fillOpacity:0.4, borders:{visible:false}
    });
    board.create('polygon', [points[0], points[2], points[3]], {
        fillColor: colors[1], fillOpacity:0.4, borders:{visible:false}
    });
    board.create('polygon', [points[0], points[3], points[4]], {
        fillColor: colors[2], fillOpacity:0.4, borders:{visible:false}
    });
    
    // Etiquetas
    board.create('text', [1, -2.2, 'Desde A: (n-3) = 2 diagonales'], {fontSize:11, fontWeight:'bold', color:'#1e3a8a', anchorX:'middle'});
    board.create('text', [1, -2.5, '(n-2) = 3 triángulos'], {fontSize:11, fontWeight:'bold', color:'#1e3a8a', anchorX:'middle'});
  }
  
  initDiagVert();
})();
</script>

---

## 📖 Todas las diagonales

Si trazamos **todas** las diagonales de un polígono convexo, el número de regiones internas puede ser muy grande.

Para un polígono convexo de $n$ lados, las diagonales pueden intersectarse en puntos internos, creando muchas regiones.

---

## 📖 Encontrar n conociendo las diagonales

Si conocemos el número de diagonales $d$, podemos encontrar $n$:

$$
d = \frac{n(n-3)}{2}
$$

$$
2d = n^2 - 3n
$$

$$
n^2 - 3n - 2d = 0
$$

Resolviendo con la fórmula cuadrática:

$$
n = \frac{3 + \sqrt{9 + 8d}}{2}
$$

### Ejemplo

Si $d = 20$:

$$
n = \frac{3 + \sqrt{9 + 160}}{2} = \frac{3 + \sqrt{169}}{2} = \frac{3 + 13}{2} = 8
$$

Es un **octágono**.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular diagonales

¿Cuántas diagonales tiene cada polígono?

1. Pentágono (5 lados)
2. Heptágono (7 lados)
3. Nonágono (9 lados)

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $d = \frac{5(5-3)}{2} = \frac{10}{2} = 5$
2. $d = \frac{7(7-3)}{2} = \frac{28}{2} = 14$
3. $d = \frac{9(9-3)}{2} = \frac{54}{2} = 27$

</details>

---

### Ejercicio 2: Diagonales desde un vértice

¿Cuántas diagonales se pueden trazar desde un vértice?

1. Hexágono
2. Decágono
3. Polígono de 15 lados

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $6 - 3 = 3$ diagonales
2. $10 - 3 = 7$ diagonales
3. $15 - 3 = 12$ diagonales

</details>

---

### Ejercicio 3: Encontrar el polígono

¿Cuántos lados tiene un polígono con...?

1. 9 diagonales
2. 35 diagonales
3. 44 diagonales

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\frac{n(n-3)}{2} = 9 \Rightarrow n(n-3) = 18 \Rightarrow n = 6$ (hexágono)
2. $\frac{n(n-3)}{2} = 35 \Rightarrow n(n-3) = 70 \Rightarrow n = 10$ (decágono)
3. $\frac{n(n-3)}{2} = 44 \Rightarrow n(n-3) = 88 \Rightarrow n = 11$ (endecágono)

</details>

---

### Ejercicio 4: Verdadero o Falso

1. Un triángulo tiene 0 diagonales.
2. Un cuadrilátero tiene 4 diagonales.
3. Desde cada vértice de un octágono se pueden trazar 5 diagonales.
4. Un pentágono tiene el mismo número de lados que de diagonales.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero** - No hay vértices no adyacentes
2. **Falso** - Tiene 2 diagonales
3. **Verdadero** - $8 - 3 = 5$
4. **Verdadero** - Tiene 5 lados y 5 diagonales

</details>

---
