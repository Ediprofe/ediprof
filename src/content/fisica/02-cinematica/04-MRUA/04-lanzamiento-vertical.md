# 🚀 **Lanzamiento Vertical**

Ahora que entendemos la caída libre, vamos a estudiar qué pasa cuando lanzamos un objeto **hacia arriba**. La gravedad sigue actuando, pero esta vez **en contra** del movimiento.

---

## 🎯 **¿Qué es el Lanzamiento Vertical?**

El **Lanzamiento Vertical** ocurre cuando lanzamos un objeto hacia arriba con una velocidad inicial. La gravedad **desacelera** el objeto hasta que se detiene, y luego lo hace caer.

> 💡 **Idea clave:** La gravedad siempre apunta hacia abajo. Cuando el objeto sube, la gravedad lo frena. Cuando baja, lo acelera.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-lv-intro" width="600" height="250" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-lv-intro')) {
    var canvas = document.getElementById('roughjs-lv-intro');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Las tres fases del lanzamiento vertical', 300, 20);
    
    // FASE 1: Subida
    // Suelo
    rc.line(40, 230, 160, 230, { stroke: '#65a30d', strokeWidth: 2, roughness: 0.5 });
    // Pelota
    rc.circle(100, 180, 25, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    // Flecha velocidad (arriba)
    rc.line(100, 160, 100, 100, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.4 });
    rc.line(93, 110, 100, 100, { stroke: '#22c55e', strokeWidth: 2 });
    rc.line(107, 110, 100, 100, { stroke: '#22c55e', strokeWidth: 2 });
    // Flecha gravedad (abajo) - CONSTANTE 40px
    rc.line(130, 150, 130, 190, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.4 });
    rc.line(125, 183, 130, 190, { stroke: '#ef4444', strokeWidth: 2 });
    rc.line(135, 183, 130, 190, { stroke: '#ef4444', strokeWidth: 2 });
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.textAlign = 'center';
    ctx.fillText('① SUBIDA', 100, 245);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('v ↑, g ↓', 100, 75);
    ctx.fillText('v disminuye', 100, 60);
    
    // FASE 2: Punto más alto
    rc.line(220, 230, 340, 230, { stroke: '#65a30d', strokeWidth: 2, roughness: 0.5 });
    // Pelota en el punto más alto
    rc.circle(280, 60, 25, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.5 });
    // Solo flecha gravedad (abajo) - CONSTANTE 40px
    rc.line(280, 80, 280, 120, { stroke: '#ef4444', strokeWidth: 3, roughness: 0.4 });
    rc.line(273, 113, 280, 120, { stroke: '#ef4444', strokeWidth: 2 });
    rc.line(287, 113, 280, 120, { stroke: '#ef4444', strokeWidth: 2 });
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.textAlign = 'center';
    ctx.fillText('② PUNTO MÁS ALTO', 280, 245);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('v = 0', 280, 45);
    ctx.fillText('(se detiene)', 280, 140);
    
    // FASE 3: Bajada
    rc.line(400, 230, 520, 230, { stroke: '#65a30d', strokeWidth: 2, roughness: 0.5 });
    // Pelota
    rc.circle(460, 120, 25, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    // Flecha velocidad (abajo)
    rc.line(460, 140, 460, 200, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.4 });
    rc.line(453, 193, 460, 200, { stroke: '#22c55e', strokeWidth: 2 });
    rc.line(467, 193, 460, 200, { stroke: '#22c55e', strokeWidth: 2 });
    // Flecha gravedad (abajo) - CONSTANTE 40px
    rc.line(490, 140, 490, 180, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.4 });
    rc.line(483, 173, 490, 180, { stroke: '#ef4444', strokeWidth: 2 });
    rc.line(497, 173, 490, 180, { stroke: '#ef4444', strokeWidth: 2 });
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.textAlign = 'center';
    ctx.fillText('③ BAJADA', 460, 245);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('v ↓, g ↓', 475, 95);
    ctx.fillText('v aumenta', 475, 80);
    
    // Leyenda
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('→ Verde: velocidad', 50, 210);
    ctx.fillStyle = '#ef4444';
    ctx.fillText('→ Rojo: gravedad (siempre ↓)', 180, 210);
  }
});
</script>

### **Dos fases del movimiento:**

