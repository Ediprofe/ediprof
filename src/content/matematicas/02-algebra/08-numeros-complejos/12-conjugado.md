# 🔄 Conjugado de un Número Complejo

En esta lección aprenderemos sobre el conjugado de un número complejo y sus propiedades.

---

## 📖 Definición de conjugado

El **conjugado** de un número complejo $z = a + bi$ se denota $\bar{z}$ y se obtiene cambiando el signo de la parte imaginaria:

$$
\bar{z} = a - bi
$$

---

### Ejemplo 1

Encontrar el conjugado de $z = 3 + 4i$.

$$
\bar{z} = 3 - 4i
$$

$$
\boxed{\overline{3 + 4i} = 3 - 4i}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-conj1" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-conj1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-conj1', {
      boundingbox: [-1, 6, 5, -6], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('point', [3, 4], { name: 'z = 3+4i', size: 5, fixed: true, color: '#3b82f6', label: { fontSize: 11, offset: [5, 5] } });
    board.create('point', [3, -4], { name: 'z̄ = 3-4i', size: 5, fixed: true, color: '#22c55e', label: { fontSize: 11, offset: [5, -12] } });
    board.create('segment', [[3,4], [3,-4]], { strokeColor: '#f97316', strokeWidth: 2, dash: 2, fixed: true });
    board.create('text', [4.3, -0.5, 'Re'], { fontSize: 10, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [-0.7, 5.3, 'Im'], { fontSize: 10, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.unsuspendUpdate();
  }
});
</script>

---

### Ejemplo 2

Encontrar el conjugado de $z = 5 - 2i$.

$$
\bar{z} = 5 + 2i
$$

$$
\boxed{\overline{5 - 2i} = 5 + 2i}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-conj2" class="jsxgraph-container" style="width: 100%; height: 250px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-conj2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-conj2', {
      boundingbox: [-1, 4, 7, -4], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('point', [5, -2], { name: 'z = 5-2i', size: 5, fixed: true, color: '#3b82f6', label: { fontSize: 11, offset: [5, -12] } });
    board.create('point', [5, 2], { name: 'z̄ = 5+2i', size: 5, fixed: true, color: '#22c55e', label: { fontSize: 11, offset: [5, 5] } });
    board.create('segment', [[5,-2], [5,2]], { strokeColor: '#f97316', strokeWidth: 2, dash: 2, fixed: true });
    board.create('text', [6.3, -0.5, 'Re'], { fontSize: 10, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [-0.7, 3.3, 'Im'], { fontSize: 10, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.unsuspendUpdate();
  }
});
</script>

---

### Ejemplo 3

Encontrar el conjugado de $z = -1 + 7i$.

$$
\bar{z} = -1 - 7i
$$

