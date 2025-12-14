# 🔍 Resolución de Ecuaciones Cuadráticas

En esta lección aprenderemos diferentes métodos para resolver ecuaciones cuadráticas.

---

## 📖 Ecuación cuadrática

Una **ecuación cuadrática** tiene la forma:

$$
ax^2 + bx + c = 0
$$

donde $a \neq 0$.

---

## 📖 ¿Qué significa resolver una ecuación cuadrática?

Resolver una ecuación cuadrática es encontrar los valores de $x$ que hacen que la expresión sea igual a cero.

> 💡 **Idea clave**: Si graficamos la función $f(x) = ax^2 + bx + c$, las **soluciones** de la ecuación $ax^2 + bx + c = 0$ son exactamente los puntos donde la parábola **corta el eje X**.

En otras palabras:
- Cuando la parábola **cruza** el eje X en dos puntos → hay **2 soluciones**
- Cuando la parábola **toca** el eje X en un punto → hay **1 solución** 
- Cuando la parábola **no toca** el eje X → **no hay solución real**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-intro-soluciones" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-intro-soluciones')) {
    var chart = echarts.init(document.getElementById('echarts-intro-soluciones'));
    var data1 = [], data2 = [], data3 = [];
    for (var x = -2; x <= 4; x += 0.1) { data1.push([x, x*x - 2*x - 3]); }
    for (var x = -1; x <= 3; x += 0.1) { data2.push([x, (x-1)*(x-1)]); }
    for (var x = -1; x <= 3; x += 0.1) { data3.push([x, x*x - 2*x + 2]); }
    var option = {
      title: { text: '📊 Las soluciones son los cortes con el eje X', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['2 soluciones', '1 solución', 'Sin solución real'], top: 35, textStyle: { fontSize: 10 } },
      grid: { left: '10%', right: '8%', top: '22%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -2, max: 4, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -5, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { name: '2 soluciones', type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, itemStyle: { color: '#3b82f6' }, data: data1 },
        { name: '1 solución', type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, itemStyle: { color: '#22c55e' }, data: data2 },
        { name: 'Sin solución real', type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, itemStyle: { color: '#ef4444' }, data: data3 },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, data: [[-1, 0], [3, 0]] },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, data: [[1, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Método 1: Factorización

Si podemos factorizar la expresión, usamos la propiedad del producto cero.

### Ejemplo 1

Resolver $x^2 - 5x + 6 = 0$.

$$
(x - 2)(x - 3) = 0
$$

$$
x = 2 \quad \text{o} \quad x = 3
$$

$$
\boxed{x = 2, \quad x = 3}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-resol-ej1" style="width: 100%; height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-resol-ej1')) {
    var chart = echarts.init(document.getElementById('echarts-resol-ej1'));
    var data = [];
    for (var x = 0; x <= 5; x += 0.1) { data.push([x, x*x - 5*x + 6]); }
    var option = {
      title: { text: '📊 f(x) = x² - 5x + 6', left: 'center', textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '18%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 22, min: 0, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 25, min: -1, max: 6, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, itemStyle: { color: '#3b82f6' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return 'x=' + p.data[0]; }, position: 'top', fontSize: 10, fontWeight: 'bold', color: '#22c55e' }, data: [[2, 0], [3, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 2

Resolver $x^2 - 9 = 0$.

$$
(x - 3)(x + 3) = 0
$$

$$
\boxed{x = 3, \quad x = -3}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-resol-ej2" style="width: 100%; height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-resol-ej2')) {
    var chart = echarts.init(document.getElementById('echarts-resol-ej2'));
    var data = [];
    for (var x = -4; x <= 4; x += 0.1) { data.push([x, x*x - 9]); }
    var option = {
      title: { text: '📊 f(x) = x² - 9', left: 'center', textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '18%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 22, min: -4, max: 4, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 25, min: -10, max: 8, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, itemStyle: { color: '#22c55e' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return 'x=' + p.data[0]; }, position: 'top', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[-3, 0], [3, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Método 2: Fórmula general

La **fórmula cuadrática** resuelve cualquier ecuación $ax^2 + bx + c = 0$:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

### Ejemplo 3

Resolver $2x^2 + 5x - 3 = 0$.

$$
a = 2, \quad b = 5, \quad c = -3
$$

$$
x = \frac{-5 \pm \sqrt{25 + 24}}{4} = \frac{-5 \pm 7}{4}
$$

$$
x_1 = \frac{2}{4} = \frac{1}{2}, \quad x_2 = \frac{-12}{4} = -3
$$

$$
\boxed{x = \frac{1}{2}, \quad x = -3}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-resol-ej3" style="width: 100%; height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-resol-ej3')) {
    var chart = echarts.init(document.getElementById('echarts-resol-ej3'));
    var data = [];
    for (var x = -4; x <= 1; x += 0.1) { data.push([x, 2*x*x + 5*x - 3]); }
    var option = {
      title: { text: '📊 f(x) = 2x² + 5x - 3', left: 'center', textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '18%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 22, min: -4, max: 1, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 25, min: -5, max: 10, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#8b5cf6' }, itemStyle: { color: '#8b5cf6' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return 'x=' + p.data[0]; }, position: 'top', fontSize: 10, fontWeight: 'bold', color: '#22c55e' }, data: [[0.5, 0], [-3, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 4

Resolver $x^2 - 4x + 1 = 0$.

$$
x = \frac{4 \pm \sqrt{16 - 4}}{2} = \frac{4 \pm \sqrt{12}}{2} = \frac{4 \pm 2\sqrt{3}}{2} = 2 \pm \sqrt{3}
$$

$$
\boxed{x = 2 + \sqrt{3}, \quad x = 2 - \sqrt{3}}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-resol-ej4" style="width: 100%; height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-resol-ej4')) {
    var chart = echarts.init(document.getElementById('echarts-resol-ej4'));
    var data = [];
    for (var x = -0.5; x <= 4.5; x += 0.1) { data.push([x, x*x - 4*x + 1]); }
    var option = {
      title: { text: '📊 f(x) = x² - 4x + 1', left: 'center', textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '18%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 22, min: -0.5, max: 4.5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 25, min: -4, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#f59e0b' }, itemStyle: { color: '#f59e0b' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return 'x≈0.27'; }, position: 'top', fontSize: 9, fontWeight: 'bold', color: '#22c55e' }, data: [[0.27, 0]] },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return 'x≈3.73'; }, position: 'top', fontSize: 9, fontWeight: 'bold', color: '#22c55e' }, data: [[3.73, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 El discriminante

El **discriminante** $\Delta = b^2 - 4ac$ determina el número de soluciones:

| Discriminante | Soluciones |
|:-------------:|:-----------|
| $\Delta > 0$ | 2 soluciones reales distintas |
| $\Delta = 0$ | 1 solución real (doble) |
| $\Delta < 0$ | 2 soluciones complejas |

---

### Ejemplo 5

¿Cuántas soluciones tiene $x^2 - 6x + 9 = 0$?

$$
\Delta = 36 - 36 = 0
$$

Una solución (raíz doble): $x = 3$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-resol-ej5" style="width: 100%; height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-resol-ej5')) {
    var chart = echarts.init(document.getElementById('echarts-resol-ej5'));
    var data = [];
    for (var x = 0; x <= 6; x += 0.1) { data.push([x, (x-3)*(x-3)]); }
    var option = {
      title: { text: '📊 f(x) = x² - 6x + 9 (raíz doble)', left: 'center', textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '18%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 22, min: 0, max: 6, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 25, min: 0, max: 10, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#ec4899' }, itemStyle: { color: '#ec4899' }, data: data },
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'x=3', position: 'right', fontSize: 10, fontWeight: 'bold', color: '#22c55e' }, data: [[3, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 6

¿Cuántas soluciones tiene $x^2 + x + 1 = 0$?

$$
\Delta = 1 - 4 = -3 < 0
$$

Dos soluciones complejas.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-resol-ej6" style="width: 100%; height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-resol-ej6')) {
    var chart = echarts.init(document.getElementById('echarts-resol-ej6'));
    var data = [];
    for (var x = -2; x <= 1; x += 0.1) { data.push([x, x*x + x + 1]); }
    var option = {
      title: { text: '📊 f(x) = x² + x + 1 (no toca eje X)', left: 'center', textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '18%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 22, min: -2, max: 1, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 25, min: 0, max: 4, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, itemStyle: { color: '#ef4444' }, data: data }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Método 3: Completar el cuadrado

### Ejemplo 7

Resolver $x^2 + 6x + 5 = 0$ completando el cuadrado.

$$
x^2 + 6x = -5
$$
$$
x^2 + 6x + 9 = -5 + 9
$$
$$
(x + 3)^2 = 4
$$
$$
x + 3 = \pm 2
$$
$$
x = -1 \quad \text{o} \quad x = -5
$$

$$
\boxed{x = -1, \quad x = -5}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-resol-ej7" style="width: 100%; height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-resol-ej7')) {
    var chart = echarts.init(document.getElementById('echarts-resol-ej7'));
    var data = [];
    for (var x = -6; x <= 0; x += 0.1) { data.push([x, x*x + 6*x + 5]); }
    var option = {
      title: { text: '📊 f(x) = x² + 6x + 5', left: 'center', textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '18%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 22, min: -6, max: 0, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 25, min: -5, max: 6, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#14b8a6' }, itemStyle: { color: '#14b8a6' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return 'x=' + p.data[0]; }, position: 'top', fontSize: 10, fontWeight: 'bold', color: '#22c55e' }, data: [[-1, 0], [-5, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve $x^2 - 7x + 12 = 0$ por factorización.

<details>
<summary>Ver solución</summary>

$(x - 3)(x - 4) = 0$

$x = 3$ o $x = 4$

</details>

---

**Ejercicio 2:** Resuelve $x^2 + 2x - 8 = 0$ usando la fórmula general.

<details>
<summary>Ver solución</summary>

$x = \frac{-2 \pm \sqrt{4 + 32}}{2} = \frac{-2 \pm 6}{2}$

$x = 2$ o $x = -4$

</details>

---

**Ejercicio 3:** Calcula el discriminante de $3x^2 - 2x + 5 = 0$.

<details>
<summary>Ver solución</summary>

$\Delta = 4 - 60 = -56 < 0$ (soluciones complejas)

</details>

---

**Ejercicio 4:** Resuelve $x^2 = 16$.

<details>
<summary>Ver solución</summary>

$x = \pm 4$

</details>

---
