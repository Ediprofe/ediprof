# 📊 Representación Gráfica de Funciones Lineales

En esta lección aprenderemos diferentes métodos para graficar funciones lineales.

---

## 📖 Método 1: Tabla de valores

El método más directo es crear una **tabla de valores**, sustituyendo diferentes valores de $x$ para obtener $y$.

### Ejemplo 1

Graficar $y = 2x + 1$.

| $x$ | $y = 2x + 1$ |
|:---:|:------------:|
| $-2$ | $-3$ |
| $-1$ | $-1$ |
| $0$ | $1$ |
| $1$ | $3$ |
| $2$ | $5$ |

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo1-tabla" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo1-tabla')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo1-tabla'));
    var option = {
      title: { text: 'Ejemplo 1: y = 2x + 1', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -3, max: 3, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -4, max: 6, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[-2, -3], [2, 5]] },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, data: [[-2, -3], [-1, -1], [0, 1], [1, 3], [2, 5]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 2

Graficar $y = -x + 3$.

| $x$ | $y = -x + 3$ |
|:---:|:------------:|
| $-1$ | $4$ |
| $0$ | $3$ |
| $1$ | $2$ |
| $2$ | $1$ |
| $3$ | $0$ |

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo2-tabla" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo2-tabla')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo2-tabla'));
    var option = {
      title: { text: 'Ejemplo 2: y = -x + 3', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -2, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -1, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, data: [[-1, 4], [3, 0]] },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, data: [[-1, 4], [0, 3], [1, 2], [2, 1], [3, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Método 2: Interceptos

Solo necesitamos **dos puntos** para trazar una recta. Los más fáciles de encontrar son los interceptos.

### Pasos

1. **Intercepto Y**: Hacer $x = 0$ y encontrar $y$
2. **Intercepto X**: Hacer $y = 0$ y encontrar $x$
3. Unir los dos puntos

---

### Ejemplo 3

Graficar $y = 3x - 6$ usando interceptos.

**Intercepto Y** ($x = 0$):
$$
y = 3(0) - 6 = -6 \quad \Rightarrow \quad (0, -6)
$$

**Intercepto X** ($y = 0$):
$$
0 = 3x - 6 \quad \Rightarrow \quad x = 2 \quad \Rightarrow \quad (2, 0)
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo3-interceptos" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo3-interceptos')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo3-interceptos'));
    var option = {
      title: { text: 'Ejemplo 3: y = 3x - 6', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -7, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[-1, -9], [3, 3]] },
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return '(' + p.data[0] + ',' + p.data[1] + ')'; }, position: 'right', fontSize: 11, fontWeight: 'bold' }, data: [[0, -6], [2, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 4

Graficar $y = -2x + 4$ usando interceptos.

**Intercepto Y**: $(0, 4)$

**Intercepto X**: $0 = -2x + 4$, $x = 2$ → $(2, 0)$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo4-interceptos" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo4-interceptos')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo4-interceptos'));
    var option = {
      title: { text: 'Ejemplo 4: y = -2x + 4', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -3, max: 6, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[-1, 6], [3, -2]] },
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return '(' + p.data[0] + ',' + p.data[1] + ')'; }, position: 'right', fontSize: 11, fontWeight: 'bold' }, data: [[0, 4], [2, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Método 3: Pendiente e intercepto

Usamos el intercepto Y como punto inicial y la pendiente para encontrar otros puntos.

### Pasos

1. Marcar el intercepto Y: $(0, b)$
2. Desde ahí, usar la pendiente $m = \frac{\text{subida}}{\text{corrida}}$
3. Trazar la recta

---

### Ejemplo 5

Graficar $y = \frac{2}{3}x - 1$.

**Intercepto Y**: $(0, -1)$

**Pendiente**: $m = \frac{2}{3}$
- Subimos $2$ unidades
- Avanzamos $3$ unidades a la derecha
- Llegamos al punto $(3, 1)$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo5-pendiente" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo5-pendiente')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo5-pendiente'));
    var option = {
      title: { text: 'Ejemplo 5: y = (2/3)x - 1', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -3, max: 6, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -3, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[-3, -3], [6, 3]] },
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return '(' + p.data[0] + ',' + p.data[1] + ')'; }, position: 'right', fontSize: 11, fontWeight: 'bold' }, data: [[0, -1], [3, 1]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 6

Graficar $y = -\frac{3}{4}x + 2$.

**Intercepto Y**: $(0, 2)$

**Pendiente**: $m = -\frac{3}{4}$
- Bajamos $3$ unidades
- Avanzamos $4$ unidades a la derecha
- Llegamos al punto $(4, -1)$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo6-pendiente" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo6-pendiente')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo6-pendiente'));
    var option = {
      title: { text: 'Ejemplo 6: y = (-3/4)x + 2', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -2, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -2, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#a855f7' }, data: [[-2, 3.5], [4, -1]] },
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#a855f7', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return '(' + p.data[0] + ',' + p.data[1] + ')'; }, position: 'right', fontSize: 11, fontWeight: 'bold' }, data: [[0, 2], [4, -1]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Casos especiales

### Recta horizontal

$$
y = b
$$

### Ejemplo 7

Graficar $y = 3$.

Todos los puntos tienen $y = 3$: $(-2, 3)$, $(0, 3)$, $(5, 3)$...

Es una línea horizontal que cruza el eje Y en $3$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo7-horizontal" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo7-horizontal')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo7-horizontal'));
    var option = {
      title: { text: 'Ejemplo 7: y = 3 (horizontal)', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -4, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: 0, max: 6, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#f59e0b' }, data: [[-4, 3], [5, 3]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Recta vertical

$$
x = a
$$

> Nota: Las rectas verticales **no son funciones** porque un valor de $x$ tiene infinitos valores de $y$.

### Ejemplo 8

Graficar $x = 2$.

Todos los puntos tienen $x = 2$: $(2, -3)$, $(2, 0)$, $(2, 5)$...

Es una línea vertical que cruza el eje X en $2$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo8-vertical" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo8-vertical')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo8-vertical'));
    var option = {
      title: { text: 'Ejemplo 8: x = 2 (vertical)', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -4, max: 6, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#ef4444', type: 'dashed' }, data: [[2, -4], [2, 6]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Recta que pasa por el origen

$$
y = mx
$$

### Ejemplo 9

Graficar $y = -2x$.

Pasa por $(0, 0)$. Usamos la pendiente para encontrar otro punto:
- $m = -2 = \frac{-2}{1}$
- Desde el origen, bajamos $2$ y avanzamos $1$: $(1, -2)$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo9-origen" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo9-origen')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo9-origen'));
    var option = {
      title: { text: 'Ejemplo 9: y = -2x', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -2, max: 3, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -5, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#6366f1' }, data: [[-2, 4], [2, -4]] },
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#6366f1', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return '(' + p.data[0] + ',' + p.data[1] + ')'; }, position: 'top', fontSize: 11, fontWeight: 'bold' }, data: [[0, 0], [1, -2]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Comparando pendientes

### Ejemplo 10

Comparar las gráficas de:
- $y = x$
- $y = 2x$
- $y = \frac{1}{2}x$

Todas pasan por el origen, pero tienen diferentes inclinaciones:
- $y = 2x$ es la más empinada ($|m| = 2$)
- $y = x$ tiene inclinación media ($|m| = 1$)
- $y = \frac{1}{2}x$ es la menos empinada ($|m| = 0.5$)

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo10-comparacion" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo10-comparacion')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo10-comparacion'));
    var option = {
      title: { text: 'Ejemplo 10: Comparación de pendientes', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['y = 2x', 'y = x', 'y = ½x'], top: 30, textStyle: { fontSize: 11 } },
      grid: { left: '12%', right: '8%', top: '20%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -4, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -5, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'y = 2x', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[-2, -4], [0, 0], [2, 4]] },
        { name: 'y = x', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[-4, -4], [0, 0], [4, 4]] },
        { name: 'y = ½x', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#a855f7' }, data: [[-4, -2], [0, 0], [4, 2]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📋 Resumen de métodos

| Método | Procedimiento |
|:-------|:--------------|
| Tabla de valores | Calcular varios puntos |
| Interceptos | Encontrar donde cruza los ejes |
| Pendiente-intercepto | Usar $(0, b)$ y moverse según $m$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra los interceptos de $y = 4x - 8$.

<details>
<summary>Ver solución</summary>

Intercepto Y: $(0, -8)$

Intercepto X: $(2, 0)$

</details>

---

**Ejercicio 2:** ¿Por qué punto pasa la recta $y = 5x$?

<details>
<summary>Ver solución</summary>

Por el origen $(0, 0)$

</details>

---

**Ejercicio 3:** ¿Qué representa la ecuación $y = -4$?

<details>
<summary>Ver solución</summary>

Una recta horizontal que pasa por $(0, -4)$

</details>

---

**Ejercicio 4:** Para $y = \frac{3}{2}x + 1$, partiendo de $(0, 1)$, ¿a qué punto llegas usando la pendiente?

<details>
<summary>Ver solución</summary>

Subimos $3$, avanzamos $2$: $(2, 4)$

</details>

---

**Ejercicio 5:** ¿Es $x = 5$ una función?

<details>
<summary>Ver solución</summary>

No, porque para $x = 5$ hay infinitos valores de $y$.

</details>

---

**Ejercicio 6:** Crea una tabla de valores para $y = -x + 2$ con $x = -1, 0, 1, 2, 3$.

<details>
<summary>Ver solución</summary>

| $x$ | $y$ |
|:---:|:---:|
| $-1$ | $3$ |
| $0$ | $2$ |
| $1$ | $1$ |
| $2$ | $0$ |
| $3$ | $-1$ |

</details>

---
