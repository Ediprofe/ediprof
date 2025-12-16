# Seno, Coseno y Tangente

Si tuvieras que escalar una montaña, ¿cómo calcularías qué tan empinada es la pendiente? El **seno**, **coseno** y **tangente** son las tres razones trigonométricas más importantes, y te permiten resolver exactamente ese tipo de problemas.

---

## 🎯 ¿Qué vas a aprender?

- Las definiciones exactas de seno, coseno y tangente
- Las características de cada razón
- La identidad pitagórica fundamental
- Los valores especiales para 0°, 30°, 45°, 60° y 90°

---

## 📋 Lo Esencial

| Razón | Fórmula | Rango (ángulos agudos) | Comportamiento |
|-------|---------|------------------------|----------------|
| **Seno** | $\sin\theta = \dfrac{O}{H}$ | 0 a 1 | Aumenta con el ángulo |
| **Coseno** | $\cos\theta = \dfrac{A}{H}$ | 0 a 1 | Disminuye con el ángulo |
| **Tangente** | $\tan\theta = \dfrac{O}{A}$ | 0 a ∞ | Aumenta rápidamente |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Comportamiento de sin, cos y tan de 0° a 90°</strong>
  </div>
  <div id="echarts-sincostan-comportamiento" style="width: 100%; height: 420px; min-height: 380px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-sincostan-comportamiento')) {
    var chart = echarts.init(document.getElementById('echarts-sincostan-comportamiento'));
    
    // Generar datos
    var sinData = [], cosData = [], tanData = [];
    for (var deg = 0; deg <= 90; deg += 2) {
      var rad = deg * Math.PI / 180;
      sinData.push([deg, Math.sin(rad)]);
      cosData.push([deg, Math.cos(rad)]);
      if (deg < 85) {
        tanData.push([deg, Math.tan(rad)]);
      }
    }
    
    var option = {
      animation: true,
      animationDuration: 1000,
      title: {
        text: 'Gráficas de seno, coseno y tangente',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' }
      },
      legend: {
        data: ['sin θ', 'cos θ', 'tan θ'],
        top: 30,
        textStyle: { fontSize: 12 }
      },
      grid: { left: '10%', right: '8%', top: '18%', bottom: '15%' },
      xAxis: {
        type: 'value',
        name: 'θ (grados)',
        nameLocation: 'middle',
        nameGap: 30,
        min: 0, max: 90,
        axisLine: { lineStyle: { color: '#374151', width: 2 } },
        splitLine: { lineStyle: { color: '#e2e8f0', type: 'dashed' } },
        axisLabel: { formatter: '{value}°' }
      },
      yAxis: {
        type: 'value',
        name: 'Valor',
        min: 0, max: 3,
        axisLine: { lineStyle: { color: '#374151', width: 2 } },
        splitLine: { lineStyle: { color: '#e2e8f0', type: 'dashed' } }
      },
      series: [
        {
          name: 'sin θ',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#3b82f6' },
          itemStyle: { color: '#3b82f6' },
          data: sinData
        },
        {
          name: 'cos θ',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#22c55e' },
          itemStyle: { color: '#22c55e' },
          data: cosData
        },
        {
          name: 'tan θ',
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#f97316' },
          itemStyle: { color: '#f97316' },
          data: tanData
        },
        // Línea y=1 de referencia
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 1, color: '#94a3b8', type: 'dashed' },
          data: [[0, 1], [90, 1]]
        }
      ],
      graphic: [
        { type: 'text', left: '75%', top: '62%', style: { text: 'tan → ∞', fontSize: 11, fill: '#f97316' } },
        { type: 'text', left: '75%', top: '35%', style: { text: 'sin → 1', fontSize: 11, fill: '#3b82f6' } },
        { type: 'text', left: '75%', top: '80%', style: { text: 'cos → 0', fontSize: 11, fill: '#22c55e' } }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **Observa:** El seno empieza en 0 y sube hasta 1. El coseno empieza en 1 y baja hasta 0. La tangente empieza en 0 y crece sin límite (tiende a infinito cerca de 90°).

---

## 📖 El Seno (sin)

> **Definición:** El seno de un ángulo es el cociente entre el **cateto opuesto** y la **hipotenusa**.

$$
\sin\theta = \frac{\text{Opuesto}}{\text{Hipotenusa}} = \frac{O}{H}
$$

### Características del seno

- **Rango:** Para ángulos agudos, $0 \leq \sin\theta \leq 1$
- **Valores extremos:** $\sin 0° = 0$ y $\sin 90° = 1$
- **Comportamiento:** Aumenta conforme aumenta el ángulo

### ⚙️ Ejemplo

En un triángulo donde el cateto opuesto mide 6 y la hipotenusa mide 10:

$$
\sin\theta = \frac{6}{10} = 0.6
$$

Esto significa que el cateto opuesto es el 60% de la hipotenusa.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">El seno como proporción del opuesto respecto a la hipotenusa</strong>
  </div>
  <div id="echarts-seno-visual" style="width: 100%; height: 350px; min-height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-seno-visual')) {
    var chart = echarts.init(document.getElementById('echarts-seno-visual'));
    
    var option = {
      animation: true,
      title: {
        text: 'sin θ = Opuesto / Hipotenusa = 6/10 = 0.6',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 13, fontWeight: 'bold', color: '#3b82f6' }
      },
      grid: { left: '10%', right: '10%', top: '15%', bottom: '10%' },
      xAxis: { type: 'value', min: 0, max: 14, show: false },
      yAxis: { type: 'value', min: 0, max: 10, show: false },
      series: [
        // Triángulo
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#1e293b' },
          data: [[2, 2], [10, 2], [10, 8], [2, 2]]
        },
        // Lado opuesto destacado
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 5, color: '#ef4444' },
          data: [[10, 2], [10, 8]]
        },
        // Hipotenusa destacada
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 4, color: '#8b5cf6' },
          data: [[2, 2], [10, 8]]
        }
      ],
      graphic: [
        { type: 'text', left: '15%', top: '72%', style: { text: 'θ', fontSize: 18, fontWeight: 'bold', fill: '#3b82f6' } },
        { type: 'text', left: '75%', top: '45%', style: { text: '6', fontSize: 18, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '78%', top: '50%', style: { text: '(Opuesto)', fontSize: 11, fill: '#ef4444' } },
        { type: 'text', left: '38%', top: '35%', style: { text: '10 (Hipotenusa)', fontSize: 14, fontWeight: 'bold', fill: '#8b5cf6' } },
        { type: 'text', left: '42%', top: '85%', style: { text: '8 (Adyacente)', fontSize: 12, fill: '#64748b' } }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 El Coseno (cos)

> **Definición:** El coseno de un ángulo es el cociente entre el **cateto adyacente** y la **hipotenusa**.

$$
\cos\theta = \frac{\text{Adyacente}}{\text{Hipotenusa}} = \frac{A}{H}
$$

### Características del coseno

- **Rango:** Para ángulos agudos, $0 \leq \cos\theta \leq 1$
- **Valores extremos:** $\cos 0° = 1$ y $\cos 90° = 0$
- **Comportamiento:** Disminuye conforme aumenta el ángulo

### ⚙️ Ejemplo

En el mismo triángulo donde el cateto adyacente mide 8 y la hipotenusa mide 10:

$$
\cos\theta = \frac{8}{10} = 0.8
$$

---

## 📖 La Tangente (tan)

> **Definición:** La tangente de un ángulo es el cociente entre el **cateto opuesto** y el **cateto adyacente**.

$$
\tan\theta = \frac{\text{Opuesto}}{\text{Adyacente}} = \frac{O}{A}
$$

### Características de la tangente

- **Rango:** Para ángulos agudos, $0 \leq \tan\theta < \infty$
- **Valores especiales:** $\tan 0° = 0$, $\tan 45° = 1$, $\tan 90°$ no está definida
- **Comportamiento:** Aumenta rápidamente cerca de 90°

### ⚙️ Ejemplo

En el mismo triángulo donde el cateto opuesto mide 6 y el adyacente mide 8:

$$
\tan\theta = \frac{6}{8} = 0.75
$$

> 💡 **Tip:** La tangente te dice la "pendiente" de la recta. Si $\tan\theta = 0.75$, por cada unidad horizontal avanzas 0.75 unidades verticales.

---

## 📖 Relación entre Seno, Coseno y Tangente

Una propiedad muy útil:

$$
\tan\theta = \frac{\sin\theta}{\cos\theta}
$$

### Verificación con nuestro ejemplo (6, 8, 10)

$$
\sin\theta = 0.6, \quad \cos\theta = 0.8
$$

$$
\frac{\sin\theta}{\cos\theta} = \frac{0.6}{0.8} = 0.75 = \tan\theta \quad ✓
$$

---

## 📖 La Identidad Pitagórica Fundamental

Esta es una de las identidades más importantes de la trigonometría:

$$
\boxed{\sin^2\theta + \cos^2\theta = 1}
$$

### ¿Por qué funciona?

Del teorema de Pitágoras: $O^2 + A^2 = H^2$

Dividiendo todo entre $H^2$:

$$
\frac{O^2}{H^2} + \frac{A^2}{H^2} = 1
$$

$$
\left(\frac{O}{H}\right)^2 + \left(\frac{A}{H}\right)^2 = 1
$$

$$
\sin^2\theta + \cos^2\theta = 1 \quad ✓
$$

### Verificación con nuestro ejemplo

$$
0.6^2 + 0.8^2 = 0.36 + 0.64 = 1 \quad ✓
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">La identidad pitagórica: sin²θ + cos²θ = 1</strong>
  </div>
  <div id="echarts-identidad-pitagorica" style="width: 100%; height: 380px; min-height: 340px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-identidad-pitagorica')) {
    var chart = echarts.init(document.getElementById('echarts-identidad-pitagorica'));
    
    // Generar datos para sin² y cos²
    var sin2Data = [], cos2Data = [];
    for (var deg = 0; deg <= 90; deg += 2) {
      var rad = deg * Math.PI / 180;
      var sinVal = Math.sin(rad);
      var cosVal = Math.cos(rad);
      sin2Data.push([deg, sinVal * sinVal]);
      cos2Data.push([deg, cosVal * cosVal]);
    }
    
    var option = {
      animation: true,
      title: {
        text: 'sin²θ + cos²θ = 1 (siempre)',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' }
      },
      legend: {
        data: ['sin²θ', 'cos²θ'],
        top: 30
      },
      grid: { left: '10%', right: '8%', top: '18%', bottom: '15%' },
      xAxis: {
        type: 'value',
        name: 'θ (grados)',
        nameLocation: 'middle',
        nameGap: 30,
        min: 0, max: 90,
        axisLine: { lineStyle: { color: '#374151', width: 2 } },
        splitLine: { lineStyle: { color: '#e2e8f0', type: 'dashed' } },
        axisLabel: { formatter: '{value}°' }
      },
      yAxis: {
        type: 'value',
        name: 'Valor',
        min: 0, max: 1.1,
        axisLine: { lineStyle: { color: '#374151', width: 2 } },
        splitLine: { lineStyle: { color: '#e2e8f0', type: 'dashed' } }
      },
      series: [
        {
          name: 'sin²θ',
          type: 'line',
          symbol: 'none',
          stack: 'Total',
          areaStyle: { color: 'rgba(59, 130, 246, 0.5)' },
          lineStyle: { width: 2, color: '#3b82f6' },
          data: sin2Data
        },
        {
          name: 'cos²θ',
          type: 'line',
          symbol: 'none',
          stack: 'Total',
          areaStyle: { color: 'rgba(34, 197, 94, 0.5)' },
          lineStyle: { width: 2, color: '#22c55e' },
          data: cos2Data
        }
      ],
      graphic: [
        { type: 'text', left: '45%', top: '50%', style: { text: '¡Siempre suman 1!', fontSize: 13, fontWeight: 'bold', fill: '#1e293b' } }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Tabla de Valores Importantes

| Ángulo | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|--------|--------------|--------------|--------------|
| **0°** | 0 | 1 | 0 |
| **30°** | $\frac{1}{2}$ = 0.5 | $\frac{\sqrt{3}}{2}$ ≈ 0.866 | $\frac{\sqrt{3}}{3}$ ≈ 0.577 |
| **45°** | $\frac{\sqrt{2}}{2}$ ≈ 0.707 | $\frac{\sqrt{2}}{2}$ ≈ 0.707 | 1 |
| **60°** | $\frac{\sqrt{3}}{2}$ ≈ 0.866 | $\frac{1}{2}$ = 0.5 | $\sqrt{3}$ ≈ 1.732 |
| **90°** | 1 | 0 | ∞ (no definida) |

---

## 🔑 Resumen

| Concepto | Fórmula | Punto clave |
|----------|---------|-------------|
| Seno | $\frac{O}{H}$ | De 0 a 1, aumenta |
| Coseno | $\frac{A}{H}$ | De 1 a 0, disminuye |
| Tangente | $\frac{O}{A}$ | De 0 a ∞, crece rápido |
| Relación | $\tan = \frac{\sin}{\cos}$ | Muy útil |
| Identidad | $\sin^2 + \cos^2 = 1$ | ¡Siempre! |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1: Calcular sin, cos, tan

Triángulo con cateto opuesto = 7, cateto adyacente = 24, hipotenusa = 25.

<details>
<summary>Ver solución</summary>

$$
\sin\theta = \frac{7}{25} = 0.28
$$

$$
\cos\theta = \frac{24}{25} = 0.96
$$

$$
\tan\theta = \frac{7}{24} \approx 0.292
$$

</details>

---

### Ejercicio 2: Encontrar un lado

Si $\sin\theta = 0.6$ y la hipotenusa es 20, ¿cuánto mide el cateto opuesto?

<details>
<summary>Ver solución</summary>

$$
\sin\theta = \frac{O}{H} \Rightarrow O = H \cdot \sin\theta = 20 \times 0.6 = 12
$$

</details>

---

### Ejercicio 3: Usar la identidad pitagórica

Si $\sin\theta = \frac{3}{5}$, calcula $\cos\theta$ usando la identidad $\sin^2\theta + \cos^2\theta = 1$.

<details>
<summary>Ver solución</summary>

$$
\sin^2\theta + \cos^2\theta = 1
$$

$$
\left(\frac{3}{5}\right)^2 + \cos^2\theta = 1
$$

$$
\frac{9}{25} + \cos^2\theta = 1
$$

$$
\cos^2\theta = 1 - \frac{9}{25} = \frac{16}{25}
$$

$$
\cos\theta = \frac{4}{5}
$$

</details>

---

### Ejercicio 4: De razón a ángulo

¿Para qué ángulo $\tan\theta = 1$?

<details>
<summary>Ver solución</summary>

$\tan\theta = 1$ cuando el cateto opuesto es igual al adyacente.

Esto ocurre cuando $\theta = 45°$.

</details>
