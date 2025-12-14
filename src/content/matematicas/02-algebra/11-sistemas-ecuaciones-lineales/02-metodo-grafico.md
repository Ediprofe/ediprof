# 📊 Método Gráfico

En esta lección aprenderemos a resolver sistemas de ecuaciones lineales mediante la representación gráfica de las rectas.

---

## 📖 ¿En qué consiste el método?

1. **Expresar** cada ecuación en forma $y = mx + b$
2. **Graficar** ambas rectas en el mismo plano
3. **Identificar** el punto de intersección
4. **Leer** las coordenadas de la solución

---

## 📖 Pasos detallados

### Paso 1: Convertir a forma pendiente-intercepto

Cada ecuación debe expresarse como:
$$
y = mx + b
$$

### Paso 2: Graficar cada recta

Usar los métodos aprendidos:
- Tabla de valores
- Pendiente e intercepto
- Interceptos con los ejes

### Paso 3: Encontrar la intersección

El punto donde las rectas se cruzan es la solución.

---

## 📖 Ejemplos

### Ejemplo 1

Resolver gráficamente:
$$
\begin{cases}
x + y = 4 \\
x - y = 2
\end{cases}
$$

**Convertimos a forma pendiente-intercepto:**

Primera: $y = -x + 4$ (pendiente $-1$, intercepto $4$)

Segunda: $y = x - 2$ (pendiente $1$, intercepto $-2$)

**Las rectas se cruzan en $(3, 1)$.**