| Fase | Descripción | ¿Qué pasa con v? |
|------|-------------|------------------|
| **Subida** | El objeto sube, la gravedad lo frena | v disminuye |
| **Punto más alto** | La velocidad llega a cero | v = 0 |
| **Bajada** | El objeto cae, la gravedad lo acelera | v aumenta (negativa) |

---

## 🔗 **Conexión con MRUA: Deducción con Convención de Signos**

El lanzamiento vertical es un **MRUA** con aceleración constante (la gravedad). Veamos la situación:

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-derivacion-lv" width="500" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-derivacion-lv')) {
    var canvas = document.getElementById('roughjs-derivacion-lv');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Suelo
    rc.line(30, 160, 180, 160, { stroke: '#65a30d', strokeWidth: 3, roughness: 0.8 });
    
    // Persona/lanzador
    rc.circle(60, 145, 15, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.5 });
    
    // Objeto lanzado (abajo)
    rc.circle(100, 135, 12, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    
    // Flecha v0 hacia arriba
    rc.line(100, 120, 100, 40, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
    rc.line(93, 50, 100, 40, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    rc.line(107, 50, 100, 40, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    
    // Objeto en altura máxima
    rc.circle(100, 30, 12, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.5 });
    
    // Flecha g hacia abajo
    rc.line(140, 50, 140, 130, { stroke: '#ef4444', strokeWidth: 3, roughness: 0.5 });
    rc.line(133, 120, 140, 130, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    rc.line(147, 120, 140, 130, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    
    // Etiquetas
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('v₀ (+)', 110, 80);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('g (−)', 150, 90);
    
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('v = 0', 115, 35);
    
    // Panel de convención
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Convención de signos:', 250, 35);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('↑ Arriba = POSITIVO (+)', 250, 60);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('↓ Abajo = NEGATIVO (−)', 250, 85);
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Por eso:', 250, 115);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• v₀ > 0 (lanza hacia arriba)', 250, 135);
    ctx.fillText('• g es negativo (apunta abajo)', 250, 155);
  }
});
</script>

### **Estableciendo la Convención de Signos**

| Dirección | Signo | Ejemplo |
|-----------|-------|---------|
| **Hacia arriba** | $+$ (positivo) | Velocidad inicial $v_0 > 0$ |
| **Hacia abajo** | $-$ (negativo) | Gravedad $g = -10\,\mathrm{m/s^2}$ |

> 💡 **Por qué g es negativo:** La gravedad siempre apunta hacia abajo. Si definimos "arriba" como positivo, entonces la aceleración de la gravedad es **negativa**.

### **Paso 1: Fórmulas del MRUA**

| Fórmula MRUA | Nombre |
|--------------|--------|
| $v = v_0 + a \cdot t$ | Velocidad |
| $x = v_0 \cdot t + \frac{1}{2} a \cdot t^2$ | Posición |
| $v^2 = v_0^2 + 2ax$ | Sin conocer el tiempo |

### **Paso 2: Aplicar a = −g (gravedad hacia abajo)**

| Fórmula MRUA | Sustitución | Fórmula Lanzamiento Vertical |
|--------------|-------------|------------------------------|
| $v = v_0 + a \cdot t$ | $a = -g$ | $\boxed{v = v_0 - g \cdot t}$ |
| $x = v_0 \cdot t + \frac{1}{2} a \cdot t^2$ | $a = -g$, $x = h$ | $\boxed{h = v_0 \cdot t - \frac{1}{2} g \cdot t^2}$ |
| $v^2 = v_0^2 + 2ax$ | $a = -g$, $x = h$ | $\boxed{v^2 = v_0^2 - 2gh}$ |

> ⚠️ **Nota:** El signo **negativo** aparece porque la gravedad **se opone** al movimiento hacia arriba (desacelera el objeto).

### **Paso 3: Altura máxima (cuando v = 0)**

En el punto más alto, el objeto **se detiene** ($v = 0$) antes de caer:

De $v^2 = v_0^2 - 2gh$, cuando $v = 0$:

$$
0 = v_0^2 - 2gh_{\max} \Rightarrow h_{\max} = \frac{v_0^2}{2g}
$$

De $v = v_0 - gt$, cuando $v = 0$:

$$
0 = v_0 - gt_{\text{subida}} \Rightarrow t_{\text{subida}} = \frac{v_0}{g}
$$

> 💡 **Conclusión:** Las fórmulas con signo negativo son las mismas del MRUA con $a = -g$ por la convención de signos.

---

### 🎮 **Simulador Interactivo: Lanzamiento Vertical**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> Observa cómo sube y baja el objeto
  </div>
  <div id="jsxgraph-lanzamiento" class="jsxgraph-container" style="width: 100%; height: 400px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-lanzamiento')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-lanzamiento', {
      boundingbox: [-1, 25, 8, -5],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: {enabled: false},
      zoom: {enabled: false}
    });
    
    var v0 = 20;
    var g = 10;
    var tMax = v0 / g;
    var tTotal = 2 * tMax;
    
    var tiempo = board.create('slider', [[1, -3], [6, -3], [0, 0, tTotal]], {
      name: 't (s)',
      snapWidth: 0.1,
      precision: 1
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
        var h = v0 * t - 0.5 * g * t * t;
        return Math.max(0, h);
      }
    ], {
      name: '',
      size: 8,
      color: '#3b82f6',
      fixed: true
    });
    
    board.create('text', [4.5, 22, function() {
      return 't = ' + tiempo.Value().toFixed(1) + ' s';
    }], {fontSize: 14, strokeColor: '#1e293b', fixed: true});
    
    board.create('text', [4.5, 18, function() {
      var t = tiempo.Value();
      var v = v0 - g * t;
      return 'v = ' + v.toFixed(1) + ' m/s';
    }], {fontSize: 14, strokeColor: '#22c55e', fixed: true});
    
    board.create('text', [4.5, 14, function() {
      var t = tiempo.Value();
      var h = v0 * t - 0.5 * g * t * t;
      return 'Altura = ' + Math.max(0, h).toFixed(1) + ' m';
    }], {fontSize: 14, strokeColor: '#3b82f6', fixed: true});
    
    board.create('text', [4.5, 10, function() {
      var t = tiempo.Value();
      if (t < tMax - 0.1) return '↑ Subiendo';
      if (t > tMax + 0.1) return '↓ Bajando';
      return '● Punto más alto';
    }], {fontSize: 13, strokeColor: '#f59e0b', fixed: true});
    
    board.create('text', [0.5, 22, 'v₀ = 20 m/s'], {fontSize: 11, strokeColor: '#64748b', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## ⚙️ **Ejemplo 1 — Pelota lanzada hacia arriba**

Un jugador lanza una pelota verticalmente hacia arriba con velocidad inicial de **$20\,\mathrm{m/s}$**. ¿Cuánto tiempo tarda en alcanzar el punto más alto?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-pelota" width="550" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-pelota')) {
    var canvas = document.getElementById('roughjs-pelota');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Suelo
    rc.line(30, 165, 220, 165, { stroke: '#65a30d', strokeWidth: 3, roughness: 0.8 });
    
    // Persona
    rc.circle(60, 145, 15, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.6 });
    rc.rectangle(52, 160, 16, 5, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.4 });
    
    // Pelota inicial
    rc.circle(90, 130, 12, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 0.6 });
    
    // Flecha hacia arriba
    rc.line(90, 115, 90, 30, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.8 });
    rc.line(83, 40, 90, 30, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    rc.line(97, 40, 90, 30, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    
    // Pelota en punto más alto
    rc.circle(90, 20, 12, { fill: '#ef4444', fillStyle: 'solid', stroke: '#b91c1c', roughness: 0.6 });
    
    // Flecha de gravedad
    rc.line(120, 70, 120, 120, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    rc.line(115, 110, 120, 120, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    rc.line(125, 110, 120, 120, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    
    // Panel de datos
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Datos:', 280, 35);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• v₀ = 20 m/s (hacia arriba)', 280, 60);
    ctx.fillText('• g = 10 m/s² (hacia abajo)', 280, 80);
    ctx.fillText('• En el punto más alto: v = 0', 280, 100);
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('Hallar: t = ?', 280, 130);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('g ↓', 130, 100);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('v₀ ↑', 100, 75);
  }
});
</script>

### 📝 **Solución Paso a Paso**

**Concepto:** En el punto más alto, la velocidad es **cero** (el objeto se detiene antes de caer).

**Fórmula:** $v = v_0 - g \cdot t$

**En el punto más alto:** $v = 0$, entonces:

$$
0 = 20 - 10 \cdot t
$$

$$
t = \frac{20}{10} = \boxed{2\,\mathrm{s}}
$$

> ✅ La pelota tarda **2 segundos** en llegar al punto más alto.

### 📊 **Gráfico: Velocidad vs Tiempo**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-lanzamiento" style="width: 100%; height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-lanzamiento')) {
    var chart = echarts.init(document.getElementById('echarts-lanzamiento'));
    var option = {
      title: { text: 'Velocidad vs Tiempo', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      animation: true,
      grid: { left: '15%', right: '8%', top: '18%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, min: 0, max: 4.5, interval: 1, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      yAxis: { type: 'value', name: 'Velocidad (m/s)', nameLocation: 'middle', nameGap: 45, min: -25, max: 25, interval: 10, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      series: [{
        type: 'line',
        data: [[0, 20], [1, 10], [2, 0], [3, -10], [4, -20]],
        lineStyle: { width: 3, color: '#3b82f6' },
        symbol: 'circle',
        symbolSize: 12,
        itemStyle: { color: '#3b82f6' },
        label: { show: true, formatter: function(p) { return p.data[1] + ' m/s'; }, position: 'top', fontSize: 10 },
        markPoint: {
          symbol: 'circle',
          symbolSize: 18,
          itemStyle: { color: '#f59e0b', borderColor: '#fff', borderWidth: 2 },
          label: { show: true, formatter: 'v=0', fontSize: 9, fontWeight: 'bold', color: '#1e293b' },
          data: [{ coord: [2, 0] }]
        }
      }]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **Observa:** Después de $t = 2\,\mathrm{s}$, la velocidad es negativa (el objeto está cayendo).

---

## ⚙️ **Ejemplo 2 — Altura máxima de un cohete de agua**

Un cohete de agua es lanzado hacia arriba con velocidad inicial de **$30\,\mathrm{m/s}$**. ¿Qué altura máxima alcanza?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-cohete" width="550" height="200" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-cohete')) {
    var canvas = document.getElementById('roughjs-cohete');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Suelo
    rc.line(30, 185, 220, 185, { stroke: '#65a30d', strokeWidth: 3, roughness: 0.8 });
    
    // Cohete en el suelo
    rc.rectangle(55, 150, 20, 35, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 0.5 });
    rc.polygon([[55, 150], [65, 130], [75, 150]], { fill: '#ef4444', fillStyle: 'solid', stroke: '#b91c1c', roughness: 0.4 });
    
    // Agua saliendo
    rc.line(60, 185, 55, 195, { stroke: '#60a5fa', strokeWidth: 2, roughness: 0.8 });
    rc.line(65, 185, 65, 198, { stroke: '#60a5fa', strokeWidth: 2, roughness: 0.8 });
    rc.line(70, 185, 75, 195, { stroke: '#60a5fa', strokeWidth: 2, roughness: 0.8 });
    
    // Flecha hacia arriba
    rc.line(100, 170, 100, 30, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.8 });
    rc.line(93, 40, 100, 30, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    rc.line(107, 40, 100, 30, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    
    // Cohete en altura máxima
    rc.rectangle(90, 10, 20, 25, { fill: '#f59e0b', fillStyle: 'solid', stroke: '#d97706', roughness: 0.5 });
    
    // Panel de datos
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Datos:', 280, 35);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• v₀ = 30 m/s', 280, 60);
    ctx.fillText('• v = 0 (en el punto más alto)', 280, 80);
    ctx.fillText('• g = 10 m/s²', 280, 100);
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Hallar: h_máx = ?', 280, 130);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('v₀ = 30 m/s', 110, 110);
    
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('v = 0', 120, 25);
  }
});
</script>

