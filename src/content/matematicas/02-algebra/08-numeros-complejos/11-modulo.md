# 📏 Módulo de un Número Complejo

En esta lección aprenderemos a calcular el módulo (o valor absoluto) de un número complejo.

---

## 📖 Definición de módulo

El **módulo** de un número complejo $z = a + bi$, denotado $|z|$, es la distancia desde el origen hasta el punto $(a, b)$ en el plano complejo.

$$
|z| = |a + bi| = \sqrt{a^2 + b^2}
$$

---

## 📖 Interpretación geométrica

El módulo es la **longitud** del vector que va del origen al punto que representa el número complejo.

Por el teorema de Pitágoras:

$$
|z|^2 = a^2 + b^2
$$

$$
|z| = \sqrt{a^2 + b^2}
$$

---

### Ejemplo 1

Calcular $|3 + 4i|$.

$$
|3 + 4i| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

$$
\boxed{|3 + 4i| = 5}
$$

Visualización del módulo:

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-modulo" style="width: 100%; height: 380px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-modulo')) {
    var chart = echarts.init(document.getElementById('echarts-modulo'));
    var option = {
      title: { text: 'Módulo de z = 3 + 4i', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true, animationDuration: 1000,
      grid: { left: '12%', right: '8%', top: '10%', bottom: '15%', show: true, borderColor: '#cbd5e1' },
      xAxis: { type: 'value', name: 'Re', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 14, fontWeight: 'bold', color: '#374151' }, min: -1, max: 6, interval: 1, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, axisLabel: { fontSize: 11 } },
      yAxis: { type: 'value', name: 'Im', nameLocation: 'middle', nameGap: 30, nameTextStyle: { fontSize: 14, fontWeight: 'bold', color: '#374151' }, min: -1, max: 6, interval: 1, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', width: 1 } }, axisLabel: { fontSize: 11 } },
      series: [
        { name: 'Cateto a (parte real)', type: 'line', lineStyle: { width: 3, color: '#ef4444' }, symbol: 'none', data: [[0, 0], [3, 0]] },
        { name: 'Cateto b (parte imaginaria)', type: 'line', lineStyle: { width: 3, color: '#22c55e' }, symbol: 'none', data: [[3, 0], [3, 4]] },
        { name: 'Módulo |z| = 5', type: 'line', lineStyle: { width: 4, color: '#3b82f6' }, symbol: 'none', data: [[0, 0], [3, 4]] },
        { name: 'z = 3 + 4i', type: 'scatter', symbolSize: 18, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'z = 3 + 4i', position: 'right', fontSize: 12, fontWeight: 'bold' }, data: [[3, 4]] },
        { name: 'a = 3', type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'a = 3', fontSize: 12, fontWeight: 'bold', color: '#ef4444' }, data: [[1.5, -0.5]] },
        { name: 'b = 4', type: 'scatter', symbolSize: 0, label: { show: true, formatter: 'b = 4', fontSize: 12, fontWeight: 'bold', color: '#22c55e' }, data: [[3.5, 2]] },
        { name: '|z| = 5', type: 'scatter', symbolSize: 0, label: { show: true, formatter: '|z| = 5', fontSize: 14, fontWeight: 'bold', color: '#3b82f6' }, data: [[0.8, 2.5]] }
      ],
      tooltip: { trigger: 'item' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 El **módulo** es la hipotenusa del triángulo rectángulo formado por la parte real (cateto horizontal) y la parte imaginaria (cateto vertical).

---

### Ejemplo 2

Calcular $|5 - 12i|$.

$$
|5 - 12i| = \sqrt{5^2 + (-12)^2} = \sqrt{25 + 144} = \sqrt{169} = 13
$$

$$
\boxed{|5 - 12i| = 13}
$$

---

### Ejemplo 3

Calcular $|-2 + i|$.

$$
|-2 + i| = \sqrt{(-2)^2 + 1^2} = \sqrt{4 + 1} = \sqrt{5}
$$

$$
\boxed{|-2 + i| = \sqrt{5}}
$$

---

### Ejemplo 4

Calcular $|4|$ (número real).

$$
|4| = |4 + 0i| = \sqrt{16 + 0} = 4
$$

Para números reales, el módulo coincide con el valor absoluto.

$$
\boxed{|4| = 4}
$$

---

### Ejemplo 5

Calcular $|3i|$ (imaginario puro).

$$
|3i| = |0 + 3i| = \sqrt{0 + 9} = 3
$$

$$
\boxed{|3i| = 3}
$$

---

### Ejemplo 6

Calcular $|1 + i|$.

$$
|1 + i| = \sqrt{1 + 1} = \sqrt{2}
$$

$$
\boxed{|1 + i| = \sqrt{2}}
$$

---

## 📖 Propiedades del módulo

### Propiedad 1: Siempre no negativo

$$
|z| \geq 0
$$

$|z| = 0$ solo si $z = 0$.

---

### Propiedad 2: Módulo del producto

$$
|z_1 \cdot z_2| = |z_1| \cdot |z_2|
$$

### Ejemplo 7

Verificar que $|(3 + 4i)(1 + 2i)| = |3 + 4i| \cdot |1 + 2i|$.

**Lado derecho:**

$$
|3 + 4i| = 5, \quad |1 + 2i| = \sqrt{5}
$$

$$
5 \cdot \sqrt{5} = 5\sqrt{5}
$$

**Lado izquierdo:**

$(3 + 4i)(1 + 2i) = 3 + 6i + 4i + 8i^2 = 3 + 10i - 8 = -5 + 10i$

$$
|-5 + 10i| = \sqrt{25 + 100} = \sqrt{125} = 5\sqrt{5}
$$

$$
\boxed{|-5 + 10i| = 5\sqrt{5} \quad ✓}
$$

---

### Propiedad 3: Módulo del cociente

$$
\left|\frac{z_1}{z_2}\right| = \frac{|z_1|}{|z_2|}
$$

---

### Propiedad 4: Módulo del conjugado

$$
|\bar{z}| = |z|
$$

### Ejemplo 8

Si $z = 3 - 4i$, verificar que $|z| = |\bar{z}|$.

$$
|z| = |3 - 4i| = \sqrt{9 + 16} = 5
$$

$$
|\bar{z}| = |3 + 4i| = \sqrt{9 + 16} = 5
$$

$$
\boxed{|z| = |\bar{z}| = 5 \quad ✓}
$$

---

### Propiedad 5: Relación con el conjugado

$$
|z|^2 = z \cdot \bar{z}
$$

### Ejemplo 9

Verificar para $z = 2 + 3i$.

$$
z \cdot \bar{z} = (2 + 3i)(2 - 3i) = 4 + 9 = 13
$$

$$
|z|^2 = 2^2 + 3^2 = 4 + 9 = 13
$$

$$
\boxed{|z|^2 = z \cdot \bar{z} = 13 \quad ✓}
$$

---

### Ejemplo 10

Calcular $|2 - 5i|^2$ sin calcular la raíz.

$$
|2 - 5i|^2 = 2^2 + (-5)^2 = 4 + 25 = 29
$$

$$
\boxed{|2 - 5i|^2 = 29}
$$

---

## 📋 Resumen

| Propiedad | Fórmula |
|:----------|:-------:|
| Definición | $\|z\| = \sqrt{a^2 + b^2}$ |
| Producto | $\|z_1 z_2\| = \|z_1\| \|z_2\|$ |
| Cociente | $\left\|\frac{z_1}{z_2}\right\| = \frac{\|z_1\|}{\|z_2\|}$ |
| Conjugado | $\|\bar{z}\| = \|z\|$ |
| Con conjugado | $\|z\|^2 = z \bar{z}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula $|8 + 6i|$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{64 + 36} = \sqrt{100} = 10
$$

</details>

---

**Ejercicio 2:** Calcula $|-4 + 3i|$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{16 + 9} = \sqrt{25} = 5
$$

</details>

---

**Ejercicio 3:** Calcula $|2 - 2i|$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{4 + 4} = \sqrt{8} = 2\sqrt{2}
$$

</details>

---

**Ejercicio 4:** Calcula $|-7i|$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{0 + 49} = 7
$$

</details>

---

**Ejercicio 5:** Si $|z| = 5$, ¿cuánto es $|z|^2$?

<details>
<summary>Ver solución</summary>

$$
|z|^2 = 25
$$

</details>

---

**Ejercicio 6:** Calcula $|1 - i|^2$ sin calcular la raíz.

<details>
<summary>Ver solución</summary>

$$
1^2 + (-1)^2 = 1 + 1 = 2
$$

</details>

---
