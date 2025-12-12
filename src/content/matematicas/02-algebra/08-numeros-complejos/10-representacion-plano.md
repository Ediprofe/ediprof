# 📍 Representación en el Plano Complejo

En esta lección aprenderemos a representar números complejos gráficamente en el plano complejo (también llamado plano de Argand).

---

## 📖 El plano complejo

El **plano complejo** es un sistema de coordenadas donde:

- El **eje horizontal** representa la parte real (eje real)
- El **eje vertical** representa la parte imaginaria (eje imaginario)

Un número complejo $z = a + bi$ se representa como el punto $(a, b)$ en este plano.

---

## 📖 Representación de números complejos

### Ejemplo 1

Representar $z = 3 + 2i$.

El número $z = 3 + 2i$ corresponde al punto $(3, 2)$:
- $3$ unidades a la derecha en el eje real
- $2$ unidades hacia arriba en el eje imaginario

---

### Ejemplo 2

Representar $z = -2 + 4i$.

El punto es $(-2, 4)$:
- $2$ unidades a la izquierda
- $4$ unidades hacia arriba

---

### Ejemplo 3

Representar $z = 4 - 3i$.

El punto es $(4, -3)$:
- $4$ unidades a la derecha
- $3$ unidades hacia abajo

---

### Ejemplo 4

Representar $z = -1 - 2i$.

El punto es $(-1, -2)$:
- $1$ unidad a la izquierda
- $2$ unidades hacia abajo

