# 📍 Plano Cartesiano

En esta lección estudiaremos el plano cartesiano, el sistema de coordenadas donde representaremos las funciones lineales.

---

## 📖 El sistema de coordenadas cartesianas

El **plano cartesiano** es un sistema formado por dos rectas numéricas perpendiculares:

- **Eje X** (horizontal): también llamado eje de las abscisas
- **Eje Y** (vertical): también llamado eje de las ordenadas
- **Origen**: punto donde se cruzan ambos ejes, con coordenadas $(0, 0)$

En la siguiente visualización puedes ver el plano cartesiano con sus ejes y los cuatro cuadrantes:

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-plano-intro" style="width: 100%; height: 420px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-plano-intro')) {
    var chart = echarts.init(document.getElementById('echarts-plano-intro'));
    var option = {
      title: { text: 'El Plano Cartesiano', left: 'center', textStyle: { fontSize: 16, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '5%', right: '5%', top: '10%', bottom: '8%', show: true, borderColor: '#cbd5e1' },
      xAxis: { 
        type: 'value', 
        min: -6, max: 6, interval: 1, 
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, 
        splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, 
        axisLabel: { show: false },
        axisTick: { show: true, length: 6, alignWithLabel: true }
      },
      yAxis: { 
        type: 'value', 
        min: -6, max: 6, interval: 1, 
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, 
        splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, 
        axisLabel: { show: false },
        axisTick: { show: true, length: 6, alignWithLabel: true }
      },
      series: [
        // Etiquetas del eje X (números a lo largo de y=0)
        { type: 'scatter', symbolSize: 0, label: { show: true, position: 'bottom', fontSize: 10, color: '#374151', formatter: function(p) { return p.data[0] !== 0 ? p.data[0] : ''; } }, data: [[-6,0],[-5,0],[-4,0],[-3,0],[-2,0],[-1,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]] },
        // Etiquetas del eje Y (números a lo largo de x=0)
        { type: 'scatter', symbolSize: 0, label: { show: true, position: 'left', fontSize: 10, color: '#374151', formatter: function(p) { return p.data[1] !== 0 ? p.data[1] : ''; } }, data: [[0,-6],[0,-5],[0,-4],[0,-3],[0,-2],[0,-1],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6]] },
        // Etiqueta "x" al final del eje X
        { type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'x', position: 'right', fontSize: 14, fontWeight: 'bold', color: '#374151' }, data: [[6, 0]] },
        // Etiqueta "y" al final del eje Y
        { type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'y', position: 'top', fontSize: 14, fontWeight: 'bold', color: '#374151' }, data: [[0, 6]] },
        // Origen
        { type: 'scatter', symbolSize: 14, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '0', position: 'bottom', fontSize: 10, color: '#374151', offset: [-8, 0] }, data: [[0, 0]] },
        // Cuadrantes
        { type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'I', fontSize: 28, fontWeight: 'bold', color: '#3b82f6' }, data: [[3, 3]] },
        { type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'II', fontSize: 28, fontWeight: 'bold', color: '#22c55e' }, data: [[-3, 3]] },
        { type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'III', fontSize: 28, fontWeight: 'bold', color: '#f97316' }, data: [[-3, -3]] },
        { type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'IV', fontSize: 28, fontWeight: 'bold', color: '#a855f7' }, data: [[3, -3]] }
      ],
      tooltip: { show: false }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Coordenadas de un punto

Cada punto en el plano se representa con un **par ordenado** $(x, y)$:

- $x$ = coordenada horizontal (abscisa)
- $y$ = coordenada vertical (ordenada)

### Ejemplo 1

El punto $P(3, 4)$ está ubicado:
- $3$ unidades a la derecha del origen
- $4$ unidades hacia arriba

### Ejemplo 2

El punto $Q(-2, 5)$ está ubicado:
- $2$ unidades a la izquierda del origen
- $5$ unidades hacia arriba

### Ejemplo 3

El punto $R(4, -3)$ está ubicado:
- $4$ unidades a la derecha
- $3$ unidades hacia abajo

### Ejemplo 4

El punto $S(-1, -2)$ está ubicado:
- $1$ unidad a la izquierda
- $2$ unidades hacia abajo

