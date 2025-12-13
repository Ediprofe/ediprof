# 🚗 **MRU: Introducción**

El **Movimiento Rectilíneo Uniforme (MRU)** es el modelo de movimiento más fundamental en la física. Se caracteriza por cumplir estrictamente dos condiciones:

1.  **Trayectoria Rectilínea:** El objeto se desplaza en línea recta, sin cambiar su dirección.
2.  **Velocidad Constante:** El objeto mantiene siempre la misma rapidez y dirección. Esto implica que la aceleración es nula ($a=0$).

> 💡 **Principio Fundamental:**
> En el MRU, el objeto recorre **distancias iguales en tiempos iguales**.
> Una velocidad de $10\,\mathrm{m/s}$ significa físicamente que **por cada segundo que transcurre, el cuerpo avanza exactamente 10 metros**.

---

## ⚙️ **Ejercicio 1 — Análisis por definición**

Un robot de juguete se mueve en línea recta con una velocidad constante de $4\,\mathrm{m/s}$. Si parte desde la posición cero, determinar su posición final después de $3\,\mathrm{s}$.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-robot" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-robot')) {
    var chart = echarts.init(document.getElementById('echarts-robot'));
    
    var option = {
      title: {
        text: 'Posición del robot vs Tiempo',
        left: 'center',
        textStyle: { fontSize: 16, fontWeight: 'bold', color: '#1e293b' }
      },
      animation: true,
      animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '12%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: {
        type: 'value',
        name: 'Tiempo (s)',
        nameLocation: 'middle',
        nameGap: 30,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: 0, max: 3.5,
        axisLine: { lineStyle: { color: '#64748b' } },
        splitLine: { show: true, lineStyle: { type: 'solid', color: '#94a3b8', width: 1 } }
      },
      yAxis: {
        type: 'value',
        name: 'Posición (m)',
        nameLocation: 'middle',
        nameGap: 45,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: 0, max: 14,
        axisLine: { lineStyle: { color: '#64748b' } },
        splitLine: { show: true, lineStyle: { type: 'solid', color: '#94a3b8', width: 1 } }
      },
      series: [
        {
          name: 'Posición',
          type: 'line',
          smooth: false,
          symbol: 'circle',
          symbolSize: 12,
          lineStyle: { width: 3, color: '#3b82f6' },
          areaStyle: {
            color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
              colorStops: [{ offset: 0, color: 'rgba(59, 130, 246, 0.3)' }, { offset: 1, color: 'rgba(59, 130, 246, 0.05)' }]
            }
          },
          itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 },
          label: { show: true, formatter: function(p) { return p.data[1] + ' m'; }, position: 'top', fontSize: 11, fontWeight: 'bold' },
          data: [[0, 0], [1, 4], [2, 8], [3, 12]]
        }
      ],
      tooltip: { trigger: 'axis', formatter: 't = {b} s<br/>x = {c} m' }
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 El gráfico muestra cómo el robot avanza **exactamente 4 metros cada segundo** (distancias iguales en tiempos iguales).

### **✅ Solución**

El dato $v = 4\,\mathrm{m/s}$ indica que el robot avanza **4 metros cada segundo**.

| Tiempo | Avance | Posición |
|--------|--------|----------|
| $t=0\,\mathrm{s}$ | — | $0\,\mathrm{m}$ |
| $t=1\,\mathrm{s}$ | $+4\,\mathrm{m}$ | $4\,\mathrm{m}$ |
| $t=2\,\mathrm{s}$ | $+4\,\mathrm{m}$ | $8\,\mathrm{m}$ |
| $t=3\,\mathrm{s}$ | $+4\,\mathrm{m}$ | $12\,\mathrm{m}$ |

**Cálculo directo:**

$$
d = v \cdot t = 4\,\mathrm{m/s} \times 3\,\mathrm{s} = 12\,\mathrm{m}
$$

---

## ⚙️ **Ejercicio 2 — Deducción de parámetros**

Un corredor de larga distancia entrena manteniendo un ritmo constante. Se observa que recorre $20\,\mathrm{m}$ cada $4\,\mathrm{s}$.

1.  ¿Cuál es su velocidad constante?
2.  Si mantiene ese mismo ritmo, ¿qué distancia recorrerá en $10\,\mathrm{s}$?

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-corredor" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-corredor')) {
    var chart = echarts.init(document.getElementById('echarts-corredor'));
    
    var option = {
      title: {
        text: 'Posición del corredor vs Tiempo',
        left: 'center',
        textStyle: { fontSize: 16, fontWeight: 'bold', color: '#1e293b' }
      },
      animation: true,
      animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '12%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: {
        type: 'value',
        name: 'Tiempo (s)',
        nameLocation: 'middle',
        nameGap: 30,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: 0, max: 11,
        axisLine: { lineStyle: { color: '#64748b' } },
        splitLine: { show: true, lineStyle: { type: 'solid', color: '#94a3b8', width: 1 } }
      },
      yAxis: {
        type: 'value',
        name: 'Posición (m)',
        nameLocation: 'middle',
        nameGap: 45,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: 0, max: 55,
        axisLine: { lineStyle: { color: '#64748b' } },
        splitLine: { show: true, lineStyle: { type: 'solid', color: '#94a3b8', width: 1 } }
      },
      series: [
        {
          name: 'Posición',
          type: 'line',
          smooth: false,
          symbol: 'circle',
          symbolSize: 10,
          lineStyle: { width: 3, color: '#3b82f6' },
          areaStyle: {
            color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
              colorStops: [{ offset: 0, color: 'rgba(59, 130, 246, 0.25)' }, { offset: 1, color: 'rgba(59, 130, 246, 0.02)' }]
            }
          },
          itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 },
          data: [[0, 0], [2, 10], [4, 20], [6, 30], [8, 40], [10, 50]]
        },
        {
          name: 'Dato (4s, 20m)',
          type: 'scatter',
          symbolSize: 16,
          itemStyle: { color: '#f59e0b', borderColor: '#fff', borderWidth: 2 },
          label: { show: true, formatter: 'Dato: 20m en 4s', position: 'right', fontSize: 11, fontWeight: 'bold', color: '#f59e0b' },
          data: [[4, 20]]
        },
        {
          name: 'Resultado',
          type: 'scatter',
          symbolSize: 16,
          itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 },
          label: { show: true, formatter: '50m en 10s', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#22c55e' },
          data: [[10, 50]]
        }
      ],
      tooltip: { trigger: 'axis' }
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

### **✅ Solución**

**Paso 1: Calcular la velocidad** (¿cuánto avanza por segundo?)

$$
v = \frac{20\,\mathrm{m}}{4\,\mathrm{s}} = 5\,\mathrm{m/s}
$$

El corredor avanza **5 metros cada segundo**.

**Paso 2: Predecir la distancia en 10 segundos**

$$
d = v \cdot t = 5\,\mathrm{m/s} \times 10\,\mathrm{s} = 50\,\mathrm{m}
$$

> 💡 El gráfico muestra: en 4s recorre 20m (dato), luego en los 6s restantes recorre 30m más → total 50m.