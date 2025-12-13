# 🚗 **MRU: Introducción**

El **Movimiento Rectilíneo Uniforme (MRU)** es el modelo de movimiento más sencillo de la física. Antes de aprender fórmulas, vamos a entender qué significa realmente.

---

## 📖 **¿Qué es el MRU?**

Un objeto está en MRU cuando cumple **dos condiciones**:

1. **Se mueve en línea recta** (no cambia de dirección).
2. **Mantiene su velocidad constante** (no acelera ni frena).

> 💡 Si la velocidad es constante, significa que la aceleración es **cero** ($a = 0$).

---

## 🧠 **La Idea Clave: Distancias Iguales en Tiempos Iguales**

Piensa en un tren que viaja a **60 km/h** de manera constante:

- En la **primera hora** recorre 60 km.
- En la **segunda hora** recorre otros 60 km.
- En la **tercera hora** recorre otros 60 km más.

¿Ves el patrón? **Siempre avanza lo mismo en cada unidad de tiempo.**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 550px;">
  <canvas id="rough-tren-mru" width="500" height="150" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var canvas = document.getElementById('rough-tren-mru');
  if (!canvas || typeof rough === 'undefined') return;
  
  var rc = rough.canvas(canvas);
  var ctx = canvas.getContext('2d');
  
  // Título
  ctx.font = 'bold 12px Inter, sans-serif';
  ctx.fillStyle = '#1e293b';
  ctx.textAlign = 'center';
  ctx.fillText('Tren a 60 km/h constante', 250, 18);
  
  // Vía del tren
  rc.line(30, 100, 470, 100, { stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
  
  // Marcadores de kilómetros
  var kms = [0, 60, 120, 180];
  var horas = ['0h', '1h', '2h', '3h'];
  
  for (var i = 0; i < kms.length; i++) {
    var x = 50 + i * 130;
    rc.line(x, 95, x, 105, { stroke: '#1e293b', strokeWidth: 2, roughness: 0.3 });
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.textAlign = 'center';
    ctx.fillText(kms[i] + ' km', x, 120);
    ctx.fillText(horas[i], x, 135);
  }
  
  // Tren (en posición km 0)
  rc.rectangle(35, 65, 50, 30, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 0.8 });
  rc.rectangle(35, 85, 50, 12, { fill: '#60a5fa', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 0.6 });
  
  // Flechas de avance iguales
  var colores = ['#22c55e', '#f59e0b', '#a855f7'];
  var textos = ['+60 km', '+60 km', '+60 km'];
  
  for (var j = 0; j < 3; j++) {
    var x1 = 60 + j * 130;
    var x2 = 170 + j * 130;
    
    rc.line(x1, 50, x2, 50, { stroke: colores[j], strokeWidth: 2, roughness: 0.5 });
    rc.line(x2 - 10, 45, x2, 50, { stroke: colores[j], strokeWidth: 2, roughness: 0.5 });
    rc.line(x2 - 10, 55, x2, 50, { stroke: colores[j], strokeWidth: 2, roughness: 0.5 });
    
    ctx.font = 'bold 10px Inter, sans-serif';
    ctx.fillStyle = colores[j];
    ctx.fillText(textos[j], (x1 + x2) / 2, 45);
  }
});
</script>

Esta es la esencia del MRU: **el objeto avanza la misma distancia en cada segundo** (o en cada hora, minuto, etc.).

---

## ⚙️ **Ejercicio 1 — Entendiendo la Velocidad**

Un robot se mueve a **$4\,\mathrm{m/s}$** constante. ¿Qué significa esto en la práctica?

Significa que **por cada segundo**, el robot avanza exactamente **4 metros**:

