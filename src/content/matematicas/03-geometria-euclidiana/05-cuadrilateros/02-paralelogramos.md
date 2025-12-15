# Paralelogramos

Un **paralelogramo** es un cuadrilátero con dos pares de lados paralelos. Es la base de muchas figuras importantes como el rectángulo, el rombo y el cuadrado.

---

## 📖 Definición

> **Definición:** Un paralelogramo es un cuadrilátero cuyos lados opuestos son **paralelos**.

$$
AB \parallel CD \quad \text{y} \quad BC \parallel AD
$$

**Ilustración: Propiedades del Paralelogramo:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-paralelogramo" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initParalelogramo() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-paralelogramo')) {
      setTimeout(initParalelogramo, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-paralelogramo']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-paralelogramo', {
      boundingbox: [-2, 5, 10, -3],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos fijos
    // Base 6. Altura 3. Skew 2.
    // A(0,0), B(6,0), D(2,3), C(8,3).
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, -10]}});
    var B = board.create('point', [6, 0], {name: 'B', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, -10]}});
    var C = board.create('point', [8, 3], {name: 'C', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, 10]}});
    var D = board.create('point', [2, 3], {name: 'D', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, 10]}});
    
    // Polígono
    var poly = board.create('polygon', [A, B, C, D], {
      fillColor: '#dbeafe', 
      fillOpacity: 0.5, 
      borders: {strokeColor: '#3b82f6', strokeWidth: 2}
    });

    // Ángulos
    var angleStyle = {radius: 0.5, fillOpacity: 0.3};
    // A y C son agudos. B y D son obtusos.
    // Coloreamos pares iguales.
    // Orden CCW para angulos interiores: (Previous, Vertex, Next)
    // A es (0,0). Prev es D, Next es B. Angle(B, A, D)? No, Angle(Vertex) uses 3 points. Angle(p1, p2, p3): Angle at p2. From p1 to p3 counter-clock-wise.
    // Vector A->B (6,0). Vector A->D (2,3).
    // B(6,0) es 0 deg. D(2,3) es approx 56 deg.
    // De B a D CCW es 56 deg (interno).
    // Angle(B, A, D) -> empieza en AB, va a AD. Correcto.
    board.create('angle', [B, A, D], { ...angleStyle, fillColor: '#22c55e', strokeColor: '#166534', name: 'α' });
    
    // C(8,3). Prev B(6,0). Next D(2,3).
    // Vector C->B (-2, -3). Vector C->D (-6, 0).
    // CB angle approx 236 deg. CD angle 180 deg.
    // De D a B CCW. 180 -> 236. Delta 56 deg. (Interno).
    // Angle(D, C, B).
    board.create('angle', [D, C, B], { ...angleStyle, fillColor: '#22c55e', strokeColor: '#166534', name: 'α' });
    
    // B(6,0). Prev A, Next C.
    // Vector B->A (-6,0). Vector B->C (2,3).
    // BA 180 deg. BC approx 56 deg (360+56=416).
    // De C a A CCW?
    // C (approx 56) -> A (180). Delta 124 deg.
    // Angle(C, B, A).
    board.create('angle', [C, B, A], { ...angleStyle, fillColor: '#f97316', strokeColor: '#c2410c', name: 'β' });
    
    // D(2,3). Prev C(8,3). Next A(0,0).
    // Vector D->C (6,0). Vector D->A (-2,-3).
    // DC 0 deg. DA approx 236.
    // De A a C CCW?
    // A (236) -> C (0/360). Delta 124.
    // Angle(A, D, C).
    board.create('angle', [A, D, C], { ...angleStyle, fillColor: '#f97316', strokeColor: '#c2410c', name: 'β' });
    
    // Etiquetas de lados (mostrando igualdad)
    // Lados paralelos horizontales (a)
    board.create('text', [3, -0.3, 'a'], {color: '#3b82f6', fontSize: 12, fixed: true, anchorX: 'middle'});
    board.create('text', [5, 3.3, 'a'], {color: '#3b82f6', fontSize: 12, fixed: true, anchorX: 'middle'});

    // Lados paralelos inclinados (b)
    board.create('text', [0.8, 1.5, 'b'], {color: '#3b82f6', fontSize: 12, fixed: true, anchorX: 'right'});
    board.create('text', [7.2, 1.5, 'b'], {color: '#3b82f6', fontSize: 12, fixed: true, anchorX: 'left'});

    // Altura (opcional pero instructiva para el área)
    var H = board.create('point', [2, 0], {visible: false});
    board.create('segment', [D, H], {strokeColor: '#64748b', dash: 2});
    board.create('text', [2.2, 1.5, 'h'], {color: '#64748b', fontSize: 11, fixed: true});
    // Ángulo recto de la altura (Removido por petición del usuario - se sobreentiende)
    // board.create('angle', [D, H, B], {orthoType: 'sectordot', radius: 0.3, fillColor: 'none', strokeColor: '#64748b'});

  }
  
  initParalelogramo();
})();
</script>

