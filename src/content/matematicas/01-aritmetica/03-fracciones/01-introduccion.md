# **Introducción a las Fracciones**

Imagina que tienes una pizza deliciosa pero tienes que compartirla con tus amigos. Si la cortas en pedazos iguales y repartes algunos, estás usando fracciones. Una fracción es simplemente una forma de decir "una parte de algo completo". No son monstruos matemáticos, son pedazos de realidad.

---

## 🎯 ¿Qué vas a aprender?

- Comprender el concepto de fracción como parte de una unidad.
- Identificar los elementos: Numerador y Denominador.
- Distinguir entre fracciones propias e impropias.
- Interpretar fracciones en contextos reales (comida, grupos).

---

## ¿Qué es una Fracción?

Una fracción representa una parte de un total.
Se escribe de la forma $\frac{a}{b}$, donde:

-   **Denominador ($b$):** En cuántas partes iguales dividimos el total (El número de abajo).
-   **Numerador ($a$):** Cuántas partes tomamos (El número de arriba).

$$ \text{Fracción} = \frac{\text{Partes que tomo}}{\text{Total de partes}} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: La Pizza
Dividimos una pizza en 8 rebanadas iguales y te comes 3.
-   Total de partes (Denominador): 8
-   Partes que tomas (Numerador): 3
**Fracción:** $\boxed{\frac{3}{8}}$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
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

#### Ejemplo 2: El grupo de clase
En un salón hay 12 estudiantes. 7 son mujeres.
-   Total (Denominador): 12
-   Mujeres (Numerador): 7
**Fracción:** $\boxed{\frac{7}{12}}$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
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

#### Ejemplo 3: Días de la semana
¿Qué fracción de la semana representan los días de fin de semana (sábado y domingo)?
-   Total días: 7
-   Fin de semana: 2
**Fracción:** $\boxed{\frac{2}{7}}$

#### Ejemplo 4: El chocolate
Tienes una barra de chocolate de 10 cuadros. Te comes 1.
**Fracción:** $\boxed{\frac{1}{10}}$

#### Ejemplo 5: El tanque de gasolina
Un tanque se divide en 4 cuartos. Si está lleno hasta la mitad (2 cuartos).
**Fracción:** $\boxed{\frac{2}{4}}$ (que es lo mismo que $\frac{1}{2}$).

---

## Tipos de Fracciones

Dependiendo de si tomamos menos, igual o más que la unidad, las fracciones tienen nombres.

### 1. Fracción Propia
El numerador es **menor** que el denominador ($a < b$). Representa **menos de 1 unidad**.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: $\frac{3}{5}$
Tomas 3 de 5 partes. No completas el total.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
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

#### Ejemplo 7: $\frac{2}{7}$
Tomas 2 de 7 partes. Es propia.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
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

#### Ejemplo 8: $\frac{1}{2}$
Tomas la mitad. 1 es menor que 2. Es propia.

#### Ejemplo 9: $\frac{99}{100}$
Casi llegas, pero 99 es menor que 100. Es propia.

#### Ejemplo 10: $\frac{0}{5}$
No tomas nada. 0 es menor que 5. Es propia.

---

### 2. Fracción Impropia
El numerador es **mayor o igual** que el denominador ($a \ge b$). Representa **1 unidad o más**.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 11: $\frac{7}{4}$
Tomas 7 cuartos. Como un entero solo tiene 4 cuartos, necesitas **dos pasteles** (uno entero y 3 pedazos del otro).

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

#### Ejemplo 12: $\frac{9}{9}$
Tomas todo. Es igual a 1 (La unidad completa). Se considera impropia (o fracción unidad).

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
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

#### Ejemplo 13: $\frac{10}{5}$
Tomas 10 quintos. $10 \div 5 = 2$. Son exactamente 2 unidades.

#### Ejemplo 14: $\frac{5}{4}$
Un poco más de 1 unidad ($1.25$).

#### Ejemplo 15: $\frac{100}{1}$
Son 100 enteros. Toda fracción es una división.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
En una caja de 6 huevos, usas 2 para el desayuno. Escribe la fracción de huevos usados.

<details>
<summary>Ver solución</summary>

-   Total: 6
-   Usados: 2
**Resultado:** $\boxed{\frac{2}{6}}$

</details>

### Ejercicio 2
Identifica el numerador y el denominador de $\frac{5}{9}$.

<details>
<summary>Ver solución</summary>

-   **Numerador:** 5 (arriba).
-   **Denominador:** 9 (abajo).

</details>

### Ejercicio 3
Clasifica $\frac{2}{3}$ como propia o impropia.

<details>
<summary>Ver solución</summary>

$2 < 3$. Es menor que 1.
**Resultado:** $\boxed{\text{Propia}}$

</details>

### Ejercicio 4
Clasifica $\frac{8}{5}$ como propia o impropia.

<details>
<summary>Ver solución</summary>

$8 > 5$. Es mayor que 1.
**Resultado:** $\boxed{\text{Impropia}}$

</details>

### Ejercicio 5
¿Cómo se lee la fracción $\frac{3}{4}$?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{\text{Tres cuartos}}$

</details>

### Ejercicio 6
Representa "cinco días de una semana" como fracción.

<details>
<summary>Ver solución</summary>

Una semana tiene 7 días.
**Resultado:** $\boxed{\frac{5}{7}}$

</details>

### Ejercicio 7
Clasifica $\frac{12}{12}$.

<details>
<summary>Ver solución</summary>

Numerador igual a denominador.
**Resultado:** $\boxed{\text{Impropia (o unidad)}}$

</details>

### Ejercicio 8
Si te comes 4 pedazos de una pizza de 8, ¿qué fracción quedó?

<details>
<summary>Ver solución</summary>

Quedan $8 - 4 = 4$ pedazos.
**Resultado:** $\boxed{\frac{4}{8}}$

</details>

### Ejercicio 9
Escribe una fracción impropia con denominador 3.

<details>
<summary>Ver solución</summary>

El numerador debe ser 3 o mayor. Ejemplos: $\frac{4}{3}, \frac{5}{3}, \frac{10}{3}$.
**Resultado:** $\boxed{\frac{4}{3} \text{ (ejemplo)}}$

</details>

### Ejercicio 10
¿Qué fracción representa 50 centavos de un peso (100 centavos)?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{\frac{50}{100}}$

</details>

---

## 🔑 Resumen

| Tipo | Numerador vs Denominador | Valor | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Propia** | Numerador < Denominador | Menor que 1 | $\frac{1}{2}$ |
| **Impropia** | Numerador >= Denominador | Mayor o igual que 1 | $\frac{3}{2}, \frac{5}{5}$ |

> **Conclusión:** Las fracciones son la forma matemática de compartir. Recuerda siempre: el denominador (abajo) dice "en cuántos cortamos" y el numerador (arriba) dice "cuántos tomamos".