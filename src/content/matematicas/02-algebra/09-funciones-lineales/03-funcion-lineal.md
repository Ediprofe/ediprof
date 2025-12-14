# 📐 Función Lineal

En esta lección profundizaremos en la función lineal, comprendiendo la pendiente, el intercepto, y analizando diferentes casos.

---

## 📖 Forma pendiente-intercepto

La forma más común de escribir una función lineal es:

$$
y = mx + b
$$

donde:
- $m$ = **pendiente** (razón de cambio)
- $b$ = **intercepto con el eje y** (ordenada al origen)

---

## 📖 La pendiente

La **pendiente** mide cuánto cambia $y$ por cada unidad que cambia $x$:

$$
m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}
$$

También se interpreta como:

$$
m = \frac{\text{cambio vertical}}{\text{cambio horizontal}} = \frac{\text{subida}}{\text{corrida}}
$$

---

### Ejemplo 1

Encontrar la pendiente de la recta que pasa por $A(1, 2)$ y $B(4, 8)$.

$$
m = \frac{8 - 2}{4 - 1} = \frac{6}{3} = 2
$$

$$
\boxed{m = 2}
$$

Interpretación: Por cada unidad que $x$ aumenta, $y$ aumenta $2$ unidades.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo1" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo1')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo1'));
    var option = {
      title: { text: 'Ejemplo 1: m = 2', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: 0, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: 0, max: 10, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[0, 0], [5, 10]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return '(' + p.data[0] + ',' + p.data[1] + ')'; }, position: 'top', fontSize: 11, fontWeight: 'bold' }, data: [[1, 2], [4, 8]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 2

Encontrar la pendiente de la recta que pasa por $P(-2, 5)$ y $Q(3, -5)$.

$$
m = \frac{-5 - 5}{3 - (-2)} = \frac{-10}{5} = -2
$$

$$
\boxed{m = -2}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo2" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo2')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo2'));
    var option = {
      title: { text: 'Ejemplo 2: m = -2', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -3, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -6, max: 7, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, data: [[-3, 7], [4, -7]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return '(' + p.data[0] + ',' + p.data[1] + ')'; }, position: 'top', fontSize: 11, fontWeight: 'bold' }, data: [[-2, 5], [3, -5]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 3

Encontrar la pendiente de la recta que pasa por $(0, 4)$ y $(6, 4)$.

$$
m = \frac{4 - 4}{6 - 0} = \frac{0}{6} = 0
$$

$$
\boxed{m = 0}
$$

Cuando $m = 0$, la recta es **horizontal**.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo3" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo3')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo3'));
    var option = {
      title: { text: 'Ejemplo 3: m = 0 (horizontal)', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 7, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: 0, max: 6, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[-1, 4], [7, 4]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return '(' + p.data[0] + ',' + p.data[1] + ')'; }, position: 'top', fontSize: 11, fontWeight: 'bold' }, data: [[0, 4], [6, 4]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Tipos de pendiente

| Pendiente | Comportamiento de la recta |
|:---------:|:---------------------------|
| $m > 0$ | Recta **ascendente** (sube hacia la derecha) |
| $m < 0$ | Recta **descendente** (baja hacia la derecha) |
| $m = 0$ | Recta **horizontal** |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> Tipos de pendiente
  </div>
  <div id="echarts-tipos-pendiente" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-tipos-pendiente')) {
    var chart = echarts.init(document.getElementById('echarts-tipos-pendiente'));
    var option = {
      title: { text: 'Tipos de pendiente', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      legend: { data: ['m > 0 (ascendente)', 'm < 0 (descendente)', 'm = 0 (horizontal)'], bottom: 5, textStyle: { fontSize: 11 } },
      grid: { left: '8%', right: '8%', top: '12%', bottom: '18%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', min: -5, max: 5, interval: 1, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed', width: 1 } }, axisLabel: { fontSize: 10 } },
      yAxis: { type: 'value', min: -4, max: 6, interval: 1, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed', width: 1 } }, axisLabel: { fontSize: 10 } },
      series: [
        { name: 'm > 0 (ascendente)', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[-4, -2], [0, 2], [3, 5]] },
        { name: 'm < 0 (descendente)', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, data: [[-3, 5], [0, 2], [3, -1]] },
        { name: 'm = 0 (horizontal)', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[-4, -2], [0, -2], [4, -2]] }
      ],
      tooltip: { trigger: 'item' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 El intercepto con el eje Y

El **intercepto** $b$ es el valor de $y$ cuando $x = 0$. Es el punto $(0, b)$ donde la recta cruza el eje vertical.

### Ejemplo 4

Para $y = 3x + 5$:

Cuando $x = 0$: $y = 3(0) + 5 = 5$

El intercepto es $(0, 5)$.

$$
\boxed{b = 5}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo4" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo4')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo4'));
    var option = {
      title: { text: 'Ejemplo 4: y = 3x + 5', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -2, max: 2, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -2, max: 12, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[-2, -1], [2, 11]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(0, 5)', position: 'right', fontSize: 11, fontWeight: 'bold' }, data: [[0, 5]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 5

Para $y = -2x - 3$:

Cuando $x = 0$: $y = -3$

El intercepto es $(0, -3)$.

$$
\boxed{b = -3}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo5" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo5')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo5'));
    var option = {
      title: { text: 'Ejemplo 5: y = -2x - 3', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -3, max: 2, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -8, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, data: [[-3, 3], [2, -7]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(0, -3)', position: 'right', fontSize: 11, fontWeight: 'bold' }, data: [[0, -3]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 El intercepto con el eje X

El **intercepto con el eje X** es el punto donde $y = 0$. Para encontrarlo, despejamos $x$:

$$
0 = mx + b \quad \Rightarrow \quad x = -\frac{b}{m}
$$

### Ejemplo 6

Para $y = 2x + 6$, encontrar el intercepto con el eje X.

$$
0 = 2x + 6 \quad \Rightarrow \quad 2x = -6 \quad \Rightarrow \quad x = -3
$$

El intercepto con el eje X es $(-3, 0)$.

$$
\boxed{x = -3}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo6" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo6')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo6'));
    var option = {
      title: { text: 'Ejemplo 6: y = 2x + 6', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -4, max: 2, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -3, max: 11, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[-4, -2], [2, 10]] },
        { type: 'scatter', symbolSize: 16, symbol: 'diamond', itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(-3, 0)', position: 'bottom', fontSize: 11, fontWeight: 'bold' }, data: [[-3, 0]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(0, 6)', position: 'right', fontSize: 11, fontWeight: 'bold' }, data: [[0, 6]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Función constante

Cuando $m = 0$:

$$
y = b
$$

Esta es una **función constante**. Para cualquier valor de $x$, $y$ siempre vale $b$.

### Ejemplo 7

La función $y = 4$ es una recta horizontal que pasa por el punto $(0, 4)$.

---

## 📖 Función lineal que pasa por el origen

Cuando $b = 0$:

$$
y = mx
$$

Esta recta pasa por el origen $(0, 0)$.

### Ejemplo 8

La función $y = 3x$ pasa por el origen con pendiente $3$.

---

## 📖 Escribiendo ecuaciones de rectas

### Ejemplo 9

Escribir la ecuación de la recta con pendiente $m = 4$ e intercepto $b = -2$.

$$
y = 4x - 2
$$

$$
\boxed{y = 4x - 2}
$$

---

### Ejemplo 10

Una recta pasa por $(0, 3)$ y tiene pendiente $-\frac{1}{2}$. Escribir su ecuación.

Como pasa por $(0, 3)$, el intercepto es $b = 3$.

$$
y = -\frac{1}{2}x + 3
$$

$$
\boxed{y = -\frac{1}{2}x + 3}
$$

---

## 📋 Resumen

| Elemento | Significado |
|:---------|:------------|
| $m > 0$ | Recta ascendente |
| $m < 0$ | Recta descendente |
| $m = 0$ | Recta horizontal |
| $b$ | Punto donde cruza el eje Y |
| $b = 0$ | Pasa por el origen |

### Efecto de la pendiente $m$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-resumen-pendiente" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-resumen-pendiente')) {
    var chart = echarts.init(document.getElementById('echarts-resumen-pendiente'));
    var option = {
      title: { text: 'Efecto de la pendiente m (con b = 0)', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['m > 0 (ascendente)', 'm < 0 (descendente)', 'm = 0 (horizontal)'], top: 30, textStyle: { fontSize: 10 } },
      grid: { left: '12%', right: '8%', top: '22%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -4, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -4, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'm > 0 (ascendente)', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[-4, -4], [4, 4]], markPoint: { data: [{ coord: [2, 2], name: 'm = 1', label: { show: true, formatter: 'm > 0', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#22c55e' } }] } },
        { name: 'm < 0 (descendente)', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, data: [[-4, 4], [4, -4]], markPoint: { data: [{ coord: [2, -2], name: 'm = -1', label: { show: true, formatter: 'm < 0', position: 'bottom', fontSize: 11, fontWeight: 'bold', color: '#ef4444' } }] } },
        { name: 'm = 0 (horizontal)', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[-4, 0], [4, 0]], markPoint: { data: [{ coord: [2, 0], name: 'm = 0', label: { show: true, formatter: 'm = 0', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#3b82f6' } }] } }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

### Efecto del intercepto $b$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-resumen-intercepto" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-resumen-intercepto')) {
    var chart = echarts.init(document.getElementById('echarts-resumen-intercepto'));
    var option = {
      title: { text: 'Efecto del intercepto b (con m = 1)', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['b > 0', 'b = 0', 'b < 0'], top: 30, textStyle: { fontSize: 11 } },
      grid: { left: '12%', right: '8%', top: '20%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -4, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -4, max: 6, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'b > 0', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#a855f7' }, data: [[-2, 0], [4, 6]], markPoint: { data: [{ coord: [0, 2], name: 'b = 2', symbol: 'circle', symbolSize: 12, itemStyle: { color: '#a855f7', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'b = 2', position: 'right', fontSize: 11, fontWeight: 'bold', color: '#a855f7' } }] } },
        { name: 'b = 0', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[-4, -4], [4, 4]], markPoint: { data: [{ coord: [0, 0], name: 'b = 0', symbol: 'circle', symbolSize: 12, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'b = 0', position: 'right', fontSize: 11, fontWeight: 'bold', color: '#22c55e' } }] } },
        { name: 'b < 0', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#f59e0b' }, data: [[-4, -6], [2, 0]], markPoint: { data: [{ coord: [0, -2], name: 'b = -2', symbol: 'circle', symbolSize: 12, itemStyle: { color: '#f59e0b', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'b = -2', position: 'right', fontSize: 11, fontWeight: 'bold', color: '#f59e0b' } }] } }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra la pendiente de la recta que pasa por $(2, 3)$ y $(5, 9)$.

<details>
<summary>Ver solución</summary>

$$
m = \frac{9-3}{5-2} = \frac{6}{3} = 2
$$

</details>

---

**Ejercicio 2:** Identifica la pendiente e intercepto de $y = -3x + 7$.

<details>
<summary>Ver solución</summary>

$m = -3$, $b = 7$

</details>

---

**Ejercicio 3:** ¿La recta $y = 5x - 2$ es ascendente o descendente?

<details>
<summary>Ver solución</summary>

Ascendente ($m = 5 > 0$)

</details>

---

**Ejercicio 4:** Encuentra el intercepto X de $y = 4x - 8$.

<details>
<summary>Ver solución</summary>

$0 = 4x - 8$, $x = 2$

</details>

---

**Ejercicio 5:** Escribe la ecuación de una recta con $m = -2$ y $b = 5$.

<details>
<summary>Ver solución</summary>

$$
y = -2x + 5
$$

</details>

---

**Ejercicio 6:** ¿Qué tipo de recta es $y = 7$?

<details>
<summary>Ver solución</summary>

Recta horizontal (función constante)

</details>

---
