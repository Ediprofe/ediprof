# Trapezoide

Un **trapezoide** es un cuadrilátero sin lados paralelos. Es la forma más general de cuadrilátero.

---

## 📖 Definición

> **Definición:** Un trapezoide es un cuadrilátero que **no tiene ningún par de lados paralelos**.

También se conoce como cuadrilátero **irregular** o cuadrilátero **general**.

**Ilustración: Trapezoide General:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-trapezoide-general" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initTrapezoideGen() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-trapezoide-general')) {
      setTimeout(initTrapezoideGen, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-trapezoide-general']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-trapezoide-general', {
      boundingbox: [-2, 6, 8, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos fijos (Irregular)
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, -10]}});
    var B = board.create('point', [7, 1], {name: 'B', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, -10]}});
    var C = board.create('point', [5, 5], {name: 'C', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, 10]}});
    var D = board.create('point', [2, 4], {name: 'D', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, 10]}});
    
    // Polígono
    board.create('polygon', [A, B, C, D], {
      fillColor: '#dbeafe', 
      fillOpacity: 0.5, 
      borders: {strokeColor: '#3b82f6', strokeWidth: 2}
    });

    // Ángulos internos (para mostrar que son diferentes)
    var angleStyle = {orthoType: 'sectordot', radius: 0.5, fillColor: '#22c55e', strokeColor: '#166534', fillOpacity: 0.3};
    // Orden CCW para angulos interiores
    board.create('angle', [B, A, D], { ...angleStyle, name: 'α' });
    board.create('angle', [C, B, A], { ...angleStyle, name: 'β' });
    board.create('angle', [D, C, B], { ...angleStyle, name: 'γ' });
    board.create('angle', [A, D, C], { ...angleStyle, name: 'δ' });

    board.create('text', [3.5, -1, 'Ningún lado paralelo'], {fontSize: 12, color: '#1e293b', fixed: true, anchorX: 'middle'});
  }
  
  initTrapezoideGen();
})();
</script>

---

## 📖 Propiedades básicas

### Suma de ángulos

Como todo cuadrilátero:

$$
\angle A + \angle B + \angle C + \angle D = 360°
$$

### Diagonales

- Tiene 2 diagonales
- En general, no tienen propiedades especiales (no se bisecan, no son iguales, no son perpendiculares)

---

## 📖 Tipos de trapezoides

### Trapezoide simétrico (o deltoide/cometa)

Un cuadrilátero con dos pares de lados consecutivos iguales, pero que no son paralelos.

**Propiedades del deltoide:**
- Una diagonal es eje de simetría
- Las diagonales son perpendiculares
- Una diagonal biseca a la otra

### Trapezoide asimétrico

No tiene lados iguales ni ninguna simetría especial.

---

## 📖 El deltoide (cometa)

El **deltoide** es un caso especial importante de trapezoide.

### Definición

> Un deltoide es un cuadrilátero con dos pares de lados **consecutivos** iguales.

$$
AB = AD \quad \text{y} \quad BC = DC
$$

**Ilustración: El Deltoide (Cometa):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-deltoide" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initDeltoide() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-deltoide')) {
      setTimeout(initDeltoide, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-deltoide']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-deltoide', {
      boundingbox: [-4, 8, 4, -4],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos fijos (Simetría eje Y)
    // A (arriba): (0, 6). C (abajo): (0, -2).
    // B (derecha): (3, 3). D (izquierda): (-3, 3).
    // Diagonales se cruzan en (0,3).
    
    var A = board.create('point', [0, 6], {name: 'A', size: 3, color: '#1e293b', fixed: true, label: {offset: [0, 10], anchorX: 'middle'}});
    var B = board.create('point', [3, 3], {name: 'B', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, 0]}});
    var C = board.create('point', [0, -2], {name: 'C', size: 3, color: '#1e293b', fixed: true, label: {offset: [0, -10], anchorX: 'middle'}});
    var D = board.create('point', [-3, 3], {name: 'D', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, 0]}});
    
    // Polígono
    board.create('polygon', [A, B, C, D], {
      fillColor: '#fef3c7', 
      fillOpacity: 0.5, 
      borders: {strokeColor: '#f59e0b', strokeWidth: 2}
    });

    // Diagonales
    // AC (Eje de simetría)
    board.create('segment', [A, C], {strokeColor: '#f97316', strokeWidth: 2, dash: 2});
    // BD (Perpendicular)
    board.create('segment', [B, D], {strokeColor: '#f97316', strokeWidth: 2, dash: 2});
    
    // Intersección M
    var M = board.create('point', [0, 3], {visible: false, name: 'M'});
    
    // Ángulo recto intersección (Interior: A(90) -> D(180) CCW = 90)
    board.create('angle', [A, M, D], {orthoType: 'sectordot', radius: 0.4, fillColor: 'none', strokeColor: '#f97316'});
    board.create('text', [0.4, 3.4, '90°'], {color: '#f97316', fontSize: 11});
    
    // Ticks de lados iguales
    var tickStyle = {color: '#d97706', anchorX: 'middle', fontSize: 12};
    // AB = AD (Arriba)
    board.create('text', [-1.5, 4.8, '|'], { ...tickStyle, rotation: -45});
    board.create('text', [1.5, 4.8, '|'], { ...tickStyle, rotation: 45});
    
    // CB = CD (Abajo)
    board.create('text', [-1.5, 0.5, '||'], { ...tickStyle, rotation: 60});
    board.create('text', [1.5, 0.5, '||'], { ...tickStyle, rotation: -60});

  }
  
  initDeltoide();
})();
</script>