En la siguiente gráfica puedes ver los cuatro puntos ubicados en el plano:

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-puntos-ejemplos" style="width: 100%; height: 420px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-puntos-ejemplos')) {
    var chart = echarts.init(document.getElementById('echarts-puntos-ejemplos'));
    var option = {
      title: { text: 'Puntos en el plano cartesiano', left: 'center', textStyle: { fontSize: 16, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '5%', right: '5%', top: '10%', bottom: '8%', show: true, borderColor: '#cbd5e1' },
      xAxis: { 
        type: 'value', min: -5, max: 6, interval: 1, 
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, 
        splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, 
        axisLabel: { show: false },
        axisTick: { show: true, length: 6 }
      },
      yAxis: { 
        type: 'value', min: -5, max: 7, interval: 1, 
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, 
        splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, 
        axisLabel: { show: false },
        axisTick: { show: true, length: 6 }
      },
      series: [
        // Etiquetas eje X (sobre y=0)
        { type: 'scatter', symbolSize: 0, label: { show: true, position: 'bottom', fontSize: 10, color: '#374151', formatter: function(p) { return p.data[0] !== 0 ? p.data[0] : ''; } }, data: [[-5,0],[-4,0],[-3,0],[-2,0],[-1,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]] },
        // Etiquetas eje Y (sobre x=0)
        { type: 'scatter', symbolSize: 0, label: { show: true, position: 'left', fontSize: 10, color: '#374151', formatter: function(p) { return p.data[1] !== 0 ? p.data[1] : ''; } }, data: [[0,-5],[0,-4],[0,-3],[0,-2],[0,-1],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]] },
        // Etiquetas x, y
        { type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'x', position: 'right', fontSize: 14, fontWeight: 'bold', color: '#374151' }, data: [[6, 0]] },
        { type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'y', position: 'top', fontSize: 14, fontWeight: 'bold', color: '#374151' }, data: [[0, 7]] },
        // Origen
        { type: 'scatter', symbolSize: 0, label: { show: true, formatter: '0', position: 'bottom', fontSize: 10, color: '#374151', offset: [-8, 0] }, data: [[0, 0]] },
        // Puntos
        { name: 'P', type: 'scatter', symbolSize: 16, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'P(3, 4)', position: 'right', fontSize: 12, fontWeight: 'bold', color: '#3b82f6' }, data: [[3, 4]] },
        { name: 'Q', type: 'scatter', symbolSize: 16, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Q(-2, 5)', position: 'left', fontSize: 12, fontWeight: 'bold', color: '#22c55e' }, data: [[-2, 5]] },
        { name: 'R', type: 'scatter', symbolSize: 16, itemStyle: { color: '#a855f7', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'R(4, -3)', position: 'right', fontSize: 12, fontWeight: 'bold', color: '#a855f7' }, data: [[4, -3]] },
        { name: 'S', type: 'scatter', symbolSize: 16, itemStyle: { color: '#f97316', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'S(-1, -2)', position: 'left', fontSize: 12, fontWeight: 'bold', color: '#f97316' }, data: [[-1, -2]] }
      ],
      tooltip: { trigger: 'item', formatter: function(p) { return p.seriesName + ': (' + p.data[0] + ', ' + p.data[1] + ')'; } }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Los cuatro cuadrantes

El plano se divide en cuatro regiones llamadas **cuadrantes**:

| Cuadrante | Signos de $(x, y)$ | Ubicación |
|:---------:|:------------------:|:----------|
| I | $(+, +)$ | Superior derecho |
| II | $(-, +)$ | Superior izquierdo |
| III | $(-, -)$ | Inferior izquierdo |
| IV | $(+, -)$ | Inferior derecho |

---

### Ejemplo 5

¿En qué cuadrante está cada punto?

| Punto | Cuadrante |
|:-----:|:---------:|
| $(5, 3)$ | I |
| $(-4, 2)$ | II |
| $(-3, -1)$ | III |
| $(2, -5)$ | IV |

