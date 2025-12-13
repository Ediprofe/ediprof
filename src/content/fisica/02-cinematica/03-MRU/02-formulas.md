# 📐 **Fórmulas del Movimiento Rectilíneo Uniforme (MRU)**

Para describir matemáticamente el movimiento de manera sencilla y progresiva, usaremos la letra **$x$** para representar el **Desplazamiento**.

### **1. El Caso Simple (Partiendo de Cero)**

Imaginemos la situación más común: encendemos el cronómetro justo cuando el objeto arranca desde el punto de inicio ($0$).

En este caso, el **desplazamiento ($x$)** es simplemente la multiplicación de la velocidad por el tiempo.

#### **A. Para calcular el Desplazamiento ($x$)**
$$
x = v \cdot t
$$

#### **B. Para calcular la Velocidad ($v$)**
$$
v = \frac{x}{t}
$$

#### **C. Para calcular el Tiempo ($t$)**
$$
t = \frac{x}{v}
$$

> **Nota:** Estas fórmulas asumen que el objeto parte desde el origen ($0$).

---

### **2. El Caso General (Con Posición Inicial)**

En la realidad, no siempre empezamos a contar desde cero. A veces el objeto ya se encuentra en una **Posición Inicial ($x_i$)** y termina en una **Posición Final ($x_f$)**.

Aquí debemos ser más precisos: el **Desplazamiento** ya no es solo $x$, sino la diferencia entre dónde terminas y dónde empezaste. A esto lo llamamos **Delta x ($\Delta x$)**.

$$
\Delta x = x_f - x_i
$$

Sustituyendo esto en nuestras fórmulas, la ecuación de la posición evoluciona así:

$$
x_f = x_i + v \cdot t
$$

**Donde:**
* $x_f$: **Posición Final** (Ubicación de llegada).
* $x_i$: **Posición Inicial** (Ubicación de partida).
* $v \cdot t$: **Desplazamiento** (Lo que recorrió).

**Para hallar el tiempo en este caso:**
Primero calculamos cuánto se desplazó realmente ($\Delta x$) y dividimos por la velocidad.

$$
t = \frac{x_f - x_i}{v}
$$

---

## ⚙️ **Ejercicio 1 — Caso Simple (Hallar Velocidad)**

