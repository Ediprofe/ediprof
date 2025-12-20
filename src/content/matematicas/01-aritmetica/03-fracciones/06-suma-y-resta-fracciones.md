# ➕ Suma y Resta de Fracciones

En este tema aprenderemos a sumar y restar fracciones, tanto con igual denominador como con denominadores diferentes.

---

## 📖 Suma con el mismo denominador

Cuando las fracciones tienen el **mismo denominador**, sumamos los numeradores y mantenemos el denominador.

$$
\frac{a}{c} + \frac{b}{c} = \frac{a + b}{c}
$$

### Ejemplo 1

$$
\frac{2}{7} + \frac{3}{7} = \frac{2 + 3}{7} = \frac{5}{7}
$$

Visualmente: combinamos las partes de ambas fracciones:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div style="display: flex; justify-content: center; align-items: center; gap: 0.5rem; flex-wrap: wrap;">
    <div style="text-align: center;">
      <div style="width: 70px;"><canvas id="chart-suma-27"></canvas></div>
      <p style="font-size: 11px; color: #374151;">2/7</p>
    </div>
    <span style="font-size: 1.2rem; color: #374151;">+</span>
    <div style="text-align: center;">
      <div style="width: 70px;"><canvas id="chart-suma-37"></canvas></div>
      <p style="font-size: 11px; color: #374151;">3/7</p>
    </div>
    <span style="font-size: 1.2rem; color: #374151;">=</span>
    <div style="text-align: center;">
      <div style="width: 70px;"><canvas id="chart-suma-57"></canvas></div>
      <p style="font-size: 11px; color: #22c55e; font-weight: bold;">5/7</p>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined') {
    var labels7 = ['1','2','3','4','5','6','7'];
    var data7 = [1,1,1,1,1,1,1];
    if (document.getElementById('chart-suma-27')) {
      new Chart(document.getElementById('chart-suma-27'), { type: 'pie', data: { labels: labels7, datasets: [{ data: data7, backgroundColor: ['#3b82f6','#3b82f6','#e5e7eb','#e5e7eb','#e5e7eb','#e5e7eb','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] }, options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } } });
    }
    if (document.getElementById('chart-suma-37')) {
      new Chart(document.getElementById('chart-suma-37'), { type: 'pie', data: { labels: labels7, datasets: [{ data: data7, backgroundColor: ['#ef4444','#ef4444','#ef4444','#e5e7eb','#e5e7eb','#e5e7eb','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] }, options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } } });
    }
    if (document.getElementById('chart-suma-57')) {
      new Chart(document.getElementById('chart-suma-57'), { type: 'pie', data: { labels: labels7, datasets: [{ data: data7, backgroundColor: ['#22c55e','#22c55e','#22c55e','#22c55e','#22c55e','#e5e7eb','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] }, options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } } });
    }
  }
});
</script>

---

### Ejemplo 2

$$
\frac{4}{9} + \frac{2}{9} = \frac{4 + 2}{9} = \frac{6}{9} = \frac{2}{3}
$$

---

## 📖 Resta con el mismo denominador

Restamos los numeradores y mantenemos el denominador.

$$
\frac{a}{c} - \frac{b}{c} = \frac{a - b}{c}
$$

### Ejemplo 1

$$
\frac{5}{8} - \frac{2}{8} = \frac{5 - 2}{8} = \frac{3}{8}
$$

---

### Ejemplo 2

$$
\frac{7}{10} - \frac{3}{10} = \frac{7 - 3}{10} = \frac{4}{10} = \frac{2}{5}
$$

---

## 📖 Suma con diferente denominador

Debemos convertir las fracciones a un **denominador común** (usando el MCM).

### Ejemplo 1

Calcular $\frac{2}{3} + \frac{1}{4}$

MCM$(3, 4) = 12$

$$
\frac{2}{3} = \frac{8}{12} \quad \text{y} \quad \frac{1}{4} = \frac{3}{12}
$$

$$
\frac{8}{12} + \frac{3}{12} = \frac{11}{12}
$$

---

### Ejemplo 2

Calcular $\frac{1}{2} + \frac{2}{5}$

MCM$(2, 5) = 10$

$$
\frac{1}{2} = \frac{5}{10} \quad \text{y} \quad \frac{2}{5} = \frac{4}{10}
$$

$$
\frac{5}{10} + \frac{4}{10} = \frac{9}{10}
$$

---

## 📖 Resta con diferente denominador

El mismo proceso: denominador común y luego restar.

### Ejemplo 1

Calcular $\frac{5}{6} - \frac{1}{4}$

MCM$(6, 4) = 12$

$$
\frac{5}{6} = \frac{10}{12} \quad \text{y} \quad \frac{1}{4} = \frac{3}{12}
$$

$$
\frac{10}{12} - \frac{3}{12} = \frac{7}{12}
$$

---

### Ejemplo 2

Calcular $\frac{3}{4} - \frac{1}{3}$

MCM$(4, 3) = 12$

$$
\frac{3}{4} = \frac{9}{12} \quad \text{y} \quad \frac{1}{3} = \frac{4}{12}
$$

$$
\frac{9}{12} - \frac{4}{12} = \frac{5}{12}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** $\frac{3}{8} + \frac{4}{8}$

**Ejercicio 2:** $\frac{1}{3} + \frac{1}{4}$

**Ejercicio 3:** $\frac{5}{6} - \frac{1}{2}$

**Ejercicio 4:** $\frac{7}{10} - \frac{2}{5}$

---
