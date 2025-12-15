# Teorema de Tales

El **Teorema de Tales** es uno de los resultados más importantes de la geometría. Establece proporciones entre segmentos cuando rectas paralelas cortan a dos rectas transversales.

---

## 📖 Tales de Mileto

Tales de Mileto (624-546 a.C.) fue un matemático y filósofo griego. Según la leyenda, usó este teorema para calcular la altura de las pirámides de Egipto midiendo su sombra.

---

## 📖 Configuración del teorema

Imagina:
- **Dos rectas** (transversales) que salen de un punto $O$ o son paralelas
- **Tres o más rectas paralelas** que las cortan

Los segmentos que se forman en una transversal son **proporcionales** a los segmentos que se forman en la otra.

---

## 📖 Enunciado del Teorema de Tales

> **Teorema:** Si varias rectas paralelas son cortadas por dos transversales, los segmentos que determinan en una transversal son proporcionales a los correspondientes de la otra.

$$
\boxed{\frac{AB}{BC} = \frac{A'B'}{B'C'}}
$$

**Ilustración: Teorema de Tales (paralelas cortando transversales):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-tales-intro" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jsxgraph-tales-intro', {
    boundingbox: [-1, 8, 12, -1],
    axis: false,
    showCopyright: false,
    showNavigation: false
  });
  
  // Transversal 1 (izquierda)
  board.create('segment', [[2, 0.5], [2, 7]], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
  // Transversal 2 (derecha)
  board.create('segment', [[8, 0.5], [8, 7]], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
  
  // Líneas paralelas horizontales
  board.create('segment', [[1, 2], [9, 2]], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true});
  board.create('segment', [[1, 4], [9, 4]], {strokeColor: '#22c55e', strokeWidth: 2, fixed: true});
  board.create('segment', [[1, 6.5], [9, 6.5]], {strokeColor: '#f59e0b', strokeWidth: 2, fixed: true});
  
  // Puntos en transversal 1
  var A = board.create('point', [2, 2], {name: 'A', size: 4, color: '#3b82f6', fixed: true, label: {fontSize: 12, offset: [-15, 0]}});
  var B = board.create('point', [2, 4], {name: 'B', size: 4, color: '#22c55e', fixed: true, label: {fontSize: 12, offset: [-15, 0]}});
  var C = board.create('point', [2, 6.5], {name: 'C', size: 4, color: '#f59e0b', fixed: true, label: {fontSize: 12, offset: [-15, 0]}});
  
  // Puntos en transversal 2
  var Ap = board.create('point', [8, 2], {name: "A'", size: 4, color: '#3b82f6', fixed: true, label: {fontSize: 12, offset: [10, 0]}});
  var Bp = board.create('point', [8, 4], {name: "B'", size: 4, color: '#22c55e', fixed: true, label: {fontSize: 12, offset: [10, 0]}});
  var Cp = board.create('point', [8, 6.5], {name: "C'", size: 4, color: '#f59e0b', fixed: true, label: {fontSize: 12, offset: [10, 0]}});
  
  // Etiquetas de segmentos
  board.create('text', [1.3, 3, '4'], {fontSize: 12, color: '#ef4444', fixed: true});
  board.create('text', [1.3, 5.2, '6'], {fontSize: 12, color: '#a855f7', fixed: true});
  board.create('text', [8.5, 3, '8'], {fontSize: 12, color: '#ef4444', fixed: true});
  board.create('text', [8.5, 5.2, '12'], {fontSize: 12, color: '#a855f7', fixed: true});
  
  // Etiquetas "paralelas"
  board.create('text', [9.5, 2, '∥'], {fontSize: 14, color: '#3b82f6', fixed: true});
  board.create('text', [9.5, 4, '∥'], {fontSize: 14, color: '#22c55e', fixed: true});
  board.create('text', [9.5, 6.5, '∥'], {fontSize: 14, color: '#f59e0b', fixed: true});
  
  board.create('text', [5, -0.3, 'AB/BC = A\'B\'/B\'C\' → 4/6 = 8/12 ✓'], {fontSize: 13, color: '#1e293b', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
});
</script>

---

## 📖 Caso 1: Dos transversales cortadas por paralelas

Si las rectas paralelas $l_1$, $l_2$, $l_3$ cortan a las transversales $r$ y $s$:

$$
\frac{AB}{BC} = \frac{DE}{EF}
$$

### Ejemplo

Si en una transversal los segmentos miden 4 cm y 6 cm, y en la otra el primer segmento mide 8 cm:

$$
\frac{4}{6} = \frac{8}{x} \Rightarrow x = \frac{6 \times 8}{4} = 12 \text{ cm}
$$

---

## 📖 Caso 2: Teorema de Tales en triángulos

Si una recta es **paralela a un lado** de un triángulo y corta a los otros dos lados, entonces divide a estos lados en segmentos **proporcionales**.

### En el triángulo ABC

Si $DE \parallel BC$ y $D$ está en $AB$, $E$ está en $AC$:

$$
\frac{AD}{DB} = \frac{AE}{EC}
$$

También se cumple:

$$
\frac{AD}{AB} = \frac{AE}{AC} = \frac{DE}{BC}
$$

**Ilustración: Tales en triángulos (recta paralela a un lado):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-tales-triangulo" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jsxgraph-tales-triangulo', {
    boundingbox: [-1, 7, 10, -1.5],
    axis: false,
    showCopyright: false,
    showNavigation: false
  });
  
  // Triángulo ABC
  var A = board.create('point', [4.5, 6], {name: 'A', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [0, 10]}});
  var B = board.create('point', [1, 0.5], {name: 'B', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [-10, -10]}});
  var C = board.create('point', [8, 0.5], {name: 'C', size: 4, color: '#1e293b', fixed: true, label: {fontSize: 13, offset: [10, -10]}});
  
  board.create('segment', [A, B], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
  board.create('segment', [A, C], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
  board.create('segment', [B, C], {strokeColor: '#1e293b', strokeWidth: 2, fixed: true});
  
  // Puntos D y E en los lados (DE paralelo a BC)
  var D = board.create('point', [2.75, 3.25], {name: 'D', size: 4, color: '#22c55e', fixed: true, label: {fontSize: 12, color: '#22c55e', offset: [-15, 0]}});
  var E = board.create('point', [6.25, 3.25], {name: 'E', size: 4, color: '#22c55e', fixed: true, label: {fontSize: 12, color: '#22c55e', offset: [10, 0]}});
  
  // Línea DE paralela a BC
  board.create('segment', [D, E], {strokeColor: '#ef4444', strokeWidth: 3, fixed: true});
  
  // Etiquetas
  board.create('text', [1.7, 4.7, 'AD'], {fontSize: 11, color: '#3b82f6', fixed: true});
  board.create('text', [1.5, 1.8, 'DB'], {fontSize: 11, color: '#a855f7', fixed: true});
  board.create('text', [7, 4.7, 'AE'], {fontSize: 11, color: '#3b82f6', fixed: true});
  board.create('text', [7.3, 1.8, 'EC'], {fontSize: 11, color: '#a855f7', fixed: true});
  
  board.create('text', [4.5, 3.6, 'DE ∥ BC'], {fontSize: 11, color: '#ef4444', fixed: true, anchorX: 'middle'});
  board.create('text', [4.5, -0.8, 'AD/DB = AE/EC (proporcionales)'], {fontSize: 13, color: '#1e293b', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
});
</script>

---

## 📖 Ejemplo 1: Calcular un segmento

En el triángulo $ABC$, la recta $DE$ es paralela a $BC$. Si:
- $AD = 3$ cm
- $DB = 6$ cm
- $AE = 4$ cm

¿Cuánto mide $EC$?

**Solución:**

Por el Teorema de Tales:

$$
\frac{AD}{DB} = \frac{AE}{EC}
$$

$$
\frac{3}{6} = \frac{4}{EC}
$$

$$
EC = \frac{6 \times 4}{3} = 8 \text{ cm}
$$

---

## 📖 Ejemplo 2: Calcular la altura de un edificio

Un poste de 3 metros proyecta una sombra de 2 metros. Un edificio proyecta una sombra de 20 metros. ¿Cuánto mide el edificio?

**Solución:**

Los rayos del sol forman triángulos semejantes:

$$
\frac{\text{altura del poste}}{\text{sombra del poste}} = \frac{\text{altura del edificio}}{\text{sombra del edificio}}
$$

$$
\frac{3}{2} = \frac{h}{20}
$$

$$
h = \frac{3 \times 20}{2} = 30 \text{ metros}
$$

**Ilustración: Problema de sombras:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-sombras" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jsxgraph-sombras', {
    boundingbox: [-1, 8, 14, -1.5],
    axis: false,
    showCopyright: false,
    showNavigation: false
  });
  
  // Suelo
  board.create('segment', [[0, 0.5], [13, 0.5]], {strokeColor: '#94a3b8', strokeWidth: 2, fixed: true});
  
  // Poste (3m)
  board.create('segment', [[2, 0.5], [2, 2.5]], {strokeColor: '#22c55e', strokeWidth: 4, fixed: true});
  board.create('text', [1.5, 1.5, '3m'], {fontSize: 11, color: '#22c55e', fixed: true});
  
  // Sombra del poste (2m)
  board.create('segment', [[2, 0.5], [4, 0.5]], {strokeColor: '#64748b', strokeWidth: 3, fixed: true});
  board.create('text', [3, 0.1, '2m'], {fontSize: 10, color: '#64748b', fixed: true, anchorX: 'middle'});
  
  // Edificio (30m = h)
  board.create('segment', [[8, 0.5], [8, 7]], {strokeColor: '#3b82f6', strokeWidth: 5, fixed: true});
  board.create('text', [7.3, 3.5, 'h=?'], {fontSize: 12, color: '#3b82f6', fixed: true});
  
  // Sombra del edificio (20m)
  board.create('segment', [[8, 0.5], [12, 0.5]], {strokeColor: '#64748b', strokeWidth: 3, fixed: true});
  board.create('text', [10, 0.1, '20m'], {fontSize: 10, color: '#64748b', fixed: true, anchorX: 'middle'});
  
  // Rayos del sol
  board.create('segment', [[2, 2.5], [4, 0.5]], {strokeColor: '#f59e0b', strokeWidth: 1, dash: 2, fixed: true});
  board.create('segment', [[8, 7], [12, 0.5]], {strokeColor: '#f59e0b', strokeWidth: 1, dash: 2, fixed: true});
  
  // Sol
  board.create('point', [0.5, 7], {name: '☀️', size: 0, color: 'transparent', fixed: true, label: {fontSize: 20, offset: [0, 0]}});
  
  board.create('text', [6.5, -0.8, '3/2 = h/20 → h = 30 metros'], {fontSize: 13, color: '#1e293b', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
});
</script>

