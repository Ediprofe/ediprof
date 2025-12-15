# Puntos Notables del Triángulo

Las rectas notables (medianas, alturas, bisectrices, mediatrices) se cortan en 4 puntos clave.

## ⚡ Conceptos Clave

| Punto | Rectas | Característica |
|---|---|---|
| **Baricentro (G)** | Medianas | Centro de Gravedad (2:1) |
| **Ortocentro (H)** | Alturas | Puede caer FUERA del triángulo |
| **Incentro (I)** | Bisectrices | Centro del círculo INSCRITO |
| **Circuncentro (O)** | Mediatrices | Centro del círculo CIRCUNSCRITO |

---

## 1. El Baricentro (G)

Es la intersección de las **Medianas**.

> **📝 ¿Qué es una Mediana?**
> Es la línea que une un **vértice** con el **punto medio** del lado opuesto.

El baricentro es el **centro de gravedad**. Si sostienes el triángulo por este punto, se mantiene en equilibrio.

### Propiedad Clave: Regla 2 a 1
Divide la mediana en dos partes proporcionales:
*   La parte larga (vértice a $G$) mide el **doble** que la corta.

> **⚙️ Ejemplo:**
> Si la mediana mide 9 cm:
> *   Lado largo ($AG$): 6 cm
> *   Lado corto ($GM$): 3 cm

**Ilustración: El baricentro divide cada mediana en razón 2:1:**

<div id="jxgbox-baricentro" class="jxgbox" style="width:100%; height:350px; border-radius:12px; border:1px solid #cbd5e1; background:#f8fafc;"></div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jxgbox-baricentro', {boundingbox: [-1, 6, 9, -1], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}});
  var A = board.create('point', [1, 0.5], {name: 'A', fixed: true, size: 4, color: '#1e293b'});
  var B = board.create('point', [7, 0.5], {name: 'B', fixed: true, size: 4, color: '#1e293b'});
  var C = board.create('point', [4, 5], {name: 'C', fixed: true, size: 4, color: '#1e293b'});
  board.create('polygon', [A,B,C], {borders: {strokeColor: '#334155', strokeWidth: 2}, fillColor: '#f1f5f9', highlight: false});
  // Midpoints manual calc
  var M_AB = board.create('point', [(A.X()+B.X())/2, (A.Y()+B.Y())/2], {name: '', size: 2, color: '#94a3b8', fixed: true});
  var M_BC = board.create('point', [(B.X()+C.X())/2, (B.Y()+C.Y())/2], {name: '', size: 2, color: '#94a3b8', fixed: true});
  var M_CA = board.create('point', [(C.X()+A.X())/2, (C.Y()+A.Y())/2], {name: '', size: 2, color: '#94a3b8', fixed: true});
  // Medians (Green)
  board.create('segment', [C, M_AB], {strokeColor: '#16a34a', strokeWidth: 2, dash: 2});
  board.create('segment', [A, M_BC], {strokeColor: '#16a34a', strokeWidth: 2, dash: 2});
  board.create('segment', [B, M_CA], {strokeColor: '#16a34a', strokeWidth: 2, dash: 2});
  // Baricentro
  var G = board.create('point', [(A.X()+B.X()+C.X())/3, (A.Y()+B.Y()+C.Y())/3], {name: 'G', size: 5, color: '#dc2626', fixed: true, label: {offset: [10,0]}});
});
</script>

### Coordenadas del baricentro

Si los vértices son $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$:

$$
G = \left( \frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3} \right)
$$

---

## 2. El Ortocentro (H)

Es la intersección de las **Alturas**.

> **📝 ¿Qué es una Altura?**
> Es la línea que baja desde un **vértice** perpendicularmente ($90^\circ$) al lado opuesto (o su prolongación).

Su ubicación depende totalmente del tipo de triángulo:

> **⚙️ Ejemplo de Identificación:**
> En un triángulo rectángulo ($90^\circ$), el Ortocentro es **el mismo vértice del ángulo recto**.

### 1. Acutángulo (Dentro)
Cae **dentro** del triángulo.

