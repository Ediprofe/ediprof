# Teorema de Pitágoras

El **Teorema de Pitágoras** es probablemente el teorema más famoso de las matemáticas. Relaciona los lados de un triángulo rectángulo y tiene incontables aplicaciones prácticas.

---

## 📖 Pitágoras de Samos

Pitágoras (570-495 a.C.) fue un matemático y filósofo griego. Aunque el teorema lleva su nombre, los babilonios y egipcios ya conocían esta relación siglos antes.

---

## 📖 Enunciado del teorema

> **Teorema de Pitágoras:** En todo triángulo rectángulo, el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos.

$$
\boxed{c^2 = a^2 + b^2}
$$

Donde:
- $c$ = **hipotenusa** (lado opuesto al ángulo recto, el más largo)
- $a$ y $b$ = **catetos** (los lados que forman el ángulo recto)

**Ilustración: Partes del triángulo rectángulo:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-partes" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initPartes() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-partes')) {
      setTimeout(initPartes, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-partes']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-partes', {
      boundingbox: [-1, 5, 6, -1], // Ajustado para triángulo 3-4-5
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Puntos fijos (Triángulo 3-4-5)
    var A = board.create('point', [0, 0], {name: '', size: 3, color: '#1e293b', fixed: true});
    var B = board.create('point', [4, 0], {name: '', size: 3, color: '#1e293b', fixed: true});
    var C = board.create('point', [0, 3], {name: '', size: 3, color: '#1e293b', fixed: true});
    
    // Triángulo
    board.create('polygon', [A, B, C], {
      fillColor: '#dbeafe', 
      fillOpacity: 0.5, 
      borders: {strokeColor: '#1e293b', strokeWidth: 2}
    });

    // Ángulo Recto
    board.create('angle', [B, A, C], {
      radius: 0.4, 
      orthoType: 'sectordot', 
      fillColor: 'none', 
      strokeColor: '#ef4444', // Rojo para destacar
      strokeWidth: 2,
      fixed: true,
      name: ''
    });
    
    // Etiquetas descriptivas
    // Hipotenusa
    board.create('text', [2.2, 1.7, 'Hipotenusa (c)'], {
      fontSize: 12, 
      color: '#b45309', 
      fixed: true, 
      anchorX: 'left',
      anchorY: 'bottom',
      rotate: 37 // Rotar texto alineado aprox
    });

    // Cateto a (vertical)
    board.create('text', [-0.2, 1.5, 'Cateto (a)'], {
      fontSize: 12, 
      color: '#166534', 
      fixed: true, 
      anchorX: 'right',
      anchorY: 'middle',
      rotate: 90
    });

    // Cateto b (base)
    board.create('text', [2, -0.3, 'Cateto (b)'], {
      fontSize: 12, 
      color: '#1e40af', 
      fixed: true, 
      anchorX: 'middle',
      anchorY: 'top'
    });

    // Nota Ángulo recto
    board.create('text', [0.6, 0.6, '90°'], {
      fontSize: 11, 
      color: '#ef4444', 
      fixed: true
    });

  }
  
  initPartes();
})();
</script>

---

## 📖 Recordatorio: Partes del triángulo rectángulo

| Elemento | Descripción |
|----------|-------------|
| Ángulo recto | El ángulo de 90° |
| Catetos | Los dos lados que forman el ángulo recto |
| Hipotenusa | El lado opuesto al ángulo recto (siempre el más largo) |



---

## 📖 Fórmulas derivadas

### Calcular la hipotenusa

$$
c = \sqrt{a^2 + b^2}
$$

### Calcular un cateto

$$
a = \sqrt{c^2 - b^2}
$$

$$
b = \sqrt{c^2 - a^2}
$$

---

## 📖 Ejemplo 1: Encontrar la hipotenusa

Un triángulo rectángulo tiene catetos de 3 cm y 4 cm. ¿Cuánto mide la hipotenusa?

**Solución:**

$$
c^2 = 3^2 + 4^2 = 9 + 16 = 25
$$

