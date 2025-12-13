# 🚀 **Movimiento Rectilíneo Uniformemente Acelerado (MRUA)**

Hasta ahora habíamos estudiado movimientos donde la velocidad nunca cambiaba (MRU). Pero en la vida real, lo más común es que los objetos arranquen, frenen o aumenten su rapidez.

El **MRUA** es aquel movimiento en línea recta donde la **velocidad cambia** de manera uniforme.

La clave para entender este movimiento es una nueva magnitud física: la **Aceleración ($a$)**.

---

## ⚡ **El Concepto de Aceleración**

La **Aceleración** nos dice **qué tan rápido cambia la velocidad** de un objeto.

* Si la velocidad se mantiene igual, la aceleración es **cero** ($a=0$).
* Si la velocidad aumenta o disminuye, existe una **aceleración** ($a \neq 0$).

### **¿Qué significa la unidad m/s²?**

La unidad de medida es **metros por segundo al cuadrado**. Aunque suena complejo, su significado es muy lógico si lo leemos así: **"Metros por segundo, cada segundo"**.

$$
a = \frac{\Delta v}{t} = \frac{\mathrm{m/s}}{\mathrm{s}} = \mathrm{m/s^2}
$$

> **La Regla de Oro:**
> Si un objeto tiene una aceleración de **$2\,\mathrm{m/s^2}$**, significa que su velocidad **aumenta en $2\,\mathrm{m/s}$ por cada segundo que pasa.**

---

## ✨ **Características del MRUA**

1.  **Trayectoria Rectilínea:** El objeto se mueve siempre en línea recta.
2.  **Velocidad Variable:** La velocidad no es fija; cambia instante a instante.
3.  **Aceleración Constante:** El ritmo al que cambia la velocidad es siempre el mismo (no cambia de golpe).

---

## ⚙️ **Ejercicio 1 — El Arranque de una Moto**

