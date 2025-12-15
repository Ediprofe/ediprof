# Ángulos Complementarios y Suplementarios

Además de clasificar ángulos por su medida individual, podemos estudiar **relaciones entre pares de ángulos**. Las relaciones más importantes son: ángulos complementarios, suplementarios y conjugados.

---

## 📖 Ángulos Complementarios

Dos ángulos son **complementarios** cuando la suma de sus medidas es igual a $90°$.

$$
\boxed{\alpha + \beta = 90°}
$$

### Ejemplo 1

Si un ángulo mide $30°$, su complemento mide:

$$
90° - 30° = 60°
$$

Los ángulos de $30°$ y $60°$ son complementarios.

### Ejemplo 2

Si un ángulo mide $45°$, su complemento mide:

$$
90° - 45° = 45°
$$

Un ángulo de $45°$ es **complemento de sí mismo**.

### Ejemplo 3

Si un ángulo mide $25°$, su complemento mide:

$$
90° - 25° = 65°
$$

### Fórmula del complemento

Si un ángulo mide $\alpha$, su **complemento** es:

$$
\text{Complemento de } \alpha = 90° - \alpha
$$

### Nota importante

> Solo los ángulos **agudos** (menores de 90°) tienen complemento positivo.

Un ángulo de $100°$ no tiene complemento (sería negativo: $90° - 100° = -10°$).

---

## 📖 Ángulos Suplementarios

Dos ángulos son **suplementarios** cuando la suma de sus medidas es igual a $180°$.

$$
\boxed{\alpha + \beta = 180°}
$$

### Ejemplo 1

Si un ángulo mide $60°$, su suplemento mide:

$$
180° - 60° = 120°
$$

Los ángulos de $60°$ y $120°$ son suplementarios.

### Ejemplo 2

Si un ángulo mide $90°$, su suplemento mide:

$$
180° - 90° = 90°
$$

Un ángulo recto es **suplemento de sí mismo**.

### Ejemplo 3

Si un ángulo mide $45°$, su suplemento mide:

$$
180° - 45° = 135°
$$

### Fórmula del suplemento

Si un ángulo mide $\alpha$, su **suplemento** es:

$$
\text{Suplemento de } \alpha = 180° - \alpha
$$

### Nota importante

> Solo los ángulos menores de $180°$ tienen suplemento positivo.

---

## 📖 Ángulos Conjugados

Dos ángulos son **conjugados** (o **explementarios**) cuando la suma de sus medidas es igual a $360°$.

$$
\boxed{\alpha + \beta = 360°}
$$

### Ejemplo 1

Si un ángulo mide $60°$, su conjugado mide:

$$
360° - 60° = 300°
$$

### Ejemplo 2

Si un ángulo mide $180°$, su conjugado mide:

$$
360° - 180° = 180°
$$

Un ángulo llano es **conjugado de sí mismo**.

### Fórmula del conjugado

Si un ángulo mide $\alpha$, su **conjugado** es:

$$
\text{Conjugado de } \alpha = 360° - \alpha
$$

---

## 📖 Tabla Resumen

| Relación | Suma | Condición |
|----------|------|-----------|
| Complementarios | $90°$ | Solo ángulos agudos tienen complemento |
| Suplementarios | $180°$ | Ángulos menores de 180° |
| Conjugados | $360°$ | Cualquier ángulo |

---

## 📖 Ejemplos comparativos

Para un ángulo de $50°$:

| Relación | Cálculo | Resultado |
|----------|---------|-----------|
| Complemento | $90° - 50°$ | $40°$ |
| Suplemento | $180° - 50°$ | $130°$ |
| Conjugado | $360° - 50°$ | $310°$ |

