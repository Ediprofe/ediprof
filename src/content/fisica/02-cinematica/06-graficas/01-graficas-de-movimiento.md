# 📈 **Gráficas de Movimiento**

Las gráficas son una herramienta poderosa para **visualizar** y **analizar** el movimiento. En esta lección aprenderás a leerlas como un experto.

---

## 🎯 **Las Tres Gráficas Fundamentales**

| Gráfica | Eje vertical | ¿Qué muestra? |
|---------|-------------|---------------|
| **x vs t** | Posición (m) | Dónde está el objeto |
| **v vs t** | Velocidad (m/s) | Qué tan rápido y hacia dónde |
| **a vs t** | Aceleración (m/s²) | Cómo cambia la velocidad |

### **Relaciones clave**

| Relación | Significado |
|----------|-------------|
| Pendiente de **x-t** | = **velocidad** |
| Pendiente de **v-t** | = **aceleración** |
| Área bajo **v-t** | = **desplazamiento** |

---

## 📊 **Gráficas por Tipo de Movimiento**

### **1. Reposo (Objeto quieto)**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-reposo" style="width: 100%; height: 200px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-reposo')) {
    var chart = echarts.init(document.getElementById('echarts-reposo'));
    var option = {
      title: { text: 'Reposo', left: 'center', textStyle: { fontSize: 13, color: '#1e293b' } },
      grid: [
        { left: '8%', right: '68%', top: '25%', bottom: '20%' },
        { left: '38%', right: '38%', top: '25%', bottom: '20%' },
        { left: '68%', right: '8%', top: '25%', bottom: '20%' }
      ],
      xAxis: [
        { gridIndex: 0, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 }, nameTextStyle: { fontSize: 10 } },
        { gridIndex: 1, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 }, nameTextStyle: { fontSize: 10 } },
        { gridIndex: 2, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 }, nameTextStyle: { fontSize: 10 } }
      ],
      yAxis: [
        { gridIndex: 0, type: 'value', name: 'x', min: 0, max: 8, axisLabel: { fontSize: 9 }, nameTextStyle: { fontSize: 10 } },
        { gridIndex: 1, type: 'value', name: 'v', min: -2, max: 4, axisLabel: { fontSize: 9 }, nameTextStyle: { fontSize: 10 } },
        { gridIndex: 2, type: 'value', name: 'a', min: -2, max: 2, axisLabel: { fontSize: 9 }, nameTextStyle: { fontSize: 10 } }
      ],
      series: [
        { type: 'line', xAxisIndex: 0, yAxisIndex: 0, data: [[0, 4], [4, 4]], lineStyle: { width: 3, color: '#3b82f6' }, symbol: 'none' },
        { type: 'line', xAxisIndex: 1, yAxisIndex: 1, data: [[0, 0], [4, 0]], lineStyle: { width: 3, color: '#22c55e' }, symbol: 'none' },
        { type: 'line', xAxisIndex: 2, yAxisIndex: 2, data: [[0, 0], [4, 0]], lineStyle: { width: 3, color: '#ef4444' }, symbol: 'none' }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

**Características:** x = constante, v = 0, a = 0

---

### **2. MRU hacia adelante (v > 0)**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-mru-adelante" style="width: 100%; height: 200px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-mru-adelante')) {
    var chart = echarts.init(document.getElementById('echarts-mru-adelante'));
    var option = {
      title: { text: 'MRU hacia adelante (v > 0)', left: 'center', textStyle: { fontSize: 13, color: '#1e293b' } },
      grid: [
        { left: '8%', right: '68%', top: '25%', bottom: '20%' },
        { left: '38%', right: '38%', top: '25%', bottom: '20%' },
        { left: '68%', right: '8%', top: '25%', bottom: '20%' }
      ],
      xAxis: [
        { gridIndex: 0, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 } },
        { gridIndex: 1, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 } },
        { gridIndex: 2, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 } }
      ],
      yAxis: [
        { gridIndex: 0, type: 'value', name: 'x', min: 0, max: 16, axisLabel: { fontSize: 9 } },
        { gridIndex: 1, type: 'value', name: 'v', min: 0, max: 6, axisLabel: { fontSize: 9 } },
        { gridIndex: 2, type: 'value', name: 'a', min: -2, max: 2, axisLabel: { fontSize: 9 } }
      ],
      series: [
        { type: 'line', xAxisIndex: 0, yAxisIndex: 0, data: [[0, 0], [1, 4], [2, 8], [3, 12], [4, 16]], lineStyle: { width: 3, color: '#3b82f6' }, symbol: 'none' },
        { type: 'line', xAxisIndex: 1, yAxisIndex: 1, data: [[0, 4], [4, 4]], lineStyle: { width: 3, color: '#22c55e' }, symbol: 'none' },
        { type: 'line', xAxisIndex: 2, yAxisIndex: 2, data: [[0, 0], [4, 0]], lineStyle: { width: 3, color: '#ef4444' }, symbol: 'none' }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

**Características:** x crece linealmente (recta ↗), v = constante positiva, a = 0

---

### **3. MRU hacia atrás (v < 0)**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-mru-atras" style="width: 100%; height: 200px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-mru-atras')) {
    var chart = echarts.init(document.getElementById('echarts-mru-atras'));
    var option = {
      title: { text: 'MRU hacia atrás (v < 0)', left: 'center', textStyle: { fontSize: 13, color: '#1e293b' } },
      grid: [
        { left: '8%', right: '68%', top: '25%', bottom: '20%' },
        { left: '38%', right: '38%', top: '25%', bottom: '20%' },
        { left: '68%', right: '8%', top: '25%', bottom: '20%' }
      ],
      xAxis: [
        { gridIndex: 0, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 } },
        { gridIndex: 1, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 } },
        { gridIndex: 2, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 } }
      ],
      yAxis: [
        { gridIndex: 0, type: 'value', name: 'x', min: 0, max: 16, axisLabel: { fontSize: 9 } },
        { gridIndex: 1, type: 'value', name: 'v', min: -6, max: 2, axisLabel: { fontSize: 9 } },
        { gridIndex: 2, type: 'value', name: 'a', min: -2, max: 2, axisLabel: { fontSize: 9 } }
      ],
      series: [
        { type: 'line', xAxisIndex: 0, yAxisIndex: 0, data: [[0, 16], [1, 12], [2, 8], [3, 4], [4, 0]], lineStyle: { width: 3, color: '#3b82f6' }, symbol: 'none' },
        { type: 'line', xAxisIndex: 1, yAxisIndex: 1, data: [[0, -4], [4, -4]], lineStyle: { width: 3, color: '#22c55e' }, symbol: 'none' },
        { type: 'line', xAxisIndex: 2, yAxisIndex: 2, data: [[0, 0], [4, 0]], lineStyle: { width: 3, color: '#ef4444' }, symbol: 'none' }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

**Características:** x decrece linealmente (recta ↘), v = constante negativa, a = 0

---

### **4. MRUA — Acelerando (a > 0)**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-mrua-acelera" style="width: 100%; height: 200px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-mrua-acelera')) {
    var chart = echarts.init(document.getElementById('echarts-mrua-acelera'));
    var option = {
      title: { text: 'MRUA — Acelerando (a > 0)', left: 'center', textStyle: { fontSize: 13, color: '#1e293b' } },
      grid: [
        { left: '8%', right: '68%', top: '25%', bottom: '20%' },
        { left: '38%', right: '38%', top: '25%', bottom: '20%' },
        { left: '68%', right: '8%', top: '25%', bottom: '20%' }
      ],
      xAxis: [
        { gridIndex: 0, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 } },
        { gridIndex: 1, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 } },
        { gridIndex: 2, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 } }
      ],
      yAxis: [
        { gridIndex: 0, type: 'value', name: 'x', min: 0, max: 18, axisLabel: { fontSize: 9 } },
        { gridIndex: 1, type: 'value', name: 'v', min: 0, max: 10, axisLabel: { fontSize: 9 } },
        { gridIndex: 2, type: 'value', name: 'a', min: 0, max: 4, axisLabel: { fontSize: 9 } }
      ],
      series: [
        { type: 'line', xAxisIndex: 0, yAxisIndex: 0, data: [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16]], lineStyle: { width: 3, color: '#3b82f6' }, symbol: 'none', smooth: true },
        { type: 'line', xAxisIndex: 1, yAxisIndex: 1, data: [[0, 0], [1, 2], [2, 4], [3, 6], [4, 8]], lineStyle: { width: 3, color: '#22c55e' }, symbol: 'none' },
        { type: 'line', xAxisIndex: 2, yAxisIndex: 2, data: [[0, 2], [4, 2]], lineStyle: { width: 3, color: '#ef4444' }, symbol: 'none' }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

