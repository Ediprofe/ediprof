# **Números Mixtos**

A veces, una sola pizza no alcanza. Cuando necesitamos más de una unidad completa, usamos **números mixtos**. Un número mixto es la mezcla perfecta entre un número entero (las pizzas enteras) y una fracción propia (las rebanadas sueltas). Son otra forma de escribir las fracciones impropias.

---

## 🎯 ¿Qué vas a aprender?

- Qué es un número mixto y cómo se forma.
- Convertir fracciones impropias a números mixtos (de "todo fracción" a "enteros y sobras").
- Convertir números mixtos a fracciones impropias (de vuelta a "todo fracción").
- Visualizar cantidades mayores a la unidad.

---

## ¿Qué es un Número Mixto?

Es una expresión formada por una **parte entera** y una **parte fraccionaria**.

$$ \text{Mixto} = \text{Entero} + \text{Fracción} = A\frac{b}{c} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: $2\frac{3}{4}$
Significa que tienes 2 enteros completos y $\frac{3}{4}$ de otro.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div style="display: flex; justify-content: center; align-items: center; gap: 0.5rem; flex-wrap: wrap;">
    <div style="text-align: center;">
      <div style="width: 80px;"><canvas id="chart-mixto1"></canvas></div>
      <p style="font-size: 12px; color: #374151; margin-top: 0.25rem;">1</p>
    </div>
    <span style="font-size: 1.5rem; color: #374151;">+</span>
    <div style="text-align: center;">
      <div style="width: 80px;"><canvas id="chart-mixto2"></canvas></div>
      <p style="font-size: 12px; color: #374151; margin-top: 0.25rem;">1</p>
    </div>
    <span style="font-size: 1.5rem; color: #374151;">+</span>
    <div style="text-align: center;">
      <div style="width: 80px;"><canvas id="chart-mixto3"></canvas></div>
      <p style="font-size: 12px; color: #374151; margin-top: 0.25rem;">3/4</p>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined') {
    var pieConfig = function(colors) {
      return {
        type: 'pie',
        data: { labels: ['1','2','3','4'], datasets: [{ data: [1,1,1,1], backgroundColor: colors, borderColor: '#374151', borderWidth: 2 }] },
        options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
      };
    };
    new Chart(document.getElementById('chart-mixto1'), pieConfig(['#3b82f6','#3b82f6','#3b82f6','#3b82f6']));
    new Chart(document.getElementById('chart-mixto2'), pieConfig(['#3b82f6','#3b82f6','#3b82f6','#3b82f6']));
    new Chart(document.getElementById('chart-mixto3'), pieConfig(['#3b82f6','#3b82f6','#3b82f6','#e5e7eb']));
  }
});
</script>

