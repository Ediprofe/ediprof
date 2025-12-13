# 📈 Introducción a las Funciones Lineales

En esta lección introduciremos el concepto de función lineal, su importancia y aplicaciones en la vida cotidiana.

---

## 📖 ¿Por qué estudiar funciones lineales?

Las funciones lineales están en todas partes en nuestra vida cotidiana:

- **Salarios**: Si ganas 50 pesos por hora, tu ingreso depende linealmente de las horas trabajadas.
- **Distancia**: Si un auto viaja a velocidad constante de 80 km/h, la distancia recorrida es proporcional al tiempo.
- **Costos**: El costo total de un taxi incluye una tarifa base más un costo por kilómetro.
- **Temperatura**: La conversión entre Celsius y Fahrenheit es una relación lineal.

---

## 📖 ¿Qué es una función?

Una **función** es una relación entre dos variables donde a cada valor de la variable independiente ($x$) le corresponde un único valor de la variable dependiente ($y$).

$$
y = f(x)
$$

Se lee "$y$ es igual a $f$ de $x$" o "$y$ es función de $x$".

---

## 📖 Función lineal: Definición

Una **función lineal** es aquella cuya gráfica es una **línea recta**. Tiene la forma:

$$
f(x) = mx + b
$$

o equivalentemente:

$$
y = mx + b
$$

donde:
- $m$ es la **pendiente** (indica la inclinación de la recta)
- $b$ es el **intercepto con el eje y** (punto donde la recta cruza el eje vertical)

---

## 📖 Ejemplos de funciones lineales

### Ejemplo 1: Salario por horas

Un trabajador gana 15 pesos por hora. Si trabaja $x$ horas, su salario es:

$$
f(x) = 15x
$$

Aquí $m = 15$ (gana 15 por hora) y $b = 0$ (no hay pago base).

| Horas ($x$) | Salario ($y$) |
|:-----------:|:-------------:|
| 0 | 0 |
| 1 | 15 |
| 5 | 75 |
| 8 | 120 |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-salario" style="width: 100%; height: 400px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-salario')) {
    var chart = echarts.init(document.getElementById('echarts-salario'));
    
    var option = {
      title: {
        text: 'Salario vs Horas trabajadas',
        subtext: 'f(x) = 15x',
        left: 'center',
        textStyle: { fontSize: 16, fontWeight: 'bold', color: '#1e293b' },
        subtextStyle: { fontSize: 13, color: '#3b82f6', fontWeight: 'bold' }
      },
      animation: true,
      animationDuration: 1000,
      grid: { left: '15%', right: '8%', top: '18%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: {
        type: 'value',
        name: 'Horas (x)',
        nameLocation: 'middle',
        nameGap: 32,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: 0,
        max: 9,
        axisLine: { lineStyle: { color: '#64748b' } },
        splitLine: { show: true, lineStyle: { type: 'solid', color: '#94a3b8', width: 1 } }
      },
      yAxis: {
        type: 'value',
        name: 'Salario ($)',
        nameLocation: 'middle',
        nameGap: 50,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: 0,
        max: 140,
        axisLine: { lineStyle: { color: '#64748b' } },
        splitLine: { show: true, lineStyle: { type: 'solid', color: '#94a3b8', width: 1 } }
      },
      series: [
        {
          name: 'f(x) = 15x',
          type: 'line',
          smooth: true,
          symbol: 'none',
          lineStyle: { width: 3, color: '#3b82f6' },
          areaStyle: {
            color: {
              type: 'linear',
              x: 0, y: 0, x2: 0, y2: 1,
              colorStops: [
                { offset: 0, color: 'rgba(59, 130, 246, 0.3)' },
                { offset: 1, color: 'rgba(59, 130, 246, 0.05)' }
              ]
            }
          },
          data: [[0, 0], [1, 15], [2, 30], [3, 45], [4, 60], [5, 75], [6, 90], [7, 105], [8, 120]]
        },
        {
          name: 'Puntos',
          type: 'scatter',
          symbolSize: 12,
          itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 },
          label: { show: true, formatter: function(p) { return '(' + p.data[0] + ', ' + p.data[1] + ')'; }, position: 'top', fontSize: 10 },
          data: [[0, 0], [1, 15], [5, 75], [8, 120]]
        }
      ],
      tooltip: { trigger: 'axis', formatter: 'Horas: {b}<br/>Salario: ${c}' }
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 2: Servicio de taxi

