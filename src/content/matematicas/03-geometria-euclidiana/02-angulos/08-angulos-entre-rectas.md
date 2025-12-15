# Ángulos entre Rectas

Cuando dos rectas se cruzan, forman varios ángulos en el punto de intersección. En esta lección estudiaremos los tipos de ángulos que se forman y sus propiedades.

---

## 📖 Ángulos formados por dos rectas secantes

Cuando dos rectas se cruzan en un punto, se forman **cuatro ángulos**. Estos ángulos tienen relaciones especiales entre sí.

---

## 📖 Ángulos Opuestos por el Vértice

Dos ángulos son **opuestos por el vértice** cuando comparten el vértice pero sus lados son prolongaciones uno del otro (están "enfrentados").

### Propiedad fundamental

$$
\boxed{\text{Los ángulos opuestos por el vértice son iguales}}
$$

### Ejemplo 1

Si dos rectas se cruzan y uno de los ángulos mide $50°$, el ángulo opuesto por el vértice también mide $50°$.

Los otros dos ángulos (suplementarios) miden $180° - 50° = 130°$ cada uno.

### Ejemplo 2

Cuando abres las tijeras, los dos espacios "pequeños" tienen la misma abertura (son opuestos por el vértice), y los dos espacios "grandes" también son iguales entre sí.

### Demostración

Si llamamos $\alpha$ a un ángulo y $\beta$ a un ángulo adyacente:

- $\alpha + \beta = 180°$ (son suplementarios porque forman línea recta)
- El ángulo opuesto a $\beta$ es $\gamma$
- $\beta + \gamma = 180°$ (también son suplementarios)

Por lo tanto: $\alpha = \gamma$ (ambos igual a $180° - \beta$)

---

## 📖 Ángulos Adyacentes

Dos ángulos son **adyacentes** cuando:
1. Comparten el **vértice**
2. Comparten un **lado**
3. Sus otros lados están en **semiplanos opuestos**

> Los ángulos adyacentes están "uno al lado del otro".

### Propiedad

$$
\boxed{\text{Dos ángulos adyacentes formados por rectas secantes son suplementarios}}
$$

Es decir, suman $180°$.

### Ejemplo

Si un ángulo mide $65°$, su ángulo adyacente mide:

$$
180° - 65° = 115°
$$

---

## 📖 Ángulos Contiguos

Dos ángulos son **contiguos** cuando comparten el vértice y un lado, pero sin otra condición adicional.

> Todos los ángulos adyacentes son contiguos, pero no todos los contiguos son adyacentes.

### Diferencia con adyacentes

- **Contiguos**: Solo comparten vértice y un lado
- **Adyacentes**: Además, sus otros lados forman una línea recta (suman 180°)

---

## 📖 Resumen de los cuatro ángulos

Cuando dos rectas se cruzan, los cuatro ángulos cumplen:

| Posición | Relación | Propiedad |
|----------|----------|-----------|
| Opuestos | Son iguales | $\alpha = \gamma$ y $\beta = \delta$ |
| Adyacentes | Son suplementarios | $\alpha + \beta = 180°$ |
| Los cuatro | Suman 360° | $\alpha + \beta + \gamma + \delta = 360°$ |

### Ejemplo numérico

Si uno de los cuatro ángulos mide $70°$:

| Ángulo | Medida | Razón |
|--------|--------|-------|
| $\alpha$ | 70° | Dado |
| $\beta$ | 110° | Adyacente a α (suplementario) |
| $\gamma$ | 70° | Opuesto a α |
| $\delta$ | 110° | Opuesto a β |

Verificación: $70° + 110° + 70° + 110° = 360°$ ✓

