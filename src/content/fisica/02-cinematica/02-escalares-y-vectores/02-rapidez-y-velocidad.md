# 🏎️ **Rapidez vs. Velocidad**

Al igual que ocurre con la distancia y el desplazamiento, en el lenguaje cotidiano usamos "rapidez" y "velocidad" como sinónimos. Sin embargo, en física describen aspectos diferentes del movimiento.

---

## ⚡ **Rapidez**

Es una magnitud **escalar** que indica qué tan deprisa se recorrió una **distancia** total. No tiene en cuenta la dirección.

* **Relación:** Se calcula con la **distancia** ($d$).
* **Signo:** Siempre es positiva.

$$
\text{Rapidez media} = \frac{\text{distancia recorrida}}{\text{tiempo transcurrido}}
$$

$$
v = \frac{d}{t}
$$

## 🧭 **Velocidad**

Es una magnitud **vectorial** que indica qué tan rápido cambió la **posición** (desplazamiento) y en qué dirección.

* **Relación:** Se calcula con el **desplazamiento** ($\Delta x$).
* **Signo:** Puede ser positiva o negativa (indica el sentido del movimiento).

$$
\text{Velocidad media} = \frac{\text{desplazamiento}}{\text{tiempo transcurrido}}
$$

$$
\vec{v} = \frac{\Delta x}{t}
$$

---

## ⚙️ **Ejercicio 1 — Carrera de 100 metros**

Un atleta olímpico corre en una pista recta. Inicia en la línea de salida y cruza la meta ubicada a $100\,\mathrm{m}$ de distancia en un tiempo de $10\,\mathrm{s}$.

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-atleta-rv" width="600" height="100" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-atleta-rv')) {
    var canvas = document.getElementById('roughjs-atleta-rv');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Pista (línea principal) - estilo dibujado a mano
    rc.line(50, 50, 550, 50, { stroke: '#374151', strokeWidth: 2, roughness: 1.5 });
    
    // Flecha de movimiento
    rc.line(60, 50, 540, 50, { stroke: '#3b82f6', strokeWidth: 3, roughness: 1.2 });
    rc.line(520, 40, 540, 50, { stroke: '#3b82f6', strokeWidth: 2, roughness: 1 });
    rc.line(520, 60, 540, 50, { stroke: '#3b82f6', strokeWidth: 2, roughness: 1 });
    
    // Círculo de inicio
    rc.circle(50, 50, 14, { fill: '#22c55e', fillStyle: 'solid', stroke: '#22c55e', roughness: 0.8 });
    
    // Bandera de meta
    rc.rectangle(545, 35, 10, 30, { fill: '#ef4444', fillStyle: 'solid', stroke: '#ef4444', roughness: 0.6 });
    
    // Textos
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('🏃 Salida', 30, 80);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('🏁 Meta', 520, 80);
    
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.textAlign = 'center';
    ctx.fillText('← 100 m →', 300, 25);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('t = 10 s', 300, 95);
  }
});
</script>

---

### 📝 **Paso 1: Identifica los datos**

| Dato | Valor |
|------|-------|
| Posición inicial | $0\,\mathrm{m}$ (línea de salida) |
| Posición final | $100\,\mathrm{m}$ (meta) |
| Tiempo | $10\,\mathrm{s}$ |

---

### 📐 **Paso 2: Analiza el movimiento**

El atleta corre en **línea recta sin retroceder**, por lo tanto:

- **Distancia recorrida:** $d = 100\,\mathrm{m}$
- **Desplazamiento:** $\Delta x = 100\,\mathrm{m}$ (hacia adelante)

> 💡 En este caso especial: distancia = desplazamiento

---

### 🧮 **Paso 3: Calcula rapidez y velocidad**

**Rapidez media:**
$$
v = \frac{d}{t} = \frac{100\,\mathrm{m}}{10\,\mathrm{s}} = 10\,\mathrm{m/s}
$$

**Velocidad media:**
$$
\vec{v} = \frac{\Delta x}{t} = \frac{+100\,\mathrm{m}}{10\,\mathrm{s}} = +10\,\mathrm{m/s}
$$

---

### 📊 **Visualización del movimiento**

Observa cómo el atleta avanza uniformemente desde la salida hasta la meta:

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-100m" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-100m')) {
    var chart = echarts.init(document.getElementById('echarts-100m'));
    var option = {
      title: { text: 'Carrera de 100 metros', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '12%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 11, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Posición (m)', nameLocation: 'middle', nameGap: 50, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 110, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 14, lineStyle: { width: 3, color: '#3b82f6' }, areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: 'rgba(59, 130, 246, 0.3)' }, { offset: 1, color: 'rgba(59, 130, 246, 0.05)' }] } }, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, data: [[0, 0], [5, 50], [10, 100]] },
        { type: 'scatter', symbolSize: 18, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Salida (0m)', position: 'bottom', fontSize: 11, fontWeight: 'bold', color: '#22c55e' }, data: [[0, 0]] },
        { type: 'scatter', symbolSize: 18, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Meta (100m)', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#ef4444' }, data: [[10, 100]] }
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
| **Rapidez** | $\frac{100\,\mathrm{m}}{10\,\mathrm{s}}$ | $10\,\mathrm{m/s}$ |
| **Velocidad** | $\frac{+100\,\mathrm{m}}{10\,\mathrm{s}}$ | $+10\,\mathrm{m/s}$ |