<div id="jxgbox-acute" class="jxgbox" style="width:100%; height:320px; border-radius:12px; border:1px solid #cbd5e1; background:#f8fafc;"></div>
<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jxgbox-acute', {boundingbox: [-1, 5, 8, -1], axis: false, showCopyright: false, showNavigation: false});
  var A = board.create('point', [2, 4], {name:'A', fixed:true, size:3, color:'#1e293b'});
  var B = board.create('point', [0, 0], {name:'B', fixed:true, size:3, color:'#1e293b'});
  var C = board.create('point', [6, 0], {name:'C', fixed:true, size:3, color:'#1e293b'});
  board.create('polygon', [A,B,C], {fillColor:'#f1f5f9', borders:{strokeColor:'#1e293b'}});
  // Helper: Foot of altitude from P to segment QR
  function getFoot(P, Q, R) {
    var dx = R.X() - Q.X(), dy = R.Y() - Q.Y();
    var t = ((P.X() - Q.X()) * dx + (P.Y() - Q.Y()) * dy) / (dx * dx + dy * dy);
    return [Q.X() + t * dx, Q.Y() + t * dy];
  }
  var Fa = board.create('point', getFoot(A, B, C), {size:0, visible:false});
  var Fb = board.create('point', getFoot(B, A, C), {size:0, visible:false});
  var Fc = board.create('point', getFoot(C, A, B), {size:0, visible:false});
  // Altitudes (Orange)
  board.create('segment', [A, Fa], {strokeColor:'#ea580c', strokeWidth:2, dash:2});
  board.create('segment', [B, Fb], {strokeColor:'#ea580c', strokeWidth:2, dash:2});
  board.create('segment', [C, Fc], {strokeColor:'#ea580c', strokeWidth:2, dash:2});
  // Orthocentro (Intersection)
  var H = board.create('intersection', [board.create('line', [A, Fa], {visible:false}), board.create('line', [B, Fb], {visible:false})], {name:'H', size:4, color:'#ea580c', fixed:true});
});
</script>


### 2. Rectángulo (En el Vértice)
Coincide con el **vértice del ángulo recto**.

<div id="jxgbox-right" class="jxgbox" style="width:100%; height:320px; border-radius:12px; border:1px solid #cbd5e1; background:#f8fafc;"></div>
<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jxgbox-right', {boundingbox: [-1, 5, 8, -1], axis: false, showCopyright: false, showNavigation: false});
  var A = board.create('point', [0, 4], {name:'A', fixed:true, size:3, color:'#1e293b'});
  var B = board.create('point', [0, 0], {name:'B = H', fixed:true, size:5, color:'#ea580c', label:{offset:[10,10]}}); // Right angle at B
  var C = board.create('point', [6, 0], {name:'C', fixed:true, size:3, color:'#1e293b'});
  board.create('polygon', [A,B,C], {fillColor:'#f1f5f9', borders:{strokeColor:'#1e293b'}});
  // Right angle symbol
  board.create('curve', [[0, 0.5], [0.5, 0.5], [0.5, 0]], {strokeColor:'black', strokeWidth:1});
  var H = B; // H is B
  // Altitudes are legs
  board.create('segment', [A, B], {strokeColor:'#ea580c', strokeWidth:3});
  board.create('segment', [C, B], {strokeColor:'#ea580c', strokeWidth:3});
  // Altitude from B to AC
  function getFoot(P, Q, R) {
    var dx = R.X() - Q.X(), dy = R.Y() - Q.Y();
    var t = ((P.X() - Q.X()) * dx + (P.Y() - Q.Y()) * dy) / (dx * dx + dy * dy);
    return [Q.X() + t * dx, Q.Y() + t * dy];
  }
  var Fb = board.create('point', getFoot(B, A, C), {visible:false});
  board.create('segment', [B, Fb], {strokeColor:'#ea580c', strokeWidth:2, dash:2});
});
</script>

### 3. Obtusángulo (Fuera)
Cae **fuera** del triángulo (en la prolongación de los lados).

<div id="jxgbox-obtuse" class="jxgbox" style="width:100%; height:400px; border-radius:12px; border:1px solid #cbd5e1; background:#f8fafc;"></div>
<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jxgbox-obtuse', {boundingbox: [-3, 6, 9, -2], axis: false, showCopyright: false, showNavigation: false});
  var A = board.create('point', [1, 4], {name:'A', fixed:true, size:3, color:'#1e293b'});
  var B = board.create('point', [4, 4], {name:'B', fixed:true, size:3, color:'#1e293b'});
  var C = board.create('point', [0, 0], {name:'C', fixed:true, size:3, color:'#1e293b'});
  board.create('polygon', [A,B,C], {fillColor:'#f1f5f9', borders:{strokeColor:'#1e293b'}});
  // Helper
  function getFoot(P, Q, R) {
    var dx = R.X() - Q.X(), dy = R.Y() - Q.Y();
    var t = ((P.X() - Q.X()) * dx + (P.Y() - Q.Y()) * dy) / (dx * dx + dy * dy);
    return [Q.X() + t * dx, Q.Y() + t * dy];
  }
  // Feet
  var Fa = board.create('point', getFoot(A, B, C), {visible:false});
  var Fb = board.create('point', getFoot(B, A, C), {visible:false});
  var Fc = board.create('point', getFoot(C, A, B), {visible:false});
  // Extensions
  board.create('line', [B, C], {strokeColor:'#94a3b8', strokeWidth:1, dash:3});
  board.create('line', [A, C], {strokeColor:'#94a3b8', strokeWidth:1, dash:3});
  board.create('line', [A, B], {strokeColor:'#94a3b8', strokeWidth:1, dash:3});
  // Altitudes
  var lA = board.create('line', [A, Fa], {strokeColor:'#ea580c', strokeWidth:1, dash:2});
  var lB = board.create('line', [B, Fb], {strokeColor:'#ea580c', strokeWidth:1, dash:2});
  var lC = board.create('line', [C, Fc], {strokeColor:'#ea580c', strokeWidth:1, dash:2});
  // H
  var H = board.create('intersection', [lA, lB], {name:'H', size:4, color:'#ea580c', fixed:true});
});
</script>

