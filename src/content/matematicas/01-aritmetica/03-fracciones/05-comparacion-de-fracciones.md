# **Comparación de Fracciones**

Si te ofrecen $\frac{1}{3}$ de un pastel o $\frac{1}{4}$ del mismo pastel, ¿cuál eliges si tienes mucha hambre? A veces el instinto nos falla con los números. Aprender a **comparar fracciones** te permitirá saber exactamente quién tiene más, quién tiene menos o si todos tienen lo mismo.

---

## 🎯 ¿Qué vas a aprender?

- Comparar fracciones con el mismo denominador (fácil).
- Comparar fracciones con diferente denominador usando el "Producto Cruzado" (el truco maestro).
- Comparar fracciones con el mismo numerador (lógica inversa).
- Ordenar varias fracciones de menor a mayor.

---

## Comparación con Mismo Denominador

Si el pastel está partido igual (mismo denominador), solo miramos quién tomó más pedazos (numerador).
**Mayor numerador = Mayor fracción**.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: $\frac{5}{8}$ vs $\frac{3}{8}$
Mismo denominador (8).
Como 5 es más que 3:
$$ \frac{5}{8} > \frac{3}{8} $$

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

#### Ejemplo 2: $\frac{7}{12}$ vs $\frac{11}{12}$
$7 < 11$.
**Resultado:** $\boxed{\frac{7}{12} < \frac{11}{12}}$

#### Ejemplo 3: $\frac{1}{5}$ vs $\frac{2}{5}$
$1 < 2$.
**Resultado:** $\boxed{\frac{1}{5} < \frac{2}{5}}$

#### Ejemplo 4: $\frac{10}{20}$ vs $\frac{15}{20}$
**Resultado:** $\boxed{\frac{10}{20} < \frac{15}{20}}$

#### Ejemplo 5: Ordenar
$\frac{4}{9}, \frac{1}{9}, \frac{8}{9}$.
**Resultado:** $\boxed{\frac{1}{9} < \frac{4}{9} < \frac{8}{9}}$

---

## Comparación con Diferente Denominador (Producto Cruzado)

El "truco ninja" para no dibujar:
1.  Multiplica el numerador de la primera por el denominador de la segunda (diagonal abajo).
2.  Multiplica el denominador de la primera por el numerador de la segunda (diagonal arriba).
3.  Compara los resultados.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: $\frac{3}{4}$ vs $\frac{5}{7}$
Multiplicamos cruzado:
-   $3 \times 7 = 21$ (Lado izquierdo).
-   $4 \times 5 = 20$ (Lado derecho).
Como $21 > 20$, entonces:
$$ \boxed{\frac{3}{4} > \frac{5}{7}} $$

#### Ejemplo 7: $\frac{2}{5}$ vs $\frac{3}{7}$
-   $2 \times 7 = 14$
-   $5 \times 3 = 15$
$14 < 15$.
$$ \boxed{\frac{2}{5} < \frac{3}{7}} $$

#### Ejemplo 8: $\frac{1}{3}$ vs $\frac{2}{6}$
-   $1 \times 6 = 6$
-   $3 \times 2 = 6$
¡Son iguales!
$$ \boxed{\frac{1}{3} = \frac{2}{6}} $$

#### Ejemplo 9: $\frac{4}{5}$ vs $\frac{7}{9}$
-   $4 \times 9 = 36$
-   $5 \times 7 = 35$
$$ \boxed{\frac{4}{5} > \frac{7}{9}} $$

#### Ejemplo 10: $\frac{1}{2}$ vs $\frac{1}{3}$
-   $1 \times 3 = 3$
-   $2 \times 1 = 2$
$$ \boxed{\frac{1}{2} > \frac{1}{3}} $$

---

## Comparación con Mismo Numerador

Si tomas la **misma cantidad** de partes (mismo numerador), será más grande la fracción que tenga pedazos más grandes (menor denominador).
**Menor denominador = Mayor fracción**.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 11: $\frac{1}{2}$ vs $\frac{1}{4}$
Ambas toman 1 pedazo. Pero los de $\frac{1}{2}$ son gigantes y los de $\frac{1}{4}$ son pequeños.
$$ \boxed{\frac{1}{2} > \frac{1}{4}} $$

