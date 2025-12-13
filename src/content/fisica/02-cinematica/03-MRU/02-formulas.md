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

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-atleta" width="600" height="100" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-atleta')) {
    var canvas = document.getElementById('roughjs-atleta');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Línea principal (camino del atleta) - estilo dibujado a mano
    rc.line(50, 50, 550, 50, { stroke: '#3b82f6', strokeWidth: 2, roughness: 1.5 });
    
    // Punta de flecha
    rc.line(530, 40, 550, 50, { stroke: '#3b82f6', strokeWidth: 2, roughness: 1 });
    rc.line(530, 60, 550, 50, { stroke: '#3b82f6', strokeWidth: 2, roughness: 1 });
    
    // Círculo de inicio
    rc.circle(50, 50, 12, { fill: '#22c55e', fillStyle: 'solid', stroke: '#22c55e', roughness: 0.8 });
    
    // Círculo de fin
    rc.circle(550, 50, 12, { fill: '#ef4444', fillStyle: 'solid', stroke: '#ef4444', roughness: 0.8 });
    
    // Textos
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('🏃 Salida', 35, 75);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('🏁 Meta', 520, 75);
    
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.textAlign = 'center';
    ctx.fillText('← 100 m →', 300, 30);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('t = 10 s  |  v = ?', 300, 95);
  }
});
</script>

---

### 📝 **Paso 1: Identifica los datos**

| Dato | Valor | Significado |
|------|-------|-------------|
| $x$ | $100\,\mathrm{m}$ | Desplazamiento |
| $t$ | $10\,\mathrm{s}$ | Tiempo |
| $v$ | **?** | Velocidad (lo que buscamos) |

---

### 🧮 **Paso 2: Selecciona la fórmula adecuada**

Como buscamos la **velocidad**, usamos:

$$
v = \frac{x}{t}
$$

---

### 📐 **Paso 3: Sustituye y calcula**

$$
v = \frac{100\,\mathrm{m}}{10\,\mathrm{s}} = \boxed{10\,\mathrm{m/s}}
$$

---

### 📊 **Visualización del movimiento**

Observa cómo la posición aumenta uniformemente con el tiempo:

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
      title: { text: 'Posición vs Tiempo del atleta', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '18%', right: '8%', top: '15%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 11, interval: 1, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Posición (m)', nameLocation: 'middle', nameGap: 50, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 110, interval: 10, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
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

---

### ✅ **Resumen**

| Magnitud | Fórmula | Resultado |
|----------|---------|-----------|
| **Velocidad** | $v = \frac{x}{t} = \frac{100\,\mathrm{m}}{10\,\mathrm{s}}$ | $10\,\mathrm{m/s}$ |

> 💡 **Conclusión:** El atleta corrió a una velocidad constante de 10 metros por segundo.

---

## ⚙️ **Ejercicio 2 — Caso Simple (Hallar Desplazamiento)**

El sonido viaja a una velocidad constante de $340\,\mathrm{m/s}$. Si un trueno se escucha $3\,\mathrm{s}$ después del relámpago, ¿cuál fue el desplazamiento ($x$) del sonido?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-trueno" width="600" height="100" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-trueno')) {
    var canvas = document.getElementById('roughjs-trueno');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Línea punteada (sonido viajando) - estilo dibujado a mano
    for (var i = 0; i < 10; i++) {
      var x1 = 70 + i * 50;
      var x2 = x1 + 30;
      rc.line(x1, 50, x2, 50, { stroke: '#f59e0b', strokeWidth: 2, roughness: 1.2 });
    }
    
    // Ondas de sonido cerca del origen
    rc.arc(60, 50, 30, 20, 0.5, 2.6, false, { stroke: '#f59e0b', strokeWidth: 1.5, roughness: 0.8 });
    rc.arc(60, 50, 45, 25, 0.5, 2.6, false, { stroke: '#f59e0b', strokeWidth: 1.5, roughness: 0.8 });
    
    // Punta de flecha
    rc.line(530, 40, 550, 50, { stroke: '#f59e0b', strokeWidth: 2, roughness: 1 });
    rc.line(530, 60, 550, 50, { stroke: '#f59e0b', strokeWidth: 2, roughness: 1 });
    
    // Textos
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('⚡ Relámpago', 20, 85);
    
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('👂 Oído', 530, 85);
    
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.textAlign = 'center';
    ctx.fillText('← ¿Qué distancia recorrió? →', 300, 25);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('v = 340 m/s  |  t = 3 s', 300, 95);
  }
});
</script>

---

### 📝 **Paso 1: Identifica los datos**