#### Ejemplo 2: $5\frac{1}{2}$
Cinco enteros y medio.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div style="display: flex; justify-content: center; align-items: center; gap: 0.3rem; flex-wrap: wrap;">
    <div style="width: 50px;"><canvas id="chart-mixto-5a"></canvas></div>
    <div style="width: 50px;"><canvas id="chart-mixto-5b"></canvas></div>
    <div style="width: 50px;"><canvas id="chart-mixto-5c"></canvas></div>
    <div style="width: 50px;"><canvas id="chart-mixto-5d"></canvas></div>
    <div style="width: 50px;"><canvas id="chart-mixto-5e"></canvas></div>
    <span style="font-size: 1rem; color: #374151;">+</span>
    <div style="width: 50px;"><canvas id="chart-mixto-5f"></canvas></div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined') {
    var fullPie = { type: 'pie', data: { labels: ['1','2'], datasets: [{ data: [1,1], backgroundColor: ['#22c55e','#22c55e'], borderColor: '#374151', borderWidth: 2 }] }, options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } } };
    ['chart-mixto-5a','chart-mixto-5b','chart-mixto-5c','chart-mixto-5d','chart-mixto-5e'].forEach(function(id) {
      if (document.getElementById(id)) new Chart(document.getElementById(id), fullPie);
    });
    if (document.getElementById('chart-mixto-5f')) {
      new Chart(document.getElementById('chart-mixto-5f'), { type: 'pie', data: { labels: ['1','2'], datasets: [{ data: [1,1], backgroundColor: ['#22c55e','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] }, options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } } });
    }
  }
});
</script>

#### Ejemplo 3: $1\frac{1}{3}$
Un entero y un tercio.

#### Ejemplo 4: $3\frac{3}{4}$ horas
Tres horas completas y tres cuartos de hora (45 minutos).

#### Ejemplo 5: Edad
"Tengo 7 años y medio" = $7\frac{1}{2}$.

---

## Convertir Fracción Impropia a Mixto

Dividimos el numerador entre el denominador. El cociente es el **entero**, el residuo es el nuevo **numerador**.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: Convertir $\frac{17}{5}$
1.  Dividimos: $17 \div 5$.
2.  Cabe 3 veces ($3 \times 5 = 15$). Sobran 2.
3.  Entero: 3. Numerador: 2. Denominador: 5 (sigue igual).
**Resultado:** $\boxed{3\frac{2}{5}}$

#### Ejemplo 7: Convertir $\frac{23}{6}$
1.  $23 \div 6 = 3$ (porque $6 \times 3 = 18$).
2.  Sobra $23 - 18 = 5$.
**Resultado:** $\boxed{3\frac{5}{6}}$

#### Ejemplo 8: Convertir $\frac{11}{4}$
1.  $11 \div 4 = 2$ (sobran 3).
**Resultado:** $\boxed{2\frac{3}{4}}$

#### Ejemplo 9: Convertir $\frac{9}{2}$
1.  $9 \div 2 = 4$ (sobra 1).
**Resultado:** $\boxed{4\frac{1}{2}}$

#### Ejemplo 10: Convertir $\frac{5}{5}$
1.  $5 \div 5 = 1$ (sobra 0).
**Resultado:** $\boxed{1}$ (Es un entero, no hay parte fraccionaria).

---

## Convertir Número Mixto a Fracción Impropia

Multiplicamos el entero por el denominador y sumamos el numerador. El denominador se mantiene.

$$ \text{Numerador Final} = (\text{Entero} \times \text{Denominador}) + \text{Numerador} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 11: Convertir $4\frac{2}{3}$
1.  Multiplico: $4 \times 3 = 12$.
2.  Sumo numerador: $12 + 2 = 14$.
3.  Denominador igual: 3.
**Resultado:** $\boxed{\frac{14}{3}}$

#### Ejemplo 12: Convertir $2\frac{5}{7}$
1.  $2 \times 7 = 14$.
2.  $14 + 5 = 19$.
**Resultado:** $\boxed{\frac{19}{7}}$

#### Ejemplo 13: Convertir $1\frac{1}{2}$
1.  $1 \times 2 = 2$.
2.  $2 + 1 = 3$.
**Resultado:** $\boxed{\frac{3}{2}}$

#### Ejemplo 14: Convertir $10\frac{1}{10}$
1.  $10 \times 10 = 100$.
2.  $100 + 1 = 101$.
**Resultado:** $\boxed{\frac{101}{10}}$

#### Ejemplo 15: Convertir $3\frac{3}{4}$
1.  $3 \times 4 = 12$.
2.  $12 + 3 = 15$.
**Resultado:** $\boxed{\frac{15}{4}}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Convierte $\frac{25}{4}$ a número mixto.

<details>
<summary>Ver solución</summary>

$25 \div 4 = 6$ (sobra 1).
**Resultado:** $\boxed{6\frac{1}{4}}$

</details>

### Ejercicio 2
Convierte $\frac{31}{6}$ a número mixto.

<details>
<summary>Ver solución</summary>

$31 \div 6 = 5$ (sobra 1).
**Resultado:** $\boxed{5\frac{1}{6}}$

</details>

### Ejercicio 3
Convierte $3\frac{2}{5}$ a fracción impropia.

<details>
<summary>Ver solución</summary>

$3 \times 5 + 2 = 17$.
**Resultado:** $\boxed{\frac{17}{5}}$

</details>

### Ejercicio 4
Convierte $7\frac{3}{8}$ a fracción impropia.

<details>
<summary>Ver solución</summary>

$7 \times 8 + 3 = 59$.
**Resultado:** $\boxed{\frac{59}{8}}$

</details>

### Ejercicio 5
Convierte $\frac{100}{9}$ a mixto.

<details>
<summary>Ver solución</summary>

$100 \div 9 = 11$ (sobra 1).
**Resultado:** $\boxed{11\frac{1}{9}}$

</details>

### Ejercicio 6
Convierte $5\frac{5}{6}$ a impropia.

<details>
<summary>Ver solución</summary>

$5 \times 6 + 5 = 35$.
**Resultado:** $\boxed{\frac{35}{6}}$

</details>

### Ejercicio 7
¿Qué número es mayor: $3\frac{1}{2}$ o $\frac{7}{2}$?

<details>
<summary>Ver solución</summary>

Convertimos $3\frac{1}{2} = \frac{7}{2}$.
**Resultado:** $\boxed{\text{Son iguales}}$

</details>

### Ejercicio 8
Convierte $\frac{15}{2}$ a mixto.

<details>
<summary>Ver solución</summary>

$15 \div 2 = 7$ (sobra 1).
**Resultado:** $\boxed{7\frac{1}{2}}$

</details>

### Ejercicio 9
Convierte $1\frac{7}{8}$ a impropia.

<details>
<summary>Ver solución</summary>

$1 \times 8 + 7 = 15$.
**Resultado:** $\boxed{\frac{15}{8}}$

</details>

### Ejercicio 10
Si tienes $2\frac{1}{4}$ pizzas, ¿cuántos cuartos de pizza tienes?

<details>
<summary>Ver solución</summary>

Convertimos a impropia: $2 \times 4 + 1 = 9$.
**Resultado:** $\boxed{9 \text{ cuartos}}$

</details>

---

## 🔑 Resumen

| Conversión | Procedimiento | Fórmula |
| :--- | :--- | :--- |
| **Impropia $\to$ Mixto** | Dividir numerador entre denominador. | $C \frac{R}{D}$ |
| **Mixto $\to$ Impropia** | Multiplicar entero por denominador y sumar numerador. | $\frac{E \times D + N}{D}$ |

> **Conclusión:** Los números mixtos son fáciles de entender en la vida real ("dos pasteles y medio"), pero las fracciones impropias son más fáciles para hacer cálculos matemáticos.