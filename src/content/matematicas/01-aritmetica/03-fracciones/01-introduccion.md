# 🍕 Introducción a las Fracciones

En este tema aprenderemos qué son las fracciones, sus elementos y cómo interpretarlas en diferentes contextos.

---

## 📖 ¿Qué es una fracción?

Una **fracción** representa una o más partes iguales de una unidad o cantidad.

$$
\text{Fracción} = \frac{a}{b}
$$

Donde:
* $a$ se llama **numerador** (indica cuántas partes tomamos)
* $b$ se llama **denominador** (indica en cuántas partes iguales se divide la unidad)

### Ejemplo 1

Si dividimos una pizza en $8$ partes iguales y tomamos $3$:

$$
\frac{3}{8}
$$

En la siguiente figura, las **porciones azules** representan las partes que tomamos, mientras que las **porciones grises** son las que quedan:

<div style="max-width: 250px; margin: 1.5rem auto;">
  <canvas id="chart-pizza-38"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined') {
    new Chart(document.getElementById('chart-pizza-38'), {
      type: 'pie',
      data: {
        labels: ['1', '2', '3', '4', '5', '6', '7', '8'],
        datasets: [{
          data: [1, 1, 1, 1, 1, 1, 1, 1],
          backgroundColor: ['#3b82f6', '#3b82f6', '#3b82f6', '#e5e7eb', '#e5e7eb', '#e5e7eb', '#e5e7eb', '#e5e7eb'],
          borderColor: '#374151',
          borderWidth: 2
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false },
          title: { display: true, text: '3/8 de la pizza', font: { size: 16, weight: 'bold' } },
          tooltip: { enabled: false }
        }
      }
    });
  }
});
</script>

**Interpretación:** "Tres de ocho partes" o "tres octavos" de la pizza.

---

### Ejemplo 2

En un grupo de $12$ estudiantes, $7$ son mujeres:

$$
\frac{7}{12}
$$

En el gráfico, las **porciones azules** representan a las mujeres y las **grises** a los hombres:

<div style="max-width: 220px; margin: 1rem auto;">
  <canvas id="chart-estudiantes"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined' && document.getElementById('chart-estudiantes')) {
    new Chart(document.getElementById('chart-estudiantes'), {
      type: 'pie',
      data: { labels: ['1','2','3','4','5','6','7','8','9','10','11','12'], datasets: [{ data: [1,1,1,1,1,1,1,1,1,1,1,1], backgroundColor: ['#3b82f6','#3b82f6','#3b82f6','#3b82f6','#3b82f6','#3b82f6','#3b82f6','#e5e7eb','#e5e7eb','#e5e7eb','#e5e7eb','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] },
      options: { responsive: true, plugins: { legend: { display: false }, title: { display: true, text: '7 de 12 estudiantes', font: { size: 14, weight: 'bold' } }, tooltip: { enabled: false } } }
    });
  }
});
</script>

**Interpretación:** "$7$ de cada $12$ estudiantes son mujeres".

---

## 📖 Tipos de fracciones

### Fracción propia

El numerador es **menor** que el denominador. Su valor es menor que $1$.

### Ejemplo 1: $\frac{3}{5}$

Tomamos 3 partes de un total de 5:

<div style="max-width: 180px; margin: 1rem auto;">
  <canvas id="chart-propia-35"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined' && document.getElementById('chart-propia-35')) {
    new Chart(document.getElementById('chart-propia-35'), {
      type: 'pie',
      data: { labels: ['1','2','3','4','5'], datasets: [{ data: [1,1,1,1,1], backgroundColor: ['#3b82f6','#3b82f6','#3b82f6','#e5e7eb','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] },
      options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
    });
  }
});
</script>

Como 3 < 5, la fracción es **menor que 1** (no llenamos todo el círculo).

### Ejemplo 2: $\frac{2}{7}$

Tomamos solo 2 partes de un total de 7:

<div style="max-width: 180px; margin: 1rem auto;">
  <canvas id="chart-propia-27"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined' && document.getElementById('chart-propia-27')) {
    new Chart(document.getElementById('chart-propia-27'), {
      type: 'pie',
      data: { labels: ['1','2','3','4','5','6','7'], datasets: [{ data: [1,1,1,1,1,1,1], backgroundColor: ['#3b82f6','#3b82f6','#e5e7eb','#e5e7eb','#e5e7eb','#e5e7eb','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] },
      options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
    });
  }
});
</script>

Como 2 < 7, esta también es una fracción **propia**.

---

### Fracción impropia

El numerador es **mayor o igual** que el denominador. Su valor es mayor o igual a $1$.

### Ejemplo 1: $\frac{7}{4}$

Necesitamos más de una unidad: $7 \div 4 = 1$ unidad completa más $\frac{3}{4}$:

<div style="display: flex; justify-content: center; align-items: center; gap: 0.5rem; margin: 1rem auto;">
  <div style="width: 80px;"><canvas id="chart-impropia-74a"></canvas></div>
  <span style="font-size: 1.2rem; color: #374151;">+</span>
  <div style="width: 80px;"><canvas id="chart-impropia-74b"></canvas></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined') {
    if (document.getElementById('chart-impropia-74a')) {
      new Chart(document.getElementById('chart-impropia-74a'), {
        type: 'pie', data: { labels: ['1','2','3','4'], datasets: [{ data: [1,1,1,1], backgroundColor: ['#ef4444','#ef4444','#ef4444','#ef4444'], borderColor: '#374151', borderWidth: 2 }] },
        options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
      });
    }
    if (document.getElementById('chart-impropia-74b')) {
      new Chart(document.getElementById('chart-impropia-74b'), {
        type: 'pie', data: { labels: ['1','2','3','4'], datasets: [{ data: [1,1,1,1], backgroundColor: ['#ef4444','#ef4444','#ef4444','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] },
        options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
      });
    }
  }
});
</script>

Como 7 > 4, es una fracción **impropia** (mayor que 1).

### Ejemplo 2: $\frac{9}{9}$

Cuando numerador y denominador son iguales, la fracción es exactamente 1:

<div style="max-width: 150px; margin: 1rem auto;">
  <canvas id="chart-impropia-99"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined' && document.getElementById('chart-impropia-99')) {
    new Chart(document.getElementById('chart-impropia-99'), {
      type: 'pie', data: { labels: ['1','2','3','4','5','6','7','8','9'], datasets: [{ data: [1,1,1,1,1,1,1,1,1], backgroundColor: ['#22c55e','#22c55e','#22c55e','#22c55e','#22c55e','#22c55e','#22c55e','#22c55e','#22c55e'], borderColor: '#374151', borderWidth: 2 }] },
      options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
    });
  }
});
</script>

$\frac{9}{9} = 1$ (el círculo completo está lleno).

--- 


> 💡 **Resumen:** La fracción **propia** (azul) es siempre menor que 1, mientras que la **impropia** (roja/verde) es igual o mayor que 1.

---

## 📖 Interpretaciones de una fracción

### Como parte de un todo

$$
\frac{3}{4} \text{ de una pizza significa } 3 \text{ de } 4 \text{ rebanadas}
$$

### Como división

$$
\frac{3}{4} = 3 \div 4 = 0.75
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Identifica el numerador y denominador de $\frac{5}{9}$ y explica qué representa.

**Ejercicio 2:** Clasifica como propia o impropia: $\frac{8}{5}$, $\frac{3}{7}$, $\frac{6}{6}$.

**Ejercicio 3:** María comió $2$ rebanadas de un pastel de $10$ rebanadas. Expresa esto como fracción.

**Ejercicio 4:** Expresa $\frac{5}{8}$ como decimal.

---