# Ángulos Notables: 30°, 45° y 60°

¿Te has dado cuenta de que en los exámenes siempre aparecen los mismos ángulos? Los ángulos de **30°, 45° y 60°** son especiales porque sus razones trigonométricas tienen valores exactos que debemos memorizar. ¡Estos tres ángulos son tus mejores amigos en trigonometría!

---

## 🎯 ¿Qué vas a aprender?

- Los triángulos especiales que generan estos ángulos
- Los valores exactos de seno, coseno y tangente para cada uno
- Patrones para memorizarlos fácilmente
- Cómo usar estos valores sin calculadora

---

## 📋 Lo Esencial: Tabla Maestra

| Ángulo | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|--------|--------------|--------------|--------------|
| **0°** | $0$ | $1$ | $0$ |
| **30°** | $\dfrac{1}{2}$ | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{\sqrt{3}}{3}$ |
| **45°** | $\dfrac{\sqrt{2}}{2}$ | $\dfrac{\sqrt{2}}{2}$ | $1$ |
| **60°** | $\dfrac{\sqrt{3}}{2}$ | $\dfrac{1}{2}$ | $\sqrt{3}$ |
| **90°** | $1$ | $0$ | $\infty$ |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Los dos triángulos especiales que debes conocer</strong>
  </div>
  <div id="echarts-angulos-notables-triangulos" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-angulos-notables-triangulos')) {
    var chart = echarts.init(document.getElementById('echarts-angulos-notables-triangulos'));
    
    var option = {
      animation: true,
      animationDuration: 1000,
      title: {
        text: 'Triángulo 45-45-90 y Triángulo 30-60-90',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' }
      },
      grid: { left: '5%', right: '5%', top: '12%', bottom: '5%' },
      xAxis: { type: 'value', min: 0, max: 20, show: false },
      yAxis: { type: 'value', min: 0, max: 10, show: false },
      series: [
        // Triángulo 45-45-90 (izquierda)
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#3b82f6' },
          areaStyle: { color: 'rgba(59, 130, 246, 0.15)' },
          data: [[1, 2], [5, 2], [5, 6], [1, 2]]
        },
        // Marca de ángulo recto 45-45-90
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#64748b' },
          data: [[4.6, 2], [4.6, 2.4], [5, 2.4]]
        },
        
        // Triángulo 30-60-90 (derecha)
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#22c55e' },
          areaStyle: { color: 'rgba(34, 197, 94, 0.15)' },
          data: [[11, 2], [17, 2], [17, 5.46], [11, 2]]
        },
        // Marca de ángulo recto 30-60-90
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#64748b' },
          data: [[16.6, 2], [16.6, 2.4], [17, 2.4]]
        }
      ],
      graphic: [
        // Triángulo 45-45-90
        { type: 'text', left: '8%', top: '18%', style: { text: 'TRIÁNGULO 45-45-90', fontSize: 12, fontWeight: 'bold', fill: '#3b82f6' } },
        { type: 'text', left: '8%', top: '23%', style: { text: '(Isósceles rectángulo)', fontSize: 10, fill: '#64748b' } },
        { type: 'text', left: '8%', top: '58%', style: { text: '45°', fontSize: 14, fontWeight: 'bold', fill: '#3b82f6' } },
        { type: 'text', left: '23%', top: '32%', style: { text: '45°', fontSize: 14, fontWeight: 'bold', fill: '#3b82f6' } },
        { type: 'text', left: '25%', top: '70%', style: { text: '90°', fontSize: 10, fill: '#64748b' } },
        { type: 'text', left: '14%', top: '80%', style: { text: '1', fontSize: 16, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '27%', top: '48%', style: { text: '1', fontSize: 16, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '10%', top: '42%', style: { text: '√2', fontSize: 16, fontWeight: 'bold', fill: '#8b5cf6' } },
        
        // Triángulo 30-60-90
        { type: 'text', left: '60%', top: '18%', style: { text: 'TRIÁNGULO 30-60-90', fontSize: 12, fontWeight: 'bold', fill: '#22c55e' } },
        { type: 'text', left: '60%', top: '23%', style: { text: '(Mitad de equilátero)', fontSize: 10, fill: '#64748b' } },
        { type: 'text', left: '58%', top: '58%', style: { text: '30°', fontSize: 14, fontWeight: 'bold', fill: '#22c55e' } },
        { type: 'text', left: '80%', top: '38%', style: { text: '60°', fontSize: 14, fontWeight: 'bold', fill: '#22c55e' } },
        { type: 'text', left: '82%', top: '70%', style: { text: '90°', fontSize: 10, fill: '#64748b' } },
        { type: 'text', left: '68%', top: '80%', style: { text: '√3', fontSize: 16, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '87%', top: '50%', style: { text: '1', fontSize: 16, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '62%', top: '42%', style: { text: '2', fontSize: 16, fontWeight: 'bold', fill: '#8b5cf6' } },
        
        // Proporciones
        { type: 'text', left: '8%', top: '90%', style: { text: 'Lados: 1 : 1 : √2', fontSize: 12, fontWeight: 'bold', fill: '#3b82f6' } },
        { type: 'text', left: '58%', top: '90%', style: { text: 'Lados: 1 : √3 : 2', fontSize: 12, fontWeight: 'bold', fill: '#22c55e' } }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **Memoriza las proporciones:**
> - **45-45-90:** Los catetos son iguales (1:1), hipotenusa = √2
> - **30-60-90:** Cateto menor : Cateto mayor : Hipotenusa = 1 : √3 : 2

---

## 📖 Triángulo de 45° (Isósceles Rectángulo)

Un triángulo rectángulo con dos ángulos de 45° tiene:
- **Catetos iguales:** $1$ y $1$
- **Hipotenusa:** $\sqrt{2}$

### Razones de 45°

$$
\sin 45° = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2} \approx 0.707
$$

$$
\cos 45° = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2} \approx 0.707
$$

$$
\tan 45° = \frac{1}{1} = 1
$$

> 💡 **A 45°, seno y coseno son iguales, y la tangente es exactamente 1.**

---

## 📖 Triángulo de 30°-60°-90°

Este triángulo surge de cortar un triángulo equilátero por la mitad. Sus lados están en proporción:

$$
1 : \sqrt{3} : 2
$$

Donde:
- **1** = cateto opuesto a 30° (el más corto)
- **√3** = cateto opuesto a 60°
- **2** = hipotenusa

### Razones de 30°

$$
\sin 30° = \frac{1}{2} = 0.5
$$

$$
\cos 30° = \frac{\sqrt{3}}{2} \approx 0.866
$$

$$
\tan 30° = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3} \approx 0.577
$$

### Razones de 60°

$$
\sin 60° = \frac{\sqrt{3}}{2} \approx 0.866
$$

$$
\cos 60° = \frac{1}{2} = 0.5
$$

$$
\tan 60° = \frac{\sqrt{3}}{1} = \sqrt{3} \approx 1.732
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Valores de seno, coseno y tangente para ángulos notables</strong>
  </div>
  <div id="echarts-angulos-notables-valores" style="width: 100%; height: 400px; min-height: 360px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-angulos-notables-valores')) {
    var chart = echarts.init(document.getElementById('echarts-angulos-notables-valores'));
    
    var angulos = ['0°', '30°', '45°', '60°', '90°'];
    var seno = [0, 0.5, 0.707, 0.866, 1];
    var coseno = [1, 0.866, 0.707, 0.5, 0];
    var tangente = [0, 0.577, 1, 1.732, null];
    
    var option = {
      animation: true,
      title: {
        text: 'Valores de sin, cos, tan para ángulos notables',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' }
      },
      legend: {
        data: ['sin θ', 'cos θ', 'tan θ'],
        top: 30
      },
      grid: { left: '10%', right: '8%', top: '18%', bottom: '12%' },
      xAxis: {
        type: 'category',
        data: angulos,
        axisLine: { lineStyle: { color: '#374151', width: 2 } }
      },
      yAxis: {
        type: 'value',
        name: 'Valor',
        min: 0, max: 2,
        axisLine: { lineStyle: { color: '#374151', width: 2 } },
        splitLine: { lineStyle: { color: '#e2e8f0', type: 'dashed' } }
      },
      series: [
        {
          name: 'sin θ',
          type: 'bar',
          barWidth: '20%',
          itemStyle: { color: '#3b82f6' },
          data: seno,
          label: { show: true, position: 'top', fontSize: 10 }
        },
        {
          name: 'cos θ',
          type: 'bar',
          barWidth: '20%',
          itemStyle: { color: '#22c55e' },
          data: coseno,
          label: { show: true, position: 'top', fontSize: 10 }
        },
        {
          name: 'tan θ',
          type: 'bar',
          barWidth: '20%',
          itemStyle: { color: '#f97316' },
          data: tangente,
          label: { show: true, position: 'top', fontSize: 10 }
        }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Patrón para Memorizar los Senos

Hay un patrón increíble para los senos:

| Ángulo | Seno | Patrón |
|--------|------|--------|
| 0° | 0 | $\frac{\sqrt{0}}{2}$ |
| 30° | $\frac{1}{2}$ | $\frac{\sqrt{1}}{2}$ |
| 45° | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ |
| 60° | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{2}$ |
| 90° | 1 | $\frac{\sqrt{4}}{2}$ |

**¡Los senos van de $\frac{\sqrt{0}}{2}$ a $\frac{\sqrt{4}}{2}$!**

### Y los cosenos van al revés

$$
\cos\theta = \sin(90° - \theta)
$$

Por eso:
- $\cos 30° = \sin 60°$
- $\cos 60° = \sin 30°$

---

## 📖 Razones Recíprocas de Ángulos Notables

| Ángulo | $\csc\theta$ | $\sec\theta$ | $\cot\theta$ |
|--------|--------------|--------------|--------------|
| 30° | 2 | $\frac{2\sqrt{3}}{3}$ | $\sqrt{3}$ |
| 45° | $\sqrt{2}$ | $\sqrt{2}$ | 1 |
| 60° | $\frac{2\sqrt{3}}{3}$ | 2 | $\frac{\sqrt{3}}{3}$ |

---

## 🔑 Resumen

| Ángulo | Sin | Cos | Tan |
|--------|-----|-----|-----|
| 30° | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{3}$ |
| 45° | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | 1 |
| 60° | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$ |

**Triángulos especiales:**
- 45-45-90: Lados 1 : 1 : √2
- 30-60-90: Lados 1 : √3 : 2

---

## 📝 Ejercicios de Práctica

### Ejercicio 1: Completar valores (sin calculadora)

1. $\sin 30° = $ ___
2. $\cos 60° = $ ___
3. $\tan 45° = $ ___
4. $\sin 60° = $ ___

<details>
<summary>Ver solución</summary>

1. $\sin 30° = \frac{1}{2}$
2. $\cos 60° = \frac{1}{2}$
3. $\tan 45° = 1$
4. $\sin 60° = \frac{\sqrt{3}}{2}$

</details>

---

### Ejercicio 2: Calcular expresiones

Calcula sin calculadora:

1. $\sin 30° + \cos 60°$
2. $\sin^2 45° + \cos^2 45°$
3. $\tan 30° \times \tan 60°$

<details>
<summary>Ver solución</summary>

1. $\frac{1}{2} + \frac{1}{2} = 1$
2. $\frac{1}{2} + \frac{1}{2} = 1$ (identidad pitagórica)
3. $\frac{\sqrt{3}}{3} \times \sqrt{3} = \frac{3}{3} = 1$

</details>

---

### Ejercicio 3: Aplicación

Un triángulo rectángulo tiene un ángulo de 30° y la hipotenusa mide 10. ¿Cuánto mide el cateto opuesto al ángulo de 30°?

<details>
<summary>Ver solución</summary>

$$
\sin 30° = \frac{O}{H}
$$

$$
\frac{1}{2} = \frac{O}{10}
$$

$$
O = 10 \times \frac{1}{2} = 5
$$

**Respuesta:** El cateto opuesto mide 5.

</details>

---

### Ejercicio 4: ¿Qué ángulo es?

¿Qué ángulo tiene $\sin\theta = \frac{\sqrt{3}}{2}$?

<details>
<summary>Ver solución</summary>

$\theta = 60°$

(Recuerda que $\sin 60° = \frac{\sqrt{3}}{2}$)

</details>
