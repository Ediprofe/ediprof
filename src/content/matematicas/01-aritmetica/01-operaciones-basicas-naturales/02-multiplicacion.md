# **Multiplicación de Números Naturales**

La multiplicación es simplemente una **suma rápida**. Si tienes 5 cajas y cada una tiene 4 donas, no necesitas contar una por una ($1, 2, 3... 20$). Simplemente dices: "5 veces 4" y obtienes 20. Es el superpoder de contar grupos enteros instantáneamente.

---

## 🎯 ¿Qué vas a aprender?

- Entender la multiplicación como una suma abreviada.
- Memorizar patrones clave (tablas de multiplicar).
- Realizar multiplicaciones por una, dos y más cifras.
- Aplicar propiedades para calcular más rápido.

---

## Concepto Básico

La multiplicación combina dos números llamados **factores** para obtener un **producto**.
$$ 4 \times 3 = 12 $$
Esto se lee "4 veces 3" (o 4 grupos de 3).

### Propiedades Clave

#### 1. Conmutativa (El orden no importa)
$$ 5 \times 3 = 3 \times 5 = 15 $$
Es lo mismo comprar 5 paquetes de 3 galletas, que 3 paquetes de 5 galletas. Tendrás 15 galletas igual.

#### 2. Elemento Neutro (El 1)
Cualquier número multiplicado por 1 se queda igual.
$$ 8 \times 1 = 8 $$

#### 3. Elemento Absorbente (El 0)
Cualquier número multiplicado por 0 desaparece.
$$ 1,000,000 \times 0 = 0 $$

---

## Multiplicación por 1 Cifra

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Sin llevar
Calcula $123 \times 3$.
1.  **Unidades:** $3 \times 3 = 9$.
2.  **Decenas:** $3 \times 2 = 6$.
3.  **Centenas:** $3 \times 1 = 3$.
**Resultado:** $\boxed{369}$

#### Ejemplo 2: Llevando
Calcula $47 \times 6$.
1.  **Unidades:** $6 \times 7 = 42$. Escribo 2, llevo 4.
2.  **Decenas:** $6 \times 4 = 24$. Sumo los 4 que llevaba ($24+4=28$).
**Resultado:** $\boxed{282}$

#### Ejemplo 3: Llevando (Intermedio)
Calcula $58 \times 9$.
1.  $9 \times 8 = 72$. Escribo 2, llevo 7.
2.  $9 \times 5 = 45$. Sumo 7: ($45+7=52$).
**Resultado:** $\boxed{522}$

#### Ejemplo 4: Patrón del 9
Truco: Para multiplicar por 9, multiplica por 10 y resta el número.
$58 \times 9 = (58 \times 10) - 58 = 580 - 58 = 522$.
**Resultado:** $\boxed{522}$

#### Ejemplo 5: Ceros finales
Si multiplicas $20 \times 3$, olvida el cero un momento.
$2 \times 3 = 6$. Agrega el cero.
**Resultado:** $\boxed{60}$

---

## Multiplicación por 2 o más Cifras

Aquí usamos **productos parciales**. Multiplicamos por las unidades, luego por las decenas (dejando un espacio), y al final sumamos.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: El proceso estándar
Multiplica $34 \times 25$.
1.  **Por 5 (unidades):** $34 \times 5 = 170$.
2.  **Por 2 (decenas):** $34 \times 2 = 68$. **¡OJO!** Como es 20, corremos un espacio a la izquierda: 680.
3.  **Suma:** $170 + 680$.
**Resultado:** $\boxed{850}$

#### Ejemplo 7: Tres cifras por dos cifras
Multiplica $245 \times 38$.
1.  **Fila 1 ($245 \times 8$):** $1,960$.
2.  **Fila 2 ($245 \times 3$):** $735$ (dejando un espacio a la derecha).
3.  **Suma:** $1,960 + 7,350$.
**Resultado:** $\boxed{9,310}$

#### Ejemplo 8: Multiplicación Grande
Multiplica $512 \times 75$.
1.  $512 \times 5 = 2,560$.
2.  $512 \times 7 = 3,584$ (espacio).
3.  Suma: $2,560 + 35,840$.
**Resultado:** $\boxed{38,400}$

#### Ejemplo 9: Multiplicación por 11
Truco rápido: Para $52 \times 11$, separa el 5 y el 2, y pon la suma en medio.
$5 + 2 = 7$.
**Resultado:** $\boxed{572}$

#### Ejemplo 10: Estrategia de Descomposición
Calcula $12 \times 25$ mentalmente.
- Descompone 12 en $4 \times 3$.
- $25 \times 4 = 100$.
- $100 \times 3$.
**Resultado:** $\boxed{300}$

