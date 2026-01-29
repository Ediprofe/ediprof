# **MCM y MCD: Los Reyes de la Aritmética**

Imagina que quieres cortar cintas en pedazos iguales pero lo más grandes posible (MCD), o quieres saber cuándo coincidirán dos luces parpadeantes que brillan a diferentes ritmos (MCM). Estos dos conceptos son las herramientas definitivas para resolver problemas de repetición y división.

---

## 🎯 ¿Qué vas a aprender?

- Calcular el **Máximo Común Divisor (MCD)**: El mayor número que divide a todos.
- Calcular el **Mínimo Común Múltiplo (MCM)**: El menor número en el que todos coinciden.
- El método rápido de descomposición simultánea.
- Diferenciar cuándo usar MCM y cuándo MCD en la vida real.

---

## Máximo Común Divisor (MCD)

Es el "jefe" de los divisores. El número más grande que puede dividir a dos o más números sin dejar residuo.

**Regla de oro:** Solo multiplicamos los factores que dividen a **TODOS** los números al mismo tiempo.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: MCD de 12 y 18
1.  Factores de 12: $1, 2, 3, 4, 6, 12$.
2.  Factores de 18: $1, 2, 3, 6, 9, 18$.
3.  Comunes: $1, 2, 3, 6$.
4.  El mayor es 6.
**Resultado:** $\boxed{6}$

#### Ejemplo 2: Método Rápido (12 y 18)
- $12 - 18 \mid 2$ (Divide a ambos)
- $6 - 9 \mid 3$ (Divide a ambos)
- $2 - 3 \mid$ (Ya no hay divisor común aparte de 1).
MCD = $2 \times 3 = 6$.

#### Ejemplo 3: MCD de 24 y 36
- $24 - 36 \mid 2$
- $12 - 18 \mid 2$
- $6 - 9 \mid 3$
- $2 - 3$.
MCD = $2 \times 2 \times 3 = 12$.
**Resultado:** $\boxed{12}$

#### Ejemplo 4: MCD de 15 y 20
- $15 - 20 \mid 5$
- $3 - 4$.
MCD = 5.
**Resultado:** $\boxed{5}$

#### Ejemplo 5: MCD de Primos (5 y 7)
Solo tienen el 1 en común.
MCD = 1.
**Resultado:** $\boxed{1}$

---

## Mínimo Común Múltiplo (MCM)

Es el punto de encuentro más cercano. El primer número que aparece en la tabla de multiplicar de todos.

**Regla de oro:** Multiplicamos hasta que todos los números lleguen a 1.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: MCM de 4 y 6
- Tabla del 4: $4, 8, 12, 16, 20, 24...$
- Tabla del 6: $6, 12, 18, 24...$
- Coinciden en 12 y 24.
- El menor es 12.
**Resultado:** $\boxed{12}$

#### Ejemplo 7: Método Rápido (4 y 6)
- $4 - 6 \mid 2$
- $2 - 3 \mid 2$ (Solo al 2)
- $1 - 3 \mid 3$ (Solo al 3)
- $1 - 1$.
MCM = $2 \times 2 \times 3 = 12$.

#### Ejemplo 8: MCM de 10 y 15
- $10 - 15 \mid 2$
- $5 - 15 \mid 3$
- $5 - 5 \mid 5$
- $1 - 1$.
MCM = $2 \times 3 \times 5 = 30$.
**Resultado:** $\boxed{30}$

#### Ejemplo 9: MCM de 3, 4 y 5
Multiplicamos todo porque son primos entre sí (relativos).
$3 \times 4 \times 5 = 60$.
**Resultado:** $\boxed{60}$

#### Ejemplo 10: Relación MCM y MCD
Para 12 y 18:
MCD = 6. MCM = 36.
MCD $\times$ MCM = $6 \times 36 = 216$.
Producto de números: $12 \times 18 = 216$.
¡Siempre da lo mismo!

---

