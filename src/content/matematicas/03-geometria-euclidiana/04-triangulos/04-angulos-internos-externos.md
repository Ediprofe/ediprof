# Ángulos Internos y Externos del Triángulo

Una de las propiedades más importantes de los triángulos es la suma de sus ángulos internos. En esta lección estudiaremos esta propiedad y también los ángulos externos.

---

## 📖 Suma de ángulos internos

En todo triángulo, la **suma de los ángulos interiores** es siempre igual a $180°$.

$$
\angle A + \angle B + \angle C = 180°
$$

### ¿Por qué es así?

Esta propiedad se puede demostrar trazando una recta paralela a un lado del triángulo que pase por el vértice opuesto.

Los ángulos alternos internos son iguales y juntos forman un ángulo llano (180°).

### Ejemplo 1

Si un triángulo tiene ángulos de $50°$ y $70°$, el tercer ángulo es:

$$
\angle C = 180° - 50° - 70° = 60°
$$

### Ejemplo 2

En un triángulo equilátero, los tres ángulos son iguales:

$$
3\alpha = 180° \Rightarrow \alpha = 60°
$$

### Ejemplo 3

En un triángulo rectángulo, un ángulo es $90°$. Los otros dos suman:

$$
\angle A + \angle B = 180° - 90° = 90°
$$

Por eso se dice que son **complementarios**.

### 📊 Ilustración: Suma de ángulos internos = 180°

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <span>📊</span>
  <div id="jsxgraph-angulos-internos" style="width: 100%; height: 300px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-angulos-internos')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-angulos-internos', {
      boundingbox: [-1, 5, 9, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Triángulo
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#ef4444', fixed: true, label: {fontSize: 14, color: '#ef4444', offset: [-15, -10]}});
    var B = board.create('point', [6, 0], {name: 'B', size: 3, color: '#ef4444', fixed: true, label: {fontSize: 14, color: '#ef4444', offset: [10, -10]}});
    var C = board.create('point', [4, 3.5], {name: 'C', size: 3, color: '#ef4444', fixed: true, label: {fontSize: 14, color: '#ef4444', offset: [0, 10]}});
    
    board.create('segment', [A, B], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    board.create('segment', [B, C], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    board.create('segment', [C, A], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    
    // Ángulos con colores diferentes
    board.create('angle', [B, A, C], {radius: 0.7, fillColor: '#22c55e', fillOpacity: 0.4, strokeColor: '#22c55e', name: '50°', label: {fontSize: 12}});
    board.create('angle', [C, B, A], {radius: 0.7, fillColor: '#3b82f6', fillOpacity: 0.4, strokeColor: '#3b82f6', name: '70°', label: {fontSize: 12}});
    board.create('angle', [A, C, B], {radius: 0.6, fillColor: '#f59e0b', fillOpacity: 0.4, strokeColor: '#f59e0b', name: '60°', label: {fontSize: 12}});
    
    // Fórmula
    board.create('text', [4.5, -0.6, '50° + 70° + 60° = 180° ✓'], {fontSize: 13, color: '#1e293b', fixed: true, anchorX: 'middle'});
  }
});
</script>

> 💡 **Recuerda:** No importa la forma del triángulo, sus tres ángulos internos **siempre** suman exactamente $180°$.

---

## 📖 Ángulo exterior de un triángulo

Un **ángulo exterior** se forma al prolongar uno de los lados del triángulo más allá de un vértice.

### Definición

El ángulo exterior es el ángulo formado por un lado del triángulo y la **prolongación** del lado adyacente.

### Relación con el ángulo interior

Un ángulo exterior y su ángulo interior correspondiente son **suplementarios**:

$$
\text{Ángulo exterior} + \text{Ángulo interior} = 180°
$$

### Ejemplo

Si $\angle A = 70°$, el ángulo exterior en el vértice $A$ mide:

$$
180° - 70° = 110°
$$

**Ilustración del ángulo exterior en el vértice $A$:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-angulo-exterior" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-angulo-exterior')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-angulo-exterior', {
      boundingbox: [-2, 5, 10, -3],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Triángulo con ángulo en A = 70°
    var A = board.create('point', [2, 0], {name: 'A', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 14, color: '#1e293b', offset: [-5, -20]}});
    var B = board.create('point', [8, 0], {name: 'B', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 14, color: '#1e293b', offset: [10, -10]}});
    // C posicionado para crear ángulo de 70° en A
    var Cx = 2 + 4*Math.cos(70*Math.PI/180);
    var Cy = 4*Math.sin(70*Math.PI/180);
    var C = board.create('point', [Cx, Cy], {name: 'C', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 14, color: '#1e293b', offset: [-15, 5]}});
    
    // Lados del triángulo
    board.create('segment', [A, B], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    board.create('segment', [B, C], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    board.create('segment', [C, A], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    
    // Prolongación del lado CA más allá de A (en dirección opuesta a C)
    // Vector de C a A: (A.x - C.x, A.y - C.y)
    var dx = 2 - Cx;  // dirección de C hacia A
    var dy = 0 - Cy;
    var len = Math.sqrt(dx*dx + dy*dy);
    // Punto en la prolongación: A + 2.5 * dirección normalizada
    var extX = 2 + 2.5 * (dx/len);
    var extY = 0 + 2.5 * (dy/len);
    var pExt = board.create('point', [extX, extY], {visible: false, fixed: true});
    board.create('segment', [A, pExt], {strokeColor: '#f59e0b', strokeWidth: 3, dash: 2, fixed: true});
    
    // Ángulo interior en A (70°) - verde
    board.create('angle', [B, A, C], {radius: 0.7, fillColor: '#22c55e', fillOpacity: 0.5, strokeColor: '#22c55e', strokeWidth: 2, name: '70°', label: {fontSize: 13, color: '#22c55e'}});
    
    // Ángulo exterior en A (110°) - naranja (desde B pasando por A hacia la prolongación de CA)
    board.create('angle', [pExt, A, B], {radius: 0.9, fillColor: '#f59e0b', fillOpacity: 0.4, strokeColor: '#f59e0b', strokeWidth: 2, name: '110°', label: {fontSize: 14, color: '#f59e0b', offset: [5, -5]}});
    
    // Etiquetas explicativas
    board.create('text', [4.5, -2, 'Ángulo interior (verde): 70°'], {fontSize: 12, color: '#22c55e', fixed: true});
    board.create('text', [4.5, -2.5, 'Ángulo exterior (naranja): 180° - 70° = 110°'], {fontSize: 12, color: '#f59e0b', fixed: true});
  }
});
</script>

