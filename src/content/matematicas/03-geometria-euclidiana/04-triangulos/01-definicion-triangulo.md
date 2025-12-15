# Definición de Triángulo

El **triángulo** es una de las figuras geométricas más importantes. Es el polígono más simple (tiene el menor número de lados posible) y es la base para construir y analizar figuras más complejas.

### 📊 Mira primero: Un triángulo y sus partes

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <span>📊</span>
  <div id="jsxgraph-triangulo-intro" style="width: 100%; height: 280px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-triangulo-intro')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-triangulo-intro', {
      boundingbox: [-1, 5, 7, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var A = board.create('point', [0, 0], {name: 'A', size: 4, color: '#ef4444', fixed: true, label: {fontSize: 16, color: '#ef4444', offset: [-15, -10]}});
    var B = board.create('point', [6, 0], {name: 'B', size: 4, color: '#ef4444', fixed: true, label: {fontSize: 16, color: '#ef4444', offset: [10, -10]}});
    var C = board.create('point', [3, 4], {name: 'C', size: 4, color: '#ef4444', fixed: true, label: {fontSize: 16, color: '#ef4444', offset: [0, 10]}});
    
    board.create('segment', [A, B], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('segment', [B, C], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    board.create('segment', [C, A], {strokeColor: '#f59e0b', strokeWidth: 3, fixed: true});
    
    board.create('text', [3, -0.5, 'lado c'], {fontSize: 12, color: '#3b82f6', fixed: true});
    board.create('text', [5, 2.2, 'lado a'], {fontSize: 12, color: '#22c55e', fixed: true});
    board.create('text', [0.8, 2.2, 'lado b'], {fontSize: 12, color: '#f59e0b', fixed: true});
  }
});
</script>

> 🎯 **En esta lección:** 3 vértices (A, B, C) + 3 lados + 3 ángulos = Triángulo

---

## 📖 ¿Qué es un triángulo?

Un **triángulo** es un polígono de tres lados.

> **Definición:** Un triángulo es la figura geométrica formada por tres segmentos que unen tres puntos no alineados.

### ¿Por qué "no alineados"?

Si los tres puntos estuvieran en la misma recta, no formarían una figura cerrada, sino simplemente una línea.

---

## 📖 Elementos del triángulo

Todo triángulo tiene los siguientes elementos:

### 1. Vértices

Son los **tres puntos** donde se unen los lados. Se nombran con letras mayúsculas: $A$, $B$, $C$.

### 2. Lados

Son los **tres segmentos** que unen los vértices. Se nombran:
- Con las letras de sus extremos: $\overline{AB}$, $\overline{BC}$, $\overline{CA}$
- O con letras minúsculas: $a$, $b$, $c$ (donde cada lado es opuesto al vértice de la misma letra)

### 3. Ángulos interiores

Son los **tres ángulos** formados por los lados:
- $\angle A$ o $\angle BAC$ (en el vértice $A$)
- $\angle B$ o $\angle ABC$ (en el vértice $B$)  
- $\angle C$ o $\angle BCA$ (en el vértice $C$)

### Tabla de elementos

| Elemento | Cantidad | Notación |
|----------|----------|----------|
| Vértices | 3 | $A$, $B$, $C$ |
| Lados | 3 | $\overline{AB}$, $\overline{BC}$, $\overline{CA}$ o $a$, $b$, $c$ |
| Ángulos interiores | 3 | $\angle A$, $\angle B$, $\angle C$ |

### 📊 Ilustración: Elementos del triángulo

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <span>📊</span>
  <div id="jsxgraph-triangulo-elementos" style="width: 100%; height: 320px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-triangulo-elementos')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-triangulo-elementos', {
      boundingbox: [-1, 5, 7, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Vértices
    var A = board.create('point', [0, 0], {name: 'A', size: 4, color: '#ef4444', fixed: true, label: {fontSize: 16, color: '#ef4444', offset: [-15, -10]}});
    var B = board.create('point', [6, 0], {name: 'B', size: 4, color: '#ef4444', fixed: true, label: {fontSize: 16, color: '#ef4444', offset: [10, -10]}});
    var C = board.create('point', [3, 4], {name: 'C', size: 4, color: '#ef4444', fixed: true, label: {fontSize: 16, color: '#ef4444', offset: [0, 10]}});
    
    // Lados
    board.create('segment', [A, B], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('segment', [B, C], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    board.create('segment', [C, A], {strokeColor: '#f59e0b', strokeWidth: 3, fixed: true});
    
    // Etiquetas de lados
    board.create('text', [3, -0.5, 'c'], {fontSize: 14, color: '#3b82f6', fixed: true});
    board.create('text', [4.8, 2.2, 'a'], {fontSize: 14, color: '#22c55e', fixed: true});
    board.create('text', [1, 2.2, 'b'], {fontSize: 14, color: '#f59e0b', fixed: true});
    
    // Ángulos
    board.create('angle', [B, A, C], {radius: 0.6, fillColor: '#ef4444', fillOpacity: 0.3, strokeColor: '#ef4444'});
    board.create('angle', [C, B, A], {radius: 0.6, fillColor: '#ef4444', fillOpacity: 0.3, strokeColor: '#ef4444'});
    board.create('angle', [A, C, B], {radius: 0.6, fillColor: '#ef4444', fillOpacity: 0.3, strokeColor: '#ef4444'});
  }
});
</script>

