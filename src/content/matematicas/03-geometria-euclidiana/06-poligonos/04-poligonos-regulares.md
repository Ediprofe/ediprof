# Polígonos Regulares

Los **polígonos regulares** tienen propiedades especiales que los hacen muy útiles en geometría, arquitectura y diseño. En esta lección profundizamos en sus características.

---

## 📖 Definición

> **Definición:** Un polígono regular es aquel que tiene **todos sus lados iguales** (equilátero) y **todos sus ángulos iguales** (equiángulo).

### Ejemplos

- Triángulo equilátero (3 lados)
- Cuadrado (4 lados)
- Pentágono regular (5 lados)
- Hexágono regular (6 lados)

---

## 📖 Elementos de un polígono regular

### Centro

El **centro** del polígono regular es el punto equidistante de todos los vértices y de todos los lados.

### Radio

El **radio** ($R$) es la distancia desde el centro hasta cualquier vértice. Es el radio de la circunferencia **circunscrita**.

### Apotema

El **apotema** ($a$) es la distancia desde el centro hasta el punto medio de cualquier lado. Es el radio de la circunferencia **inscrita**.

### Ángulo central

El **ángulo central** es el ángulo formado por dos radios consecutivos:

$$
\theta = \frac{360°}{n}
$$

**Ilustración: Elementos del Polígono Regular:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-elementos-regulares" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initElementosReg() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-elementos-regulares')) {
      setTimeout(initElementosReg, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-elementos-regulares']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-elementos-regulares', {
      boundingbox: [-4, 4, 4, -4],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Hexágono Regular
    var r = 2.5;
    var center = [0, 0];
    var points = [];
    for(var i=0; i<6; i++) {
        var ang = (60 * i) * Math.PI / 180;
        points.push(board.create('point', [r*Math.cos(ang), r*Math.sin(ang)], {
            visible:false, fixed:true
        }));
    }
    
    var poly = board.create('polygon', points, {
        fillColor: '#dbeafe', borders: {strokeColor: '#3b82f6', strokeWidth:2}
    });

    // Centro
    var C = board.create('point', [0, 0], {name:'Centro', size:3, color:'#1e293b', fixed:true});
    
    // Radio (R) - desde centro a vértice superior
    var R = board.create('segment', [C, points[1]], {strokeColor: '#ef4444', strokeWidth:2});
    board.create('text', [0.6, 1.5, 'R (Radio)'], {fontSize:11, color:'#ef4444', fontWeight:'bold'});
    
    // Apotema (a) - desde centro perpendicular al lado derecho
    var midPoint = board.create('point', [
        (points[0].X() + points[1].X())/2,
        (points[0].Y() + points[1].Y())/2
    ], {visible:false});
    var A = board.create('segment', [C, midPoint], {strokeColor: '#22c55e', strokeWidth:2, dash:2});
    board.create('text', [0.6, 0.3, 'a (Apotema)'], {fontSize:11, color:'#22c55e', fontWeight:'bold'});
    
    // Ángulo Central
    board.create('angle', [points[0], C, points[1]], {
        radius: 0.6, fillColor: '#f97316', fillOpacity:0.3,
        name: 'θ'
    });
    board.create('text', [-1.2, -0.5, 'Ángulo Central'], {fontSize:10, color:'#f97316'});
  }
  
  initElementosReg();
})();
</script>

---

## 📖 Tabla de elementos

| Polígono regular | n | Ángulo central | Ángulo interior |
|------------------|---|----------------|-----------------|
| Triángulo | 3 | 120° | 60° |
| Cuadrado | 4 | 90° | 90° |
| Pentágono | 5 | 72° | 108° |
| Hexágono | 6 | 60° | 120° |
| Octágono | 8 | 45° | 135° |
| Decágono | 10 | 36° | 144° |
| Dodecágono | 12 | 30° | 150° |

---

## 📖 Relación entre radio y apotema

Para un polígono regular de $n$ lados:

$$
a = R \cos\left(\frac{180°}{n}\right)
$$

### Relación con el lado

Si $l$ es la longitud del lado:

$$
l = 2R \sin\left(\frac{180°}{n}\right)
$$

---

## 📖 Perímetro

El perímetro de un polígono regular es:

$$
P = n \times l
$$

Donde $l$ es la longitud de cada lado.

---

## 📖 Área de un polígono regular

La fórmula general del área es:

$$
A = \frac{P \times a}{2} = \frac{n \times l \times a}{2}
$$

Donde:
- $P$ = perímetro
- $a$ = apotema
- $n$ = número de lados
- $l$ = longitud de cada lado

### Interpretación

El área es igual a la suma de las áreas de $n$ triángulos, cada uno con:
- Base = lado del polígono
- Altura = apotema

