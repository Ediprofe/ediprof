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

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-plano-complejo" style="width: 100%; height: 420px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-plano-complejo')) {
    var chart = echarts.init(document.getElementById('echarts-plano-complejo'));
    var option = {
      title: { text: 'Números complejos en el plano', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '10%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Eje Real', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 14, fontWeight: 'bold', color: '#374151' }, min: -5, max: 8, interval: 1, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, axisLabel: { fontSize: 11 } },
      yAxis: { type: 'value', name: 'Eje Imaginario', nameLocation: 'middle', nameGap: 55, nameTextStyle: { fontSize: 14, fontWeight: 'bold', color: '#374151' }, min: -5, max: 6, interval: 1, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, axisLabel: { fontSize: 11 } },
      series: [
        { name: 'z₁ = 3 + 2i', type: 'scatter', symbolSize: 16, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '3 + 2i', position: 'top', fontSize: 11, fontWeight: 'bold' }, data: [[3, 2]] },
        { name: 'z₂ = -2 + 4i', type: 'scatter', symbolSize: 16, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '-2 + 4i', position: 'top', fontSize: 11, fontWeight: 'bold' }, data: [[-2, 4]] },
        { name: 'z₃ = 4 - 3i', type: 'scatter', symbolSize: 16, itemStyle: { color: '#f97316', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '4 - 3i', position: 'bottom', fontSize: 11, fontWeight: 'bold' }, data: [[4, -3]] },
        { name: 'z₄ = -1 - 2i', type: 'scatter', symbolSize: 16, itemStyle: { color: '#a855f7', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '-1 - 2i', position: 'bottom', fontSize: 11, fontWeight: 'bold' }, data: [[-1, -2]] },
        { name: 'Cuadrante I', type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'I', fontSize: 22, fontWeight: 'bold', color: '#94a3b8' }, data: [[5, 4]] },
        { name: 'Cuadrante II', type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'II', fontSize: 22, fontWeight: 'bold', color: '#94a3b8' }, data: [[-4, 4]] },
        { name: 'Cuadrante III', type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'III', fontSize: 22, fontWeight: 'bold', color: '#94a3b8' }, data: [[-4, -4]] },
        { name: 'Cuadrante IV', type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'IV', fontSize: 22, fontWeight: 'bold', color: '#94a3b8' }, data: [[5, -4]] }
      ],
      tooltip: { trigger: 'item', formatter: function(p) { return p.seriesName; } }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
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

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-conjugado-opuesto" style="width: 100%; height: 400px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-conjugado-opuesto')) {
    var chart = echarts.init(document.getElementById('echarts-conjugado-opuesto'));
    var option = {
      title: { text: 'Conjugado y Opuesto', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      legend: { data: ['z = 3 + 4i', 'z̄ = 3 - 4i (conjugado)', '-z = -3 - 4i (opuesto)'], bottom: 5, textStyle: { fontSize: 10 } },
      grid: { left: '12%', right: '8%', top: '10%', bottom: '22%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Re', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 14, fontWeight: 'bold', color: '#374151' }, min: -5, max: 5, interval: 1, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, axisLabel: { fontSize: 11 } },
      yAxis: { type: 'value', name: 'Im', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 14, fontWeight: 'bold', color: '#374151' }, min: -5, max: 5, interval: 1, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, axisLabel: { fontSize: 11 } },
      series: [
        { name: 'z = 3 + 4i', type: 'scatter', symbolSize: 18, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'z = 3 + 4i', position: 'right', fontSize: 11, fontWeight: 'bold' }, data: [[3, 4]] },
        { name: 'z̄ = 3 - 4i (conjugado)', type: 'scatter', symbolSize: 18, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'z̄ = 3 - 4i', position: 'right', fontSize: 11, fontWeight: 'bold' }, data: [[3, -4]] },
        { name: '-z = -3 - 4i (opuesto)', type: 'scatter', symbolSize: 18, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '-z = -3 - 4i', position: 'left', fontSize: 11, fontWeight: 'bold' }, data: [[-3, -4]] },
        { name: 'Simetría conjugado', type: 'line', lineStyle: { width: 2, type: 'dashed', color: '#94a3b8' }, symbol: 'none', data: [[3, 4], [3, -4]] },
        { name: 'Simetría opuesto', type: 'line', lineStyle: { width: 2, type: 'dotted', color: '#f97316' }, symbol: 'none', data: [[3, 4], [-3, -4]] }
      ],
      tooltip: { trigger: 'item', formatter: function(p) { return p.seriesName; } }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
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