### 📝 **Solución Paso a Paso**

**Fórmula:** $v^2 = v_0^2 - 2gh$ (signo negativo porque g se opone al movimiento)

**En la altura máxima:** $v = 0$

$$
0 = 30^2 - 2 \times 10 \times h
$$

$$
0 = 900 - 20h
$$

$$
h = \frac{900}{20} = \boxed{45\,\mathrm{m}}
$$

> ✅ El cohete alcanza una altura máxima de **45 metros**.

---

## ⚙️ **Ejemplo 3 — Tiempo de vuelo total**

Una piedra se lanza hacia arriba con velocidad de **$40\,\mathrm{m/s}$**. ¿Cuánto tiempo tarda en volver al punto de lanzamiento?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-vuelo" width="550" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-vuelo')) {
    var canvas = document.getElementById('roughjs-vuelo');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Suelo
    rc.line(30, 165, 500, 165, { stroke: '#65a30d', strokeWidth: 3, roughness: 0.8 });
    
    // Trayectoria (parábola simulada)
    ctx.beginPath();
    ctx.moveTo(80, 155);
    ctx.quadraticCurveTo(250, -50, 420, 155);
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2;
    ctx.setLineDash([6, 4]);
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Piedra inicial
    rc.circle(80, 155, 12, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 0.6 });
    
    // Piedra en altura máxima
    rc.circle(250, 20, 12, { fill: '#f59e0b', fillStyle: 'solid', stroke: '#d97706', roughness: 0.6 });
    
    // Piedra final
    rc.circle(420, 155, 12, { fill: '#22c55e', fillStyle: 'solid', stroke: '#16a34a', roughness: 0.6 });
    
    // Textos
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Lanzamiento', 55, 145);
    ctx.fillText('t = 0', 70, 180);
    
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('Altura máxima', 220, 15);
    ctx.fillText('v = 0', 240, 40);
    ctx.fillText('t = 4s', 245, 55);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('Regresa', 400, 145);
    ctx.fillText('t = 8s', 410, 180);
    
    // Panel de datos
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('v₀ = 40 m/s', 200, 100);
    ctx.fillText('t_subida = t_bajada', 200, 120);
  }
});
</script>

