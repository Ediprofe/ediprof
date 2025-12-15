# Puntos Notables del Triángulo

Las rectas notables de un triángulo (medianas, alturas, bisectrices y mediatrices) se cortan en puntos especiales llamados **puntos notables**. Cada punto tiene propiedades geométricas únicas.

---

## 📖 Los cuatro puntos notables

| Punto | Intersección de | Característica principal |
|-------|-----------------|-------------------------|
| Baricentro (G) | Medianas | Centro de gravedad |
| Ortocentro (H) | Alturas | Depende del tipo de triángulo |
| Incentro (I) | Bisectrices | Centro de circunferencia inscrita |
| Circuncentro (O) | Mediatrices | Centro de circunferencia circunscrita |

---

## 📖 El Baricentro (G)

El **baricentro** es el punto donde se cortan las tres medianas del triángulo.

### Propiedades

1. **Siempre está dentro** del triángulo (sin importar el tipo)
2. Es el **centro de gravedad** o centro de masa del triángulo
3. Divide cada mediana en razón **2:1** desde el vértice

### La razón 2:1

Si $G$ es el baricentro y $M$ es el punto medio del lado opuesto al vértice $A$:

$$
\frac{AG}{GM} = \frac{2}{1}
$$

Esto significa que la distancia del vértice al baricentro es el **doble** de la distancia del baricentro al punto medio del lado.

### Ejemplo

Si la mediana $\overline{AM}$ mide 9 cm:
- $AG = \frac{2}{3} \times 9 = 6$ cm (del vértice al baricentro)
- $GM = \frac{1}{3} \times 9 = 3$ cm (del baricentro al punto medio)