> 💡 **Conclusión:** En movimiento rectilíneo SIN retrocesos, la rapidez y la magnitud de la velocidad son iguales.

---

## ⚙️ **Ejercicio 2 — Caminata de ida y vuelta**

Una persona camina $60\,\mathrm{m}$ hacia el este, luego retrocede $20\,\mathrm{m}$ hacia el oeste. Tiempo total: $40\,\mathrm{s}$.

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-caminata" width="600" height="130" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-caminata')) {
    var canvas = document.getElementById('roughjs-caminata');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Línea base (referencia)
    rc.line(40, 80, 560, 80, { stroke: '#cbd5e1', strokeWidth: 1, roughness: 0.5 });
    
    // Flecha IDA (60m hacia el Este) - arriba
    rc.line(50, 45, 450, 45, { stroke: '#3b82f6', strokeWidth: 3, roughness: 1.3 });
    rc.line(430, 35, 450, 45, { stroke: '#3b82f6', strokeWidth: 2, roughness: 1 });
    rc.line(430, 55, 450, 45, { stroke: '#3b82f6', strokeWidth: 2, roughness: 1 });
    
    // Flecha VUELTA (20m hacia el Oeste) - abajo
    rc.line(450, 95, 320, 95, { stroke: '#ef4444', strokeWidth: 3, roughness: 1.3 });
    rc.line(340, 85, 320, 95, { stroke: '#ef4444', strokeWidth: 2, roughness: 1 });
    rc.line(340, 105, 320, 95, { stroke: '#ef4444', strokeWidth: 2, roughness: 1 });
    
    // Puntos clave
    rc.circle(50, 70, 14, { fill: '#22c55e', fillStyle: 'solid', stroke: '#22c55e', roughness: 0.8 });
    rc.circle(450, 70, 12, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#3b82f6', roughness: 0.8 });
    rc.circle(320, 70, 14, { fill: '#ef4444', fillStyle: 'solid', stroke: '#ef4444', roughness: 0.8 });
    
    // Textos
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('🚶 Inicio', 30, 125);
    
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('60 m', 450, 30);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('20 m', 370, 115);
    
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.textAlign = 'center';
    ctx.fillText('① Ida: 60 m hacia el Este →', 250, 18);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('② Vuelta: 20 m hacia el Oeste ←', 385, 125);
    
    ctx.fillStyle = '#22c55e';
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('Final: 40 m', 320, 60);
  }
});
</script>

---

### 📝 **Paso 1: Identifica los datos**

| Dato | Valor |
|------|-------|
| Distancia hacia el este | $60\,\mathrm{m}$ |
| Distancia hacia el oeste | $20\,\mathrm{m}$ |
| Tiempo total | $40\,\mathrm{s}$ |

---

### 📐 **Paso 2: Calcula distancia y desplazamiento**

**Distancia total** (todo lo caminado):
$$
d = 60\,\mathrm{m} + 20\,\mathrm{m} = 80\,\mathrm{m}
$$

**Desplazamiento** (cambio neto de posición):
$$
\Delta x = 60\,\mathrm{m} - 20\,\mathrm{m} = +40\,\mathrm{m} \text{ (hacia el este)}
$$

---

### 🧮 **Paso 3: Calcula rapidez y velocidad**

**Rapidez media:**
$$
v = \frac{d}{t} = \frac{80\,\mathrm{m}}{40\,\mathrm{s}} = 2\,\mathrm{m/s}
$$

**Velocidad media:**
$$
\vec{v} = \frac{\Delta x}{t} = \frac{+40\,\mathrm{m}}{40\,\mathrm{s}} = +1\,\mathrm{m/s}
$$

---

### 📊 **Visualización del movimiento**

