# Concepto de Pendiente

¿Por qué algunas calles son más empinadas que otras? ¿Cómo medimos qué tan "inclinada" está una rampa o una escalera? La respuesta está en un concepto fundamental de la geometría analítica: la **pendiente**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la pendiente de una recta
- Qué nos indica su valor
- Los casos especiales de pendiente

---

## 📖 Lo Esencial de la Pendiente

| Pendiente $m$ | Tipo de recta | Descripción |
|---------------|---------------|-------------|
| $m > 0$ | Ascendente ↗ | Sube de izquierda a derecha |
| $m < 0$ | Descendente ↘ | Baja de izquierda a derecha |
| $m = 0$ | Horizontal → | Paralela al eje X |
| $m$ no existe | Vertical ↑ | Paralela al eje Y |
| $\|m\| > 1$ | Empinada | Más vertical que horizontal |
| $\|m\| < 1$ | Suave | Más horizontal que vertical |
| $\|m\| = 1$ | 45° | Igual de inclinada |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Tipos de pendiente</strong>
  </div>
  <div id="echarts-pendiente-tipos" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-pendiente-tipos')) {
    var chart = echarts.init(document.getElementById('echarts-pendiente-tipos'));
    
    // Generar datos para cada tipo de pendiente
    var positiva = [], negativa = [], horizontal = [];
    for (var x = -5; x <= 5; x += 0.5) {
      positiva.push([x, 2*x]);      // m = 2 (positiva)
      negativa.push([x, -1.5*x]);   // m = -1.5 (negativa)
      horizontal.push([x, 2]);      // m = 0 (horizontal)
    }
    
    var option = {
      animation: true,
      animationDuration: 1000,
      grid: { 
        left: '12%', right: '8%', top: '15%', bottom: '18%',
        show: true, borderColor: '#cbd5e1'
      },
      legend: {
        data: ['m = 2 (positiva ↗)', 'm = -1.5 (negativa ↘)', 'm = 0 (horizontal →)'],
        top: 5,
        textStyle: { fontSize: 11 }
      },
      xAxis: {
        type: 'value',
        name: 'x',
        nameLocation: 'middle',
        nameGap: 28,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: -5, max: 5,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } }
      },
      yAxis: {
        type: 'value',
        name: 'y',
        nameLocation: 'middle',
        nameGap: 35,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: -8, max: 10,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } }
      },
      series: [
        {
          name: 'm = 2 (positiva ↗)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#22c55e' },
          itemStyle: { color: '#22c55e' },
          data: positiva
        },
        {
          name: 'm = -1.5 (negativa ↘)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#ef4444' },
          itemStyle: { color: '#ef4444' },
          data: negativa
        },
        {
          name: 'm = 0 (horizontal →)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#3b82f6' },
          itemStyle: { color: '#3b82f6' },
          data: horizontal
        }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **Observa:** La recta verde "sube" (pendiente positiva), la roja "baja" (negativa) y la azul es horizontal (pendiente cero).

---

## 📖 ¿Qué es la Pendiente?

> La **pendiente** de una recta mide su **inclinación** respecto a la horizontal. Nos dice cuánto "sube" o "baja" la recta por cada unidad que avanzamos hacia la derecha.

Matemáticamente:

$$
m = \frac{\text{cambio vertical}}{\text{cambio horizontal}} = \frac{\Delta y}{\Delta x} = \frac{\text{subida}}{\text{avance}}
$$

### La Pendiente en la Vida Real

La pendiente está en todas partes:

| Situación | Interpretación de la pendiente |
|-----------|-------------------------------|
| Carretera | El porcentaje de inclinación |
| Escalera | Relación altura/profundidad de los escalones |
| Rampa de silla de ruedas | Qué tan empinada es |
| Techo | La inclinación para que escurra el agua |
| Gráfica de velocidad | La aceleración |