---

## 3. El Incentro (I)

Es la intersección de las **Bisectrices**.

> **📝 ¿Qué es una Bisectriz?**
> Es la semirrecta que divide un **ángulo** en dos partes iguales.

### Propiedad Clave
Está a la **misma distancia de los tres lados**.
Esto permite dibujar una circunferencia que toca los 3 lados por dentro (**Inscrita**).

> **⚙️ Ejemplo:**
> Si el incentro está a 5 cm del lado base, también está a 5 cm de los otros dos lados.

**Ilustración: El incentro y la circunferencia inscrita:**

<div id="jxgbox-incenter" class="jxgbox" style="width:100%; height:350px; border-radius:12px; border:1px solid #cbd5e1; background:#f8fafc;"></div>
<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jxgbox-incenter', {boundingbox: [-1, 6, 9, -1], axis: false, showCopyright: false, showNavigation: false});
  var A = board.create('point', [1, 0.5], {name:'A', fixed:true, color:'#1e293b'});
  var B = board.create('point', [7, 0.5], {name:'B', fixed:true, color:'#1e293b'});
  var C = board.create('point', [4, 5], {name:'C', fixed:true, color:'#1e293b'});
  board.create('polygon', [A,B,C], {fillColor:'#f1f5f9'});
  // Calc lengths
  function d(P1, P2) { return Math.sqrt(Math.pow(P1.X()-P2.X(), 2) + Math.pow(P1.Y()-P2.Y(), 2)); }
  var la = d(B,C), lb = d(A,C), lc = d(A,B);
  // Incenter
  var Ix = (la*A.X() + lb*B.X() + lc*C.X()) / (la+lb+lc);
  var Iy = (la*A.Y() + lb*B.Y() + lc*C.Y()) / (la+lb+lc);
  var I = board.create('point', [Ix, Iy], {name:'I', size:4, color:'#9333ea', fixed:true});
  // Bisectors (dashed purple)
  board.create('segment', [A,I], {strokeColor:'#9333ea', dash:2});
  board.create('segment', [B,I], {strokeColor:'#9333ea', dash:2});
  board.create('segment', [C,I], {strokeColor:'#9333ea', dash:2});
  // Incircle
  var s = (la+lb+lc)/2;
  var area = Math.abs((B.X()-A.X())*(C.Y()-A.Y()) - (C.X()-A.X())*(B.Y()-A.Y())) / 2;
  var r = area/s;
  board.create('circle', [I, r], {strokeColor:'#9333ea', fillColor:'#9333ea', fillOpacity:0.1});
});
</script>

---

## 4. El Circuncentro (O)

Es la intersección de las **Mediatrices**.

> **📝 ¿Qué es una Mediatriz?**
> Es la recta perpendicular ($90^\circ$) que pasa por el **punto medio** de un lado.
> *(Ojo: No necesariamente sale de un vértice).*

### Propiedad Clave
Está a la **misma distancia de los tres vértices**.
Esto permite dibujar una circunferencia que pasa por las 3 esquinas (**Circunscrita**).

> **⚙️ Ejemplo:**
> En un triángulo rectángulo, el circuncentro siempre es el **punto medio de la hipotenusa**.

**Ilustración: El circuncentro y la circunferencia circunscrita:**