Un atleta corre un desplazamiento de $100\,\mathrm{m}$ partiendo desde la línea de salida. Si tarda $10\,\mathrm{s}$ en llegar a la meta, ¿cuál fue su velocidad?

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-atleta" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-atleta')) {
    var chart = echarts.init(document.getElementById('echarts-atleta'));
    var option = {
      title: { text: 'Atleta: x = 100m, t = 10s → v = ?', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 11, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Posición (m)', nameLocation: 'middle', nameGap: 50, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 110, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 12, lineStyle: { width: 3, color: '#3b82f6' }, areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: 'rgba(59, 130, 246, 0.3)' }, { offset: 1, color: 'rgba(59, 130, 246, 0.05)' }] } }, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return p.data[1] + 'm'; }, position: 'top', fontSize: 11, fontWeight: 'bold' }, data: [[0, 0], [5, 50], [10, 100]] }
      ],
      tooltip: { trigger: 'axis' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

### **✅ Solución**

| Dato | Valor |
|------|-------|
| $x$ | $100\,\mathrm{m}$ |
| $t$ | $10\,\mathrm{s}$ |

$$
v = \frac{x}{t} = \frac{100\,\mathrm{m}}{10\,\mathrm{s}} = \boxed{10\,\mathrm{m/s}}
$$

---

## ⚙️ **Ejercicio 2 — Caso Simple (Hallar Desplazamiento)**

El sonido viaja a una velocidad constante de $340\,\mathrm{m/s}$. Si un trueno se escucha $3\,\mathrm{s}$ después del relámpago, ¿cuál fue el desplazamiento ($x$) del sonido?

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-trueno" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-trueno')) {
    var chart = echarts.init(document.getElementById('echarts-trueno'));
    var option = {
      title: { text: 'Sonido del trueno: v = 340 m/s, t = 3s → x = ?', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 3.5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Posición (m)', nameLocation: 'middle', nameGap: 55, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 1100, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 12, lineStyle: { width: 3, color: '#f59e0b' }, areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: 'rgba(245, 158, 11, 0.3)' }, { offset: 1, color: 'rgba(245, 158, 11, 0.05)' }] } }, itemStyle: { color: '#f59e0b', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return p.data[1] + 'm'; }, position: 'top', fontSize: 11, fontWeight: 'bold' }, data: [[0, 0], [1, 340], [2, 680], [3, 1020]] }
      ],
      tooltip: { trigger: 'axis' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

### **✅ Solución**

| Dato | Valor |
|------|-------|
| $v$ | $340\,\mathrm{m/s}$ |
| $t$ | $3\,\mathrm{s}$ |

$$
x = v \cdot t = 340\,\mathrm{m/s} \times 3\,\mathrm{s} = \boxed{1020\,\mathrm{m}}
$$

---

## ⚙️ **Ejercicio 3 — Caso General (Hallar Posición Final)**

Un ciclista se encuentra en el **Kilómetro 10** ($x_i = 10\,\mathrm{km}$). Continúa a $20\,\mathrm{km/h}$ durante **2 horas**. ¿En qué kilómetro estará?

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-ciclista" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ciclista')) {
    var chart = echarts.init(document.getElementById('echarts-ciclista'));
    var option = {
      title: { text: 'Ciclista: xᵢ = 10km, v = 20 km/h, t = 2h → xf = ?', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (h)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 2.5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Posición (km)', nameLocation: 'middle', nameGap: 45, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 55, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 12, lineStyle: { width: 3, color: '#22c55e' }, areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: 'rgba(34, 197, 94, 0.3)' }, { offset: 1, color: 'rgba(34, 197, 94, 0.05)' }] } }, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, data: [[0, 10], [1, 30], [2, 50]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#f59e0b', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'xᵢ = 10 km', position: 'left', fontSize: 11, fontWeight: 'bold', color: '#f59e0b' }, data: [[0, 10]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'xf = 50 km', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#22c55e' }, data: [[2, 50]] }
      ],
      tooltip: { trigger: 'axis' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

### **✅ Solución**

| Dato | Valor |
|------|-------|
| $x_i$ | $10\,\mathrm{km}$ |
| $v$ | $20\,\mathrm{km/h}$ |
| $t$ | $2\,\mathrm{h}$ |

$$
x_f = x_i + v \cdot t = 10 + (20 \times 2) = 10 + 40 = \boxed{50\,\mathrm{km}}
$$

---

## ⚙️ **Ejercicio 4 — Caso General (Hallar Tiempo)**

Un tren sale de **Ciudad A** ($x_i = 200\,\mathrm{km}$) hacia **Ciudad B** ($x_f = 500\,\mathrm{km}$) a $100\,\mathrm{km/h}$. ¿Cuánto tiempo tardará?

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-tren" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-tren')) {
    var chart = echarts.init(document.getElementById('echarts-tren'));
    var option = {
      title: { text: 'Tren: Δx = 300km, v = 100 km/h → t = ?', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '15%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (h)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 3.5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Posición (km)', nameLocation: 'middle', nameGap: 50, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 550, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 12, lineStyle: { width: 3, color: '#a855f7' }, areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: 'rgba(168, 85, 247, 0.3)' }, { offset: 1, color: 'rgba(168, 85, 247, 0.05)' }] } }, itemStyle: { color: '#a855f7', borderColor: '#fff', borderWidth: 2 }, data: [[0, 200], [1, 300], [2, 400], [3, 500]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#f59e0b', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Ciudad A (200km)', position: 'left', fontSize: 10, fontWeight: 'bold', color: '#f59e0b' }, data: [[0, 200]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Ciudad B (500km)', position: 'top', fontSize: 10, fontWeight: 'bold', color: '#22c55e' }, data: [[3, 500]] }
      ],
      tooltip: { trigger: 'axis' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

### **✅ Solución**

| Dato | Valor |
|------|-------|
| $x_i$ | $200\,\mathrm{km}$ |
| $x_f$ | $500\,\mathrm{km}$ |
| $v$ | $100\,\mathrm{km/h}$ |

**Paso 1:** Calcular desplazamiento
$$\Delta x = x_f - x_i = 500 - 200 = 300\,\mathrm{km}$$

**Paso 2:** Calcular tiempo
$$t = \frac{\Delta x}{v} = \frac{300\,\mathrm{km}}{100\,\mathrm{km/h}} = \boxed{3\,\mathrm{h}}$$