# 🍎 **Caída Libre**

En esta lección aplicaremos todo lo que aprendimos sobre MRUA a un caso muy especial: cuando el único "motor" que acelera un objeto es la **gravedad**.

---

## 🌍 **¿Qué es la Caída Libre?**

La **Caída Libre** es un movimiento donde un objeto cae **únicamente bajo la influencia de la gravedad**, sin ninguna otra fuerza que lo empuje o lo frene (idealmente, sin fricción del aire).

$$
g = 9.8\,\mathrm{m/s^2} \approx 10\,\mathrm{m/s^2}
$$

> 💡 **Significado:** Cada segundo que cae un objeto, su velocidad **aumenta en 10 m/s**.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-caida-intro" width="600" height="350" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-caida-intro')) {
    var canvas = document.getElementById('roughjs-caida-intro');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('La velocidad aumenta cada segundo', 300, 25);
    
    // Posiciones de las pelotas (espaciadas, más arriba)
    var positions = [[100, 55], [230, 85], [360, 125], [490, 175]];
    var times = ['t = 0s', 't = 1s', 't = 2s', 't = 3s'];
    var velocities = ['v = 0', 'v = 10 m/s', 'v = 20 m/s', 'v = 30 m/s'];
    var arrowLengths = [0, 30, 55, 80];
    
    for (var i = 0; i < positions.length; i++) {
      var x = positions[i][0];
      var y = positions[i][1];
      
      // Pelota
      rc.circle(x, y, 28, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
      
      // Flecha de velocidad (hacia abajo)
      if (arrowLengths[i] > 0) {
        rc.line(x, y + 17, x, y + 17 + arrowLengths[i], { stroke: '#ef4444', strokeWidth: 3, roughness: 0.4 });
        rc.line(x - 7, y + 11 + arrowLengths[i], x, y + 17 + arrowLengths[i], { stroke: '#ef4444', strokeWidth: 2 });
        rc.line(x + 7, y + 11 + arrowLengths[i], x, y + 17 + arrowLengths[i], { stroke: '#ef4444', strokeWidth: 2 });
      }
      
      // Etiquetas de tiempo
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillStyle = '#64748b';
      ctx.textAlign = 'center';
      ctx.fillText(times[i], x, y - 22);
      
      // Etiquetas de velocidad
      ctx.font = 'bold 11px Inter, sans-serif';
      ctx.fillStyle = '#ef4444';
      ctx.fillText(velocities[i], x, y + 30 + arrowLengths[i] + 10);
    }
    
    // Leyenda
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.textAlign = 'left';
    ctx.fillText('📌 Las flechas rojas muestran la velocidad (más larga = más rápido)', 80, 335);
  }
});
</script>

| Tiempo de caída | Velocidad |
|-----------------|-----------| 
| $t = 0\,\mathrm{s}$ | $0\,\mathrm{m/s}$ |
| $t = 1\,\mathrm{s}$ | $10\,\mathrm{m/s}$ |
| $t = 2\,\mathrm{s}$ | $20\,\mathrm{m/s}$ |
| $t = 3\,\mathrm{s}$ | $30\,\mathrm{m/s}$ |

---

## 🔗 **Conexión con MRUA: Deducción de las Fórmulas**

