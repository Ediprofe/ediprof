# Razones Trigonométricas

¿Cómo podemos expresar matemáticamente la relación entre un ángulo y los lados de un triángulo? La respuesta son las **razones trigonométricas**: cocientes que nos permiten calcular lados desconocidos y resolver problemas de la vida real.

---

## 🎯 ¿Qué vas a aprender?

- Qué son las razones trigonométricas
- Las 6 razones: seno, coseno, tangente y sus recíprocas
- La regla mnemotécnica SOH-CAH-TOA
- Cómo calcular las razones dado un triángulo

---

## 📋 Lo Esencial: Las 6 Razones Trigonométricas

| Razón | Símbolo | Fórmula | Recíproca |
|-------|---------|---------|-----------|
| **Seno** | $\sin\theta$ | $\dfrac{\text{Opuesto}}{\text{Hipotenusa}}$ | Cosecante |
| **Coseno** | $\cos\theta$ | $\dfrac{\text{Adyacente}}{\text{Hipotenusa}}$ | Secante |
| **Tangente** | $\tan\theta$ | $\dfrac{\text{Opuesto}}{\text{Adyacente}}$ | Cotangente |
| **Cosecante** | $\csc\theta$ | $\dfrac{\text{Hipotenusa}}{\text{Opuesto}}$ | Seno |
| **Secante** | $\sec\theta$ | $\dfrac{\text{Hipotenusa}}{\text{Adyacente}}$ | Coseno |
| **Cotangente** | $\cot\theta$ | $\dfrac{\text{Adyacente}}{\text{Opuesto}}$ | Tangente |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Las razones trigonométricas en el triángulo 3-4-5</strong>
  </div>
  <div id="echarts-razones-visual" style="width: 100%; height: 420px; min-height: 380px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-razones-visual')) {
    var chart = echarts.init(document.getElementById('echarts-razones-visual'));
    
    var option = {
      animation: true,
      animationDuration: 1000,
      title: {
        text: 'Triángulo 3-4-5: Las 6 razones respecto a θ',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' }
      },
      grid: { left: '5%', right: '5%', top: '12%', bottom: '5%' },
      xAxis: { type: 'value', min: 0, max: 16, show: false },
      yAxis: { type: 'value', min: 0, max: 10, show: false },
      series: [
        // Triángulo
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#1e293b' },
          areaStyle: { color: 'rgba(59, 130, 246, 0.08)' },
          data: [[1, 2], [5, 2], [5, 5], [1, 2]]
        },
        // Arco para theta
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#3b82f6' },
          smooth: true,
          data: (function() {
            var arc = [];
            for (var i = 0; i <= 37; i++) {
              var angle = i * Math.PI / 180;
              arc.push([1 + 0.7*Math.cos(angle), 2 + 0.7*Math.sin(angle)]);
            }
            return arc;
          })()
        },
        // Marca de ángulo recto
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#64748b' },
          data: [[4.7, 2], [4.7, 2.3], [5, 2.3]]
        },
        // Vértices
        {
          type: 'scatter',
          symbolSize: 10,
          itemStyle: { color: '#1e293b' },
          data: [[1, 2], [5, 2], [5, 5]]
        }
      ],
      graphic: [
        // Ángulo theta
        { type: 'text', left: '12%', top: '68%', style: { text: 'θ', fontSize: 18, fontWeight: 'bold', fill: '#3b82f6' } },
        
        // Lados del triángulo
        { type: 'text', left: '17%', top: '80%', style: { text: '4 (Adyacente)', fontSize: 13, fontWeight: 'bold', fill: '#22c55e' } },
        { type: 'text', left: '32%', top: '52%', style: { text: '3', fontSize: 13, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '29%', top: '57%', style: { text: '(Opuesto)', fontSize: 11, fill: '#ef4444' } },
        { type: 'text', left: '11%', top: '52%', style: { text: '5 (Hip)', fontSize: 13, fontWeight: 'bold', fill: '#8b5cf6' } },
        
        // Tabla de razones
        { type: 'text', left: '52%', top: '22%', style: { text: 'RAZONES PRINCIPALES', fontSize: 13, fontWeight: 'bold', fill: '#1e293b' } },
        { type: 'text', left: '52%', top: '30%', style: { text: 'sin θ = Opuesto/Hip = 3/5 = 0.6', fontSize: 12, fill: '#3b82f6' } },
        { type: 'text', left: '52%', top: '38%', style: { text: 'cos θ = Adyacente/Hip = 4/5 = 0.8', fontSize: 12, fill: '#22c55e' } },
        { type: 'text', left: '52%', top: '46%', style: { text: 'tan θ = Opuesto/Ady = 3/4 = 0.75', fontSize: 12, fill: '#f97316' } },
        
        { type: 'text', left: '52%', top: '58%', style: { text: 'RAZONES RECÍPROCAS', fontSize: 13, fontWeight: 'bold', fill: '#1e293b' } },
        { type: 'text', left: '52%', top: '66%', style: { text: 'csc θ = Hip/Opuesto = 5/3 ≈ 1.67', fontSize: 12, fill: '#64748b' } },
        { type: 'text', left: '52%', top: '74%', style: { text: 'sec θ = Hip/Adyacente = 5/4 = 1.25', fontSize: 12, fill: '#64748b' } },
        { type: 'text', left: '52%', top: '82%', style: { text: 'cot θ = Adyacente/Opuesto = 4/3 ≈ 1.33', fontSize: 12, fill: '#64748b' } }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **SOH-CAH-TOA**: La regla mnemotécnica más famosa de la trigonometría.
> - **S**eno = **O**puesto / **H**ipotenusa
> - **C**oseno = **A**dyacente / **H**ipotenusa
> - **T**angente = **O**puesto / **A**dyacente

---

## 📖 ¿Qué son las Razones Trigonométricas?

> **Definición:** Una razón trigonométrica es el **cociente** (división) entre dos lados de un triángulo rectángulo, respecto a un ángulo de referencia.

Lo increíble de las razones trigonométricas es que **solo dependen del ángulo**, no del tamaño del triángulo. Un triángulo chiquito de 3-4-5 tiene las mismas razones que uno gigante de 30-40-50, porque son semejantes.

---

## 📖 Las Tres Razones Principales

### Seno (sin)

$$
\sin\theta = \frac{\text{Opuesto}}{\text{Hipotenusa}} = \frac{O}{H}
$$

**Mnemotecnia:** **S**eno = **O**puesto / **H**ipotenusa → **SOH**

### Coseno (cos)

$$
\cos\theta = \frac{\text{Adyacente}}{\text{Hipotenusa}} = \frac{A}{H}
$$

**Mnemotecnia:** **C**oseno = **A**dyacente / **H**ipotenusa → **CAH**

### Tangente (tan)

$$
\tan\theta = \frac{\text{Opuesto}}{\text{Adyacente}} = \frac{O}{A}
$$

**Mnemotecnia:** **T**angente = **O**puesto / **A**dyacente → **TOA**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">SOH-CAH-TOA visualizado</strong>
  </div>
  <div id="echarts-razones-sohcahtoa" style="width: 100%; height: 380px; min-height: 340px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-razones-sohcahtoa')) {
    var chart = echarts.init(document.getElementById('echarts-razones-sohcahtoa'));
    
    var option = {
      animation: true,
      title: {
        text: 'SOH - CAH - TOA',
        subtext: 'La regla que nunca olvidarás',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 16, fontWeight: 'bold', color: '#1e293b' },
        subtextStyle: { fontSize: 12, color: '#64748b' }
      },
      grid: { left: '5%', right: '5%', top: '18%', bottom: '5%' },
      xAxis: { type: 'value', min: 0, max: 21, show: false },
      yAxis: { type: 'value', min: 0, max: 10, show: false },
      series: [
        // Triángulo 1 - SOH
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#1e293b' },
          areaStyle: { color: 'rgba(59, 130, 246, 0.15)' },
          data: [[1, 3], [4, 3], [4, 7], [1, 3]]
        },
        // Triángulo 2 - CAH
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#1e293b' },
          areaStyle: { color: 'rgba(34, 197, 94, 0.15)' },
          data: [[8, 3], [11, 3], [11, 7], [8, 3]]
        },
        // Triángulo 3 - TOA
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#1e293b' },
          areaStyle: { color: 'rgba(249, 115, 22, 0.15)' },
          data: [[15, 3], [18, 3], [18, 7], [15, 3]]
        }
      ],
      graphic: [
        // SOH
        { type: 'text', left: '8%', top: '25%', style: { text: 'SOH', fontSize: 20, fontWeight: 'bold', fill: '#3b82f6' } },
        { type: 'text', left: '5%', top: '35%', style: { text: 'Seno = O/H', fontSize: 12, fill: '#3b82f6' } },
        { type: 'text', left: '7%', top: '78%', style: { text: 'θ', fontSize: 14, fontWeight: 'bold', fill: '#3b82f6' } },
        { type: 'text', left: '21%', top: '52%', style: { text: 'O', fontSize: 13, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '8%', top: '48%', style: { text: 'H', fontSize: 13, fontWeight: 'bold', fill: '#8b5cf6' } },
        
        // CAH
        { type: 'text', left: '42%', top: '25%', style: { text: 'CAH', fontSize: 20, fontWeight: 'bold', fill: '#22c55e' } },
        { type: 'text', left: '38%', top: '35%', style: { text: 'Coseno = A/H', fontSize: 12, fill: '#22c55e' } },
        { type: 'text', left: '40%', top: '78%', style: { text: 'θ', fontSize: 14, fontWeight: 'bold', fill: '#3b82f6' } },
        { type: 'text', left: '44%', top: '85%', style: { text: 'A', fontSize: 13, fontWeight: 'bold', fill: '#22c55e' } },
        { type: 'text', left: '42%', top: '48%', style: { text: 'H', fontSize: 13, fontWeight: 'bold', fill: '#8b5cf6' } },
        
        // TOA
        { type: 'text', left: '75%', top: '25%', style: { text: 'TOA', fontSize: 20, fontWeight: 'bold', fill: '#f97316' } },
        { type: 'text', left: '71%', top: '35%', style: { text: 'Tangente = O/A', fontSize: 12, fill: '#f97316' } },
        { type: 'text', left: '73%', top: '78%', style: { text: 'θ', fontSize: 14, fontWeight: 'bold', fill: '#3b82f6' } },
        { type: 'text', left: '87%', top: '52%', style: { text: 'O', fontSize: 13, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '77%', top: '85%', style: { text: 'A', fontSize: 13, fontWeight: 'bold', fill: '#22c55e' } }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Las Tres Razones Recíprocas

Las razones recíprocas son simplemente "dar la vuelta" a las principales:

| Razón principal | Recíproca | Relación |
|-----------------|-----------|----------|
| $\sin\theta$ | $\csc\theta = \frac{1}{\sin\theta}$ | $\sin\theta \cdot \csc\theta = 1$ |
| $\cos\theta$ | $\sec\theta = \frac{1}{\cos\theta}$ | $\cos\theta \cdot \sec\theta = 1$ |
| $\tan\theta$ | $\cot\theta = \frac{1}{\tan\theta}$ | $\tan\theta \cdot \cot\theta = 1$ |

---

## 📖 Relación entre Tangente, Seno y Coseno

Una propiedad muy útil:

$$
\tan\theta = \frac{\sin\theta}{\cos\theta}
$$

**¿Por qué funciona?**

$$
\frac{\sin\theta}{\cos\theta} = \frac{O/H}{A/H} = \frac{O}{H} \times \frac{H}{A} = \frac{O}{A} = \tan\theta \quad ✓
$$

---

## ⚙️ Ejemplo 1: Calcular las 6 razones

Dado un triángulo rectángulo con:
- Cateto opuesto a θ = 5
- Cateto adyacente a θ = 12
- Hipotenusa = 13

Calcula las 6 razones trigonométricas.

**Solución:**

| Razón | Cálculo | Resultado |
|-------|---------|-----------|
| $\sin\theta$ | $\frac{5}{13}$ | ≈ 0.385 |
| $\cos\theta$ | $\frac{12}{13}$ | ≈ 0.923 |
| $\tan\theta$ | $\frac{5}{12}$ | ≈ 0.417 |
| $\csc\theta$ | $\frac{13}{5}$ | = 2.6 |
| $\sec\theta$ | $\frac{13}{12}$ | ≈ 1.083 |
| $\cot\theta$ | $\frac{12}{5}$ | = 2.4 |

---

## ⚙️ Ejemplo 2: Encontrar las razones con Pitágoras

Si sabemos que el cateto opuesto = 8 y la hipotenusa = 17, encuentra todas las razones.

**Paso 1:** Encontrar el cateto adyacente con Pitágoras

$$
a^2 + 8^2 = 17^2
$$
$$
a^2 = 289 - 64 = 225
$$
$$
a = 15
$$

**Paso 2:** Calcular las razones

| Razón | Valor |
|-------|-------|
| $\sin\theta$ | $\frac{8}{17}$ |
| $\cos\theta$ | $\frac{15}{17}$ |
| $\tan\theta$ | $\frac{8}{15}$ |

---

## 📖 Propiedad Fundamental

> Las razones trigonométricas **solo dependen del ángulo**, no del tamaño del triángulo.

Triángulos semejantes (mismo ángulo, diferentes tamaños) tienen exactamente las mismas razones trigonométricas.

---

## 🔑 Resumen

| Razón | Fórmula | SOH-CAH-TOA |
|-------|---------|-------------|
| Seno | $\frac{O}{H}$ | **S**eno = **O**puesto/**H**ipotenusa |
| Coseno | $\frac{A}{H}$ | **C**oseno = **A**dyacente/**H**ipotenusa |
| Tangente | $\frac{O}{A}$ | **T**angente = **O**puesto/**A**dyacente |
| Cosecante | $\frac{H}{O}$ | Recíproco del seno |
| Secante | $\frac{H}{A}$ | Recíproco del coseno |
| Cotangente | $\frac{A}{O}$ | Recíproco de la tangente |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1: Calcular razones principales

En un triángulo rectángulo con catetos 5 y 12 (hipotenusa = 13), si θ está opuesto al cateto de 5, calcula:

1. $\sin\theta$
2. $\cos\theta$
3. $\tan\theta$

<details>
<summary>Ver solución</summary>

1. $\sin\theta = \frac{5}{13}$
2. $\cos\theta = \frac{12}{13}$
3. $\tan\theta = \frac{5}{12}$

</details>

---

### Ejercicio 2: Razones recíprocas

Con los datos del ejercicio anterior, calcula:

1. $\csc\theta$
2. $\sec\theta$
3. $\cot\theta$

<details>
<summary>Ver solución</summary>

1. $\csc\theta = \frac{13}{5} = 2.6$
2. $\sec\theta = \frac{13}{12} \approx 1.083$
3. $\cot\theta = \frac{12}{5} = 2.4$

</details>

---

### Ejercicio 3: Identificar razones

¿Qué razón trigonométrica representa cada cociente?

1. $\frac{\text{Opuesto}}{\text{Hipotenusa}}$
2. $\frac{\text{Adyacente}}{\text{Opuesto}}$
3. $\frac{\text{Hipotenusa}}{\text{Adyacente}}$

<details>
<summary>Ver solución</summary>

1. **Seno** ($\sin\theta$)
2. **Cotangente** ($\cot\theta$)
3. **Secante** ($\sec\theta$)

</details>

---

### Ejercicio 4: Usar Pitágoras primero

Si $\sin\theta = \frac{3}{5}$, encuentra $\cos\theta$ y $\tan\theta$.

<details>
<summary>Ver solución</summary>

Si $\sin\theta = \frac{3}{5}$, entonces: Opuesto = 3, Hipotenusa = 5

Usando Pitágoras: $\text{Adyacente} = \sqrt{5^2 - 3^2} = \sqrt{16} = 4$

Por lo tanto:
- $\cos\theta = \frac{4}{5}$
- $\tan\theta = \frac{3}{4}$

</details>