**Características:** x es parábola (crece cada vez más), v crece linealmente, a = constante positiva

---

### **5. MRUA — Frenando (a < 0)**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-mrua-frena" style="width: 100%; height: 200px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-mrua-frena')) {
    var chart = echarts.init(document.getElementById('echarts-mrua-frena'));
    var option = {
      title: { text: 'MRUA — Frenando (a < 0)', left: 'center', textStyle: { fontSize: 13, color: '#1e293b' } },
      grid: [
        { left: '8%', right: '68%', top: '25%', bottom: '20%' },
        { left: '38%', right: '38%', top: '25%', bottom: '20%' },
        { left: '68%', right: '8%', top: '25%', bottom: '20%' }
      ],
      xAxis: [
        { gridIndex: 0, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 } },
        { gridIndex: 1, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 } },
        { gridIndex: 2, type: 'value', name: 't', min: 0, max: 4, axisLabel: { fontSize: 9 } }
      ],
      yAxis: [
        { gridIndex: 0, type: 'value', name: 'x', min: 0, max: 35, axisLabel: { fontSize: 9 } },
        { gridIndex: 1, type: 'value', name: 'v', min: 0, max: 10, axisLabel: { fontSize: 9 } },
        { gridIndex: 2, type: 'value', name: 'a', min: -4, max: 1, axisLabel: { fontSize: 9 } }
      ],
      series: [
        { type: 'line', xAxisIndex: 0, yAxisIndex: 0, data: [[0, 0], [1, 7], [2, 12], [3, 15], [4, 16]], lineStyle: { width: 3, color: '#3b82f6' }, symbol: 'none', smooth: true },
        { type: 'line', xAxisIndex: 1, yAxisIndex: 1, data: [[0, 8], [1, 6], [2, 4], [3, 2], [4, 0]], lineStyle: { width: 3, color: '#22c55e' }, symbol: 'none' },
        { type: 'line', xAxisIndex: 2, yAxisIndex: 2, data: [[0, -2], [4, -2]], lineStyle: { width: 3, color: '#ef4444' }, symbol: 'none' }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

**Características:** x es parábola (crece cada vez menos hasta detenerse), v decrece linealmente hasta 0, a = constante negativa

---

## 📋 **Tabla Maestra: Resumen de Gráficas**

| Tipo de movimiento | x vs t | v vs t | a vs t |
|--------------------|--------|--------|--------|
| **Reposo** | Horizontal | En cero | En cero |
| **MRU adelante** | Recta ↗ | Horizontal positiva | En cero |
| **MRU atrás** | Recta ↘ | Horizontal negativa | En cero |
| **MRUA acelera** | Parábola ⌒ | Recta ↗ | Horizontal positiva |
| **MRUA frena** | Parábola ⌒ aplana | Recta ↘ | Horizontal negativa |

---

## 📝 **Ejercicios Resueltos con Contexto**

### **Ejercicio 1 — El ciclista en la ciudad**

Un ciclista recorre una avenida. Su gráfica x-t se muestra abajo. Describe su movimiento en cada tramo.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ej1" style="width: 100%; height: 250px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ej1')) {
    var chart = echarts.init(document.getElementById('echarts-ej1'));
    var option = {
      title: { text: 'Ejercicio 1: El ciclista', left: 'center', textStyle: { fontSize: 13 } },
      grid: { left: '15%', right: '8%', top: '15%', bottom: '20%', show: true, borderColor: '#94a3b8', borderWidth: 1 },
      xAxis: { type: 'value', name: 't (min)', min: 0, max: 20, nameLocation: 'middle', nameGap: 28, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, axisLine: { lineStyle: { color: '#475569', width: 1 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'x (km)', min: 0, max: 12, nameLocation: 'middle', nameGap: 40, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, axisLine: { lineStyle: { color: '#475569', width: 1 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [{ type: 'line', data: [[0, 0], [5, 5], [10, 5], [15, 10], [20, 10]], lineStyle: { width: 3, color: '#3b82f6' }, symbol: 'circle', symbolSize: 8 }]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

<details>
<summary><strong>Ver solución</strong></summary>

| Tramo | Tiempo | Forma | Interpretación |
|-------|--------|-------|----------------|
| **A** | 0-5 min | Recta ↗ | MRU hacia adelante (v = 1 km/min) |
| **B** | 5-10 min | Horizontal | Reposo (semáforo o descanso) |
| **C** | 10-15 min | Recta ↗ | MRU hacia adelante (v = 1 km/min) |
| **D** | 15-20 min | Horizontal | Reposo (llegó al destino) |

</details>

---

### **Ejercicio 2 — La carrera de autos**

Dos autos parten del mismo lugar. Observa sus gráficas v-t y responde: ¿Cuál recorrió más distancia en 4 segundos?

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ej2" style="width: 100%; height: 250px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ej2')) {
    var chart = echarts.init(document.getElementById('echarts-ej2'));
    var option = {
      title: { text: 'Ejercicio 2: Carrera de autos', left: 'center', textStyle: { fontSize: 13 } },
      legend: { data: ['Auto A', 'Auto B'], top: 25 },
      grid: { left: '15%', right: '8%', top: '22%', bottom: '20%', show: true, borderColor: '#94a3b8', borderWidth: 1 },
      xAxis: { type: 'value', name: 't (s)', min: 0, max: 4, nameLocation: 'middle', nameGap: 28, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, axisLine: { lineStyle: { color: '#475569', width: 1 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'v (m/s)', min: 0, max: 16, nameLocation: 'middle', nameGap: 40, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, axisLine: { lineStyle: { color: '#475569', width: 1 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'Auto A', type: 'line', data: [[0, 8], [4, 8]], lineStyle: { width: 3, color: '#3b82f6' }, areaStyle: { color: 'rgba(59, 130, 246, 0.2)' } },
        { name: 'Auto B', type: 'line', data: [[0, 0], [4, 16]], lineStyle: { width: 3, color: '#ef4444' }, areaStyle: { color: 'rgba(239, 68, 68, 0.2)' } }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

<details>
<summary><strong>Ver solución</strong></summary>

El **área bajo v-t** = desplazamiento:

- **Auto A:** Área = 8 × 4 = **32 m** (rectángulo)
- **Auto B:** Área = ½ × 16 × 4 = **32 m** (triángulo)

**¡Ambos recorrieron la misma distancia!** Aunque B aceleró y A fue constante.

</details>

---

### **Ejercicio 3 — El tren que frena**

Un tren viaja a 20 m/s y frena uniformemente hasta detenerse en 10 segundos. Calcula la aceleración y la distancia de frenado.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ej3" style="width: 100%; height: 250px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ej3')) {
    var chart = echarts.init(document.getElementById('echarts-ej3'));
    var option = {
      title: { text: 'Ejercicio 3: Tren frenando', left: 'center', textStyle: { fontSize: 13 } },
      grid: { left: '15%', right: '8%', top: '15%', bottom: '20%', show: true, borderColor: '#94a3b8', borderWidth: 1 },
      xAxis: { type: 'value', name: 't (s)', min: 0, max: 10, nameLocation: 'middle', nameGap: 28, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, axisLine: { lineStyle: { color: '#475569', width: 1 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'v (m/s)', min: 0, max: 25, nameLocation: 'middle', nameGap: 40, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, axisLine: { lineStyle: { color: '#475569', width: 1 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [{ type: 'line', data: [[0, 20], [10, 0]], lineStyle: { width: 3, color: '#22c55e' }, areaStyle: { color: 'rgba(34, 197, 94, 0.2)' } }]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

<details>
<summary><strong>Ver solución</strong></summary>

**Aceleración** (pendiente de v-t):
$$
a = \frac{\Delta v}{\Delta t} = \frac{0 - 20}{10 - 0} = -2\,\mathrm{m/s^2}
$$

**Distancia** (área bajo v-t):
$$
d = \frac{1}{2} \times 20 \times 10 = 100\,\mathrm{m}
$$

</details>

---

### **Ejercicio 4 — La pelota que rebota**

Una pelota se lanza hacia arriba y cae. Observa su gráfica v-t. ¿En qué instante alcanzó la altura máxima?

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ej4" style="width: 100%; height: 250px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ej4')) {
    var chart = echarts.init(document.getElementById('echarts-ej4'));
    var option = {
      title: { text: 'Ejercicio 4: Pelota lanzada', left: 'center', textStyle: { fontSize: 13 } },
      grid: { left: '18%', right: '8%', top: '15%', bottom: '20%', show: true, borderColor: '#94a3b8', borderWidth: 1 },
      xAxis: { type: 'value', name: 't (s)', min: 0, max: 4, nameLocation: 'middle', nameGap: 28, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, axisLine: { lineStyle: { color: '#475569', width: 1 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'v (m/s)', min: -25, max: 25, nameLocation: 'middle', nameGap: 50, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, axisLine: { lineStyle: { color: '#475569', width: 1 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [{ type: 'line', data: [[0, 20], [1, 10], [2, 0], [3, -10], [4, -20]], lineStyle: { width: 3, color: '#a855f7' }, symbol: 'circle', symbolSize: 8 }]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

<details>
<summary><strong>Ver solución</strong></summary>

La altura máxima se alcanza cuando **v = 0**.

Observando la gráfica: v = 0 en **t = 2 s**.

En ese instante la pelota alcanzó la altura máxima y comenzó a caer (v se vuelve negativa).

</details>

---

### **Ejercicio 5 — Comparación de movimientos**

Tres objetos tienen las siguientes gráficas x-t. ¿Cuál tiene mayor velocidad?

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ej5" style="width: 100%; height: 250px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ej5')) {
    var chart = echarts.init(document.getElementById('echarts-ej5'));
    var option = {
      title: { text: 'Ejercicio 5: Comparación', left: 'center', textStyle: { fontSize: 13 } },
      legend: { data: ['Objeto A', 'Objeto B', 'Objeto C'], top: 25 },
      grid: { left: '15%', right: '8%', top: '22%', bottom: '20%', show: true, borderColor: '#94a3b8', borderWidth: 1 },
      xAxis: { type: 'value', name: 't (s)', min: 0, max: 4, nameLocation: 'middle', nameGap: 28, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, axisLine: { lineStyle: { color: '#475569', width: 1 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'x (m)', min: 0, max: 25, nameLocation: 'middle', nameGap: 40, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, axisLine: { lineStyle: { color: '#475569', width: 1 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'Objeto A', type: 'line', data: [[0, 0], [4, 8]], lineStyle: { width: 3, color: '#3b82f6' } },
        { name: 'Objeto B', type: 'line', data: [[0, 0], [4, 16]], lineStyle: { width: 3, color: '#22c55e' } },
        { name: 'Objeto C', type: 'line', data: [[0, 0], [4, 24]], lineStyle: { width: 3, color: '#ef4444' } }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

<details>
<summary><strong>Ver solución</strong></summary>

La **velocidad = pendiente** de la gráfica x-t:

| Objeto | Pendiente | Velocidad |
|--------|-----------|-----------|
| A | 8/4 = 2 | **2 m/s** |
| B | 16/4 = 4 | **4 m/s** |
| C | 24/4 = 6 | **6 m/s** |

**El objeto C tiene la mayor velocidad** porque su línea tiene la mayor pendiente.

</details>