> 💡 **Observa:** Los **vértices** (A, B, C) son los puntos rojos. Los **lados** (a, b, c) son los segmentos de colores. El lado $a$ (verde) es opuesto al vértice $A$.

---

## 📖 Notación del triángulo

Un triángulo se nombra con el símbolo $\triangle$ seguido de los tres vértices:

$$
\triangle ABC
$$

Se lee: "triángulo ABC"

### Orden de los vértices

El orden de las letras indica cómo recorremos el triángulo. $\triangle ABC$ y $\triangle BCA$ son el mismo triángulo.

---

## 📖 Lados opuestos a vértices

Cada vértice tiene un lado **opuesto** (el lado que no lo toca):

| Vértice | Lado opuesto |
|---------|--------------|
| $A$ | lado $a$ = $\overline{BC}$ |
| $B$ | lado $b$ = $\overline{AC}$ |
| $C$ | lado $c$ = $\overline{AB}$ |

Esta convención es muy útil para escribir fórmulas de manera clara.

---

## 📖 Propiedades básicas

### Propiedad 1: Los triángulos son rígidos

A diferencia de los cuadriláteros, un triángulo **no se puede deformar** si sus lados tienen longitud fija. Por eso se usan en construcción y estructuras.

### Ejemplo

Las grúas, puentes y techos usan triángulos porque son estructuras estables.

### Propiedad 2: Desigualdad triangular

Para que tres segmentos puedan formar un triángulo, cada lado debe ser **menor que la suma de los otros dos**:

$$
a < b + c, \quad b < a + c, \quad c < a + b
$$

### Ejemplo

¿Pueden tres segmentos de 3 cm, 4 cm y 8 cm formar un triángulo?

- ¿$3 < 4 + 8$? → $3 < 12$ ✓
- ¿$4 < 3 + 8$? → $4 < 11$ ✓
- ¿$8 < 3 + 4$? → $8 < 7$ ✗

**No pueden formar un triángulo** porque $8$ no es menor que $3 + 4$.

---

## 📖 Los triángulos en la vida real

| Ejemplo | ¿Por qué usa triángulos? |
|---------|-------------------------|
| Techos de casas | Estructura estable |
| Torres de alta tensión | Rigidez |
| Bicicletas (marco) | No se deforma |
| Pizza cortada | Cada porción es un triángulo |
| Señales de tránsito | Forma distintiva |
| Pirámides de Egipto | Caras triangulares |

### Ejemplo 1: El marco de una bicicleta

El marco de una bicicleta tiene forma triangular porque es la forma más rígida y ligera para conectar tres puntos.

### Ejemplo 2: Las señales de "ceda el paso"

Las señales triangulares se usan porque su forma única las hace fáciles de reconocer, incluso de lejos.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar elementos

En el triángulo $\triangle PQR$, identifica:

1. Los tres vértices
2. Los tres lados (usa notación de segmentos)
3. El lado opuesto al vértice $Q$
4. Los dos lados que forman el ángulo $\angle P$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Vértices: $P$, $Q$, $R$
2. Lados: $\overline{PQ}$, $\overline{QR}$, $\overline{RP}$
3. Lado opuesto a $Q$: $\overline{PR}$ (o lado $q$)
4. Lados que forman $\angle P$: $\overline{PQ}$ y $\overline{PR}$

</details>

---

### Ejercicio 2: Desigualdad triangular

¿Pueden los siguientes conjuntos de medidas formar un triángulo?

1. 5 cm, 7 cm, 10 cm
2. 2 cm, 3 cm, 6 cm
3. 4 cm, 4 cm, 4 cm
4. 1 cm, 1 cm, 3 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Sí** → $10 < 5 + 7 = 12$ ✓
2. **No** → $6 < 2 + 3 = 5$? → $6 < 5$ ✗
3. **Sí** → $4 < 4 + 4 = 8$ ✓
4. **No** → $3 < 1 + 1 = 2$? → $3 < 2$ ✗

</details>

---

### Ejercicio 3: Notación

Escribe de dos formas diferentes el lado opuesto al vértice $B$ en el triángulo $\triangle ABC$.

<details>
<summary><strong>Ver respuesta</strong></summary>

- Como segmento: $\overline{AC}$
- Como lado: $b$

</details>

---
