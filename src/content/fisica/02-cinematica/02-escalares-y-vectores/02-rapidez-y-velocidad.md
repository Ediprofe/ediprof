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
      title: { text: 'Carrera de 100 metros', subtext: '100m en 10s → v = 10 m/s', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' }, subtextStyle: { fontSize: 12, color: '#3b82f6' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '18%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 11, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Posición (m)', nameLocation: 'middle', nameGap: 50, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 110, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 14, lineStyle: { width: 3, color: '#3b82f6' }, areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: 'rgba(59, 130, 246, 0.3)' }, { offset: 1, color: 'rgba(59, 130, 246, 0.05)' }] } }, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, data: [[0, 0], [5, 50], [10, 100]] },
        { type: 'scatter', symbolSize: 18, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Salida', position: 'bottom', fontSize: 11, fontWeight: 'bold', color: '#22c55e' }, data: [[0, 0]] },
        { type: 'scatter', symbolSize: 18, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Meta', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#ef4444' }, data: [[10, 100]] }
      ],
      tooltip: { trigger: 'axis' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

### **✅ Solución**

**Análisis:** Al ser línea recta sin retrocesos: $d = \Delta x = 100\,\mathrm{m}$

$$
\text{Rapidez} = \frac{100\,\mathrm{m}}{10\,\mathrm{s}} = 10\,\mathrm{m/s} \qquad \text{Velocidad} = \frac{+100\,\mathrm{m}}{10\,\mathrm{s}} = +10\,\mathrm{m/s}
$$

> 💡 En movimiento rectilíneo sin retrocesos, rapidez = |velocidad|.

---

## ⚙️ **Ejercicio 2 — Caminata de ida y vuelta**

Una persona camina $60\,\mathrm{m}$ hacia el este, luego retrocede $20\,\mathrm{m}$ hacia el oeste. Tiempo total: $40\,\mathrm{s}$.

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
      title: { text: 'Caminata de ida y vuelta', subtext: 'Distancia = 80m, Desplazamiento = 40m', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' }, subtextStyle: { fontSize: 12, color: '#f59e0b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '18%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 45, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Posición (m)', nameLocation: 'middle', nameGap: 45, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 70, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 12, lineStyle: { width: 3, color: '#3b82f6' }, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, data: [[0, 0], [30, 60]] },
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 12, lineStyle: { width: 3, color: '#ef4444' }, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, data: [[30, 60], [40, 40]] },
        { type: 'scatter', symbolSize: 18, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Inicio', position: 'right', fontSize: 11, fontWeight: 'bold', color: '#22c55e' }, data: [[0, 0]] },
        { type: 'scatter', symbolSize: 18, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '60m (ida)', position: 'top', fontSize: 10, fontWeight: 'bold', color: '#3b82f6' }, data: [[30, 60]] },
        { type: 'scatter', symbolSize: 18, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '40m (final)', position: 'right', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[40, 40]] }
      ],
      tooltip: { trigger: 'axis' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

### **✅ Solución**

| Magnitud | Cálculo | Resultado |
|----------|---------|-----------|
| Distancia | $60 + 20$ | $80\,\mathrm{m}$ |
| Desplazamiento | $60 - 20$ | $+40\,\mathrm{m}$ |

$$
\text{Rapidez} = \frac{80\,\mathrm{m}}{40\,\mathrm{s}} = 2\,\mathrm{m/s} \qquad \text{Velocidad} = \frac{+40\,\mathrm{m}}{40\,\mathrm{s}} = +1\,\mathrm{m/s}
$$

> 💡 La rapidez es mayor porque considera todo el movimiento; la velocidad solo el cambio neto de posición.

---

## ⚙️ **Ejercicio 3 — Vuelta a la pista**

Un ciclista da una vuelta completa a un velódromo circular de $500\,\mathrm{m}$ en $50\,\mathrm{s}$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 250px;">
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

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 300px;">
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