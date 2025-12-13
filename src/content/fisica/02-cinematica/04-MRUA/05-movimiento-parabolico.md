# 🏀 **Movimiento Parabólico**

¿Has visto cómo un balón de fútbol traza un arco en el aire al ser pateado? Esa trayectoria en forma de **parábola** es el resultado de combinar dos movimientos simultáneos.

---

## 🎯 **¿Qué es el Movimiento Parabólico?**

El **Movimiento Parabólico** (también llamado *Tiro Oblicuo*) ocurre cuando un objeto es lanzado con un ángulo respecto al suelo.

La clave para entenderlo es que son **dos movimientos independientes que ocurren al mismo tiempo**:

| Dirección | Tipo de movimiento | ¿Por qué? |
|-----------|-------------------|-----------|
| **Horizontal (x)** | MRU (velocidad constante) | No hay fuerza horizontal |
| **Vertical (y)** | Caída libre | La gravedad actúa hacia abajo |

> 💡 **Principio de independencia:** Lo que pasa en x no afecta a y, y viceversa.

---

## 🔗 **Conexión con MRU y MRUA: Deducción de las Fórmulas**

El movimiento parabólico **no es un movimiento nuevo** — es simplemente la **combinación** de dos movimientos que ya conocemos. Veamos la situación:

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-derivacion-mp" width="550" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-derivacion-mp')) {
    var canvas = document.getElementById('roughjs-derivacion-mp');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Suelo
    rc.line(30, 160, 200, 160, { stroke: '#65a30d', strokeWidth: 3, roughness: 0.8 });
    
    // Punto de lanzamiento
    rc.circle(50, 150, 14, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
    
    // Vector v0
    rc.line(50, 150, 130, 70, { stroke: '#3b82f6', strokeWidth: 3, roughness: 0.5 });
    rc.line(118, 78, 130, 70, { stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5 });
    
    // Vector vx (horizontal)
    rc.line(50, 150, 130, 150, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    rc.line(120, 147, 130, 150, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    rc.line(120, 153, 130, 150, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    
    // Vector vy (vertical)
    rc.line(130, 150, 130, 70, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    rc.line(127, 80, 130, 70, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    rc.line(133, 80, 130, 70, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    
    // Ángulo
    ctx.beginPath();
    ctx.arc(50, 150, 35, -Math.PI/3, 0);
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 2;
    ctx.stroke();
    
    // Etiquetas
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('v₀', 80, 95);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('vₓ (MRU)', 75, 170);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('vᵧ (MRUA)', 135, 115);
    
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('θ', 90, 145);
    
    // Panel explicativo
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Dos movimientos independientes:', 250, 35);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('En x → MRU:', 250, 60);
    ctx.fillStyle = '#64748b';
    ctx.fillText('vₓ = constante, x = vₓ·t', 320, 60);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('En y → MRUA:', 250, 90);
    ctx.fillStyle = '#64748b';
    ctx.fillText('vᵧ cambia por gravedad', 330, 90);
    
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Descomposición:', 250, 125);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('vₓ = v₀ · cos(θ)', 250, 145);
    ctx.fillText('vᵧ = v₀ · sen(θ)', 250, 165);
  }
});
</script>

### **Paso 1: Descomponer la velocidad inicial**

Al lanzar con ángulo $\theta$, usamos **trigonometría** para descomponer:

$$
v_x = v_0 \cdot \cos\theta \qquad v_y = v_0 \cdot \sin\theta
$$

### **Paso 2: Aplicar MRU en la dirección horizontal**

No hay fuerza horizontal, entonces $a_x = 0$ (velocidad constante):

| Fórmula MRU | Resultado |
|-------------|-----------|
| $x = v_x \cdot t$ | $\boxed{x = (v_0 \cos\theta) \cdot t}$ |
| $v_x = \text{constante}$ | $\boxed{v_x = v_0 \cos\theta}$ (siempre) |

### **Paso 3: Aplicar MRUA (caída libre) en la dirección vertical**

La gravedad actúa hacia abajo, entonces $a_y = -g$:

| Fórmula MRUA | Con $a = -g$ | Fórmula para y |
|--------------|--------------|----------------|
| $v = v_0 + at$ | $v_y = v_{y0} - gt$ | $\boxed{v_y = v_0\sin\theta - gt}$ |
| $y = v_0 t + \frac{1}{2}at^2$ | $y = v_{y0}t - \frac{1}{2}gt^2$ | $\boxed{y = (v_0\sin\theta)t - \frac{1}{2}gt^2}$ |

### **Paso 4: Deducir fórmulas especiales**

**Altura máxima** (cuando $v_y = 0$):

$$
0 = v_0\sin\theta - gt \Rightarrow t_{subida} = \frac{v_0\sin\theta}{g}
$$

$$
h_{\max} = \frac{(v_0\sin\theta)^2}{2g}
$$

**Tiempo de vuelo** (sube + baja):

$$
t_{total} = 2 \cdot t_{subida} = \frac{2v_0\sin\theta}{g}
$$

**Alcance horizontal** (x cuando vuelve al suelo):

$$
x = v_x \cdot t_{total} = v_0\cos\theta \cdot \frac{2v_0\sin\theta}{g} = \frac{v_0^2 \sin(2\theta)}{g}
$$

> 💡 **Conclusión:** Todas las fórmulas del mov. parabólico vienen de combinar MRU (horizontal) + Caída Libre (vertical).

---

## 📐 **Descomponiendo la Velocidad Inicial**

Cuando lanzamos un objeto con ángulo $\theta$, su velocidad inicial $v_0$ se descompone en dos componentes:

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-intro" width="600" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-intro')) {
    var canvas = document.getElementById('roughjs-intro');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Suelo
    rc.line(30, 160, 570, 160, { stroke: '#65a30d', strokeWidth: 3, roughness: 0.8 });
    
    // Trayectoria
    ctx.beginPath();
    ctx.moveTo(60, 150);
    ctx.quadraticCurveTo(300, -10, 540, 150);
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2;
    ctx.setLineDash([6, 4]);
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Pelotas
    rc.circle(60, 150, 18, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(180, 70, 16, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(300, 35, 16, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(420, 70, 16, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(540, 150, 18, { fill: '#22c55e', fillStyle: 'solid', roughness: 0.5 });
    
    // Textos
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('Inicio', 45, 175);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('Altura máxima', 260, 25);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('Llegada', 520, 175);
  }
});
</script>

> 💡 **Principio Fundamental:** El movimiento horizontal y el vertical son **independientes**. Lo que pasa en x no afecta a y, y viceversa.

---

## 📐 **Descomponiendo la Velocidad Inicial**

Cuando lanzamos un objeto con ángulo $\theta$, su velocidad inicial $v_0$ se descompone en dos componentes:

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-componentes" width="550" height="220" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-componentes')) {
    var canvas = document.getElementById('roughjs-componentes');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Origen
    rc.circle(60, 180, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
    
    // Vector v0
    rc.line(60, 180, 200, 60, { stroke: '#3b82f6', strokeWidth: 4, roughness: 0.5 });
    rc.line(185, 70, 200, 60, { stroke: '#3b82f6', strokeWidth: 3, roughness: 0.5 });
    rc.line(190, 80, 200, 60, { stroke: '#3b82f6', strokeWidth: 3, roughness: 0.5 });
    
    // vx
    rc.line(60, 180, 200, 180, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
    rc.line(190, 175, 200, 180, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    rc.line(190, 185, 200, 180, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    
    // vy
    rc.line(200, 180, 200, 60, { stroke: '#ef4444', strokeWidth: 3, roughness: 0.5 });
    rc.line(195, 70, 200, 60, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    rc.line(205, 70, 200, 60, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    
    // Ángulo
    ctx.beginPath();
    ctx.arc(60, 180, 50, -Math.atan(120/140), 0);
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 3;
    ctx.stroke();
    
    // Etiquetas
    ctx.font = 'bold 18px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('θ', 115, 170);
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('v₀', 100, 100);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('vₓ', 125, 205);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('vᵧ', 210, 125);
    
    // Fórmulas
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Fórmulas:', 280, 50);
    
    ctx.font = '13px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('vₓ = v₀ · cos(θ)', 280, 80);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('vᵧ = v₀ · sen(θ)', 280, 105);
  }
});
</script>

**Fórmulas de descomposición:**

$$
v_x = v_0 \cdot \cos(\theta) \qquad v_y = v_0 \cdot \sin(\theta)
$$

---

## ⚙️ **Ejemplo 1 — Tiro libre de fútbol**

Un jugador patea un balón con velocidad de **$20\,\mathrm{m/s}$** a un ángulo de **$30°$**. Calcular las componentes de velocidad, el tiempo de vuelo y el alcance.

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-futbol" width="550" height="160" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-futbol')) {
    var canvas = document.getElementById('roughjs-futbol');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Campo
    rc.line(30, 130, 520, 130, { stroke: '#65a30d', strokeWidth: 4, roughness: 0.8 });
    
    // Jugador
    rc.circle(60, 110, 15, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.6 });
    
    // Balón
    rc.circle(90, 125, 10, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.6 });
    
    // Trayectoria
    ctx.beginPath();
    ctx.moveTo(90, 120);
    ctx.quadraticCurveTo(250, 20, 420, 120);
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 2;
    ctx.setLineDash([5, 3]);
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Balón final
    rc.circle(420, 125, 10, { fill: '#22c55e', fillStyle: 'solid', roughness: 0.6 });
    
    // Panel de datos
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Datos:', 330, 40);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• v₀ = 20 m/s', 330, 60);
    ctx.fillText('• θ = 30°', 330, 78);
    ctx.fillText('• cos(30°) = 0.866', 330, 96);
    ctx.fillText('• sen(30°) = 0.5', 330, 114);
  }
});
</script>

### 📝 **Solución Paso a Paso**

**Paso 1: Calcular las componentes de velocidad**

$$
v_x = 20 \times \cos(30°) = 20 \times 0.866 = \boxed{17.3\,\mathrm{m/s}}
$$

$$
v_y = 20 \times \sin(30°) = 20 \times 0.5 = \boxed{10\,\mathrm{m/s}}
$$

**Paso 2: Tiempo de vuelo** (sube + baja)

$$
t_{\text{subida}} = \frac{v_y}{g} = \frac{10}{10} = 1\,\mathrm{s}
$$

$$
t_{\text{total}} = 2 \times 1 = \boxed{2\,\mathrm{s}}
$$

**Paso 3: Alcance horizontal** (MRU en x)

$$
x = v_x \cdot t = 17.3 \times 2 = \boxed{34.6\,\mathrm{m}}
$$

> ✅ El balón vuela durante **2 segundos** y alcanza **34.6 metros**.

---

## ⚙️ **Ejemplo 2 — Cañón de confeti**

Un cañón de confeti dispara a **$30°$** con velocidad de **$25\,\mathrm{m/s}$**. ¿Qué altura máxima alcanza?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-confeti" width="550" height="160" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-confeti')) {
    var canvas = document.getElementById('roughjs-confeti');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Suelo
    rc.line(30, 140, 500, 140, { stroke: '#65a30d', strokeWidth: 3, roughness: 0.8 });
    
    // Cañón
    rc.rectangle(40, 110, 50, 30, { fill: '#64748b', fillStyle: 'solid', stroke: '#1e293b', roughness: 0.6 });
    rc.ellipse(85, 125, 25, 15, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
    
    // Trayectoria
    ctx.beginPath();
    ctx.moveTo(95, 115);
    ctx.quadraticCurveTo(240, -30, 400, 130);
    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 2;
    ctx.setLineDash([5, 3]);
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Confeti en altura máxima
    rc.circle(240, 30, 8, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(230, 40, 5, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.4 });
    rc.circle(250, 40, 5, { fill: '#22c55e', fillStyle: 'solid', roughness: 0.4 });
    
    // Panel de datos
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Datos:', 350, 40);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• v₀ = 25 m/s', 350, 60);
    ctx.fillText('• θ = 30°', 350, 78);
    ctx.fillText('• vᵧ = 25 × 0.5 = 12.5 m/s', 350, 96);
    
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('Hallar: h_máx = ?', 350, 120);
    
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('Altura máxima', 210, 18);
  }
});
</script>

