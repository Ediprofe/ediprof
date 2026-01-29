# **Números Primos y Compuestos**

Los números son como los átomos de la química. Algunos no se pueden dividir en partes más pequeñas (excepto por 1 y ellos mismos); esos son los **números primos**. Otros se pueden "romper" en piezas más pequeñas; esos son los **números compuestos**. ¡Entender esto es la clave para toda la Aritmética avanzada!

---

## 🎯 ¿Qué vas a aprender?

- Distinguir entre números primos (los "indestructibles") y compuestos (los "armables").
- Identificar por qué el 1 no es ni primo ni compuesto.
- Memorizar los primeros números primos.
- Usar la Criba de Eratóstenes (mentalmente) para cazar primos.

---

## Números Primos

Un número primo tiene **exactamente dos divisores**:
1.  El número 1.
2.  Él mismo.

Son los "bloques de construcción" de todos los números.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1
El **2** es primo.
Divisores: $1, 2$.
(Es el único primo par).

#### Ejemplo 2
El **3** es primo.
Divisores: $1, 3$.

#### Ejemplo 3
El **5** es primo.
Divisores: $1, 5$.

#### Ejemplo 4
El **13** es primo.
Divisores: $1, 13$.

#### Ejemplo 5
El **7** es primo.
Divisores: $1, 7$.

---

## Números Compuestos

Un número compuesto tiene **más de dos divisores** (al menos tres). Se pueden formar multiplicando otros números más pequeños.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6
El **4** es compuesto.
Divisores: $1, 2, 4$.
($2 \times 2 = 4$).

#### Ejemplo 7
El **6** es compuesto.
Divisores: $1, 2, 3, 6$.
($2 \times 3 = 6$).

#### Ejemplo 8
El **9** es compuesto.
Divisores: $1, 3, 9$.
($3 \times 3 = 9$).

#### Ejemplo 9
El **15** es compuesto.
Divisores: $1, 3, 5, 15$.

#### Ejemplo 10
El **1** UN CASO ESPECIAL.
**No es primo** (solo tiene un divisor, el 1).
**No es compuesto** (no tiene más de dos).
Es simplemente... la unidad.

---

## Cómo Saber si un Número es Primo

Para saber si un número grande (como 97) es primo, intenta dividirlo por los primos pequeños ($2, 3, 5, 7, 11...$). Si ninguno lo divide, es primo.

### Lista de Primos Menores a 50
$$ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 $$

---

<!-- Conservando imágenes existentes -->

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-primo7" class="jsxgraph-container" style="width: 100%; height: 120px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-primo7')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-primo7', {
      boundingbox: [-0.5, 2.5, 8, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 7 cuadrados
    for (var c = 0; c < 7; c++) {
      board.create('polygon', [[c*1.05, 1.8], [c*1.05+0.9, 1.8], [c*1.05+0.9, 1], [c*1.05, 1]], {fillColor: '#22c55e', fillOpacity: 0.8, strokeColor: '#166534', strokeWidth: 2, fixed: true, vertices: {visible: false}});
    }
    board.create('text', [3.7, 2.3, '7 = 1 × 7 (única forma)'], {fontSize: 13, strokeColor: '#166534', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [3.7, 0.4, 'D(7) = {1, 7}'], {fontSize: 12, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.unsuspendUpdate();
  }
});
</script>

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Clasifica el número 17.

<details>
<summary>Ver solución</summary>

Solo divisores 1 y 17.
**Resultado:** $\boxed{\text{Primo}}$

</details>

### Ejercicio 2
Clasifica el número 25.

<details>
<summary>Ver solución</summary>

Divisores 1, 5, 25.
**Resultado:** $\boxed{\text{Compuesto}}$

</details>

### Ejercicio 3
¿Es 27 primo o compuesto?

<details>
<summary>Ver solución</summary>

$27 = 3 \times 9$.
**Resultado:** $\boxed{\text{Compuesto}}$

</details>

### Ejercicio 4
¿Es 31 primo?

<details>
<summary>Ver solución</summary>

No es par, no suma 3, no termina en 5.
**Resultado:** $\boxed{\text{Primo}}$

</details>

### Ejercicio 5
¿Cuál es el único número primo que es par?

<details>
<summary>Ver solución</summary>

El único.
**Resultado:** $\boxed{2}$

</details>

### Ejercicio 6
Clasifica el número 57. (Cuidado).

<details>
<summary>Ver solución</summary>

Suma de cifras: $5+7=12$ (Múltiplo de 3).
**Resultado:** $\boxed{\text{Compuesto}}$

</details>

### Ejercicio 7
Clasifica el número 91. (Trampa clásica).

<details>
<summary>Ver solución</summary>

Pruébalo con 7. $91 \div 7 = 13$.
**Resultado:** $\boxed{\text{Compuesto}}$

</details>

### Ejercicio 8
¿Cuántos números primos hay entre 1 y 10?

<details>
<summary>Ver solución</summary>

Son: 2, 3, 5, 7.
**Resultado:** $\boxed{4}$

</details>

### Ejercicio 9
¿Es 1 primo, compuesto o ninguno?

<details>
<summary>Ver solución</summary>

Solo tiene un divisor.
**Resultado:** $\boxed{\text{Ninguno}}$

</details>

### Ejercicio 10
Encuentra dos números primos que sumados den 8.

<details>
<summary>Ver solución</summary>

Prueba con 3 y 5.
**Resultado:** $\boxed{3 \text{ y } 5}$

</details>

---

## 🔑 Resumen

| Tipo | Divisores | Ejemplos |
|------|-----------|----------|
| **Primo** | Exactamente 2 ($1$ y él mismo) | $2, 3, 5, 7, 11, 13$ |
| **Compuesto** | Más de 2 | $4, 6, 8, 9, 10, 12$ |
| **Uno (1)** | Solo 1 | $1$ (Ni primo ni compuesto) |

> **Conclusión:** Si te encuentras un número, pregúntale: ¿Te puedo romper en factores más chicos? Si dice **NO**, es un **Primo**. Si dice **SÍ**, es **Compuesto**.