---

<!-- Conservando imágenes existentes -->

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-mult4" class="jsxgraph-container" style="width: 100%; height: 260px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-mult4')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-mult4', {
      boundingbox: [-0.5, 6.5, 6, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // 34
    board.create('text', [2, 5.5, '3'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 5.5, '4'], {fontSize: 22, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // × 25
    board.create('text', [0.8, 4.5, '×'], {fontSize: 20, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 4.5, '2'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 4.5, '5'], {fontSize: 22, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Línea
    board.create('segment', [[0.5, 4], [3.3, 4]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Producto parcial 1: 34 × 5 = 170
    board.create('text', [1.3, 3.2, '1'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 3.2, '7'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 3.2, '0'], {fontSize: 18, strokeColor: '#9333ea', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 3.2, '← 34×5'], {fontSize: 10, strokeColor: '#9333ea', fixed: true});
    // Producto parcial 2: 34 × 20 = 680
    board.create('text', [0.3, 2.4, '+'], {fontSize: 16, strokeColor: '#374151', fixed: true, anchorX: 'middle'});
    board.create('text', [0.6, 2.4, '6'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.3, 2.4, '8'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 2.4, '0'], {fontSize: 18, strokeColor: '#f59e0b', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4, 2.4, '← 34×20'], {fontSize: 10, strokeColor: '#f59e0b', fixed: true});
    // Línea de suma
    board.create('segment', [[0.2, 1.9], [3, 1.9]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Resultado: 850
    board.create('text', [1.3, 1.1, '8'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2, 1.1, '5'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.7, 1.1, '0'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
En un cine hay 8 filas con 9 sillas cada una. ¿Cuántas sillas hay en total?

<details>
<summary>Ver solución</summary>

**Operación:** $8 \times 9$.
**Resultado:** $\boxed{72}$

</details>

### Ejercicio 2
Calcula $56 \times 4$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
- $4 \times 6 = 24$ (llevo 2)
- $4 \times 5 = 20$. Sumo 2: $22$.
**Resultado:** $\boxed{224}$

</details>

### Ejercicio 3
Calcula $67 \times 9$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
- $9 \times 7 = 63$ (llevo 6)
- $9 \times 6 = 54$. Sumo 6: $60$.
**Resultado:** $\boxed{603}$

</details>

### Ejercicio 4
Si una caja tiene 25 lápices, ¿cuántos lápices hay en 12 cajas?

<details>
<summary>Ver solución</summary>

**Operación:** $25 \times 12$.
- $25 \times 2 = 50$
- $25 \times 10 = 250$
- $50 + 250 = 300$
**Resultado:** $\boxed{300}$

</details>

### Ejercicio 5
Calcula $48 \times 15$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
- $48 \times 5 = 240$
- $48 \times 10 = 480$
- $240 + 480 = 720$
**Resultado:** $\boxed{720}$

</details>

### Ejercicio 6
Una fábrica produce 134 juguetes por hora. ¿Cuántos hace en 26 horas?

<details>
<summary>Ver solución</summary>

**Operación:** $134 \times 26$.
- $134 \times 6 = 804$
- $134 \times 20 = 2680$
- Suma: $3484$
**Resultado:** $\boxed{3,484}$

</details>

### Ejercicio 7
Calcula $245 \times 38$.

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{9,310}$
(Ver Ejemplo 7 arriba).

</details>

### Ejercicio 8
Calcula $367 \times 52$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
- $367 \times 2 = 734$
- $367 \times 50 = 18350$
- Suma: 19084
**Resultado:** $\boxed{19,084}$

</details>

### Ejercicio 9
Si compras 458 paquetes de galletas a \$67 pesos cada uno.

<details>
<summary>Ver solución</summary>

**Operación:** $458 \times 67$.
**Resultado:** $\boxed{\$30,686}$

</details>

### Ejercicio 10
Calcula $625 \times 84$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
- $625 \times 4 = 2500$
- $625 \times 80 = 50000$
- Suma: 52500
**Resultado:** $\boxed{52,500}$

</details>

---

## 🔑 Resumen

| Propiedad | Descripción | Ejemplo |
|-----------|-------------|---------|
| **Conmutativa** | El orden no altera el producto | $3 \times 4 = 4 \times 3$ |
| **Asociativa** | Agrupar no altera el producto | $(2 \times 3) \times 4 = 24$ |
| **Neutro** | Multiplicar por 1 | $7 \times 1 = 7$ |
| **Absorbente** | Multiplicar por 0 | $7 \times 0 = 0$ |

> **Conclusión:** La multiplicación te ahorra tiempo. Domina las tablas del 1 al 9 y podrás multiplicar cualquier número, por gigante que sea.
