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