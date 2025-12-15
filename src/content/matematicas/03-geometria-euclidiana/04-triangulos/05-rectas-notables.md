# Rectas Notables del Triángulo

En todo triángulo existen cuatro tipos de rectas especiales llamadas **rectas notables**: medianas, alturas, bisectrices y mediatrices. Cada una tiene propiedades únicas y aplicaciones importantes.

---

## 📖 Las cuatro rectas notables

| Recta | Definición | Se traza desde |
|-------|------------|----------------|
| Mediana | Une un vértice con el punto medio del lado opuesto | Vértice → punto medio |
| Altura | Perpendicular desde un vértice al lado opuesto | Vértice → lado (⊥) |
| Bisectriz | Divide un ángulo en dos partes iguales | Vértice → lado opuesto |
| Mediatriz | Perpendicular al punto medio de un lado | Punto medio de lado (⊥) |

---

## 📖 Medianas

Una **mediana** es el segmento que une un **vértice** con el **punto medio** del lado opuesto.

### Propiedades de las medianas

1. Todo triángulo tiene **3 medianas** (una desde cada vértice)
2. Las tres medianas se cortan en un único punto llamado **baricentro**
3. Cada mediana divide al triángulo en dos triángulos de **igual área**
4. El baricentro divide cada mediana en razón $2:1$ (desde el vértice)

### Fórmula del baricentro

Si los vértices son $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$:

$$
G = \left( \frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3} \right)
$$

### Aplicación

El baricentro es el **centro de gravedad** del triángulo. Si recortamos un triángulo de cartón, podemos equilibrarlo en la punta de un lápiz colocándolo en el baricentro.

