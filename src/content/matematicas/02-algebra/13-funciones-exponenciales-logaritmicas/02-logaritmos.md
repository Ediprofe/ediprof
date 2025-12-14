# 📉 Logaritmos

---

## 📖 Retomemos el ejemplo de las bacterias

En la lección anterior vimos que si una bacteria se duplica cada hora:

$$
\text{Cantidad} = 2^t
$$

donde $t$ es el tiempo en horas.

Por ejemplo:
- Hora 0: $2^0 = 1$ bacteria
- Hora 3: $2^3 = 8$ bacterias

---

## 📖 Una pregunta diferente

Ahora imagina que alguien te hace una pregunta **al revés**:

> *"Si hay 8 bacterias, ¿cuántas horas han pasado?"*

Sabemos que $2^t = 8$. Necesitamos encontrar $t$.

**Razonamiento**:
- $2^1 = 2$ ❌
- $2^2 = 4$ ❌
- $2^3 = 8$ ✅

¡Han pasado **3 horas**!

> 💡 **Este tipo de pregunta —encontrar el exponente— es exactamente lo que resuelve un LOGARITMO.**

---

## 📖 Definiendo el logaritmo

El **logaritmo** es la operación que responde: *"¿A qué exponente debo elevar la base para obtener este número?"*

$$
\log_2(8) = 3 \quad \text{porque} \quad 2^3 = 8
$$

En general:

$$
\log_b(x) = y \quad \Longleftrightarrow \quad b^y = x
$$

> 🔑 **El logaritmo ES el exponente.**

---

## 📖 Más ejemplos: La pregunta que responde

| Si te preguntan... | Significa... | Razonamiento | Respuesta |
|:-------------------|:-------------|:-------------|:---------:|
| $\log_2(16) = ?$ | ¿$2$ elevado a qué da $16$? | $2^4 = 16$ | $4$ |
| $\log_3(27) = ?$ | ¿$3$ elevado a qué da $27$? | $3^3 = 27$ | $3$ |
| $\log_{10}(1000) = ?$ | ¿$10$ elevado a qué da $1000$? | $10^3 = 1000$ | $3$ |
| $\log_5(25) = ?$ | ¿$5$ elevado a qué da $25$? | $5^2 = 25$ | $2$ |

---

## 📖 Visualización: Exponencial y logaritmo son inversas

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem 0;">
  <div id="echarts-log-inversas" style="width: 100%; height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-log-inversas')) {
    var chart = echarts.init(document.getElementById('echarts-log-inversas'));
    var data1 = [], data2 = [], diagonal = [];
    for (var x = -1; x <= 3; x += 0.1) { data1.push([x, Math.pow(2, x)]); }
    for (var x = 0.2; x <= 8; x += 0.1) { data2.push([x, Math.log2(x)]); }
    for (var x = 0; x <= 4; x += 0.5) { diagonal.push([x, x]); }
    var option = {
      title: { text: '📊 Exponencial y logaritmo son operaciones inversas', left: 'center', textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' } },
      legend: { data: ['y = 2^x', 'y = log₂(x)'], top: 30, textStyle: { fontSize: 11 } },
      grid: { left: '12%', right: '8%', top: '22%', bottom: '12%', show: true, borderColor: '#94a3b8' },
      xAxis: { type: 'value', name: 'x', nameLocation: 'middle', nameGap: 22, min: -1, max: 8, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      yAxis: { type: 'value', name: 'y', nameLocation: 'middle', nameGap: 30, min: -1, max: 8, axisLine: { lineStyle: { color: '#374151', width: 2 } }, splitLine: { lineStyle: { color: '#cbd5e1', type: 'dashed' } } },
      series: [
        { name: 'y = 2^x', type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, itemStyle: { color: '#22c55e' }, data: data1 },
        { name: 'y = log₂(x)', type: 'line', smooth: true, symbol: 'none', lineStyle: { width: 3, color: '#ef4444' }, itemStyle: { color: '#ef4444' }, data: data2 },
        { type: 'line', symbol: 'none', lineStyle: { width: 1, color: '#94a3b8', type: 'dashed' }, data: diagonal }
      ]
    };
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 📌 **Observa**: Las curvas son simétricas respecto a la línea $y = x$. ¡Son "reflejos" una de la otra!

---

## 📖 Casos especiales (memorízalos)

Hay dos resultados que siempre son verdad para cualquier base $b$:

| Expresión | Resultado | ¿Por qué? |
|:---------:|:---------:|:----------|
| $\log_b(1) = $ | $0$ | Porque $b^0 = 1$ siempre |
| $\log_b(b) = $ | $1$ | Porque $b^1 = b$ siempre |

**Ejemplos**:
- $\log_2(1) = 0$ porque $2^0 = 1$
- $\log_5(5) = 1$ porque $5^1 = 5$
- $\log_{10}(10) = 1$ porque $10^1 = 10$

---

## 📖 Bases especiales

Hay dos logaritmos que tienen nombres especiales porque son muy usados:

| Notación | Base | Nombre | Uso común |
|:--------:|:----:|:-------|:----------|
| $\log(x)$ | $10$ | Logaritmo común (o decimal) | Calculadoras, escalas |
| $\ln(x)$ | $e \approx 2.718$ | Logaritmo natural | Ciencias, crecimiento continuo |

**Ejemplos**:
- $\log(100) = 2$ porque $10^2 = 100$
- $\log(1000) = 3$ porque $10^3 = 1000$

---

## 📖 Resumen: Lo que debes recordar

| Concepto | Significado |
|:---------|:------------|
| $\log_b(x) = y$ | $b$ elevado a $y$ da $x$ |
| El logaritmo es... | El **exponente** al que hay que elevar la base |
| $\log_b(1) = 0$ | Siempre, porque $b^0 = 1$ |
| $\log_b(b) = 1$ | Siempre, porque $b^1 = b$ |
| Exponencial y logaritmo | Son operaciones **inversas** |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Si una bacteria se duplica cada hora y hay 32 bacterias, ¿cuántas horas han pasado?

<details>
<summary>Ver solución</summary>

Buscamos $t$ tal que $2^t = 32$.

$2^5 = 32$, entonces $\log_2(32) = 5$

Han pasado **5 horas**.

</details>

---

**Ejercicio 2:** Calcula $\log_3(81)$.

<details>
<summary>Ver solución</summary>

¿$3$ elevado a qué da $81$?

$3^1 = 3$, $3^2 = 9$, $3^3 = 27$, $3^4 = 81$ ✓

$\log_3(81) = 4$

</details>

---

**Ejercicio 3:** Calcula $\log_{10}(10000)$.

<details>
<summary>Ver solución</summary>

¿$10$ elevado a qué da $10000$?

$10^4 = 10000$

$\log_{10}(10000) = 4$

</details>

---

**Ejercicio 4:** ¿Cuánto vale $\log_7(1)$?

<details>
<summary>Ver solución</summary>

$\log_7(1) = 0$ porque $7^0 = 1$.

(Esto es verdad para cualquier base.)

</details>

---

**Ejercicio 5:** Si $\log_2(x) = 6$, ¿cuánto vale $x$?

<details>
<summary>Ver solución</summary>

Si $\log_2(x) = 6$, entonces $2^6 = x$.

$x = 64$

</details>

---
