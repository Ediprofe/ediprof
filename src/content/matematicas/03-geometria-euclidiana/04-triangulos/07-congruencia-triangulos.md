# Congruencia de Triángulos

Dos triángulos son **congruentes** cuando tienen la misma forma y el mismo tamaño. En esta lección estudiaremos qué significa la congruencia y los criterios para determinar si dos triángulos son congruentes.

---

## 📖 ¿Qué es la congruencia?

Dos figuras son **congruentes** cuando tienen exactamente la **misma forma** y el **mismo tamaño**.

> **Definición:** Dos triángulos son congruentes si sus tres lados y sus tres ángulos son respectivamente iguales.

### Símbolo

$$
\triangle ABC \cong \triangle DEF
$$

Se lee: "El triángulo ABC es congruente al triángulo DEF"

### ¿Qué significa "respectivamente iguales"?

Significa que los elementos correspondientes son iguales:
- Lado $AB$ = Lado $DE$
- Lado $BC$ = Lado $EF$
- Lado $CA$ = Lado $FD$
- $\angle A = \angle D$
- $\angle B = \angle E$
- $\angle C = \angle F$

**Ilustración: Triángulos congruentes:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-congruentes" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jsxgraph-congruentes', {
    boundingbox: [-1, 5, 13, -1],
    axis: false,
    showCopyright: false,
    showNavigation: false
  });
  
  // Triángulo ABC
  var A = board.create('point', [0.5, 0.5], {name: 'A', size: 4, color: '#22c55e', fixed: true, label: {fontSize: 12, color: '#22c55e', offset: [-10, -10]}});
  var B = board.create('point', [4.5, 0.5], {name: 'B', size: 4, color: '#22c55e', fixed: true, label: {fontSize: 12, color: '#22c55e', offset: [5, -10]}});
  var C = board.create('point', [2.5, 3.5], {name: 'C', size: 4, color: '#22c55e', fixed: true, label: {fontSize: 12, color: '#22c55e', offset: [0, 10]}});
  board.create('polygon', [A, B, C], {fillColor: '#dcfce7', fillOpacity: 0.4, borders: {strokeColor: '#22c55e', strokeWidth: 2}, fixed: true});
  board.create('text', [2.5, -0.3, '△ABC'], {fontSize: 13, color: '#22c55e', fixed: true, anchorX: 'middle'});
  
  // Triángulo DEF (congruente)
  var D = board.create('point', [7, 0.5], {name: 'D', size: 4, color: '#3b82f6', fixed: true, label: {fontSize: 12, color: '#3b82f6', offset: [-10, -10]}});
  var E = board.create('point', [11, 0.5], {name: 'E', size: 4, color: '#3b82f6', fixed: true, label: {fontSize: 12, color: '#3b82f6', offset: [5, -10]}});
  var F = board.create('point', [9, 3.5], {name: 'F', size: 4, color: '#3b82f6', fixed: true, label: {fontSize: 12, color: '#3b82f6', offset: [0, 10]}});
  board.create('polygon', [D, E, F], {fillColor: '#dbeafe', fillOpacity: 0.4, borders: {strokeColor: '#3b82f6', strokeWidth: 2}, fixed: true});
  board.create('text', [9, -0.3, '△DEF'], {fontSize: 13, color: '#3b82f6', fixed: true, anchorX: 'middle'});
  
  // Símbolo de congruencia
  board.create('text', [5.75, 2, '≅'], {fontSize: 24, color: '#1e293b', fixed: true, anchorX: 'middle'});
  
  board.create('text', [6, 4.3, 'Misma forma + Mismo tamaño = CONGRUENTES'], {fontSize: 12, color: '#1e293b', fixed: true, anchorX: 'middle'});
});
</script>

---

## 📖 Los criterios de congruencia

No es necesario verificar los 6 elementos (3 lados + 3 ángulos) para saber si dos triángulos son congruentes. Existen **criterios** que permiten demostrarlo con menos información.