**Las tres medianas y el baricentro G (calculado):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-medianas" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-medianas')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-medianas', {
      boundingbox: [-1, 7, 9, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Vertices del triangulo
    var A = [1, 1], B = [7, 1], C = [4, 6];
    
    // Puntos medios (calculados)
    var mBC = [(B[0]+C[0])/2, (B[1]+C[1])/2];
    var mAC = [(A[0]+C[0])/2, (A[1]+C[1])/2];
    var mAB = [(A[0]+B[0])/2, (A[1]+B[1])/2];
    
    // Baricentro (calculado)
    var G = [(A[0]+B[0]+C[0])/3, (A[1]+B[1]+C[1])/3];
    
    // Dibujar triangulo
    var pA = board.create('point', A, {name: 'A', size: 5, fixed: true, color: '#1e293b', label: {fontSize: 13, offset: [-15, -10]}});
    var pB = board.create('point', B, {name: 'B', size: 5, fixed: true, color: '#1e293b', label: {fontSize: 13, offset: [10, -10]}});
    var pC = board.create('point', C, {name: 'C', size: 5, fixed: true, color: '#1e293b', label: {fontSize: 13, offset: [0, 10]}});
    
    board.create('segment', [pA, pB], {strokeColor: '#1e293b', strokeWidth: 2});
    board.create('segment', [pB, pC], {strokeColor: '#1e293b', strokeWidth: 2});
    board.create('segment', [pC, pA], {strokeColor: '#1e293b', strokeWidth: 2});
    
    // Puntos medios
    var pmBC = board.create('point', mBC, {name: '', size: 4, fixed: true, color: '#22c55e'});
    var pmAC = board.create('point', mAC, {name: '', size: 4, fixed: true, color: '#22c55e'});
    var pmAB = board.create('point', mAB, {name: '', size: 4, fixed: true, color: '#22c55e'});
    
    // Medianas
    board.create('segment', [pA, pmBC], {strokeColor: '#22c55e', strokeWidth: 2.5});
    board.create('segment', [pB, pmAC], {strokeColor: '#22c55e', strokeWidth: 2.5});
    board.create('segment', [pC, pmAB], {strokeColor: '#22c55e', strokeWidth: 2.5});
    
    // Baricentro
    board.create('point', G, {name: 'G', size: 7, fixed: true, color: '#ef4444', label: {fontSize: 14, color: '#ef4444', offset: [10, 5]}});
    
    board.create('text', [4, -0.3, 'G = Baricentro = ((x1+x2+x3)/3, (y1+y2+y3)/3)'], {fontSize: 11, color: '#ef4444', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Alturas

Una **altura** es el segmento **perpendicular** trazado desde un **vértice** hasta el lado opuesto (o su prolongación).

### Propiedades de las alturas

1. Todo triángulo tiene **3 alturas**
2. Las tres alturas se cortan en un punto llamado **ortocentro**
3. En un triángulo **acutángulo**, el ortocentro está **dentro** del triángulo
4. En un triángulo **obtusángulo**, el ortocentro está **fuera** del triángulo
5. En un triángulo **rectángulo**, el ortocentro está en el **vértice del ángulo recto**

### Aplicación

La altura es esencial para calcular el **área** del triángulo:

$$
\text{Área} = \frac{base \times altura}{2}
$$

**Las tres alturas y el ortocentro H (calculado):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-alturas" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-alturas')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-alturas', {
      boundingbox: [-1, 7, 9, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Vertices
    var A = [1, 1], B = [7, 1], C = [4, 6];
    
    // Funcion para proyectar punto P sobre linea definida por Q-R
    function footOfAltitude(P, Q, R) {
      var dx = R[0] - Q[0];
      var dy = R[1] - Q[1];
      var t = ((P[0] - Q[0]) * dx + (P[1] - Q[1]) * dy) / (dx * dx + dy * dy);
      return [Q[0] + t * dx, Q[1] + t * dy];
    }
    
    // Pies de las alturas (calculados)
    var hA = footOfAltitude(A, B, C);
    var hB = footOfAltitude(B, A, C);
    var hC = footOfAltitude(C, A, B);
    
    // Ortocentro (interseccion de alturas) - calculado
    // Para triangulo con base horizontal en y=1 y vertice superior
    var H = [C[0], A[1] + (C[0] - A[0]) * (C[0] - B[0]) / (C[1] - A[1])];
    // Simplificado para este triangulo: H esta en x=4
    H = [4, 1 + (4-1)*(4-7)/(6-1) * (-1)];
    H = [4, 2.8];
    
    // Dibujar triangulo
    var pA = board.create('point', A, {name: 'A', size: 5, fixed: true, color: '#1e293b', label: {fontSize: 13, offset: [-15, -10]}});
    var pB = board.create('point', B, {name: 'B', size: 5, fixed: true, color: '#1e293b', label: {fontSize: 13, offset: [10, -10]}});
    var pC = board.create('point', C, {name: 'C', size: 5, fixed: true, color: '#1e293b', label: {fontSize: 13, offset: [0, 10]}});
    
    board.create('segment', [pA, pB], {strokeColor: '#1e293b', strokeWidth: 2});
    board.create('segment', [pB, pC], {strokeColor: '#1e293b', strokeWidth: 2});
    board.create('segment', [pC, pA], {strokeColor: '#1e293b', strokeWidth: 2});
    
    // Alturas (segmentos perpendiculares)
    board.create('segment', [A, hA], {strokeColor: '#3b82f6', strokeWidth: 2.5});
    board.create('segment', [B, hB], {strokeColor: '#3b82f6', strokeWidth: 2.5});
    board.create('segment', [C, hC], {strokeColor: '#3b82f6', strokeWidth: 2.5});
    
    // Pies de altura
    board.create('point', hA, {name: '', size: 3, fixed: true, color: '#3b82f6'});
    board.create('point', hB, {name: '', size: 3, fixed: true, color: '#3b82f6'});
    board.create('point', hC, {name: '', size: 3, fixed: true, color: '#3b82f6'});
    
    // Ortocentro
    board.create('point', H, {name: 'H', size: 7, fixed: true, color: '#ef4444', label: {fontSize: 14, color: '#ef4444', offset: [10, 5]}});
    
    board.create('text', [4, -0.3, 'H = Ortocentro (interseccion de alturas)'], {fontSize: 11, color: '#ef4444', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Bisectrices

Una **bisectriz** es el rayo que divide un **ángulo** del triángulo en dos ángulos **iguales**.

### Propiedades de las bisectrices

1. Todo triángulo tiene **3 bisectrices interiores**
2. Las tres bisectrices se cortan en un punto llamado **incentro**
3. El incentro es equidistante a los tres lados
4. El incentro es el centro de la **circunferencia inscrita** en el triángulo

### Fórmula del incentro

Si los lados opuestos a $A$, $B$, $C$ miden $a$, $b$, $c$:

$$
I = \left( \frac{a \cdot x_A + b \cdot x_B + c \cdot x_C}{a+b+c}, \frac{a \cdot y_A + b \cdot y_B + c \cdot y_C}{a+b+c} \right)
$$

### Aplicación

La circunferencia inscrita es la circunferencia más grande que cabe dentro del triángulo, tocando los tres lados.

**Las tres bisectrices, el incentro I y el inradio (calculados):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-bisectrices" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-bisectrices')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-bisectrices', {
      boundingbox: [-1, 7, 9, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Vertices
    var A = [1, 1], B = [7, 1], C = [4, 6];
    
    // Calcular longitudes de lados
    function dist(p1, p2) {
      return Math.sqrt((p2[0]-p1[0])*(p2[0]-p1[0]) + (p2[1]-p1[1])*(p2[1]-p1[1]));
    }
    
    var a = dist(B, C);  // Lado opuesto a A
    var b = dist(A, C);  // Lado opuesto a B
    var c = dist(A, B);  // Lado opuesto a C
    
    // Incentro (calculado con formula)
    var I = [
      (a * A[0] + b * B[0] + c * C[0]) / (a + b + c),
      (a * A[1] + b * B[1] + c * C[1]) / (a + b + c)
    ];
    
    // Inradio = Area / semiperimetro
    var s = (a + b + c) / 2;
    var area = Math.abs((B[0]-A[0])*(C[1]-A[1]) - (C[0]-A[0])*(B[1]-A[1])) / 2;
    var inradius = area / s;
    
    // Dibujar triangulo
    var pA = board.create('point', A, {name: 'A', size: 5, fixed: true, color: '#1e293b', label: {fontSize: 13, offset: [-15, -10]}});
    var pB = board.create('point', B, {name: 'B', size: 5, fixed: true, color: '#1e293b', label: {fontSize: 13, offset: [10, -10]}});
    var pC = board.create('point', C, {name: 'C', size: 5, fixed: true, color: '#1e293b', label: {fontSize: 13, offset: [0, 10]}});
    
    board.create('segment', [pA, pB], {strokeColor: '#1e293b', strokeWidth: 2});
    board.create('segment', [pB, pC], {strokeColor: '#1e293b', strokeWidth: 2});
    board.create('segment', [pC, pA], {strokeColor: '#1e293b', strokeWidth: 2});
    
    // Bisectrices (desde vertices hacia incentro, extendidas)
    var extA = [I[0] + (I[0] - A[0]) * 2, I[1] + (I[1] - A[1]) * 2];
    var extB = [I[0] + (I[0] - B[0]) * 2, I[1] + (I[1] - B[1]) * 2];
    var extC = [I[0] + (I[0] - C[0]) * 2, I[1] + (I[1] - C[1]) * 2];
    
    board.create('segment', [A, extA], {strokeColor: '#a855f7', strokeWidth: 2});
    board.create('segment', [B, extB], {strokeColor: '#a855f7', strokeWidth: 2});
    board.create('segment', [C, extC], {strokeColor: '#a855f7', strokeWidth: 2});
    
    // Incentro
    var pI = board.create('point', I, {name: 'I', size: 7, fixed: true, color: '#ef4444', label: {fontSize: 14, color: '#ef4444', offset: [10, 5]}});
    
    // Circunferencia inscrita
    board.create('circle', [I, inradius], {strokeColor: '#f59e0b', strokeWidth: 2, fillColor: 'transparent'});
    
    board.create('text', [4, -0.3, 'I = Incentro, r = ' + inradius.toFixed(2)], {fontSize: 11, color: '#ef4444', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Mediatrices

Una **mediatriz** es la recta **perpendicular** a un lado del triángulo que pasa por su **punto medio**.

### Propiedades de las mediatrices

1. Todo triángulo tiene **3 mediatrices** (una para cada lado)
2. Las tres mediatrices se cortan en un punto llamado **circuncentro**
3. El circuncentro es equidistante a los tres vértices
4. El circuncentro es el centro de la **circunferencia circunscrita**

### Diferencia con la altura

- **Altura**: perpendicular desde un vértice
- **Mediatriz**: perpendicular desde el punto medio del lado

### Aplicación

La circunferencia circunscrita pasa por los tres vértices del triángulo.

### Fórmula del circuncentro

Si los vértices son $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$:

$$
D = 2[x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)]
$$

$$
O_x = \frac{(x_1^2 + y_1^2)(y_2 - y_3) + (x_2^2 + y_2^2)(y_3 - y_1) + (x_3^2 + y_3^2)(y_1 - y_2)}{D}
$$

$$
O_y = \frac{(x_1^2 + y_1^2)(x_3 - x_2) + (x_2^2 + y_2^2)(x_1 - x_3) + (x_3^2 + y_3^2)(x_2 - x_1)}{D}
$$

### Fórmula del circunradio

$$
R = \frac{abc}{4 \cdot \text{Área}}
$$

donde $a$, $b$, $c$ son las longitudes de los lados.

---

## 📖 Resumen comparativo

| Recta | Se traza en | Punto de encuentro | Propiedad especial |
|-------|-------------|-------------------|-------------------|
| Mediana | Vértice → punto medio lado | Baricentro | Centro de gravedad |
| Altura | Vértice ⊥ lado opuesto | Ortocentro | Para calcular área |
| Bisectriz | Divide ángulo en 2 iguales | Incentro | Circunferencia inscrita |
| Mediatriz | ⊥ al punto medio del lado | Circuncentro | Circunferencia circunscrita |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar rectas

Indica qué recta notable es cada descripción:

1. Une el vértice $A$ con el punto medio de $\overline{BC}$
2. Es perpendicular al lado $\overline{AB}$ y pasa por su punto medio
3. Divide el ángulo $\angle B$ en dos partes iguales
4. Sale del vértice $C$ y es perpendicular al lado $\overline{AB}$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Mediana** desde $A$
2. **Mediatriz** del lado $AB$
3. **Bisectriz** del ángulo $B$
4. **Altura** desde $C$

</details>

---

### Ejercicio 2: Puntos notables

Relaciona cada punto con las rectas que lo determinan:

| Punto | Intersección de... |
|-------|-------------------|
| Baricentro | |
| Ortocentro | |
| Incentro | |
| Circuncentro | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Punto | Intersección de... |
|-------|-------------------|
| Baricentro | Las 3 medianas |
| Ortocentro | Las 3 alturas |
| Incentro | Las 3 bisectrices |
| Circuncentro | Las 3 mediatrices |

</details>

---

### Ejercicio 3: Verdadero o Falso

1. La mediatriz pasa siempre por un vértice del triángulo.
2. El baricentro siempre está dentro del triángulo.
3. En un triángulo obtusángulo, el ortocentro está afuera.
4. La altura y la mediana desde un mismo vértice son siempre iguales.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** - Pasa por el punto medio del lado, no por el vértice
2. **Verdadero** - El baricentro siempre está en el interior
3. **Verdadero** - En triángulos obtusángulos, el ortocentro está afuera
4. **Falso** - Solo coinciden en el triángulo equilátero

</details>

---
