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

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-general" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
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
      boundingbox: [-2, 6, 8, -2],
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

    // Ángulos
    var angleStyle = {radius: 0.5, fillColor: '#22c55e', fillOpacity: 0.3, strokeColor: '#166534'};
    board.create('angle', [D, A, B], { ...angleStyle, name: 'α' });
    board.create('angle', [A, B, C], { ...angleStyle, name: 'β' });
    board.create('angle', [B, C, D], { ...angleStyle, name: 'γ' });
    board.create('angle', [C, D, A], { ...angleStyle, name: 'δ' });
    
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

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-tipos" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
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
      boundingbox: [-1, 5, 11, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // --- CONVEXO ---
    var A1 = board.create('point', [0, 0], {name: '', size: 2, color: '#1e293b', fixed: true});
    var B1 = board.create('point', [3, 0], {name: '', size: 2, color: '#1e293b', fixed: true});
    var C1 = board.create('point', [3.5, 3], {name: '', size: 2, color: '#1e293b', fixed: true});
    var D1 = board.create('point', [0.5, 2.5], {name: '', size: 2, color: '#1e293b', fixed: true});
    
    board.create('polygon', [A1, B1, C1, D1], {fillColor: '#22c55e', fillOpacity: 0.3, borders: {strokeColor: '#166534'}});
    board.create('segment', [A1, C1], {strokeColor: '#166534', dash: 2}); // Diagonal interna
    board.create('text', [1.8, -1, 'Convexo'], {fontSize: 12, fontWeight: 'bold', color: '#166534', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, -1.5, 'Diagonales internas'], {fontSize: 10, color: '#1e293b', fixed: true, anchorX: 'middle'});

    // --- CÓNCAVO ---
    var A2 = board.create('point', [6, 0], {name: '', size: 2, color: '#1e293b', fixed: true});
    var B2 = board.create('point', [10, 0], {name: '', size: 2, color: '#1e293b', fixed: true});
    var C2 = board.create('point', [8, 1.5], {name: '', size: 2, color: '#1e293b', fixed: true}); // Vértice entrante
    var D2 = board.create('point', [8, 3.5], {name: '', size: 2, color: '#1e293b', fixed: true});
    
    board.create('polygon', [A2, B2, C2, D2], {fillColor: '#ef4444', fillOpacity: 0.3, borders: {strokeColor: '#b91c1c'}});
    
    // Diagonal externa
    board.create('segment', [D2, C2], {visible: false}); // Ocultar segmento del polígono para no confundir con diagonal
    board.create('segment', [A2, B2], {visible: true, strokeColor: '#b91c1c'});
    
    // Diagonal que sale fuera (A2-B2 ya es lado, D2-C2 es lado... diagonal es D2-A2? No, diagonal une opuestos: D2-A2 y C2-B2 son lados. Diagonales: D2-B2 y A2-C2... )
    // Hmmm en este "delta head" (o punta de flecha), A, B, C(entrante), D(punta arriba).
    // Orden puntos: A(6,0) -> B(10,0) -> C(8,1.5) -> D(8,3.5)
    // Lados: AB, BC, CD, DA.
    // Opuestos: A y C. B y D.
    // Diagonal AC: (6,0) a (8,1.5). Pasa por dentro.
    // Diagonal BD: (10,0) a (8,3.5). Pasa por FUERA si el orden es A-B-C-D?
    // Espera, si es A->B->C->D, A(6,0), B(10,0), C(8,1.5), D(8,3.5).
    // Poligono cruzado? No.
    // Dibujémoslo mentalmente: Base AB grande. C está "arriba" en medio. D más arriba en medio.
    // Es como una punta de flecha apuntando arriba, pero C está 'metido'.
    // Vértices A, B, C, D.
    // Si recorro A->B->C->D->A.
    // A(6,0) -> B(10,0) -> C(8,1.5) (sube e izquierda) -> D(8,3.5) (sube) -> A (baja izq).
    // C es el vértice cóncavo (ángulo > 180 interior).
    // Diagonal une opuestos: A con C, B con D.
    // A-C: (6,0)-(8,1.5). Dentro.
    // B-D: (10,0)-(8,3.5). Dentro?
    // El punto cóncavo es C? Ángulo en C es interior del polígono. El interior está "a la izquierda" del recorrido A->B->C->D ?
    // A->B (derecha). B->C (izq arriba). C->D (arriba). D->A (abajo izq).
    // El "interior" es lo encerrado.
    // El ángulo en C (B-C-D) ... vector CB (-2, 1.5), CD (0, 2).
    // Producto cruz...
    // Mejor usaremos una forma clásica de "boomerang" o "delta".
    // A(6,0), B(8,1), C(10,0), D(8,4). Orden A,B,C,D.
    // Vértice B es el entrante.
    // Diagonal AC une (6,0) y (10,0). Pasa por (8,0). El punto B está en (8,1).
    // Entonces AC pasa por DEBAJO de B? No, si B está en (8,1), el segmento (6,0)-(10,0) está en y=0. B está "encima".
    // Si el polígono es A-B-C-D-A.
    // El interior depende del winding.
    // Usemos la forma clásica:
    // A(6,3), B(8,1) [entrante], C(10,3), D(8,5).
    // Diagonal AC (horizontal y=3). B está en y=1. D en y=5.
    // Si B es el vértice entrante, la diagonal AC pasa "fuera" del polígono (porque B se "metió" hacia D).
    
    // Puntos redefinidos para Cóncavo:
    var P1 = board.create('point', [6, 3], {name: '', size: 2, color: '#1e293b', fixed: true});
    var P2 = board.create('point', [8, 1.5], {name: '', size: 2, color: '#1e293b', fixed: true}); // Entrante
    var P3 = board.create('point', [10, 3], {name: '', size: 2, color: '#1e293b', fixed: true});
    var P4 = board.create('point', [8, 5], {name: '', size: 2, color: '#1e293b', fixed: true});
    
    board.create('polygon', [P1, P2, P3, P4], {fillColor: '#ef4444', fillOpacity: 0.3, borders: {strokeColor: '#b91c1c'}});
    
    // Diagonal externa P1-P3
    board.create('segment', [P1, P3], {strokeColor: '#b91c1c', dash: 2}); 
    
    board.create('text', [8, -1, 'Cóncavo'], {fontSize: 12, fontWeight: 'bold', color: '#b91c1c', fixed: true, anchorX: 'middle'});
    board.create('text', [8, -1.5, 'Diagonal externa'], {fontSize: 10, color: '#1e293b', fixed: true, anchorX: 'middle'});
    
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