> 💡 Cuando ves un letrero que dice "pendiente del 10%", significa que por cada 100 metros horizontales, subes 10 metros verticalmente.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Concepto de pendiente: subida/avance</strong>
  </div>
  <div id="echarts-pendiente-concepto" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-pendiente-concepto')) {
    var chart = echarts.init(document.getElementById('echarts-pendiente-concepto'));
    
    // Recta con m = 2 pasando por origen
    var recta = [];
    for (var x = -1; x <= 4; x += 0.3) {
      recta.push([x, 2*x]);
    }
    
    var option = {
      animation: true,
      animationDuration: 1000,
      title: {
        text: 'Pendiente m = 2',
        subtext: 'Por cada 1 de avance, sube 2',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' },
        subtextStyle: { fontSize: 12, color: '#3b82f6' }
      },
      grid: { 
        left: '12%', right: '8%', top: '18%', bottom: '15%',
        show: true, borderColor: '#cbd5e1'
      },
      xAxis: {
        type: 'value',
        name: 'x',
        nameLocation: 'middle',
        nameGap: 28,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: -1, max: 5,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } }
      },
      yAxis: {
        type: 'value',
        name: 'y',
        nameLocation: 'middle',
        nameGap: 35,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: -1, max: 9,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } }
      },
      series: [
        {
          name: 'f(x) = 2x',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#3b82f6' },
          itemStyle: { color: '#3b82f6' },
          data: recta
        },
        {
          name: 'Puntos',
          type: 'scatter',
          symbolSize: 12,
          itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 },
          label: {
            show: true,
            formatter: function(p) { return '(' + p.data[0] + ', ' + p.data[1] + ')'; },
            position: 'top',
            fontSize: 11,
            fontWeight: 'bold',
            color: '#1e293b'
          },
          data: [[1, 2], [2, 4], [3, 6]]
        },
        {
          name: 'Avance (Δx)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#22c55e', type: 'solid' },
          data: [[1, 2], [2, 2]]
        },
        {
          name: 'Subida (Δy)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#f97316', type: 'solid' },
          data: [[2, 2], [2, 4]]
        }
      ],
      graphic: [
        {
          type: 'text',
          left: '55%',
          top: '55%',
          style: {
            text: 'Δx = 1 (avance)',
            fontSize: 12,
            fontWeight: 'bold',
            fill: '#22c55e'
          }
        },
        {
          type: 'text',
          left: '60%',
          top: '42%',
          style: {
            text: 'Δy = 2 (subida)',
            fontSize: 12,
            fontWeight: 'bold',
            fill: '#f97316'
          }
        },
        {
          type: 'text',
          left: '62%',
          top: '72%',
          style: {
            text: 'm = Δy/Δx = 2/1 = 2',
            fontSize: 13,
            fontWeight: 'bold',
            fill: '#3b82f6'
          }
        }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **Observa el triángulo:** La línea verde es el "avance" ($\Delta x = 1$) y la naranja es la "subida" ($\Delta y = 2$). La pendiente es $m = \frac{2}{1} = 2$.

---

## 📖 Interpretación del Signo de la Pendiente

El **signo** de la pendiente nos dice la dirección:

### Pendiente Positiva ($m > 0$)

La recta **sube** de izquierda a derecha.

**Ejemplo:** Si $m = 2$, por cada unidad que avanzamos a la derecha, subimos 2 unidades.

### Pendiente Negativa ($m < 0$)

La recta **baja** de izquierda a derecha.

**Ejemplo:** Si $m = -3$, por cada unidad que avanzamos a la derecha, bajamos 3 unidades.

### Pendiente Cero ($m = 0$)

La recta es **horizontal**, no sube ni baja.

Todas las rectas horizontales tienen pendiente $m = 0$.

### Pendiente No Definida (o infinita)

Las rectas **verticales** tienen pendiente **indefinida** porque el cambio horizontal es cero, y no podemos dividir entre cero.

---

## 📖 Interpretación del Valor Absoluto

El **valor absoluto** de la pendiente nos dice qué tan empinada es la recta:

| Valor de $\lvert m \rvert$ | Interpretación                   |
|--------------------------|-----------------------------------|
| $\lvert m \rvert < 1$    | Recta "suave", más horizontal     |
| $\lvert m \rvert = 1$    | Recta a 45°                       |
| $\lvert m \rvert > 1$    | Recta "empinada", más vertical    |

### ⚙️ Ejemplo 1: Comparar pendientes

¿Cuál recta es más empinada, una con $m = 2$ o una con $m = -5$?

**Análisis:**
- $|m_1| = |2| = 2$
- $|m_2| = |-5| = 5$

Como $5 > 2$, la recta con pendiente $m = -5$ es **más empinada**.

> 💡 El signo indica la dirección (sube o baja), pero el valor absoluto indica la inclinación.

### ⚙️ Ejemplo 2: Describir la pendiente

Describe qué tipo de recta tiene pendiente $m = -0.5$:

**Análisis:**
- $m < 0$ → La recta es **descendente** (baja de izquierda a derecha)
- $|m| = 0.5 < 1$ → La recta es **suave** (más horizontal que vertical)

**Respuesta:** Es una recta descendente con inclinación suave.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Comparación de pendientes por valor absoluto</strong>
  </div>
  <div id="echarts-pendiente-absoluto" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-pendiente-absoluto')) {
    var chart = echarts.init(document.getElementById('echarts-pendiente-absoluto'));
    
    // Generar datos para diferentes valores absolutos
    var suave = [], media = [], empinada = [];
    for (var x = -4; x <= 4; x += 0.3) {
      suave.push([x, 0.3*x]);      // |m| = 0.3 (suave)
      media.push([x, x]);          // |m| = 1 (45°)
      empinada.push([x, 3*x]);     // |m| = 3 (empinada)
    }
    
    var option = {
      animation: true,
      animationDuration: 1000,
      grid: { 
        left: '12%', right: '8%', top: '15%', bottom: '18%',
        show: true, borderColor: '#cbd5e1'
      },
      legend: {
        data: ['|m| = 0.3 (suave)', '|m| = 1 (45°)', '|m| = 3 (empinada)'],
        top: 5,
        textStyle: { fontSize: 11 }
      },
      xAxis: {
        type: 'value',
        name: 'x',
        nameLocation: 'middle',
        nameGap: 28,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: -4, max: 4,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } }
      },
      yAxis: {
        type: 'value',
        name: 'y',
        nameLocation: 'middle',
        nameGap: 35,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: -6, max: 6,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } }
      },
      series: [
        {
          name: '|m| = 0.3 (suave)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#22c55e' },
          itemStyle: { color: '#22c55e' },
          data: suave
        },
        {
          name: '|m| = 1 (45°)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#f59e0b' },
          itemStyle: { color: '#f59e0b' },
          data: media
        },
        {
          name: '|m| = 3 (empinada)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#ef4444' },
          itemStyle: { color: '#ef4444' },
          data: empinada
        }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **Observa:** Mientras mayor sea $|m|$, más "vertical" se ve la recta. La recta naranja ($m=1$) forma exactamente 45° con el eje X.

