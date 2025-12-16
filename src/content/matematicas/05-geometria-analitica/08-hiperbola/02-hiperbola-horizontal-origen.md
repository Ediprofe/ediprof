# Hipérbola Horizontal con Centro en el Origen

¿Sabías que las señales de GPS que usas en tu celular viajan siguiendo trayectorias hiperbólicas? ¿Y que el sistema de navegación de los barcos funciona calculando intersecciones de hipérbolas? Esta cónica aparece en la tecnología que usamos todos los días.

En esta lección aprenderás a dominar la **hipérbola horizontal** con centro en el origen.

---

## 🎯 ¿Qué vas a aprender?

- Qué forma tiene la ecuación canónica de una hipérbola horizontal
- Cómo identificar sus elementos: vértices, focos, asíntotas
- Cómo graficar una hipérbola paso a paso
- Cómo calcular $c$ usando la relación fundamental

---

## 📋 Lo Esencial de la Hipérbola Horizontal

| Elemento | Fórmula/Valor |
|----------|---------------|
| **Ecuación canónica** | $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ |
| **Eje transversal** | Horizontal (sobre el eje X) |
| **Centro** | $(0, 0)$ |
| **Vértices** | $V_1(-a, 0)$ y $V_2(a, 0)$ |
| **Focos** | $F_1(-c, 0)$ y $F_2(c, 0)$ |
| **Relación fundamental** | $c^2 = a^2 + b^2$ |
| **Asíntotas** | $y = \pm \dfrac{b}{a}x$ |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Hipérbola horizontal: elementos principales</strong>
  </div>
  <div id="echarts-hiperbola-elementos" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-hiperbola-elementos')) {
    var chart = echarts.init(document.getElementById('echarts-hiperbola-elementos'));
    
    // Hipérbola: x²/16 - y²/9 = 1 → a=4, b=3, c=5
    var a = 4, b = 3;
    var c = Math.sqrt(a*a + b*b); // c = 5
    
    // Rama derecha
    var ramaDerecha = [];
    for (var x = a; x <= 8; x += 0.1) {
      var y = b * Math.sqrt(x*x/(a*a) - 1);
      ramaDerecha.push([x, y]);
    }
    var ramaDerechaInf = [];
    for (var x = a; x <= 8; x += 0.1) {
      var y = -b * Math.sqrt(x*x/(a*a) - 1);
      ramaDerechaInf.push([x, y]);
    }
    
    // Rama izquierda
    var ramaIzquierda = [];
    for (var x = -8; x <= -a; x += 0.1) {
      var y = b * Math.sqrt(x*x/(a*a) - 1);
      ramaIzquierda.push([x, y]);
    }
    var ramaIzquierdaInf = [];
    for (var x = -8; x <= -a; x += 0.1) {
      var y = -b * Math.sqrt(x*x/(a*a) - 1);
      ramaIzquierdaInf.push([x, y]);
    }
    
    // Asíntotas
    var asintota1 = [], asintota2 = [];
    for (var x = -8; x <= 8; x += 0.5) {
      asintota1.push([x, (b/a)*x]);
      asintota2.push([x, -(b/a)*x]);
    }
    
    var option = {
      animation: true,
      animationDuration: 1200,
      title: {
        text: 'Hipérbola: x²/16 - y²/9 = 1',
        subtext: 'a = 4, b = 3, c = 5',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' },
        subtextStyle: { fontSize: 12, color: '#3b82f6' }
      },
      grid: { 
        left: '10%', right: '10%', top: '15%', bottom: '12%',
        show: true, borderColor: '#cbd5e1'
      },
      xAxis: {
        type: 'value',
        name: 'x',
        nameLocation: 'middle',
        nameGap: 25,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: -9, max: 9,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#e2e8f0', type: 'dashed' } }
      },
      yAxis: {
        type: 'value',
        name: 'y',
        nameLocation: 'middle',
        nameGap: 30,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: -7, max: 7,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#e2e8f0', type: 'dashed' } }
      },
      series: [
        // Ramas de la hipérbola
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: ramaDerecha },
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: ramaDerechaInf },
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: ramaIzquierda },
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: ramaIzquierdaInf },
        // Asíntotas
        { name: 'Asíntotas', type: 'line', symbol: 'none', lineStyle: { width: 2, color: '#94a3b8', type: 'dashed' }, data: asintota1 },
        { type: 'line', symbol: 'none', lineStyle: { width: 2, color: '#94a3b8', type: 'dashed' }, data: asintota2 },
        // Vértices
        {
          name: 'Vértices',
          type: 'scatter',
          symbolSize: 14,
          itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 },
          label: { show: true, formatter: function(p) { return 'V(' + p.data[0] + ', 0)'; }, position: 'bottom', fontSize: 11, fontWeight: 'bold', color: '#22c55e' },
          data: [[-4, 0], [4, 0]]
        },
        // Focos
        {
          name: 'Focos',
          type: 'scatter',
          symbolSize: 14,
          itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 },
          label: { show: true, formatter: function(p) { return 'F(' + p.data[0] + ', 0)'; }, position: 'top', fontSize: 11, fontWeight: 'bold', color: '#ef4444' },
          data: [[-5, 0], [5, 0]]
        },
        // Centro
        {
          name: 'Centro',
          type: 'scatter',
          symbolSize: 12,
          itemStyle: { color: '#1e293b' },
          label: { show: true, formatter: 'C(0,0)', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#1e293b', offset: [0, -5] },
          data: [[0, 0]]
        }
      ],
      graphic: [
        { type: 'text', left: '82%', top: '25%', style: { text: 'y = (3/4)x', fontSize: 11, fill: '#64748b' } },
        { type: 'text', left: '82%', top: '70%', style: { text: 'y = -(3/4)x', fontSize: 11, fill: '#64748b' } }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **Tip para recordar:** En la hipérbola **horizontal**, el término con $x^2$ es **positivo** (va primero), y los vértices y focos están sobre el **eje X**. ¡La letra "H" de Horizontal te recuerda que todo está alineado Horizontalmente!

---

## 📖 ¿Por qué se llama "horizontal"?

Una hipérbola se llama **horizontal** cuando su **eje transversal** (la línea que une los dos vértices) está sobre el eje X.

Esto ocurre cuando en la ecuación canónica el **término positivo** contiene $x^2$:

$$
\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 \quad \leftarrow \text{Horizontal (}x^2\text{ positivo)}
$$

Si fuera al revés ($y^2$ positivo), sería vertical.

---

## 📖 Los Elementos de la Hipérbola

### El Centro

El **centro** de esta hipérbola está en el **origen** $(0, 0)$.

Es el punto medio entre los dos vértices y también entre los dos focos.

### Los Vértices

Los **vértices** son los puntos donde la hipérbola "cambia de dirección". Son los puntos más cercanos al centro.

Para una hipérbola horizontal con centro en el origen:

$$
V_1 = (-a, 0) \quad \text{y} \quad V_2 = (a, 0)
$$

El valor de $a$ se obtiene de la ecuación: $a^2$ es el denominador bajo $x^2$.

### Los Focos

Los **focos** son puntos especiales ubicados sobre el eje transversal, más allá de los vértices.

$$
F_1 = (-c, 0) \quad \text{y} \quad F_2 = (c, 0)
$$

### La Relación Fundamental: $c^2 = a^2 + b^2$

Esta es la fórmula más importante de la hipérbola:

$$
\boxed{c^2 = a^2 + b^2}
$$

A diferencia de la elipse (donde $c^2 = a^2 - b^2$), en la hipérbola **sumamos**.

> 💡 **Regla mnemotécnica:** "En la **H**ipérbola, **H**ay que sumar" (c² = a² **+** b²)

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Relación entre a, b y c</strong>
  </div>
  <div id="echarts-hiperbola-abc" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-hiperbola-abc')) {
    var chart = echarts.init(document.getElementById('echarts-hiperbola-abc'));
    
    var a = 4, b = 3, c = 5;
    
    var option = {
      animation: true,
      animationDuration: 1000,
      title: {
        text: 'Triángulo rectángulo: a, b, c',
        subtext: 'c² = a² + b² → 25 = 16 + 9',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' },
        subtextStyle: { fontSize: 12, color: '#3b82f6' }
      },
      grid: { 
        left: '12%', right: '12%', top: '18%', bottom: '12%',
        show: true, borderColor: '#cbd5e1'
      },
      xAxis: {
        type: 'value',
        min: -1, max: 7,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#e2e8f0', type: 'dashed' } }
      },
      yAxis: {
        type: 'value',
        min: -1, max: 5,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#e2e8f0', type: 'dashed' } }
      },
      series: [
        // Triángulo
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[0, 0], [4, 0]], name: 'a = 4' },
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#f97316' }, data: [[4, 0], [4, 3]], name: 'b = 3' },
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, data: [[0, 0], [4, 3]], name: 'c = 5' },
        // Puntos
        {
          type: 'scatter',
          symbolSize: 12,
          itemStyle: { color: '#1e293b' },
          data: [[0, 0], [4, 0], [4, 3]],
          label: { show: true, formatter: function(p) {
            if (p.dataIndex === 0) return 'Centro';
            if (p.dataIndex === 1) return 'Vértice (a,0)';
            return '(a, b)';
          }, position: 'top', fontSize: 10, fontWeight: 'bold' }
        }
      ],
      graphic: [
        { type: 'text', left: '35%', top: '72%', style: { text: 'a = 4', fontSize: 14, fontWeight: 'bold', fill: '#22c55e' } },
        { type: 'text', left: '68%', top: '52%', style: { text: 'b = 3', fontSize: 14, fontWeight: 'bold', fill: '#f97316' } },
        { type: 'text', left: '42%', top: '42%', style: { text: 'c = 5', fontSize: 14, fontWeight: 'bold', fill: '#ef4444' } }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Las Asíntotas

Las **asíntotas** son rectas a las que la hipérbola se acerca cada vez más pero nunca toca.

Para una hipérbola horizontal con centro en el origen:

$$
y = \pm \frac{b}{a}x
$$

Estas dos rectas forman una "X" que pasa por el centro y guía la forma de la hipérbola.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Las asíntotas guían la forma de la hipérbola</strong>
  </div>
  <div id="echarts-hiperbola-asintotas" style="width: 100%; height: 420px; min-height: 380px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-hiperbola-asintotas')) {
    var chart = echarts.init(document.getElementById('echarts-hiperbola-asintotas'));
    
    var a = 4, b = 3;
    
    // Hipérbola
    var rama1 = [], rama2 = [], rama3 = [], rama4 = [];
    for (var x = a; x <= 10; x += 0.1) {
      var y = b * Math.sqrt(x*x/(a*a) - 1);
      rama1.push([x, y]);
      rama2.push([x, -y]);
    }
    for (var x = -10; x <= -a; x += 0.1) {
      var y = b * Math.sqrt(x*x/(a*a) - 1);
      rama3.push([x, y]);
      rama4.push([x, -y]);
    }
    
    // Asíntotas
    var as1 = [], as2 = [];
    for (var x = -10; x <= 10; x += 0.5) {
      as1.push([x, (b/a)*x]);
      as2.push([x, -(b/a)*x]);
    }
    
    var option = {
      animation: true,
      animationDuration: 1000,
      title: {
        text: 'Las asíntotas: y = ±(3/4)x',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' }
      },
      legend: {
        data: ['Hipérbola', 'Asíntotas'],
        top: 30,
        textStyle: { fontSize: 11 }
      },
      grid: { 
        left: '10%', right: '10%', top: '18%', bottom: '12%',
        show: true, borderColor: '#cbd5e1'
      },
      xAxis: {
        type: 'value',
        min: -10, max: 10,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#e2e8f0', type: 'dashed' } }
      },
      yAxis: {
        type: 'value',
        min: -8, max: 8,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#e2e8f0', type: 'dashed' } }
      },
      series: [
        { name: 'Hipérbola', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: rama1 },
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: rama2 },
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: rama3 },
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: rama4 },
        { name: 'Asíntotas', type: 'line', symbol: 'none', lineStyle: { width: 2, color: '#ef4444', type: 'dashed' }, data: as1 },
        { type: 'line', symbol: 'none', lineStyle: { width: 2, color: '#ef4444', type: 'dashed' }, data: as2 }
      ],
      graphic: [
        { type: 'text', left: '78%', top: '22%', style: { text: 'La curva se', fontSize: 10, fill: '#64748b' } },
        { type: 'text', left: '78%', top: '26%', style: { text: 'acerca pero', fontSize: 10, fill: '#64748b' } },
        { type: 'text', left: '78%', top: '30%', style: { text: 'nunca toca', fontSize: 10, fill: '#64748b' } }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## ⚙️ Ejemplo 1: Identificar todos los elementos

Dada la ecuación $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$, encuentra todos los elementos.

**Solución paso a paso:**

**Paso 1:** Identificar $a^2$ y $b^2$
- $a^2 = 16 \Rightarrow a = 4$
- $b^2 = 9 \Rightarrow b = 3$

**Paso 2:** Calcular $c$ usando $c^2 = a^2 + b^2$
$$
c^2 = 16 + 9 = 25 \Rightarrow c = 5
$$

**Paso 3:** Determinar todos los elementos

| Elemento | Cálculo | Resultado |
|----------|---------|-----------|
| Centro | — | $(0, 0)$ |
| Vértices | $(\pm a, 0)$ | $(-4, 0)$ y $(4, 0)$ |
| Focos | $(\pm c, 0)$ | $(-5, 0)$ y $(5, 0)$ |
| Asíntotas | $y = \pm \frac{b}{a}x$ | $y = \pm \frac{3}{4}x$ |

$$
\boxed{V: (\pm 4, 0), \quad F: (\pm 5, 0), \quad \text{Asíntotas: } y = \pm \frac{3}{4}x}
$$

---

## ⚙️ Ejemplo 2: Encontrar la ecuación dada información

Una hipérbola horizontal con centro en el origen tiene vértices en $(\pm 5, 0)$ y focos en $(\pm 13, 0)$. Encuentra su ecuación.

**Solución paso a paso:**

**Paso 1:** Identificar $a$ y $c$
- Vértices en $(\pm 5, 0)$ → $a = 5$
- Focos en $(\pm 13, 0)$ → $c = 13$

**Paso 2:** Calcular $b$ usando $c^2 = a^2 + b^2$
$$
b^2 = c^2 - a^2 = 169 - 25 = 144 \Rightarrow b = 12
$$

**Paso 3:** Escribir la ecuación

$$
\boxed{\frac{x^2}{25} - \frac{y^2}{144} = 1}
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Hipérbola del Ejemplo 2</strong>
  </div>
  <div id="echarts-hiperbola-ej2" style="width: 100%; height: 420px; min-height: 380px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-hiperbola-ej2')) {
    var chart = echarts.init(document.getElementById('echarts-hiperbola-ej2'));
    
    var a = 5, b = 12, c = 13;
    
    var rama1 = [], rama2 = [], rama3 = [], rama4 = [];
    for (var x = a; x <= 18; x += 0.15) {
      var y = b * Math.sqrt(x*x/(a*a) - 1);
      rama1.push([x, y]);
      rama2.push([x, -y]);
    }
    for (var x = -18; x <= -a; x += 0.15) {
      var y = b * Math.sqrt(x*x/(a*a) - 1);
      rama3.push([x, y]);
      rama4.push([x, -y]);
    }
    
    var as1 = [], as2 = [];
    for (var x = -18; x <= 18; x += 1) {
      as1.push([x, (b/a)*x]);
      as2.push([x, -(b/a)*x]);
    }
    
    var option = {
      animation: true,
      animationDuration: 1000,
      title: {
        text: 'x²/25 - y²/144 = 1',
        subtext: 'a=5, b=12, c=13',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' },
        subtextStyle: { fontSize: 12, color: '#3b82f6' }
      },
      grid: { 
        left: '10%', right: '10%', top: '16%', bottom: '12%',
        show: true, borderColor: '#cbd5e1'
      },
      xAxis: {
        type: 'value',
        min: -18, max: 18,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#e2e8f0', type: 'dashed' } }
      },
      yAxis: {
        type: 'value',
        min: -35, max: 35,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#e2e8f0', type: 'dashed' } }
      },
      series: [
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: rama1 },
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: rama2 },
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: rama3 },
        { type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: rama4 },
        { type: 'line', symbol: 'none', lineStyle: { width: 2, color: '#94a3b8', type: 'dashed' }, data: as1 },
        { type: 'line', symbol: 'none', lineStyle: { width: 2, color: '#94a3b8', type: 'dashed' }, data: as2 },
        {
          type: 'scatter', symbolSize: 12, itemStyle: { color: '#22c55e' },
          label: { show: true, formatter: 'V', position: 'bottom', fontSize: 11, fontWeight: 'bold', color: '#22c55e' },
          data: [[-5, 0], [5, 0]]
        },
        {
          type: 'scatter', symbolSize: 12, itemStyle: { color: '#ef4444' },
          label: { show: true, formatter: 'F', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#ef4444' },
          data: [[-13, 0], [13, 0]]
        }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 🔑 Resumen

| Elemento | Fórmula | Nota clave |
|----------|---------|------------|
| **Ecuación** | $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ | $x^2$ positivo → horizontal |
| **Vértices** | $(\pm a, 0)$ | Sobre el eje X |
| **Focos** | $(\pm c, 0)$ | Más lejos que los vértices |
| **$c$** | $c = \sqrt{a^2 + b^2}$ | ¡En hipérbola SUMAMOS! |
| **Asíntotas** | $y = \pm \frac{b}{a}x$ | Guían la forma |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1

Encuentra los vértices, focos y asíntotas de $\dfrac{x^2}{25} - \dfrac{y^2}{144} = 1$.

<details>
<summary>Ver solución</summary>

**Paso 1:** Identificar valores
- $a^2 = 25 \Rightarrow a = 5$
- $b^2 = 144 \Rightarrow b = 12$

**Paso 2:** Calcular $c$
$$
c = \sqrt{25 + 144} = \sqrt{169} = 13
$$

**Paso 3:** Resultados

$$
\boxed{\text{Vértices: } (\pm 5, 0), \quad \text{Focos: } (\pm 13, 0), \quad \text{Asíntotas: } y = \pm \frac{12}{5}x}
$$

</details>

### Ejercicio 2

Encuentra las asíntotas de $\dfrac{x^2}{9} - \dfrac{y^2}{16} = 1$.

<details>
<summary>Ver solución</summary>

- $a^2 = 9 \Rightarrow a = 3$
- $b^2 = 16 \Rightarrow b = 4$

Las asíntotas son:

$$
\boxed{y = \pm \frac{4}{3}x}
$$

</details>

### Ejercicio 3

Una hipérbola horizontal con centro en el origen tiene $a = 6$ y $c = 10$. Encuentra su ecuación.

<details>
<summary>Ver solución</summary>

**Paso 1:** Calcular $b$
$$
b^2 = c^2 - a^2 = 100 - 36 = 64 \Rightarrow b = 8
$$

**Paso 2:** Escribir la ecuación

$$
\boxed{\frac{x^2}{36} - \frac{y^2}{64} = 1}
$$

</details>

### Ejercicio 4

Los focos de una hipérbola horizontal están en $(\pm 17, 0)$ y los vértices en $(\pm 8, 0)$. Encuentra $b$ y la ecuación.

<details>
<summary>Ver solución</summary>

- $c = 17$, $a = 8$

**Paso 1:** Calcular $b$
$$
b^2 = c^2 - a^2 = 289 - 64 = 225 \Rightarrow b = 15
$$

**Paso 2:** Ecuación

$$
\boxed{\frac{x^2}{64} - \frac{y^2}{225} = 1}
$$

</details>
