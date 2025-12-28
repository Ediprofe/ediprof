# **Múltiplos y Divisores**

Imagina que tienes una caja de chocolates. Si puedes repartirlos exactamente entre 4 amigos sin que sobre ninguno, entonces el número de chocolates es un **múltiplo** de 4, y 4 es un **divisor** de ese número. Estos dos conceptos son como el anverso y el reverso de una misma moneda: si $A$ es múltiplo de $B$, entonces $B$ divide a $A$.

---

## 🎯 ¿Qué vas a aprender?

- Qué es un múltiplo y cómo encontrarlos.
- Qué es un divisor y cómo identificarlos.
- La relación inseparable entre múltiplo y divisor.
- Propiedades clave (infinitos múltiplos, divisores finitos).

---

## 🔢 Múltiplos

Un **múltiplo** de un número es el resultado de multiplicarlo por cualquier número natural ($0, 1, 2, 3...$).
Piensa en la "tabla de multiplicar" extendida hasta el infinito.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Múltiplos de 3
Multiplicamos 3 por los naturales:
- $3 \times 0 = 0$
- $3 \times 1 = 3$
- $3 \times 2 = 6$
- $3 \times 3 = 9$
- ...
$$ M(3) = \{0, 3, 6, 9, 12, 15, ...\} $$

#### Ejemplo 2: Múltiplos de 5
Vamos saltando de 5 en 5.
$$ M(5) = \{0, 5, 10, 15, 20, 25, 30...\} $$

#### Ejemplo 3: ¿Es 24 múltiplo de 6?
Sí, porque existe un número ($4$) tal que $6 \times 4 = 24$.
También porque si divides $24 \div 6$, el residuo es 0.

#### Ejemplo 4: Múltiplos comunes
Encuentra múltiplos comunes de 2 y 3.
- $M(2) = \{0, 2, 4, 6, 8, 10, 12...\}$
- $M(3) = \{0, 3, 6, 9, 12...\}$
- **Comunes:** $0, 6, 12...$ (Son los múltiplos de 6).

#### Ejemplo 5: Propiedades
- El 0 es múltiplo de todos.
- Todo número es múltiplo de sí mismo ($5 \times 1 = 5$).
- Los múltiplos son **infinitos**.

---

## ➗ Divisores

Un **divisor** es un número que divide a otro **exactamente** (el residuo es cero).
Piensa en "formar grupos exactos".

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: Divisores de 12
¿Qué números dividen al 12 sin dejar residuo?
- $12 \div 1 = 12$ (Sí)
- $12 \div 2 = 6$ (Sí)
- $12 \div 3 = 4$ (Sí)
- $12 \div 4 = 3$ (Sí)
- $12 \div 5$ (No, sobra 2)
- $12 \div 6 = 2$ (Sí)
- ...
- $12 \div 12 = 1$ (Sí)
$$ D(12) = \{1, 2, 3, 4, 6, 12\} $$

#### Ejemplo 7: Divisores de 7
- $7 \div 1 = 7$
- $7 \div 7 = 1$
Solo tiene dos divisores: $\{1, 7\}$. (Es un número primo).

#### Ejemplo 8: ¿Es 5 divisor de 20?
Sí, porque $20$ termina en 0 (regla del 5) y $5 \times 4 = 20$.

#### Ejemplo 9: Relación Múltiplo-Divisor
- 20 es **múltiplo** de 5.
- 5 es **divisor** de 20.
Es la misma relación vista desde dos lados.

#### Ejemplo 10: Número Perfecto
El 6 es curioso. Sus divisores (sin contarse a sí mismo) son $1, 2, 3$.
Si los sumas: $1 + 2 + 3 = 6$.
¡La suma da el mismo número! Se llama número perfecto.

---