La **caída libre** es simplemente un **MRUA** donde la aceleración es la **gravedad**. Observemos la situación:

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-derivacion" width="500" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-derivacion')) {
    var canvas = document.getElementById('roughjs-derivacion');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Altura inicial
    rc.line(50, 20, 50, 160, { stroke: '#64748b', strokeWidth: 1, roughness: 0.3 });
    
    // Objeto arriba
    rc.circle(80, 35, 20, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.6 });
    
    // Flecha hacia abajo (g)
    rc.line(80, 50, 80, 140, { stroke: '#ef4444', strokeWidth: 3, roughness: 0.5 });
    rc.line(72, 130, 80, 140, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    rc.line(88, 130, 80, 140, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    
    // Objeto abajo (fantasma)
    rc.circle(80, 150, 20, { stroke: '#94a3b8', strokeWidth: 1, fill: 'transparent', roughness: 0.6 });
    
    // Suelo
    rc.line(30, 165, 150, 165, { stroke: '#65a30d', strokeWidth: 3, roughness: 0.8 });
    
    // Etiquetas
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('v₀ (inicial)', 100, 40);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('g = 10 m/s²', 95, 100);
    
    ctx.fillStyle = '#64748b';
    ctx.fillText('h', 35, 95);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('v (final)', 100, 155);
    
    // Panel explicativo
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('En MRUA:', 220, 35);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• a = aceleración', 220, 60);
    ctx.fillText('• x = desplazamiento', 220, 80);
    
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('En Caída Libre:', 220, 110);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• a = g (gravedad)', 220, 135);
    ctx.fillText('• x = h (altura)', 220, 155);
  }
});
</script>

### **Las fórmulas del MRUA se transforman así:**

| Fórmula MRUA | Nombre |
|--------------|--------|
| $v = v_0 + a \cdot t$ | Velocidad |
| $x = v_0 \cdot t + \frac{1}{2} a \cdot t^2$ | Posición |
| $v^2 = v_0^2 + 2 \cdot a \cdot x$ | Sin conocer el tiempo |

### **Reemplazamos a por g y x por h:**

En caída libre, la aceleración es la **gravedad**: $a = g = 10\,\mathrm{m/s^2}$

| Fórmula MRUA | → | Fórmula Caída Libre |
|--------------|---|---------------------|
| $v = v_0 + a \cdot t$ | $a = g$ | $v = v_0 + g \cdot t$ |
| $x = v_0 \cdot t + \frac{1}{2} a \cdot t^2$ | $a = g$, $x = h$ | $h = v_0 \cdot t + \frac{1}{2} g \cdot t^2$ |
| $v^2 = v_0^2 + 2ax$ | $a = g$, $x = h$ | $v^2 = v_0^2 + 2gh$ |

### **Paso 3: Caso especial — Objeto que se suelta (parte del reposo)**

Si el objeto **se suelta** (no se lanza), entonces $v_0 = 0$:

| Fórmula general | Con $v_0 = 0$ | Fórmula simplificada |
|-----------------|--------------|----------------------|
| $v = v_0 + g \cdot t$ | $v = 0 + g \cdot t$ | $\boxed{v = g \cdot t}$ |
| $h = v_0 \cdot t + \frac{1}{2} g \cdot t^2$ | $h = 0 + \frac{1}{2} g \cdot t^2$ | $\boxed{h = \frac{1}{2} g \cdot t^2}$ |
| $v^2 = v_0^2 + 2gh$ | $v^2 = 0 + 2gh$ | $\boxed{v^2 = 2gh}$ |

> 💡 **Conclusión:** Las fórmulas de caída libre son las **mismas** del MRUA con $a = g$ y $v_0 = 0$ (cuando se suelta).

---