---

## 📖 Criterio LLL (Lado-Lado-Lado)

Dos triángulos son congruentes si sus **tres lados** son respectivamente iguales.

$$
\boxed{LLL: \text{ Si } a = a', b = b', c = c' \Rightarrow \triangle ABC \cong \triangle A'B'C'}
$$

### Ejemplo

Si el triángulo $ABC$ tiene lados de 3, 4 y 5 cm, y el triángulo $DEF$ también tiene lados de 3, 4 y 5 cm, entonces son congruentes por LLL.

**Ilustración: Criterio LLL (Lado-Lado-Lado):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-lll" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jsxgraph-lll', {
    boundingbox: [-1, 5, 13, -1.5],
    axis: false,
    showCopyright: false,
    showNavigation: false
  });
  
  // Triángulo 1 (3-4-5)
  var A1 = board.create('point', [0.5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B1 = board.create('point', [4.5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C1 = board.create('point', [0.5, 3.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A1, B1, C1], {fillColor: '#fef3c7', fillOpacity: 0.4, borders: {strokeColor: '#1e293b', strokeWidth: 2}, fixed: true});
  
  // Etiquetas de lados
  board.create('text', [2.5, 0.2, '4'], {fontSize: 12, color: '#ef4444', fixed: true, anchorX: 'middle'});
  board.create('text', [0.1, 2, '3'], {fontSize: 12, color: '#3b82f6', fixed: true});
  board.create('text', [2.8, 2.3, '5'], {fontSize: 12, color: '#22c55e', fixed: true});
  
  // Triángulo 2 (3-4-5) - idéntico
  var A2 = board.create('point', [7, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B2 = board.create('point', [11, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C2 = board.create('point', [7, 3.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A2, B2, C2], {fillColor: '#fef3c7', fillOpacity: 0.4, borders: {strokeColor: '#1e293b', strokeWidth: 2}, fixed: true});
  
  board.create('text', [9, 0.2, '4'], {fontSize: 12, color: '#ef4444', fixed: true, anchorX: 'middle'});
  board.create('text', [6.6, 2, '3'], {fontSize: 12, color: '#3b82f6', fixed: true});
  board.create('text', [9.3, 2.3, '5'], {fontSize: 12, color: '#22c55e', fixed: true});
  
  board.create('text', [5.75, 2, '≅'], {fontSize: 24, color: '#1e293b', fixed: true, anchorX: 'middle'});
  board.create('text', [6, -1, 'LLL: Los 3 lados son iguales → Congruentes'], {fontSize: 12, color: '#1e293b', fixed: true, anchorX: 'middle'});
});
</script>

---

## 📖 Criterio LAL (Lado-Ángulo-Lado)

Dos triángulos son congruentes si tienen **dos lados iguales** y el **ángulo comprendido** (entre esos lados) también es igual.

$$
\boxed{LAL: \text{ Si } a = a', \angle B = \angle B', c = c' \Rightarrow \triangle ABC \cong \triangle A'B'C'}
$$

### Importante

El ángulo debe ser el que está **entre** los dos lados considerados.

### Ejemplo

Si dos triángulos tienen:
- Un lado de 5 cm
- Un ángulo de 60° (entre los dos lados)
- Otro lado de 7 cm

Entonces son congruentes por LAL.

**Ilustración: Criterio LAL (Lado-Ángulo-Lado):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-lal" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jsxgraph-lal', {
    boundingbox: [-1, 5, 13, -1.5],
    axis: false,
    showCopyright: false,
    showNavigation: false
  });
  
  // Triángulo 1
  var A1 = board.create('point', [0.5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B1 = board.create('point', [4, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C1 = board.create('point', [1.5, 3.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A1, B1, C1], {fillColor: '#dbeafe', fillOpacity: 0.4, borders: {strokeColor: '#1e293b', strokeWidth: 2}, fixed: true});
  
  // Ángulo destacado
  board.create('angle', [B1, A1, C1], {radius: 0.5, fillColor: '#f59e0b', fillOpacity: 0.5, strokeColor: '#f59e0b', name: '60°', label: {fontSize: 10}});
  board.create('text', [2.2, 0.2, '5'], {fontSize: 12, color: '#ef4444', fixed: true});
  board.create('text', [0.7, 2, '7'], {fontSize: 12, color: '#3b82f6', fixed: true});
  
  // Triángulo 2
  var A2 = board.create('point', [7, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B2 = board.create('point', [10.5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C2 = board.create('point', [8, 3.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A2, B2, C2], {fillColor: '#dbeafe', fillOpacity: 0.4, borders: {strokeColor: '#1e293b', strokeWidth: 2}, fixed: true});
  
  board.create('angle', [B2, A2, C2], {radius: 0.5, fillColor: '#f59e0b', fillOpacity: 0.5, strokeColor: '#f59e0b', name: '60°', label: {fontSize: 10}});
  board.create('text', [8.7, 0.2, '5'], {fontSize: 12, color: '#ef4444', fixed: true});
  board.create('text', [7.2, 2, '7'], {fontSize: 12, color: '#3b82f6', fixed: true});
  
  board.create('text', [5.75, 2, '≅'], {fontSize: 24, color: '#1e293b', fixed: true, anchorX: 'middle'});
  board.create('text', [6, -1, 'LAL: 2 lados + ángulo entre ellos iguales → Congruentes'], {fontSize: 12, color: '#1e293b', fixed: true, anchorX: 'middle'});
});
</script>

---

## 📖 Criterio ALA (Ángulo-Lado-Ángulo)

Dos triángulos son congruentes si tienen **un lado igual** y los **dos ángulos adyacentes** a ese lado también son iguales.

$$
\boxed{ALA: \text{ Si } \angle A = \angle A', c = c', \angle B = \angle B' \Rightarrow \triangle ABC \cong \triangle A'B'C'}
$$

### Ejemplo

Si dos triángulos tienen:
- Un ángulo de 40°
- Un lado de 8 cm (entre los dos ángulos)
- Un ángulo de 70°

Entonces son congruentes por ALA.

**Ilustración: Criterio ALA (Ángulo-Lado-Ángulo):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-ala" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jsxgraph-ala', {
    boundingbox: [-1, 5, 13, -1.5],
    axis: false,
    showCopyright: false,
    showNavigation: false
  });
  
  // Triángulo 1
  var A1 = board.create('point', [0.5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B1 = board.create('point', [4.5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C1 = board.create('point', [2.5, 3.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A1, B1, C1], {fillColor: '#dcfce7', fillOpacity: 0.4, borders: {strokeColor: '#1e293b', strokeWidth: 2}, fixed: true});
  
  // Ángulos destacados
  board.create('angle', [B1, A1, C1], {radius: 0.5, fillColor: '#a855f7', fillOpacity: 0.5, strokeColor: '#a855f7', name: '40°', label: {fontSize: 10}});
  board.create('angle', [C1, B1, A1], {radius: 0.5, fillColor: '#f59e0b', fillOpacity: 0.5, strokeColor: '#f59e0b', name: '70°', label: {fontSize: 10}});
  board.create('text', [2.5, 0.2, '8'], {fontSize: 12, color: '#ef4444', fixed: true, anchorX: 'middle'});
  
  // Triángulo 2
  var A2 = board.create('point', [7, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B2 = board.create('point', [11, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C2 = board.create('point', [9, 3.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A2, B2, C2], {fillColor: '#dcfce7', fillOpacity: 0.4, borders: {strokeColor: '#1e293b', strokeWidth: 2}, fixed: true});
  
  board.create('angle', [B2, A2, C2], {radius: 0.5, fillColor: '#a855f7', fillOpacity: 0.5, strokeColor: '#a855f7', name: '40°', label: {fontSize: 10}});
  board.create('angle', [C2, B2, A2], {radius: 0.5, fillColor: '#f59e0b', fillOpacity: 0.5, strokeColor: '#f59e0b', name: '70°', label: {fontSize: 10}});
  board.create('text', [9, 0.2, '8'], {fontSize: 12, color: '#ef4444', fixed: true, anchorX: 'middle'});
  
  board.create('text', [5.75, 2, '≅'], {fontSize: 24, color: '#1e293b', fixed: true, anchorX: 'middle'});
  board.create('text', [6, -1, 'ALA: 2 ángulos + lado entre ellos iguales → Congruentes'], {fontSize: 12, color: '#1e293b', fixed: true, anchorX: 'middle'});
});
</script>

---

## 📖 Criterio LLA (Lado-Lado-Ángulo) - Caso especial

Este criterio solo funciona cuando el ángulo es el **opuesto al lado mayor**.

En la práctica, se usa más el caso especial para triángulos **rectángulos** (ver abajo).

---

## 📖 Criterio para triángulos rectángulos

Para triángulos rectángulos existe un criterio adicional:

### Criterio Hipotenusa-Cateto

Dos triángulos rectángulos son congruentes si tienen **la hipotenusa y un cateto** respectivamente iguales.

---

## 📖 Tabla resumen de criterios

| Criterio | Elementos iguales | Observación |
|----------|-------------------|-------------|
| LLL | 3 lados | El más básico |
| LAL | 2 lados + ángulo entre ellos | El ángulo debe estar "en medio" |
| ALA | 2 ángulos + lado entre ellos | El lado debe estar "en medio" |
| Hipotenusa-Cateto | Hipotenusa + 1 cateto | Solo para triángulos rectángulos |

---

## 📖 Ejemplo completo

**Problema:** Demostrar que los triángulos $ABC$ y $DEF$ son congruentes si:
- $AB = DE = 5$ cm
- $\angle B = \angle E = 50°$
- $BC = EF = 7$ cm

**Solución:**

Tenemos:
- Lado $AB = DE$ ✓
- Ángulo $\angle B = \angle E$ ✓ (el ángulo está entre los dos lados)
- Lado $BC = EF$ ✓

Por el criterio **LAL**, los triángulos son congruentes:

$$
\triangle ABC \cong \triangle DEF
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar el criterio

¿Qué criterio de congruencia se aplica en cada caso?

1. Ambos triángulos tienen lados de 6, 8 y 10 cm
2. Ambos tienen ángulos de 30° y 60° con un lado de 5 cm entre ellos
3. Ambos tienen lados de 4 y 7 cm con un ángulo de 90° entre ellos

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **LLL** (tres lados iguales)
2. **ALA** (dos ángulos y el lado entre ellos)
3. **LAL** (dos lados y el ángulo entre ellos)

</details>

---

### Ejercicio 2: ¿Son congruentes?

Determina si los triángulos son congruentes:

Triángulo 1: Lados de 5, 7, 9 cm
Triángulo 2: Lados de 5, 9, 7 cm

<details>
<summary><strong>Ver respuesta</strong></summary>

**Sí**, son congruentes por **LLL**.

Los lados son los mismos (5, 7, 9), solo están listados en diferente orden.

</details>

---

### Ejercicio 3: Verdadero o Falso

1. Dos triángulos con los mismos tres ángulos son congruentes.
2. Si dos triángulos tienen un lado de 10 cm y ángulos de 60° y 50°, son congruentes.
3. Dos triángulos equiláteros con el mismo perímetro son congruentes.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** - Pueden tener la misma forma pero diferente tamaño (semejantes, no congruentes)
2. **Verdadero** - Por ALA (el tercer ángulo sería 70°, y el lado está "entre" los ángulos)
3. **Verdadero** - Si tienen el mismo perímetro, tienen los mismos lados (LLL)

</details>

---