### 📝 **Solución Paso a Paso**

**Concepto:** El movimiento es **simétrico**. El tiempo de subida es igual al tiempo de bajada.

**Tiempo de subida** (hasta $v = 0$):

$$
t_{\text{subida}} = \frac{v_0}{g} = \frac{40}{10} = 4\,\mathrm{s}
$$

**Tiempo total:**

$$
t_{\text{total}} = 2 \times t_{\text{subida}} = 2 \times 4 = \boxed{8\,\mathrm{s}}
$$

> ✅ La piedra sube 4 segundos y baja 4 segundos. **Tiempo total: 8 segundos**.

---

## 📋 **Fórmulas del Lanzamiento Vertical**

| Fórmula | Uso |
|---------|-----|
| $v = v_0 - g \cdot t$ | Velocidad en cualquier instante |
| $h = v_0 \cdot t - \frac{1}{2} g \cdot t^2$ | Altura en cualquier instante |
| $t_{\text{subida}} = \frac{v_0}{g}$ | Tiempo para llegar al punto más alto |
| $h_{\max} = \frac{v_0^2}{2g}$ | Altura máxima |

> ⚠️ **Nota:** El signo negativo aparece porque la gravedad **se opone** al movimiento hacia arriba.

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 1**

Un balón se lanza hacia arriba con velocidad de **$15\,\mathrm{m/s}$**. ¿Cuánto tiempo tarda en alcanzar el punto más alto?