Una motocicleta está detenida frente a un semáforo en rojo. Cuando cambia a verde, el conductor acelera con $a = 5\,\mathrm{m/s^2}$ durante 4 segundos.

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-moto-sit" width="600" height="110" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-moto-sit')) {
    var canvas = document.getElementById('roughjs-moto-sit');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Carretera
    rc.line(30, 60, 570, 60, { stroke: '#64748b', strokeWidth: 2, roughness: 0.8 });
    
    // Semáforo (poste y círculos)
    rc.rectangle(45, 15, 25, 40, { fill: '#1f2937', fillStyle: 'solid', stroke: '#1f2937', roughness: 0.6 });
    rc.circle(57, 25, 10, { fill: '#22c55e', fillStyle: 'solid', stroke: '#22c55e', roughness: 0.5 });
    rc.rectangle(55, 55, 5, 20, { fill: '#64748b', fillStyle: 'solid', stroke: '#64748b', roughness: 0.4 });
    
    // Moto (en el inicio)
    rc.circle(90, 55, 14, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#3b82f6', roughness: 0.8 });
    
    // Flecha de movimiento (acelerando)
    rc.line(110, 50, 450, 50, { stroke: '#3b82f6', strokeWidth: 3, roughness: 1.3 });
    rc.line(430, 40, 450, 50, { stroke: '#3b82f6', strokeWidth: 2, roughness: 1 });
    rc.line(430, 60, 450, 50, { stroke: '#3b82f6', strokeWidth: 2, roughness: 1 });
    
    // Velocidades en puntos intermedios
    rc.circle(200, 50, 6, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(300, 50, 6, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(400, 50, 6, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    
    // Moto al final
    rc.circle(480, 55, 14, { fill: '#22c55e', fillStyle: 'solid', stroke: '#22c55e', roughness: 0.8 });
    
    // Textos
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('🏍️ v₀=0', 70, 90);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('🏍️ v=?', 460, 90);
    
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.textAlign = 'center';
    ctx.fillText('a = 5 m/s² durante t = 4 s', 300, 20);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('La velocidad aumenta cada segundo', 300, 105);
  }
});
</script>

---

### 📊 **Visualización: Velocidad vs Tiempo**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-moto" style="width: 100%; height: 380px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-moto')) {
    var chart = echarts.init(document.getElementById('echarts-moto'));
    var option = {
      title: { text: 'Velocidad vs Tiempo: Moto acelerando', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '12%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 4.5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Velocidad (m/s)', nameLocation: 'middle', nameGap: 50, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 22, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 14, lineStyle: { width: 3, color: '#3b82f6' }, areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: 'rgba(59, 130, 246, 0.3)' }, { offset: 1, color: 'rgba(59, 130, 246, 0.05)' }] } }, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return p.data[1] + ' m/s'; }, position: 'top', fontSize: 11, fontWeight: 'bold' }, data: [[0, 0], [1, 5], [2, 10], [3, 15], [4, 20]] }
      ],
      tooltip: { trigger: 'axis', formatter: 't = {b} s<br/>v = {c} m/s' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 El gráfico muestra cómo la velocidad aumenta **+5 m/s cada segundo** (pendiente constante = aceleración constante).

### **✅ Análisis**

$a = 5\,\mathrm{m/s^2}$ significa: **"Cada segundo, la moto suma 5 m/s a su velocidad"**.

| Tiempo | Operación | Velocidad |
|--------|-----------|-----------|
| $0\,\mathrm{s}$ | — | $0\,\mathrm{m/s}$ |
| $1\,\mathrm{s}$ | $0 + 5$ | $5\,\mathrm{m/s}$ |
| $2\,\mathrm{s}$ | $5 + 5$ | $10\,\mathrm{m/s}$ |
| $3\,\mathrm{s}$ | $10 + 5$ | $15\,\mathrm{m/s}$ |
| $4\,\mathrm{s}$ | $15 + 5$ | $\boxed{20\,\mathrm{m/s}}$ |

---

## ⚙️ **Ejercicio 2 — Caída Libre (La Gravedad)**

Un estudiante deja caer una piedra desde la azotea de un edificio alto. La **Caída Libre** es MRUA donde la aceleración es la **Gravedad**: $g = 9.8\,\mathrm{m/s^2}$.

### 🎯 **Representación de la situación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-caida-sit" width="600" height="150" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-caida-sit')) {
    var canvas = document.getElementById('roughjs-caida-sit');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Edificio
    rc.rectangle(50, 20, 80, 120, { fill: '#cbd5e1', fillStyle: 'solid', stroke: '#64748b', roughness: 0.6 });
    
    // Ventanas del edificio
    for (var row = 0; row < 3; row++) {
      for (var col = 0; col < 2; col++) {
        rc.rectangle(60 + col * 35, 35 + row * 35, 20, 20, { fill: '#93c5fd', fillStyle: 'solid', stroke: '#3b82f6', roughness: 0.4 });
      }
    }
    
    // Azotea
    rc.line(45, 20, 135, 20, { stroke: '#475569', strokeWidth: 3, roughness: 0.5 });
    
    // Persona en la azotea
    rc.circle(115, 15, 8, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.6 });
    
    // Piedra inicial
    rc.circle(160, 20, 10, { fill: '#ef4444', fillStyle: 'solid', stroke: '#ef4444', roughness: 0.8 });
    
    // Flecha de caída (hacia abajo)
    rc.line(160, 35, 160, 130, { stroke: '#ef4444', strokeWidth: 3, roughness: 1.2 });
    rc.line(150, 115, 160, 130, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.8 });
    rc.line(170, 115, 160, 130, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.8 });
    
    // Marcas de velocidad creciente
    rc.circle(160, 50, 5, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(160, 75, 5, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(160, 100, 5, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    
    // Suelo
    rc.line(30, 140, 200, 140, { stroke: '#65a30d', strokeWidth: 3, roughness: 0.8 });
    
    // Textos - sección derecha
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('g = 9.8 m/s²', 220, 40);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('v₀ = 0 (se suelta)', 220, 60);
    ctx.fillText('t = 1s → v = 9.8 m/s', 220, 80);
    ctx.fillText('t = 2s → v = 19.6 m/s', 220, 100);
    ctx.fillText('t = 3s → v = 29.4 m/s', 220, 120);
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('⬇️ La velocidad aumenta', 350, 70);
    ctx.fillText('cada segundo por la gravedad', 350, 90);
  }
});
</script>