**Ángulos complementarios ($\alpha + \beta = 90°$) y suplementarios ($\alpha + \beta = 180°$):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-relaciones-angulos" style="width: 100%; height: 380px; min-height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-relaciones-angulos')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-relaciones-angulos', {
      boundingbox: [-1, 9, 15, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    board.create('text', [7, 8.3, 'Relaciones entre Ángulos'], {fontSize: 14, fontWeight: 'bold', color: '#1e293b', anchorX: 'middle'});
    
    // COMPLEMENTARIOS (suman 90°) - izquierda
    board.create('text', [2.5, 7, 'COMPLEMENTARIOS'], {fontSize: 11, fontWeight: 'bold', color: '#22c55e', anchorX: 'middle'});
    var c_v = board.create('point', [2.5, 4.5], {name: '', size: 4, fixed: true, color: '#1e293b'});
    var c_p1 = board.create('point', [5, 4.5], {visible: false, fixed: true});
    var c_p2 = board.create('point', [4.3, 6.3], {visible: false, fixed: true}); // ~60°
    var c_p3 = board.create('point', [2.5, 6.5], {visible: false, fixed: true}); // 90°
    
    board.create('segment', [c_v, c_p1], {strokeColor: '#22c55e', strokeWidth: 2});
    board.create('segment', [c_v, c_p2], {strokeColor: '#f59e0b', strokeWidth: 2});
    board.create('segment', [c_v, c_p3], {strokeColor: '#22c55e', strokeWidth: 2, dash: 2});
    
    board.create('text', [3.8, 5, 'α'], {fontSize: 12, color: '#22c55e'});
    board.create('text', [3.2, 5.8, 'β'], {fontSize: 12, color: '#f59e0b'});
    board.create('text', [2.5, 3, 'α + β = 90°'], {fontSize: 11, color: '#64748b', anchorX: 'middle'});
    
    // SUPLEMENTARIOS (suman 180°) - centro
    board.create('text', [7.5, 7, 'SUPLEMENTARIOS'], {fontSize: 11, fontWeight: 'bold', color: '#3b82f6', anchorX: 'middle'});
    var s_v = board.create('point', [7.5, 4.5], {name: '', size: 4, fixed: true, color: '#1e293b'});
    var s_p1 = board.create('point', [10, 4.5], {visible: false, fixed: true});
    var s_p2 = board.create('point', [5, 4.5], {visible: false, fixed: true});
    var s_p3 = board.create('point', [9, 6], {visible: false, fixed: true}); // ~45°
    
    board.create('segment', [s_v, s_p1], {strokeColor: '#3b82f6', strokeWidth: 2});
    board.create('segment', [s_v, s_p2], {strokeColor: '#3b82f6', strokeWidth: 2});
    board.create('segment', [s_v, s_p3], {strokeColor: '#ef4444', strokeWidth: 2});
    
    board.create('text', [8.5, 5, 'α'], {fontSize: 12, color: '#ef4444'});
    board.create('text', [6.2, 5, 'β'], {fontSize: 12, color: '#3b82f6'});
    board.create('text', [7.5, 3, 'α + β = 180°'], {fontSize: 11, color: '#64748b', anchorX: 'middle'});
    
    // Leyenda
    board.create('text', [7, 1.5, 'Los ángulos complementarios suman 90° (ángulo recto)'], {fontSize: 10, color: '#475569', anchorX: 'middle'});
    board.create('text', [7, 0.8, 'Los ángulos suplementarios suman 180° (ángulo llano)'], {fontSize: 10, color: '#475569', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Aplicaciones prácticas

### Ejemplo 1: Ángulos de un triángulo rectángulo

En un triángulo rectángulo, los dos ángulos agudos son **complementarios** (suman 90°).

Si uno mide $35°$, el otro mide $90° - 35° = 55°$.

### Ejemplo 2: Ángulos adyacentes en línea recta

Dos ángulos que forman una línea recta son **suplementarios** (suman 180°).

Si uno mide $115°$, el otro mide $180° - 115° = 65°$.

### Ejemplo 3: Encontrar un ángulo

Si el complemento de un ángulo es el doble del ángulo, ¿cuánto mide el ángulo?

Sea $x$ el ángulo. Su complemento es $90° - x$.

$$
90° - x = 2x
$$

$$
90° = 3x
$$

$$
x = 30°
$$

El ángulo mide $30°$ y su complemento es $60°$.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Encontrar el complemento

Calcula el complemento de cada ángulo:

1. 20°
2. 45°
3. 75°
4. 10°
5. 89°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $90° - 20° = 70°$
2. $90° - 45° = 45°$
3. $90° - 75° = 15°$
4. $90° - 10° = 80°$
5. $90° - 89° = 1°$

</details>

---

### Ejercicio 2: Encontrar el suplemento

Calcula el suplemento de cada ángulo:

1. 30°
2. 90°
3. 120°
4. 45°
5. 179°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $180° - 30° = 150°$
2. $180° - 90° = 90°$
3. $180° - 120° = 60°$
4. $180° - 45° = 135°$
5. $180° - 179° = 1°$

</details>

---

### Ejercicio 3: Encontrar complemento, suplemento y conjugado

Para el ángulo de $70°$, calcula:

1. Su complemento
2. Su suplemento
3. Su conjugado

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Complemento: $90° - 70° = 20°$
2. Suplemento: $180° - 70° = 110°$
3. Conjugado: $360° - 70° = 290°$

</details>

---

### Ejercicio 4: Problema con ecuación

El suplemento de un ángulo es cinco veces el ángulo. ¿Cuánto mide el ángulo?

<details>
<summary><strong>Ver respuesta</strong></summary>

Sea $x$ el ángulo. Su suplemento es $180° - x$.

$$
180° - x = 5x
$$

$$
180° = 6x
$$

$$
x = 30°
$$

El ángulo mide $30°$ y su suplemento es $150°$.

Verificación: $150° = 5 \times 30°$ ✓

</details>

---

### Ejercicio 5: Problema con ecuación (complemento)

La diferencia entre un ángulo y su complemento es $20°$. ¿Cuánto mide el ángulo?

<details>
<summary><strong>Ver respuesta</strong></summary>

Sea $x$ el ángulo. Su complemento es $90° - x$.

$$
x - (90° - x) = 20°
$$

$$
x - 90° + x = 20°
$$

$$
2x = 110°
$$

$$
x = 55°
$$

El ángulo mide $55°$ y su complemento es $35°$.

Verificación: $55° - 35° = 20°$ ✓

</details>

---