### 📝 **Solución Paso a Paso**

**La altura máxima solo depende de la componente vertical:**

$$
v_y = 25 \times \sin(30°) = 25 \times 0.5 = 12.5\,\mathrm{m/s}
$$

$$
h_{\max} = \frac{v_y^2}{2g} = \frac{12.5^2}{2 \times 10} = \frac{156.25}{20} = \boxed{7.8\,\mathrm{m}}
$$

> ✅ El confeti alcanza una altura máxima de **7.8 metros**.

---

## ⚙️ **Ejemplo 3 — Baloncesto: Tiro al aro**

Un jugador lanza un balón con **$v_0 = 15\,\mathrm{m/s}$** a **$45°$**. ¿A qué distancia horizontal cae el balón?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-basket" width="550" height="160" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-basket')) {
    var canvas = document.getElementById('roughjs-basket');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Cancha
    rc.line(30, 140, 520, 140, { stroke: '#f59e0b', strokeWidth: 3, roughness: 0.8 });
    
    // Jugador
    rc.circle(60, 115, 15, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.6 });
    rc.rectangle(52, 130, 16, 10, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.4 });
    
    // Balón
    rc.circle(90, 100, 10, { fill: '#f97316', fillStyle: 'solid', stroke: '#ea580c', roughness: 0.5 });
    
    // Trayectoria
    ctx.beginPath();
    ctx.moveTo(90, 100);
    ctx.quadraticCurveTo(240, 10, 400, 100);
    ctx.strokeStyle = '#f97316';
    ctx.lineWidth = 2;
    ctx.setLineDash([5, 3]);
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Balón cayendo
    rc.circle(400, 130, 10, { fill: '#22c55e', fillStyle: 'solid', roughness: 0.5 });
    
    // Panel de datos
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Datos:', 350, 40);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• v₀ = 15 m/s', 350, 60);
    ctx.fillText('• θ = 45°', 350, 78);
    ctx.fillText('• cos(45°) = sen(45°) = 0.707', 350, 96);
    
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('Hallar: alcance = ?', 350, 120);
  }
});
</script>

