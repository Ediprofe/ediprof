# 🔍 Comparación de Fracciones

En este tema aprenderemos diferentes métodos para comparar fracciones y determinar cuál es mayor o menor.

---

## 📖 Comparación con el mismo denominador

Cuando dos fracciones tienen el **mismo denominador**, la mayor es la que tiene el **mayor numerador**.

### Ejemplo 1

Comparar $\frac{5}{8}$ y $\frac{3}{8}$:

Como $5 > 3$ y ambas tienen denominador $8$:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div style="display: flex; justify-content: center; align-items: center; gap: 1rem;">
    <div style="text-align: center;">
      <div style="width: 100px;"><canvas id="chart-comp-58"></canvas></div>
      <p style="font-size: 12px; color: #374151; margin-top: 0.25rem;">5/8</p>
    </div>
    <span style="font-size: 1.5rem; color: #374151; font-weight: bold;">></span>
    <div style="text-align: center;">
      <div style="width: 100px;"><canvas id="chart-comp-38"></canvas></div>
      <p style="font-size: 12px; color: #374151; margin-top: 0.25rem;">3/8</p>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined') {
    // 5/8
    if (document.getElementById('chart-comp-58')) {
      new Chart(document.getElementById('chart-comp-58'), {
        type: 'pie', data: { labels: ['1','2','3','4','5','6','7','8'], datasets: [{ data: [1,1,1,1,1,1,1,1], backgroundColor: ['#3b82f6','#3b82f6','#3b82f6','#3b82f6','#3b82f6','#e5e7eb','#e5e7eb','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] },
        options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
      });
    }
    // 3/8
    if (document.getElementById('chart-comp-38')) {
      new Chart(document.getElementById('chart-comp-38'), {
        type: 'pie', data: { labels: ['1','2','3','4','5','6','7','8'], datasets: [{ data: [1,1,1,1,1,1,1,1], backgroundColor: ['#ef4444','#ef4444','#ef4444','#e5e7eb','#e5e7eb','#e5e7eb','#e5e7eb','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] },
        options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
      });
    }
  }
});
</script>

$$
\frac{5}{8} > \frac{3}{8}
$$

---

### Ejemplo 2

Comparar $\frac{7}{12}$ y $\frac{11}{12}$:

Como $7 < 11$:

$$
\frac{7}{12} < \frac{11}{12}
$$

---

## 📖 Comparación con el mismo numerador

Cuando dos fracciones tienen el **mismo numerador**, la mayor es la que tiene el **menor denominador**.

### Ejemplo 1

Comparar $\frac{3}{5}$ y $\frac{3}{7}$:

Como $5 < 7$ y ambas tienen numerador $3$:

$$
\frac{3}{5} > \frac{3}{7}
$$

---

### Ejemplo 2

Comparar $\frac{4}{9}$ y $\frac{4}{6}$:

Como $9 > 6$:

$$
\frac{4}{9} < \frac{4}{6}
$$

---

## 📖 Método del producto cruzado

Para comparar $\frac{a}{b}$ y $\frac{c}{d}$:

$$
a \times d \quad \Box \quad b \times c
$$

El símbolo que corresponde es el mismo para las fracciones.

### Ejemplo 1

Comparar $\frac{3}{4}$ y $\frac{5}{7}$:

$$
3 \times 7 = 21 \quad \text{y} \quad 4 \times 5 = 20
$$

Como $21 > 20$:

$$
\frac{3}{4} > \frac{5}{7}
$$

---

### Ejemplo 2

Comparar $\frac{2}{5}$ y $\frac{3}{7}$:

$$
2 \times 7 = 14 \quad \text{y} \quad 5 \times 3 = 15
$$

Como $14 < 15$:

$$
\frac{2}{5} < \frac{3}{7}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Ordena de menor a mayor: $\frac{2}{9}$, $\frac{5}{9}$, $\frac{8}{9}$

**Ejercicio 2:** Compara usando producto cruzado: $\frac{4}{5}$ y $\frac{7}{9}$

**Ejercicio 3:** ¿Cuál es mayor, $\frac{5}{6}$ o $\frac{7}{8}$?

**Ejercicio 4:** Ordena de mayor a menor: $\frac{3}{4}$, $\frac{3}{5}$, $\frac{3}{8}$

---
