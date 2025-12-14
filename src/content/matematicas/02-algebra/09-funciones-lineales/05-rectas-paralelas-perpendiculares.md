# ⊥ Rectas Paralelas, Secantes y Perpendiculares

En esta lección estudiaremos las relaciones entre rectas usando sus pendientes.

---

## 📖 Clasificación de rectas

Dos rectas en el plano pueden ser:

| Tipo | Descripción | Intersección |
|:-----|:------------|:-------------|
| **Paralelas** | Nunca se cruzan | Ningún punto |
| **Secantes** | Se cruzan en un punto | Un punto |
| **Perpendiculares** | Se cruzan formando ángulo de 90° | Un punto |

> Las rectas perpendiculares son un caso especial de rectas secantes.

---

## 📖 Rectas paralelas

Dos rectas son **paralelas** si nunca se intersectan. Para que esto ocurra, deben tener la **misma pendiente** pero **diferente intercepto**.

### Condición de paralelismo

$$
\ell_1 \parallel \ell_2 \quad \Leftrightarrow \quad m_1 = m_2 \text{ y } b_1 \neq b_2
$$

---

### Ejemplo 1

¿Son paralelas $y = 3x + 2$ y $y = 3x - 5$?

Ambas tienen pendiente $m = 3$, pero diferentes interceptos.

