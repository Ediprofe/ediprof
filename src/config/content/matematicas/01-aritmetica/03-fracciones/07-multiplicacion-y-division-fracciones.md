---
title: "Multiplicación y División de Fracciones"
---

# **Multiplicación y División de Fracciones**

Multiplicar fracciones es la operación más fácil del mundo (solo se trata de seguir la línea). Dividirlas, en cambio, tiene un pequeño truco de magia: ¡se convierte en una multiplicación!

---

## 🎯 ¿Qué vas a aprender?

- Multiplicar fracciones (numerador con numerador, denominador con denominador).
- Multiplicar una fracción por un número entero.
- Dividir fracciones usando el truco del "Inverso" (o "Vuelta de Carnero").
- Simplificar resultados finales.

---

## Multiplicación de Fracciones

Es directa. Lo de arriba por lo de arriba, lo de abajo por lo de abajo.

$$ \frac{a}{b} \times \frac{c}{d} = \frac{a \times c}{b \times d} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: $\frac{2}{3} \times \frac{4}{5}$
-   Arriba: $2 \times 4 = 8$.
-   Abajo: $3 \times 5 = 15$.
**Resultado:** $\boxed{\frac{8}{15}}$

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

#### Ejemplo 2: $\frac{1}{2} \times \frac{1}{2}$ (La mitad de la mitad)
-   $1 \times 1 = 1$.
-   $2 \times 2 = 4$.
**Resultado:** $\boxed{\frac{1}{4}}$ (un cuarto).

#### Ejemplo 3: $\frac{3}{4} \times \frac{2}{7}$
-   $3 \times 2 = 6$.
-   $4 \times 7 = 28$.
$\frac{6}{28} \implies \text{simplificamos} \implies \boxed{\frac{3}{14}}$.

#### Ejemplo 4: Multiplicar por un Entero ($5 \times \frac{3}{4}$)
Imagina que el 5 tiene un 1 abajo: $\frac{5}{1} \times \frac{3}{4}$.
-   $5 \times 3 = 15$.
-   $1 \times 4 = 4$.
**Resultado:** $\boxed{\frac{15}{4}}$ (o $3\frac{3}{4}$).

#### Ejemplo 5: $\frac{10}{3} \times \frac{3}{5}$
-   $10 \times 3 = 30$.
-   $3 \times 5 = 15$.
$30 \div 15 = 2$.
**Resultado:** $\boxed{2}$

---

## División de Fracciones

Para dividir $\frac{a}{b} \div \frac{c}{d}$, damos una "vuelta de carnero" a la segunda fracción ($\frac{d}{c}$) y transformamos la división en **multiplicación**.

$$ \frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: $\frac{1}{2} \div \frac{1}{4}$
Invertimos $\frac{1}{4}$ a $\frac{4}{1}$ y multiplicamos:
$\frac{1}{2} \times \frac{4}{1} = \frac{4}{2} = 2$.
**Resultado:** $\boxed{2}$ (En una mitad caben dos cuartos).

#### Ejemplo 7: $\frac{3}{4} \div \frac{2}{5}$
Invertimos $\frac{2}{5}$ a $\frac{5}{2}$.
$\frac{3}{4} \times \frac{5}{2} = \frac{15}{8}$.
**Resultado:** $\boxed{\frac{15}{8}}$

#### Ejemplo 8: $\frac{5}{7} \div 3$
El 3 es $\frac{3}{1}$. Al invertir queda $\frac{1}{3}$.
$\frac{5}{7} \times \frac{1}{3} = \frac{5}{21}$.
**Resultado:** $\boxed{\frac{5}{21}}$

#### Ejemplo 9: $4 \div \frac{1}{2}$
¿Cuántas mitades caben en 4 enteros?
$4 \times \frac{2}{1} = 8$.
**Resultado:** $\boxed{8}$

#### Ejemplo 10: $\frac{2}{3} \div \frac{2}{3}$
Cualquier cosa dividida por sí misma es 1.
$\frac{2}{3} \times \frac{3}{2} = \frac{6}{6} = 1$.
**Resultado:** $\boxed{1}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Multiplica $\frac{3}{5} \times \frac{2}{3}$.

<details>
<summary>Ver solución</summary>

$\frac{6}{15} \to \frac{2}{5}$.
**Resultado:** $\boxed{\frac{2}{5}}$

</details>

### Ejercicio 2
Divide $\frac{1}{2} \div \frac{1}{3}$.

<details>
<summary>Ver solución</summary>

$\frac{1}{2} \times 3 = \frac{3}{2}$.
**Resultado:** $\boxed{\frac{3}{2}}$

</details>

### Ejercicio 3
Calcula $\frac{4}{7} \times 2$.

<details>
<summary>Ver solución</summary>

$\frac{8}{7}$.
**Resultado:** $\boxed{\frac{8}{7}}$

</details>

### Ejercicio 4
Divide $\frac{2}{5} \div 2$.

<details>
<summary>Ver solución</summary>

$\frac{2}{5} \times \frac{1}{2} = \frac{2}{10} = \frac{1}{5}$.
**Resultado:** $\boxed{\frac{1}{5}}$

</details>

### Ejercicio 5
Multiplica $\frac{5}{8} \times \frac{8}{5}$.

<details>
<summary>Ver solución</summary>

Es un número por su inverso.
**Resultado:** $\boxed{1}$

</details>

### Ejercicio 6
Divide $\frac{3}{4} \div \frac{3}{4}$.

<details>
<summary>Ver solución</summary>

Son iguales.
**Resultado:** $\boxed{1}$

</details>

### Ejercicio 7
Calcula el área de un rectángulo de lados $\frac{1}{2}$ m y $\frac{3}{4}$ m.

<details>
<summary>Ver solución</summary>

Área = Base $\times$ Altura = $\frac{1}{2} \times \frac{3}{4} = \frac{3}{8}$.
**Resultado:** $\boxed{\frac{3}{8} m^2}$

</details>

### Ejercicio 8
Divide $\frac{7}{9} \div \frac{1}{2}$.

<details>
<summary>Ver solución</summary>

$\frac{7}{9} \times 2 = \frac{14}{9}$.
**Resultado:** $\boxed{\frac{14}{9}}$

</details>

### Ejercicio 9
Multiplica $2\frac{1}{2} \times \frac{1}{3}$.

<details>
<summary>Ver solución</summary>

Convertir mixto: $\frac{5}{2} \times \frac{1}{3} = \frac{5}{6}$.
**Resultado:** $\boxed{\frac{5}{6}}$

</details>

### Ejercicio 10
Si repartes $\frac{1}{2}$ pastel entre 4 personas, ¿cuánto le toca a cada una?

<details>
<summary>Ver solución</summary>

$\frac{1}{2} \div 4 = \frac{1}{2} \times \frac{1}{4} = \frac{1}{8}$.
**Resultado:** $\boxed{\frac{1}{8}}$

</details>

---

## 🔑 Resumen

| Operación | Método | Fórmula |
| :--- | :--- | :--- |
| **Multiplicación** | Directo (Línea recta) | $\frac{a \times c}{b \times d}$ |
| **División** | Invertir el segundo y multiplicar | $\frac{a}{b} \times \frac{d}{c}$ |

> **Conclusión:** Multiplicar fracciones suele hacer el número más pequeño (si son propias). Dividir fracciones por una fracción pequeña hace el resultado más grande.
