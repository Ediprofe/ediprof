# 📈 **Gráficas de Movimiento**

Las gráficas son una herramienta poderosa para **visualizar** y **analizar** el movimiento. En esta lección aprenderás a construir e interpretar las gráficas más importantes de la cinemática.

---

## 🎯 **Las Tres Gráficas Fundamentales**

Existen tres tipos de gráficas que describen completamente cualquier movimiento:

| Gráfica | Eje vertical | Eje horizontal | ¿Qué muestra? |
|---------|-------------|----------------|---------------|
| **Posición vs Tiempo** | $x$ (metros) | $t$ (segundos) | Dónde está el objeto en cada instante |
| **Velocidad vs Tiempo** | $v$ (m/s) | $t$ (segundos) | Qué tan rápido se mueve en cada instante |
| **Aceleración vs Tiempo** | $a$ (m/s²) | $t$ (segundos) | Cómo cambia la velocidad en cada instante |

---

## 📊 **Gráfica Posición vs Tiempo (x-t)**

### **Caso 1: Objeto en reposo**

Si el objeto no se mueve, su posición no cambia con el tiempo.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-reposo" style="width: 100%; height: 280px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-reposo')) {
    var chart = echarts.init(document.getElementById('echarts-reposo'));
    var option = {
      title: { text: 'Posición vs Tiempo: Objeto en Reposo', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      animation: true,
      grid: { left: '15%', right: '10%', top: '18%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, min: 0, max: 5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      yAxis: { type: 'value', name: 'Posición (m)', nameLocation: 'middle', nameGap: 40, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, min: 0, max: 10, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      series: [{ type: 'line', data: [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5]], lineStyle: { width: 3, color: '#3b82f6' }, symbol: 'circle', symbolSize: 8, itemStyle: { color: '#3b82f6' } }]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **Interpretación:** Una **línea horizontal** indica que la posición no cambia → **objeto en reposo**.

---

### **Caso 2: MRU (Velocidad Constante)**

El objeto avanza la misma distancia en cada segundo.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> Interactivo: Arrastra el deslizador para cambiar la velocidad
  </div>
  <div id="jsxgraph-mru-grafica" class="jsxgraph-container" style="width: 100%; height: 300px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mru-grafica')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mru-grafica', {
      boundingbox: [-0.5, 25, 6, -3],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: {enabled: false},
      zoom: {enabled: false}
    });
    
    // Deslizador para la velocidad
    var velocidad = board.create('slider', [[0.5, -1.5], [4, -1.5], [1, 4, 8]], {
      name: 'v (m/s)',
      snapWidth: 0.5,
      precision: 1
    });
    
    // Línea de posición vs tiempo
    var linea = board.create('functiongraph', [function(t) {
      return velocidad.Value() * t;
    }, 0, 5], {
      strokeColor: '#3b82f6',
      strokeWidth: 3
    });
    
    // Etiquetas
    board.create('text', [0.2, 23, 'Posición (m)'], {fontSize: 12, strokeColor: '#374151', fixed: true});
    board.create('text', [5.2, -0.5, 'Tiempo (s)'], {fontSize: 12, strokeColor: '#374151', fixed: true});
    
    board.create('text', [3.5, 20, function() {
      return 'Pendiente = v = ' + velocidad.Value().toFixed(1) + ' m/s';
    }], {fontSize: 12, strokeColor: '#3b82f6', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **Interpretación:** Una **línea recta inclinada** indica MRU. La **pendiente** de la recta es igual a la **velocidad**.

$$
\text{Pendiente} = \frac{\Delta x}{\Delta t} = v
$$

---

### **Caso 3: MRUA (Aceleración Constante)**

El objeto avanza cada vez más (o cada vez menos) en cada segundo.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> Interactivo: Cambia la aceleración
  </div>
  <div id="jsxgraph-mrua-grafica" class="jsxgraph-container" style="width: 100%; height: 300px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mrua-grafica')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mrua-grafica', {
      boundingbox: [-0.5, 55, 6, -8],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: {enabled: false},
      zoom: {enabled: false}
    });
    
    // Deslizador para la aceleración
    var aceleracion = board.create('slider', [[0.5, -4], [4, -4], [1, 4, 8]], {
      name: 'a (m/s²)',
      snapWidth: 0.5,
      precision: 1
    });
    
    // Parábola de posición vs tiempo
    var parabola = board.create('functiongraph', [function(t) {
      return 0.5 * aceleracion.Value() * t * t;
    }, 0, 5], {
      strokeColor: '#ef4444',
      strokeWidth: 3
    });
    
    // Etiquetas
    board.create('text', [0.2, 52, 'Posición (m)'], {fontSize: 12, strokeColor: '#374151', fixed: true});
    board.create('text', [5.2, -1, 'Tiempo (s)'], {fontSize: 12, strokeColor: '#374151', fixed: true});
    
    board.create('text', [3, 45, function() {
      return 'a = ' + aceleracion.Value().toFixed(1) + ' m/s²';
    }], {fontSize: 12, strokeColor: '#ef4444', fixed: true});
    
    board.create('text', [3, 40, 'x = ½at²'], {fontSize: 11, strokeColor: '#64748b', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **Interpretación:** Una **parábola** indica MRUA. La curva se hace más pronunciada si la aceleración es mayor.

---

## 📊 **Gráfica Velocidad vs Tiempo (v-t)**

### **El Área Bajo la Curva = Desplazamiento**

Un concepto muy importante: el **área bajo la gráfica v-t** representa el **desplazamiento** del objeto.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-vt-area" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-vt-area')) {
    var chart = echarts.init(document.getElementById('echarts-vt-area'));
    var option = {
      title: { text: 'Velocidad vs Tiempo (MRU)', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      animation: true,
      grid: { left: '15%', right: '10%', top: '18%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, min: 0, max: 5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      yAxis: { type: 'value', name: 'Velocidad (m/s)', nameLocation: 'middle', nameGap: 40, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, min: 0, max: 12, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      series: [{
        type: 'line',
        data: [[0, 8], [1, 8], [2, 8], [3, 8], [4, 8]],
        lineStyle: { width: 3, color: '#22c55e' },
        symbol: 'circle',
        symbolSize: 8,
        itemStyle: { color: '#22c55e' },
        areaStyle: {
          color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
            colorStops: [{ offset: 0, color: 'rgba(34, 197, 94, 0.4)' }, { offset: 1, color: 'rgba(34, 197, 94, 0.1)' }]
          }
        }
      }]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

| Tipo de movimiento | Forma de gráfica v-t | Área bajo la curva |
|--------------------|---------------------|-------------------|
| **MRU** | Línea horizontal | Rectángulo: $\Delta x = v \cdot t$ |
| **MRUA** | Línea inclinada | Triángulo + rectángulo |

---

### **La Pendiente = Aceleración**

$$
\text{Pendiente de v-t} = \frac{\Delta v}{\Delta t} = a
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-vt-mrua" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-vt-mrua')) {
    var chart = echarts.init(document.getElementById('echarts-vt-mrua'));
    var option = {
      title: { text: 'Velocidad vs Tiempo (MRUA)', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      animation: true,
      grid: { left: '15%', right: '10%', top: '18%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, min: 0, max: 5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      yAxis: { type: 'value', name: 'Velocidad (m/s)', nameLocation: 'middle', nameGap: 40, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, min: 0, max: 25, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      series: [{
        type: 'line',
        data: [[0, 0], [1, 5], [2, 10], [3, 15], [4, 20]],
        lineStyle: { width: 3, color: '#ef4444' },
        symbol: 'circle',
        symbolSize: 10,
        itemStyle: { color: '#ef4444' },
        label: { show: true, formatter: function(p) { return p.data[1] + ' m/s'; }, position: 'top', fontSize: 10 },
        areaStyle: {
          color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
            colorStops: [{ offset: 0, color: 'rgba(239, 68, 68, 0.3)' }, { offset: 1, color: 'rgba(239, 68, 68, 0.05)' }]
          }
        }
      }]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 En este ejemplo: $a = \frac{20 - 0}{4 - 0} = \frac{20}{4} = 5\,\mathrm{m/s^2}$

---

## 📋 **Resumen: Cómo Leer las Gráficas**

| Si en la gráfica x-t veo... | Significa que... |
|----------------------------|------------------|
| Línea horizontal | El objeto está en **reposo** |
| Línea recta inclinada hacia arriba | Movimiento con **velocidad positiva constante** (MRU) |
| Línea recta inclinada hacia abajo | Movimiento con **velocidad negativa** (regresa) |
| Parábola hacia arriba | **Aceleración positiva** (MRUA) |
| Parábola hacia abajo | **Desaceleración** (frena) |

| Si en la gráfica v-t veo... | Significa que... |
|----------------------------|------------------|
| Línea horizontal en v > 0 | MRU hacia adelante |
| Línea horizontal en v < 0 | MRU hacia atrás |
| Línea inclinada hacia arriba | **Aceleración positiva** |
| Línea inclinada hacia abajo | **Aceleración negativa** (frena o invierte) |

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 1 — Identificar el movimiento**

Observa la siguiente gráfica y determina qué tipo de movimiento representa cada tramo:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-ejercicio" style="width: 100%; height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejercicio')) {
    var chart = echarts.init(document.getElementById('echarts-ejercicio'));
    var option = {
      title: { text: 'Posición vs Tiempo', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      animation: true,
      grid: { left: '15%', right: '10%', top: '18%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, min: 0, max: 12, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      yAxis: { type: 'value', name: 'Posición (m)', nameLocation: 'middle', nameGap: 40, nameTextStyle: { fontSize: 12, fontWeight: 'bold' }, min: 0, max: 25, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      series: [{
        type: 'line',
        data: [[0, 0], [2, 10], [4, 20], [6, 20], [8, 20], [10, 10], [12, 0]],
        lineStyle: { width: 3, color: '#3b82f6' },
        symbol: 'circle',
        symbolSize: 10,
        itemStyle: { color: '#3b82f6' }
      }]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

<details>
<summary><strong>Ver solución</strong></summary>

| Tramo | Tiempo | Tipo de movimiento |
|-------|--------|-------------------|
| **A** | 0s → 4s | MRU (avanza a velocidad constante) |
| **B** | 4s → 8s | Reposo (no se mueve) |
| **C** | 8s → 12s | MRU en sentido contrario (regresa) |

</details>

---

### **Ejercicio 2 — Calcular velocidad desde gráfica**

En la gráfica del ejercicio anterior, calcula la velocidad en el tramo A.

<details>
<summary><strong>Ver solución</strong></summary>

**Datos del tramo A:**
- $x_i = 0\,\mathrm{m}$, $x_f = 20\,\mathrm{m}$
- $t_i = 0\,\mathrm{s}$, $t_f = 4\,\mathrm{s}$

**Cálculo:**

$$
v = \frac{\Delta x}{\Delta t} = \frac{20 - 0}{4 - 0} = \boxed{5\,\mathrm{m/s}}
$$

</details>

---

### **Ejercicio 3 — Construir gráfica desde datos**

Un auto parte del reposo y acelera a $2\,\mathrm{m/s^2}$ durante 5 segundos. Construye la gráfica v-t.

<details>
<summary><strong>Ver solución</strong></summary>

**Tabla de valores:**

| t (s) | v (m/s) |
|-------|---------|
| 0 | 0 |
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |
| 5 | 10 |

La gráfica es una **línea recta** que parte de (0, 0) y llega a (5, 10).

La **pendiente** de esta línea es $\frac{10}{5} = 2\,\mathrm{m/s^2}$, que es exactamente la aceleración.

</details>