$$
\boxed{\text{Sí, son paralelas}}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo1-paralelas" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo1-paralelas')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo1-paralelas'));
    var option = {
      title: { text: 'Ejemplo 1: Rectas paralelas', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['y = 3x + 2', 'y = 3x - 5'], top: 30, textStyle: { fontSize: 11 } },
      grid: { left: '12%', right: '8%', top: '20%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -2, max: 3, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -8, max: 10, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'y = 3x + 2', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[-2, -4], [2, 8]] },
        { name: 'y = 3x - 5', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#60a5fa' }, data: [[-1, -8], [3, 4]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 2

¿Son paralelas $y = 2x + 1$ y $y = -2x + 1$?

$m_1 = 2$ y $m_2 = -2$

Las pendientes son diferentes.

$$
\boxed{\text{No, no son paralelas}}
$$

---

### Ejemplo 3

Encontrar la ecuación de la recta paralela a $y = 4x - 3$ que pasa por $(0, 5)$.

La pendiente debe ser $m = 4$ (igual a la original).

El punto $(0, 5)$ nos da el intercepto $b = 5$.

$$
y = 4x + 5
$$

$$
\boxed{y = 4x + 5}
$$

---

## 📖 Rectas secantes

Dos rectas son **secantes** si se cruzan en exactamente **un punto**. Esto ocurre cuando tienen **pendientes diferentes**.

### Condición de rectas secantes

$$
\ell_1 \text{ y } \ell_2 \text{ son secantes} \quad \Leftrightarrow \quad m_1 \neq m_2
$$

---

### Ejemplo 4

¿Son secantes $y = 2x + 3$ y $y = 5x - 1$?

$m_1 = 2$ y $m_2 = 5$

Las pendientes son diferentes, por lo tanto se cruzan en un punto.

$$
\boxed{\text{Sí, son secantes}}
$$

---

### Ejemplo 5

Encontrar el punto de intersección de $y = x + 1$ y $y = -2x + 7$.

Igualamos las ecuaciones:
$$
x + 1 = -2x + 7
$$
$$
3x = 6
$$
$$
x = 2
$$
$$
y = 2 + 1 = 3
$$

$$
\boxed{\text{Punto de intersección: } (2, 3)}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo5-secantes" style="width: 100%; height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo5-secantes')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo5-secantes'));
    var option = {
      title: { text: 'Ejemplo 5: Rectas secantes', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['y = x + 1', 'y = -2x + 7'], top: 30, textStyle: { fontSize: 11 } },
      grid: { left: '12%', right: '8%', top: '20%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -1, max: 5, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -2, max: 8, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'y = x + 1', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: [[-1, 0], [4, 5]] },
        { name: 'y = -2x + 7', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#f59e0b' }, data: [[0, 7], [4, -1]] },
        { type: 'scatter', symbolSize: 16, symbol: 'diamond', itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: '(2, 3)', position: 'top', fontSize: 11, fontWeight: 'bold', color: '#ef4444' }, data: [[2, 3]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 6

¿Las rectas $y = 4x + 2$ y $y = 4x - 3$ son secantes?

Ambas tienen $m = 4$. Como las pendientes son iguales, son paralelas, **no secantes**.

$$
\boxed{\text{No, son paralelas}}
$$

---

## 📖 Rectas perpendiculares

Dos rectas son **perpendiculares** si se intersectan formando un ángulo de $90°$.

### Condición de perpendicularidad

$$
\ell_1 \perp \ell_2 \quad \Leftrightarrow \quad m_1 \cdot m_2 = -1
$$

Equivalentemente:

$$
m_2 = -\frac{1}{m_1}
$$

Las pendientes son **recíprocas negativas**.

---

### Ejemplo 7

¿Son perpendiculares $y = 2x + 3$ y $y = -\frac{1}{2}x + 1$?

$m_1 = 2$ y $m_2 = -\frac{1}{2}$

$$
m_1 \cdot m_2 = 2 \cdot \left(-\frac{1}{2}\right) = -1 \quad ✓
$$

$$
\boxed{\text{Sí, son perpendiculares}}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-ejemplo7-perpendiculares" style="width: 100%; height: 400px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-ejemplo7-perpendiculares')) {
    var chart = echarts.init(document.getElementById('echarts-ejemplo7-perpendiculares'));
    var option = {
      title: { text: 'Ejemplo 7: Rectas perpendiculares', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['y = 2x + 3', 'y = -½x + 1'], top: 30, textStyle: { fontSize: 11 } },
      grid: { left: '12%', right: '8%', top: '20%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 25, min: -5, max: 5, interval: 1, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -5, max: 5, interval: 1, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'y = 2x + 3', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#a855f7' }, data: [[-4, -5], [1, 5]] },
        { name: 'y = -½x + 1', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#ec4899' }, data: [[-4, 3], [5, -1.5]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

### Ejemplo 8

Encontrar la pendiente de una recta perpendicular a $y = 4x + 2$.

Si $m_1 = 4$, entonces:

$$
m_2 = -\frac{1}{4}
$$

$$
\boxed{m = -\frac{1}{4}}
$$

---

### Ejemplo 9

Encontrar la ecuación de la recta perpendicular a $y = 3x - 1$ que pasa por $(6, 2)$.

Pendiente de la perpendicular: $m = -\frac{1}{3}$

$$
y - 2 = -\frac{1}{3}(x - 6)
$$
$$
y = -\frac{1}{3}x + 2 + 2 = -\frac{1}{3}x + 4
$$

$$
\boxed{y = -\frac{1}{3}x + 4}
$$

---

### Ejemplo 10

¿Son perpendiculares $y = \frac{3}{4}x + 1$ y $y = -\frac{4}{3}x - 2$?

$$
m_1 \cdot m_2 = \frac{3}{4} \cdot \left(-\frac{4}{3}\right) = -1 \quad ✓
$$

$$
\boxed{\text{Sí, son perpendiculares}}
$$

---

## 📖 Casos especiales

### Recta horizontal y vertical

Una recta **horizontal** ($y = b$) y una **vertical** ($x = a$) son siempre perpendiculares.

### Ejemplo 11

$y = 5$ (horizontal) y $x = 3$ (vertical) son perpendiculares.

---

## 📋 Resumen

| Relación | Condición |
|:---------|:----------|
| Paralelas | $m_1 = m_2$ (misma pendiente) |
| Secantes | $m_1 \neq m_2$ (diferentes pendientes) |
| Perpendiculares | $m_1 \cdot m_2 = -1$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** ¿Son paralelas $y = 5x - 3$ y $y = 5x + 7$?

<details>
<summary>Ver solución</summary>

Sí, ambas tienen $m = 5$.

</details>

---

**Ejercicio 2:** ¿Son secantes $y = 2x + 1$ y $y = 3x - 4$?

<details>
<summary>Ver solución</summary>

Sí, tienen pendientes diferentes ($m_1 = 2$, $m_2 = 3$).

</details>

---

**Ejercicio 3:** Encuentra el punto de intersección de $y = x + 2$ y $y = 3x - 2$.

<details>
<summary>Ver solución</summary>

$x + 2 = 3x - 2$, $2x = 4$, $x = 2$

$y = 4$

Punto: $(2, 4)$

</details>

---

**Ejercicio 4:** Encuentra la pendiente perpendicular a $m = 2$.

<details>
<summary>Ver solución</summary>

$m = -\frac{1}{2}$

</details>

---

**Ejercicio 5:** ¿Son perpendiculares $y = -5x + 1$ y $y = \frac{1}{5}x - 3$?

<details>
<summary>Ver solución</summary>

$(-5) \cdot \frac{1}{5} = -1$ ✓ Sí.

</details>

---

**Ejercicio 6:** ¿Qué relación tienen las rectas $y = 7$ y $x = -2$?

<details>
<summary>Ver solución</summary>

Son perpendiculares (horizontal y vertical).

</details>

---