---

## 📖 Casos Especiales: Rectas Horizontales y Verticales

### Rectas Horizontales

Una recta horizontal tiene ecuación $y = k$ (donde $k$ es constante).

- Todos sus puntos tienen la misma ordenada
- Cambio vertical: $\Delta y = 0$
- Pendiente: $m = \frac{0}{\Delta x} = 0$

**Ejemplos:** $y = 3$, $y = -2$, $y = 0$ (el eje X)

### Rectas Verticales

Una recta vertical tiene ecuación $x = k$ (donde $k$ es constante).

- Todos sus puntos tienen la misma abscisa
- Cambio horizontal: $\Delta x = 0$
- Pendiente: $m = \frac{\Delta y}{0}$ → **No definida**

**Ejemplos:** $x = 4$, $x = -1$, $x = 0$ (el eje Y)

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Rectas horizontales y verticales</strong>
  </div>
  <div id="echarts-pendiente-especiales" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-pendiente-especiales')) {
    var chart = echarts.init(document.getElementById('echarts-pendiente-especiales'));
    
    // Rectas horizontales y verticales
    var h1 = [], h2 = [], h3 = [];
    for (var x = -5; x <= 5; x += 0.5) {
      h1.push([x, 3]);    // y = 3
      h2.push([x, 0]);    // y = 0 (eje X)
      h3.push([x, -2]);   // y = -2
    }
    
    // Las verticales se hacen con markLine
    var option = {
      animation: true,
      animationDuration: 1000,
      grid: { 
        left: '12%', right: '8%', top: '12%', bottom: '18%',
        show: true, borderColor: '#cbd5e1'
      },
      legend: {
        data: ['y = 3 (m = 0)', 'y = 0 (m = 0)', 'y = -2 (m = 0)'],
        top: 5,
        textStyle: { fontSize: 10 }
      },
      xAxis: {
        type: 'value',
        name: 'x',
        nameLocation: 'middle',
        nameGap: 28,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: -5, max: 5,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } }
      },
      yAxis: {
        type: 'value',
        name: 'y',
        nameLocation: 'middle',
        nameGap: 35,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: -4, max: 5,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } }
      },
      series: [
        {
          name: 'y = 3 (m = 0)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#3b82f6' },
          itemStyle: { color: '#3b82f6' },
          data: h1
        },
        {
          name: 'y = 0 (m = 0)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#22c55e' },
          itemStyle: { color: '#22c55e' },
          data: h2
        },
        {
          name: 'y = -2 (m = 0)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#f59e0b' },
          itemStyle: { color: '#f59e0b' },
          data: h3
        },
        {
          name: 'x = 2 (m indefinida)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#ef4444' },
          itemStyle: { color: '#ef4444' },
          markLine: {
            symbol: 'none',
            lineStyle: { color: '#ef4444', width: 3, type: 'solid' },
            data: [{ xAxis: 2 }],
            label: { 
              show: true, 
              formatter: 'x = 2',
              position: 'end',
              fontSize: 11,
              fontWeight: 'bold'
            }
          },
          data: []
        },
        {
          name: 'x = -3 (m indefinida)',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#a855f7' },
          itemStyle: { color: '#a855f7' },
          markLine: {
            symbol: 'none',
            lineStyle: { color: '#a855f7', width: 3, type: 'solid' },
            data: [{ xAxis: -3 }],
            label: { 
              show: true, 
              formatter: 'x = -3',
              position: 'end',
              fontSize: 11,
              fontWeight: 'bold'
            }
          },
          data: []
        }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **Observa:** Las rectas horizontales (azul, verde, naranja) tienen $m = 0$. Las rectas verticales (roja, morada) tienen pendiente **indefinida**.