---

## 📖 Propiedades de los lados

### Propiedad 1: Lados opuestos iguales

Los lados opuestos de un paralelogramo son **congruentes** (tienen la misma longitud).

$$
AB = CD \quad \text{y} \quad BC = AD
$$

### Ejemplo

Si $AB = 8$ cm y $BC = 5$ cm, entonces:
- $CD = 8$ cm
- $AD = 5$ cm
- Perímetro = $2(8) + 2(5) = 26$ cm

---

## 📖 Propiedades de los ángulos

### Propiedad 2: Ángulos opuestos iguales

Los ángulos opuestos de un paralelogramo son **iguales**.

$$
\angle A = \angle C \quad \text{y} \quad \angle B = \angle D
$$

### Propiedad 3: Ángulos consecutivos suplementarios

Dos ángulos consecutivos (adyacentes) suman **180°**.

$$
\angle A + \angle B = 180°
$$

### Ejemplo

Si $\angle A = 70°$, entonces:
- $\angle C = 70°$ (opuesto)
- $\angle B = 180° - 70° = 110°$ (consecutivo)
- $\angle D = 110°$ (opuesto a B)

---

## 📖 Propiedades de las diagonales

### Propiedad 4: Las diagonales se bisecan

Las diagonales de un paralelogramo se **cortan en su punto medio**.

Si $M$ es el punto de intersección:

$$
AM = MC \quad \text{y} \quad BM = MD
$$

### Ejemplo

Si la diagonal $AC = 12$ cm, entonces $AM = MC = 6$ cm.

**Ilustración: Las diagonales se bisecan:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-diagonales" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initDiagonales() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-diagonales')) {
      setTimeout(initDiagonales, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-diagonales']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-diagonales', {
        boundingbox: [-2, 6, 12, -3],
        axis: false,
        showCopyright: false,
        showNavigation: false,
        keepaspectratio: true
    });

    // Puntos fijos para un paralelogramo atractivo
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, -10]}});
    var B = board.create('point', [7, 0], {name: 'B', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, -10]}});
    var C = board.create('point', [10, 4], {name: 'C', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, 10]}});
    var D = board.create('point', [3, 4], {name: 'D', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, 10]}});

    // Polígono
    board.create('polygon', [A, B, C, D], {
        fillColor: '#f1f5f9', 
        borders: {strokeColor: '#64748b', strokeWidth: 1}
    });

    // Diagonales
    var AC = board.create('segment', [A, C], {strokeColor: '#ef4444', strokeWidth: 2});
    var BD = board.create('segment', [B, D], {strokeColor: '#3b82f6', strokeWidth: 2});

    // Punto medio M (Calculado explícitamente)
    var Mx = (A.X() + C.X()) / 2;
    var My = (A.Y() + C.Y()) / 2;
    var M = board.create('point', [Mx, My], {name: 'M', size: 3, color: '#f97316', fixed: true, label:{autoPosition:true}});

    // Marcas de igualdad (ticks) o etiquetas
    // AM = MC
    board.create('text', [(A.X()+Mx)/2, (A.Y()+My)/2 + 0.3, '6'], {color: '#ef4444', anchorX:'middle'});
    board.create('text', [(C.X()+Mx)/2, (C.Y()+My)/2 + 0.3, '6'], {color: '#ef4444', anchorX:'middle'});

    // BM = MD
    // Usamos ticks visuales para diferenciar
    board.create('text', [(D.X()+Mx)/2, (D.Y()+My)/2, '||'], {color: '#3b82f6', anchorX:'middle', rotation: 45});
    board.create('text', [(B.X()+Mx)/2, (B.Y()+My)/2, '||'], {color: '#3b82f6', anchorX:'middle', rotation: 45});

  }
  
  initDiagonales();
})();
</script>

---

## 📖 Resumen de propiedades

| Propiedad | Descripción |
|-----------|-------------|
| Lados opuestos | Paralelos e iguales |
| Ángulos opuestos | Iguales |
| Ángulos consecutivos | Suplementarios (suman 180°) |
| Diagonales | Se bisecan mutuamente |

---

## 📖 Área del paralelogramo

El área de un paralelogramo se calcula como:

$$
A = b \times h
$$

Donde:
- $b$ = base (cualquier lado)
- $h$ = altura (distancia perpendicular entre las bases)

### Ejemplo

Si $b = 10$ cm y $h = 6$ cm:

$$
A = 10 \times 6 = 60 \text{ cm}^2
$$

**Ilustración: Área del Paralelogramo:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-area" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initArea() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-area')) {
      setTimeout(initArea, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-area']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-area', {
        boundingbox: [-2, 8, 12, -2],
        axis: false,
        showCopyright: false,
        showNavigation: false,
        keepaspectratio: true
    });

    // Ejemplo: b=10, h=6.
    // Usamos coordenadas exactas para representar esto.
    // A(0,0), B(10,0). Altura 6.
    // Skew opcional. D(2, 6) -> C(12, 6).
    
    var A = board.create('point', [0, 0], {name: 'A', size: 2, color: '#1e293b', fixed: true, label: {visible:false}});
    var B = board.create('point', [10, 0], {name: 'B', size: 2, color: '#1e293b', fixed: true, label: {visible:false}});
    var C = board.create('point', [12, 6], {name: 'C', size: 2, color: '#1e293b', fixed: true, label: {visible:false}});
    var D = board.create('point', [2, 6], {name: 'D', size: 2, color: '#1e293b', fixed: true, label: {visible:false}});

    // Área coloreada
    board.create('polygon', [A, B, C, D], {
        fillColor: '#22c55e', 
        fillOpacity: 0.3,
        borders: {strokeColor: '#166534', strokeWidth: 2}
    });

    // Base
    board.create('text', [5, -0.6, 'b = 10 cm'], {fontSize: 12, fontWeight: 'bold', color: '#166534', anchorX: 'middle', fixed: true});

    // Altura (segmento perpendicular)
    // Desde D(2,6) hasta proyección en eje x: (2,0). Llamemos H.
    var H = board.create('point', [2, 0], {name: 'H', visible: false, fixed: true});
    board.create('segment', [D, H], {strokeColor: '#f97316', strokeWidth: 2, dash: 2});
    
    // Etiqueta altura
    board.create('text', [1.5, 3, 'h = 6 cm'], {fontSize: 12, fontWeight: 'bold', color: '#f97316', anchorX: 'right', fixed: true});

    // Nota del área
    board.create('text', [6, 3, 'Área = 60 cm²'], {fontSize: 14, fontWeight: 'bold', color: '#22c55e', anchorX: 'middle', fixed: true});

  }
  
  initArea();
})();
</script>

---

## 📖 Casos especiales de paralelogramos

| Figura | Característica adicional |
|--------|-------------------------|
| Rectángulo | 4 ángulos rectos |
| Rombo | 4 lados iguales |
| Cuadrado | 4 ángulos rectos Y 4 lados iguales |

> **Nota:** El cuadrado es a la vez rectángulo Y rombo.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular lados

En un paralelogramo $ABCD$, $AB = 12$ cm y $BC = 7$ cm. Calcula:

1. La longitud de $CD$
2. La longitud de $AD$
3. El perímetro

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $CD = AB = 12$ cm (lados opuestos iguales)
2. $AD = BC = 7$ cm (lados opuestos iguales)
3. Perímetro = $2(12) + 2(7) = 24 + 14 = 38$ cm

</details>

---

### Ejercicio 2: Calcular ángulos

En un paralelogramo, $\angle A = 65°$. Calcula los demás ángulos.

<details>
<summary><strong>Ver respuestas</strong></summary>

- $\angle C = 65°$ (opuesto a A)
- $\angle B = 180° - 65° = 115°$ (consecutivo a A)
- $\angle D = 115°$ (opuesto a B)

Verificación: $65° + 115° + 65° + 115° = 360°$ ✓

</details>

---

### Ejercicio 3: Diagonales

Las diagonales de un paralelogramo miden 14 cm y 10 cm. ¿Cuánto mide cada segmento desde un vértice hasta el punto de intersección?

<details>
<summary><strong>Ver respuestas</strong></summary>

Como las diagonales se bisecan:
- Diagonal de 14 cm: cada mitad mide $14 \div 2 = 7$ cm
- Diagonal de 10 cm: cada mitad mide $10 \div 2 = 5$ cm

</details>

---

### Ejercicio 4: Área

Calcula el área de un paralelogramo con:

1. Base = 15 cm, altura = 8 cm
2. Base = 20 cm, altura = 12 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = 15 \times 8 = 120$ cm²
2. $A = 20 \times 12 = 240$ cm²

</details>

---
