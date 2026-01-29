# **División de Números Naturales**

La división es simplemente **repartir equitativamente**. Si tienes 20 dulces y 4 amigos, a todos les quieres dar lo mismo para que nadie se enoje. Eso es dividir. Es la operación inversa de multiplicar: si $5 \times 4 = 20$, entonces $20 \div 4 = 5$.

---

## 🎯 ¿Qué vas a aprender?

- Entender el concepto de reparto (división exacta e inexacta).
- Dominar partes de la división: Dividendo, divisor, cociente y residuo.
- Realizar divisiones por 1, 2 y más cifras.
- Verificar si tu resultado está bien hecho (La Prueba de la División).

---

## Conceptos Clave

La división responde a la pregunta: "¿Cuántas veces cabe este número en aquel otro?".

Partes:
- **Dividendo:** La cantidad total a repartir (Adentro o izquierda).
- **Divisor:** En cuántas partes se reparte (Afuera o derecha).
- **Cociente:** Cuánto le toca a cada uno (Resultado).
- **Residuo:** Lo que sobra (Siempre debe ser menor que el divisor).

$$ \text{Dividendo} = (\text{Divisor} \times \text{Cociente}) + \text{Residuo} $$

---

## División por 1 Cifra

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: División Exacta
Divide $24 \div 6$.
- Busco en la tabla del 6: $6 \times 4 = 24$.
- Cabe exactamente 4 veces.
**Residuo:** 0. **Cociente:** $\boxed{4}$

#### Ejemplo 2: División Inexacta
Divide $20 \div 3$.
- Tabla del 3: $3 \times 6 = 18$ (Se acerca). $3 \times 7 = 21$ (Se pasa).
- Cabe 6 veces. Sobran $20 - 18 = 2$.
**Cociente:** $\boxed{6}$ **Residuo:** $\boxed{2}$

#### Ejemplo 3: Dividendo de dos cifras
Divide $95 \div 4$.
1.  **Tomo el 9:** $4$ cabe 2 veces en $9$. ($4 \times 2 = 8$). Sobra 1.
2.  **Bajo el 5:** Se forma el 15.
3.  **Tomo el 15:** $4$ cabe 3 veces en $15$. ($4 \times 3 = 12$). Sobran 3.
**Cociente:** $\boxed{23}$ **Residuo:** $\boxed{3}$

#### Ejemplo 4: División con cero al cociente
Divide $61 \div 3$.
1.  **Tomo el 6:** $3$ cabe 2 veces ($3 \times 2 = 6$). Sobra 0.
2.  **Bajo el 1:** ¿Cuántas veces cabe 3 en 1? Cero veces. Pongo 0 en el cociente.
**Cociente:** $\boxed{20}$ **Residuo:** $\boxed{1}$

#### Ejemplo 5: División Grande
Divide $500 \div 5$.
1.  $5$ en $5$ cabe 1. Sobra 0.
2.  Bajo 0. $5$ en $0$ cabe 0.
3.  Bajo 0. $5$ en $0$ cabe 0.
**Cociente:** $\boxed{100}$

---

## División por 2 Cifras

El proceso es el mismo: "Tomo cifras, busco, multiplico, resto y bajo la siguiente". A veces hay que tantear (probar) el número.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: División Exacta
Divide $144 \div 12$.
1.  Tomo 14. 12 cabe 1 vez en 14. Sobran 2.
2.  Bajo el 4. Se forma 24.
3.  12 cabe 2 veces en 24 ($12 \times 2 = 24$). Sobra 0.
**Cociente:** $\boxed{12}$

#### Ejemplo 7: Tanteo
Divide $245 \div 35$.
- Tapo las unidades: ¿Cuántas veces cabe 3 en 24? Parece 8.
- Pruebo $35 \times 8 = 280$. ¡Se pasa!
- Pruebo con 7. $35 \times 7 = 245$. Exacto.
**Cociente:** $\boxed{7}$

#### Ejemplo 8: División Larga
Divide $1728 \div 24$.
1.  Tomo 17... no cabe. Tomo 172.
2.  ¿24 en 172? Pruebo con 7 ($24 \times 7 = 168$). Sobran $172-168=4$.
3.  Bajo el 8. Se forma 48.
4.  24 en 48 cabe 2 veces exactas.
**Cociente:** $\boxed{72}$

#### Ejemplo 9: Residuo Grande
Divide $100 \div 23$.
- Pruebo 4. $23 \times 4 = 92$.
- $100 - 92 = 8$.
- Como 8 es menor que 23, terminamos.
**Cociente:** $\boxed{4}$ **Residuo:** $\boxed{8}$

#### Ejemplo 10: La Prueba
Verifica si $89 \div 6 = 14$ con residuo 5.
$$ (6 \times 14) + 5 = 84 + 5 = 89 $$
Es correcto porque nos dio el dividendo original.

---

