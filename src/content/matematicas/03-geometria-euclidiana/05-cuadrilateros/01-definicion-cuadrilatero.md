# Definición de Cuadrilátero

Un **cuadrilátero** es un polígono de cuatro lados. Es una de las figuras geométricas más comunes en nuestra vida cotidiana: ventanas, puertas, libros, pantallas...

---

## 📖 ¿Qué es un cuadrilátero?

> **Definición:** Un cuadrilátero es un polígono formado por **cuatro lados**, **cuatro vértices** y **cuatro ángulos**.

### Elementos

| Elemento | Descripción |
|----------|-------------|
| Vértices | Los 4 puntos donde se unen los lados (A, B, C, D) |
| Lados | Los 4 segmentos que forman el contorno |
| Ángulos | Los 4 ángulos interiores |
| Diagonales | Segmentos que unen vértices no consecutivos |

---

## 📖 Las diagonales

Un cuadrilátero tiene exactamente **2 diagonales**:
- Diagonal $\overline{AC}$ (une vértices opuestos)
- Diagonal $\overline{BD}$ (une los otros vértices opuestos)

Las diagonales dividen al cuadrilátero en **triángulos**.

**Ilustración: Elementos del Cuadrilátero:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-general" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initGeneral() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-general')) {
      setTimeout(initGeneral, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-general']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-general', {
      boundingbox: [-2, 7, 8, -3],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos fijos
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, -10]}});
    var B = board.create('point', [5, 1], {name: 'B', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, -5]}});
    var C = board.create('point', [4, 5], {name: 'C', size: 3, color: '#1e293b', fixed: true, label: {offset: [5, 10]}});
    var D = board.create('point', [1, 4], {name: 'D', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, 10]}});
    
    // Polígono
    var poly = board.create('polygon', [A, B, C, D], {
      fillColor: '#dbeafe', 
      fillOpacity: 0.5, 
      borders: {strokeColor: '#3b82f6', strokeWidth: 2}
    });

    // Diagonales
    board.create('segment', [A, C], {strokeColor: '#ef4444', strokeWidth: 2, dash: 2});
    board.create('segment', [B, D], {strokeColor: '#f97316', strokeWidth: 2, dash: 2});

    // Ángulos (Orden: Siguiente, Vértice, Anterior para ángulos interiores en polígono CCW)
    var angleStyle = {radius: 0.5, fillColor: '#22c55e', fillOpacity: 0.3, strokeColor: '#166534'};
    board.create('angle', [B, A, D], { ...angleStyle, name: 'α' });
    board.create('angle', [C, B, A], { ...angleStyle, name: 'β' });
    board.create('angle', [D, C, B], { ...angleStyle, name: 'γ' });
    board.create('angle', [A, D, C], { ...angleStyle, name: 'δ' });
    
    // Etiquetas adicionales
    board.create('text', [2.5, 2.5, 'Diagonales'], {color: '#ef4444', fontSize: 11, fixed: true, anchorX: 'middle'});
    board.create('text', [2.5, -0.5, 'Lado AB'], {color: '#3b82f6', fontSize: 11, fixed: true});

  }
  
  initGeneral();
})();
</script>

---

## 📖 Suma de ángulos interiores

> **Propiedad fundamental:** La suma de los ángulos interiores de cualquier cuadrilátero es **360°**.

$$
\angle A + \angle B + \angle C + \angle D = 360°
$$

### ¿Por qué 360°?

Una diagonal divide al cuadrilátero en 2 triángulos. Como cada triángulo tiene ángulos que suman 180°:

$$
2 \times 180° = 360°
$$

### Ejemplo

Si tres ángulos de un cuadrilátero miden 80°, 90° y 110°, el cuarto ángulo es:

$$
\angle D = 360° - 80° - 90° - 110° = 80°
$$

---

## 📖 Clasificación general

Los cuadriláteros se clasifican según el **paralelismo de sus lados**:

| Tipo | Lados paralelos | Ejemplos |
|------|-----------------|----------|
| Paralelogramos | 2 pares de lados paralelos | Cuadrado, rectángulo, rombo |
| Trapecios | 1 par de lados paralelos | Trapecio isósceles, escaleno |
| Trapezoides | Ningún par de lados paralelos | Cuadrilátero irregular |

---

## 📖 Cuadriláteros convexos y cóncavos

### Convexo

Todos los ángulos interiores son **menores que 180°**. Las diagonales están completamente **dentro** de la figura.

### Cóncavo

Un ángulo interior es **mayor que 180°** (ángulo reflejo). Una diagonal queda **fuera** de la figura.

**Ilustración: Convexo vs Cóncavo:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-tipos" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initTipos() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-tipos')) {
      setTimeout(initTipos, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-tipos']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-tipos', {
      boundingbox: [-1, 7, 11, -3],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // --- CONVEXO ---
    // Un cuadrilátero convexo simple
    var A1 = board.create('point', [0, 0], {name: 'A', size: 2, color: '#1e293b', variable: false, fixed: true, label:{visible:false}});
    var B1 = board.create('point', [3, 0], {name: 'B', size: 2, color: '#1e293b', variable: false, fixed: true, label:{visible:false}});
    var C1 = board.create('point', [3.5, 3], {name: 'C', size: 2, color: '#1e293b', variable: false, fixed: true, label:{visible:false}});
    var D1 = board.create('point', [0.5, 2.5], {name: 'D', size: 2, color: '#1e293b', variable: false, fixed: true, label:{visible:false}});
    
    board.create('polygon', [A1, B1, C1, D1], {fillColor: '#22c55e', fillOpacity: 0.3, borders: {strokeColor: '#166534', strokeWidth: 2}});
    
    // Diagonales (ambas internas)
    board.create('segment', [A1, C1], {strokeColor: '#166534', strokeWidth: 2, dash: 2}); 
    board.create('segment', [B1, D1], {strokeColor: '#166534', strokeWidth: 2, dash: 2});
    
    board.create('text', [1.8, -1, 'Convexo'], {fontSize: 12, fontWeight: 'bold', color: '#166534', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, -1.5, 'Diagonales internas'], {fontSize: 11, color: '#1e293b', fixed: true, anchorX: 'middle'});

    // --- CÓNCAVO ---
    // Polígono tipo "Punta de Flecha" (Arrowhead)
    // L(Left), T(Tip/Top), R(Right), I(Indent/Bottom)
    var L = board.create('point', [6, 2], {name: '', size: 2, color: '#1e293b', fixed: true, visible: true});
    var T = board.create('point', [8, 5], {name: '', size: 2, color: '#1e293b', fixed: true, visible: true});
    var R = board.create('point', [10, 2], {name: '', size: 2, color: '#1e293b', fixed: true, visible: true});
    var I = board.create('point', [8, 3], {name: '', size: 2, color: '#1e293b', fixed: true, visible: true});
    
    // El polígono se dibuja L -> T -> R -> I -> L.
    board.create('polygon', [L, T, R, I], {
        fillColor: '#ef4444', 
        fillOpacity: 0.3, 
        borders: {strokeColor: '#b91c1c', strokeWidth: 2}
    });
    
    // Diagonal Externa: Une L y R.
    board.create('segment', [L, R], {strokeColor: '#b91c1c', strokeWidth: 2, dash: 2}); 
    
    // Diagonal Interna: Une I y T.
    board.create('segment', [I, T], {strokeColor: '#b91c1c', strokeWidth: 1, dash: 3, opacity: 0.5});

    // Ángulo reflejo en I (> 180°). 
    // El ángulo interior en I se define por los vértices adyacentes R y L.
    // En JSXGraph, angle(p1, p2, p3) dibuja el ángulo p1->p2->p3 en sentido antihorario.
    // Queremos el ángulo interior, que es el "grande".
    // Viniendo de R, pasando por I, hacia L.
    // Vector IR: (2, -1). Vector IL: (-2, -1).
    // Si vamos R -> I -> L antihorario, barremos el ángulo de abajo (el pequeño, < 180).
    // Si vamos L -> I -> R antihorario, barremos el ángulo de arriba (el grande, reflejo).
    // Comprobemos: L(6,2) -> I(8,3) -> R(10,2).
    // L está a la izquierda. R a la derecha. I arriba.
    // Vector IL = (-2, -1). Vector IR = (2, -1).
    // Ángulo de IL a IR en sentido antihorario:
    // IL está en 3er cuadrante (apunta izq abajo). IR está en 4to cuadrante (apunta der abajo).
    // De 3er a 4to cuadrante antihorario pasa por 2do y 1er? No.
    // De 210 grados a 330 grados?
    // IL angle approx 206 deg. IR angle approx 333 deg.
    // Diferencia 333 - 206 = 127 deg.
    // Ese sería el ángulo pequeño.
    // Entonces para el ángulo GRANDE (reflejo) necesitamos ir de IR a IL?
    // Angle(R, I, L)?
    // R(-2, -1 from I?) -> angle -26 deg.
    // L(-2, -1 from I?).
    // De R a L antihorario... -26 -> ... -> 206. Total ~230 grados.
    // Exacto. Así que Angle(R, I, L) debe darnos el reflejo.
    
    var reflexAngle = board.create('angle', [R, I, L], {
      radius: 0.5, 
      fillColor: '#ef4444', 
      fillOpacity: 0.3, 
      strokeColor: '#b91c1c',
      name: '> 180°'
    });
    // Forzamos etiqueta visible un poco desplazada si es necesario, pero JSXGraph suele colocarla bien.

    board.create('text', [8, -1, 'Cóncavo'], {fontSize: 12, fontWeight: 'bold', color: '#b91c1c', fixed: true, anchorX: 'middle'});
    board.create('text', [8, -1.5, 'Diagonal externa'], {fontSize: 11, color: '#1e293b', fixed: true, anchorX: 'middle'});
    
  }
  
  initTipos();
})();
</script>

