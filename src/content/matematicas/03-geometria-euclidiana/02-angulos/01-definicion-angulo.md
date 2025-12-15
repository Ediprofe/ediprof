# Definición de Ángulo

En geometría, después de conocer los elementos básicos como el punto, la recta y el plano, es fundamental estudiar el **ángulo**. Los ángulos están presentes en todas las figuras geométricas y en infinidad de situaciones cotidianas.

---

## 📖 ¿Qué es un ángulo?

Un **ángulo** es la abertura formada por dos rayos que comparten el mismo punto de origen.

> **Definición:** Un ángulo es la región del plano comprendida entre dos rayos (semirrectas) que tienen un origen común llamado vértice.

### Elementos de un ángulo

Todo ángulo tiene tres elementos:

| Elemento | Descripción |
|----------|-------------|
| **Vértice** | El punto donde se unen los dos rayos (punto común) |
| **Lados** | Los dos rayos que forman el ángulo |
| **Abertura** | La amplitud o "apertura" entre los lados |

### Ejemplo 1

Cuando abres un compás, los dos brazos forman un ángulo:
- El **vértice** es el punto donde se unen los brazos (el tornillo)
- Los **lados** son cada brazo del compás
- La **abertura** es qué tan abierto está el compás

### Ejemplo 2

Las manecillas de un reloj forman un ángulo:
- El **vértice** es el centro del reloj
- Los **lados** son la manecilla de la hora y la de los minutos
- La **abertura** cambia conforme pasa el tiempo