**Ilustración: El baricentro divide cada mediana en razón 2:1:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-baricentro" style="width: 100%; height: 380px; min-height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-baricentro')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-baricentro', {
      boundingbox: [-1, 6, 9, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var Ax = 1, Ay = 0.5;
    var Bx = 7, By = 0.5;
    var Cx = 4, Cy = 5;
    
    var A = board.create('point', [Ax, Ay], {name: 'A', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [-10, -10]}});
    var B = board.create('point', [Bx, By], {name: 'B', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [5, -10]}});
    var C = board.create('point', [Cx, Cy], {name: 'C', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [0, 10]}});
    
    board.create('segment', [A, B], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
    board.create('segment', [B, C], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
    board.create('segment', [C, A], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
    
    // Punto medio de AB
    var M = board.create('point', [(Ax+Bx)/2, (Ay+By)/2], {name: 'M', size: 4, color: '#22c55e', fixed: true, label: {fontSize: 12, color: '#22c55e', offset: [0, -12]}});
    
    // Mediana CM
    board.create('segment', [C, M], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    
    // Baricentro
    var Gx = (Ax+Bx+Cx)/3;
    var Gy = (Ay+By+Cy)/3;
    var G = board.create('point', [Gx, Gy], {name: 'G', size: 5, color: '#ef4444', fixed: true, label: {fontSize: 13, color: '#ef4444', offset: [10, 5]}});
    
    // Etiquetas de segmentos
    board.create('text', [(Cx+Gx)/2 - 0.5, (Cy+Gy)/2 + 0.3, '2'], {fontSize: 14, color: '#3b82f6', fixed: true, fontWeight: 'bold'});
    board.create('text', [(Gx+M.X())/2 + 0.3, (Gy+M.Y())/2, '1'], {fontSize: 14, color: '#3b82f6', fixed: true, fontWeight: 'bold'});
    
    board.create('text', [4, -0.5, 'CG : GM = 2 : 1'], {fontSize: 13, color: '#1e293b', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
  }
});
</script>

### Coordenadas del baricentro

Si los vértices son $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$:

$$
G = \left( \frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3} \right)
$$

---

## 📖 El Ortocentro (H)

El **ortocentro** es el punto donde se cortan las tres alturas del triángulo.

### Propiedades

1. Su posición depende del **tipo de triángulo** (por ángulos)
2. En triángulos **acutángulos**: el ortocentro está **dentro**
3. En triángulos **obtusángulos**: el ortocentro está **fuera**
4. En triángulos **rectángulos**: el ortocentro coincide con el **vértice del ángulo recto**

### Ejemplo

En un triángulo rectángulo con el ángulo recto en $C$, el ortocentro es exactamente el punto $C$.

### Caso 1: Triángulo acutángulo → H está DENTRO

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-orto-acutangulo" style="width: 100%; height: 320px; min-height: 280px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-orto-acutangulo')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-orto-acutangulo', {
      boundingbox: [-1, 6, 9, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Vertices del triangulo acutangulo
    var Ax = 1, Ay = 0.5;
    var Bx = 7, By = 0.5;
    var Cx = 4, Cy = 5;
    
    // Funcion para calcular pie de altura
    function footOfAltitude(Px, Py, Qx, Qy, Rx, Ry) {
      var dx = Rx - Qx, dy = Ry - Qy;
      var t = ((Px - Qx) * dx + (Py - Qy) * dy) / (dx * dx + dy * dy);
      return [Qx + t * dx, Qy + t * dy];
    }
    
    // Pies de alturas
    var hA = footOfAltitude(Ax, Ay, Bx, By, Cx, Cy);
    var hB = footOfAltitude(Bx, By, Ax, Ay, Cx, Cy);
    var hC = footOfAltitude(Cx, Cy, Ax, Ay, Bx, By);
    
    // Ortocentro (calculado)
    var Hx = Ax + Bx + Cx - 2 * ((Ax+Bx)/2 + (Bx+Cx)/2 + (Cx+Ax)/2) / 3 * 0 + Cx;
    // Simplificado para este triangulo
    Hx = 4; var Hy = 2.1;
    
    // Triangulo
    var pA = board.create('point', [Ax, Ay], {name: 'A', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 12, offset: [-10, -10]}});
    var pB = board.create('point', [Bx, By], {name: 'B', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 12, offset: [5, -10]}});
    var pC = board.create('point', [Cx, Cy], {name: 'C', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 12, offset: [0, 10]}});
    
    board.create('polygon', [pA, pB, pC], {fillColor: '#dcfce7', fillOpacity: 0.3, borders: {strokeColor: '#22c55e', strokeWidth: 2}, fixed: true});
    
    // Alturas (lineas punteadas)
    board.create('segment', [[Ax, Ay], hA], {strokeColor: '#3b82f6', strokeWidth: 2, dash: 2, fixed: true});
    board.create('segment', [[Bx, By], hB], {strokeColor: '#3b82f6', strokeWidth: 2, dash: 2, fixed: true});
    board.create('segment', [[Cx, Cy], hC], {strokeColor: '#3b82f6', strokeWidth: 2, dash: 2, fixed: true});
    
    // Pies de altura
    board.create('point', hA, {name: '', size: 3, color: '#3b82f6', fixed: true});
    board.create('point', hB, {name: '', size: 3, color: '#3b82f6', fixed: true});
    board.create('point', hC, {name: '', size: 3, color: '#3b82f6', fixed: true});
    
    // Ortocentro
    board.create('point', [Hx, Hy], {name: 'H', size: 6, color: '#ef4444', fixed: true, label: {fontSize: 13, color: '#ef4444', offset: [8, 5]}});
    
    board.create('text', [4, -0.5, 'Triangulo acutangulo: H esta DENTRO'], {fontSize: 12, color: '#22c55e', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
  }
});
</script>