<details>
<summary><strong>Ver solución</strong></summary>

$$
t = \frac{v_0}{g} = \frac{15}{10} = \boxed{1.5\,\mathrm{s}}
$$

</details>

---

### **Ejercicio 2**

Una flecha se dispara hacia arriba con velocidad de **$50\,\mathrm{m/s}$**. ¿Qué altura máxima alcanza?

<details>
<summary><strong>Ver solución</strong></summary>

$$
h_{\max} = \frac{v_0^2}{2g} = \frac{50^2}{2 \times 10} = \frac{2500}{20} = \boxed{125\,\mathrm{m}}
$$

</details>

---

### **Ejercicio 3**

Un objeto lanzado hacia arriba alcanza una altura máxima de **$20\,\mathrm{m}$**. ¿Con qué velocidad fue lanzado?

<details>
<summary><strong>Ver solución</strong></summary>

$$
h = \frac{v_0^2}{2g} \Rightarrow v_0 = \sqrt{2gh} = \sqrt{2 \times 10 \times 20} = \sqrt{400} = \boxed{20\,\mathrm{m/s}}
$$

</details>

---

### **Ejercicio 4**

Una pelota se lanza hacia arriba con **$25\,\mathrm{m/s}$**. ¿Cuál es su velocidad después de **3 segundos**?

<details>
<summary><strong>Ver solución</strong></summary>

$$
v = v_0 - g \cdot t = 25 - 10 \times 3 = 25 - 30 = \boxed{-5\,\mathrm{m/s}}
$$

> El signo negativo indica que el objeto **ya está bajando**.

</details>