---

## 📖 Recíproco del Teorema de Tales

El teorema también funciona "al revés":

> Si una recta corta a dos lados de un triángulo en segmentos proporcionales, entonces es paralela al tercer lado.

### Uso

Si verificamos que $\frac{AD}{DB} = \frac{AE}{EC}$, entonces podemos concluir que $DE \parallel BC$.

---

## 📖 Aplicaciones del Teorema de Tales

| Aplicación | Uso |
|------------|-----|
| Dividir un segmento en partes iguales | Construcción geométrica |
| Medir distancias inaccesibles | Altura de edificios, ancho de ríos |
| Escalas en mapas | Proporciones |
| Ampliaciones y reducciones | Diseño gráfico |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Aplicar Tales en un triángulo

En el triángulo $ABC$, se traza $DE \parallel BC$ con $D$ en $AB$ y $E$ en $AC$.

Si $AD = 5$, $DB = 10$ y $AC = 24$, calcula $AE$ y $EC$.

<details>
<summary><strong>Ver respuesta</strong></summary>

Por Tales: $\frac{AD}{DB} = \frac{AE}{EC}$, es decir $\frac{5}{10} = \frac{AE}{EC}$

También: $\frac{AD}{AB} = \frac{AE}{AC}$

$$
\frac{5}{15} = \frac{AE}{24} \Rightarrow AE = \frac{5 \times 24}{15} = 8
$$

$$
EC = 24 - 8 = 16
$$

Verificación: $\frac{5}{10} = \frac{8}{16} = \frac{1}{2}$ ✓

</details>

---

### Ejercicio 2: Problema de sombras

Un árbol proyecta una sombra de 15 metros y una persona de 1.8 m proyecta una sombra de 1.2 m (medidas tomadas al mismo tiempo). ¿Cuánto mide el árbol?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\frac{h_{árbol}}{s_{árbol}} = \frac{h_{persona}}{s_{persona}}
$$

$$
\frac{h}{15} = \frac{1.8}{1.2}
$$

$$
h = \frac{1.8 \times 15}{1.2} = \frac{27}{1.2} = 22.5 \text{ metros}
$$

</details>

---

### Ejercicio 3: Tres paralelas

Tres rectas paralelas cortan a dos transversales. En la primera transversal los segmentos miden 6 cm y 9 cm. En la segunda, el primer segmento mide 8 cm. ¿Cuánto mide el segundo segmento?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\frac{6}{9} = \frac{8}{x}
$$

$$
x = \frac{9 \times 8}{6} = 12 \text{ cm}
$$

</details>

---