### Caso 2: Triángulo rectángulo → H está EN EL VÉRTICE del ángulo recto

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-orto-rectangulo" style="width: 100%; height: 320px; min-height: 280px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-orto-rectangulo')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-orto-rectangulo', {
      boundingbox: [-1, 6, 9, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Triangulo rectangulo (angulo recto en A)
    var Ax = 2, Ay = 0.5;
    var Bx = 7, By = 0.5;
    var Cx = 2, Cy = 4.5;
    
    // Triangulo
    var pA = board.create('point', [Ax, Ay], {name: 'A', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 12, offset: [-15, -10]}});
    var pB = board.create('point', [Bx, By], {name: 'B', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 12, offset: [5, -10]}});
    var pC = board.create('point', [Cx, Cy], {name: 'C', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 12, offset: [-15, 5]}});
    
    board.create('polygon', [pA, pB, pC], {fillColor: '#dbeafe', fillOpacity: 0.3, borders: {strokeColor: '#3b82f6', strokeWidth: 2}, fixed: true});
    
    // Simbolo de angulo recto
    board.create('segment', [[Ax + 0.4, Ay], [Ax + 0.4, Ay + 0.4]], {strokeColor: '#64748b', strokeWidth: 1.5, fixed: true});
    board.create('segment', [[Ax, Ay + 0.4], [Ax + 0.4, Ay + 0.4]], {strokeColor: '#64748b', strokeWidth: 1.5, fixed: true});
    
    // Alturas (los catetos SON las alturas, mas la altura a la hipotenusa)
    // Altura desde C a AB (el cateto CA es perpendicular a AB)
    board.create('segment', [[Cx, Cy], [Cx, Ay]], {strokeColor: '#ef4444', strokeWidth: 2, dash: 2, fixed: true});
    // Altura desde B a AC
    board.create('segment', [[Bx, By], [Ax, Ay]], {strokeColor: '#ef4444', strokeWidth: 2, dash: 2, fixed: true});
    
    // El ortocentro ES el vertice A
    board.create('point', [Ax, Ay], {name: 'H=A', size: 7, color: '#ef4444', fixed: true, label: {fontSize: 12, color: '#ef4444', offset: [10, -15]}});
    
    board.create('text', [4.5, -0.5, 'Triangulo rectangulo: H = vertice del angulo recto'], {fontSize: 12, color: '#3b82f6', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
  }
});
</script>

### Caso 3: Triángulo obtusángulo → H está FUERA

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-orto-obtusangulo" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-orto-obtusangulo')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-orto-obtusangulo', {
      boundingbox: [-1, 5, 10, -3],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Triangulo obtusangulo (angulo obtuso en A)
    var Ax = 2, Ay = 1;
    var Bx = 8, By = 1;
    var Cx = 1, Cy = 3;
    
    // Triangulo
    var pA = board.create('point', [Ax, Ay], {name: 'A', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 12, offset: [-5, -15]}});
    var pB = board.create('point', [Bx, By], {name: 'B', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 12, offset: [5, -10]}});
    var pC = board.create('point', [Cx, Cy], {name: 'C', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 12, offset: [-15, 5]}});
    
    board.create('polygon', [pA, pB, pC], {fillColor: '#fef3c7', fillOpacity: 0.3, borders: {strokeColor: '#f59e0b', strokeWidth: 2}, fixed: true});
    
    // Extension del lado AB (punteado, hacia la izquierda)
    board.create('segment', [[Ax, Ay], [-0.5, Ay]], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 3, fixed: true});
    
    // Extension del lado BC (punteado)
    board.create('segment', [[Cx, Cy], [Cx - 1, Cy + 0.5]], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 3, fixed: true});
    
    // Altura desde C a AB (cae dentro)
    board.create('segment', [[Cx, Cy], [Cx, Ay]], {strokeColor: '#3b82f6', strokeWidth: 2, dash: 2, fixed: true});
    board.create('point', [Cx, Ay], {name: '', size: 3, color: '#3b82f6', fixed: true});
    
    // Altura desde B a AC (extendido, cae fuera)
    // La prolongacion de AC pasa por debajo del triangulo
    board.create('segment', [[Bx, By], [0.5, -1]], {strokeColor: '#3b82f6', strokeWidth: 2, dash: 2, fixed: true});
    
    // Altura desde A a BC
    board.create('segment', [[Ax, Ay], [1.3, 2.4]], {strokeColor: '#3b82f6', strokeWidth: 2, dash: 2, fixed: true});
    
    // Ortocentro FUERA del triangulo
    var Hx = 0.8, Hy = -0.8;
    board.create('point', [Hx, Hy], {name: 'H', size: 6, color: '#ef4444', fixed: true, label: {fontSize: 13, color: '#ef4444', offset: [-15, -10]}});
    
    board.create('text', [4.5, -2.3, 'Triangulo obtusangulo: H esta FUERA del triangulo'], {fontSize: 12, color: '#f59e0b', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
  }
});
</script>