$$
\boxed{x = 3, \quad y = 1}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo1-sistema" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo1-sistema')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo1-sistema'));
    var option = {
      title: { text: 'Ejemplo 1: x+y=4, x-y=2', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['y = -x + 4', 'y = x - 2'], top: 30, textStyle: { fontSize: 11 } },
      grid: { left: '12%', right: '8%', top: '20%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: 0, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -3, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'y = -x + 4', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[0, 4], [4, 0]] },
        { name: 'y = x - 2', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[0, -2], [5, 3]] },
        { type: 'scatter', symbolSize: 16, symbol: 'diamond', itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(3, 1)', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#ef4444' }, data: [[3, 1]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 2

Resolver gráficamente:
$$
\begin{cases}
2x + y = 6 \\
x - y = 0
\end{cases}
$$

**Convertimos:**

Primera: $y = -2x + 6$

Segunda: $y = x$

**Punto de intersección: $(2, 2)$**

$$
\boxed{x = 2, \quad y = 2}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo2-sistema" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo2-sistema')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo2-sistema'));
    var option = {
      title: { text: 'Ejemplo 2: 2x+y=6, x-y=0', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['y = -2x + 6', 'y = x'], top: 30, textStyle: { fontSize: 11 } },
      grid: { left: '12%', right: '8%', top: '20%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: 0, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: 0, max: 7, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'y = -2x + 6', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[0, 6], [3, 0]] },
        { name: 'y = x', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[0, 0], [4, 4]] },
        { type: 'scatter', symbolSize: 16, symbol: 'diamond', itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(2, 2)', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#ef4444' }, data: [[2, 2]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 3

Resolver gráficamente:
$$
\begin{cases}
y = 2x - 1 \\
y = -x + 5
\end{cases}
$$

Ya están en forma pendiente-intercepto.

**Punto de intersección: $(2, 3)$**

$$
\boxed{x = 2, \quad y = 3}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo3-sistema" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo3-sistema')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo3-sistema'));
    var option = {
      title: { text: 'Ejemplo 3: y=2x-1, y=-x+5', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['y = 2x - 1', 'y = -x + 5'], top: 30, textStyle: { fontSize: 11 } },
      grid: { left: '12%', right: '8%', top: '20%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: 0, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -2, max: 6, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'y = 2x - 1', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[0, -1], [3, 5]] },
        { name: 'y = -x + 5', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[0, 5], [5, 0]] },
        { type: 'scatter', symbolSize: 16, symbol: 'diamond', itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(2, 3)', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#ef4444' }, data: [[2, 3]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 4 (Rectas paralelas)

$$
\begin{cases}
y = 2x + 1 \\
y = 2x - 3
\end{cases}
$$

Ambas rectas tienen pendiente $m = 2$ pero diferentes interceptos.

**Las rectas son paralelas** → No se cruzan → **Sin solución**

$$
\boxed{\text{Sin solución (sistema incompatible)}}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo4-incompatible" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo4-incompatible')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo4-incompatible'));
    var option = {
      title: { text: 'Ejemplo 4: Sistema incompatible (paralelas)', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['y = 2x + 1', 'y = 2x - 3'], top: 30, textStyle: { fontSize: 11 } },
      grid: { left: '12%', right: '8%', top: '20%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 4, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -4, max: 10, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'y = 2x + 1', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, data: [[-1, -1], [4, 9]] },
        { name: 'y = 2x - 3', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#f87171', type: 'dashed' }, data: [[-1, -5], [4, 5]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 5 (Rectas coincidentes)

$$
\begin{cases}
x + y = 3 \\
2x + 2y = 6
\end{cases}
$$

**Convertimos:**

Primera: $y = -x + 3$

Segunda: $y = -x + 3$

**Son la misma recta** → **Infinitas soluciones**

$$
\boxed{\text{Infinitas soluciones}}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo5-indeterminado" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo5-indeterminado')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo5-indeterminado'));
    var option = {
      title: { text: 'Ejemplo 5: Sistema compatible indeterminado (coincidentes)', left: 'center', textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['x + y = 3', '2x + 2y = 6 (misma recta)'], top: 30, textStyle: { fontSize: 10 } },
      grid: { left: '12%', right: '8%', top: '22%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -1, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'x + y = 3', type: 'line', symbol: 'none', lineStyle: { width: 4, color: '#22c55e' }, data: [[0, 3], [3, 0]] },
        { name: '2x + 2y = 6 (misma recta)', type: 'line', symbol: 'none', lineStyle: { width: 2, color: '#86efac', type: 'dashed' }, data: [[0, 3], [3, 0]] },
        { type: 'scatter', symbolSize: 10, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 1 }, data: [[0, 3], [1, 2], [2, 1], [3, 0]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Interpretación gráfica de los tipos de sistemas

| Tipo | Gráfica | Solución |
|:-----|:--------|:---------|
| Compatible determinado | Rectas secantes | Un punto |
| Compatible indeterminado | Rectas coincidentes | Infinitos puntos |
| Incompatible | Rectas paralelas | Ningún punto |

---

## 📖 Ventajas y desventajas

### Ventajas
- Visual e intuitivo
- Permite ver la relación entre las ecuaciones
- Útil para estimar soluciones

### Desventajas
- Impreciso si la solución no son enteros
- Difícil con números grandes o fracciones
- Requiere papel cuadriculado o software

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Grafica y resuelve: $\begin{cases} x + y = 5 \\ x - y = 1 \end{cases}$

<details>
<summary>Ver solución</summary>

$y = -x + 5$ y $y = x - 1$

Intersección en $(3, 2)$

</details>

---

**Ejercicio 2:** ¿Qué tipo de sistema es si ambas rectas tienen pendiente $m = 3$?

<details>
<summary>Ver solución</summary>

- Si tienen el mismo intercepto: infinitas soluciones
- Si tienen diferente intercepto: sin solución

</details>

---

**Ejercicio 3:** Grafica y resuelve: $\begin{cases} y = x + 2 \\ y = -x + 4 \end{cases}$

<details>
<summary>Ver solución</summary>

Igualando: $x + 2 = -x + 4$, $x = 1$, $y = 3$

Intersección en $(1, 3)$

</details>

---

**Ejercicio 4:** ¿Cuántas soluciones tiene $\begin{cases} 4x - 2y = 6 \\ 2x - y = 3 \end{cases}$?

<details>
<summary>Ver solución</summary>

Segunda × 2 = Primera → Son la misma recta

Infinitas soluciones.

</details>

---