<!-- Conservando imágenes existentes -->

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-mult3" class="jsxgraph-container" style="width: 100%; height: 100px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult3')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult3', {
      boundingbox: [-1, 2, 20, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Recta numérica
    board.create('segment', [[0, 0.8], [18, 0.8]], {strokeWidth: 2, strokeColor: '#374151', fixed: true});
    // Marcas cada 3 unidades (múltiplos de 3)
    for (var i = 0; i <= 18; i += 3) {
      board.create('point', [i, 0.8], {size: 5, fixed: true, color: '#22c55e', name: String(i), label: {offset: [0, -18], strokeColor: '#22c55e', fontSize: 11}});
    }
    // Marcas intermedias
    for (var i = 0; i <= 18; i++) {
      if (i % 3 !== 0) {
        board.create('point', [i, 0.8], {size: 2, fixed: true, color: '#94a3b8', name: '', withLabel: false});
      }
    }
    board.create('text', [9, 1.6, 'M(3) = {3, 6, 9, 12, 15, 18, ...}'], {fontSize: 12, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe los primeros 5 múltiplos de 8.

<details>
<summary>Ver solución</summary>

**Cálculo:** $8 \times 0, 8 \times 1, 8 \times 2, 8 \times 3, 8 \times 4$.
**Resultado:** $\boxed{0, 8, 16, 24, 32}$

</details>

### Ejercicio 2
Encuentra todos los divisores de 15.

<details>
<summary>Ver solución</summary>

**Prueba:**
- $1 \times 15$
- $3 \times 5$
**Resultado:** $\boxed{1, 3, 5, 15}$

</details>

### Ejercicio 3
¿Es 45 múltiplo de 9?

<details>
<summary>Ver solución</summary>

**Verificación:** ¿Existe un número tal que $9 \times n = 45$? Sí, el 5.
**Resultado:** $\boxed{\text{Sí}}$

</details>

### Ejercicio 4
¿Es 7 divisor de 40?

<details>
<summary>Ver solución</summary>

**Verificación:** $40 \div 7$.
$7 \times 5 = 35$, $7 \times 6 = 42$. No es exacto.
**Resultado:** $\boxed{\text{No}}$

</details>

### Ejercicio 5
Halla un número que sea múltiplo de 3 y de 4 a la vez (diferente de 0).

<details>
<summary>Ver solución</summary>

- Multiplos de 3: 3, 6, 9, 12...
- Multiplos de 4: 4, 8, 12...
**Resultado:** $\boxed{12}$

</details>

### Ejercicio 6
Encuentra los divisores de 13.

<details>
<summary>Ver solución</summary>

Es un número primo. Solo lo dividen el 1 y él mismo.
**Resultado:** $\boxed{1, 13}$

</details>

### Ejercicio 7
Si un número termina en 0, ¿qué número es seguro su divisor? (Además del 1 y él mismo).

<details>
<summary>Ver solución</summary>

**Razonamiento:** Todos los múltiplos de 2 son pares (0,2...), los de 5 terminan en 0 o 5, los de 10 terminan en 0.
**Resultado:** $\boxed{2, 5, 10}$

</details>

### Ejercicio 8
Escribe un múltiplo de 7 mayor que 50.

<details>
<summary>Ver solución</summary>

**Tabla del 7:** $7 \times 7 = 49$, $7 \times 8 = 56$.
**Resultado:** $\boxed{56}$

</details>

### Ejercicio 9
¿Cuántos divisores tiene el 5?

<details>
<summary>Ver solución</summary>

El 1 y el 5.
**Resultado:** $\boxed{2}$

</details>

### Ejercicio 10
¿El 1 es múltiplo o divisor de 8?

<details>
<summary>Ver solución</summary>

- Múltiplo de 8 sería $8, 16...$ (Grande).
- Divisor de 8 es 1, 2, 4, 8 (Pequeño que contenido).
**Resultado:** $\boxed{\text{Divisor}}$

</details>

---

## 🔑 Resumen

| Concepto | Definición | Ejemplo | Cantidad |
|----------|------------|---------|----------|
| **Múltiplo** | Resultado de multiplicar (Tabla). | $M(5) = \{0, 5, 10...\}$ | Infinitos |
| **Divisor** | Número que divide exacto. | $D(10) = \{1, 2, 5, 10\}$ | Finitos (pocos) |

> **Conclusión:** Los múltiplos crecen hacia el infinito (como saltos de rana). Los divisores son piezas de rompecabezas que forman al número exacto.