---

## 📖 El Incentro (I)

El **incentro** es el punto donde se cortan las tres bisectrices interiores del triángulo.

### Propiedades

1. **Siempre está dentro** del triángulo
2. Es **equidistante a los tres lados**
3. Es el centro de la **circunferencia inscrita** (la más grande que cabe dentro)

### El radio del incírculo

El radio de la circunferencia inscrita se llama **inradio** ($r$) y se calcula:

$$
r = \frac{\text{Área del triángulo}}{\text{Semiperímetro}}
$$

Donde el semiperímetro es $s = \frac{a + b + c}{2}$.

### Ejemplo

Si un triángulo tiene área $= 30$ cm² y semiperímetro $= 10$ cm:

$$
r = \frac{30}{10} = 3 \text{ cm}
$$

**Ilustración: El incentro y la circunferencia inscrita:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-incentro" style="width: 100%; height: 380px; min-height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-incentro')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-incentro', {
      boundingbox: [-1, 6, 9, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var Ax = 1, Ay = 0.5;
    var Bx = 7, By = 0.5;
    var Cx = 4, Cy = 5;
    
    var A = board.create('point', [Ax, Ay], {name: 'A', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [-10, -10]}});
    var B = board.create('point', [Bx, By], {name: 'B', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [5, -10]}});
    var C = board.create('point', [Cx, Cy], {name: 'C', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [0, 10]}});
    
    board.create('segment', [A, B], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
    board.create('segment', [B, C], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
    board.create('segment', [C, A], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
    
    // Calcular longitudes de lados
    function dist(x1, y1, x2, y2) {
      return Math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
    }
    var a = dist(Bx, By, Cx, Cy);
    var b = dist(Ax, Ay, Cx, Cy);
    var c = dist(Ax, Ay, Bx, By);
    
    // Incentro calculado
    var Ix = (a * Ax + b * Bx + c * Cx) / (a + b + c);
    var Iy = (a * Ay + b * By + c * Cy) / (a + b + c);
    
    // Inradio = Area / semiperimetro
    var s = (a + b + c) / 2;
    var area = Math.abs((Bx-Ax)*(Cy-Ay) - (Cx-Ax)*(By-Ay)) / 2;
    var inradius = area / s;
    
    var I = board.create('point', [Ix, Iy], {name: 'I', size: 5, color: '#a855f7', fixed: true, label: {fontSize: 13, color: '#a855f7', offset: [8, 5]}});
    
    // Circunferencia inscrita
    board.create('circle', [[Ix, Iy], inradius], {strokeColor: '#f59e0b', strokeWidth: 2, fillColor: '#fef3c7', fillOpacity: 0.3, fixed: true});
    
    board.create('text', [4, -0.5, 'I = Incentro (equidistante a los 3 lados)'], {fontSize: 12, color: '#a855f7', fixed: true, anchorX: 'middle'});
  }
});
</script>

---

## 📖 El Circuncentro (O)

El **circuncentro** es el punto donde se cortan las tres mediatrices del triángulo.

### Propiedades

1. Es **equidistante a los tres vértices**
2. Es el centro de la **circunferencia circunscrita** (la que pasa por los tres vértices)
3. Su posición depende del tipo de triángulo:
   - **Acutángulo**: dentro del triángulo
   - **Rectángulo**: en el punto medio de la hipotenusa
   - **Obtusángulo**: fuera del triángulo

