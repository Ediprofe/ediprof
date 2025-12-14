# |x| Ecuaciones Lineales con Valor Absoluto

En esta lección resolveremos ecuaciones que contienen valores absolutos.

---

## 📖 ¿Qué es el valor absoluto?

El **valor absoluto** de un número es su distancia al cero, siempre positiva:

$$
|x| = \begin{cases} x & \text{si } x \geq 0 \\ -x & \text{si } x < 0 \end{cases}
$$

### Ejemplos

$$
|5| = 5, \quad |-5| = 5, \quad |0| = 0
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> El valor absoluto como distancia al cero
  </div>
  <div id="echarts-valor-absoluto" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-valor-absoluto')) {
    var chart = echarts.init(document.getElementById('echarts-valor-absoluto'));
    var option = {
      title: { text: 'Función y = |x|', left: 'center', textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' } },
      animation: true,
      grid: { left: '10%', right: '8%', top: '15%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', min: -8, max: 8, interval: 1, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      yAxis: { type: 'value', min: 0, max: 8, interval: 1, axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } }, splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } } },
      series: [
        { name: 'y = |x|', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: [[-8, 8], [-4, 4], [0, 0], [4, 4], [8, 8]] },
        { type: 'scatter', symbolSize: 16, itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: 'Vértice', position: 'top', fontSize: 10, fontWeight: 'bold', color: '#ef4444' }, data: [[0, 0]] },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 }, label: { show: true, formatter: function(p) { return '|' + p.data[0] + '|=' + p.data[1]; }, position: 'right', fontSize: 10 }, data: [[5, 5], [-5, 5]] }
      ],
      tooltip: { trigger: 'axis' }
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Ecuaciones básicas con valor absoluto

### Tipo 1: $|x| = a$ (donde $a > 0$)

Tiene **dos soluciones**:

$$
|x| = a \quad \Rightarrow \quad x = a \quad \text{o} \quad x = -a
$$

---

### Ejemplo 1

Resolver $|x| = 7$.

$$
x = 7 \quad \text{o} \quad x = -7
$$

$$
\boxed{x = 7, \quad x = -7}
$$

---

### Ejemplo 2

Resolver $|x| = 0$.

$$
x = 0
$$

$$
\boxed{x = 0}
$$

---

### Tipo 2: $|x| = a$ (donde $a < 0$)

**Sin solución**, porque el valor absoluto nunca es negativo.

### Ejemplo 3

Resolver $|x| = -3$.

$$
\boxed{\text{Sin solución}}
$$

---

## 📖 Ecuaciones de la forma $|ax + b| = c$

### Ejemplo 4

Resolver $|2x - 3| = 5$.

**Caso 1:** $2x - 3 = 5$
$$
2x = 8 \quad \Rightarrow \quad x = 4
$$

**Caso 2:** $2x - 3 = -5$
$$
2x = -2 \quad \Rightarrow \quad x = -1
$$

$$
\boxed{x = 4, \quad x = -1}
$$

---

### Ejemplo 5

Resolver $|3x + 1| = 7$.

**Caso 1:** $3x + 1 = 7$
$$
x = 2
$$

**Caso 2:** $3x + 1 = -7$
$$
x = -\frac{8}{3}
$$

$$
\boxed{x = 2, \quad x = -\frac{8}{3}}
$$

---

### Ejemplo 6

Resolver $|5 - x| = 2$.

**Caso 1:** $5 - x = 2$
$$
x = 3
$$

**Caso 2:** $5 - x = -2$
$$
x = 7
$$

$$
\boxed{x = 3, \quad x = 7}
$$

---

## 📖 Ecuaciones con operaciones adicionales

### Ejemplo 7

Resolver $|x - 4| + 3 = 8$.

**Paso 1:** Aislamos el valor absoluto:
$$
|x - 4| = 5
$$

**Paso 2:** Resolvemos los dos casos:
$$
x - 4 = 5 \quad \Rightarrow \quad x = 9
$$
$$
x - 4 = -5 \quad \Rightarrow \quad x = -1
$$

$$
\boxed{x = 9, \quad x = -1}
$$

---

### Ejemplo 8

Resolver $2|x + 1| = 12$.

**Paso 1:** Aislamos:
$$
|x + 1| = 6
$$

**Paso 2:** Casos:
$$
x + 1 = 6 \quad \Rightarrow \quad x = 5
$$
$$
x + 1 = -6 \quad \Rightarrow \quad x = -7
$$

$$
\boxed{x = 5, \quad x = -7}
$$

---

### Ejemplo 9

Resolver $3|2x - 1| - 5 = 10$.

**Paso 1:** Aislamos:
$$
3|2x - 1| = 15
$$
$$
|2x - 1| = 5
$$

**Paso 2:** Casos:
$$
2x - 1 = 5 \quad \Rightarrow \quad x = 3
$$
$$
2x - 1 = -5 \quad \Rightarrow \quad x = -2
$$

$$
\boxed{x = 3, \quad x = -2}
$$

---

## 📖 Igualdad de valores absolutos

### Ejemplo 10

Resolver $|x - 2| = |x + 4|$.

Esto significa que las distancias son iguales. Hay dos posibilidades:

**Caso 1:** $(x - 2) = (x + 4)$
$$
-2 = 4 \quad \text{(Falso, sin solución)}
$$

**Caso 2:** $(x - 2) = -(x + 4)$
$$
x - 2 = -x - 4
$$
$$
2x = -2
$$
$$
x = -1
$$

$$
\boxed{x = -1}
$$

---

### Ejemplo 11

Resolver $|2x + 1| = |x - 3|$.

**Caso 1:** $2x + 1 = x - 3$
$$
x = -4
$$

**Caso 2:** $2x + 1 = -(x - 3)$
$$
2x + 1 = -x + 3
$$
$$
3x = 2
$$
$$
x = \frac{2}{3}
$$

$$
\boxed{x = -4, \quad x = \frac{2}{3}}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve $|x| = 12$.

<details>
<summary>Ver solución</summary>

$x = 12$ o $x = -12$

</details>

---

**Ejercicio 2:** Resuelve $|x + 5| = 8$.

<details>
<summary>Ver solución</summary>

$x + 5 = 8$ → $x = 3$

$x + 5 = -8$ → $x = -13$

</details>

---

**Ejercicio 3:** Resuelve $|3x - 6| = 0$.

<details>
<summary>Ver solución</summary>

$3x - 6 = 0$, $x = 2$

</details>

---

**Ejercicio 4:** Resuelve $|2x + 4| = -5$.

<details>
<summary>Ver solución</summary>

Sin solución (valor absoluto no puede ser negativo).

</details>

---

**Ejercicio 5:** Resuelve $|x - 1| + 4 = 9$.

<details>
<summary>Ver solución</summary>

$|x - 1| = 5$

$x = 6$ o $x = -4$

</details>

---

**Ejercicio 6:** Resuelve $|x + 3| = |2x - 1|$.

<details>
<summary>Ver solución</summary>

Caso 1: $x + 3 = 2x - 1$ → $x = 4$

Caso 2: $x + 3 = -2x + 1$ → $x = -\frac{2}{3}$

</details>

---