> 💡 **Importante:** El ángulo exterior y su ángulo interior adyacente siempre suman $180°$ porque forman un par lineal.

---

## 📖 Teorema del ángulo exterior

> **Teorema:** El ángulo exterior de un triángulo es igual a la **suma de los dos ángulos interiores no adyacentes**.

> **Fórmula:** Ángulo exterior en $C = \angle A + \angle B$

### Demostración

Sabemos que:
- $\angle A + \angle B + \angle C = 180°$
- Ángulo exterior en $C = 180° - \angle C$

Por lo tanto:
$$
\text{Ángulo exterior en } C = 180° - \angle C = \angle A + \angle B
$$

### Ejemplo 1

Si $\angle A = 50°$ y $\angle B = 60°$, el ángulo exterior en $C$ es:

$$
\angle A + \angle B = 50° + 60° = 110°
$$

### Ejemplo 2

Si $\angle A = 45°$ y $\angle B = 75°$, el ángulo exterior en $C$ es:

$$
45° + 75° = 120°
$$

**Ilustración del Teorema del ángulo exterior:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-teorema-exterior" style="width: 100%; height: 380px; min-height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-teorema-exterior')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-teorema-exterior', {
      boundingbox: [-1, 6, 11, -1.5],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Triángulo con ángulos específicos: A=50°, B=60°, C=70°
    var Ax = 0, Ay = 0;
    var Bx = 6, By = 0;
    var Cx = 4, Cy = 3.2;
    
    var A = board.create('point', [Ax, Ay], {name: 'A', size: 4, color: '#22c55e', fixed: true, label: {fontSize: 14, color: '#22c55e', offset: [-15, -10]}});
    var B = board.create('point', [Bx, By], {name: 'B', size: 4, color: '#3b82f6', fixed: true, label: {fontSize: 14, color: '#3b82f6', offset: [5, -15]}});
    var C = board.create('point', [Cx, Cy], {name: 'C', size: 4, color: '#a855f7', fixed: true, label: {fontSize: 14, color: '#a855f7', offset: [5, 8]}});
    
    // Lados del triángulo
    board.create('segment', [A, B], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    board.create('segment', [B, C], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    board.create('segment', [C, A], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    
    // Prolongación del lado AC más allá de C (en la dirección de A hacia C)
    // Vector de A a C: (Cx - Ax, Cy - Ay)
    var dx = Cx - Ax;  // 4 - 0 = 4
    var dy = Cy - Ay;  // 3.2 - 0 = 3.2
    var len = Math.sqrt(dx*dx + dy*dy);
    // Punto en la prolongación: C + 2 * dirección normalizada
    var extX = Cx + 2 * (dx/len);
    var extY = Cy + 2 * (dy/len);
    var pExt = board.create('point', [extX, extY], {visible: false, fixed: true});
    board.create('segment', [C, pExt], {strokeColor: '#ef4444', strokeWidth: 3, dash: 2, fixed: true});
    
    // Ángulo en A (50°)
    board.create('angle', [B, A, C], {radius: 0.6, fillColor: '#22c55e', fillOpacity: 0.5, strokeColor: '#22c55e', name: '50°', label: {fontSize: 12}});
    
    // Ángulo en B (60°)
    board.create('angle', [C, B, A], {radius: 0.6, fillColor: '#3b82f6', fillOpacity: 0.5, strokeColor: '#3b82f6', name: '60°', label: {fontSize: 12}});
    
    // Ángulo interior en C (70°)
    board.create('angle', [A, C, B], {radius: 0.5, fillColor: '#a855f7', fillOpacity: 0.3, strokeColor: '#a855f7', name: '70°', label: {fontSize: 11}});
    
    // Ángulo exterior en C (110°) - entre B, C y la prolongación de AC
    board.create('angle', [B, C, pExt], {radius: 0.7, fillColor: '#ef4444', fillOpacity: 0.4, strokeColor: '#ef4444', name: '110°', label: {fontSize: 13}});
    
    // Fórmula
    board.create('text', [5, -0.7, 'Ángulo exterior en C = ∠A + ∠B'], {fontSize: 13, color: '#1e293b', fixed: true});
    board.create('text', [5, -1.2, '110° = 50° + 60° ✓'], {fontSize: 13, color: '#ef4444', fixed: true, fontWeight: 'bold'});
  }
});
</script>

> 💡 **Tip visual:** Observa cómo el ángulo exterior (rojo) es exactamente la suma de los dos ángulos interiores no adyacentes (verde + azul).

---

## 📖 Suma de ángulos exteriores

En todo triángulo, la **suma de los ángulos exteriores** (uno en cada vértice) es siempre $360°$.

$$
\text{Ext}_A + \text{Ext}_B + \text{Ext}_C = 360°
$$

### ¿Por qué?

Cada ángulo exterior es $180° - \text{ángulo interior}$. Entonces:

$$
(180° - A) + (180° - B) + (180° - C) = 540° - (A + B + C) = 540° - 180° = 360°
$$

**Ilustración: Los tres ángulos exteriores suman 360°:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-suma-exteriores" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-suma-exteriores')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma-exteriores', {
      boundingbox: [-3, 7, 11, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Triángulo: A=50°, B=70°, C=60°
    var Ax = 0, Ay = 0;
    var Bx = 7, By = 0;
    var Cx = 5, Cy = 4;
    
    var A = board.create('point', [Ax, Ay], {name: 'A', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 14, color: '#1e293b', offset: [-10, -15]}});
    var B = board.create('point', [Bx, By], {name: 'B', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 14, color: '#1e293b', offset: [10, -15]}});
    var C = board.create('point', [Cx, Cy], {name: 'C', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 14, color: '#1e293b', offset: [0, 12]}});
    
    // Lados del triángulo
    board.create('segment', [A, B], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    board.create('segment', [B, C], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    board.create('segment', [C, A], {strokeColor: '#1e293b', strokeWidth: 3, fixed: true});
    
    // Prolongación en A: prolongar BA hacia la izquierda
    var extA = board.create('point', [-2, 0], {visible: false, fixed: true});
    board.create('segment', [A, extA], {strokeColor: '#94a3b8', strokeWidth: 2, dash: 2, fixed: true});
    
    // Prolongación en B: prolongar AB hacia la derecha
    var extB = board.create('point', [9.5, 0], {visible: false, fixed: true});
    board.create('segment', [B, extB], {strokeColor: '#94a3b8', strokeWidth: 2, dash: 2, fixed: true});
    
    // Prolongación en C: prolongar AC más allá de C
    var dxAC = Cx - Ax;
    var dyAC = Cy - Ay;
    var lenAC = Math.sqrt(dxAC*dxAC + dyAC*dyAC);
    var extCx = Cx + 2 * (dxAC/lenAC);
    var extCy = Cy + 2 * (dyAC/lenAC);
    var extC = board.create('point', [extCx, extCy], {visible: false, fixed: true});
    board.create('segment', [C, extC], {strokeColor: '#94a3b8', strokeWidth: 2, dash: 2, fixed: true});
    
    // Ángulo exterior en A (130°) - entre CA y la prolongación de BA
    board.create('angle', [C, A, extA], {radius: 0.7, fillColor: '#22c55e', fillOpacity: 0.5, strokeColor: '#22c55e', name: '130°', label: {fontSize: 12}});
    
    // Ángulo exterior en B (110°) - entre la prolongación de AB y CB
    board.create('angle', [extB, B, C], {radius: 0.7, fillColor: '#3b82f6', fillOpacity: 0.5, strokeColor: '#3b82f6', name: '110°', label: {fontSize: 12}});
    
    // Ángulo exterior en C (120°) - entre CB y la prolongación de AC (EXTERIOR)
    // Cambiamos el orden: de B a extC pasando por C, en sentido antihorario = exterior
    board.create('angle', [B, C, extC], {radius: 0.6, fillColor: '#f59e0b', fillOpacity: 0.5, strokeColor: '#f59e0b', name: '120°', label: {fontSize: 12}});
    
    // Suma
    board.create('text', [4, -1.5, '130° + 110° + 120° = 360° ✓'], {fontSize: 14, color: '#1e293b', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
  }
});
</script>

> 💡 **Dato curioso:** Esta propiedad aplica a TODOS los polígonos. La suma de ángulos exteriores siempre es $360°$, sin importar cuántos lados tenga.

---

## 📖 Aplicaciones prácticas

### Encontrar un ángulo desconocido

Si conocemos dos ángulos de un triángulo, podemos calcular el tercero:

$$
\text{Ángulo desconocido} = 180° - \text{(suma de los otros dos)}
$$

### Verificar si es un triángulo válido

La suma de tres ángulos debe ser exactamente $180°$. Si no lo es, no forman un triángulo.

### Ejemplo: ¿Pueden 40°, 60° y 70° formar un triángulo?

$$
40° + 60° + 70° = 170° \neq 180°
$$

**No**, no pueden formar un triángulo.

**Ilustración: Verificación de triángulos válidos:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-validacion" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-validacion')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-validacion', {
      boundingbox: [-1, 5, 11, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Triángulo VÁLIDO (izquierda): 50° + 60° + 70° = 180°
    var A1 = board.create('point', [0.5, 0.5], {name: '', size: 3, color: '#22c55e', fixed: true});
    var B1 = board.create('point', [4, 0.5], {name: '', size: 3, color: '#22c55e', fixed: true});
    var C1 = board.create('point', [3, 3], {name: '', size: 3, color: '#22c55e', fixed: true});
    
    board.create('polygon', [A1, B1, C1], {fillColor: '#dcfce7', fillOpacity: 0.4, borders: {strokeColor: '#22c55e', strokeWidth: 3}, fixed: true});
    
    board.create('angle', [B1, A1, C1], {radius: 0.4, fillColor: '#22c55e', fillOpacity: 0.5, strokeColor: '#22c55e', name: '50°', label: {fontSize: 10}});
    board.create('angle', [C1, B1, A1], {radius: 0.4, fillColor: '#22c55e', fillOpacity: 0.5, strokeColor: '#22c55e', name: '60°', label: {fontSize: 10}});
    board.create('angle', [A1, C1, B1], {radius: 0.35, fillColor: '#22c55e', fillOpacity: 0.5, strokeColor: '#22c55e', name: '70°', label: {fontSize: 10}});
    
    board.create('text', [2.2, 4.2, '✓ Válido'], {fontSize: 14, color: '#22c55e', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
    board.create('text', [2.2, 3.7, '50°+60°+70°=180°'], {fontSize: 11, color: '#22c55e', fixed: true, anchorX: 'middle'});
    
    // Triángulo INVÁLIDO (derecha): 40° + 60° + 70° = 170° ≠ 180°
    var A2 = board.create('point', [6, 0.5], {name: '', size: 3, color: '#ef4444', fixed: true});
    var B2 = board.create('point', [9.5, 0.5], {name: '', size: 3, color: '#ef4444', fixed: true});
    var C2 = board.create('point', [8.5, 2.8], {name: '', size: 3, color: '#ef4444', fixed: true});
    
    // Segmentos que no cierran (simulación visual de triángulo incompleto)
    board.create('segment', [A2, B2], {strokeColor: '#ef4444', strokeWidth: 3, fixed: true});
    board.create('segment', [B2, C2], {strokeColor: '#ef4444', strokeWidth: 3, fixed: true});
    board.create('segment', [C2, A2], {strokeColor: '#ef4444', strokeWidth: 3, dash: 3, fixed: true}); // Línea punteada = no cierra bien
    
    board.create('text', [7.75, 4.2, '✗ Inválido'], {fontSize: 14, color: '#ef4444', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
    board.create('text', [7.75, 3.7, '40°+60°+70°=170°'], {fontSize: 11, color: '#ef4444', fixed: true, anchorX: 'middle'});
    board.create('text', [7.75, -0.3, '¡No suma 180°!'], {fontSize: 11, color: '#ef4444', fixed: true, anchorX: 'middle'});
  }
});
</script>

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular el tercer ángulo

Calcula el tercer ángulo de cada triángulo:

| $\angle A$ | $\angle B$ | $\angle C$ |
|------------|------------|------------|
| 60° | 80° | |
| 90° | 45° | |
| 55° | 55° | |
| 120° | 30° | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| $\angle A$ | $\angle B$ | $\angle C$ |
|------------|------------|------------|
| 60° | 80° | 40° |
| 90° | 45° | 45° |
| 55° | 55° | 70° |
| 120° | 30° | 30° |

</details>

---

### Ejercicio 2: Ángulo exterior

Calcula el ángulo exterior en el vértice $C$ si:

1. $\angle A = 40°$ y $\angle B = 60°$
2. $\angle A = 55°$ y $\angle B = 75°$
3. $\angle A = 90°$ y $\angle B = 30°$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $40° + 60° = 100°$
2. $55° + 75° = 130°$
3. $90° + 30° = 120°$

(O también: $180° - \angle C$)

</details>

---

### Ejercicio 3: Problema con ecuación

En un triángulo, los ángulos miden $x$, $(x + 20°)$ y $(x + 40°)$. Encuentra el valor de $x$ y las medidas de los tres ángulos.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
x + (x + 20°) + (x + 40°) = 180°
$$

$$
3x + 60° = 180°
$$

$$
3x = 120°
$$

$$
x = 40°
$$

Los ángulos miden:
- $40°$
- $40° + 20° = 60°$
- $40° + 40° = 80°$

Verificación: $40° + 60° + 80° = 180°$ ✓

</details>

---

### Ejercicio 4: Ángulo exterior con ecuación

El ángulo exterior en $C$ de un triángulo mide $130°$. Si $\angle A = 50°$, ¿cuánto mide $\angle B$?

<details>
<summary><strong>Ver respuesta</strong></summary>

Por el teorema del ángulo exterior:

$$
\text{Ángulo exterior en } C = \angle A + \angle B
$$

$$
130° = 50° + \angle B
$$

$$
\angle B = 80°
$$

</details>

---

### Ejercicio 5: Verdadero o Falso

1. La suma de los ángulos interiores de cualquier triángulo es 180°.
2. Un triángulo puede tener un ángulo de 100° y otro de 90°.
3. El ángulo exterior es siempre mayor que cada ángulo interior no adyacente.
4. La suma de los ángulos exteriores de un triángulo es 180°.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero** - Es una propiedad fundamental
2. **Falso** - Sumarían 190°, excediendo 180°
3. **Verdadero** - Es mayor que cada uno (pero igual a su suma)
4. **Falso** - La suma de los ángulos exteriores es 360°

</details>

---