| Tiempo | Avance en ese segundo | Posición acumulada |
|--------|----------------------|-------------------|
| $t = 0\,\mathrm{s}$ | — | $0\,\mathrm{m}$ (inicio) |
| $t = 1\,\mathrm{s}$ | $+4\,\mathrm{m}$ | $4\,\mathrm{m}$ |
| $t = 2\,\mathrm{s}$ | $+4\,\mathrm{m}$ | $8\,\mathrm{m}$ |
| $t = 3\,\mathrm{s}$ | $+4\,\mathrm{m}$ | $12\,\mathrm{m}$ |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 550px;">
  <canvas id="rough-robot" width="500" height="120" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var canvas = document.getElementById('rough-robot');
  if (!canvas || typeof rough === 'undefined') return;
  
  var rc = rough.canvas(canvas);
  var ctx = canvas.getContext('2d');
  
  // Línea de referencia (piso)
  rc.line(20, 85, 480, 85, { stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
  
  // Marcas de posición
  for (var i = 0; i <= 12; i += 4) {
    var x = 40 + (i / 12) * 400;
    rc.line(x, 80, x, 90, { stroke: '#64748b', strokeWidth: 2, roughness: 0.3 });
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.textAlign = 'center';
    ctx.fillText(i + 'm', x, 105);
  }
  
  // Robot en posición inicial
  rc.rectangle(35, 50, 35, 30, { fill: '#94a3b8', fillStyle: 'solid', stroke: '#475569', roughness: 0.8 });
  rc.circle(42, 80, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
  rc.circle(62, 80, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
  
  // Flechas de 4m cada una
  var colores = ['#22c55e', '#f59e0b', '#a855f7'];
  var posiciones = [40, 173, 306];
  
  for (var j = 0; j < 3; j++) {
    rc.line(posiciones[j] + 30, 55, posiciones[j] + 130, 55, { stroke: colores[j], strokeWidth: 2, roughness: 0.5 });
    rc.line(posiciones[j] + 120, 48, posiciones[j] + 130, 55, { stroke: colores[j], strokeWidth: 2, roughness: 0.5 });
    rc.line(posiciones[j] + 120, 62, posiciones[j] + 130, 55, { stroke: colores[j], strokeWidth: 2, roughness: 0.5 });
    
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = colores[j];
    ctx.fillText('+4m', posiciones[j] + 80, 48);
  }
  
  // Robot en posición final
  rc.rectangle(405, 50, 35, 30, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', roughness: 0.8 });
  rc.circle(412, 80, 12, { fill: '#60a5fa', fillStyle: 'solid', roughness: 0.5 });
  rc.circle(432, 80, 12, { fill: '#60a5fa', fillStyle: 'solid', roughness: 0.5 });
  
  ctx.font = 'bold 10px Inter, sans-serif';
  ctx.fillStyle = '#3b82f6';
  ctx.fillText('12m', 422, 42);
});
</script>

### ✅ **Conclusión del Ejercicio 1**

Si la velocidad es **$4\,\mathrm{m/s}$** y el tiempo es **$3\,\mathrm{s}$**, entonces:

$$
\text{Posición final} = 4\,\mathrm{m/s} \times 3\,\mathrm{s} = 12\,\mathrm{m}
$$

Esto nos da una pista de la **fórmula**: $x = v \cdot t$

---

## 📊 **Visualización: El Gráfico Posición vs Tiempo**

Ahora que entendemos la idea, veamos cómo se ve esto en un **gráfico**:

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
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
      grid: { left: '15%', right: '8%', top: '15%', bottom: '18%', show: true, borderColor: '#cbd5e1' },
      xAxis: {
        type: 'value',
        name: 'Tiempo (s)',
        nameLocation: 'middle',
        nameGap: 30,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: 0, max: 4,
        interval: 1,
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
        interval: 2,
        axisLine: { lineStyle: { color: '#64748b' } },
        splitLine: { show: true, lineStyle: { type: 'solid', color: '#94a3b8', width: 1 } }
      },
      series: [
        {
          name: 'Posición',
          type: 'line',
          smooth: false,
          symbol: 'circle',
          symbolSize: 14,
          lineStyle: { width: 3, color: '#3b82f6' },
          areaStyle: {
            color: { type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
              colorStops: [{ offset: 0, color: 'rgba(59, 130, 246, 0.3)' }, { offset: 1, color: 'rgba(59, 130, 246, 0.05)' }]
            }
          },
          itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 },
          label: { show: true, formatter: function(p) { return p.data[1] + 'm'; }, position: 'top', fontSize: 11, fontWeight: 'bold' },
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

### **¿Qué observas en el gráfico?**

1. **Es una línea recta** → Eso indica velocidad constante (MRU).
2. **La pendiente es siempre igual** → Cada segundo avanza los mismos 4 metros.
3. **El gráfico sube de manera uniforme** → No hay aceleración.

> 💡 **Recuerda:** En MRU, el gráfico posición vs tiempo es **siempre una línea recta**.

---

## ⚙️ **Ejercicio 2 — Calculando la Velocidad**

Un corredor recorre **$20\,\mathrm{m}$** en **$4\,\mathrm{s}$**. ¿Cuál es su velocidad?

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 550px;">
  <canvas id="rough-corredor" width="500" height="100" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var canvas = document.getElementById('rough-corredor');
  if (!canvas || typeof rough === 'undefined') return;
  
  var rc = rough.canvas(canvas);
  var ctx = canvas.getContext('2d');
  
  // Pista
  rc.line(30, 70, 470, 70, { stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
  
  // Corredor inicio
  rc.circle(50, 50, 20, { fill: '#22c55e', fillStyle: 'solid', stroke: '#16a34a', roughness: 0.5 });
  rc.line(50, 60, 50, 68, { stroke: '#16a34a', strokeWidth: 2, roughness: 0.5 });
  
  // Flecha de 20m
  rc.line(70, 45, 420, 45, { stroke: '#3b82f6', strokeWidth: 3, roughness: 0.5 });
  rc.line(410, 38, 420, 45, { stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5 });
  rc.line(410, 52, 420, 45, { stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5 });
  
  ctx.font = 'bold 14px Inter, sans-serif';
  ctx.fillStyle = '#1d4ed8';
  ctx.textAlign = 'center';
  ctx.fillText('← 20 m →', 245, 35);
  
  // Corredor fin
  rc.circle(440, 50, 20, { fill: '#ef4444', fillStyle: 'solid', stroke: '#dc2626', roughness: 0.5 });
  rc.line(440, 60, 440, 68, { stroke: '#dc2626', strokeWidth: 2, roughness: 0.5 });
  
  ctx.font = '11px Inter, sans-serif';
  ctx.fillStyle = '#64748b';
  ctx.fillText('Tiempo: 4 segundos', 245, 90);
});
</script>

### 📝 **Análisis paso a paso**

**Pensamiento:** Si recorrió 20m en 4s, ¿cuántos metros avanzó cada segundo?

$$
\text{Cada segundo avanzó} = \frac{20\,\mathrm{m}}{4\,\mathrm{s}} = 5\,\mathrm{m}
$$

> ✅ **Respuesta:** La velocidad es **$5\,\mathrm{m/s}$**

Esto nos confirma la fórmula: $v = \frac{x}{t}$

---

## 📋 **Resumen: Lo que hemos aprendido**

| Concepto | Explicación |
|----------|-------------|
| **MRU** | Movimiento en línea recta con velocidad constante |
| **Velocidad constante** | Avanza **la misma distancia** en cada segundo |
| **Aceleración** | Es **cero** en MRU |
| **Gráfico x vs t** | Es una **línea recta** |

---

> 💡 **Siguiente lección:** Aprenderemos las fórmulas del MRU y cómo resolver problemas más complejos con posición inicial.