---

## 📖 Nomenclatura

Los cuadriláteros se nombran con 4 letras en orden (siguiendo el contorno):

$$
ABCD \quad \text{o} \quad DCBA
$$

Los vértices se nombran en orden, en sentido horario o antihorario.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular el ángulo faltante

Calcula el cuarto ángulo de cada cuadrilátero:

| $\angle A$ | $\angle B$ | $\angle C$ | $\angle D$ |
|------------|------------|------------|------------|
| 70° | 100° | 85° | ? |
| 90° | 90° | 90° | ? |
| 120° | 60° | 120° | ? |

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\angle D = 360° - 70° - 100° - 85° = 105°$
2. $\angle D = 360° - 90° - 90° - 90° = 90°$ (es un rectángulo)
3. $\angle D = 360° - 120° - 60° - 120° = 60°$ (es un paralelogramo)

</details>

---

### Ejercicio 2: Clasificar

Clasifica cada cuadrilátero según el paralelismo de sus lados:

1. Una ventana rectangular
2. Una cometa (con dos pares de lados iguales consecutivos, pero no paralelos)
3. Un cartel con forma de rombo

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Paralelogramo** (específicamente un rectángulo)
2. **Trapezoide** (ningún lado paralelo)
3. **Paralelogramo** (el rombo tiene dos pares de lados paralelos)

</details>

---

### Ejercicio 3: Verdadero o Falso

1. Todo cuadrilátero tiene exactamente 2 diagonales.
2. La suma de los ángulos de un cuadrilátero puede ser diferente de 360°.
3. Un cuadrilátero cóncavo tiene un ángulo mayor que 180°.
4. Las diagonales de un cuadrilátero siempre se cortan dentro de la figura.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero**
2. **Falso** - Siempre es exactamente 360°
3. **Verdadero**
4. **Falso** - En cuadriláteros cóncavos pueden cortarse fuera

</details>

---