**Ilustración: Composición del Área:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-area-composicion" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initAreaComp() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-area-composicion')) {
      setTimeout(initAreaComp, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-area-composicion']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-area-composicion', {
      boundingbox: [-4, 4, 4, -4],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Hexágono Regular
    var r = 2.5;
    var center = [0, 0];
    var points = [];
    for(var i=0; i<6; i++) {
        var ang = (60 * i) * Math.PI / 180;
        points.push(board.create('point', [r*Math.cos(ang), r*Math.sin(ang)], {
            visible:false, fixed:true
        }));
    }
    
    var poly = board.create('polygon', points, {
        fillColor: 'none', borders: {strokeColor: '#3b82f6', strokeWidth:2}
    });

    // Centro
    var C = board.create('point', [0, 0], {name:'', size:2, color:'#1e293b', fixed:true});
    
    // Radios a todos los vértices (creando triángulos)
    var colors = ['#bfdbfe', '#fef3c7', '#bfdbfe', '#fef3c7', '#bfdbfe', '#fef3c7'];
    for(var i=0; i<6; i++) {
        var next = (i+1)%6;
        // Crear triángulo
        var tri = board.create('polygon', [C, points[i], points[next]], {
            fillColor: colors[i], fillOpacity:0.6,
            borders: {strokeColor: '#94a3b8', strokeWidth:1}
        });
    }
    
    // Etiquetar un triángulo (el superior)
    var mid0 = [(points[0].X() + points[1].X())/2, (points[0].Y() + points[1].Y())/2];
    board.create('text', [mid0[0], mid0[1]+0.3, 'l (lado)'], {fontSize:10, color:'#3b82f6', fontWeight:'bold'});
    board.create('text', [0, 0.8, 'a'], {fontSize:10, color:'#22c55e', fontWeight:'bold'});
    
    board.create('text', [0, -3.2, '6 triángulos: A = 6 × (l × a / 2)'], {anchorX:'middle', fontSize:11, fontWeight:'bold', color:'#1e3a8a'});
  }
  
  initAreaComp();
})();
</script>

---

## 📖 Casos especiales

### Triángulo equilátero

Para un triángulo de lado $l$:

$$
A = \frac{l^2 \sqrt{3}}{4}
$$

### Cuadrado

Para un cuadrado de lado $l$:

$$
A = l^2
$$

### Hexágono regular

Para un hexágono de lado $l$:

$$
A = \frac{3l^2\sqrt{3}}{2}
$$

---

## 📖 Circunferencias asociadas

### Circunferencia circunscrita

Pasa por **todos los vértices**. Su radio es $R$.

### Circunferencia inscrita

Es **tangente a todos los lados**. Su radio es $a$ (apotema).

**Ilustración: Circunferencias Inscrita y Circunscrita:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.5rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.25rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-circunferencias" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
(function() {
  function initCircunf() {
    if (typeof JXG === 'undefined' || !document.getElementById('jsxgraph-circunferencias')) {
      setTimeout(initCircunf, 100);
      return;
    }
    
    if (JXG.boards['jsxgraph-circunferencias']) return;

    var board = JXG.JSXGraph.initBoard('jsxgraph-circunferencias', {
      boundingbox: [-4, 4, 4, -4],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      keepaspectratio: true
    });
    
    // Pentágono Regular
    var R = 2.5; // Radio circunscrito
    var center = [0, 0];
    var points = [];
    for(var i=0; i<5; i++) {
        var ang = (72 * i + 18) * Math.PI / 180;
        points.push(board.create('point', [R*Math.cos(ang), R*Math.sin(ang)], {
            size:2, color:'#1e293b', fixed:true, name:''
        }));
    }
    
    var poly = board.create('polygon', points, {
        fillColor: '#dbeafe', fillOpacity:0.3, borders: {strokeColor: '#3b82f6', strokeWidth:2}
    });

    // Centro
    var C = board.create('point', [0, 0], {name:'Centro', size:3, color:'#1e293b', fixed:true});
    
    // Circunferencia Circunscrita (pasa por vértices)
    var circCirc = board.create('circle', [C, R], {
        strokeColor: '#ef4444', strokeWidth:2, dash:2
    });
    
    // Apotema (radio inscrito)
    var a = R * Math.cos(Math.PI / 5); // Para pentágono: cos(36°)
    
    // Circunferencia Inscrita (tangente a lados)
    var circInsc = board.create('circle', [C, a], {
        strokeColor: '#22c55e', strokeWidth:2, dash:2
    });
    
    // Etiquetas
    board.create('text', [2, 2.8, 'Circunscrita (R)'], {fontSize:11, color:'#ef4444', fontWeight:'bold'});
    board.create('text', [1.2, 1.2, 'Inscrita (a)'], {fontSize:11, color:'#22c55e', fontWeight:'bold'});
  }
  
  initCircunf();
})();
</script>

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Ángulo central

Calcula el ángulo central de:

1. Pentágono regular
2. Octágono regular
3. Decágono regular

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\theta = \frac{360°}{5} = 72°$
2. $\theta = \frac{360°}{8} = 45°$
3. $\theta = \frac{360°}{10} = 36°$

</details>

---

### Ejercicio 2: Perímetro

Calcula el perímetro de:

1. Hexágono regular de lado 5 cm
2. Octágono regular de lado 4 cm
3. Decágono regular de lado 3 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $P = 6 \times 5 = 30$ cm
2. $P = 8 \times 4 = 32$ cm
3. $P = 10 \times 3 = 30$ cm

</details>

---

### Ejercicio 3: Área

Calcula el área de polígonos regulares con:

1. Perímetro = 24 cm, apotema = 4 cm
2. Perímetro = 36 cm, apotema = 6 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \frac{24 \times 4}{2} = 48$ cm²
2. $A = \frac{36 \times 6}{2} = 108$ cm²

</details>

---

### Ejercicio 4: Problema completo

Un hexágono regular tiene lado de 6 cm y apotema de aproximadamente 5.2 cm. Calcula:

1. El perímetro
2. El área
3. El ángulo central

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Perímetro = $6 \times 6 = 36$ cm
2. Área = $\frac{36 \times 5.2}{2} = 93.6$ cm²
3. Ángulo central = $\frac{360°}{6} = 60°$

</details>

---

### Ejercicio 5: Encontrar el lado

Un pentágono regular tiene perímetro de 45 cm. ¿Cuánto mide cada lado?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
l = \frac{P}{n} = \frac{45}{5} = 9 \text{ cm}
$$

</details>

---