#### Ejemplo 12: $\frac{3}{5}$ vs $\frac{3}{8}$
Tomas 3. Pero 5 significa "partir menos" (pedazos grandes).
$$ \boxed{\frac{3}{5} > \frac{3}{8}} $$

#### Ejemplo 13: $\frac{10}{20}$ vs $\frac{10}{5}$
$$ \boxed{\frac{10}{20} < \frac{10}{5}} $$

#### Ejemplo 14: $\frac{7}{7}$ vs $\frac{7}{8}$
$\frac{7}{7}$ es un entero. $\frac{7}{8}$ es menos que un entero.
$$ \boxed{\frac{7}{7} > \frac{7}{8}} $$

#### Ejemplo 15: $\frac{5}{100}$ vs $\frac{5}{2}$
$$ \boxed{\frac{5}{100} < \frac{5}{2}} $$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Compara $\frac{2}{3}$ y $\frac{4}{5}$.

<details>
<summary>Ver solución</summary>

$2 \times 5 = 10$. $3 \times 4 = 12$.
**Resultado:** $\boxed{<}$

</details>

### Ejercicio 2
Compara $\frac{7}{9}$ y $\frac{6}{9}$.

<details>
<summary>Ver solución</summary>

Mismo denominador. $7 > 6$.
**Resultado:** $\boxed{>}$

</details>

### Ejercicio 3
Compara $\frac{3}{8}$ y $\frac{3}{5}$.

<details>
<summary>Ver solución</summary>

Mismo numerador. 8 parte más pequeño que 5.
**Resultado:** $\boxed{<}$

</details>

### Ejercicio 4
Compara $\frac{1}{2}$ y $\frac{50}{100}$.

<details>
<summary>Ver solución</summary>

$1 \times 100 = 100$. $2 \times 50 = 100$.
**Resultado:** $\boxed{=}$

</details>

### Ejercicio 5
Ordena: $\frac{1}{5}, \frac{1}{2}, \frac{1}{10}$.

<details>
<summary>Ver solución</summary>

Mismo numerador. Gana el denominador pequeño.
**Resultado:** $\boxed{\frac{1}{10} < \frac{1}{5} < \frac{1}{2}}$

</details>

### Ejercicio 6
Compara $\frac{6}{7}$ y $\frac{7}{8}$.

<details>
<summary>Ver solución</summary>

$6 \times 8 = 48$. $7 \times 7 = 49$.
**Resultado:** $\boxed{<}$

</details>

### Ejercicio 7
¿Quién comió más? Ana ($\frac{2}{3}$) o Luis ($\frac{4}{6}$).

<details>
<summary>Ver solución</summary>

$2 \times 6 = 12$. $3 \times 4 = 12$.
**Resultado:** $\boxed{\text{Igual}}$

</details>

### Ejercicio 8
Compara $\frac{9}{5}$ y $1$.

<details>
<summary>Ver solución</summary>

$\frac{9}{5}$ es impropia (>1).
**Resultado:** $\boxed{>}$

</details>

### Ejercicio 9
Compara $2\frac{1}{2}$ y $\frac{5}{2}$.

<details>
<summary>Ver solución</summary>

$2 \times 2 + 1 = 5$.
**Resultado:** $\boxed{=}$

</details>

### Ejercicio 10
Ordena $\frac{3}{4}, \frac{1}{4}, \frac{5}{4}$.

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{\frac{1}{4} < \frac{3}{4} < \frac{5}{4}}$

</details>

---

## 🔑 Resumen

| Caso | Regla Directa | Método Infalible |
| :--- | :--- | :--- |
| **Mismo denominador** | Gana numerador mayor. | - |
| **Mismo numerador** | Gana denominador menor. | - |
| **Diferentes** | - | Producto Cruzado ($a \times d \text{ vs } b \times c$) |

> **Conclusión:** Ante la duda, ¡cruza los números! El producto cruzado nunca miente.