<div id="jxgbox-circumcenter" class="jxgbox" style="width:100%; height:400px; border-radius:12px; border:1px solid #cbd5e1; background:#f8fafc;"></div>
<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jxgbox-circumcenter', {boundingbox: [-1, 7, 9, -2], axis: false, showCopyright: false, showNavigation: false});
  var A = board.create('point', [0.5, 1], {name:'A', fixed:true, color:'#1e293b'});
  var B = board.create('point', [7.5, 1], {name:'B', fixed:true, color:'#1e293b'});
  var C = board.create('point', [3, 5], {name:'C', fixed:true, color:'#1e293b'});
  board.create('polygon', [A,B,C], {fillColor:'#f1f5f9'});
  // Circumcenter Calc
  var D = 2 * (A.X()*(B.Y()-C.Y()) + B.X()*(C.Y()-A.Y()) + C.X()*(A.Y()-B.Y()));
  var Ox = ((A.X()*A.X()+A.Y()*A.Y())*(B.Y()-C.Y()) + (B.X()*B.X()+B.Y()*B.Y())*(C.Y()-A.Y()) + (C.X()*C.X()+C.Y()*C.Y())*(A.Y()-B.Y())) / D;
  var Oy = ((A.X()*A.X()+A.Y()*A.Y())*(C.X()-B.X()) + (B.X()*B.X()+B.Y()*B.Y())*(A.X()-C.X()) + (C.X()*C.X()+C.Y()*C.Y())*(B.X()-A.X())) / D;
  var O = board.create('point', [Ox, Oy], {name:'O', size:4, color:'#be123c', fixed:true});
  // Circumcircle
  board.create('circle', [O, A], {strokeColor:'#be123c', fillColor:'#be123c', fillOpacity:0.05});
  // Mediatrices (Perpendicular Bisectors) - Pink
  var M_AB = board.create('point', [(A.X()+B.X())/2, (A.Y()+B.Y())/2], {visible:false});
  var M_BC = board.create('point', [(B.X()+C.X())/2, (B.Y()+C.Y())/2], {visible:false});
  var M_CA = board.create('point', [(C.X()+A.X())/2, (C.Y()+A.Y())/2], {visible:false});
  board.create('line', [O, M_AB], {strokeColor:'#be123c', dash:2, strokeWidth:1});
  board.create('line', [O, M_BC], {strokeColor:'#be123c', dash:2, strokeWidth:1});
  board.create('line', [O, M_CA], {strokeColor:'#be123c', dash:2, strokeWidth:1});
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

## 5. La Recta de Euler

En la mayoría de triángulos, tres puntos están **alineados en una recta**:
1.  **O**rtocentro
2.  **B**aricentro
3.  **C**ircuncentro

> **Nota:** El Incentro NO suele estar en esta recta.

**Ilustración: La recta de Euler (G, H, O alineados):**

<div id="jxgbox-euler" class="jxgbox" style="width:100%; height:350px; border-radius:12px; border:1px solid #cbd5e1; background:#f8fafc;"></div>
<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jxgbox-euler', {boundingbox: [-1, 7, 10, -1], axis: false, showCopyright: false, showNavigation: false});
  var A = board.create('point', [1, 1], {name:'A', fixed:true, color:'#1e293b'});
  var B = board.create('point', [9, 1], {name:'B', fixed:true, color:'#1e293b'});
  var C = board.create('point', [3, 6], {name:'C', fixed:true, color:'#1e293b'});
  board.create('polygon', [A,B,C], {fillColor:'#f1f5f9'});
  // Calc G
  var Gx = (A.X()+B.X()+C.X())/3, Gy = (A.Y()+B.Y()+C.Y())/3;
  var G = board.create('point', [Gx, Gy], {name:'G', size:4, color:'#16a34a', fixed:true});
  // Calc O
  var D = 2 * (A.X()*(B.Y()-C.Y()) + B.X()*(C.Y()-A.Y()) + C.X()*(A.Y()-B.Y()));
  var Ox = ((A.X()*A.X()+A.Y()*A.Y())*(B.Y()-C.Y()) + (B.X()*B.X()+B.Y()*B.Y())*(C.Y()-A.Y()) + (C.X()*C.X()+C.Y()*C.Y())*(A.Y()-B.Y())) / D;
  var Oy = ((A.X()*A.X()+A.Y()*A.Y())*(C.X()-B.X()) + (B.X()*B.X()+B.Y()*B.Y())*(A.X()-C.X()) + (C.X()*C.X()+C.Y()*C.Y())*(B.X()-A.X())) / D;
  var O = board.create('point', [Ox, Oy], {name:'O', size:4, color:'#be123c', fixed:true});
  // Calc H (Euler relation: O, G, Hcollinear, HG = 2GO => H = 3G - 2O)
  var Hx = 3*Gx - 2*Ox;
  var Hy = 3*Gy - 2*Oy;
  var H = board.create('point', [Hx, Hy], {name:'H', size:4, color:'#ea580c', fixed:true});
  // Euler Line
  board.create('line', [O, H], {strokeColor:'#7c3aed', strokeWidth:2, dash:2});
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