**Elementos del ángulo $\angle ABC$ (vértice, lados y abertura):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-angulo-elementos" style="width: 100%; height: 320px; min-height: 280px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-angulo-elementos')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-angulo-elementos', {
      boundingbox: [-1, 6, 12, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Vértice
    var V = board.create('point', [3, 2.5], {name: 'V', size: 6, fixed: true, color: '#ef4444', label: {fontSize: 14, color: '#ef4444', offset: [-20, -10]}});
    
    // Lados del ángulo (rayos desde V)
    var lado1End = board.create('point', [8, 2.5], {visible: false, fixed: true});
    var lado2End = board.create('point', [7, 5.5], {visible: false, fixed: true});
    
    board.create('line', [V, lado1End], {strokeColor: '#3b82f6', strokeWidth: 3, straightFirst: false, straightLast: true});
    board.create('line', [V, lado2End], {strokeColor: '#3b82f6', strokeWidth: 3, straightFirst: false, straightLast: true});
    
    // Arco para mostrar la abertura
    board.create('angle', [lado1End, V, lado2End], {
      radius: 1.2,
      fillColor: '#fef3c7',
      fillOpacity: 0.6,
      strokeColor: '#f59e0b',
      strokeWidth: 2,
      name: 'α',
      label: {fontSize: 16, color: '#f59e0b', offset: [0, 0]}
    });
    
    // Etiquetas con flechas
    board.create('text', [3, 1, 'VÉRTICE'], {fontSize: 11, fontWeight: 'bold', color: '#ef4444', anchorX: 'middle'});
    board.create('text', [9, 2.5, 'LADO'], {fontSize: 11, fontWeight: 'bold', color: '#3b82f6'});
    board.create('text', [7.5, 5.8, 'LADO'], {fontSize: 11, fontWeight: 'bold', color: '#3b82f6'});
    board.create('text', [5, 3.8, 'ABERTURA'], {fontSize: 11, fontWeight: 'bold', color: '#f59e0b'});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Notación de ángulos

Existen varias formas de nombrar un ángulo:

### 1. Con tres letras

Se usan tres puntos: uno en cada lado y el vértice en el medio.

$$
\angle ABC \quad \text{o} \quad \angle CBA
$$

El vértice ($B$) siempre va en el **centro**.

### 2. Con una letra en el vértice

Cuando no hay confusión, se usa solo la letra del vértice:

$$
\angle B
$$

### 3. Con una letra griega

Se usa una letra griega minúscula:

$$
\alpha, \quad \beta, \quad \gamma, \quad \theta
$$

(alfa, beta, gamma, theta)

### 4. Con un número

Se usa un número dentro del ángulo:

$$
\angle 1, \quad \angle 2
$$

---

## 📖 Cómo se "abre" un ángulo

Imagina que uno de los lados del ángulo está fijo (horizontal, llamado **lado inicial**) y el otro lado gira alrededor del vértice (llamado **lado terminal**):

- Si el lado móvil gira **poco**, el ángulo es pequeño
- Si gira **más**, el ángulo es más grande
- Si gira **media vuelta** (180°), forma una línea recta (**ángulo llano**)
- Si gira una **vuelta completa** (360°), vuelve a la posición inicial

Esta "cantidad de giro" es lo que medimos en un ángulo.

### Convención de signos: ángulos positivos y negativos

> **Regla importante:** Por convención matemática:
> - **Ángulo positivo (+)**: cuando el lado terminal gira en sentido **antihorario** (contrario a las agujas del reloj) ↺
> - **Ángulo negativo (−)**: cuando el lado terminal gira en sentido **horario** (igual que las agujas del reloj) ↻

Esta convención es fundamental en trigonometría y en muchas aplicaciones de física e ingeniería.

**Ángulo positivo (+45°) vs Ángulo negativo (−45°):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-signos-angulos" style="width: 100%; height: 280px; min-height: 250px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-signos-angulos')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-signos-angulos', {
      boundingbox: [-1, 5, 13, -3],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // === ÁNGULO POSITIVO (izquierda) ===
    var cx1 = 3, cy = 1.5, r = 2;
    
    // Lado inicial (horizontal)
    board.create('segment', [[cx1, cy], [cx1 + r, cy]], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    board.create('point', [cx1, cy], {name: '', size: 5, fixed: true, color: '#1e293b'});
    
    // Lado terminal (+45°)
    var rad45 = 45 * Math.PI / 180;
    board.create('segment', [[cx1, cy], [cx1 + r * Math.cos(rad45), cy + r * Math.sin(rad45)]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    
    // Arco del ángulo positivo
    var p1a = board.create('point', [cx1 + r, cy], {visible: false, fixed: true});
    var p1b = board.create('point', [cx1 + r * Math.cos(rad45), cy + r * Math.sin(rad45)], {visible: false, fixed: true});
    board.create('angle', [p1a, [cx1, cy], p1b], {
      radius: 0.8,
      fillColor: '#dcfce7',
      fillOpacity: 0.7,
      strokeColor: '#22c55e',
      strokeWidth: 2,
      name: '+45°',
      label: {fontSize: 12, color: '#22c55e', offset: [5, 5]}
    });
    
    // Flecha curva antihorario
    board.create('text', [cx1 + 1.3, cy + 1.5, '↺'], {fontSize: 24, color: '#22c55e', fixed: true});
    board.create('text', [cx1, 4, 'ÁNGULO POSITIVO'], {fontSize: 12, fontWeight: 'bold', color: '#22c55e', anchorX: 'middle', fixed: true});
    board.create('text', [cx1, 3.4, 'Giro antihorario'], {fontSize: 10, color: '#64748b', anchorX: 'middle', fixed: true});
    
    // === ÁNGULO NEGATIVO (derecha) ===
    var cx2 = 9;
    
    // Lado inicial (horizontal)
    board.create('segment', [[cx2, cy], [cx2 + r, cy]], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    board.create('point', [cx2, cy], {name: '', size: 5, fixed: true, color: '#1e293b'});
    
    // Lado terminal (-45°)
    var radNeg45 = -45 * Math.PI / 180;
    board.create('segment', [[cx2, cy], [cx2 + r * Math.cos(radNeg45), cy + r * Math.sin(radNeg45)]], {strokeColor: '#ef4444', strokeWidth: 3, fixed: true});
    
    // Arco del ángulo negativo
    var p2a = board.create('point', [cx2 + r, cy], {visible: false, fixed: true});
    var p2b = board.create('point', [cx2 + r * Math.cos(radNeg45), cy + r * Math.sin(radNeg45)], {visible: false, fixed: true});
    board.create('angle', [p2b, [cx2, cy], p2a], {
      radius: 0.8,
      fillColor: '#fee2e2',
      fillOpacity: 0.7,
      strokeColor: '#ef4444',
      strokeWidth: 2,
      name: '−45°',
      label: {fontSize: 12, color: '#ef4444', offset: [5, -15]}
    });
    
    // Flecha curva horario
    board.create('text', [cx2 + 1.3, cy - 1.3, '↻'], {fontSize: 24, color: '#ef4444', fixed: true});
    board.create('text', [cx2, 4, 'ÁNGULO NEGATIVO'], {fontSize: 12, fontWeight: 'bold', color: '#ef4444', anchorX: 'middle', fixed: true});
    board.create('text', [cx2, 3.4, 'Giro horario'], {fontSize: 10, color: '#64748b', anchorX: 'middle', fixed: true});
    
    // Leyenda
    board.create('text', [6, -2, 'Verde = Lado inicial | Azul/Rojo = Lado terminal'], {fontSize: 9, color: '#94a3b8', anchorX: 'middle', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>


### El transportador: instrumento para medir ángulos

Para medir ángulos usamos un **transportador**. Es un semicírculo graduado con marcas de 0° a 180°.

**Cómo usarlo:**
1. Coloca el **centro** del transportador sobre el **vértice** del ángulo
2. Alinea la **base** (0°) con el lado inicial del ángulo
3. Lee el valor donde cruza el **lado terminal**

**¡Arrastra el punto azul para explorar diferentes ángulos!**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-transportador-completo" style="width: 100%; height: 400px; min-height: 360px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-transportador-completo')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-transportador-completo', {
      boundingbox: [-1, 7, 11, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var cx = 5, cy = 2, r = 4;
    
    // Arco del transportador (semicírculo) - FIJO
    board.create('arc', [[cx, cy], [cx + r, cy], [cx - r, cy]], {
      strokeColor: '#64748b',
      strokeWidth: 2,
      fillColor: '#e2e8f0',
      fillOpacity: 0.3,
      fixed: true
    });
    
    // Línea base del transportador - FIJA
    board.create('segment', [[cx - r, cy], [cx + r, cy]], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    
    // Centro del transportador - FIJO
    board.create('point', [cx, cy], {name: 'Vértice', size: 5, fixed: true, color: '#ef4444', label: {fontSize: 10, color: '#ef4444', offset: [0, -18]}});
    
    // Marcas de grado cada 30° - FIJAS
    var marcas = [0, 30, 60, 90, 120, 150, 180];
    marcas.forEach(function(deg) {
      var rad = deg * Math.PI / 180;
      var x1 = cx + (r - 0.3) * Math.cos(rad);
      var y1 = cy + (r - 0.3) * Math.sin(rad);
      var x2 = cx + r * Math.cos(rad);
      var y2 = cy + r * Math.sin(rad);
      board.create('segment', [[x1, y1], [x2, y2]], {strokeColor: '#475569', strokeWidth: 2, fixed: true});
      
      var xLabel = cx + (r + 0.4) * Math.cos(rad);
      var yLabel = cy + (r + 0.4) * Math.sin(rad);
      board.create('text', [xLabel, yLabel, deg + '°'], {fontSize: 11, fontWeight: 'bold', color: '#1e293b', anchorX: 'middle', anchorY: 'middle', fixed: true});
    });
    
    // Marcas pequeñas cada 10° - FIJAS
    for (var deg = 10; deg < 180; deg += 10) {
      if (deg % 30 !== 0) {
        var rad = deg * Math.PI / 180;
        var x1 = cx + (r - 0.15) * Math.cos(rad);
        var y1 = cy + (r - 0.15) * Math.sin(rad);
        var x2 = cx + r * Math.cos(rad);
        var y2 = cy + r * Math.sin(rad);
        board.create('segment', [[x1, y1], [x2, y2]], {strokeColor: '#94a3b8', strokeWidth: 1, fixed: true});
      }
    }
    
    // Lado inicial (fijo, en 0°)
    board.create('segment', [[cx, cy], [cx + r, cy]], {strokeColor: '#22c55e', strokeWidth: 4, fixed: true});
    board.create('text', [cx + r + 0.3, cy - 0.5, 'Lado inicial'], {fontSize: 9, color: '#22c55e', fixed: true});
    
    // Glider sobre el arco para el lado terminal (INTERACTIVO)
    var arcoInvisible = board.create('arc', [[cx, cy], [cx + r, cy], [cx - r, cy]], {visible: false});
    var pMovil = board.create('glider', [cx + r * Math.cos(Math.PI/4), cy + r * Math.sin(Math.PI/4), arcoInvisible], {
      name: '', size: 10, color: '#3b82f6', 
      label: {fontSize: 12, offset: [12, 5]}
    });
    
    // Lado terminal (móvil)
    board.create('segment', [[cx, cy], pMovil], {strokeColor: '#3b82f6', strokeWidth: 4});
    
    // Arco del ángulo medido
    var pBase = board.create('point', [cx + r, cy], {visible: false, fixed: true});
    board.create('angle', [pBase, [cx, cy], pMovil], {
      radius: 1,
      fillColor: '#fef3c7',
      fillOpacity: 0.7,
      strokeColor: '#f59e0b',
      strokeWidth: 2,
      name: ''
    });
    
    // Texto que muestra el ángulo medido
    board.create('text', [cx, -0.5, function() {
      var dx = pMovil.X() - cx;
      var dy = pMovil.Y() - cy;
      var angleRad = Math.atan2(dy, dx);
      var angleDeg = angleRad * 180 / Math.PI;
      if (angleDeg < 0) angleDeg += 360;
      if (angleDeg > 180) angleDeg = 360 - angleDeg;
      return '📐 Medición: ' + Math.round(angleDeg) + '° (positivo ↺)';
    }], {fontSize: 14, fontWeight: 'bold', color: '#1e293b', anchorX: 'middle', fixed: true});
    
    // Etiqueta lado terminal
    board.create('text', [function() { return pMovil.X() + 0.3; }, function() { return pMovil.Y() + 0.3; }, 'Lado terminal'], {fontSize: 9, color: '#3b82f6'});
    
    // Instrucción
    board.create('text', [cx, 6.5, '¡Arrastra el punto azul sobre el arco!'], {fontSize: 11, color: '#64748b', anchorX: 'middle', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Ángulos en la vida cotidiana

Los ángulos están en todas partes:

| Situación | Ángulo formado |
|-----------|----------------|
| Esquina de una habitación | 90° (ángulo recto) |
| Pendiente de un techo | Aproximadamente 30° |
| Escalera apoyada en pared | Aproximadamente 75° |
| Abanico completamente abierto | 180° (ángulo llano) |
| Reloj a las 3:00 | 90° |
| Reloj a las 6:00 | 180° |
| Tijeras medio abiertas | Aproximadamente 45° |

### Ejemplo 1

A las **3:00 en punto**, las manecillas del reloj forman un ángulo de 90° (ángulo recto).

### Ejemplo 2

A las **6:00 en punto**, las manecillas están opuestas y forman un ángulo de 180° (ángulo llano).

### Ejemplo 3

A las **12:00 en punto**, las manecillas están superpuestas y forman un ángulo de 0°.

---

## 📖 Unidad de medida: el grado

La unidad más común para medir ángulos es el **grado** (°).

> **Definición:** Un grado es la medida de un ángulo que resulta de dividir un ángulo completo (una vuelta) en 360 partes iguales.

### ¿Por qué 360?

Los babilonios usaban un sistema de numeración en base 60. Ellos observaron que el año tiene aproximadamente 360 días, así que dividieron el círculo en 360 partes.

### Valores importantes

| Giro | Grados |
|------|--------|
| Sin giro | 0° |
| Cuarto de vuelta | 90° |
| Media vuelta | 180° |
| Tres cuartos de vuelta | 270° |
| Vuelta completa | 360° |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar elementos

En el ángulo $\angle PQR$:

1. ¿Cuál es el vértice?
2. ¿Cuáles son los lados?

<details>
<summary><strong>Ver respuestas</strong></summary>

1. El vértice es $Q$ (la letra del medio)
2. Los lados son $\overrightarrow{QP}$ y $\overrightarrow{QR}$

</details>

---

### Ejercicio 2: Ángulos del reloj

Indica aproximadamente qué ángulo forman las manecillas del reloj en cada hora:

| Hora | Ángulo |
|------|--------|
| 3:00 | |
| 6:00 | |
| 9:00 | |
| 12:00 | |
| 1:00 | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Hora | Ángulo |
|------|--------|
| 3:00 | 90° |
| 6:00 | 180° |
| 9:00 | 90° |
| 12:00 | 0° |
| 1:00 | 30° |

</details>

---

### Ejercicio 3: Notación

Escribe tres formas diferentes de nombrar un ángulo cuyo vértice es el punto $M$ y cuyos lados pasan por los puntos $L$ y $N$.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\angle LMN$
2. $\angle NML$
3. $\angle M$

</details>

---