| Dato | Valor | Significado |
|------|-------|-------------|
| $v$ | $340\,\mathrm{m/s}$ | Velocidad del sonido |
| $t$ | $3\,\mathrm{s}$ | Tiempo transcurrido |
| $x$ | **?** | Desplazamiento (lo que buscamos) |

---

### 🧮 **Paso 2: Selecciona la fórmula adecuada**

Como buscamos el **desplazamiento**, usamos:

$$
x = v \cdot t
$$

---

### 📐 **Paso 3: Sustituye y calcula**

$$
x = 340\,\mathrm{m/s} \times 3\,\mathrm{s} = \boxed{1020\,\mathrm{m}}
$$

---

### 📊 **Visualización del movimiento**

Observa cómo la posición del sonido aumenta con el tiempo:

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
      title: { text: 'Posición del sonido vs Tiempo', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '18%', right: '8%', top: '15%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 3.5, interval: 0.5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Posición (m)', nameLocation: 'middle', nameGap: 55, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 1100, interval: 200, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
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

---

### ✅ **Resumen**

| Magnitud | Fórmula | Resultado |
|----------|---------|-----------|
| **Desplazamiento** | $x = v \cdot t = 340 \times 3$ | $1020\,\mathrm{m}$ |

> 💡 **Conclusión:** El trueno estaba a más de 1 kilómetro de distancia.

---

## ⚙️ **Ejercicio 3 — Caso General (Hallar Posición Final)**

Un ciclista se encuentra en el **Kilómetro 10**. Continúa pedaleando a **20 km/h** durante **2 horas**. ¿En qué kilómetro estará?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-ciclista" width="600" height="100" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-ciclista')) {
    var canvas = document.getElementById('roughjs-ciclista');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Carretera (línea base)
    rc.line(40, 55, 560, 55, { stroke: '#94a3b8', strokeWidth: 2, roughness: 0.8 });
    
    // Flecha de movimiento del ciclista
    rc.line(100, 50, 500, 50, { stroke: '#22c55e', strokeWidth: 3, roughness: 1.3 });
    rc.line(480, 40, 500, 50, { stroke: '#22c55e', strokeWidth: 2, roughness: 1 });
    rc.line(480, 60, 500, 50, { stroke: '#22c55e', strokeWidth: 2, roughness: 1 });
    
    // Marcadores de kilómetros
    rc.circle(100, 55, 14, { fill: '#f59e0b', fillStyle: 'solid', stroke: '#f59e0b', roughness: 0.8 });
    rc.circle(500, 55, 14, { fill: '#22c55e', fillStyle: 'solid', stroke: '#22c55e', roughness: 0.8 });
    
    // Textos
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('🚴 Km 10', 70, 85);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('🏁 ¿Km ?', 475, 85);
    
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.textAlign = 'center';
    ctx.fillText('20 km/h durante 2 horas', 300, 25);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('¿A qué kilómetro llegó?', 300, 95);
  }
});
</script>

---

### 📝 **Paso 1: Identifica los datos**

| Dato | Valor | Significado |
|------|-------|-------------|
| $x_i$ | $10\,\mathrm{km}$ | Posición inicial |
| $v$ | $20\,\mathrm{km/h}$ | Velocidad |
| $t$ | $2\,\mathrm{h}$ | Tiempo |
| $x_f$ | **?** | Posición final (lo que buscamos) |

---

### 🧮 **Paso 2: Selecciona la fórmula adecuada**

Como buscamos la **posición final** y tenemos posición inicial, usamos:

$$
x_f = x_i + v \cdot t
$$

---

### 📐 **Paso 3: Sustituye y calcula**

$$
x_f = 10 + (20 \times 2) = 10 + 40 = \boxed{50\,\mathrm{km}}
$$

---

### 📊 **Visualización del movimiento**

