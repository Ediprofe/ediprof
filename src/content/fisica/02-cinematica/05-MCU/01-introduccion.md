# 🎡 **Movimiento Circular Uniforme (MCU)**

¿Has visto la rueda de la fortuna girar? ¿O las manecillas de un reloj moviéndose? Estos son ejemplos perfectos del **Movimiento Circular Uniforme**.

---

## 🔄 **¿Qué es el MCU?**

El **Movimiento Circular Uniforme (MCU)** es aquel donde un objeto se mueve en una **trayectoria circular** manteniendo una **rapidez constante**.

Aunque la rapidez no cambia, la **dirección** de la velocidad sí cambia constantemente (siempre es tangente al círculo). Por eso existe una aceleración especial llamada **aceleración centrípeta**.

### **Características del MCU:**

| Característica | Descripción |
|----------------|-------------|
| **Trayectoria** | Circular (un círculo) |
| **Rapidez** | Constante |
| **Dirección** | Cambia continuamente |
| **Aceleración** | Centrípeta (hacia el centro) |

---

## 🔗 **Deducción de las Fórmulas del MCU**

Las fórmulas del MCU se derivan de **conceptos geométricos básicos** y de la relación entre distancia, velocidad y tiempo.

### **Paso 1: Circunferencia de un círculo**

Un objeto que da una vuelta completa recorre la **circunferencia**:

$$
C = 2\pi r
$$

donde $r$ es el radio del círculo.

### **Paso 2: Relación entre período, frecuencia y velocidad**

**Período (T):** tiempo para dar 1 vuelta completa.

**Frecuencia (f):** número de vueltas por segundo.

$$
f = \frac{1}{T} \qquad \text{(son inversos)}
$$

**Velocidad tangencial:** Si recorre $C$ en tiempo $T$:

$$
v = \frac{C}{T} = \frac{2\pi r}{T}
$$

### **Paso 3: Velocidad angular**

El objeto recorre un ángulo de $2\pi$ radianes (360°) en un período $T$:

$$
\omega = \frac{2\pi}{T} = 2\pi f
$$

De aquí podemos relacionar $v$ y $\omega$:

$$
v = \frac{2\pi r}{T} = r \cdot \frac{2\pi}{T} = \boxed{r \cdot \omega}
$$

### **Paso 4: Aceleración centrípeta**

Aunque la **rapidez** es constante, la **dirección** cambia continuamente. Este cambio de dirección produce una aceleración hacia el centro:

$$
a_c = \frac{v^2}{r} = \omega^2 \cdot r
$$

> 💡 **Conclusión:** Todas las fórmulas del MCU se derivan de la geometría del círculo y la definición de velocidad.

### **Resumen de fórmulas derivadas:**

| Fórmula | Deducción |
|---------|-----------|
| $f = \frac{1}{T}$ | Definición (inverso del período) |
| $\omega = \frac{2\pi}{T} = 2\pi f$ | Ángulo por unidad de tiempo |
| $v = \omega r = \frac{2\pi r}{T}$ | Distancia (circunferencia) / tiempo |
| $a_c = \frac{v^2}{r}$ | Cambio de dirección hacia el centro |

---

## 📐 **Las Magnitudes del MCU — ¿Qué significa cada una?**