### El radio del circuncírculo

El radio de la circunferencia circunscrita se llama **circunradio** ($R$).

### Ejemplo especial

En un triángulo rectángulo, el circuncentro está en el **punto medio de la hipotenusa**, y el circunradio es la **mitad de la hipotenusa**.

**Ilustración: El circuncentro y la circunferencia circunscrita:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-circuncentro" style="width: 100%; height: 380px; min-height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-circuncentro')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-circuncentro', {
      boundingbox: [-1, 7, 9, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var Ax = 1, Ay = 0.5;
    var Bx = 7, By = 0.5;
    var Cx = 4, Cy = 5;
    
    var A = board.create('point', [Ax, Ay], {name: 'A', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [-10, -10]}});
    var B = board.create('point', [Bx, By], {name: 'B', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [5, -10]}});
    var C = board.create('point', [Cx, Cy], {name: 'C', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [0, 10]}});
    
    board.create('segment', [A, B], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
    board.create('segment', [B, C], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
    board.create('segment', [C, A], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
    
    // Circuncentro calculado
    var D = 2 * (Ax*(By-Cy) + Bx*(Cy-Ay) + Cx*(Ay-By));
    var Ox = ((Ax*Ax+Ay*Ay)*(By-Cy) + (Bx*Bx+By*By)*(Cy-Ay) + (Cx*Cx+Cy*Cy)*(Ay-By)) / D;
    var Oy = ((Ax*Ax+Ay*Ay)*(Cx-Bx) + (Bx*Bx+By*By)*(Ax-Cx) + (Cx*Cx+Cy*Cy)*(Bx-Ax)) / D;
    var circumradius = Math.sqrt((Ax-Ox)*(Ax-Ox) + (Ay-Oy)*(Ay-Oy));
    
    var O = board.create('point', [Ox, Oy], {name: 'O', size: 5, color: '#f97316', fixed: true, label: {fontSize: 13, color: '#f97316', offset: [8, 5]}});
    
    // Circunferencia circunscrita
    board.create('circle', [[Ox, Oy], circumradius], {strokeColor: '#3b82f6', strokeWidth: 2, fillColor: '#dbeafe', fillOpacity: 0.2, fixed: true});
    
    // Radios a cada vértice
    board.create('segment', [[Ox, Oy], A], {strokeColor: '#22c55e', strokeWidth: 1, dash: 2, fixed: true});
    board.create('segment', [[Ox, Oy], B], {strokeColor: '#22c55e', strokeWidth: 1, dash: 2, fixed: true});
    board.create('segment', [[Ox, Oy], C], {strokeColor: '#22c55e', strokeWidth: 1, dash: 2, fixed: true});
    
    board.create('text', [4, -1.3, 'O = Circuncentro (equidistante a los 3 vertices)'], {fontSize: 12, color: '#f97316', fixed: true, anchorX: 'middle'});
  }
});
</script>

---

## 📖 Resumen de ubicaciones

| Tipo de triángulo | Baricentro | Ortocentro | Incentro | Circuncentro |
|-------------------|------------|------------|----------|--------------|
| Acutángulo | Dentro | Dentro | Dentro | Dentro |
| Rectángulo | Dentro | En vértice recto | Dentro | Medio de hipotenusa |
| Obtusángulo | Dentro | Fuera | Dentro | Fuera |

---

## 📖 La recta de Euler

En todo triángulo, tres de los puntos notables están **alineados**: el **Baricentro (G)**, el **Ortocentro (H)** y el **Circuncentro (O)**.

Esta recta se llama **recta de Euler**.

### Propiedad adicional

El baricentro $G$ divide el segmento $\overline{OH}$ en razón $1:2$:

$$
OG = \frac{1}{3} OH, \quad GH = \frac{2}{3} OH
$$

> **Nota:** El incentro generalmente NO está en la recta de Euler.

