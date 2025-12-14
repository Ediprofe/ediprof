# 📈 Introducción a las Funciones Cuadráticas

En esta lección introduciremos las funciones cuadráticas, su forma general y sus características.

---

## 📖 Definición

Una **función cuadrática** es una función polinómica de segundo grado:

$$
f(x) = ax^2 + bx + c
$$

donde $a$, $b$, $c$ son constantes y $a \neq 0$.

---

## 📖 La parábola

La gráfica de una función cuadrática es una **parábola**, una curva en forma de U (o U invertida).

| Valor de $a$ | Orientación |
|:------------:|:------------|
| $a > 0$ | Abre hacia arriba ∪ |
| $a < 0$ | Abre hacia abajo ∩ |

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-efecto-a" style="width: 100%; height: 400px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-efecto-a')) {
    var chart = echarts.init(document.getElementById('echarts-efecto-a'));
    var xData = [];
    var y1 = [], y2 = [], y3 = [];
    for (var i = -3; i <= 3; i += 0.1) {
      xData.push(i.toFixed(1));
      y1.push([i, i * i]);
      y2.push([i, -i * i]);
      y3.push([i, 0.5 * i * i]);
    }
    var option = {
      title: { text: '📊 Efecto del coeficiente a', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      tooltip: { trigger: 'axis' },
      legend: { data: ['a = 1 (arriba)', 'a = -1 (abajo)', 'a = 0.5 (más abierta)'], top: 35, textStyle: { fontSize: 11 } },
      grid: { left: '10%', right: '8%', top: '22%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -3, max: 3, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -5, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { name: 'a = 1 (arriba)', type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, itemStyle: { color: '#3b82f6' }, data: y1 },
        { name: 'a = -1 (abajo)', type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, itemStyle: { color: '#ef4444' }, data: y2 },
        { name: 'a = 0.5 (más abierta)', type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, itemStyle: { color: '#22c55e' }, data: y3 }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Elementos de la parábola

### Vértice

El punto más bajo (si $a > 0$) o más alto (si $a < 0$) de la parábola.

$$
x_v = -\frac{b}{2a}, \quad y_v = f(x_v)
$$

### Eje de simetría

Recta vertical que pasa por el vértice:

$$
x = -\frac{b}{2a}
$$

### Intercepto Y

Punto donde la parábola cruza el eje Y:

$$
(0, c)
$$

---

## 📖 Ejemplos

### Ejemplo 1

Para $f(x) = x^2 - 4x + 3$, identificar $a$, $b$, $c$.

$$
a = 1, \quad b = -4, \quad c = 3
$$

Como $a > 0$, la parábola abre hacia arriba.

**Vértice:**
$$
x_v = -\frac{-4}{2(1)} = 2
$$
$$
y_v = (2)^2 - 4(2) + 3 = 4 - 8 + 3 = -1
$$

Vértice: $(2, -1)$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo1" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo1')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo1'));
    var data = [];
    for (var x = -1; x <= 5; x += 0.1) { data.push([x, x*x - 4*x + 3]); }
    var option = {
      title: { text: '📊 Ejemplo 1: f(x) = x² - 4x + 3', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -2, max: 8, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#8b5cf6' }, data: data },
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'V(2,-1)', position: 'bottom', fontSize: 11, fontWeight: 'bold', color: '#ef4444' }, data: [[2, -1]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 2

Para $f(x) = -2x^2 + 8x - 6$:

$$
a = -2, \quad b = 8, \quad c = -6
$$

Como $a < 0$, la parábola abre hacia abajo.

**Vértice:**
$$
x_v = -\frac{8}{2(-2)} = 2
$$
$$
y_v = -2(4) + 16 - 6 = 2
$$

Vértice: $(2, 2)$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo2" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo2')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo2'));
    var data = [];
    for (var x = -0.5; x <= 4.5; x += 0.1) { data.push([x, -2*x*x + 8*x - 6]); }
    var option = {
      title: { text: '📊 Ejemplo 2: f(x) = -2x² + 8x - 6', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -7, max: 3, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: data },
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'V(2,2)', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#ef4444' }, data: [[2, 2]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 3

Para $f(x) = 3x^2 + 6x$:

$$
a = 3, \quad b = 6, \quad c = 0
$$

**Vértice:**
$$
x_v = -\frac{6}{6} = -1
$$
$$
y_v = 3(1) - 6 = -3
$$

Vértice: $(-1, -3)$

Intercepto Y: $(0, 0)$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo3" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo3')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo3'));
    var data = [];
    for (var x = -3; x <= 1; x += 0.1) { data.push([x, 3*x*x + 6*x]); }
    var option = {
      title: { text: '📊 Ejemplo 3: f(x) = 3x² + 6x', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -4, max: 2, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -4, max: 10, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#f59e0b' }, data: data },
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'V(-1,-3)', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#ef4444' }, data: [[-1, -3]] },
        { type: 'scatter', symbolSize: 10, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(0,0)', position: 'right', fontSize: 10, color: '#3b82f6' }, data: [[0, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Evaluando la función

### Ejemplo 4

Si $f(x) = x^2 - 5x + 6$, calcular $f(3)$.

$$
f(3) = 9 - 15 + 6 = 0
$$

$$
\boxed{f(3) = 0}
$$

---

### Ejemplo 5

Si $f(x) = 2x^2 - 3x + 1$, calcular $f(-2)$.

$$
f(-2) = 2(4) + 6 + 1 = 15
$$

$$
\boxed{f(-2) = 15}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Identifica $a$, $b$, $c$ en $f(x) = -x^2 + 6x - 5$.

<details>
<summary>Ver solución</summary>

$a = -1$, $b = 6$, $c = -5$

</details>

---

**Ejercicio 2:** ¿La parábola de $f(x) = 4x^2 - 1$ abre hacia arriba o hacia abajo?

<details>
<summary>Ver solución</summary>

Hacia arriba ($a = 4 > 0$)

</details>

---

**Ejercicio 3:** Encuentra el vértice de $f(x) = x^2 + 2x - 3$.

<details>
<summary>Ver solución</summary>

$x_v = -1$, $y_v = 1 - 2 - 3 = -4$

Vértice: $(-1, -4)$

</details>

---

**Ejercicio 4:** Calcula $f(2)$ si $f(x) = x^2 - 4x + 4$.

<details>
<summary>Ver solución</summary>

$f(2) = 4 - 8 + 4 = 0$

</details>

---