Un taxi cobra 3 pesos de tarifa base más 2 pesos por kilómetro. El costo de un viaje de $x$ kilómetros es:

$$
f(x) = 2x + 3
$$

Aquí $m = 2$ (costo por km) y $b = 3$ (tarifa base).

| Kilómetros ($x$) | Costo ($y$) |
|:----------------:|:-----------:|
| 0 | 3 |
| 5 | 13 |
| 10 | 23 |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-taxi" style="width: 100%; height: 400px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-taxi')) {
    var chart = echarts.init(document.getElementById('echarts-taxi'));
    
    var option = {
      title: {
        text: 'Costo del taxi vs Kilómetros',
        subtext: 'f(x) = 2x + 3',
        left: 'center',
        textStyle: { fontSize: 16, fontWeight: 'bold', color: '#1e293b' },
        subtextStyle: { fontSize: 13, color: '#ef4444', fontWeight: 'bold' }
      },
      animation: true,
      animationDuration: 1000,
      grid: { left: '15%', right: '8%', top: '18%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: {
        type: 'value',
        name: 'Kilómetros (x)',
        nameLocation: 'middle',
        nameGap: 32,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: 0,
        max: 12,
        axisLine: { lineStyle: { color: '#64748b' } },
        splitLine: { show: true, lineStyle: { type: 'solid', color: '#94a3b8', width: 1 } }
      },
      yAxis: {
        type: 'value',
        name: 'Costo ($)',
        nameLocation: 'middle',
        nameGap: 45,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: 0,
        max: 28,
        axisLine: { lineStyle: { color: '#64748b' } },
        splitLine: { show: true, lineStyle: { type: 'solid', color: '#94a3b8', width: 1 } }
      },
      series: [
        {
          name: 'f(x) = 2x + 3',
          type: 'line',
          smooth: true,
          symbol: 'none',
          lineStyle: { width: 3, color: '#ef4444' },
          areaStyle: {
            color: {
              type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
              colorStops: [
                { offset: 0, color: 'rgba(239, 68, 68, 0.25)' },
                { offset: 1, color: 'rgba(239, 68, 68, 0.02)' }
              ]
            }
          },
          data: [[0, 3], [2, 7], [4, 11], [6, 15], [8, 19], [10, 23]]
        },
        {
          name: 'Puntos',
          type: 'scatter',
          symbolSize: 12,
          itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 },
          label: { show: true, formatter: function(p) { return '(' + p.data[0] + ', ' + p.data[1] + ')'; }, position: 'top', fontSize: 10 },
          data: [[0, 3], [5, 13], [10, 23]]
        },
        {
          name: 'Intercepto',
          type: 'scatter',
          symbolSize: 14,
          symbol: 'diamond',
          itemStyle: { color: '#f97316', borderColor: '#fff', borderWidth: 2 },
          label: { show: true, formatter: 'b = 3', position: 'right', fontSize: 11, fontWeight: 'bold', color: '#f97316' },
          data: [[0, 3]]
        }
      ],
      tooltip: { trigger: 'axis' }
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 3: Temperatura

La conversión de Celsius a Fahrenheit es:

$$
F = \frac{9}{5}C + 32
$$

Aquí $m = \frac{9}{5} = 1.8$ y $b = 32$.

| Celsius | Fahrenheit |
|:-------:|:----------:|
| 0 | 32 |
| 20 | 68 |
| 100 | 212 |

---

## 📖 Elementos de una función lineal

### La pendiente (m)

La **pendiente** indica:
- **Cuánto cambia $y$** cuando $x$ aumenta en una unidad
- La **inclinación** de la recta