Observa cómo el ciclista avanza desde el km 10 hasta el km 50:

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
      title: { text: 'Posición del ciclista vs Tiempo', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '18%', right: '8%', top: '15%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (h)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 2.5, interval: 0.5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Posición (km)', nameLocation: 'middle', nameGap: 45, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 55, interval: 10, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
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

---

### ✅ **Resumen**

| Magnitud | Fórmula | Resultado |
|----------|---------|-----------|
| **Posición final** | $x_f = x_i + v \cdot t = 10 + 40$ | $50\,\mathrm{km}$ |

> 💡 **Conclusión:** El ciclista terminará en el kilómetro 50.

---

## ⚙️ **Ejercicio 4 — Caso General (Hallar Tiempo)**

Un tren sale de **Montería**, ubicada en el **kilómetro 200**, hacia **Cartagena**, ubicada en el **kilómetro 500**. El tren viaja a **100 km/h**. ¿Cuánto tiempo tardará en llegar?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-tren" width="600" height="120" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-tren')) {
    var canvas = document.getElementById('roughjs-tren');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Vías del tren (líneas paralelas)
    rc.line(40, 45, 560, 45, { stroke: '#64748b', strokeWidth: 2, roughness: 0.6 });
    rc.line(40, 51, 560, 51, { stroke: '#64748b', strokeWidth: 2, roughness: 0.6 });
    
    // Travesaños de las vías
    for (var i = 0; i < 12; i++) {
      var x = 60 + i * 45;
      rc.line(x, 41, x, 55, { stroke: '#94a3b8', strokeWidth: 2, roughness: 0.5 });
    }
    
    // Flecha de movimiento del tren
    rc.line(80, 35, 520, 35, { stroke: '#a855f7', strokeWidth: 3, roughness: 1.3 });
    rc.line(500, 25, 520, 35, { stroke: '#a855f7', strokeWidth: 2, roughness: 1 });
    rc.line(500, 45, 520, 35, { stroke: '#a855f7', strokeWidth: 2, roughness: 1 });
    
    // Ciudades (rectángulos)
    rc.rectangle(55, 58, 55, 22, { fill: '#f59e0b', fillStyle: 'solid', stroke: '#f59e0b', roughness: 0.8 });
    rc.rectangle(490, 58, 60, 22, { fill: '#22c55e', fillStyle: 'solid', stroke: '#22c55e', roughness: 0.8 });
    
    // Textos de ciudades
    ctx.font = 'bold 10px Inter, sans-serif';
    ctx.fillStyle = '#fff';
    ctx.fillText('Montería', 58, 73);
    ctx.fillText('Cartagena', 493, 73);
    
    // Kilómetros debajo
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('km 200', 60, 95);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('km 500', 500, 95);
    
    // Velocidad arriba
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#a855f7';
    ctx.textAlign = 'center';
    ctx.fillText('🚂 Velocidad: 100 km/h', 300, 18);
    
    // Pregunta
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('¿Cuánto tiempo tardará?', 300, 115);
  }
});
</script>

---

### 📝 **Paso 1: Identifica los datos**

| Dato | Valor | Significado |
|------|-------|-------------|
| $x_i$ | $200\,\mathrm{km}$ | Posición inicial (Montería) |
| $x_f$ | $500\,\mathrm{km}$ | Posición final (Cartagena) |
| $v$ | $100\,\mathrm{km/h}$ | Velocidad |
| $t$ | **?** | Tiempo (lo que buscamos) |

---

### 🧮 **Paso 2: Selecciona la fórmula adecuada**

Como buscamos el **tiempo** con posiciones inicial y final, usamos:

$$
t = \frac{x_f - x_i}{v} = \frac{\Delta x}{v}
$$

---

### 📐 **Paso 3: Sustituye y calcula**

**Primero calculamos el desplazamiento:**
$$
\Delta x = x_f - x_i = 500 - 200 = 300\,\mathrm{km}
$$

**Luego el tiempo:**
$$
t = \frac{300\,\mathrm{km}}{100\,\mathrm{km/h}} = \boxed{3\,\mathrm{h}}
$$

---

### 📊 **Visualización del movimiento**

Observa cómo el tren viaja de Montería a Cartagena:

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
      title: { text: 'Posición del tren vs Tiempo', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '18%', right: '8%', top: '15%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (h)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 3.5, interval: 0.5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Posición (km)', nameLocation: 'middle', nameGap: 50, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 550, interval: 100, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 12, lineStyle: { width: 3, color: '#a855f7' }, areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: 'rgba(168, 85, 247, 0.3)' }, { offset: 1, color: 'rgba(168, 85, 247, 0.05)' }] } }, itemStyle: { color: '#a855f7', borderColor: '#fff', borderWidth: 2 }, data: [[0, 200], [1, 300], [2, 400], [3, 500]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#f59e0b', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Montería', position: 'right', fontSize: 10, fontWeight: 'bold', color: '#f59e0b' }, data: [[0, 200]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Cartagena', position: 'top', fontSize: 10, fontWeight: 'bold', color: '#22c55e' }, data: [[3, 500]] }
      ],
      tooltip: { trigger: 'axis' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### ✅ **Resumen**

| Magnitud | Fórmula | Resultado |
|----------|---------|-----------|
| **Tiempo** | $t = \frac{\Delta x}{v} = \frac{300}{100}$ | $3\,\mathrm{h}$ |

> 💡 **Conclusión:** El viaje de Montería a Cartagena durará 3 horas.