---

## 🔑 Resumen

| Concepto | Significado |
|----------|-------------|
| **Pendiente** | Mide la inclinación de una recta |
| **$m > 0$** | Recta ascendente |
| **$m < 0$** | Recta descendente |
| **$m = 0$** | Recta horizontal |
| **$m$ indefinida** | Recta vertical |
| **$\|m\|$ grande** | Más empinada |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Clasifica cada recta según su pendiente:
a) $m = 4$
b) $m = -1$
c) $m = 0$
d) $m = \frac{1}{3}$

<details>
<summary>Ver solución</summary>

a) $m = 4 > 0$ → **Ascendente, empinada** (sube, $|m| > 1$)
b) $m = -1 < 0$ → **Descendente, 45°** (baja, $|m| = 1$)
c) $m = 0$ → **Horizontal**
d) $m = \frac{1}{3} > 0$ → **Ascendente, suave** (sube, $|m| < 1$)

</details>

### Ejercicio 2
Una rampa tiene pendiente $m = 0.08$. ¿Cuántos metros sube la rampa por cada 10 metros horizontales?

<details>
<summary>Ver solución</summary>

La pendiente es:
$$
m = \frac{\text{subida}}{\text{avance}} = 0.08
$$

Si el avance es 10 metros:
$$
\text{subida} = m \times \text{avance} = 0.08 \times 10 = 0.8 \text{ metros}
$$

**Respuesta:** La rampa sube 0.8 metros (80 cm) por cada 10 metros horizontales.

</details>

### Ejercicio 3
¿Cuál recta es más empinada?
- Recta A: $m = -3$
- Recta B: $m = 2.5$

<details>
<summary>Ver solución</summary>

Comparamos los valores absolutos:
- $|m_A| = |-3| = 3$
- $|m_B| = |2.5| = 2.5$

Como $3 > 2.5$, la **Recta A es más empinada**.

> Nota: La recta A baja (pendiente negativa) y la B sube (positiva), pero A es más inclinada.

</details>

### Ejercicio 4
¿Qué tipo de recta tiene pendiente indefinida? Da un ejemplo de su ecuación.

<details>
<summary>Ver solución</summary>

Las rectas **verticales** tienen pendiente indefinida.

Ejemplos: $x = 5$, $x = -3$, $x = 0$

Estas rectas no pueden escribirse en la forma $y = mx + b$ porque para un mismo valor de $x$, hay infinitos valores de $y$.

</details>

### Ejercicio 5
Un techo tiene pendiente $m = 0.4$. Si el techo tiene 6 metros de base horizontal, ¿cuál es la altura máxima del techo?

<details>
<summary>Ver solución</summary>

$$
\text{altura} = m \times \text{base} = 0.4 \times 6 = 2.4 \text{ metros}
$$

**Respuesta:** La altura máxima del techo es 2.4 metros.

</details>