| Valor de $m$ | Tipo de recta |
|:------------:|:--------------|
| $m > 0$ | Recta ascendente (sube de izquierda a derecha) |
| $m < 0$ | Recta descendente (baja de izquierda a derecha) |
| $m = 0$ | Recta horizontal |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-pendientes" style="width: 100%; height: 400px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-pendientes')) {
    var chart = echarts.init(document.getElementById('echarts-pendientes'));
    var option = {
      title: { text: 'Tipos de pendiente en funciones lineales', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      legend: { data: ['m > 0 (ascendente)', 'm < 0 (descendente)', 'm = 0 (horizontal)'], bottom: 5, textStyle: { fontSize: 11 } },
      grid: { left: '12%', right: '8%', top: '12%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'end', min: -5, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'end', min: -4, max: 6, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { name: 'm > 0 (ascendente)', type: 'line', smooth: false, symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[-4, -3], [-2, -1], [0, 1], [2, 3], [4, 5]] },
        { name: 'm < 0 (descendente)', type: 'line', smooth: false, symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, data: [[-4, 5], [-2, 3], [0, 1], [2, -1], [4, -3]] },
        { name: 'm = 0 (horizontal)', type: 'line', smooth: false, symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[-4, -2], [0, -2], [4, -2]] }
      ],
      tooltip: { trigger: 'item' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### El intercepto (b)

El **intercepto** $b$ es el valor de $y$ cuando $x = 0$. Es el punto donde la recta cruza el eje $y$.

| Valor de $b$ | Significado |
|:------------:|:------------|
| $b > 0$ | Cruza el eje $y$ arriba del origen |
| $b < 0$ | Cruza el eje $y$ abajo del origen |
| $b = 0$ | Pasa por el origen |

---

## 📖 Caso especial: Función constante

Cuando $m = 0$, la función se convierte en:

$$
f(x) = b
$$

Esta es una **función constante**. Sin importar el valor de $x$, $y$ siempre es igual a $b$.

### Ejemplo 4

$$
f(x) = 5
$$

Para cualquier valor de $x$, $f(x) = 5$. La gráfica es una línea horizontal que pasa por $y = 5$.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-constante" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-constante')) {
    var chart = echarts.init(document.getElementById('echarts-constante'));
    var option = {
      title: { text: 'Función constante: f(x) = 5', subtext: 'Para cualquier valor de x, f(x) = 5', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' }, subtextStyle: { fontSize: 12, color: '#22c55e' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '18%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'end', min: -5, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'f(x)', nameLocation: 'end', min: 0, max: 8, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { name: 'f(x) = 5', type: 'line', smooth: false, symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[-4.5, 5], [0, 5], [4.5, 5]] },
        { name: 'Puntos', type: 'scatter', symbolSize: 14, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return '(' + p.data[0] + ', 5)'; }, position: 'top', fontSize: 10 }, data: [[-3, 5], [0, 5], [3, 5]] }
      ],
      tooltip: { trigger: 'item' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Evaluando funciones lineales

Para evaluar una función, sustituimos el valor de $x$ en la expresión.

### Ejemplo 5

Si $f(x) = 3x - 2$, encontrar $f(4)$.

$$
f(4) = 3(4) - 2 = 12 - 2 = 10
$$

$$
\boxed{f(4) = 10}
$$

---

### Ejemplo 6

Si $f(x) = -2x + 7$, encontrar $f(-3)$.

$$
f(-3) = -2(-3) + 7 = 6 + 7 = 13
$$

$$
\boxed{f(-3) = 13}
$$

---

## 📋 Resumen

| Elemento | Símbolo | Significado |
|:---------|:-------:|:------------|
| Pendiente | $m$ | Inclinación de la recta |
| Intercepto | $b$ | Punto donde cruza el eje $y$ |
| Forma general | $y = mx + b$ | Ecuación de la recta |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Si $f(x) = 4x + 1$, calcula $f(3)$.

<details>
<summary>Ver solución</summary>

$$
f(3) = 4(3) + 1 = 13
$$

</details>

---

**Ejercicio 2:** Si $f(x) = -x + 5$, calcula $f(-2)$.

<details>
<summary>Ver solución</summary>

$$
f(-2) = -(-2) + 5 = 2 + 5 = 7
$$

</details>

---

**Ejercicio 3:** Identifica la pendiente y el intercepto de $f(x) = 2x - 3$.

<details>
<summary>Ver solución</summary>

$m = 2$ (pendiente), $b = -3$ (intercepto)

</details>

---

**Ejercicio 4:** Un plan de celular cobra 20 pesos fijos más 0.10 pesos por minuto. Escribe la función de costo.

<details>
<summary>Ver solución</summary>

$$
f(x) = 0.10x + 20
$$

</details>

---

**Ejercicio 5:** Si la pendiente es $0$, ¿qué tipo de recta es?

<details>
<summary>Ver solución</summary>

Es una recta horizontal (función constante).

</details>

---

**Ejercicio 6:** ¿La función $f(x) = 3x - 1$ es ascendente o descendente?

<details>
<summary>Ver solución</summary>

Ascendente, porque $m = 3 > 0$.

</details>

---
