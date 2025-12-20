# ✖️ Multiplicación y División de Fracciones

En este tema aprenderemos a multiplicar y dividir fracciones.

---

## 📖 Multiplicación de fracciones

Multiplicamos **numerador con numerador** y **denominador con denominador**.

$$
\frac{a}{b} \times \frac{c}{d} = \frac{a \times c}{b \times d}
$$

### Ejemplo 1

$$
\frac{2}{3} \times \frac{4}{5} = \frac{2 \times 4}{3 \times 5} = \frac{8}{15}
$$

Multiplicar $\frac{2}{3}$ por $\frac{4}{5}$ significa tomar **2/3 de 4/5**:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div style="display: flex; justify-content: center; align-items: center; gap: 0.5rem;">
    <div style="text-align: center;">
      <div style="width: 80px;"><canvas id="chart-mult-23"></canvas></div>
      <p style="font-size: 11px; color: #374151;">2/3</p>
    </div>
    <span style="font-size: 1rem; color: #374151;">de</span>
    <div style="text-align: center;">
      <div style="width: 80px;"><canvas id="chart-mult-45"></canvas></div>
      <p style="font-size: 11px; color: #374151;">4/5</p>
    </div>
    <span style="font-size: 1rem; color: #374151;">=</span>
    <div style="text-align: center;">
      <div style="width: 80px;"><canvas id="chart-mult-815"></canvas></div>
      <p style="font-size: 11px; color: #22c55e; font-weight: bold;">8/15</p>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined') {
    if (document.getElementById('chart-mult-23')) {
      new Chart(document.getElementById('chart-mult-23'), { type: 'pie', data: { labels: ['1','2','3'], datasets: [{ data: [1,1,1], backgroundColor: ['#3b82f6','#3b82f6','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] }, options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } } });
    }
    if (document.getElementById('chart-mult-45')) {
      new Chart(document.getElementById('chart-mult-45'), { type: 'pie', data: { labels: ['1','2','3','4','5'], datasets: [{ data: [1,1,1,1,1], backgroundColor: ['#ef4444','#ef4444','#ef4444','#ef4444','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] }, options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } } });
    }
    if (document.getElementById('chart-mult-815')) {
      var colors15 = [];
      for (var i = 0; i < 15; i++) colors15.push(i < 8 ? '#22c55e' : '#e5e7eb');
      new Chart(document.getElementById('chart-mult-815'), { type: 'pie', data: { labels: Array(15).fill(''), datasets: [{ data: Array(15).fill(1), backgroundColor: colors15, borderColor: '#374151', borderWidth: 1 }] }, options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } } });
    }
  }
});
</script>

---

### Ejemplo 2

$$
\frac{3}{4} \times \frac{2}{7} = \frac{3 \times 2}{4 \times 7} = \frac{6}{28} = \frac{3}{14}
$$

---

## 📖 Multiplicar fracción por entero

El entero se escribe como fracción con denominador $1$.

### Ejemplo 1

$$
\frac{3}{4} \times 5 = \frac{3}{4} \times \frac{5}{1} = \frac{15}{4} = 3\frac{3}{4}
$$

---

### Ejemplo 2

$$
\frac{2}{5} \times 10 = \frac{2 \times 10}{5} = \frac{20}{5} = 4
$$

---

## 📖 División de fracciones

Para dividir, multiplicamos por el **recíproco** de la segunda fracción.

$$
\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c}
$$

### Ejemplo 1

$$
\frac{3}{4} \div \frac{2}{5} = \frac{3}{4} \times \frac{5}{2} = \frac{15}{8} = 1\frac{7}{8}
$$

---

### Ejemplo 2

$$
\frac{5}{6} \div \frac{1}{3} = \frac{5}{6} \times \frac{3}{1} = \frac{15}{6} = \frac{5}{2} = 2\frac{1}{2}
$$

---

## 📖 Recíproco de una fracción

El **recíproco** de $\frac{a}{b}$ es $\frac{b}{a}$.

| Fracción | Recíproco |
|----------|-----------|
| $\frac{2}{3}$ | $\frac{3}{2}$ |
| $\frac{5}{7}$ | $\frac{7}{5}$ |
| $4 = \frac{4}{1}$ | $\frac{1}{4}$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** $\frac{2}{5} \times \frac{3}{7}$

**Ejercicio 2:** $\frac{4}{9} \times 6$

**Ejercicio 3:** $\frac{5}{8} \div \frac{3}{4}$

**Ejercicio 4:** $\frac{7}{10} \div \frac{2}{5}$

---