<!-- Conservando imágenes existentes -->

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-mcd1" class="jsxgraph-container" style="width: 100%; height: 280px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mcd1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mcd1', {
      boundingbox: [-0.5, 6, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Líneas divisoras
    board.create('segment', [[1.5, 5.5], [1.5, 1]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    board.create('segment', [[3, 5.5], [3, 1]], {strokeColor: '#374151', strokeWidth: 3, fixed: true});
    // Encabezados
    board.create('text', [0.7, 5.5, '12'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 5.5, '18'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    // Fila 1: ÷2
    board.create('text', [0.7, 4.5, '6'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 4.5, '9'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 4.5, '2'], {fontSize: 16, strokeColor: '#ef4444', fixed: true, cssStyle: 'font-weight: bold;'});
    // Fila 2: ÷3
    board.create('text', [0.7, 3.5, '2'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 3.5, '3'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 3.5, '3'], {fontSize: 16, strokeColor: '#3b82f6', fixed: true, cssStyle: 'font-weight: bold;'});
    // Fila 3: ÷2
    board.create('text', [0.7, 2.5, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 2.5, '3'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 2.5, '2'], {fontSize: 16, strokeColor: '#94a3b8', fixed: true, cssStyle: 'font-weight: bold;'});
    // Fila 4: ÷3
    board.create('text', [0.7, 1.5, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.3, 1.5, '1'], {fontSize: 16, strokeColor: '#22c55e', fixed: true, anchorX: 'right', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.5, 1.5, '3'], {fontSize: 16, strokeColor: '#94a3b8', fixed: true, cssStyle: 'font-weight: bold;'});
    // Líneas horizontales
    for (var i = 0; i < 4; i++) {
      board.create('segment', [[0, 5-i], [4.2, 5-i]], {strokeColor: '#d1d5db', strokeWidth: 1, fixed: true});
    }
    // Resultado
    board.create('text', [2, 0.5, 'MCD = 2 × 3 = 6'], {fontSize: 14, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [5, 3.5, '← comunes'], {fontSize: 11, strokeColor: '#22c55e', fixed: true});
    board.unsuspendUpdate();
  }
});
</script>

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el MCD de 30 y 45.

<details>
<summary>Ver solución</summary>

- $30-45 \mid 3 \to 10-15$
- $10-15 \mid 5 \to 2-3$
MCD = $3 \times 5 = 15$.
**Resultado:** $\boxed{15}$

</details>

### Ejercicio 2
Calcula el MCM de 5 y 8.

<details>
<summary>Ver solución</summary>

Como no tienen factores comunes: $5 \times 8 = 40$.
**Resultado:** $\boxed{40}$

</details>

### Ejercicio 3
Calcula el MCD de 8 y 20.

<details>
<summary>Ver solución</summary>

- $8-20 \mid 2 \to 4-10$
- $4-10 \mid 2 \to 2-5$
MCD = 4.
**Resultado:** $\boxed{4}$

</details>

### Ejercicio 4
Calcula el MCM de 12 y 15.

<details>
<summary>Ver solución</summary>

- $12-15 \mid 3 \to 4-5$
- $4-5 \mid 2 \to 2-5$
- $2-5 \mid 2 \to 1-5$
- $1-5 \mid 5 \to 1-1$
MCM = $3 \times 4 \times 5 = 60$. (Ojo: $3 \times 2 \times 2 \times 5$).
**Resultado:** $\boxed{60}$

</details>

### Ejercicio 5
Calcula el MCD de 100 y 150.

<details>
<summary>Ver solución</summary>

- $100-150 \mid 10 \to 10-15$
- $10-15 \mid 5 \to 2-3$
MCD = $10 \times 5 = 50$.
**Resultado:** $\boxed{50}$

</details>

### Ejercicio 6
Calcula el MCM de 6, 8 y 12.

<details>
<summary>Ver solución</summary>

- $\mid 2 \to 3-4-6$
- $\mid 2 \to 3-2-3$
- $\mid 2 \to 3-1-3$
- $\mid 3 \to 1-1-1$
MCM = $8 \times 3 = 24$.
**Resultado:** $\boxed{24}$

</details>

### Ejercicio 7
Busco el menor número divisible por 4 y 5 a la vez.

<details>
<summary>Ver solución</summary>

Buscas el MCM(4, 5).
**Resultado:** $\boxed{20}$

</details>

### Ejercicio 8
Tengo cuerdas de 20m y 30m. Quiero trozos iguales lo más grandes posibles.

<details>
<summary>Ver solución</summary>

Buscas el MCD(20, 30).
MCD = 10.
**Resultado:** $\boxed{10 \text{ metros}}$

</details>

### Ejercicio 9
Calcula el MCM de 2, 3 y 5.

<details>
<summary>Ver solución</summary>

Son primos. $2 \times 3 \times 5 = 30$.
**Resultado:** $\boxed{30}$

</details>

### Ejercicio 10
Si MCD(A,B) = 1, ¿Cuánto es MCM(A,B)?

<details>
<summary>Ver solución</summary>

Es su producto directo $A \times B$.
**Resultado:** $\boxed{A \times B}$

</details>

---

## 🔑 Resumen

| Concepto | Qué buscamos | Operación | Clave |
|----------|--------------|-----------|-------|
| **MCD** | El **mayor** divisor común | Multiplicar primos comunes | Cortar, dividir, agrupar. |
| **MCM** | El **menor** múltiplo común | Multiplicar todos los factores | Coincidir, repetir, encontrar. |

> **Conclusión:** El MCD divide cosas grandes en trozos pequeños. El MCM infla cosas pequeñas hasta que se encuentran en un punto gigante común.