<!-- Conservando imágenes existentes -->

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-div2" class="jsxgraph-container" style="width: 100%; height: 260px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-div2')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-div2', {
      boundingbox: [-0.5, 6, 8, -0.5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Dividendo: 144
    board.create('text', [1, 5, '1'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [1.8, 5, '4'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [2.6, 5, '4'], {fontSize: 24, strokeColor: '#3b82f6', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // L
    board.create('segment', [[3.3, 5.6], [3.3, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    board.create('segment', [[3.3, 4.2], [5.8, 4.2]], {strokeColor: '#374151', strokeWidth: 2, fixed: true});
    // Divisor: 12
    board.create('text', [4, 5, '1'], {fontSize: 24, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4.7, 5, '2'], {fontSize: 24, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Cociente: 12
    board.create('text', [4, 3.4, '1'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.create('text', [4.7, 3.4, '2'], {fontSize: 24, strokeColor: '#ef4444', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    // Desarrollo: 12 × 1 = 12
    board.create('text', [1, 3.8, '1'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [1.8, 3.8, '2'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[0.6, 3.5], [2.2, 3.5]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Resto: 14 - 12 = 2, baja 4 → 24
    board.create('text', [1.8, 2.9, '2'], {fontSize: 16, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    board.create('text', [2.6, 2.9, '4'], {fontSize: 16, strokeColor: '#64748b', fixed: true, anchorX: 'middle'});
    // 12 × 2 = 24
    board.create('text', [1.8, 2.2, '2'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('text', [2.6, 2.2, '4'], {fontSize: 16, strokeColor: '#9333ea', fixed: true, anchorX: 'middle'});
    board.create('segment', [[1.4, 1.9], [3, 1.9]], {strokeColor: '#9333ea', strokeWidth: 1, fixed: true});
    // Residuo: 0
    board.create('text', [2.6, 1.3, '0'], {fontSize: 18, strokeColor: '#22c55e', fixed: true, anchorX: 'middle', cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Reparte 72 manzanas en 9 cajas. ¿Cuántas van en cada caja?

<details>
<summary>Ver solución</summary>

**Operación:** $72 \div 9$.
**Cálculo:** $9 \times 8 = 72$.
**Resultado:** $\boxed{8}$

</details>

### Ejercicio 2
Divide $84 \div 7$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
- 7 en 8 cabe 1 (sobra 1).
- Bajo el 4 (se forma 14).
- 7 en 14 cabe 2.
**Resultado:** $\boxed{12}$

</details>

### Ejercicio 3
Divide $96 \div 8$.

<details>
<summary>Ver solución</summary>

- 8 en 9 cabe 1 (sobra 1).
- 8 en 16 cabe 2.
**Resultado:** $\boxed{12}$

</details>

### Ejercicio 4
Divide $125 \div 5$.

<details>
<summary>Ver solución</summary>

- 5 en 12 cabe 2 (sobran 2).
- 5 en 25 cabe 5.
**Resultado:** $\boxed{25}$

</details>

### Ejercicio 5
Calcula $156 \div 12$.

<details>
<summary>Ver solución</summary>

- 12 en 15 cabe 1 (sobran 3).
- 12 en 36 cabe 3.
**Resultado:** $\boxed{13}$

</details>

### Ejercicio 6
Divide $89 \div 6$ y halla el residuo.

<details>
<summary>Ver solución</summary>

- 6 en 8 cabe 1 (sobra 2).
- 6 en 29 cabe 4 ($6 \times 4 = 24$). Sobran $29-24=5$.
**Resultado:** $\boxed{\text{Cociente: } 14, \text{ Residuo: } 5}$

</details>

### Ejercicio 7
Divide $250 \div 15$ y halla el residuo.

<details>
<summary>Ver solución</summary>

- 15 en 25 cabe 1 (sobran 10).
- 15 en 100 cabe 6 ($15 \times 6 = 90$). Sobran 10.
**Resultado:** $\boxed{\text{Cociente: } 16, \text{ Residuo: } 10}$

</details>

### Ejercicio 8
Divide $1000 \div 8$.

<details>
<summary>Ver solución</summary>

- 8 en 10 cabe 1 (sobra 2).
- 8 en 20 cabe 2 (sobra 4).
- 8 en 40 cabe 5.
**Resultado:** $\boxed{125}$

</details>

### Ejercicio 9
Calcula $2340 \div 45$.

<details>
<summary>Ver solución</summary>

- 45 en 234: probamos 5. ($45 \times 5 = 225$). Sobra 9.
- 45 en 90 cabe 2.
**Resultado:** $\boxed{52}$

</details>

### Ejercicio 10
Verifica si $20 \div 6 = 3$ con residuo 2 está bien.

<details>
<summary>Ver solución</summary>

**Prueba:** $(6 \times 3) + 2 = 18 + 2 = 20$.
**Resultado:** $\boxed{\text{Correcto}}$

</details>

---

## 🔑 Resumen

| Concepto | Significado | Ejemplo |
|----------|-------------|---------|
| **Exacta** | Residuo es 0 | $10 \div 2 = 5$ |
| **Inexacta** | Residuo no es 0 | $10 \div 3 = 3$ (sobra 1) |
| **Prueba** | $(D \times C) + R$ | $3 \times 3 + 1 = 10$ |

> **Conclusión:** Dividir es repartir. Siempre cuida que lo que sobre (residuo) sea más pequeño que el número por el que divides. Si sobra más, ¡te cupo una vez más!
