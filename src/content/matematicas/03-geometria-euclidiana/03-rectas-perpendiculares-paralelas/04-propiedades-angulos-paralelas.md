# Propiedades de Ángulos en Paralelas

En la lección anterior identificamos los tipos de ángulos. Ahora aprenderás **las propiedades** que te permiten calcularlos.

### 🎯 Cheat Sheet: Propiedades clave

| Tipo de ángulos | Propiedad | Pares |
|-----------------|-----------|-------|
| Correspondientes | **=** IGUALES | (1,5), (2,6), (3,7), (4,8) |
| Alternos internos | **=** IGUALES | (3,5), (4,6) |
| Alternos externos | **=** IGUALES | (1,7), (2,8) |
| Conjugados internos | **+** SUMAN 180° | (3,6), (4,5) |
| Conjugados externos | **+** SUMAN 180° | (1,8), (2,7) |

### 📊 Referencia visual de los 8 ángulos:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div id="jsxgraph-propiedades-angulos" style="width: 100%; height: 320px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-propiedades-angulos')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-propiedades-angulos', {
      boundingbox: [-7, 6, 7, -6],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Paralelas horizontales
    board.create('line', [[-6, 2], [6, 2]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    board.create('line', [[-6, -2], [6, -2]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    
    // Transversal
    board.create('line', [[-3, -5], [3, 5]], {strokeColor: '#ef4444', strokeWidth: 3, fixed: true});
    
    // En P1 (intersección superior): ángulos 1,2,3,4
    board.create('text', [2.3, 3.2, '1'], {fontSize: 16, color: '#22c55e', fixed: true});
    board.create('text', [1, 3.2, '2'], {fontSize: 16, color: '#22c55e', fixed: true});
    board.create('text', [0, 1, '3'], {fontSize: 16, color: '#f59e0b', fixed: true});
    board.create('text', [1.3, 0.8, '4'], {fontSize: 16, color: '#f59e0b', fixed: true});
    
    // En P2 (intersección inferior): ángulos 5,6,7,8
    board.create('text', [-0.2, -1.2, '5'], {fontSize: 16, color: '#f59e0b', fixed: true});
    board.create('text', [-1.8, -1.2, '6'], {fontSize: 16, color: '#f59e0b', fixed: true});
    board.create('text', [-2.5, -3.2, '7'], {fontSize: 16, color: '#22c55e', fixed: true});
    board.create('text', [-1, -3.2, '8'], {fontSize: 16, color: '#22c55e', fixed: true});
    
    // Puntos de intersección
    board.create('point', [1.2, 2], {size: 4, color: '#1e293b', fixed: true, name: '', withLabel: false});
    board.create('point', [-1.2, -2], {size: 4, color: '#1e293b', fixed: true, name: '', withLabel: false});
    
    // Etiquetas
    board.create('text', [6.2, 2, 'l₁'], {fontSize: 14, color: '#3b82f6', fixed: true});
    board.create('text', [6.2, -2, 'l₂'], {fontSize: 14, color: '#3b82f6', fixed: true});
    board.create('text', [3.3, 5, 't'], {fontSize: 14, color: '#ef4444', fixed: true});
  }
});
</script>

> 💡 **Truco para recordar:**
> - **Alternos/Correspondientes** = IGUALES (posición cruzada o misma)
> - **Conjugados** = SUPLEMENTARIOS (mismo lado)

## 📖 Propiedad de los ángulos correspondientes

> **Propiedad:** Si dos rectas paralelas son cortadas por una transversal, los ángulos correspondientes son **iguales**.

### Ejemplo

Si $l \parallel m$ y la transversal las corta:

Los ángulos $\angle 1$ y $\angle 5$ son correspondientes, por lo tanto:

$$
\angle 1 = \angle 5
$$

### Aplicación

Si $\angle 1 = 70°$, entonces $\angle 5 = 70°$

---

## 📖 Propiedad de los ángulos alternos internos

> **Propiedad:** Si dos rectas paralelas son cortadas por una transversal, los ángulos alternos internos son **iguales**.

### Ejemplo

Los ángulos $\angle 3$ y $\angle 6$ son alternos internos, por lo tanto:

$$
\angle 3 = \angle 6
$$

### Aplicación

Si $\angle 4 = 110°$, entonces $\angle 5 = 110°$ (son alternos internos)

---

## 📖 Propiedad de los ángulos alternos externos

> **Propiedad:** Si dos rectas paralelas son cortadas por una transversal, los ángulos alternos externos son **iguales**.

### Ejemplo

Los ángulos $\angle 1$ y $\angle 8$ son alternos externos, por lo tanto:

$$
\angle 1 = \angle 8
$$

### Aplicación

Si $\angle 2 = 65°$, entonces $\angle 7 = 65°$

---

## 📖 Propiedad de los ángulos conjugados internos

> **Propiedad:** Si dos rectas paralelas son cortadas por una transversal, los ángulos conjugados internos son **suplementarios** (suman 180°).

Es decir, suman $180°$.

### Ejemplo

Los ángulos $\angle 3$ y $\angle 5$ son conjugados internos, por lo tanto:

$$
\angle 3 + \angle 5 = 180°
$$

### Aplicación

Si $\angle 3 = 75°$, entonces:

$$
\angle 5 = 180° - 75° = 105°
$$

---

## 📖 Propiedad de los ángulos conjugados externos

> **Propiedad:** Si dos rectas paralelas son cortadas por una transversal, los ángulos conjugados externos son **suplementarios** (suman 180°).

### Ejemplo

Los ángulos $\angle 1$ y $\angle 7$ son conjugados externos, por lo tanto:

$$
\angle 1 + \angle 7 = 180°
$$

---

## 📖 Resumen de propiedades

| Tipo de ángulos | Relación | Fórmula |
|-----------------|----------|---------|
| Correspondientes | Iguales | $\angle 1 = \angle 5$ |
| Alternos internos | Iguales | $\angle 3 = \angle 6$ |
| Alternos externos | Iguales | $\angle 1 = \angle 8$ |
| Conjugados internos | Suplementarios | $\angle 3 + \angle 5 = 180°$ |
| Conjugados externos | Suplementarios | $\angle 1 + \angle 7 = 180°$ |

### Regla mnemotécnica

- **Alternos** (posición cruzada) → **Iguales**
- **Correspondientes** (misma posición) → **Iguales**
- **Conjugados** (mismo lado) → **Suplementarios**

---

## 📖 El recíproco: Demostrar que son paralelas

Estas propiedades también funcionan "al revés". Si se cumple alguna de estas condiciones, las rectas son paralelas:

- Si ángulos correspondientes son iguales → las rectas son paralelas
- Si ángulos alternos internos son iguales → las rectas son paralelas
- Si ángulos conjugados internos son suplementarios → las rectas son paralelas

---

## 📖 Ejemplo completo

Dos rectas paralelas $a$ y $b$ son cortadas por una transversal $t$. Si uno de los ángulos mide $50°$, calcula todos los demás.

### Solución

Llamemos $\angle 1 = 50°$ (ángulo exterior, izquierda, arriba de $a$)

**Ángulos iguales a 50°:**
- $\angle 5$ (correspondiente a $\angle 1$) = $50°$
- $\angle 4$ (opuesto por el vértice a $\angle 1$) = $50°$
- $\angle 8$ (alterno externo a $\angle 1$) = $50°$

**Ángulos suplementarios (= 130°):**
- $\angle 2$ (adyacente a $\angle 1$) = $180° - 50° = 130°$
- $\angle 3$ (opuesto por el vértice a $\angle 2$) = $130°$
- $\angle 6$ (correspondiente a $\angle 2$) = $130°$
- $\angle 7$ (opuesto por el vértice a $\angle 6$) = $130°$

**Resultado:** Los 8 ángulos son: 50°, 130°, 130°, 50°, 50°, 130°, 130°, 50°

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular ángulos

Dos rectas paralelas son cortadas por una transversal. Si $\angle 1 = 65°$, encuentra:

1. $\angle 5$ (correspondiente)
2. $\angle 4$ (opuesto por el vértice)
3. $\angle 8$ (alterno externo)
4. $\angle 2$ (adyacente)
5. $\angle 3$ (conjugado interno de $\angle 5$)

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\angle 5 = 65°$ (correspondientes son iguales)
2. $\angle 4 = 65°$ (opuestos por el vértice son iguales)
3. $\angle 8 = 65°$ (alternos externos son iguales)
4. $\angle 2 = 115°$ (adyacentes son suplementarios)
5. $\angle 3 = 115°$ (conjugados internos son suplementarios: $180° - 65° = 115°$)

</details>

---

### Ejercicio 2: Verificar paralelismo

Una transversal corta a dos rectas. Los ángulos correspondientes miden $72°$ y $72°$. ¿Las rectas son paralelas?

<details>
<summary><strong>Ver respuesta</strong></summary>

**Sí**, las rectas son paralelas.

Cuando los ángulos correspondientes son iguales, las rectas cortadas por la transversal son paralelas.

</details>

---

### Ejercicio 3: Problema con ecuación

Dos rectas paralelas son cortadas por una transversal. Dos ángulos alternos internos miden $3x + 10°$ y $5x - 20°$. Encuentra el valor de $x$ y la medida de los ángulos.

<details>
<summary><strong>Ver respuesta</strong></summary>

Los alternos internos son iguales:

$$
3x + 10° = 5x - 20°
$$

$$
10° + 20° = 5x - 3x
$$

$$
30° = 2x
$$

$$
x = 15°
$$

Cada ángulo mide: $3(15°) + 10° = 45° + 10° = 55°$

Verificación: $5(15°) - 20° = 75° - 20° = 55°$ ✓

</details>

---

### Ejercicio 4: Problema con conjugados

Dos ángulos conjugados internos miden $(2x)°$ y $(3x + 30)°$. Encuentra $x$ y las medidas de los ángulos.

<details>
<summary><strong>Ver respuesta</strong></summary>

Los conjugados internos son suplementarios:

$$
2x + 3x + 30° = 180°
$$

$$
5x = 150°
$$

$$
x = 30°
$$

Los ángulos miden:
- Primer ángulo: $2(30°) = 60°$
- Segundo ángulo: $3(30°) + 30° = 120°$

Verificación: $60° + 120° = 180°$ ✓

</details>

---

### Ejercicio 5: Verdadero o Falso

1. Los ángulos correspondientes de paralelas cortadas por transversal son siempre iguales.
2. Los ángulos alternos internos son suplementarios.
3. Si los ángulos conjugados internos suman 180°, las rectas son paralelas.
4. Todos los ángulos formados por paralelas y transversal son iguales.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero**
2. **Falso** - Son iguales, no suplementarios
3. **Verdadero** - Es el recíproco de la propiedad
4. **Falso** - Hay dos grupos: unos de una medida y otros de su suplemento

</details>

---