$$
c = \sqrt{25} = 5 \text{ cm}
$$

---

## 📖 Ejemplo 2: Encontrar un cateto

Un triángulo rectángulo tiene hipotenusa de 13 cm y un cateto de 5 cm. ¿Cuánto mide el otro cateto?

**Solución:**

$$
a^2 = c^2 - b^2 = 13^2 - 5^2 = 169 - 25 = 144
$$

$$
a = \sqrt{144} = 12 \text{ cm}
$$

---

## 📖 Ternas pitagóricas

Una **terna pitagórica** es un conjunto de tres números enteros que satisfacen el Teorema de Pitágoras.

### Ternas más conocidas

| Terna | Verificación |
|-------|--------------|
| (3, 4, 5) | $9 + 16 = 25$ |
| (5, 12, 13) | $25 + 144 = 169$ |
| (8, 15, 17) | $64 + 225 = 289$ |
| (7, 24, 25) | $49 + 576 = 625$ |

### Propiedad

Si $(a, b, c)$ es una terna pitagórica, entonces $(ka, kb, kc)$ también lo es para cualquier $k$ entero.

### Ejemplo

$(3, 4, 5) \times 2 = (6, 8, 10)$ también es una terna pitagórica:

$$
6^2 + 8^2 = 36 + 64 = 100 = 10^2 \quad ✓
$$