### Propiedades del deltoide

| Propiedad | Descripción |
|-----------|-------------|
| Simetría | Una diagonal es eje de simetría |
| Diagonales | Perpendiculares |
| Diagonal mayor | Biseca a la diagonal menor |
| Ángulos | Los ángulos entre lados desiguales son iguales |

### Área del deltoide

$$
A = \frac{d_1 \times d_2}{2}
$$

(Igual que el rombo, ya que las diagonales son perpendiculares)

---

## 📖 Área de un trapezoide general

Para calcular el área de un trapezoide irregular, se puede:

### Método 1: Dividir en triángulos

Trazar una diagonal y calcular el área de los dos triángulos resultantes.

**Ilustración: Área por Triangulación:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-area-trapezoide" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initAreaTrap() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-area-trapezoide')) {
      setTimeout(initAreaTrap, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-area-trapezoide']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-area-trapezoide', {
      boundingbox: [-2, 6, 8, -2],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos fijos (Mismo irregular)
    var A = board.create('point', [0, 0], {name: 'A', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, -10]}});
    var B = board.create('point', [7, 1], {name: 'B', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, -10]}});
    var C = board.create('point', [5, 5], {name: 'C', size: 3, color: '#1e293b', fixed: true, label: {offset: [10, 10]}});
    var D = board.create('point', [2, 4], {name: 'D', size: 3, color: '#1e293b', fixed: true, label: {offset: [-10, 10]}});
    
    // Diagonal AC divide en 2 triángulos
    // Triángulo 1: ABC
    board.create('polygon', [A, B, C], {
      fillColor: '#bfdbfe', // Azul claro
      fillOpacity: 0.6, 
      borders: {strokeColor: 'none'}
    });
    
    // Triángulo 2: ADC
    board.create('polygon', [A, D, C], {
      fillColor: '#bbf7d0', // Verde claro
      fillOpacity: 0.6, 
      borders: {strokeColor: 'none'}
    });
    
    // Borde exterior
    board.create('line', [A, B], {strokeColor: '#334155', strokeWidth: 2, straightFirst:false, straightLast:false});
    board.create('line', [B, C], {strokeColor: '#334155', strokeWidth: 2, straightFirst:false, straightLast:false});
    board.create('line', [C, D], {strokeColor: '#334155', strokeWidth: 2, straightFirst:false, straightLast:false});
    board.create('line', [D, A], {strokeColor: '#334155', strokeWidth: 2, straightFirst:false, straightLast:false});

    // Diagonal punteada
    board.create('line', [A, C], {strokeColor: '#64748b', strokeWidth: 2, dash: 2, straightFirst:false, straightLast:false});
    
    // Etiquetas de Área
    // Centroide aprox T1
    board.create('text', [4, 1.5, 'Área 1'], {fontSize: 14, color: '#1e3a8a', anchorX: 'middle'});
    // Centroide aprox T2
    board.create('text', [2, 2.5, 'Área 2'], {fontSize: 14, color: '#14532d', anchorX: 'middle'});
    
    board.create('text', [3.5, 5.5, 'A_total = Área 1 + Área 2'], {fontSize: 14, fontWeight: 'bold', color: '#1e293b', anchorX: 'middle', fixed: true});
  }
  
  initAreaTrap();
})();
</script>

### Método 2: Fórmula de Herón generalizada

Usando las coordenadas de los vértices o la fórmula del área para cuadriláteros.

### Método 3: Fórmula del topógrafo

Si conocemos las coordenadas $(x_1, y_1), (x_2, y_2), (x_3, y_3), (x_4, y_4)$:

$$
A = \frac{1}{2}|x_1(y_2 - y_4) + x_2(y_3 - y_1) + x_3(y_4 - y_2) + x_4(y_1 - y_3)|
$$

---

## 📖 Comparación: Trapezoide vs otros cuadriláteros

| Cuadrilátero | Pares de lados paralelos |
|--------------|-------------------------|
| Paralelogramo | 2 pares |
| Trapecio | 1 par |
| Trapezoide | 0 pares |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificar

Indica si cada cuadrilátero es paralelogramo, trapecio o trapezoide:

1. Ningún lado paralelo
2. Dos pares de lados paralelos
3. Un par de lados paralelos
4. Una cometa (deltoide)

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Trapezoide**
2. **Paralelogramo**
3. **Trapecio**
4. **Trapezoide** (específicamente, un deltoide)

</details>

---

### Ejercicio 2: Ángulos

En un trapezoide, tres ángulos miden 85°, 95° y 110°. ¿Cuánto mide el cuarto ángulo?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\angle D = 360° - 85° - 95° - 110° = 70°
$$

</details>

---

### Ejercicio 3: Área del deltoide

Calcula el área de un deltoide con diagonales de 12 cm y 8 cm.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A = \frac{12 \times 8}{2} = \frac{96}{2} = 48 \text{ cm}^2
$$

</details>

---

### Ejercicio 4: Verdadero o Falso

1. Todo trapezoide tiene exactamente un par de lados paralelos.
2. Un deltoide tiene diagonales perpendiculares.
3. La suma de los ángulos de un trapezoide es 360°.
4. Las diagonales de cualquier trapezoide se bisecan.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** - No tiene ningún par de lados paralelos
2. **Verdadero**
3. **Verdadero** - Como todo cuadrilátero
4. **Falso** - Solo en paralelogramos

</details>

---