### 🎮 **Simulador Interactivo: Caída Libre**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> Mueve el deslizador para ver cómo cambian la velocidad y la altura
  </div>
  <div id="jsxgraph-caida-sim" class="jsxgraph-container" style="width: 100%; height: 380px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-caida-sim')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-caida-sim', {
      boundingbox: [-1, 50, 8, -10],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: {enabled: false},
      zoom: {enabled: false}
    });
    
    var tiempo = board.create('slider', [[1, -5], [6, -5], [0, 0, 3]], {
      name: 't (s)',
      snapWidth: 0.1,
      precision: 1
    });
    
    var hInicial = 45;
    board.create('line', [[0, hInicial], [7, hInicial]], {
      strokeColor: '#cbd5e1',
      strokeWidth: 2,
      dash: 2,
      fixed: true
    });
    
    board.create('line', [[0, 0], [7, 0]], {
      strokeColor: '#65a30d',
      strokeWidth: 3,
      fixed: true
    });
    
    var objeto = board.create('point', [
      function() { return 2; },
      function() {
        var t = tiempo.Value();
        var h = hInicial - 0.5 * 10 * t * t;
        return Math.max(0, h);
      }
    ], {
      name: '',
      size: 8,
      color: '#ef4444',
      fixed: true
    });
    
    board.create('text', [4.5, 42, function() {
      var t = tiempo.Value();
      return 'Tiempo: ' + t.toFixed(1) + ' s';
    }], {fontSize: 14, strokeColor: '#1e293b', fixed: true});
    
    board.create('text', [4.5, 36, function() {
      var t = tiempo.Value();
      var v = 10 * t;
      return 'Velocidad: ' + v.toFixed(1) + ' m/s';
    }], {fontSize: 14, strokeColor: '#22c55e', fixed: true});
    
    board.create('text', [4.5, 30, function() {
      var t = tiempo.Value();
      var h = hInicial - 0.5 * 10 * t * t;
      return 'Altura: ' + Math.max(0, h).toFixed(1) + ' m';
    }], {fontSize: 14, strokeColor: '#3b82f6', fixed: true});
    
    board.create('text', [0.5, 46, 'h₀ = 45 m'], {fontSize: 11, strokeColor: '#64748b', fixed: true});
    board.create('text', [0.5, 2, 'Suelo'], {fontSize: 11, strokeColor: '#65a30d', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## ⚙️ **Ejemplo 1 — Piedra soltada desde un puente**

Un estudiante suelta una piedra desde lo alto de un puente. La piedra cae libremente durante **3 segundos** antes de tocar el agua. ¿Con qué velocidad llegó al agua?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-puente" width="550" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-puente')) {
    var canvas = document.getElementById('roughjs-puente');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Puente
    rc.rectangle(30, 20, 150, 20, { fill: '#94a3b8', fillStyle: 'solid', stroke: '#64748b', roughness: 0.8 });
    rc.rectangle(40, 40, 15, 30, { fill: '#64748b', fillStyle: 'solid', roughness: 0.6 });
    rc.rectangle(155, 40, 15, 30, { fill: '#64748b', fillStyle: 'solid', roughness: 0.6 });
    
    // Persona
    rc.circle(120, 15, 10, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.6 });
    
    // Piedra inicial
    rc.circle(140, 25, 12, { fill: '#ef4444', fillStyle: 'solid', stroke: '#b91c1c', roughness: 0.8 });
    
    // Flecha de caída
    rc.line(140, 45, 140, 150, { stroke: '#ef4444', strokeWidth: 3, roughness: 1 });
    rc.line(130, 140, 140, 150, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.8 });
    rc.line(150, 140, 140, 150, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.8 });
    
    // Marcas de posición
    rc.circle(140, 60, 5, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(140, 90, 5, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(140, 120, 5, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    
    // Agua
    rc.line(20, 165, 200, 165, { stroke: '#3b82f6', strokeWidth: 3, roughness: 1.2 });
    rc.line(30, 172, 190, 172, { stroke: '#60a5fa', strokeWidth: 2, roughness: 1 });
    
    // Panel de datos
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Datos:', 250, 35);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• v₀ = 0 (se suelta)', 250, 60);
    ctx.fillText('• t = 3 s', 250, 80);
    ctx.fillText('• g = 10 m/s²', 250, 100);
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('Hallar: v = ?', 250, 130);
  }
});
</script>

### 📝 **Solución Paso a Paso**

**Fórmula:** $v = v_0 + g \cdot t$

Como se **suelta** (no se lanza), la velocidad inicial es cero: $v_0 = 0$

**Cálculo:**

$$
v = 0 + 10 \times 3 = \boxed{30\,\mathrm{m/s}}
$$

> ✅ La piedra llega al agua a **30 m/s** (equivalente a 108 km/h).