**Ilustración: La recta de Euler (G, H, O alineados):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-euler" style="width: 100%; height: 380px; min-height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-euler')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-euler', {
      boundingbox: [-1, 7, 10, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var Ax = 1, Ay = 0.5;
    var Bx = 8, By = 0.5;
    var Cx = 4.5, Cy = 5.5;
    
    var A = board.create('point', [Ax, Ay], {name: 'A', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [-10, -10]}});
    var B = board.create('point', [Bx, By], {name: 'B', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [5, -10]}});
    var C = board.create('point', [Cx, Cy], {name: 'C', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [0, 10]}});
    
    board.create('segment', [A, B], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
    board.create('segment', [B, C], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
    board.create('segment', [C, A], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
    
    // Circuncentro calculado
    var D = 2 * (Ax*(By-Cy) + Bx*(Cy-Ay) + Cx*(Ay-By));
    var Ox = ((Ax*Ax+Ay*Ay)*(By-Cy) + (Bx*Bx+By*By)*(Cy-Ay) + (Cx*Cx+Cy*Cy)*(Ay-By)) / D;
    var Oy = ((Ax*Ax+Ay*Ay)*(Cx-Bx) + (Bx*Bx+By*By)*(Ax-Cx) + (Cx*Cx+Cy*Cy)*(Bx-Ax)) / D;
    
    var O = board.create('point', [Ox, Oy], {name: 'O', size: 5, color: '#3b82f6', fixed: true, label: {fontSize: 12, color: '#3b82f6', offset: [-15, 5]}});
    
    // Baricentro calculado
    var Gx = (Ax+Bx+Cx)/3;
    var Gy = (Ay+By+Cy)/3;
    var G = board.create('point', [Gx, Gy], {name: 'G', size: 5, color: '#22c55e', fixed: true, label: {fontSize: 12, color: '#22c55e', offset: [8, 5]}});
    
    // Ortocentro calculado (H = A + B + C - 2*O para triángulo escaleno)
    var Hx = Ax + Bx + Cx - 2*Ox;
    var Hy = Ay + By + Cy - 2*Oy;
    var H = board.create('point', [Hx, Hy], {name: 'H', size: 5, color: '#ef4444', fixed: true, label: {fontSize: 12, color: '#ef4444', offset: [8, 5]}});
    
    // Recta de Euler
    board.create('line', [O, H], {strokeColor: '#a855f7', strokeWidth: 2, dash: 2, fixed: true});
    
    board.create('text', [5, -0.5, 'Recta de Euler: O, G y H estan alineados'], {fontSize: 12, color: '#a855f7', fixed: true, anchorX: 'middle'});
  }
});
</script>

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar puntos

Indica qué punto notable corresponde a cada descripción:

1. Centro de la circunferencia que pasa por los tres vértices
2. Punto donde se equilibra el triángulo en cartón
3. Punto equidistante a los tres lados
4. Intersección de las alturas

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Circuncentro**
2. **Baricentro**
3. **Incentro**
4. **Ortocentro**

</details>

---

### Ejercicio 2: Ubicación del ortocentro

¿Dónde está el ortocentro en cada caso?

1. Triángulo con ángulos 60°, 70°, 50°
2. Triángulo con ángulos 90°, 45°, 45°
3. Triángulo con ángulos 120°, 30°, 30°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Dentro** (es acutángulo, todos los ángulos < 90°)
2. **En el vértice del ángulo recto** (es rectángulo)
3. **Fuera** (es obtusángulo, tiene un ángulo > 90°)

</details>

---

### Ejercicio 3: Razón del baricentro

Si la mediana desde el vértice $A$ hasta el punto medio $M$ del lado opuesto mide 12 cm, calcula:

1. La distancia del vértice $A$ al baricentro $G$
2. La distancia del baricentro $G$ al punto medio $M$

<details>
<summary><strong>Ver respuestas</strong></summary>

El baricentro divide la mediana en razón 2:1.

1. $AG = \frac{2}{3} \times 12 = 8$ cm
2. $GM = \frac{1}{3} \times 12 = 4$ cm

</details>

---