Antes de usar las fórmulas, entendamos **visualmente** qué representa cada magnitud:

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-magnitudes" width="550" height="220" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-magnitudes')) {
    var canvas = document.getElementById('roughjs-magnitudes');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    var cx = 130, cy = 110, r = 80;
    
    // Círculo (trayectoria)
    rc.circle(cx, cy, r*2, { stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5, fill: 'transparent' });
    
    // Centro
    rc.circle(cx, cy, 8, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.3 });
    
    // Radio
    rc.line(cx, cy, cx + r, cy, { stroke: '#f59e0b', strokeWidth: 2, roughness: 0.5 });
    
    // Objeto en el borde (a la derecha)
    rc.circle(cx + r, cy, 14, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    
    // Vector velocidad (TANGENTE al círculo, hacia arriba)
    rc.line(cx + r, cy, cx + r, cy - 50, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
    rc.line(cx + r - 5, cy - 42, cx + r, cy - 50, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    rc.line(cx + r + 5, cy - 42, cx + r, cy - 50, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    
    // Arco para ángulo θ
    ctx.beginPath();
    ctx.arc(cx, cy, 30, -0.3, 0);
    ctx.strokeStyle = '#a855f7';
    ctx.lineWidth = 2;
    ctx.stroke();
    
    // Etiquetas en el diagrama
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('r (radio)', cx + 20, cy - 8);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('v', cx + r + 10, cy - 25);
    
    ctx.fillStyle = '#a855f7';
    ctx.fillText('θ', cx + 35, cy + 5);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('objeto', cx + r + 5, cy + 25);
    
    // Panel de definiciones
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Definiciones:', 290, 30);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('T = Período:', 290, 55);
    ctx.fillStyle = '#64748b';
    ctx.fillText('tiempo de 1 vuelta completa', 350, 55);
    
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('f = Frecuencia:', 290, 80);
    ctx.fillStyle = '#64748b';
    ctx.fillText('vueltas por segundo', 375, 80);
    
    ctx.fillStyle = '#a855f7';
    ctx.fillText('ω = Vel. angular:', 290, 105);
    ctx.fillStyle = '#64748b';
    ctx.fillText('ángulo por segundo', 385, 105);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('v = Vel. tangencial:', 290, 130);
    ctx.fillStyle = '#64748b';
    ctx.fillText('velocidad lineal', 400, 130);
    
    ctx.fillStyle = '#ef4444';
    ctx.fillText('aᶜ = Acel. centrípeta:', 290, 155);
    ctx.fillStyle = '#64748b';
    ctx.fillText('hacia el centro', 410, 155);
    
    // Nota importante
    ctx.font = 'italic 10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('* v es siempre tangente al círculo', 290, 190);
  }
});
</script>

### **1. Período (T)**

El **período** es el **tiempo que tarda el objeto en dar UNA vuelta completa**.

<div style="background: #eff6ff; border-left: 4px solid #3b82f6; padding: 0.75rem 1rem; margin: 1rem 0; border-radius: 0 8px 8px 0;">
<strong>Ejemplo:</strong> Si la manecilla de un reloj da 1 vuelta en 60 segundos → T = 60 s
</div>

### **2. Frecuencia (f)**

La **frecuencia** es el **número de vueltas que da por segundo**.

$$
f = \frac{1}{T} \qquad \text{(son inversos)}
$$

<div style="background: #fefce8; border-left: 4px solid #f59e0b; padding: 0.75rem 1rem; margin: 1rem 0; border-radius: 0 8px 8px 0;">
<strong>Ejemplo:</strong> Si T = 0.5 s → f = 1/0.5 = 2 Hz (2 vueltas por segundo)
</div>

### **3. Velocidad Angular (ω)**

La **velocidad angular** es el **ángulo que recorre por unidad de tiempo**. Una vuelta completa = $2\pi$ radianes.

$$
\omega = \frac{\theta}{t} = \frac{2\pi}{T} = 2\pi f
$$

<div style="background: #faf5ff; border-left: 4px solid #a855f7; padding: 0.75rem 1rem; margin: 1rem 0; border-radius: 0 8px 8px 0;">
<strong>Ejemplo:</strong> Si da 1 vuelta (2π rad) en 2 segundos → ω = 2π/2 = π rad/s
</div>

### **4. Velocidad Tangencial (v)**

La **velocidad tangencial** es la **velocidad lineal** del objeto. Siempre es **tangente** al círculo (perpendicular al radio).

$$
v = \omega \cdot r = \frac{2\pi r}{T}
$$

<div style="background: #f0fdf4; border-left: 4px solid #22c55e; padding: 0.75rem 1rem; margin: 1rem 0; border-radius: 0 8px 8px 0;">
<strong>Ejemplo:</strong> Si ω = 10 rad/s y r = 0.5 m → v = 10 × 0.5 = 5 m/s
</div>

---

## ⚙️ **Ejemplo 1 — Rueda de bicicleta**

Una rueda de bicicleta tiene un radio de **$0.35\,\mathrm{m}$** y da **2 vueltas por segundo**. Calcular el período, la velocidad angular y la velocidad tangencial.

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-rueda" width="500" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-rueda')) {
    var canvas = document.getElementById('roughjs-rueda');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Rueda
    rc.circle(120, 90, 120, { stroke: '#1e293b', strokeWidth: 4, roughness: 0.8 });
    
    // Rayos
    for (var i = 0; i < 6; i++) {
      var angle = i * Math.PI / 3;
      var x1 = 120 + Math.cos(angle) * 20;
      var y1 = 90 + Math.sin(angle) * 20;
      var x2 = 120 + Math.cos(angle) * 55;
      var y2 = 90 + Math.sin(angle) * 55;
      rc.line(x1, y1, x2, y2, { stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
    }
    
    // Centro
    rc.circle(120, 90, 20, { fill: '#64748b', fillStyle: 'solid', roughness: 0.5 });
    
    // Punto en el borde
    rc.circle(175, 90, 10, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    
    // Radio
    rc.line(120, 90, 175, 90, { stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5 });
    
    // Vector velocidad
    rc.line(175, 90, 175, 45, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
    rc.line(170, 55, 175, 45, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    rc.line(180, 55, 175, 45, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    
    // Panel de datos
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Datos:', 260, 40);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• r = 0.35 m', 260, 60);
    ctx.fillText('• f = 2 Hz (2 vueltas/s)', 260, 80);
    
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Hallar: T, ω, v', 260, 110);
    
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('r', 145, 85);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('v', 185, 65);
  }
});
</script>

### 📝 **Solución Paso a Paso**

**Paso 1: Período**

$$
T = \frac{1}{f} = \frac{1}{2} = \boxed{0.5\,\mathrm{s}}
$$

**Paso 2: Velocidad Angular**

$$
\omega = 2\pi f = 2\pi \times 2 = 4\pi = \boxed{12.57\,\mathrm{rad/s}}
$$

**Paso 3: Velocidad Tangencial**

$$
v = \omega \cdot r = 12.57 \times 0.35 = \boxed{4.4\,\mathrm{m/s}}
$$

> ✅ Un punto en el borde de la rueda viaja a **4.4 m/s** (15.8 km/h).

---

## ⚙️ **Ejemplo 2 — Segundero de un reloj**

El segundero de un reloj mide **15 cm** de largo. ¿Cuál es la velocidad de la punta del segundero?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-reloj" width="500" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-reloj')) {
    var canvas = document.getElementById('roughjs-reloj');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Reloj
    rc.circle(100, 90, 140, { fill: '#fafafa', fillStyle: 'solid', stroke: '#1e293b', strokeWidth: 3, roughness: 0.5 });
    
    // Marcas de horas
    for (var i = 0; i < 12; i++) {
      var angle = i * Math.PI / 6 - Math.PI / 2;
      var x = 100 + Math.cos(angle) * 60;
      var y = 90 + Math.sin(angle) * 60;
      rc.circle(x, y, 5, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.3 });
    }
    
    // Centro
    rc.circle(100, 90, 8, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.4 });
    
    // Segundero (apuntando hacia arriba)
    rc.line(100, 90, 100, 25, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.3 });
    
    // Punta del segundero
    rc.circle(100, 25, 6, { fill: '#22c55e', fillStyle: 'solid', roughness: 0.4 });
    
    // Panel de datos
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Datos:', 260, 40);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• r = 15 cm = 0.15 m', 260, 60);
    ctx.fillText('• T = 60 s (1 vuelta/minuto)', 260, 80);
    
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('Hallar: v = ?', 260, 110);
  }
});
</script>

