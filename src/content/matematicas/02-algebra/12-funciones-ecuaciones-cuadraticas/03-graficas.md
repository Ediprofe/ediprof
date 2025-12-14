# 📊 Gráficas de Funciones Cuadráticas

En esta lección aprenderemos a graficar parábolas y analizar sus características.

---

## 📖 La idea clave

> 💡 **Para graficar completamente una parábola solo necesitas 3 cosas:**
> 
> 1. **¿Hacia dónde abre?** → Mira el signo de $a$
> 2. **¿Dónde está el vértice?** → Calcula $x_v = -\frac{b}{2a}$
> 3. **¿Dónde corta los ejes?** → Intercepto Y en $(0, c)$ y raíces (si existen)

Una vez tengas estos 3 elementos, ¡ya puedes trazar la parábola!

---

## 📖 Resumen de elementos

| Elemento | Cómo encontrarlo | Qué te dice |
|:---------|:-----------------|:------------|
| **Orientación** | Si $a > 0$ → ∪ (arriba), si $a < 0$ → ∩ (abajo) | Forma general de la curva |
| **Vértice** | $x_v = -\frac{b}{2a}$, luego $y_v = f(x_v)$ | Punto más bajo o más alto |
| **Intercepto Y** | $(0, c)$ — evaluar $f(0)$ | Dónde cruza el eje Y |
| **Interceptos X** | Resolver $ax^2 + bx + c = 0$ | Dónde cruza el eje X (raíces) |
| **Eje de simetría** | $x = x_v$ | Línea vertical por el vértice |

---

## 📖 Ejemplos

### Ejemplo 1

Graficar $f(x) = x^2 - 4x + 3$.

**Orientación**: $a = 1 > 0$, abre arriba

**Vértice**: $x_v = 2$, $y_v = 4 - 8 + 3 = -1$ → $(2, -1)$

**Intercepto Y**: $(0, 3)$