### 📊 **Gráfico: Velocidad vs Tiempo**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-piedra" style="width: 100%; height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-piedra')) {
    var chart = echarts.init(document.getElementById('echarts-piedra'));
    var option = {
      title: { text: 'Velocidad vs Tiempo', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      animation: true,
      grid: { left: '15%', right: '8%', top: '18%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, min: 0, max: 3.5, interval: 1, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      yAxis: { type: 'value', name: 'Velocidad (m/s)', nameLocation: 'middle', nameGap: 40, min: 0, max: 35, interval: 10, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      series: [{ type: 'line', data: [[0, 0], [1, 10], [2, 20], [3, 30]], lineStyle: { width: 3, color: '#ef4444' }, symbol: 'circle', symbolSize: 12, itemStyle: { color: '#ef4444' }, label: { show: true, formatter: function(p) { return p.data[1] + ' m/s'; }, position: 'top', fontSize: 10 } }]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## ⚙️ **Ejemplo 2 — Paracaidista saltando de un avión**

Un paracaidista salta desde un avión y cae en caída libre durante **4 segundos** antes de abrir el paracaídas. ¿Qué distancia recorrió?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-paracaidista" width="550" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-paracaidista')) {
    var canvas = document.getElementById('roughjs-paracaidista');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Avión
    rc.ellipse(80, 30, 80, 30, { fill: '#cbd5e1', fillStyle: 'solid', stroke: '#64748b', roughness: 0.8 });
    rc.line(45, 30, 30, 15, { stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
    rc.line(45, 30, 30, 45, { stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
    
    // Persona cayendo
    rc.circle(130, 55, 14, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.6 });
    
    // Flecha de caída
    rc.line(130, 70, 130, 160, { stroke: '#ef4444', strokeWidth: 3, roughness: 0.8 });
    rc.line(122, 150, 130, 160, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    rc.line(138, 150, 130, 160, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    
    // Marcas de posición
    rc.circle(130, 90, 5, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(130, 115, 5, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(130, 140, 5, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    
    // Persona abriendo paracaídas
    rc.circle(130, 170, 12, { fill: '#22c55e', fillStyle: 'solid', roughness: 0.6 });
    
    // Panel de datos
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Datos:', 250, 35);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• v₀ = 0', 250, 60);
    ctx.fillText('• t = 4 s', 250, 80);
    ctx.fillText('• g = 10 m/s²', 250, 100);
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Hallar: h = ?', 250, 130);
  }
});
</script>

### 📝 **Solución Paso a Paso**

**Fórmula de distancia en caída libre:**

$$
h = \frac{1}{2} g \cdot t^2
$$

**Cálculo:**

$$
h = \frac{1}{2} \times 10 \times 4^2 = \frac{1}{2} \times 10 \times 16 = \boxed{80\,\mathrm{m}}
$$

**¿Con qué velocidad llegó?**

$$
v = g \cdot t = 10 \times 4 = 40\,\mathrm{m/s} = 144\,\mathrm{km/h}
$$

> ✅ El paracaidista cayó **80 metros** y alcanzó **144 km/h** antes de abrir el paracaídas.

---

## ⚙️ **Ejemplo 3 — Moneda desde un edificio**

Una moneda se deja caer desde un edificio de **45 metros** de altura. ¿Cuánto tiempo tarda en llegar al suelo?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-edificio" width="550" height="200" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-edificio')) {
    var canvas = document.getElementById('roughjs-edificio');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Edificio
    rc.rectangle(30, 10, 100, 170, { fill: '#e2e8f0', fillStyle: 'solid', stroke: '#64748b', roughness: 0.6 });
    
    // Ventanas
    for (var row = 0; row < 4; row++) {
      for (var col = 0; col < 2; col++) {
        rc.rectangle(45 + col * 40, 25 + row * 40, 25, 25, { fill: '#93c5fd', fillStyle: 'solid', stroke: '#3b82f6', roughness: 0.4 });
      }
    }
    
    // Azotea
    rc.rectangle(25, 0, 110, 15, { fill: '#94a3b8', fillStyle: 'solid', stroke: '#64748b', roughness: 0.5 });
    
    // Moneda cayendo
    rc.circle(145, 20, 10, { fill: '#f59e0b', fillStyle: 'solid', stroke: '#d97706', roughness: 0.5 });
    
    // Flecha de caída
    rc.line(145, 35, 145, 165, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.8 });
    rc.line(140, 155, 145, 165, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    rc.line(150, 155, 145, 165, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    
    // Moneda en el suelo
    rc.circle(145, 178, 10, { fill: '#22c55e', fillStyle: 'solid', stroke: '#16a34a', roughness: 0.5 });
    
    // Suelo
    rc.line(20, 185, 200, 185, { stroke: '#65a30d', strokeWidth: 3, roughness: 0.8 });
    
    // Altura
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('h = 45 m', 155, 100);
    
    // Panel de datos
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Datos:', 280, 35);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• v₀ = 0', 280, 60);
    ctx.fillText('• h = 45 m', 280, 80);
    ctx.fillText('• g = 10 m/s²', 280, 100);
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('Hallar: t = ?', 280, 130);
  }
});
</script>

### 📝 **Solución Paso a Paso**

**Fórmula:** $h = \frac{1}{2} g \cdot t^2$

**Despejando $t$:**

$$
t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{2 \times 45}{10}} = \sqrt{\frac{90}{10}} = \sqrt{9} = \boxed{3\,\mathrm{s}}
$$

> ✅ La moneda tarda **3 segundos** en llegar al suelo.

---

## 📋 **Fórmulas de Caída Libre**

Las fórmulas son las mismas del MRUA, pero reemplazando $a$ por $g$:

| Fórmula | Uso | Cuándo usarla |
|---------|-----|---------------|
| $v = g \cdot t$ | Calcular velocidad | Conoces el tiempo |
| $h = \frac{1}{2} g \cdot t^2$ | Calcular distancia | Parte del reposo |
| $v^2 = 2 \cdot g \cdot h$ | Sin conocer el tiempo | Conoces la altura |

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 1**

Un niño suelta una pelota desde una ventana. La pelota cae durante **2 segundos**. ¿A qué altura está la ventana?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_0 = 0$, $t = 2\,\mathrm{s}$, $g = 10\,\mathrm{m/s^2}$

$$
h = \frac{1}{2} g \cdot t^2 = \frac{1}{2} \times 10 \times 2^2 = \boxed{20\,\mathrm{m}}
$$

</details>

---

### **Ejercicio 2**

Una piedra cae desde un acantilado de **80 metros**. ¿Con qué velocidad llega al suelo?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v_0 = 0$, $h = 80\,\mathrm{m}$, $g = 10\,\mathrm{m/s^2}$

$$
v^2 = 2gh = 2 \times 10 \times 80 = 1600
$$

$$
v = \sqrt{1600} = \boxed{40\,\mathrm{m/s}}
$$

</details>

---

### **Ejercicio 3**

Un objeto llega al suelo con una velocidad de **50 m/s**. ¿Desde qué altura cayó?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $v = 50\,\mathrm{m/s}$, $v_0 = 0$, $g = 10\,\mathrm{m/s^2}$

$$
v^2 = 2gh \Rightarrow h = \frac{v^2}{2g} = \frac{50^2}{2 \times 10} = \frac{2500}{20} = \boxed{125\,\mathrm{m}}
$$

</details>

---

### **Ejercicio 4**

Una manzana cae de un árbol de **5 metros** de altura. ¿Cuánto tiempo tarda en caer?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:** $h = 5\,\mathrm{m}$, $g = 10\,\mathrm{m/s^2}$

$$
t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{2 \times 5}{10}} = \sqrt{1} = \boxed{1\,\mathrm{s}}
$$

</details>