### 📝 **Solución Paso a Paso**

**Velocidad Angular:**

$$
\omega = \frac{2\pi}{T} = \frac{2\pi}{60} = \frac{\pi}{30} = 0.105\,\mathrm{rad/s}
$$

**Velocidad Tangencial:**

$$
v = \omega \cdot r = 0.105 \times 0.15 = \boxed{0.0157\,\mathrm{m/s}} = 1.57\,\mathrm{cm/s}
$$

> ✅ La punta del segundero se mueve a **1.57 cm/s** (¡muy lento!).

---

## ⚙️ **Ejemplo 3 — Atleta en pista circular**

Un atleta corre a **$8\,\mathrm{m/s}$** en una pista circular de radio **$25\,\mathrm{m}$**. ¿Cuánto tarda en dar una vuelta?

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-atleta" width="500" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-atleta')) {
    var canvas = document.getElementById('roughjs-atleta');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Pista
    rc.circle(120, 90, 130, { stroke: '#dc2626', strokeWidth: 4, roughness: 0.8, fill: '#fef2f2', fillStyle: 'solid' });
    rc.circle(120, 90, 90, { stroke: '#dc2626', strokeWidth: 2, roughness: 0.6 });
    
    // Centro
    rc.circle(120, 90, 8, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
    
    // Atleta
    rc.circle(180, 65, 12, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    
    // Panel de datos
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Datos:', 280, 40);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• v = 8 m/s', 280, 60);
    ctx.fillText('• r = 25 m', 280, 80);
    
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Hallar: T = ?', 280, 110);
  }
});
</script>

### 📝 **Solución Paso a Paso**

**Circunferencia de la pista:**

$$
C = 2\pi r = 2\pi \times 25 = 157.08\,\mathrm{m}
$$

**Período (tiempo para una vuelta):**

$$
T = \frac{C}{v} = \frac{157.08}{8} = \boxed{19.6\,\mathrm{s}}
$$

> ✅ El atleta tarda casi **20 segundos** en dar una vuelta a la pista.

---

## 🎯 **Aceleración Centrípeta**

