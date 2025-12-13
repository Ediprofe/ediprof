# 🔮 Introducción a los Números Imaginarios

En esta lección introduciremos el concepto de número imaginario, su origen histórico y su importancia en las matemáticas y la vida real.

---

## 📖 El problema que motivó los imaginarios

Consideremos la ecuación:

$$
x^2 = -1
$$

¿Existe algún número real que multiplicado por sí mismo dé $-1$?

- Si $x$ es positivo: $x^2$ es positivo ✗
- Si $x$ es negativo: $x^2$ también es positivo ✗
- Si $x$ es cero: $x^2 = 0$ ✗

**No existe ningún número real cuyo cuadrado sea negativo.**

Sin embargo, esta ecuación tiene soluciones muy útiles en ingeniería, física y matemáticas avanzadas.

---

## 📖 Definición de la unidad imaginaria

Para resolver el problema anterior, los matemáticos definieron la **unidad imaginaria** $i$:

$$
i = \sqrt{-1}
$$

O equivalentemente:

$$
i^2 = -1
$$

Con esta definición, la ecuación $x^2 = -1$ tiene solución: $x = i$ o $x = -i$.

Observa cómo el eje imaginario **extiende** la recta numérica real hacia una nueva dimensión vertical:

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-eje-imaginario" style="width: 100%; height: 400px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-eje-imaginario')) {
    var chart = echarts.init(document.getElementById('echarts-eje-imaginario'));
    var option = {
      title: { text: 'El Plano Complejo', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '15%', right: '10%', top: '10%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Reales', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 14, fontWeight: 'bold', color: '#3b82f6' }, min: -4, max: 4, interval: 1, axisLine: { lineStyle: { color: '#3b82f6', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, axisLabel: { fontSize: 11 } },
      yAxis: { type: 'value', name: 'Imaginarios', nameLocation: 'middle', nameGap: 55, nameTextStyle: { fontSize: 14, fontWeight: 'bold', color: '#22c55e' }, min: -4, max: 4, interval: 1, axisLine: { lineStyle: { color: '#22c55e', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, axisLabel: { fontSize: 11 } },
      series: [
        { name: 'Origen', type: 'scatter', symbolSize: 16, itemStyle: { color: '#374151', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '0', position: 'left', fontSize: 11, fontWeight: 'bold' }, data: [[0, 0]] },
        { name: 'Reales', type: 'scatter', symbolSize: 12, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return p.data[0]; }, position: 'bottom', fontSize: 10 }, data: [[-2, 0], [-1, 0], [1, 0], [2, 0]] },
        { name: 'Imaginarios +', type: 'scatter', symbolSize: 14, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return p.data[1] + 'i'; }, position: 'right', fontSize: 11, fontWeight: 'bold', fontStyle: 'italic' }, data: [[0, 1], [0, 2]] },
        { name: 'Imaginarios -', type: 'scatter', symbolSize: 14, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return p.data[1] + 'i'; }, position: 'right', fontSize: 11, fontWeight: 'bold', fontStyle: 'italic' }, data: [[0, -1], [0, -2]] }
      ],
      tooltip: { trigger: 'item' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **Observa:** La unidad imaginaria $i$ está ubicada en el punto $(0, 1)$ del plano, exactamente una unidad hacia arriba desde el origen.

---

## 📖 Aplicaciones en el mundo real

Aunque se llaman "imaginarios", estos números tienen aplicaciones muy reales:

### Ingeniería eléctrica

Los números imaginarios son esenciales para analizar **circuitos de corriente alterna**. La impedancia de un circuito se expresa con números complejos.

### Procesamiento de señales

Las **ondas de radio, audio y video** se analizan matemáticamente usando números complejos y la transformada de Fourier.

### Mecánica cuántica

El comportamiento de las partículas subatómicas se describe con ecuaciones que requieren números complejos.

### Aerodinámica

El diseño de alas de avión utiliza análisis complejo para estudiar el flujo de aire.

---

## 📖 Definición de número imaginario

Un **número imaginario puro** es un número de la forma:

$$
bi
$$

donde $b$ es un número real y $b \neq 0$.

### Ejemplos

| Número | Clasificación |
|:------:|:--------------|
| $3i$ | Imaginario puro |
| $-5i$ | Imaginario puro |
| $\frac{1}{2}i$ | Imaginario puro |
| $\sqrt{2}i$ | Imaginario puro |

En el eje imaginario, podemos visualizar estos números:

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-imaginarios-puros" style="width: 100%; height: 380px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-imaginarios-puros')) {
    var chart = echarts.init(document.getElementById('echarts-imaginarios-puros'));
    var option = {
      title: { text: 'Números Imaginarios Puros', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '20%', right: '15%', top: '10%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', min: -1, max: 1, show: false },
      yAxis: { type: 'value', name: 'Eje Imaginario', nameLocation: 'middle', nameGap: 50, nameTextStyle: { fontSize: 14, fontWeight: 'bold', color: '#374151' }, min: -6, max: 6, interval: 1, axisLine: { lineStyle: { color: '#64748b', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, axisLabel: { fontSize: 11 } },
      series: [
        { name: '0', type: 'scatter', symbolSize: 14, itemStyle: { color: '#374151', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '0', position: 'right', fontSize: 11 }, data: [[0, 0]] },
        { name: '3i', type: 'scatter', symbolSize: 16, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '3i', position: 'right', fontSize: 14, fontWeight: 'bold', fontStyle: 'italic' }, data: [[0, 3]] },
        { name: '√2i', type: 'scatter', symbolSize: 14, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '√2 i', position: 'right', fontSize: 12, fontStyle: 'italic' }, data: [[0, 1.41]] },
        { name: '½i', type: 'scatter', symbolSize: 14, itemStyle: { color: '#f97316', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '½i', position: 'right', fontSize: 12, fontStyle: 'italic' }, data: [[0, 0.5]] },
        { name: '-5i', type: 'scatter', symbolSize: 16, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '-5i', position: 'right', fontSize: 14, fontWeight: 'bold', fontStyle: 'italic' }, data: [[0, -5]] }
      ],
      tooltip: { trigger: 'item', formatter: function(p) { return p.seriesName; } }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Raíces cuadradas de números negativos

Usando la unidad imaginaria, podemos calcular raíces cuadradas de números negativos:

$$
\sqrt{-a} = \sqrt{a} \cdot \sqrt{-1} = \sqrt{a} \cdot i = i\sqrt{a}
$$

(para $a > 0$)

---

### Ejemplo 1

Simplificar $\sqrt{-4}$.

$$
\sqrt{-4} = \sqrt{4} \cdot \sqrt{-1} = 2i
$$

$$
\boxed{\sqrt{-4} = 2i}
$$

---

### Ejemplo 2

Simplificar $\sqrt{-9}$.

$$
\sqrt{-9} = \sqrt{9} \cdot i = 3i
$$

$$
\boxed{\sqrt{-9} = 3i}
$$

---

### Ejemplo 3

Simplificar $\sqrt{-25}$.

$$
\sqrt{-25} = \sqrt{25} \cdot i = 5i
$$

$$
\boxed{\sqrt{-25} = 5i}
$$

---

### Ejemplo 4

Simplificar $\sqrt{-7}$.

$$
\sqrt{-7} = \sqrt{7} \cdot i = i\sqrt{7}
$$

$$
\boxed{\sqrt{-7} = i\sqrt{7}}
$$

---

### Ejemplo 5

Simplificar $\sqrt{-12}$.

$$
\sqrt{-12} = \sqrt{12} \cdot i = \sqrt{4 \cdot 3} \cdot i = 2\sqrt{3} \cdot i = 2i\sqrt{3}
$$

$$
\boxed{\sqrt{-12} = 2i\sqrt{3}}
$$

---

### Ejemplo 6

Simplificar $\sqrt{-50}$.

$$
\sqrt{-50} = \sqrt{50} \cdot i = 5\sqrt{2} \cdot i = 5i\sqrt{2}
$$

$$
\boxed{\sqrt{-50} = 5i\sqrt{2}}
$$

---

## 📖 Notación

Es convención escribir $i$ **antes** del radical para evitar confusión:

- ✅ $3i\sqrt{5}$ (correcto)
- ⚠️ $3\sqrt{5}i$ (puede confundirse con $3\sqrt{5i}$)

---

## 📋 Resumen

| Concepto | Definición |
|:---------|:-----------|
| Unidad imaginaria | $i = \sqrt{-1}$, por lo tanto $i^2 = -1$ |
| Número imaginario puro | $bi$ donde $b \in \mathbb{R}$, $b \neq 0$ |
| Raíz de número negativo | $\sqrt{-a} = i\sqrt{a}$ para $a > 0$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Simplifica $\sqrt{-16}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{-16} = 4i
$$

</details>

---

**Ejercicio 2:** Simplifica $\sqrt{-49}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{-49} = 7i
$$

</details>

---

**Ejercicio 3:** Simplifica $\sqrt{-3}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{-3} = i\sqrt{3}
$$

</details>

---

**Ejercicio 4:** Simplifica $\sqrt{-18}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{-18} = \sqrt{9 \cdot 2} \cdot i = 3i\sqrt{2}
$$

</details>

---

**Ejercicio 5:** Simplifica $\sqrt{-72}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{-72} = \sqrt{36 \cdot 2} \cdot i = 6i\sqrt{2}
$$

</details>

---

**Ejercicio 6:** Si $i^2 = -1$, ¿cuánto es $(-i)^2$?

<details>
<summary>Ver solución</summary>

$$
(-i)^2 = (-1)^2 \cdot i^2 = 1 \cdot (-1) = -1
$$

</details>

---
