# 📈 Exponentes

---

## 📖 Empecemos con una situación real

Imagina que tienes **una bacteria** en un cultivo de laboratorio. Esta bacteria se **duplica** cada hora.

| Hora | Cantidad de bacterias |
|:----:|:---------------------:|
| 0 | 1 |
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |

> 🤔 **Observa algo importante**: La cantidad no crece sumando... ¡crece **multiplicando** por 2!

---

## 📖 Encontrando el patrón

Miremos más de cerca qué está pasando:

| Hora ($t$) | Cálculo | Cantidad |
|:----------:|:--------|:--------:|
| 0 | $1$ | $1$ |
| 1 | $1 \times 2$ | $2$ |
| 2 | $1 \times 2 \times 2 = 1 \times 2^2$ | $4$ |
| 3 | $1 \times 2 \times 2 \times 2 = 1 \times 2^3$ | $8$ |
| 4 | $1 \times 2^4$ | $16$ |
| $t$ | $1 \times 2^t$ | $2^t$ |

> 💡 **¡Ahí está el patrón!** La cantidad de bacterias en la hora $t$ es: $\text{Cantidad} = 2^t$

Esto se llama **crecimiento exponencial** porque la variable ($t$) está en el **exponente**.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-bacterias" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-bacterias')) {
    var chart = echarts.init(document.getElementById('echarts-bacterias'));
    var data = [];
    for (var x = 0; x <= 5; x += 0.1) { data.push([x, Math.pow(2, x)]); }
    var option = {
      title: { text: '📊 Crecimiento de bacterias: Cantidad = 2^t', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '18%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'Hora (t)', nameLocation: 'middle', nameGap: 25, min: 0, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'Bacterias', nameLocation: 'middle', nameGap: 35, min: 0, max: 35, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, itemStyle: { color: '#22c55e' }, data: data },
        { type: 'scatter', symbolSize: 12, itemStyle: { color: '#3b82f6', borderColor: '#fff', borderWidth: 2 }, data: [[0,1], [1,2], [2,4], [3,8], [4,16], [5,32]] }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 ¿Y si empezamos con más bacterias?

Ahora imagina que empiezas con **5 bacterias** (no solo 1). Cada una se duplica cada hora.

| Hora ($t$) | Cálculo | Cantidad |
|:----------:|:--------|:--------:|
| 0 | $5$ | $5$ |
| 1 | $5 \times 2$ | $10$ |
| 2 | $5 \times 2^2$ | $20$ |
| 3 | $5 \times 2^3$ | $40$ |
| $t$ | $5 \times 2^t$ | $5 \cdot 2^t$ |

> 💡 **Nueva fórmula**: $\text{Cantidad} = 5 \cdot 2^t$

El **5** es la **cantidad inicial**. Podemos llamarlo $a$.

---

## 📖 ¿Y si se triplican en lugar de duplicarse?

Ahora imagina bacterias más productivas que se **triplican** cada hora, empezando con 2.

| Hora ($t$) | Cálculo | Cantidad |
|:----------:|:--------|:--------:|
| 0 | $2$ | $2$ |
| 1 | $2 \times 3$ | $6$ |
| 2 | $2 \times 3^2$ | $18$ |
| 3 | $2 \times 3^3$ | $54$ |
| $t$ | $2 \times 3^t$ | $2 \cdot 3^t$ |

> 💡 **Fórmula general**: $\text{Cantidad} = 2 \cdot 3^t$

El **3** es el **factor de multiplicación** (por cuánto se multiplica cada hora). Podemos llamarlo $b$.

---

## 📖 La fórmula general

De los ejemplos anteriores, descubrimos que:

$$
f(x) = a \cdot b^x
$$

donde:

| Elemento | Qué representa | En el ejemplo de bacterias |
|:---------|:---------------|:---------------------------|
| $a$ | **Valor inicial** (cuando $x = 0$) | Cantidad de bacterias al inicio |
| $b$ | **Base** (factor de multiplicación) | Por cuánto se multiplica cada periodo |
| $x$ | **Exponente** (variable) | El tiempo (horas, días, etc.) |

> 🔑 **Regla práctica**: Cuando $x = 0$, siempre obtienes $a$ (porque $b^0 = 1$).

---

## 📖 ¿Crece o decrece?

No todo crece. A veces las cosas **disminuyen** multiplicándose por un número menor que 1.

### Ejemplo: Decaimiento

Una sustancia radioactiva se reduce a la **mitad** cada año. Empiezas con 100 gramos.

| Año ($t$) | Cálculo | Cantidad (g) |
|:---------:|:--------|:------------:|
| 0 | $100$ | $100$ |
| 1 | $100 \times 0.5$ | $50$ |
| 2 | $100 \times 0.5^2$ | $25$ |
| 3 | $100 \times 0.5^3$ | $12.5$ |

$$
f(t) = 100 \cdot (0.5)^t
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-decaimiento" style="width: 100%; height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-decaimiento')) {
    var chart = echarts.init(document.getElementById('echarts-decaimiento'));
    var data = [];
    for (var x = 0; x <= 5; x += 0.1) { data.push([x, 100 * Math.pow(0.5, x)]); }
    var option = {
      title: { text: '📊 Decaimiento: f(t) = 100·(0.5)^t', left: 'center', textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' } },
      grid: { left: '12%', right: '8%', top: '18%', bottom: '15%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'Años (t)', nameLocation: 'middle', nameGap: 25, min: 0, max: 5, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'Gramos', nameLocation: 'middle', nameGap: 35, min: 0, max: 100, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, itemStyle: { color: '#ef4444' }, data: data }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 🎯 **Regla simple**: 
> - Si $b > 1$ → la función **crece** (se multiplica por más de 1)
> - Si $0 < b < 1$ → la función **decrece** (se multiplica por menos de 1)

---

## 📖 Comparación visual

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-comparacion" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-comparacion')) {
    var chart = echarts.init(document.getElementById('echarts-comparacion'));
    var data1 = [], data2 = [];
    for (var x = -1; x <= 3; x += 0.1) { data1.push([x, Math.pow(2, x)]); data2.push([x, Math.pow(0.5, x)]); }
    var option = {
      title: { text: '📊 Crecimiento vs Decrecimiento', left: 'center', textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['b = 2 (crece)', 'b = 0.5 (decrece)'], top: 35, textStyle: { fontSize: 11 } },
      grid: { left: '12%', right: '8%', top: '25%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 22, min: -1, max: 3, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: 0, max: 8, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { name: 'b = 2 (crece)', type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, itemStyle: { color: '#22c55e' }, data: data1 },
        { name: 'b = 0.5 (decrece)', type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, itemStyle: { color: '#ef4444' }, data: data2 }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Resumen: Lo que debes recordar

| Concepto | Significado |
|:---------|:------------|
| $f(x) = a \cdot b^x$ | Forma general de una función exponencial |
| $a$ | Valor inicial (cuando $x = 0$) |
| $b > 1$ | La función **crece** |
| $0 < b < 1$ | La función **decrece** |
| La variable está en el exponente | Por eso se llama "exponencial" |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Una población de conejos se triplica cada año. Si empiezas con 10 conejos, ¿cuántos habrá en 3 años?

<details>
<summary>Ver solución</summary>

$f(t) = 10 \cdot 3^t$

$f(3) = 10 \cdot 3^3 = 10 \cdot 27 = 270$ conejos

</details>

---

**Ejercicio 2:** Un medicamento se reduce a la mitad en el cuerpo cada 4 horas. Si tomas 200 mg, ¿cuánto queda después de 3 periodos de 4 horas?

<details>
<summary>Ver solución</summary>

$f(t) = 200 \cdot (0.5)^t$

$f(3) = 200 \cdot (0.5)^3 = 200 \cdot 0.125 = 25$ mg

</details>

---

**Ejercicio 3:** ¿La función $f(x) = 5 \cdot (0.8)^x$ crece o decrece? ¿Por qué?

<details>
<summary>Ver solución</summary>

Decrece, porque la base $b = 0.8 < 1$.

</details>

---

**Ejercicio 4:** Si $f(x) = 4 \cdot 2^x$, calcula $f(0)$, $f(1)$ y $f(2)$.

<details>
<summary>Ver solución</summary>

- $f(0) = 4 \cdot 2^0 = 4 \cdot 1 = 4$
- $f(1) = 4 \cdot 2^1 = 4 \cdot 2 = 8$
- $f(2) = 4 \cdot 2^2 = 4 \cdot 4 = 16$

</details>

---