Observa cómo la persona avanza 60m y luego retrocede 20m:

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-idavuelta" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-idavuelta')) {
    var chart = echarts.init(document.getElementById('echarts-idavuelta'));
    var option = {
      title: { text: 'Caminata de ida y vuelta', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '12%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 45, interval: 5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Posición (m)', nameLocation: 'middle', nameGap: 45, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 70, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 12, lineStyle: { width: 3, color: '#3b82f6' }, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, data: [[0, 0], [30, 60]] },
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 12, lineStyle: { width: 3, color: '#ef4444' }, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, data: [[30, 60], [40, 40]] },
        { type: 'scatter', symbolSize: 18, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Inicio (0m)', position: 'right', fontSize: 11, fontWeight: 'bold', color: '#22c55e' }, data: [[0, 0]] },
        { type: 'scatter', symbolSize: 18, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Llegó a 60m', position: 'top', fontSize: 10, fontWeight: 'bold', color: '#3b82f6' }, data: [[30, 60]] },
        { type: 'scatter', symbolSize: 18, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Final: 40m', position: 'right', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[40, 40]] }
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
| **Rapidez** | $\frac{80\,\mathrm{m}}{40\,\mathrm{s}}$ | $2\,\mathrm{m/s}$ |
| **Velocidad** | $\frac{+40\,\mathrm{m}}{40\,\mathrm{s}}$ | $+1\,\mathrm{m/s}$ |

> 💡 **Conclusión:** La rapidez es mayor porque considera **todo** el movimiento (80m). La velocidad solo considera el **cambio neto** de posición (40m).

---

## ⚙️ **Ejercicio 3 — Vuelta a la pista**

Un ciclista da una vuelta completa a un velódromo circular de $500\,\mathrm{m}$ en $50\,\mathrm{s}$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-velodromo" class="jsxgraph-container" style="width: 100%; height: 250px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-velodromo')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-velodromo', {
      boundingbox: [-4, 4, 4, -4], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('circle', [[0, 0], 2.5], {strokeColor: '#3b82f6', strokeWidth: 3, fillColor: 'transparent', fixed: true});
    board.create('point', [2.5, 0], {name: 'Inicio/Fin', size: 5, fixed: true, color: '#22c55e', label: {offset: [10, 0], strokeColor: '#22c55e'}});
    board.create('arrow', [[0, 2.5], [1.5, 2]], {strokeColor: '#f59e0b', strokeWidth: 2, fixed: true});
    board.create('text', [0, 3.2, 'd = 500 m'], {fontSize: 11, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [0, -3.2, 'Δx = 0 m'], {fontSize: 11, strokeColor: '#ef4444', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

### **✅ Solución**

$$
\text{Rapidez} = \frac{500\,\mathrm{m}}{50\,\mathrm{s}} = 10\,\mathrm{m/s} \qquad \text{Velocidad} = \frac{0\,\mathrm{m}}{50\,\mathrm{s}} = 0\,\mathrm{m/s}
$$

> 💡 ¡Aunque se movió muy rápido, su velocidad media es cero porque regresó al punto de partida!

---

## ⚙️ **Ejercicio 4 — Movimiento en "L"**

Un robot se mueve $3\,\mathrm{m}$ al Norte en $2\,\mathrm{s}$, luego $4\,\mathrm{m}$ al Este en $3\,\mathrm{s}$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-robotL" class="jsxgraph-container" style="width: 100%; height: 250px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-robotL')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-robotL', {
      boundingbox: [-1, 5, 6, -1], axis: true, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    var A = board.create('point', [0, 0], {name: 'Inicio', size: 4, fixed: true, color: '#22c55e', label: {offset: [-15, -15], strokeColor: '#22c55e'}});
    var B = board.create('point', [0, 3], {name: '', size: 3, fixed: true, color: '#3b82f6'});
    var C = board.create('point', [4, 3], {name: 'Fin', size: 4, fixed: true, color: '#ef4444', label: {offset: [10, 0], strokeColor: '#ef4444'}});
    board.create('arrow', [A, B], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('arrow', [B, C], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('arrow', [A, C], {strokeColor: '#22c55e', strokeWidth: 3, dash: 2, fixed: true});
    board.create('text', [-0.5, 1.5, '3m ↑'], {fontSize: 12, strokeColor: '#3b82f6', fixed: true, anchorX: 'right'});
    board.create('text', [2, 3.5, '4m'], {fontSize: 12, strokeColor: '#3b82f6', fixed: true});
    board.create('text', [2.5, 1, 'Δx=5m'], {fontSize: 11, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    board.unsuspendUpdate();
  }
});
</script>

### **✅ Solución**

| Magnitud | Cálculo | Resultado |
|----------|---------|-----------|
| Distancia | $3 + 4$ | $7\,\mathrm{m}$ |
| Desplazamiento | $\sqrt{3^2 + 4^2}$ | $5\,\mathrm{m}$ |
| Tiempo total | $2 + 3$ | $5\,\mathrm{s}$ |

$$
\text{Rapidez} = \frac{7\,\mathrm{m}}{5\,\mathrm{s}} = 1.4\,\mathrm{m/s} \qquad \text{Velocidad} = \frac{5\,\mathrm{m}}{5\,\mathrm{s}} = 1\,\mathrm{m/s}
$$

> 💡 El robot recorrió más distancia de la que avanzó en línea recta.