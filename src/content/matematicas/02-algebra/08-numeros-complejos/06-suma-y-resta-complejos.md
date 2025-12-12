# ➕ Suma y Resta de Números Complejos

En esta lección aprenderemos a sumar y restar números complejos.

---

## 📖 Regla de suma

Para sumar números complejos, sumamos las partes reales entre sí y las partes imaginarias entre sí:

$$
(a + bi) + (c + di) = (a + c) + (b + d)i
$$

---

### Ejemplo 1

Calcular $(3 + 2i) + (5 + 4i)$.

$$
(3 + 2i) + (5 + 4i) = (3 + 5) + (2 + 4)i = 8 + 6i
$$

$$
\boxed{(3 + 2i) + (5 + 4i) = 8 + 6i}
$$

Visualización de la suma (método punta a cola):

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 480px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-suma-complejos" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var board = JXG.JSXGraph.initBoard('jsxgraph-suma-complejos', {
      boundingbox: [-1, 8, 10, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Origen
    var O = board.create('point', [0, 0], { name: '', size: 3, fixed: true, color: '#64748b' });
    
    // PASO 1: z₁ = 3 + 2i (azul, desde el origen)
    var z1 = board.create('point', [3, 2], { name: '', size: 5, fixed: true, color: '#3b82f6' });
    board.create('arrow', [O, z1], { strokeColor: '#3b82f6', strokeWidth: 4, fixed: true });
    board.create('text', [1, 2.3, '① z₁ = 3 + 2i'], { fontSize: 13, strokeColor: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true });
    
    // PASO 2: z₂ = 5 + 4i (verde, desde la PUNTA de z₁)
    var sum = board.create('point', [8, 6], { name: '', size: 5, fixed: true, color: '#ef4444' });
    board.create('arrow', [z1, sum], { strokeColor: '#22c55e', strokeWidth: 4, fixed: true });
    board.create('text', [5.5, 5, '② z₂ = 5 + 4i'], { fontSize: 13, strokeColor: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true });
    
    // RESULTADO: z₁ + z₂ = 8 + 6i (rojo, del origen al final)
    board.create('arrow', [O, sum], { strokeColor: '#ef4444', strokeWidth: 3, dash: 2, fixed: true });
    board.create('text', [6.5, 7, '③ Resultado = 8 + 6i'], { fontSize: 13, strokeColor: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true });
    
    // Etiquetas de ejes
    board.create('text', [9.3, -0.5, 'Real'], { fontSize: 11, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    board.create('text', [-0.7, 7.3, 'Imag'], { fontSize: 11, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true });
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **Método punta a cola:**  
> ① Dibujamos $z_1$ desde el origen (azul).  
> ② Dibujamos $z_2$ desde la **punta** de $z_1$ (verde).  
> ③ El **resultado** va del origen a donde terminamos (rojo punteado).

---

### Ejemplo 2

Calcular $(4 + 7i) + (-2 + 3i)$.

$$
(4 + 7i) + (-2 + 3i) = (4 - 2) + (7 + 3)i = 2 + 10i
$$

$$
\boxed{(4 + 7i) + (-2 + 3i) = 2 + 10i}
$$

---

### Ejemplo 3

Calcular $(-1 + 5i) + (3 - 2i)$.

$$
(-1 + 5i) + (3 - 2i) = (-1 + 3) + (5 - 2)i = 2 + 3i
$$

$$
\boxed{(-1 + 5i) + (3 - 2i) = 2 + 3i}
$$

---

## 📖 Regla de resta

Para restar números complejos, restamos las partes reales y las partes imaginarias:

$$
(a + bi) - (c + di) = (a - c) + (b - d)i
$$

---

### Ejemplo 4

Calcular $(7 + 4i) - (3 + 2i)$.

$$
(7 + 4i) - (3 + 2i) = (7 - 3) + (4 - 2)i = 4 + 2i
$$

$$
\boxed{(7 + 4i) - (3 + 2i) = 4 + 2i}
$$

---

### Ejemplo 5

Calcular $(5 + 3i) - (8 - i)$.

$$
(5 + 3i) - (8 - i) = (5 - 8) + (3 - (-1))i = -3 + 4i
$$

$$
\boxed{(5 + 3i) - (8 - i) = -3 + 4i}
$$

---

### Ejemplo 6

Calcular $(2 - 6i) - (-4 + 2i)$.

$$
(2 - 6i) - (-4 + 2i) = (2 - (-4)) + (-6 - 2)i = 6 - 8i
$$

$$
\boxed{(2 - 6i) - (-4 + 2i) = 6 - 8i}
$$

---

## 📖 Operaciones combinadas

### Ejemplo 7

Calcular $(2 + 3i) + (4 - i) - (1 + 5i)$.

$$
= (2 + 4 - 1) + (3 - 1 - 5)i = 5 - 3i
$$

$$
\boxed{(2 + 3i) + (4 - i) - (1 + 5i) = 5 - 3i}
$$

---

### Ejemplo 8

Calcular $3(2 + i) + 2(1 - 3i)$.

**Paso 1:** Distribuimos:

$$
3(2 + i) = 6 + 3i
$$

$$
2(1 - 3i) = 2 - 6i
$$

**Paso 2:** Sumamos:

$$
(6 + 3i) + (2 - 6i) = 8 - 3i
$$

$$
\boxed{3(2 + i) + 2(1 - 3i) = 8 - 3i}
$$

---

### Ejemplo 9

Simplificar $(a + bi) + (a - bi)$.

$$
(a + bi) + (a - bi) = 2a + 0i = 2a
$$

$$
\boxed{(a + bi) + (a - bi) = 2a}
$$

> La suma de un complejo con su conjugado da el doble de la parte real.

---

### Ejemplo 10

Simplificar $(a + bi) - (a - bi)$.

$$
(a + bi) - (a - bi) = 0 + 2bi = 2bi
$$

$$
\boxed{(a + bi) - (a - bi) = 2bi}
$$

> La diferencia de un complejo con su conjugado da el doble de la parte imaginaria.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula $(5 + 2i) + (3 + 4i)$.

<details>
<summary>Ver solución</summary>

$$
8 + 6i
$$

</details>

---

**Ejercicio 2:** Calcula $(6 - 3i) + (-2 + 7i)$.

<details>
<summary>Ver solución</summary>

$$
4 + 4i
$$

</details>

---

**Ejercicio 3:** Calcula $(9 + i) - (4 + 6i)$.

<details>
<summary>Ver solución</summary>

$$
5 - 5i
$$

</details>

---

**Ejercicio 4:** Calcula $(-3 + 2i) - (-5 - 4i)$.

<details>
<summary>Ver solución</summary>

$$
2 + 6i
$$

</details>

---

**Ejercicio 5:** Calcula $2(3 + 4i) - 3(1 - 2i)$.

<details>
<summary>Ver solución</summary>

$$
(6 + 8i) - (3 - 6i) = 3 + 14i
$$

</details>

---

**Ejercicio 6:** Calcula $(1 + i) + (2 + 2i) + (3 + 3i)$.

<details>
<summary>Ver solución</summary>

$$
(1 + 2 + 3) + (1 + 2 + 3)i = 6 + 6i
$$

</details>

---