Visualización de estos 4 puntos:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-plano-complejo" class="jsxgraph-container" style="width: 100%; height: 400px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board = JXG.JSXGraph.initBoard('jsxgraph-plano-complejo', {
      boundingbox: [-6, 6, 9, -5],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Cuadrantes
    board.create('text', [5, 4, 'I'], { fontSize: 20, strokeColor: '#94a3b8', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [-4, 4, 'II'], { fontSize: 20, strokeColor: '#94a3b8', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [-4, -3.5, 'III'], { fontSize: 20, strokeColor: '#94a3b8', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [5, -3.5, 'IV'], { fontSize: 20, strokeColor: '#94a3b8', cssStyle: 'font-weight: bold;', fixed: true });
    
    // Puntos de los ejemplos
    var z1 = board.create('point', [3, 2], { name: '3 + 2i', size: 5, fixed: true, color: '#3b82f6', label: { fontSize: 12, offset: [8, 8] } });
    var z2 = board.create('point', [-2, 4], { name: '-2 + 4i', size: 5, fixed: true, color: '#22c55e', label: { fontSize: 12, offset: [8, 8] } });
    var z3 = board.create('point', [4, -3], { name: '4 - 3i', size: 5, fixed: true, color: '#f97316', label: { fontSize: 12, offset: [8, -12] } });
    var z4 = board.create('point', [-1, -2], { name: '-1 - 2i', size: 5, fixed: true, color: '#a855f7', label: { fontSize: 12, offset: [8, -12] } });
    
    // Vectores desde el origen
    board.create('arrow', [[0, 0], z1], { strokeColor: '#3b82f6', strokeWidth: 2, fixed: true });
    board.create('arrow', [[0, 0], z2], { strokeColor: '#22c55e', strokeWidth: 2, fixed: true });
    board.create('arrow', [[0, 0], z3], { strokeColor: '#f97316', strokeWidth: 2, fixed: true });
    board.create('arrow', [[0, 0], z4], { strokeColor: '#a855f7', strokeWidth: 2, fixed: true });
    
    // Etiquetas de ejes
    board.create('text', [8.3, -0.5, 'Eje Real'], { fontSize: 11, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [0.3, 5.5, 'Eje Imaginario'], { fontSize: 11, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 Cada número complejo se representa como un punto (o vector) en el plano. La parte real va en el eje horizontal y la parte imaginaria en el vertical.

---

## 📖 Casos especiales

### Números reales

Los números reales están sobre el **eje horizontal**:

- $z = 5$ corresponde al punto $(5, 0)$
- $z = -3$ corresponde al punto $(-3, 0)$

---

### Números imaginarios puros

Los imaginarios puros están sobre el **eje vertical**:

- $z = 4i$ corresponde al punto $(0, 4)$
- $z = -2i$ corresponde al punto $(0, -2)$

---

### El origen

$z = 0$ corresponde al punto $(0, 0)$.

---

## 📖 Los cuatro cuadrantes

| Cuadrante | Parte real | Parte imaginaria | Ejemplo |
|:---------:|:----------:|:----------------:|:-------:|
| I | $+$ | $+$ | $3 + 2i$ |
| II | $-$ | $+$ | $-2 + 4i$ |
| III | $-$ | $-$ | $-1 - 3i$ |
| IV | $+$ | $-$ | $4 - 2i$ |

---

## 📖 Vectores en el plano complejo

Cada número complejo puede representarse también como un **vector** desde el origen hasta el punto $(a, b)$.

### Ejemplo 5

El número $z = 3 + 4i$ se puede ver como una flecha:
- Comienza en $(0, 0)$
- Termina en $(3, 4)$

---

## 📖 Suma gráfica de complejos

La suma de números complejos sigue la **regla del paralelogramo**:

Para sumar $z_1$ y $z_2$:
1. Dibujamos ambos vectores desde el origen
2. Completamos el paralelogramo
3. El resultado es la diagonal desde el origen

### Ejemplo 6

Sumar gráficamente $(2 + i) + (1 + 3i)$.

- $z_1 = 2 + i$ → punto $(2, 1)$
- $z_2 = 1 + 3i$ → punto $(1, 3)$
- $z_1 + z_2 = 3 + 4i$ → punto $(3, 4)$

El punto $(3, 4)$ es la diagonal del paralelogramo formado.

---

## 📖 Conjugado en el plano

El conjugado de $z = a + bi$ es $\bar{z} = a - bi$.

Gráficamente, el conjugado es la **reflexión** respecto al eje real.

### Ejemplo 7

Si $z = 3 + 4i$, entonces $\bar{z} = 3 - 4i$.

- $z$ está en $(3, 4)$ (cuadrante I)
- $\bar{z}$ está en $(3, -4)$ (cuadrante IV)

Son simétricos respecto al eje horizontal.

---

## 📖 Opuesto en el plano

El opuesto de $z = a + bi$ es $-z = -a - bi$.

Gráficamente, el opuesto es la **reflexión** respecto al origen.

Si $z = 2 + 3i$, entonces $-z = -2 - 3i$.

- $z$ está en $(2, 3)$ (cuadrante I)
- $-z$ está en $(-2, -3)$ (cuadrante III)

Visualización del conjugado y opuesto:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 480px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-conjugado-opuesto" class="jsxgraph-container" style="width: 100%; height: 380px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board = JXG.JSXGraph.initBoard('jsxgraph-conjugado-opuesto', {
      boundingbox: [-5, 5, 5, -5],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // z = 3 + 4i
    var z = board.create('point', [3, 4], { name: 'z = 3 + 4i', size: 5, fixed: true, color: '#3b82f6', label: { fontSize: 11, offset: [8, 8] } });
    board.create('arrow', [[0, 0], z], { strokeColor: '#3b82f6', strokeWidth: 2, fixed: true });
    
    // Conjugado z̄ = 3 - 4i
    var zbar = board.create('point', [3, -4], { name: 'z̄ = 3 - 4i', size: 5, fixed: true, color: '#22c55e', label: { fontSize: 11, offset: [8, -12] } });
    board.create('arrow', [[0, 0], zbar], { strokeColor: '#22c55e', strokeWidth: 2, fixed: true });
    
    // Línea de simetría (eje real)
    board.create('segment', [z, zbar], { strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true });
    
    // Opuesto -z = -3 - 4i
    var negz = board.create('point', [-3, -4], { name: '-z = -3 - 4i', size: 5, fixed: true, color: '#ef4444', label: { fontSize: 11, offset: [-80, -12] } });
    board.create('arrow', [[0, 0], negz], { strokeColor: '#ef4444', strokeWidth: 2, fixed: true });
    
    // Línea de simetría (origen)
    board.create('segment', [z, negz], { strokeColor: '#f97316', strokeWidth: 1, dash: 3, fixed: true });
    
    // Etiquetas de ejes
    board.create('text', [4.3, -0.4, 'Re'], { fontSize: 12, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [0.2, 4.5, 'Im'], { fontSize: 12, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 El **conjugado** (verde) es la reflexión respecto al eje real. El **opuesto** (rojo) es la reflexión respecto al origen.

---

## 📋 Resumen de representaciones

| Número | Punto | Cuadrante |
|:------:|:-----:|:---------:|
| $3 + 2i$ | $(3, 2)$ | I |
| $-4 + i$ | $(-4, 1)$ | II |
| $-2 - 5i$ | $(-2, -5)$ | III |
| $1 - 3i$ | $(1, -3)$ | IV |
| $5$ | $(5, 0)$ | Eje real |
| $-3i$ | $(0, -3)$ | Eje imaginario |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿En qué cuadrante está $z = -3 + 5i$?

<details>
<summary>Ver solución</summary>

Cuadrante II (parte real negativa, parte imaginaria positiva)

</details>

---

**Ejercicio 2:** ¿Cuáles son las coordenadas del punto que representa $z = 4 - 7i$?

<details>
<summary>Ver solución</summary>

$(4, -7)$

</details>

---

**Ejercicio 3:** Si un punto está en $(0, 5)$, ¿qué número complejo representa?

<details>
<summary>Ver solución</summary>

$z = 5i$

</details>

---

**Ejercicio 4:** ¿Dónde está ubicado el conjugado de $z = -2 + 6i$?

<details>
<summary>Ver solución</summary>

$\bar{z} = -2 - 6i$ → punto $(-2, -6)$ en el cuadrante III

</details>

---

**Ejercicio 5:** ¿Dónde está el opuesto de $z = 3 - 4i$?

<details>
<summary>Ver solución</summary>

$-z = -3 + 4i$ → punto $(-3, 4)$ en el cuadrante II

</details>

---

**Ejercicio 6:** ¿Qué número complejo tiene parte real $-5$ y está sobre el eje real?

<details>
<summary>Ver solución</summary>

$z = -5$ (parte imaginaria igual a 0)

</details>

---