**Ilustración: Ternas pitagóricas comunes:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-ternas" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initTernas() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-ternas')) {
      setTimeout(initTernas, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-ternas']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-ternas', {
      boundingbox: [-1, 6, 15, -1.5],
      axis: false,
      showCopyright: false,
      showNavigation: false
    });
    
    // Terna 3-4-5
    var A1 = board.create('point', [0.5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
    var B1 = board.create('point', [3.5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
    var C1 = board.create('point', [0.5, 2.75], {name: '', size: 3, color: '#1e293b', fixed: true});
    board.create('polygon', [A1, B1, C1], {fillColor: '#22c55e', fillOpacity: 0.3, borders: {strokeColor: '#22c55e', strokeWidth: 2}, fixed: true});
    board.create('text', [2, 0.2, '4'], {fontSize: 10, color: '#22c55e', fixed: true, anchorX: 'middle'});
    board.create('text', [0.2, 1.6, '3'], {fontSize: 10, color: '#22c55e', fixed: true});
    board.create('text', [2.2, 2, '5'], {fontSize: 10, color: '#22c55e', fixed: true});
    board.create('text', [2, -0.8, '(3,4,5)'], {fontSize: 11, color: '#22c55e', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
    
    // Terna 5-12-13
    var A2 = board.create('point', [5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
    var B2 = board.create('point', [9, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
    var C2 = board.create('point', [5, 2.2], {name: '', size: 3, color: '#1e293b', fixed: true});
    board.create('polygon', [A2, B2, C2], {fillColor: '#3b82f6', fillOpacity: 0.3, borders: {strokeColor: '#3b82f6', strokeWidth: 2}, fixed: true});
    board.create('text', [7, 0.2, '12'], {fontSize: 10, color: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [4.7, 1.3, '5'], {fontSize: 10, color: '#3b82f6', fixed: true});
    board.create('text', [7.2, 1.5, '13'], {fontSize: 10, color: '#3b82f6', fixed: true});
    board.create('text', [7, -0.8, '(5,12,13)'], {fontSize: 11, color: '#3b82f6', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
    
    // Terna 8-15-17
    var A3 = board.create('point', [10, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
    var B3 = board.create('point', [14.5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
    var C3 = board.create('point', [10, 2.9], {name: '', size: 3, color: '#1e293b', fixed: true});
    board.create('polygon', [A3, B3, C3], {fillColor: '#f59e0b', fillOpacity: 0.3, borders: {strokeColor: '#f59e0b', strokeWidth: 2}, fixed: true});
    board.create('text', [12.2, 0.2, '15'], {fontSize: 10, color: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [9.6, 1.7, '8'], {fontSize: 10, color: '#f59e0b', fixed: true});
    board.create('text', [12.5, 2, '17'], {fontSize: 10, color: '#f59e0b', fixed: true});
    board.create('text', [12.2, -0.8, '(8,15,17)'], {fontSize: 11, color: '#f59e0b', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
    
    board.create('text', [7.5, 5, 'Ternas pitagóricas: números enteros que cumplen a² + b² = c²'], {fontSize: 12, color: '#1e293b', fixed: true, anchorX: 'middle'});
  }
  
  initTernas();
})();
</script>

---

## 📖 Aplicaciones prácticas

### Ejemplo 1: Escalera apoyada en pared

Una escalera de 5 m está apoyada en una pared. Su base está a 3 m de la pared. ¿A qué altura llega la escalera?

$$
h^2 = 5^2 - 3^2 = 25 - 9 = 16
$$

$$
h = 4 \text{ m}
$$

**Ilustración: Escalera apoyada en pared:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> Interactivo: Desliza el punto azul de la base
  </div>
  <div id="jsxgraph-escalera" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initEscalera() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-escalera')) {
      setTimeout(initEscalera, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-escalera']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-escalera', {
      boundingbox: [-1, 6, 8, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false
    });
    
    // Pared
    board.create('segment', [[0.5, 0], [0.5, 5.5]], {strokeColor: '#94a3b8', strokeWidth: 6, fixed: true});
    
    // Suelo
    board.create('segment', [[0, 0], [6, 0]], {strokeColor: '#94a3b8', strokeWidth: 4, fixed: true});
    
    // Eje X invisible para restringir movimiento
    var xaxis = board.create('line', [[0,0], [1,0]], {visible: false});
    
    // Punto base (deslizable)
    var B = board.create('glider', [3.5, 0, xaxis], {name: '', size: 5, color: '#3b82f6'});
    
    // Punto base de la pared (fijo)
    var origin = board.create('point', [0.5, 0], {visible: false, fixed: true});
    
    // Calcular punto superior de la escalera
    var T = board.create('point', [0.5, function() {
      var dist = B.X() - 0.5;
      if (dist < 0 || dist > 5) return 0;
      return Math.sqrt(25 - dist*dist);
    }], {name: '', size: 5, color: '#ef4444', fixed: true}); 

    // Escalera
    board.create('segment', [T, B], {strokeColor: '#ef4444', strokeWidth: 4});
    
    // Altura (linea punteada)
    board.create('segment', [origin, T], {strokeColor: '#22c55e', strokeWidth: 3, dash: 2});
    
    // Base (linea punteada)
    board.create('segment', [origin, B], {strokeColor: '#3b82f6', strokeWidth: 3, dash: 2});
    
    // Ángulo recto (construido con puntos invisibles fijos para evitar deformación)
    var p1 = board.create('point', [0.5, 0], {visible: false, fixed: true});
    var p2 = board.create('point', [0.5, 0.3], {visible: false, fixed: true});
    var p3 = board.create('point', [0.8, 0.3], {visible: false, fixed: true});
    var p4 = board.create('point', [0.8, 0], {visible: false, fixed: true});
    
    board.create('polygon', [p1, p2, p3, p4], {
      fillColor: '#1e293b', 
      fillOpacity: 0.3, 
      borders: {strokeColor: '#1e293b', strokeWidth: 1}, 
      fixed: true,
      hasInnerPoints: false
    });
    
    // Etiquetas
    board.create('text', [0.1, function(){ return T.Y()/2; }, function() { 
      return 'h=' + T.Y().toFixed(1) + 'm';
    }], {fontSize: 12, color: '#22c55e'});

    board.create('text', [function(){ return (B.X()+0.5)/2; }, -0.4, function() {
      return (B.X()-0.5).toFixed(1) + 'm';
    }], {fontSize: 12, color: '#3b82f6', anchorX: 'middle'});

    board.create('text', [function(){ return (B.X()+0.5)/2 + 0.3; }, function(){ return T.Y()/2 + 0.3; }, '5m'], {fontSize: 12, color: '#ef4444'});
    
    // Cálculos
    board.create('text', [5.5, 3, function() {
      var base = B.X() - 0.5;
      return 'h² + ' + base.toFixed(1) + '² = 5²';
    }], {fontSize: 12, color: '#1e293b'});
    
    board.create('text', [5.5, 2.3, function() {
       var base = B.X() - 0.5;
       var h2 = 25 - base*base;
       return 'h² = ' + h2.toFixed(1);
    }], {fontSize: 12, color: '#1e293b'});
    
    board.create('text', [5.5, 1.6, function() {
      return 'h = ' + T.Y().toFixed(2) + ' m';
    }], {fontSize: 12, color: '#22c55e', fontWeight: 'bold'});
  }
  
  initEscalera();
})();
</script>

### Ejemplo 2: Diagonal de un rectángulo

Un rectángulo mide 6 m de largo y 8 m de ancho. ¿Cuánto mide su diagonal?

$$
d = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10 \text{ m}
$$

### Ejemplo 3: Distancia entre dos puntos

La distancia entre los puntos $(1, 2)$ y $(4, 6)$ se calcula con Pitágoras:

$$
d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

---

## 📖 El recíproco

El teorema también funciona al revés:

> Si en un triángulo se cumple que $c^2 = a^2 + b^2$, entonces el triángulo es rectángulo.

### Ejemplo

Un triángulo tiene lados 6, 8 y 10. ¿Es rectángulo?

$$
6^2 + 8^2 = 36 + 64 = 100 = 10^2 \quad ✓
$$

Sí, es un triángulo rectángulo.

---

## 📖 Clasificación por la relación pitagórica

| Condición | Tipo de triángulo |
|-----------|-------------------|
| $c^2 = a^2 + b^2$ | Rectángulo |
| $c^2 < a^2 + b^2$ | Acutángulo |
| $c^2 > a^2 + b^2$ | Obtusángulo |

### Ejemplo

Triángulo con lados 4, 5, 6:
- Mayor lado: 6
- $6^2 = 36$
- $4^2 + 5^2 = 16 + 25 = 41$
- $36 < 41$, entonces es **acutángulo**

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular hipotenusa

Encuentra la hipotenusa de triángulos con estos catetos:

1. $a = 6$, $b = 8$
2. $a = 5$, $b = 12$
3. $a = 8$, $b = 15$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $c = \sqrt{36 + 64} = \sqrt{100} = 10$
2. $c = \sqrt{25 + 144} = \sqrt{169} = 13$
3. $c = \sqrt{64 + 225} = \sqrt{289} = 17$

</details>

---

### Ejercicio 2: Calcular cateto

Encuentra el cateto faltante:

1. $c = 10$, $b = 6$, $a = ?$
2. $c = 25$, $a = 7$, $b = ?$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $a = \sqrt{100 - 36} = \sqrt{64} = 8$
2. $b = \sqrt{625 - 49} = \sqrt{576} = 24$

</details>

---

### Ejercicio 3: ¿Es triángulo rectángulo?

Determina si estos triángulos son rectángulos:

1. Lados: 9, 12, 15
2. Lados: 5, 7, 9
3. Lados: 20, 21, 29

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $15^2 = 225$, $9^2 + 12^2 = 81 + 144 = 225$ → **Sí es rectángulo**
2. $9^2 = 81$, $5^2 + 7^2 = 25 + 49 = 74$ → $81 \neq 74$, **No es rectángulo**
3. $29^2 = 841$, $20^2 + 21^2 = 400 + 441 = 841$ → **Sí es rectángulo**

</details>

---

### Ejercicio 4: Problema aplicado

Un campo de fútbol mide 100 m de largo y 64 m de ancho. Un jugador quiere correr en diagonal de una esquina a la opuesta. ¿Qué distancia recorrerá?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
d = \sqrt{100^2 + 64^2} = \sqrt{10000 + 4096} = \sqrt{14096} \approx 118.7 \text{ m}
$$

</details>

---
