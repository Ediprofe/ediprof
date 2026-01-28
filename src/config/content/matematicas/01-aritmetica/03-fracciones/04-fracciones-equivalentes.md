---
title: "Fracciones Equivalentes"
---

# **Fracciones Equivalentes**

¿Preferirías media pizza ($\frac{1}{2}$) o dos cuartos de pizza ($\frac{2}{4}$)? ¡Es exactamente la misma cantidad! Las fracciones pueden vestirse con números diferentes pero valer lo mismo. A estas "gemelas disfrazadas" las llamamos **fracciones equivalentes**.

---

## 🎯 ¿Qué vas a aprender?

- Identificar cuándo dos fracciones representan la misma cantidad.
- Amplificar fracciones (hacer los números más grandes).
- Simplificar fracciones (hacer los números más pequeños).
- Usar el producto cruzado para comprobar equivalencias.

---

## ¿Qué son Fracciones Equivalentes?

Son fracciones que representan la misma porción de la unidad, aunque tengan números distintos.

$$ \frac{1}{2} = \frac{2}{4} = \frac{4}{8} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Media Pizza
Mira estas tres fracciones. Los números cambian, pero la cantidad azul (la mitad) es idéntica.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
    <div style="text-align: center;">
      <div style="width: 90px;"><canvas id="chart-equiv-12"></canvas></div>
      <p style="font-size: 12px; color: #374151; margin-top: 0.25rem;">1/2</p>
    </div>
    <div style="text-align: center;">
      <div style="width: 90px;"><canvas id="chart-equiv-24"></canvas></div>
      <p style="font-size: 12px; color: #374151; margin-top: 0.25rem;">2/4</p>
    </div>
    <div style="text-align: center;">
      <div style="width: 90px;"><canvas id="chart-equiv-36"></canvas></div>
      <p style="font-size: 12px; color: #374151; margin-top: 0.25rem;">3/6</p>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined') {
    // 1/2
    if (document.getElementById('chart-equiv-12')) {
      new Chart(document.getElementById('chart-equiv-12'), {
        type: 'pie', data: { labels: ['1','2'], datasets: [{ data: [1,1], backgroundColor: ['#3b82f6','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] },
        options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
      });
    }
    // 2/4
    if (document.getElementById('chart-equiv-24')) {
      new Chart(document.getElementById('chart-equiv-24'), {
        type: 'pie', data: { labels: ['1','2','3','4'], datasets: [{ data: [1,1,1,1], backgroundColor: ['#3b82f6','#3b82f6','#e5e7eb','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] },
        options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
      });
    }
    // 3/6
    if (document.getElementById('chart-equiv-36')) {
      new Chart(document.getElementById('chart-equiv-36'), {
        type: 'pie', data: { labels: ['1','2','3','4','5','6'], datasets: [{ data: [1,1,1,1,1,1], backgroundColor: ['#3b82f6','#3b82f6','#3b82f6','#e5e7eb','#e5e7eb','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] },
        options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
      });
    }
  }
});
</script>

#### Ejemplo 2: El dinero
-   $\frac{1}{2}$ de un peso = 50 centavos.
-   $\frac{2}{4}$ de un peso = 50 centavos (2 monedas de 25).
-   $\frac{50}{100}$ de un peso = 50 centavos.
**Conclusión:** $\frac{1}{2} = \frac{2}{4} = \frac{50}{100}$.

#### Ejemplo 3: El tanque de gasolina
Si el tanque marca $\frac{2}{4}$, es lo mismo que decir "medio tanque" ($\frac{1}{2}$).

#### Ejemplo 4: Comprobación (Método Cruzado)
¿Es $\frac{3}{5} = \frac{6}{10}$?
Multiplicamos cruzado:
-   $3 \times 10 = 30$
-   $5 \times 6 = 30$
¡Sí son equivalentes!
**Resultado:** $\boxed{\text{Sí}}$

#### Ejemplo 5: Falsas equivalencias
¿Es $\frac{1}{3} = \frac{2}{5}$?
-   $1 \times 5 = 5$
-   $3 \times 2 = 6$
¡No son iguales!
**Resultado:** $\boxed{\text{No}}$

---

## Amplificar y Simplificar

-   **Amplificar:** Multiplicar arriba y abajo por el mismo número. (La fracción "engorda" pero vale lo mismo).
-   **Simplificar:** Dividir arriba y abajo por el mismo número. (La fracción "adelgaza" pero vale lo mismo).

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: Amplificar $\frac{2}{3}$ por 4
Multiplicamos todo por 4:
$$ \frac{2 \times 4}{3 \times 4} = \frac{8}{12} $$
**Resultado:** $\boxed{\frac{8}{12}}$

#### Ejemplo 7: Amplificar $\frac{1}{5}$ por 10
$$ \frac{1 \times 10}{5 \times 10} = \frac{10}{50} $$
**Resultado:** $\boxed{\frac{10}{50}}$

#### Ejemplo 8: Simplificar $\frac{20}{30}$
Dividimos todo entre 10 (quitamos ceros):
$$ \frac{20 \div 10}{30 \div 10} = \frac{2}{3} $$
**Resultado:** $\boxed{\frac{2}{3}}$

#### Ejemplo 9: Simplificar $\frac{12}{18}$
Dividimos entre 6 (su MCD):
$$ \frac{12 \div 6}{18 \div 6} = \frac{2}{3} $$
**Resultado:** $\boxed{\frac{2}{3}}$

#### Ejemplo 10: Simplificar $\frac{7}{21}$
Dividimos entre 7:
$$ \frac{7 \div 7}{21 \div 7} = \frac{1}{3} $$
**Resultado:** $\boxed{\frac{1}{3}}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Amplifica $\frac{3}{4}$ multiplicando por 5.

<details>
<summary>Ver solución</summary>

$3 \times 5 = 15$, $4 \times 5 = 20$.
**Resultado:** $\boxed{\frac{15}{20}}$

</details>

### Ejercicio 2
Simplifica $\frac{50}{100}$ a su mínima expresión.

<details>
<summary>Ver solución</summary>

Divides por 50.
**Resultado:** $\boxed{\frac{1}{2}}$

</details>

### Ejercicio 3
¿Son $\frac{2}{3}$ y $\frac{4}{6}$ equivalentes?

<details>
<summary>Ver solución</summary>

$2 \times 6 = 12$, $3 \times 4 = 12$.
**Resultado:** $\boxed{\text{Sí}}$

</details>

### Ejercicio 4
Encuentra el número que falta: $\frac{1}{2} = \frac{x}{10}$.

<details>
<summary>Ver solución</summary>

$1 \times 10 = 2 \times x \to 10 = 2x \to x=5$.
**Resultado:** $\boxed{5}$

</details>

### Ejercicio 5
Simplifica $\frac{8}{12}$.

<details>
<summary>Ver solución</summary>

Divide por 4.
**Resultado:** $\boxed{\frac{2}{3}}$

</details>

### Ejercicio 6
Amplifica $\frac{7}{8}$ por 2.

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{\frac{14}{16}}$

</details>

### Ejercicio 7
¿Son $\frac{4}{5}$ y $\frac{5}{6}$ equivalentes?

<details>
<summary>Ver solución</summary>

$4 \times 6 = 24$, $5 \times 5 = 25$.
**Resultado:** $\boxed{\text{No}}$

</details>

### Ejercicio 8
Simplifica $\frac{30}{45}$.

<details>
<summary>Ver solución</summary>

Divide por 15 (o por 5 y luego por 3).
**Resultado:** $\boxed{\frac{2}{3}}$

</details>

### Ejercicio 9
Escribe 3 fracciones equivalentes a $\frac{1}{3}$.

<details>
<summary>Ver solución</summary>

Por 2, 3, 4:
**Resultado:** $\boxed{\frac{2}{6}, \frac{3}{9}, \frac{4}{12}}$

</details>

### Ejercicio 10
Simplifica $\frac{11}{33}$.

<details>
<summary>Ver solución</summary>

Divide por 11.
**Resultado:** $\boxed{\frac{1}{3}}$

</details>

---

## 🔑 Resumen

| Concepto | Operación | Regla clave |
| :--- | :--- | :--- |
| **Equivalentes** | Representan lo mismo | Producto cruzado igual ($a \times d = b \times c$). |
| **Amplificar** | Multiplicar ($\times$) | Mismo número arriba y abajo. |
| **Simplificar** | Dividir ($\div$) | Mismo divisor arriba y abajo. |

> **Conclusión:** No te dejes engañar por números grandes. Siempre trata de simplificar tus fracciones a su formar más "flaca" (irreducible) para ver su verdadero valor.