**Interceptos X**: $x^2 - 4x + 3 = 0$ → $(x-1)(x-3) = 0$ → $(1, 0)$ y $(3, 0)$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-graf-ej1" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-graf-ej1')) {
    var chart = echarts.init(document.getElementById('echarts-graf-ej1'));
    var data = [];
    for (var x = -0.5; x <= 4.5; x += 0.1) { data.push([x, x*x - 4*x + 3]); }
    var option = {
      title: { text: '📊 Ejemplo 1: f(x) = x² - 4x + 3', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -2, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, itemStyle: { color: '#3b82f6' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'V', position: 'bottom', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[2, -1]] },
        { type: 'scatter', symbolSize: 10, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, data: [[1, 0], [3, 0], [0, 3]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 2

Graficar $f(x) = -x^2 + 2x + 3$.

**Orientación**: $a = -1 < 0$, abre abajo

**Vértice**: $x_v = 1$, $y_v = -1 + 2 + 3 = 4$ → $(1, 4)$

**Intercepto Y**: $(0, 3)$

**Interceptos X**: $-x^2 + 2x + 3 = 0$ → $x^2 - 2x - 3 = 0$ → $x = -1, 3$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-graf-ej2" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-graf-ej2')) {
    var chart = echarts.init(document.getElementById('echarts-graf-ej2'));
    var data = [];
    for (var x = -2; x <= 4; x += 0.1) { data.push([x, -x*x + 2*x + 3]); }
    var option = {
      title: { text: '📊 Ejemplo 2: f(x) = -x² + 2x + 3', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -2, max: 4, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -5, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, itemStyle: { color: '#22c55e' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'V', position: 'top', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[1, 4]] },
        { type: 'scatter', symbolSize: 10, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, data: [[-1, 0], [3, 0], [0, 3]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 3

Graficar $f(x) = x^2 + 2x + 2$.

**Vértice**: $x_v = -1$, $y_v = 1 - 2 + 2 = 1$ → $(-1, 1)$

**Interceptos X**: $\Delta = 4 - 8 = -4 < 0$ → No intercepta el eje X

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-graf-ej3" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-graf-ej3')) {
    var chart = echarts.init(document.getElementById('echarts-graf-ej3'));
    var data = [];
    for (var x = -3.5; x <= 1.5; x += 0.1) { data.push([x, x*x + 2*x + 2]); }
    var option = {
      title: { text: '📊 Ejemplo 3: f(x) = x² + 2x + 2 (sin raíces)', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -4, max: 2, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: 0, max: 8, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#f59e0b' }, itemStyle: { color: '#f59e0b' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'V', position: 'right', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[-1, 1]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Formas de la función cuadrática

### Forma estándar

$$
f(x) = ax^2 + bx + c
$$

### Forma vértice

$$
f(x) = a(x - h)^2 + k
$$

donde $(h, k)$ es el vértice.

---

### Ejemplo 4

Convertir $f(x) = x^2 - 6x + 5$ a forma vértice.

Completando el cuadrado:
$$
f(x) = (x^2 - 6x + 9) - 9 + 5 = (x - 3)^2 - 4
$$

Vértice: $(3, -4)$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-graf-ej4" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-graf-ej4')) {
    var chart = echarts.init(document.getElementById('echarts-graf-ej4'));
    var data = [];
    for (var x = 0; x <= 6; x += 0.1) { data.push([x, x*x - 6*x + 5]); }
    var option = {
      title: { text: '📊 Ejemplo 4: f(x) = (x-3)² - 4', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: 0, max: 6, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -5, max: 6, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#8b5cf6' }, itemStyle: { color: '#8b5cf6' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'V(3,-4)', position: 'bottom', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[3, -4]] },
        { type: 'scatter', symbolSize: 10, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, data: [[1, 0], [5, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 5

De $f(x) = 2(x + 1)^2 - 3$, identificar el vértice.

$h = -1$, $k = -3$

Vértice: $(-1, -3)$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-graf-ej5" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-graf-ej5')) {
    var chart = echarts.init(document.getElementById('echarts-graf-ej5'));
    var data = [];
    for (var x = -3; x <= 1; x += 0.1) { data.push([x, 2*(x+1)*(x+1) - 3]); }
    var option = {
      title: { text: '📊 Ejemplo 5: f(x) = 2(x+1)² - 3', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -3.5, max: 1.5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -4, max: 6, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#ec4899' }, itemStyle: { color: '#ec4899' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'V(-1,-3)', position: 'right', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[-1, -3]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Máximos y mínimos

| Si $a > 0$ | Si $a < 0$ |
|:-----------|:-----------|
| Mínimo en el vértice | Máximo en el vértice |

### Ejemplo 6

Encontrar el valor mínimo de $f(x) = x^2 - 8x + 10$.

$x_v = 4$, $y_v = 16 - 32 + 10 = -6$

El mínimo es $-6$ cuando $x = 4$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-graf-ej6" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-graf-ej6')) {
    var chart = echarts.init(document.getElementById('echarts-graf-ej6'));
    var data = [];
    for (var x = 0; x <= 8; x += 0.1) { data.push([x, x*x - 8*x + 10]); }
    var option = {
      title: { text: '📊 Ejemplo 6: Mínimo de f(x) = x² - 8x + 10', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: 0, max: 8, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -7, max: 12, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#0ea5e9' }, itemStyle: { color: '#0ea5e9' }, data: data },
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Mín(-6)', position: 'right', fontSize: 11, fontWeight: 'bold', color: '#ef4444' }, data: [[4, -6]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 7

Graficar $f(x) = -2x^2 + 4x + 1$.

**Orientación**: $a = -2 < 0$, abre abajo (máximo)

**Vértice**: $x_v = 1$, $y_v = -2 + 4 + 1 = 3$ → $(1, 3)$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-graf-ej7" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-graf-ej7')) {
    var chart = echarts.init(document.getElementById('echarts-graf-ej7'));
    var data = [];
    for (var x = -1; x <= 3; x += 0.1) { data.push([x, -2*x*x + 4*x + 1]); }
    var option = {
      title: { text: '📊 Ejemplo 7: f(x) = -2x² + 4x + 1', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 3, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -5, max: 4, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#dc2626' }, itemStyle: { color: '#dc2626' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Máx(1,3)', position: 'top', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[1, 3]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 8

Graficar $f(x) = \frac{1}{2}x^2 - 2x$.

**Vértice**: $x_v = 2$, $y_v = 2 - 4 = -2$ → $(2, -2)$

**Interceptos X**: $\frac{1}{2}x(x - 4) = 0$ → $x = 0$ y $x = 4$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-graf-ej8" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-graf-ej8')) {
    var chart = echarts.init(document.getElementById('echarts-graf-ej8'));
    var data = [];
    for (var x = -1; x <= 5; x += 0.1) { data.push([x, 0.5*x*x - 2*x]); }
    var option = {
      title: { text: '📊 Ejemplo 8: f(x) = ½x² - 2x', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -3, max: 4, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#14b8a6' }, itemStyle: { color: '#14b8a6' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'V(2,-2)', position: 'bottom', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[2, -2]] },
        { type: 'scatter', symbolSize: 10, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, data: [[0, 0], [4, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 9

Graficar $f(x) = x^2 - 1$ (diferencia de cuadrados).

**Vértice**: $x_v = 0$, $y_v = -1$ → $(0, -1)$

**Interceptos X**: $x^2 - 1 = 0$ → $x = \pm 1$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-graf-ej9" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-graf-ej9')) {
    var chart = echarts.init(document.getElementById('echarts-graf-ej9'));
    var data = [];
    for (var x = -2.5; x <= 2.5; x += 0.1) { data.push([x, x*x - 1]); }
    var option = {
      title: { text: '📊 Ejemplo 9: f(x) = x² - 1', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -3, max: 3, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -2, max: 6, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#6366f1' }, itemStyle: { color: '#6366f1' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'V(0,-1)', position: 'right', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[0, -1]] },
        { type: 'scatter', symbolSize: 10, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, data: [[-1, 0], [1, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 10

Graficar $f(x) = (x - 2)^2$ (parábola con raíz doble).

**Vértice**: $(2, 0)$ — toca el eje X en un solo punto

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-graf-ej10" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-graf-ej10')) {
    var chart = echarts.init(document.getElementById('echarts-graf-ej10'));
    var data = [];
    for (var x = -0.5; x <= 4.5; x += 0.1) { data.push([x, (x-2)*(x-2)]); }
    var option = {
      title: { text: '📊 Ejemplo 10: f(x) = (x-2)² — raíz doble', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: 0, max: 8, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#f97316' }, itemStyle: { color: '#f97316' }, data: data },
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Raíz doble', position: 'right', fontSize: 10, fontWeight: 'bold', color: '#22c55e' }, data: [[2, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 11

Graficar $f(x) = -x^2 + 4x - 4$ (máximo en el eje X).

**Vértice**: $x_v = 2$, $y_v = -4 + 8 - 4 = 0$ → $(2, 0)$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-graf-ej11" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-graf-ej11')) {
    var chart = echarts.init(document.getElementById('echarts-graf-ej11'));
    var data = [];
    for (var x = -0.5; x <= 4.5; x += 0.1) { data.push([x, -x*x + 4*x - 4]); }
    var option = {
      title: { text: '📊 Ejemplo 11: f(x) = -x² + 4x - 4', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -6, max: 2, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#a855f7' }, itemStyle: { color: '#a855f7' }, data: data },
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Máx(2,0)', position: 'top', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[2, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra el vértice de $f(x) = x^2 + 4x + 1$.

<details>
<summary>Ver solución</summary>

$x_v = -2$, $y_v = 4 - 8 + 1 = -3$

Vértice: $(-2, -3)$

</details>

---

**Ejercicio 2:** ¿La parábola $f(x) = -3x^2 + 6x$ tiene máximo o mínimo?

<details>
<summary>Ver solución</summary>

Máximo (porque $a = -3 < 0$)

</details>

---

**Ejercicio 3:** Escribe $f(x) = x^2 - 2x - 3$ en forma vértice.

<details>
<summary>Ver solución</summary>

$f(x) = (x - 1)^2 - 4$

</details>

---

**Ejercicio 4:** Encuentra los interceptos X de $f(x) = x^2 - 5x + 6$.

<details>
<summary>Ver solución</summary>

$(x - 2)(x - 3) = 0$ → $x = 2, 3$

</details>

---
