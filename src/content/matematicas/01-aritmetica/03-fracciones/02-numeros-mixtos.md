# 🔄 Números Mixtos

En este tema aprenderemos qué son los números mixtos y cómo convertirlos a fracciones impropias y viceversa.

---

## 📖 ¿Qué es un número mixto?

Un **número mixto** combina un número entero con una fracción propia.

$$
a\frac{b}{c} = a + \frac{b}{c}
$$

### Ejemplo 1

$$
2\frac{3}{4} = 2 + \frac{3}{4}
$$

Gráficamente, esto se ve como **dos unidades completas** (círculos llenos) más **tres cuartos** de una tercera unidad:

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
    
    // Dos unidades completas
    new Chart(document.getElementById('chart-mixto1'), pieConfig(['#3b82f6','#3b82f6','#3b82f6','#3b82f6']));
    new Chart(document.getElementById('chart-mixto2'), pieConfig(['#3b82f6','#3b82f6','#3b82f6','#3b82f6']));
    // 3/4
    new Chart(document.getElementById('chart-mixto3'), pieConfig(['#3b82f6','#3b82f6','#3b82f6','#e5e7eb']));
  }
});
</script>

**Interpretación:** "Dos enteros y tres cuartos" o $2\frac{3}{4}$.

---

### Ejemplo 2

$$
5\frac{1}{2} = 5 + \frac{1}{2}
$$

Gráficamente: **cinco unidades completas** más **la mitad** de otra:

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

**Interpretación:** "Cinco enteros y un medio" o $5\frac{1}{2}$.

---

## 📖 De fracción impropia a número mixto

**Método:**
1. Divide el numerador entre el denominador
2. El cociente es la parte entera
3. El residuo es el nuevo numerador
4. El denominador permanece igual

### Ejemplo 1

Convertir $\frac{17}{5}$ a número mixto:

$$
17 \div 5 = 3 \text{ con residuo } 2
$$

$$
\frac{17}{5} = 3\frac{2}{5}
$$

---

### Ejemplo 2

Convertir $\frac{23}{6}$ a número mixto:

$$
23 \div 6 = 3 \text{ con residuo } 5
$$

$$
\frac{23}{6} = 3\frac{5}{6}
$$

---

## 📖 De número mixto a fracción impropia

**Fórmula:**

$$
a\frac{b}{c} = \frac{a \times c + b}{c}
$$

### Ejemplo 1

Convertir $4\frac{2}{3}$ a fracción impropia:

$$
4\frac{2}{3} = \frac{4 \times 3 + 2}{3} = \frac{14}{3}
$$

---

### Ejemplo 2

Convertir $2\frac{5}{7}$ a fracción impropia:

$$
2\frac{5}{7} = \frac{2 \times 7 + 5}{7} = \frac{19}{7}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Convierte a número mixto: $\frac{25}{4}$

**Ejercicio 2:** Convierte a número mixto: $\frac{31}{6}$

**Ejercicio 3:** Convierte a fracción impropia: $3\frac{2}{5}$

**Ejercicio 4:** Convierte a fracción impropia: $7\frac{3}{8}$

---