Observa cada punto en su cuadrante correspondiente:

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-cuadrantes" style="width: 100%; height: 420px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-cuadrantes')) {
    var chart = echarts.init(document.getElementById('echarts-cuadrantes'));
    var option = {
      title: { text: 'Identificación de cuadrantes', left: 'center', textStyle: { fontSize: 16, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '5%', right: '5%', top: '10%', bottom: '8%', show: true, borderColor: '#cbd5e1' },
      xAxis: { 
        type: 'value', min: -7, max: 7, interval: 1, 
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, 
        splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, 
        axisLabel: { show: false },
        axisTick: { show: true, length: 6 }
      },
      yAxis: { 
        type: 'value', min: -7, max: 7, interval: 1, 
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, 
        splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, 
        axisLabel: { show: false },
        axisTick: { show: true, length: 6 }
      },
      series: [
        // Etiquetas eje X (sobre y=0)
        { type: 'scatter', symbolSize: 0, label: { show: true, position: 'bottom', fontSize: 9, color: '#374151', formatter: function(p) { return p.data[0] !== 0 ? p.data[0] : ''; } }, data: [[-7,0],[-6,0],[-5,0],[-4,0],[-3,0],[-2,0],[-1,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]] },
        // Etiquetas eje Y (sobre x=0)
        { type: 'scatter', symbolSize: 0, label: { show: true, position: 'left', fontSize: 9, color: '#374151', formatter: function(p) { return p.data[1] !== 0 ? p.data[1] : ''; } }, data: [[0,-7],[0,-6],[0,-5],[0,-4],[0,-3],[0,-2],[0,-1],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]] },
        // Etiquetas x, y
        { type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'x', position: 'right', fontSize: 14, fontWeight: 'bold', color: '#374151' }, data: [[7, 0]] },
        { type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'y', position: 'top', fontSize: 14, fontWeight: 'bold', color: '#374151' }, data: [[0, 7]] },
        // Origen
        { type: 'scatter', symbolSize: 0, label: { show: true, formatter: '0', position: 'bottom', fontSize: 9, color: '#374151', offset: [-8, 0] }, data: [[0, 0]] },
        // Cuadrantes
        { name: 'Cuad. I', type: 'scatter', symbolSize: 16, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(5, 3)\nCuad. I', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#3b82f6' }, data: [[5, 3]] },
        { name: 'Cuad. II', type: 'scatter', symbolSize: 16, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(-4, 2)\nCuad. II', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#22c55e' }, data: [[-4, 2]] },
        { name: 'Cuad. III', type: 'scatter', symbolSize: 16, itemStyle: { color: '#f97316', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(-3, -1)\nCuad. III', position: 'bottom', fontSize: 11, fontWeight: 'bold', color: '#f97316' }, data: [[-3, -1]] },
        { name: 'Cuad. IV', type: 'scatter', symbolSize: 16, itemStyle: { color: '#a855f7', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(2, -5)\nCuad. IV', position: 'bottom', fontSize: 11, fontWeight: 'bold', color: '#a855f7' }, data: [[2, -5]] }
      ],
      tooltip: { trigger: 'item', formatter: function(p) { return p.seriesName + '<br/>(' + p.data[0] + ', ' + p.data[1] + ')'; } }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Puntos sobre los ejes

Los puntos sobre los ejes no pertenecen a ningún cuadrante:

### Sobre el eje X

Si $y = 0$, el punto está **sobre el eje X**.

Ejemplo: $(3, 0)$, $(-5, 0)$, $(0, 0)$

### Sobre el eje Y

Si $x = 0$, el punto está **sobre el eje Y**.

Ejemplo: $(0, 4)$, $(0, -2)$, $(0, 0)$

---

---

## 📋 Resumen

| Concepto | Descripción |
|:---------|:------------|
| Eje X | Eje horizontal (abscisas) |
| Eje Y | Eje vertical (ordenadas) |
| Origen | Punto $(0, 0)$ donde se cruzan los ejes |
| Par ordenado | $(x, y)$ - primero horizontal, luego vertical |
| Cuadrante I | $(+, +)$ superior derecho |
| Cuadrante II | $(-, +)$ superior izquierdo |
| Cuadrante III | $(-, -)$ inferior izquierdo |
| Cuadrante IV | $(+, -)$ inferior derecho |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿En qué cuadrante está el punto $(-5, 7)$?

<details>
<summary>Ver solución</summary>

Cuadrante II ($x$ negativo, $y$ positivo)

</details>

---

**Ejercicio 2:** ¿Cuáles son las coordenadas del origen?

<details>
<summary>Ver solución</summary>

$(0, 0)$

</details>

---

**Ejercicio 3:** Si un punto tiene $y = 0$, ¿sobre qué eje está?

<details>
<summary>Ver solución</summary>

Sobre el eje X.

</details>

---

**Ejercicio 4:** ¿En qué cuadrante está el punto $(4, -2)$?

<details>
<summary>Ver solución</summary>

Cuadrante IV ($x$ positivo, $y$ negativo)

</details>

---

**Ejercicio 5:** ¿El punto $(0, 5)$ pertenece a algún cuadrante?

<details>
<summary>Ver solución</summary>

No, está sobre el eje Y (no pertenece a ningún cuadrante).

</details>

---

**Ejercicio 6:** Indica los signos de $x$ y $y$ en el cuadrante III.

<details>
<summary>Ver solución</summary>

$x$ negativo, $y$ negativo: $(-, -)$

</details>

---