**Ángulos opuestos por el vértice ($\alpha = \gamma$) y adyacentes ($\alpha + \beta = 180°$):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-angulos-rectas" style="width: 100%; height: 380px; min-height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-angulos-rectas')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-angulos-rectas', {
      boundingbox: [-1, 8, 12, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    board.create('text', [5.5, 7.3, 'Ángulos formados por dos rectas secantes'], {fontSize: 14, fontWeight: 'bold', color: '#1e293b', anchorX: 'middle'});
    
    // Punto de intersección
    var P = board.create('point', [5.5, 3.5], {name: 'P', size: 5, fixed: true, color: '#1e293b', label: {fontSize: 12, offset: [-15, -15]}});
    
    // Rectas secantes
    var r1a = board.create('point', [2, 1.5], {visible: false, fixed: true});
    var r1b = board.create('point', [9, 5.5], {visible: false, fixed: true});
    var r2a = board.create('point', [2, 5.5], {visible: false, fixed: true});
    var r2b = board.create('point', [9, 1.5], {visible: false, fixed: true});
    
    board.create('line', [r1a, r1b], {strokeColor: '#64748b', strokeWidth: 2});
    board.create('line', [r2a, r2b], {strokeColor: '#64748b', strokeWidth: 2});
    
    // Etiquetas de los 4 ángulos
    board.create('text', [6.8, 4.3, 'α'], {fontSize: 16, fontWeight: 'bold', color: '#22c55e'});
    board.create('text', [4.2, 4.3, 'β'], {fontSize: 16, fontWeight: 'bold', color: '#ef4444'});
    board.create('text', [4.2, 2.5, 'γ'], {fontSize: 16, fontWeight: 'bold', color: '#22c55e'});
    board.create('text', [6.8, 2.5, 'δ'], {fontSize: 16, fontWeight: 'bold', color: '#ef4444'});
    
    // Leyenda
    board.create('text', [5.5, 1.2, 'α = γ (opuestos por el vértice)'], {fontSize: 11, color: '#22c55e', anchorX: 'middle'});
    board.create('text', [5.5, 0.6, 'β = δ (opuestos por el vértice)'], {fontSize: 11, color: '#ef4444', anchorX: 'middle'});
    board.create('text', [5.5, 0, 'α + β = 180° (adyacentes = suplementarios)'], {fontSize: 10, color: '#64748b', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Par Lineal

Un **par lineal** es un caso especial de ángulos adyacentes donde los lados no comunes son rayos opuestos (forman una línea recta).

### Propiedad

$$
\boxed{\text{Un par lineal siempre suma } 180°}
$$

### Ejemplo

Cuando un rayo divide un ángulo llano ($180°$) en dos partes, se forma un par lineal.

---

## 📖 Ejemplos de la vida real

### Ejemplo 1: Intersección de calles

En un cruce de calles (no perpendicular), se forman cuatro esquinas. Las esquinas opuestas tienen el mismo ángulo, y las consecutivas suman $180°$.

### Ejemplo 2: Tijeras

Los ángulos formados por las hojas de las tijeras cuando están abiertas:
- Los dos ángulos "pequeños" son opuestos por el vértice (iguales)
- Los dos ángulos "grandes" son opuestos por el vértice (iguales)
- Cualquier par de ángulos consecutivos suma $180°$

### Ejemplo 3: La letra X

La letra X muestra perfectamente cuatro ángulos: dos pares de ángulos opuestos por el vértice.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular ángulos

Dos rectas se cruzan. Si uno de los ángulos mide $40°$, calcula los otros tres.

<details>
<summary><strong>Ver respuesta</strong></summary>

- Ángulo opuesto: $40°$
- Dos ángulos adyacentes: $180° - 40° = 140°$ cada uno

Los cuatro ángulos son: $40°$, $140°$, $40°$, $140°$

</details>

---

### Ejercicio 2: Identificar relaciones

Dos rectas secantes forman los ángulos $\angle 1$, $\angle 2$, $\angle 3$ y $\angle 4$ (en orden, alrededor del vértice).

Indica la relación entre:

1. $\angle 1$ y $\angle 3$
2. $\angle 1$ y $\angle 2$
3. $\angle 2$ y $\angle 4$
4. $\angle 1$ y $\angle 4$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Opuestos por el vértice (iguales)
2. Adyacentes (suplementarios)
3. Opuestos por el vértice (iguales)
4. Adyacentes (suplementarios)

</details>

---

### Ejercicio 3: Problema con ecuación

Dos rectas se cruzan. Uno de los ángulos mide $x$ y su ángulo adyacente mide $(2x + 30°)$. Encuentra el valor de $x$.

<details>
<summary><strong>Ver respuesta</strong></summary>

Los ángulos adyacentes son suplementarios:

$$
x + (2x + 30°) = 180°
$$

$$
3x + 30° = 180°
$$

$$
3x = 150°
$$

$$
x = 50°
$$

Los ángulos son: $50°$ y $130°$ (y sus opuestos: $50°$ y $130°$)

</details>

---

### Ejercicio 4: Verdadero o Falso

1. Los ángulos opuestos por el vértice siempre son iguales.
2. Los ángulos adyacentes siempre son complementarios.
3. La suma de los cuatro ángulos de dos rectas secantes es $360°$.
4. Dos ángulos opuestos por el vértice pueden sumar $180°$.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero** - Es una propiedad fundamental
2. **Falso** - Son suplementarios (suman 180°), no complementarios
3. **Verdadero** - Siempre suman una vuelta completa
4. **Verdadero** - Solo si cada uno mide 90° (rectas perpendiculares)

</details>

---

### Ejercicio 5: Problema aplicado

En el cruce de dos calles, una esquina mide $75°$. ¿Cuánto miden las otras tres esquinas?

<details>
<summary><strong>Ver respuesta</strong></summary>

- Esquina opuesta: $75°$
- Las otras dos esquinas (adyacentes): $180° - 75° = 105°$ cada una

Las cuatro esquinas miden: $75°$, $105°$, $75°$, $105°$

</details>

---
