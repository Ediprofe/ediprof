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

### Comportamiento de 0° a 90°

| θ | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|---|--------------|--------------|--------------|
| 0° | 0 | 1 | 0 |
| 30° | 0.5 | 0.866 | 0.577 |
| 45° | 0.707 | 0.707 | 1 |
| 60° | 0.866 | 0.5 | 1.732 |
| 90° | 1 | 0 | ∞ |

> 📈 **Tendencias:** A medida que θ aumenta: **seno** aumenta (0→1), **coseno** disminuye (1→0), **tangente** crece muy rápido (0→∞).

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1.1rem;">📈</span> <strong style="color: #1e293b;">Gráfica de seno, coseno y tangente</strong>
  </div>
  <div id="echarts-sincostan" style="width: 100%; height: 380px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-sincostan')) {
    var chart = echarts.init(document.getElementById('echarts-sincostan'));
    var sinData = [], cosData = [], tanData = [];
    for (var deg = 0; deg <= 90; deg += 2) {
      var rad = deg * Math.PI / 180;
      sinData.push([deg, Math.sin(rad)]);
      cosData.push([deg, Math.cos(rad)]);
      if (deg < 85) tanData.push([deg, Math.tan(rad)]);
    }
    chart.setOption({
      animation: true,
      legend: { data: ['sin θ', 'cos θ', 'tan θ'], top: 10 },
      grid: { left: '12%', right: '5%', top: '18%', bottom: '15%' },
      xAxis: { type: 'value', name: 'θ (grados)', min: 0, max: 90, axisLabel: { formatter: '{value}°' } },
      yAxis: { type: 'value', min: 0, max: 3 },
      series: [
        { name: 'sin θ', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: sinData },
        { name: 'cos θ', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: cosData },
        { name: 'tan θ', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#f97316' }, data: tanData }
      ]
    });
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

**Ejemplo:** En un triángulo con Opuesto = 6, Adyacente = 8, Hipotenusa = 10:

$$\sin\theta = \frac{6}{10} = 0.6$$

![Triángulo con razones trigonométricas](/images/geometria/trigonometria/03-triangulo-345.svg)

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

### Verificación con valores

| θ | $\sin^2\theta$ | $\cos^2\theta$ | Suma |
|---|----------------|----------------|------|
| 0° | 0 | 1 | **1** |
| 30° | 0.25 | 0.75 | **1** |
| 45° | 0.5 | 0.5 | **1** |
| 60° | 0.75 | 0.25 | **1** |
| 90° | 1 | 0 | **1** |

> ✓ **¡Siempre suman 1!** No importa el ángulo.

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
