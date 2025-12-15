# Ángulos entre Paralelas y Secante

Cuando una recta corta a dos rectas paralelas, se forman **ocho ángulos** con propiedades muy especiales.

### 🎯 Resumen rápido (lo que vas a aprender)

| Tipo de ángulos | Relación | Pares |
|-----------------|----------|-------|
| **Correspondientes** | IGUALES | (1,5), (2,6), (3,7), (4,8) |
| **Alternos internos** | IGUALES | (3,5), (4,6) |
| **Alternos externos** | IGUALES | (1,7), (2,8) |
| **Conjugados internos** | Suman 180° | (3,6), (4,5) |
| **Conjugados externos** | Suman 180° | (1,8), (2,7) |

### 📊 Mira los 8 ángulos numerados:

### 📊 Ilustración: Los 8 ángulos

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <span>📊</span>
  <div id="jsxgraph-8angulos" style="width: 100%; height: 350px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-8angulos')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-8angulos', {
      boundingbox: [-6, 6, 6, -6],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Paralela 1 (arriba)
    board.create('line', [[-5, 2], [5, 2]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    
    // Paralela 2 (abajo)
    board.create('line', [[-5, -2], [5, -2]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    
    // Transversal
    board.create('line', [[-3, -5], [3, 5]], {strokeColor: '#ef4444', strokeWidth: 3, fixed: true});
    
    // Puntos de intersección
    var P1 = board.create('point', [1.2, 2], {size: 4, color: '#1e293b', fixed: true, name: ''});
    var P2 = board.create('point', [-1.2, -2], {size: 4, color: '#1e293b', fixed: true, name: ''});
    
    // Etiquetas de ángulos (numerados 1-8)
    board.create('text', [1.8, 2.8, '1'], {fontSize: 14, color: '#22c55e', fixed: true});
    board.create('text', [0.3, 2.8, '2'], {fontSize: 14, color: '#22c55e', fixed: true});
    board.create('text', [0.3, 1.2, '3'], {fontSize: 14, color: '#f59e0b', fixed: true});
    board.create('text', [1.8, 1.2, '4'], {fontSize: 14, color: '#f59e0b', fixed: true});
    
    board.create('text', [-0.6, -1.2, '5'], {fontSize: 14, color: '#f59e0b', fixed: true});
    board.create('text', [-1.9, -1.2, '6'], {fontSize: 14, color: '#f59e0b', fixed: true});
    board.create('text', [-1.9, -2.8, '7'], {fontSize: 14, color: '#22c55e', fixed: true});
    board.create('text', [-0.6, -2.8, '8'], {fontSize: 14, color: '#22c55e', fixed: true});
    
    // Etiquetas de rectas
    board.create('text', [5.2, 2, 'l₁'], {fontSize: 14, color: '#3b82f6', fixed: true});
    board.create('text', [5.2, -2, 'l₂'], {fontSize: 14, color: '#3b82f6', fixed: true});
    board.create('text', [3.2, 5, 't'], {fontSize: 14, color: '#ef4444', fixed: true});
    
    // Leyenda
    board.create('text', [0, -5.2, 'Internos: 3,4,5,6 (naranja) | Externos: 1,2,7,8 (verde)'], {fontSize: 11, color: '#64748b', fixed: true, anchorX: 'middle'});
  }
});
</script>

---

## 📖 La recta secante (o transversal)

Una recta **secante** (también llamada **transversal**) es una recta que corta a otras dos rectas en puntos diferentes.

Cuando la transversal corta a dos rectas paralelas:
- Se forman **4 ángulos** en cada punto de corte
- En total: **8 ángulos**

---

## 📖 Nomenclatura de los ángulos

Los 8 ángulos se pueden clasificar según su posición:

### Ángulos internos

Son los 4 ángulos que están **entre** las dos paralelas.

### Ángulos externos

Son los 4 ángulos que están **fuera** de las dos paralelas (arriba de la superior y abajo de la inferior).

---

## 📖 Tipos de ángulos

### 1. Ángulos Correspondientes

Son ángulos que están en la **misma posición** relativa en cada intersección.

- Uno está arriba de una paralela, el otro arriba de la otra
- Están del **mismo lado** de la transversal

### Ejemplo de correspondientes

Si numeramos los ángulos del 1 al 8:
- $\angle 1$ y $\angle 5$ son correspondientes
- $\angle 2$ y $\angle 6$ son correspondientes
- $\angle 3$ y $\angle 7$ son correspondientes
- $\angle 4$ y $\angle 8$ son correspondientes

---

### 2. Ángulos Alternos Internos

Son ángulos que están:
- **Entre** las dos paralelas (internos)
- En **lados opuestos** de la transversal (alternos)

### Ejemplo de alternos internos

- $\angle 3$ y $\angle 5$ son alternos internos
- $\angle 4$ y $\angle 6$ son alternos internos

---

### 3. Ángulos Alternos Externos

Son ángulos que están:
- **Fuera** de las dos paralelas (externos)
- En **lados opuestos** de la transversal (alternos)

### Ejemplo de alternos externos

- $\angle 1$ y $\angle 7$ son alternos externos
- $\angle 2$ y $\angle 8$ son alternos externos

---

### 4. Ángulos Conjugados Internos (o Co-internos)

Son ángulos que están:
- **Entre** las dos paralelas (internos)
- Del **mismo lado** de la transversal (conjugados)

### Ejemplo de conjugados internos

- $\angle 3$ y $\angle 6$ son conjugados internos
- $\angle 4$ y $\angle 5$ son conjugados internos

---

### 5. Ángulos Conjugados Externos (o Co-externos)

Son ángulos que están:
- **Fuera** de las dos paralelas (externos)
- Del **mismo lado** de la transversal (conjugados)

### Ejemplo de conjugados externos

- $\angle 1$ y $\angle 8$ son conjugados externos
- $\angle 2$ y $\angle 7$ son conjugados externos

---

## 📖 Tabla Resumen

| Tipo | Ubicación | Lado de la transversal |
|------|-----------|------------------------|
| Correspondientes | Misma posición relativa | Mismo lado |
| Alternos internos | Entre las paralelas | Lados opuestos |
| Alternos externos | Fuera de las paralelas | Lados opuestos |
| Conjugados internos | Entre las paralelas | Mismo lado |
| Conjugados externos | Fuera de las paralelas | Mismo lado |

---

## 📖 Ejemplo visual con números

### 📊 Ilustración: Los 8 ángulos


<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <span>📊</span>
  <div id="jsxgraph-8angulos-resumen" style="width: 100%; height: 350px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-8angulos-resumen')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-8angulos-resumen', {
      boundingbox: [-6, 6, 6, -6],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Paralela 1 (arriba)
    board.create('line', [[-5, 2], [5, 2]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    
    // Paralela 2 (abajo)
    board.create('line', [[-5, -2], [5, -2]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    
    // Transversal
    board.create('line', [[-3, -5], [3, 5]], {strokeColor: '#ef4444', strokeWidth: 3, fixed: true});
    
    // Puntos de intersección
    var P1 = board.create('point', [1.2, 2], {size: 4, color: '#1e293b', fixed: true, name: ''});
    var P2 = board.create('point', [-1.2, -2], {size: 4, color: '#1e293b', fixed: true, name: ''});
    
    // Etiquetas de ángulos (numerados 1-8)
    board.create('text', [1.8, 2.8, '1'], {fontSize: 14, color: '#22c55e', fixed: true});
    board.create('text', [0.3, 2.8, '2'], {fontSize: 14, color: '#22c55e', fixed: true});
    board.create('text', [0.3, 1.2, '3'], {fontSize: 14, color: '#f59e0b', fixed: true});
    board.create('text', [1.8, 1.2, '4'], {fontSize: 14, color: '#f59e0b', fixed: true});
    
    board.create('text', [-0.6, -1.2, '5'], {fontSize: 14, color: '#f59e0b', fixed: true});
    board.create('text', [-1.9, -1.2, '6'], {fontSize: 14, color: '#f59e0b', fixed: true});
    board.create('text', [-1.9, -2.8, '7'], {fontSize: 14, color: '#22c55e', fixed: true});
    board.create('text', [-0.6, -2.8, '8'], {fontSize: 14, color: '#22c55e', fixed: true});
    
    // Etiquetas de rectas
    board.create('text', [5.2, 2, 'l₁'], {fontSize: 14, color: '#3b82f6', fixed: true});
    board.create('text', [5.2, -2, 'l₂'], {fontSize: 14, color: '#3b82f6', fixed: true});
    board.create('text', [3.2, 5, 't'], {fontSize: 14, color: '#ef4444', fixed: true});
    
    // Leyenda
    board.create('text', [0, -5.2, 'Internos: 3,4,5,6 (naranja) | Externos: 1,2,7,8 (verde)'], {fontSize: 11, color: '#64748b', fixed: true, anchorX: 'middle'});
  }
});
</script>

| Tipo | Pares de ángulos |
|------|------------------|
| Correspondientes | (1,5), (2,6), (3,7), (4,8) |
| Alternos internos | (3,5), (4,6) |
| Alternos externos | (1,7), (2,8) |
| Conjugados internos | (3,6), (4,5) |
| Conjugados externos | (1,8), (2,7) |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar tipos

Usando la numeración del diagrama anterior, clasifica cada par de ángulos:

1. $\angle 2$ y $\angle 6$
2. $\angle 4$ y $\angle 5$
3. $\angle 3$ y $\angle 5$
4. $\angle 1$ y $\angle 8$
5. $\angle 2$ y $\angle 8$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Correspondientes
2. Conjugados internos
3. Alternos internos
4. Conjugados externos
5. Alternos externos

</details>

---

### Ejercicio 2: Completar

Indica qué tipo de ángulos forman cada par:

| Par | Tipo |
|-----|------|
| $\angle 1$ y $\angle 5$ | |
| $\angle 3$ y $\angle 6$ | |
| $\angle 4$ y $\angle 6$ | |
| $\angle 2$ y $\angle 7$ | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Par | Tipo |
|-----|------|
| $\angle 1$ y $\angle 5$ | Correspondientes |
| $\angle 3$ y $\angle 6$ | Conjugados internos |
| $\angle 4$ y $\angle 6$ | Alternos internos |
| $\angle 2$ y $\angle 7$ | Conjugados externos |

</details>

---

### Ejercicio 3: Ubicación

Si $\angle 3$ es un ángulo interno a la derecha de la transversal, indica:

1. ¿Cuál es su alterno interno?
2. ¿Cuál es su correspondiente?
3. ¿Cuál es su conjugado interno?

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Alterno interno: $\angle 5$ (interno, lado opuesto)
2. Correspondiente: $\angle 7$ (misma posición en la otra paralela)
3. Conjugado interno: $\angle 6$ (interno, mismo lado)

</details>

---