$$
\boxed{\overline{-1 + 7i} = -1 - 7i}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-conj3" class="jsxgraph-container" style="width: 100%; height: 320px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-conj3')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-conj3', {
      boundingbox: [-4, 9, 3, -9], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('point', [-1, 7], { name: 'z = -1+7i', size: 5, fixed: true, color: '#3b82f6', label: { fontSize: 11, offset: [5, 5] } });
    board.create('point', [-1, -7], { name: 'z̄ = -1-7i', size: 5, fixed: true, color: '#22c55e', label: { fontSize: 11, offset: [5, -12] } });
    board.create('segment', [[-1,7], [-1,-7]], { strokeColor: '#f97316', strokeWidth: 2, dash: 2, fixed: true });
    board.create('text', [2.3, -0.5, 'Re'], { fontSize: 10, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [-3.5, 8.2, 'Im'], { fontSize: 10, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.unsuspendUpdate();
  }
});
</script>

---

### Ejemplo 4

Encontrar el conjugado de $z = 6$ (número real).

$$
\bar{z} = 6 - 0i = 6
$$

> El conjugado de un número real es él mismo.

$$
\boxed{\bar{6} = 6}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-conj4" class="jsxgraph-container" style="width: 100%; height: 180px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-conj4')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-conj4', {
      boundingbox: [-1, 3, 8, -3], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('point', [6, 0], { name: 'z = z̄ = 6', size: 6, fixed: true, color: '#ef4444', label: { fontSize: 12, offset: [5, 10] } });
    board.create('text', [7.3, -0.5, 'Re'], { fontSize: 10, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [-0.7, 2.3, 'Im'], { fontSize: 10, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [2, 1.5, 'Los reales están sobre el eje'], { fontSize: 9, strokeColor: '#64748b', cssStyle: 'font-style: italic;', fixed: true });
    board.unsuspendUpdate();
  }
});
</script>

> 💡 El conjugado es el **reflejo** respecto al eje real. Los números reales están sobre el eje, así que coinciden con su conjugado.

---

### Ejemplo 5

Encontrar el conjugado de $z = 4i$ (imaginario puro).

$$
\bar{z} = 0 - 4i = -4i
$$

> El conjugado de un imaginario puro es su opuesto.

$$
\boxed{\overline{4i} = -4i}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-conj5" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-conj5')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-conj5', {
      boundingbox: [-3, 6, 3, -6], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('point', [0, 4], { name: 'z = 4i', size: 5, fixed: true, color: '#3b82f6', label: { fontSize: 11, offset: [8, 5] } });
    board.create('point', [0, -4], { name: 'z̄ = -4i', size: 5, fixed: true, color: '#22c55e', label: { fontSize: 11, offset: [8, -12] } });
    board.create('segment', [[0,4], [0,-4]], { strokeColor: '#f97316', strokeWidth: 2, dash: 2, fixed: true });
    board.create('text', [2.3, -0.5, 'Re'], { fontSize: 10, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [-2.5, 5.3, 'Im'], { fontSize: 10, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Los imaginarios puros están sobre el eje imaginario. Su conjugado es el mismo punto reflejado al lado opuesto.

---

## 📖 Propiedades del conjugado

### Propiedad 1: Conjugado del conjugado

$$
\overline{\bar{z}} = z
$$

### Ejemplo 6

Si $z = 2 + 3i$, verificar que $\overline{\bar{z}} = z$.

$$
\bar{z} = 2 - 3i
$$

$$
\overline{\bar{z}} = 2 + 3i = z \quad ✓
$$

---

### Propiedad 2: Conjugado de una suma

$$
\overline{z_1 + z_2} = \bar{z_1} + \bar{z_2}
$$

### Ejemplo 7

Si $z_1 = 1 + 2i$ y $z_2 = 3 + i$, verificar la propiedad.

$$
z_1 + z_2 = 4 + 3i, \quad \overline{z_1 + z_2} = 4 - 3i
$$

$$
\bar{z_1} + \bar{z_2} = (1 - 2i) + (3 - i) = 4 - 3i \quad ✓
$$

---

### Propiedad 3: Conjugado de un producto

$$
\overline{z_1 \cdot z_2} = \bar{z_1} \cdot \bar{z_2}
$$

---

### Propiedad 4: Conjugado de un cociente

$$
\overline{\left(\frac{z_1}{z_2}\right)} = \frac{\bar{z_1}}{\bar{z_2}}
$$

---

### Propiedad 5: Suma con el conjugado

$$
z + \bar{z} = 2\text{Re}(z) = 2a
$$

### Ejemplo 8

Si $z = 5 + 3i$, calcular $z + \bar{z}$.

$$
z + \bar{z} = (5 + 3i) + (5 - 3i) = 10 = 2(5)
$$

$$
\boxed{z + \bar{z} = 10}
$$

---

### Propiedad 6: Diferencia con el conjugado

$$
z - \bar{z} = 2\text{Im}(z) \cdot i = 2bi
$$

### Ejemplo 9

Si $z = 4 + 7i$, calcular $z - \bar{z}$.

$$
z - \bar{z} = (4 + 7i) - (4 - 7i) = 14i = 2(7)i
$$

$$
\boxed{z - \bar{z} = 14i}
$$

---

### Propiedad 7: Producto con el conjugado

$$
z \cdot \bar{z} = |z|^2 = a^2 + b^2
$$

### Ejemplo 10

Si $z = 3 + 4i$, calcular $z \cdot \bar{z}$.

$$
z \cdot \bar{z} = (3 + 4i)(3 - 4i) = 9 + 16 = 25 = |z|^2
$$

$$
\boxed{z \cdot \bar{z} = 25}
$$

---

## 📖 Aplicación: Encontrar partes real e imaginaria

Usando las propiedades, podemos encontrar las partes de un complejo:

$$
\text{Re}(z) = \frac{z + \bar{z}}{2}
$$

$$
\text{Im}(z) = \frac{z - \bar{z}}{2i}
$$

---

## 📖 Uso en división

El conjugado es fundamental para dividir números complejos, como vimos en la lección de división:

$$
\frac{z_1}{z_2} = \frac{z_1 \cdot \bar{z_2}}{z_2 \cdot \bar{z_2}} = \frac{z_1 \cdot \bar{z_2}}{|z_2|^2}
$$

---

## 📋 Resumen

| Propiedad | Fórmula |
|:----------|:-------:|
| Definición | $\overline{a + bi} = a - bi$ |
| Doble conjugado | $\overline{\bar{z}} = z$ |
| Conjugado de suma | $\overline{z_1 + z_2} = \bar{z_1} + \bar{z_2}$ |
| Conjugado de producto | $\overline{z_1 z_2} = \bar{z_1} \bar{z_2}$ |
| Suma con conjugado | $z + \bar{z} = 2\text{Re}(z)$ |
| Resta con conjugado | $z - \bar{z} = 2\text{Im}(z) \cdot i$ |
| Producto con conjugado | $z \bar{z} = \|z\|^2$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra el conjugado de $z = 7 - 3i$.

<details>
<summary>Ver solución</summary>

$$
\bar{z} = 7 + 3i
$$

</details>

---

**Ejercicio 2:** Encuentra el conjugado de $z = -2 - 5i$.

<details>
<summary>Ver solución</summary>

$$
\bar{z} = -2 + 5i
$$

</details>

---

**Ejercicio 3:** Si $z = 6 + 2i$, calcula $z + \bar{z}$.

<details>
<summary>Ver solución</summary>

$$
(6 + 2i) + (6 - 2i) = 12
$$

</details>

---

**Ejercicio 4:** Si $z = 3 - 4i$, calcula $z - \bar{z}$.

<details>
<summary>Ver solución</summary>

$$
(3 - 4i) - (3 + 4i) = -8i
$$

</details>

---

**Ejercicio 5:** Si $z = 2 + 5i$, calcula $z \cdot \bar{z}$.

<details>
<summary>Ver solución</summary>

$$
(2 + 5i)(2 - 5i) = 4 + 25 = 29
$$

</details>

---

**Ejercicio 6:** Encuentra el conjugado de $-8i$.

<details>
<summary>Ver solución</summary>

$$
\overline{-8i} = 8i
$$

</details>

---