---

### 📊 **Visualización: Velocidad vs Tiempo**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-caida" style="width: 100%; height: 380px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-caida')) {
    var chart = echarts.init(document.getElementById('echarts-caida'));
    var option = {
      title: { text: 'Velocidad vs Tiempo: Caída Libre', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '12%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Tiempo (s)', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 3.5, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      yAxis: { type: 'value', name: 'Velocidad (m/s)', nameLocation: 'middle', nameGap: 50, nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' }, min: 0, max: 32, axisLine: { lineStyle: { color: '#64748b' } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } } },
      series: [
        { type: 'line', smooth: false, symbol: 'circle', symbolSize: 14, lineStyle: { width: 3, color: '#ef4444' }, areaStyle: { color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1, colorStops: [{ offset: 0, color: 'rgba(239, 68, 68, 0.3)' }, { offset: 1, color: 'rgba(239, 68, 68, 0.05)' }] } }, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return p.data[1] + ' m/s'; }, position: 'top', fontSize: 11, fontWeight: 'bold' }, data: [[0, 0], [1, 9.8], [2, 19.6], [3, 29.4]] }
      ],
      tooltip: { trigger: 'axis', formatter: 't = {b} s<br/>v = {c} m/s' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 La gravedad actúa como una "tasa de recarga" constante de velocidad: **+9.8 m/s cada segundo**.

### **✅ Análisis**

$g = 9.8\,\mathrm{m/s^2}$ significa: **"Cada segundo, la piedra suma 9.8 m/s a su velocidad"**.

| Tiempo | Operación | Velocidad |
|--------|-----------|-----------|
| $0\,\mathrm{s}$ | Se suelta | $0\,\mathrm{m/s}$ |
| $1\,\mathrm{s}$ | $0 + 9.8$ | $9.8\,\mathrm{m/s}$ |
| $2\,\mathrm{s}$ | $9.8 + 9.8$ | $19.6\,\mathrm{m/s}$ |
| $3\,\mathrm{s}$ | $19.6 + 9.8$ | $\boxed{29.4\,\mathrm{m/s}}$ |

> 💡 Sin usar fórmulas complejas, sabemos que a los 3 segundos la piedra viaja a 29.4 m/s. La caída libre es simplemente un MRUA donde la aceleración está definida por la naturaleza.

---

## 📝 **Ejercicios de Práctica**

### **Ejercicio 3 — Auto deportivo acelerando**

Un auto deportivo parte del reposo y acelera a $8\,\mathrm{m/s^2}$ durante $5$ segundos. ¿Cuál es su velocidad final?

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-deportivo" width="600" height="100" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-deportivo')) {
    var canvas = document.getElementById('roughjs-deportivo');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Carretera
    rc.line(30, 60, 570, 60, { stroke: '#64748b', strokeWidth: 2, roughness: 0.8 });
    
    // Auto inicial
    rc.rectangle(50, 35, 60, 30, { fill: '#ef4444', fillStyle: 'solid', stroke: '#b91c1c', roughness: 0.8 });
    rc.circle(65, 68, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(95, 68, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
    
    // Flechas crecientes
    rc.line(120, 45, 180, 45, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    rc.line(200, 45, 280, 45, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    rc.line(300, 45, 400, 45, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
    rc.line(390, 38, 400, 45, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    rc.line(390, 52, 400, 45, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    
    // Auto final (en movimiento)
    rc.rectangle(480, 35, 60, 30, { fill: '#22c55e', fillStyle: 'solid', stroke: '#16a34a', roughness: 0.8 });
    rc.circle(495, 68, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(525, 68, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
    
    // Etiquetas
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.textAlign = 'center';
    ctx.fillText('v₀ = 0', 80, 90);
    
    ctx.fillStyle = '#22c55e';
    ctx.fillText('v = ?', 510, 90);
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('a = 8 m/s² durante t = 5 s', 300, 25);
  }
});
</script>

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:**
- $v_0 = 0\,\mathrm{m/s}$ (parte del reposo)
- $a = 8\,\mathrm{m/s^2}$
- $t = 5\,\mathrm{s}$

**Análisis paso a paso:**

| Tiempo | Velocidad |
|--------|-----------|
| $0\,\mathrm{s}$ | $0\,\mathrm{m/s}$ |
| $1\,\mathrm{s}$ | $8\,\mathrm{m/s}$ |
| $2\,\mathrm{s}$ | $16\,\mathrm{m/s}$ |
| $3\,\mathrm{s}$ | $24\,\mathrm{m/s}$ |
| $4\,\mathrm{s}$ | $32\,\mathrm{m/s}$ |
| $5\,\mathrm{s}$ | $\boxed{40\,\mathrm{m/s}}$ |

**O directamente:** $v = a \cdot t = 8 \times 5 = 40\,\mathrm{m/s}$

> El auto alcanza **40 m/s** (144 km/h).

</details>

---

### **Ejercicio 4 — Bicicleta frenando**

Un ciclista viaja a $12\,\mathrm{m/s}$ y frena con una desaceleración de $3\,\mathrm{m/s^2}$. ¿Cuántos segundos tarda en detenerse?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:**
- $v_0 = 12\,\mathrm{m/s}$
- $v_f = 0\,\mathrm{m/s}$ (se detiene)
- $a = -3\,\mathrm{m/s^2}$ (desaceleración, por eso negativa)

**Análisis:** Cada segundo pierde 3 m/s de velocidad.

| Tiempo | Velocidad |
|--------|-----------|
| $0\,\mathrm{s}$ | $12\,\mathrm{m/s}$ |
| $1\,\mathrm{s}$ | $9\,\mathrm{m/s}$ |
| $2\,\mathrm{s}$ | $6\,\mathrm{m/s}$ |
| $3\,\mathrm{s}$ | $3\,\mathrm{m/s}$ |
| $4\,\mathrm{s}$ | $\boxed{0\,\mathrm{m/s}}$ |

> Tarda **4 segundos** en detenerse.

</details>

---

### **Ejercicio 5 — Cohete despegando**

Un cohete modelo despega desde el suelo con una aceleración de $15\,\mathrm{m/s^2}$. ¿Qué velocidad tendrá después de 6 segundos?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:**
- $v_0 = 0\,\mathrm{m/s}$ (parte del reposo)
- $a = 15\,\mathrm{m/s^2}$
- $t = 6\,\mathrm{s}$

**Cálculo:**

Cada segundo el cohete suma 15 m/s a su velocidad:

$$
v = a \cdot t = 15\,\mathrm{m/s^2} \times 6\,\mathrm{s} = \boxed{90\,\mathrm{m/s}}
$$

> El cohete viajará a **90 m/s** (324 km/h) después de 6 segundos.

</details>

---

### **Ejercicio 6 — Lanzamiento vertical hacia arriba**

Una pelota se lanza hacia arriba con una velocidad inicial de $30\,\mathrm{m/s}$. Si la gravedad la desacelera a $10\,\mathrm{m/s^2}$, ¿cuántos segundos tardará en alcanzar su punto más alto (donde $v = 0$)?

<details>
<summary><strong>Ver solución</strong></summary>

**Datos:**
- $v_0 = 30\,\mathrm{m/s}$ (hacia arriba)
- $v_f = 0\,\mathrm{m/s}$ (en el punto más alto)
- $a = -10\,\mathrm{m/s^2}$ (la gravedad desacelera el ascenso)

**Análisis:** Cada segundo pierde 10 m/s de velocidad.

| Tiempo | Velocidad |
|--------|-----------|
| $0\,\mathrm{s}$ | $30\,\mathrm{m/s}$ |
| $1\,\mathrm{s}$ | $20\,\mathrm{m/s}$ |
| $2\,\mathrm{s}$ | $10\,\mathrm{m/s}$ |
| $3\,\mathrm{s}$ | $\boxed{0\,\mathrm{m/s}}$ |

> La pelota alcanza su punto más alto a los **3 segundos** después del lanzamiento.

</details>