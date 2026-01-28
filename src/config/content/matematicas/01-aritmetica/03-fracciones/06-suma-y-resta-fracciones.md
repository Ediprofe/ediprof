---
title: "Suma y Resta de Fracciones"
---

# **Suma y Resta de Fracciones**

Sumar manzanas con manzanas es fácil, pero sumar manzanas con peras requiere convertirlas a "frutas". Con las fracciones pasa lo mismo: si tienen el mismo "apellido" (denominador) es directo, pero si no, primero debemos encontrar un terreno común.

---

## 🎯 ¿Qué vas a aprender?

- Sumar y restar fracciones homogéneas (mismo denominador).
- Sumar y restar fracciones heterogéneas (diferente denominador).
- Usar el MCM para encontrar el común denominador.
- El método de la "Carita Feliz" para sumas rápidas de dos fracciones.

---

## Fracciones con Mismo Denominador (Homogéneas)

Es como sumar rebanadas de pizzas del mismo tamaño.
**Regla:** Suma o resta los numeradores, y deja el denominador **igual**.

$$ \frac{a}{c} \pm \frac{b}{c} = \frac{a \pm b}{c} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Suma
$\frac{2}{7} + \frac{3}{7}$.
Sumamos los de arriba: $2+3=5$. Dejamos el 7.
$$ \boxed{\frac{5}{7}} $$

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

#### Ejemplo 2: Resta
$\frac{9}{10} - \frac{3}{10}$.
$9 - 3 = 6$.
$$ \frac{6}{10} \implies \text{simplificando} \implies \boxed{\frac{3}{5}} $$

#### Ejemplo 3: Suma y simplificación
$\frac{1}{8} + \frac{3}{8} = \frac{4}{8}$.
Simplificamos la mitad:
$$ \boxed{\frac{1}{2}} $$

#### Ejemplo 4: Suma de tres fracciones
$\frac{2}{9} + \frac{4}{9} + \frac{1}{9} = \frac{7}{9}$.

#### Ejemplo 5: Resta que da cero
$\frac{5}{5} - \frac{5}{5} = \frac{0}{5} = \boxed{0}$.

---

## Fracciones con Diferente Denominador (Heterogéneas)

Aquí no podemos sumar directo. Necesitamos un **Común Denominador** (usando el MCM).

**Método General (MCM):**
1. Calcula el MCM de los denominadores.
2. Amplifica cada fracción para que tenga ese denominador.
3. Suma o resta normalmente.

**Método Carita Feliz (rápido para 2 fracciones):**
$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: $\frac{1}{2} + \frac{1}{3}$
-   MCM(2, 3) = 6.
-   $\frac{1}{2} = \frac{3}{6}$ y $\frac{1}{3} = \frac{2}{6}$.
-   $\frac{3+2}{6} = \boxed{\frac{5}{6}}$.
*(O carita feliz: $1\times3 + 2\times1$ sobre $2\times3$).*

#### Ejemplo 7: $\frac{3}{4} - \frac{1}{6}$
-   MCM(4, 6) = 12.
-   $\frac{3}{4} \to \frac{9}{12}$.
-   $\frac{1}{6} \to \frac{2}{12}$.
-   $\frac{9-2}{12} = \boxed{\frac{7}{12}}$.

#### Ejemplo 8: $\frac{2}{5} + \frac{1}{10}$
-   MCM(5, 10) = 10.
-   $\frac{2}{5} = \frac{4}{10}$.
-   $\frac{4}{10} + \frac{1}{10} = \frac{5}{10} = \boxed{\frac{1}{2}}$.

#### Ejemplo 9: Carita Feliz $\frac{1}{4} + \frac{2}{5}$
-   Cruzado: $1\times5 = 5$.
-   Cruzado: $4\times2 = 8$.
-   Abajo: $4\times5 = 20$.
-   Suma: $\frac{5+8}{20} = \boxed{\frac{13}{20}}$.

#### Ejemplo 10: Suma de mixto con fracción
$1\frac{1}{2} + \frac{1}{4}$.
Convertimos mixto: $\frac{3}{2} + \frac{1}{4}$.
MCM = 4.
$\frac{6}{4} + \frac{1}{4} = \boxed{\frac{7}{4}}$.

---

## 📝 Ejercicios de Práctica

### Ejemplo 1
$\frac{2}{5} + \frac{1}{5}$.

<details>
<summary>Ver solución</summary>

Mismo denominador.
**Resultado:** $\boxed{\frac{3}{5}}$

</details>

### Ejemplo 2
$\frac{7}{8} - \frac{3}{8}$.

<details>
<summary>Ver solución</summary>

$\frac{4}{8} = \frac{1}{2}$.
**Resultado:** $\boxed{\frac{1}{2}}$

</details>

### Ejemplo 3
$\frac{1}{2} + \frac{1}{4}$.

<details>
<summary>Ver solución</summary>

$\frac{2}{4} + \frac{1}{4}$.
**Resultado:** $\boxed{\frac{3}{4}}$

</details>

### Ejemplo 4
$\frac{1}{3} + \frac{1}{5}$.

<details>
<summary>Ver solución</summary>

Carita feliz: $\frac{5+3}{15}$.
**Resultado:** $\boxed{\frac{8}{15}}$

</details>

### Ejemplo 5
$\frac{2}{3} - \frac{1}{6}$.

<details>
<summary>Ver solución</summary>

$\frac{4}{6} - \frac{1}{6} = \frac{3}{6} = \frac{1}{2}$.
**Resultado:** $\boxed{\frac{1}{2}}$

</details>

### Ejemplo 6
$\frac{3}{4} + \frac{2}{3}$.

<details>
<summary>Ver solución</summary>

$\frac{9+8}{12} = \frac{17}{12}$.
**Resultado:** $\boxed{\frac{17}{12}}$

</details>

### Ejemplo 7
$\frac{4}{5} - \frac{1}{2}$.

<details>
<summary>Ver solución</summary>

$\frac{8-5}{10}$.
**Resultado:** $\boxed{\frac{3}{10}}$

</details>

### Ejemplo 8
$\frac{5}{12} + \frac{1}{12} + \frac{6}{12}$.

<details>
<summary>Ver solución</summary>

$\frac{12}{12} = 1$.
**Resultado:** $\boxed{1}$

</details>

### Ejemplo 9
Si tienes $\frac{1}{2}$ litro de leche y compras $\frac{1}{4}$ más.

<details>
<summary>Ver solución</summary>

$\frac{2}{4} + \frac{1}{4} = \frac{3}{4}$.
**Resultado:** $\boxed{\frac{3}{4} \text{ litros}}$

</details>

### Ejemplo 10
$\frac{1}{2} - \frac{1}{3}$.

<details>
<summary>Ver solución</summary>

$\frac{3-2}{6}$.
**Resultado:** $\boxed{\frac{1}{6}}$

</details>

---

## 🔑 Resumen

| Tipo | Procedimiento |
| :--- | :--- |
| **Homogéneas** | Sumar numeradores directo. Denominador igual. |
| **Heterogéneas** | Buscar MCM, amplificar y luego sumar. |
| **Truco (2 frac)** | Carita feliz ($\frac{ad+bc}{bd}$). |

> **Conclusión:** Jamás sumes los denominadores ($\frac{1}{2} + \frac{1}{2} \neq \frac{2}{4}$). Recuerda siempre encontrar un común acuerdo (denominador) antes de operar.