### 📝 **Solución Paso a Paso**

**Componentes de velocidad:**

$$
v_x = v_y = 15 \times 0.707 = 10.6\,\mathrm{m/s}
$$

**Tiempo de vuelo:**

$$
t = \frac{2 v_y}{g} = \frac{2 \times 10.6}{10} = 2.12\,\mathrm{s}
$$

**Alcance:**

$$
x = v_x \cdot t = 10.6 \times 2.12 = \boxed{22.5\,\mathrm{m}}
$$

> ✅ El balón cae a **22.5 metros** del punto de lanzamiento.

> 💡 **Dato curioso:** Con $\theta = 45°$ se obtiene el **alcance máximo** para una velocidad dada.

---

## 📊 **Gráficas de Velocidad: vₓ vs t y vᵧ vs t**

### **vₓ (componente horizontal) es CONSTANTE**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-vx" style="width: 100%; height: 250px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-vx')) {
    var chart = echarts.init(document.getElementById('echarts-vx'));
    var option = {
      title: { text: 'vₓ vs Tiempo (Constante)', left: 'center', textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '15%', right: '10%', top: '20%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 't (s)', nameLocation: 'middle', nameGap: 25, min: 0, max: 2.5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      yAxis: { type: 'value', name: 'vₓ (m/s)', nameLocation: 'middle', nameGap: 40, min: 0, max: 20, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      series: [{ type: 'line', data: [[0, 17.3], [0.5, 17.3], [1, 17.3], [1.5, 17.3], [2, 17.3]], lineStyle: { width: 3, color: '#22c55e' }, symbol: 'circle', symbolSize: 10, itemStyle: { color: '#22c55e' } }]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

### **vᵧ (componente vertical) DISMINUYE linealmente**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-vy" style="width: 100%; height: 280px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-vy')) {
    var chart = echarts.init(document.getElementById('echarts-vy'));
    var option = {
      title: { text: 'vᵧ vs Tiempo', left: 'center', textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '15%', right: '10%', top: '20%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 't (s)', nameLocation: 'middle', nameGap: 25, min: 0, max: 2.5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      yAxis: { type: 'value', name: 'vᵧ (m/s)', nameLocation: 'middle', nameGap: 40, min: -12, max: 12, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#e2e8f0' } } },
      series: [{
        type: 'line',
        data: [[0, 10], [0.5, 5], [1, 0], [1.5, -5], [2, -10]],
        lineStyle: { width: 3, color: '#ef4444' },
        symbol: 'circle',
        symbolSize: 10,
        itemStyle: { color: '#ef4444' },
        label: { show: true, formatter: function(p) { return p.data[1]; }, position: 'top', fontSize: 10 },
        markPoint: {
          symbol: 'circle',
          symbolSize: 16,
          itemStyle: { color: '#f59e0b' },
          label: { show: true, formatter: 'vᵧ=0', fontSize: 9, fontWeight: 'bold' },
          data: [{ coord: [1, 0] }]
        }
      }]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 Cuando **vᵧ = 0**, el objeto está en la **altura máxima**. Después de eso, vᵧ es negativa (baja).

---

## 📋 **Fórmulas del Movimiento Parabólico**

| Magnitud | Fórmula |
|----------|---------|
| **Altura máxima** | $h_{\max} = \frac{(v_0 \sin\theta)^2}{2g}$ |
| **Tiempo de vuelo** | $t = \frac{2 v_0 \sin\theta}{g}$ |
| **Alcance** | $x = \frac{v_0^2 \sin(2\theta)}{g}$ |

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 1**

Un balón se lanza con $v_0 = 30\,\mathrm{m/s}$ a $60°$. ¿Cuál es la componente horizontal de la velocidad?

<details>
<summary><strong>Ver solución</strong></summary>

$$
v_x = 30 \times \cos(60°) = 30 \times 0.5 = \boxed{15\,\mathrm{m/s}}
$$

</details>

---

### **Ejercicio 2**

Una piedra se lanza con $v_0 = 20\,\mathrm{m/s}$ a $45°$. ¿Qué altura máxima alcanza?

<details>
<summary><strong>Ver solución</strong></summary>

$$
v_y = 20 \times \sin(45°) = 20 \times 0.707 = 14.14\,\mathrm{m/s}
$$

$$
h_{\max} = \frac{v_y^2}{2g} = \frac{14.14^2}{20} = \boxed{10\,\mathrm{m}}
$$

</details>

---

### **Ejercicio 3**

Un objeto se lanza con $v_0 = 40\,\mathrm{m/s}$ a $30°$. ¿Cuánto tiempo permanece en el aire?

<details>
<summary><strong>Ver solución</strong></summary>

$$
v_y = 40 \times \sin(30°) = 40 \times 0.5 = 20\,\mathrm{m/s}
$$

$$
t = \frac{2v_y}{g} = \frac{2 \times 20}{10} = \boxed{4\,\mathrm{s}}
$$

</details>

---

### **Ejercicio 4**

¿A qué ángulo se debe lanzar un objeto para obtener el máximo alcance?

<details>
<summary><strong>Ver solución</strong></summary>

El alcance máximo se obtiene cuando $\sin(2\theta)$ es máximo, es decir, cuando $\sin(2\theta) = 1$.

$$
2\theta = 90° \Rightarrow \theta = \boxed{45°}
$$

</details>
