# Semejanza de Triángulos

Dos triángulos son **semejantes** cuando tienen la misma forma, aunque no necesariamente el mismo tamaño. Es como una "copia a escala" de un triángulo.

---

## 📖 ¿Qué es la semejanza?

Dos triángulos son **semejantes** si:
- Sus **ángulos correspondientes son iguales**
- Sus **lados correspondientes son proporcionales**

> **Definición:** Dos triángulos son semejantes si uno es una ampliación o reducción del otro.

### Símbolo

$$
\triangle ABC \sim \triangle DEF
$$

Se lee: "El triángulo ABC es semejante al triángulo DEF"

---

## 📖 Diferencia entre congruencia y semejanza

| Característica | Congruencia | Semejanza |
|----------------|-------------|-----------|
| Forma | Igual | Igual |
| Tamaño | Igual | Puede ser diferente |
| Lados | Iguales | Proporcionales |
| Ángulos | Iguales | Iguales |
| Símbolo | $\cong$ | $\sim$ |

> **Nota:** Todo par de triángulos congruentes son también semejantes, pero no al revés.

**Ilustración: Congruencia vs Semejanza:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-semejanza-intro" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jsxgraph-semejanza-intro', {
    boundingbox: [-1, 6, 14, -1.5],
    axis: false,
    showCopyright: false,
    showNavigation: false
  });
  
  // Triángulo original (pequeño)
  var A1 = board.create('point', [1, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B1 = board.create('point', [3.5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C1 = board.create('point', [2.25, 2.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A1, B1, C1], {fillColor: '#22c55e', fillOpacity: 0.3, borders: {strokeColor: '#22c55e', strokeWidth: 2}, fixed: true});
  board.create('text', [2.25, -0.3, 'Original'], {fontSize: 11, color: '#22c55e', fixed: true, anchorX: 'middle'});
  
  // Triángulo congruente (mismo tamaño)
  var A2 = board.create('point', [5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B2 = board.create('point', [7.5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C2 = board.create('point', [6.25, 2.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A2, B2, C2], {fillColor: '#3b82f6', fillOpacity: 0.3, borders: {strokeColor: '#3b82f6', strokeWidth: 2}, fixed: true});
  board.create('text', [6.25, -0.3, 'Congruente'], {fontSize: 11, color: '#3b82f6', fixed: true, anchorX: 'middle'});
  board.create('text', [6.25, -0.8, '(= tamaño)'], {fontSize: 10, color: '#3b82f6', fixed: true, anchorX: 'middle'});
  
  // Triángulo semejante (diferente tamaño, misma forma)
  var A3 = board.create('point', [9, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B3 = board.create('point', [13, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C3 = board.create('point', [11, 4.2], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A3, B3, C3], {fillColor: '#f59e0b', fillOpacity: 0.3, borders: {strokeColor: '#f59e0b', strokeWidth: 2}, fixed: true});
  board.create('text', [11, -0.3, 'Semejante'], {fontSize: 11, color: '#f59e0b', fixed: true, anchorX: 'middle'});
  board.create('text', [11, -0.8, '(k=1.6)'], {fontSize: 10, color: '#f59e0b', fixed: true, anchorX: 'middle'});
  
  board.create('text', [7, 5.3, 'Semejante = misma FORMA | Congruente = misma forma + mismo TAMAÑO'], {fontSize: 12, color: '#1e293b', fixed: true, anchorX: 'middle'});
});
</script>

---

## 📖 Razón de semejanza

La **razón de semejanza** ($k$) es el factor por el cual se multiplican los lados de un triángulo para obtener los lados del otro.

$$
k = \frac{a'}{a} = \frac{b'}{b} = \frac{c'}{c}
$$

### Ejemplo

Si un triángulo tiene lados de 3, 4, 5 cm y otro tiene lados de 6, 8, 10 cm:

$$
k = \frac{6}{3} = \frac{8}{4} = \frac{10}{5} = 2
$$

La razón de semejanza es $k = 2$ (el segundo triángulo es el doble del primero).

**Ilustración: Razón de semejanza k=2:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-razon" style="width: 100%; height: 380px; min-height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jsxgraph-razon', {
    boundingbox: [-1, 6, 14, -1.5],
    axis: false,
    showCopyright: false,
    showNavigation: false
  });
  
  // Triángulo pequeño (3-4-5)
  var A1 = board.create('point', [1, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B1 = board.create('point', [4, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C1 = board.create('point', [1, 3], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A1, B1, C1], {fillColor: '#dbeafe', fillOpacity: 0.4, borders: {strokeColor: '#3b82f6', strokeWidth: 2}, fixed: true});
  
 board.create('text', [2.5, 0.2, '4'], {fontSize: 12, color: '#ef4444', fixed: true, anchorX: 'middle'});
  board.create('text', [0.6, 1.7, '3'], {fontSize: 12, color: '#22c55e', fixed: true});
  board.create('text', [2.8, 2, '5'], {fontSize: 12, color: '#3b82f6', fixed: true});
  
  // Triángulo grande (6-8-10) = k*2
  var A2 = board.create('point', [6, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B2 = board.create('point', [12, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C2 = board.create('point', [6, 5.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A2, B2, C2], {fillColor: '#fef3c7', fillOpacity: 0.4, borders: {strokeColor: '#f59e0b', strokeWidth: 2}, fixed: true});
  
  board.create('text', [9, 0.2, '8'], {fontSize: 12, color: '#ef4444', fixed: true, anchorX: 'middle'});
  board.create('text', [5.5, 3, '6'], {fontSize: 12, color: '#22c55e', fixed: true});
  board.create('text', [9.5, 3.5, '10'], {fontSize: 12, color: '#3b82f6', fixed: true});
  
  // Flecha y k
  board.create('text', [4.8, 2.5, '× k'], {fontSize: 14, color: '#a855f7', fixed: true});
  board.create('text', [9, -1, 'k = 6/3 = 8/4 = 10/5 = 2'], {fontSize: 13, color: '#1e293b', fixed: true, anchorX: 'middle', fontWeight: 'bold'});
});
</script>

---

## 📖 Criterios de semejanza

### Criterio AA (Ángulo-Ángulo)

Dos triángulos son semejantes si tienen **dos ángulos iguales**.

$$
\boxed{AA: \text{ Si } \angle A = \angle A' \text{ y } \angle B = \angle B' \Rightarrow \triangle ABC \sim \triangle A'B'C'}
$$

> **Nota:** Si dos ángulos son iguales, el tercero también lo es automáticamente (porque suman 180°).

### Ejemplo

Si un triángulo tiene ángulos de 30° y 60°, y otro tiene ángulos de 60° y 90°:
- Primer triángulo: 30°, 60°, 90°
- Segundo triángulo: 60°, 90°, 30°

Son semejantes por AA.

**Ilustración: Criterio AA (Ángulo-Ángulo):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-aa" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jsxgraph-aa', {
    boundingbox: [-1, 5, 14, -1.5],
    axis: false,
    showCopyright: false,
    showNavigation: false
  });
  
  // Triángulo 1 (pequeño)
  var A1 = board.create('point', [1, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B1 = board.create('point', [4, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C1 = board.create('point', [2.5, 3], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A1, B1, C1], {fillColor: '#dcfce7', fillOpacity: 0.4, borders: {strokeColor: '#1e293b', strokeWidth: 2}, fixed: true});
  
  board.create('angle', [B1, A1, C1], {radius: 0.4, fillColor: '#a855f7', fillOpacity: 0.5, strokeColor: '#a855f7', name: '30°', label: {fontSize: 9}});
  board.create('angle', [C1, B1, A1], {radius: 0.4, fillColor: '#f59e0b', fillOpacity: 0.5, strokeColor: '#f59e0b', name: '60°', label: {fontSize: 9}});
  
  // Triángulo 2 (grande, mismos ángulos)
  var A2 = board.create('point', [6, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B2 = board.create('point', [12, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C2 = board.create('point', [9, 4.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A2, B2, C2], {fillColor: '#dcfce7', fillOpacity: 0.4, borders: {strokeColor: '#1e293b', strokeWidth: 2}, fixed: true});
  
  board.create('angle', [B2, A2, C2], {radius: 0.5, fillColor: '#a855f7', fillOpacity: 0.5, strokeColor: '#a855f7', name: '30°', label: {fontSize: 10}});
  board.create('angle', [C2, B2, A2], {radius: 0.5, fillColor: '#f59e0b', fillOpacity: 0.5, strokeColor: '#f59e0b', name: '60°', label: {fontSize: 10}});
  
  board.create('text', [5, 2.5, '∼'], {fontSize: 24, color: '#1e293b', fixed: true, anchorX: 'middle'});
  board.create('text', [6.5, -1, 'AA: 2 ángulos iguales → Semejantes (el 3° también es igual: 90°)'], {fontSize: 12, color: '#1e293b', fixed: true, anchorX: 'middle'});
});
</script>

---

### Criterio LAL (Lado-Ángulo-Lado)

Dos triángulos son semejantes si tienen **un ángulo igual** y los **lados que lo forman son proporcionales**.

$$
\boxed{LAL: \text{ Si } \frac{a}{a'} = \frac{b}{b'} \text{ y } \angle C = \angle C' \Rightarrow \triangle ABC \sim \triangle A'B'C'}
$$

### Ejemplo

Triángulo 1: lados 3 y 4 con ángulo de 50° entre ellos
Triángulo 2: lados 6 y 8 con ángulo de 50° entre ellos

$$
\frac{6}{3} = \frac{8}{4} = 2
$$

Son semejantes por LAL (razón $k = 2$).

---

### Criterio LLL (Lado-Lado-Lado)

Dos triángulos son semejantes si sus **tres lados son proporcionales**.

$$
\boxed{LLL: \text{ Si } \frac{a}{a'} = \frac{b}{b'} = \frac{c}{c'} \Rightarrow \triangle ABC \sim \triangle A'B'C'}
$$

### Ejemplo

Triángulo 1: lados 2, 3, 4 cm
Triángulo 2: lados 4, 6, 8 cm

$$
\frac{4}{2} = \frac{6}{3} = \frac{8}{4} = 2
$$

Son semejantes por LLL.

---

## 📖 Propiedades de triángulos semejantes

### Relación de perímetros

Si $k$ es la razón de semejanza:

$$
\frac{\text{Perímetro}_2}{\text{Perímetro}_1} = k
$$

### Relación de áreas

$$
\frac{\text{Área}_2}{\text{Área}_1} = k^2
$$

### Ejemplo

Si $k = 3$:
- El perímetro se triplica
- El área se multiplica por $3^2 = 9$

**Ilustración: Relación de áreas (k²):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-areas" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var board = JXG.JSXGraph.initBoard('jsxgraph-areas', {
    boundingbox: [-1, 6, 14, -2],
    axis: false,
    showCopyright: false,
    showNavigation: false
  });
  
  // Triángulo pequeño (área = 2)
  var A1 = board.create('point', [1, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B1 = board.create('point', [3, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C1 = board.create('point', [2, 2.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A1, B1, C1], {fillColor: '#22c55e', fillOpacity: 0.5, borders: {strokeColor: '#22c55e', strokeWidth: 2}, fixed: true});
  board.create('text', [2, 1.2, 'Área=2'], {fontSize: 11, color: '#166534', fixed: true, anchorX: 'middle'});
  
  // Triángulo grande (k=2, área = 2*k² = 8)
  var A2 = board.create('point', [5, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B2 = board.create('point', [9, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var C2 = board.create('point', [7, 4.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  board.create('polygon', [A2, B2, C2], {fillColor: '#3b82f6', fillOpacity: 0.5, borders: {strokeColor: '#3b82f6', strokeWidth: 2}, fixed: true});
  board.create('text', [7, 2, 'Área=8'], {fontSize: 12, color: '#1e40af', fixed: true, anchorX: 'middle'});
  
  // Triángulo más grande (k=3, área = 2*9 = 18)
  var A3 = board.create('point', [10, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  var B3 = board.create('point', [16, 0.5], {name: '', size: 3, color: '#1e293b', fixed: true});
  // Ajustamos para que quepa
  board.create('text', [13, 2.5, 'k=3: Área=18'], {fontSize: 12, color: '#f59e0b', fixed: true, anchorX: 'middle'});
  
  board.create('text', [7, -1.3, 'Si k=2: Área₂ = Área₁ × k² = 2 × 4 = 8'], {fontSize: 12, color: '#1e293b', fixed: true, anchorX: 'middle'});
  board.create('text', [3.8, 3, 'k=2'], {fontSize: 12, color: '#a855f7', fixed: true});
});
</script>

---

## 📖 Ejemplo completo

**Problema:** Determinar si los triángulos son semejantes y calcular la razón de semejanza.

Triángulo ABC: lados 4, 6, 8 cm
Triángulo DEF: lados 6, 9, 12 cm

**Solución:**

Verificamos si los lados son proporcionales:

$$
\frac{6}{4} = 1.5, \quad \frac{9}{6} = 1.5, \quad \frac{12}{8} = 1.5
$$

Las tres razones son iguales, entonces:

$$
\triangle ABC \sim \triangle DEF \quad \text{con } k = 1.5
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: ¿Son semejantes?

Determina si los triángulos son semejantes:

1. Triángulo 1: lados 5, 10, 15 y Triángulo 2: lados 2, 4, 6
2. Triángulo 1: ángulos 40°, 60°, 80° y Triángulo 2: ángulos 40°, 80°, 60°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Sí**, son semejantes. $\frac{5}{2} = \frac{10}{4} = \frac{15}{6} = 2.5$
2. **Sí**, son semejantes. Tienen los mismos tres ángulos (AA).

</details>

---

### Ejercicio 2: Encontrar lado desconocido

Los triángulos ABC y DEF son semejantes con $k = 3$. Si $AB = 4$ cm, ¿cuánto mide $DE$?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
DE = AB \times k = 4 \times 3 = 12 \text{ cm}
$$

</details>

---

### Ejercicio 3: Relación de áreas

Dos triángulos semejantes tienen razón de semejanza $k = 2$. Si el área del triángulo pequeño es 10 cm², ¿cuál es el área del grande?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\text{Área}_2 = \text{Área}_1 \times k^2 = 10 \times 2^2 = 10 \times 4 = 40 \text{ cm}^2
$$

</details>

---