Aunque la rapidez es constante, hay una **aceleración** porque la dirección cambia. Esta aceleración siempre apunta **hacia el centro** del círculo.

$$
a_c = \frac{v^2}{r} = \omega^2 \cdot r
$$

### 🎮 **Diagrama Interactivo: Aceleración Centrípeta**

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> Arrastra el punto azul para ver cómo cambian los vectores
  </div>
  <div id="jsxgraph-centripeta" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-centripeta')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-centripeta', {
      boundingbox: [-5, 5, 5, -5],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: {enabled: false},
      zoom: {enabled: false}
    });
    
    var centro = board.create('point', [0, 0], {
      name: 'Centro',
      size: 4,
      fixed: true,
      color: '#1e293b',
      label: {offset: [-40, -15], strokeColor: '#1e293b'}
    });
    
    var circulo = board.create('circle', [centro, 3], {
      strokeColor: '#3b82f6',
      strokeWidth: 2,
      fillColor: 'transparent',
      fixed: true
    });
    
    var punto = board.create('glider', [3, 0, circulo], {
      name: 'Objeto',
      size: 6,
      color: '#3b82f6',
      label: {offset: [10, 10], strokeColor: '#3b82f6'}
    });
    
    var velocidad = board.create('arrow', [punto, function() {
      var x = punto.X();
      var y = punto.Y();
      var r = Math.sqrt(x*x + y*y);
      var vx = -y / r * 1.5;
      var vy = x / r * 1.5;
      return [x + vx, y + vy];
    }], {
      strokeColor: '#22c55e',
      strokeWidth: 3,
      fixed: true
    });
    
    var aceleracion = board.create('arrow', [punto, function() {
      var x = punto.X();
      var y = punto.Y();
      var r = Math.sqrt(x*x + y*y);
      var ax = -x / r * 1.2;
      var ay = -y / r * 1.2;
      return [x + ax, y + ay];
    }], {
      strokeColor: '#ef4444',
      strokeWidth: 3,
      fixed: true
    });
    
    board.create('segment', [centro, punto], {
      strokeColor: '#64748b',
      strokeWidth: 1,
      dash: 2,
      fixed: true
    });
    
    board.create('text', [3.2, 3.5, 'v = velocidad (tangente)'], {fontSize: 11, strokeColor: '#22c55e', fixed: true});
    board.create('text', [3.2, 3, 'aᶜ = aceleración centrípeta'], {fontSize: 11, strokeColor: '#ef4444', fixed: true});
    board.create('text', [-4.8, -4, 'Arrastra el punto azul'], {fontSize: 10, strokeColor: '#64748b', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📋 **Fórmulas del MCU**

| Magnitud | Fórmula |
|----------|---------|
| **Período** | $T = \frac{1}{f}$ |
| **Frecuencia** | $f = \frac{1}{T}$ |
| **Velocidad Angular** | $\omega = 2\pi f = \frac{2\pi}{T}$ |
| **Velocidad Tangencial** | $v = \omega \cdot r$ |
| **Aceleración Centrípeta** | $a_c = \frac{v^2}{r} = \omega^2 r$ |

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 1**

Un ventilador gira a **120 RPM** (revoluciones por minuto). ¿Cuál es su frecuencia en Hz?

<details>
<summary><strong>Ver solución</strong></summary>

$$
f = \frac{120\,\mathrm{RPM}}{60\,\mathrm{s/min}} = \boxed{2\,\mathrm{Hz}}
$$

</details>

---

### **Ejercicio 2**

Un carrusel da una vuelta cada **20 segundos**. ¿Cuál es su velocidad angular?

<details>
<summary><strong>Ver solución</strong></summary>

$$
\omega = \frac{2\pi}{T} = \frac{2\pi}{20} = \boxed{0.314\,\mathrm{rad/s}}
$$

</details>

---

### **Ejercicio 3**

Un auto toma una curva de radio **$50\,\mathrm{m}$** a **$72\,\mathrm{km/h}$** (20 m/s). ¿Cuál es su aceleración centrípeta?

<details>
<summary><strong>Ver solución</strong></summary>

$$
a_c = \frac{v^2}{r} = \frac{20^2}{50} = \frac{400}{50} = \boxed{8\,\mathrm{m/s^2}}
$$

> ¡Es casi igual a la aceleración de la gravedad!

</details>

---

### **Ejercicio 4**

Un punto en el borde de un CD (r = 6 cm) tiene velocidad de **$3\,\mathrm{m/s}$**. ¿Cuál es la velocidad angular del CD?

<details>
<summary><strong>Ver solución</strong></summary>

$$
\omega = \frac{v}{r} = \frac{3}{0.06} = \boxed{50\,\mathrm{rad/s}}
$$

</details>
