# **Suma y Resta de Números Naturales**

Imagina que tienes una alcancía. Si te dan dinero en tu cumpleaños, lo "agregas" (sumas). Si vas a comprar un helado, lo "sacas" (restas). La suma y la resta son las dos acciones más básicas de la vida: juntar y separar.

---

## 🎯 ¿Qué vas a aprender?

- Comprender qué son la suma y la resta en contextos reales.
- Realizar sumas llevando (agrupando).
- Realizar restas prestando (desagrupando).
- Verificar si tus resultados son correctos.

---

## La Suma (Adición)

La suma es la operación de combinar dos o más números para obtener un total.
$$ 5 + 3 = 8 $$
Partes:
- **Sumandos:** Los números que se suman (5 y 3).
- **Suma o Total:** El resultado (8).

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Suma Simple
Tienes 3 manzanas y compras 2 más.
$$ 3 + 2 = 5 $$
Total: 5 manzanas.

#### Ejemplo 2: Suma Vertical Llevando (Agrupando)
Suma $48 + 35$.
1.  **Unidades:** $8 + 5 = 13$. Escribes el **3** y llevas el **1** a las decenas.
2.  **Decenas:** $4 + 3 + 1 \text{ (que llevabas)} = 8$.
**Resultado:** $\boxed{83}$

#### Ejemplo 3: Suma de Tres Cifras
Suma $156 + 279$.
1.  **6 + 9 = 15.** Escribo 5, llevo 1.
2.  **5 + 7 + 1 = 13.** Escribo 3, llevo 1.
3.  **1 + 2 + 1 = 4.**
**Resultado:** $\boxed{435}$

#### Ejemplo 4: Propiedad Conmutativa
¿Es lo mismo $10 + 5$ que $5 + 10$?
- $10 + 5 = 15$
- $5 + 10 = 15$
**Conclusión:** Sí, el orden no altera el resultado.

#### Ejemplo 5: Suma con Ceros
$504 + 203$.
- $4+3=7$
- $0+0=0$
- $5+2=7$
**Resultado:** $\boxed{707}$

---

## La Resta (Sustracción)

La resta es la operación de quitar una cantidad de otra para encontrar la diferencia.
$$ 10 - 4 = 6 $$
Partes:
- **Minuendo:** El número del que restas (10).
- **Sustraendo:** El número que quitas (4).
- **Diferencia:** El resultado (6).

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Resta Simple
Tienes 8 dulces y te comes 3.
$$ 8 - 3 = 5 $$
Quedan 5 dulces.

#### Ejemplo 2: Resta Prestando (Desagrupando)
Resta $52 - 38$.
1.  **Unidades:** A 2 no le puedes quitar 8. El 5 le "presta" una decena al 2, convirtiéndolo en 12. El 5 queda en 4.
2.  **Operación:** $12 - 8 = 4$.
3.  **Decenas:** $4 - 3 = 1$.
**Resultado:** $\boxed{14}$

#### Ejemplo 3: Resta con Ceros
Resta $300 - 145$.
1.  El 0 unidades pide. El 0 decenas no tiene, así que pide al 3.
2.  El 3 se vuelve 2. El 0 decenas se vuelve 10, le presta al 0 unidades y queda en 9. El 0 unidades se vuelve 10.
3.  $10 - 5 = 5$.
4.  $9 - 4 = 5$.
5.  $2 - 1 = 1$.
**Resultado:** $\boxed{155}$

#### Ejemplo 4: Prueba de la Resta
Si $20 - 5 = 15$, entonces $15 + 5$ debe ser 20.
$15 + 5 = 20$.
**Conclusión:** Correcto.

#### Ejemplo 5: Contexto de Dinero
Tenías \$5000 y gastas \$1200.
$5000 - 1200 = 3800$.
 te quedan **\$3800**.

---

<!-- Conservando imágenes existentes -->
<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-suma1" class="jsxgraph-container" style="width: 100%; height: 180px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-suma1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma1', {
      boundingbox: [-0.5, 4.5, 5, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    board.create('text', [1, 3.5, '2'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 3.5, '3'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 3.5, '4'], {fontSize: 20, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [0.3, 2.5, '+'], {fontSize: 18, strokeColor: '#374151', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1, 2.5, '1'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 2.5, '5'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 2.5, '2'], {fontSize: 20, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('segment', [[0.5, 2], [3.1, 2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('text', [1, 1.2, '3'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 1.2, '8'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 1.2, '6'], {fontSize: 22, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $125 + 342$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
- $5+2=7$
- $2+4=6$
- $1+3=4$
**Resultado:** $\boxed{467}$

</details>

### Ejercicio 2
Calcula $589 + 134$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
- $9+4=13$ (llevo 1)
- $8+3+1=12$ (llevo 1)
- $5+1+1=7$
**Resultado:** $\boxed{723}$

</details>

### Ejercicio 3
Calcula $95 - 42$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
- $5-2=3$
- $9-4=5$
**Resultado:** $\boxed{53}$

</details>

### Ejercicio 4
Calcula $72 - 38$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
- $2-8$ no se puede. Presto. $12-8=4$.
- El 7 quedó en 6. $6-3=3$.
**Resultado:** $\boxed{34}$

</details>

### Ejercicio 5
Calcula $1000 - 456$.

<details>
<summary>Ver solución</summary>

**Cálculo:** (Prestando en cadena)
- $10-6=4$
- $9-5=4$
- $9-4=5$
**Resultado:** $\boxed{544}$

</details>

### Ejercicio 6
Tenías 50 cartas y regalaste 15. Luego te dieron 10. ¿Cuántas tienes?

<details>
<summary>Ver solución</summary>

**Análisis:** Resta y luego suma.
- $50 - 15 = 35$
- $35 + 10 = 45$
**Resultado:** $\boxed{45}$

</details>

### Ejercicio 7
Suma $1,200 + 3,500 + 400$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
- $0+0+0=0$
- $0+0+0=0$
- $2+5+4=11$ (llevo 1)
- $1+3+1=5$
**Resultado:** $\boxed{5,100}$

</details>

### Ejercicio 8
¿Cuál es la diferencia entre 500 y 299?

<details>
<summary>Ver solución</summary>

**Operación:** Resta.
**Resultado:** $\boxed{201}$

</details>

### Ejercicio 9
Si en la propiedad conmutativa $A+B = B+A$, ¿funciona la resta ($A-B = B-A$)?

<details>
<summary>Ver solución</summary>

**Prueba:** $5-2 = 3$, pero $2-5 = -3$.
**Resultado:** $\boxed{\text{No, la resta no es conmutativa}}$

</details>

### Ejercicio 10
Un bus lleva 20 pasajeros. Suben 5 y bajan 8. ¿Cuántos quedan?

<details>
<summary>Ver solución</summary>

**Cálculo:**
- $20 + 5 = 25$
- $25 - 8 = 17$
**Resultado:** $\boxed{17}$

</details>

---

## 🔑 Resumen

| Operación | Símbolo | Partes | Acción |
|-----------|---------|--------|--------|
| **Suma** | $+$ | Sumandos, Total | Juntar, agregar. |
| **Resta** | $-$ | Minuendo, Sustraendo, Diferencia | Quitar, separar. |

> **Conclusión:** La suma y la resta son las herramientas básicas para controlar cantidades. Recuerda siempre alinear las unidades con las unidades y las decenas con las decenas.
