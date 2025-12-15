# Clasificación de Triángulos por sus Lados

Los triángulos se pueden clasificar de diferentes maneras. En esta lección estudiaremos la clasificación según la **longitud de sus lados**: equiláteros, isósceles y escalenos.

---

## 📖 Tres tipos de triángulos según sus lados

| Tipo | Lados iguales | Característica |
|------|---------------|----------------|
| Equilátero | 3 iguales | Todos los lados son iguales |
| Isósceles | 2 iguales | Dos lados son iguales |
| Escaleno | 0 iguales | Todos los lados son diferentes |

---

## 📖 Triángulo Equilátero

Un triángulo es **equilátero** cuando sus **tres lados** tienen la **misma longitud**.

$$
a = b = c
$$

### Propiedades del triángulo equilátero

1. **Todos los lados son iguales** (por definición)
2. **Todos los ángulos son iguales** (y miden $60°$ cada uno)
3. Es el triángulo más **simétrico** (tiene 3 ejes de simetría)

### ¿Por qué los ángulos miden 60°?

La suma de los ángulos interiores de un triángulo es $180°$. Si los tres ángulos son iguales:

$$
3\alpha = 180° \Rightarrow \alpha = 60°
$$

### Ejemplos en la vida real

- Señal de tránsito de "ceda el paso"
- Las caras del tetraedro regular
- Logotipos y símbolos simétricos

### Ejemplo numérico

Si un lado de un triángulo equilátero mide $5$ cm, entonces:
- Lado $a = 5$ cm
- Lado $b = 5$ cm
- Lado $c = 5$ cm

---

## 📖 Triángulo Isósceles

Un triángulo es **isósceles** cuando tiene **dos lados iguales** (y uno diferente).

### Elementos especiales

- **Lados iguales**: se llaman **lados congruentes**
- **Lado diferente**: se llama **base**
- **Ángulo opuesto a la base**: se llama **ángulo del vértice**
- **Ángulos en la base**: son **iguales** entre sí

### Propiedad fundamental

En un triángulo isósceles, los **ángulos de la base son iguales**.

$$
\text{Si } a = b, \text{ entonces } \angle A = \angle B
$$

### Ejemplos en la vida real

- Percha de ropa (forma de triángulo isósceles)
- Techos de casas simétricas
- Algunas flechas y puntas

### Ejemplo numérico

Un triángulo isósceles tiene lados de $7$ cm, $7$ cm y $4$ cm.
- Lados iguales: $7$ cm y $7$ cm
- Base: $4$ cm
- Los ángulos de la base son iguales

---

## 📖 Triángulo Escaleno

Un triángulo es **escaleno** cuando sus **tres lados** tienen **longitudes diferentes**.

$$
a \neq b \neq c
$$

### Propiedades del triángulo escaleno

1. **Ningún lado es igual a otro**
2. **Ningún ángulo es igual a otro**
3. No tiene ejes de simetría

### Relación lados-ángulos

En un triángulo escaleno:
- Al lado **mayor** le corresponde el ángulo **mayor**
- Al lado **menor** le corresponde el ángulo **menor**

### Ejemplos en la vida real

- La mayoría de triángulos que dibujamos "a mano"
- Muchas formas irregulares en la naturaleza

### Ejemplo numérico

Un triángulo con lados de $3$ cm, $5$ cm y $7$ cm es escaleno porque todos sus lados son diferentes.

---

## 📖 Tabla Comparativa

| Característica | Equilátero | Isósceles | Escaleno |
|----------------|------------|-----------|----------|
| Lados iguales | 3 | 2 | 0 |
| Ángulos iguales | 3 (60° cada uno) | 2 | 0 |
| Ejes de simetría | 3 | 1 | 0 |
| Todos diferentes | No | No | Sí |

### 📊 Ilustración: Los tres tipos de triángulos

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <span>📊</span>
  <div id="jsxgraph-tipos-triangulos" style="width: 100%; height: 280px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-tipos-triangulos')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-tipos-triangulos', {
      boundingbox: [-1, 4, 15, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // EQUILÁTERO (izquierda)
    var eq1 = board.create('point', [0, 0], {size: 2, color: '#22c55e', fixed: true, name: '', withLabel: false});
    var eq2 = board.create('point', [3, 0], {size: 2, color: '#22c55e', fixed: true, name: '', withLabel: false});
    var eq3 = board.create('point', [1.5, 2.6], {size: 2, color: '#22c55e', fixed: true, name: '', withLabel: false});
    board.create('polygon', [eq1, eq2, eq3], {fillColor: '#22c55e', fillOpacity: 0.2, borders: {strokeColor: '#22c55e', strokeWidth: 3}});
    board.create('text', [1.5, -0.7, 'Equilátero'], {fontSize: 13, color: '#22c55e', fixed: true, anchorX: 'middle'});
    
    // ISÓSCELES (centro)
    var is1 = board.create('point', [5, 0], {size: 2, color: '#3b82f6', fixed: true, name: '', withLabel: false});
    var is2 = board.create('point', [9, 0], {size: 2, color: '#3b82f6', fixed: true, name: '', withLabel: false});
    var is3 = board.create('point', [7, 3], {size: 2, color: '#3b82f6', fixed: true, name: '', withLabel: false});
    board.create('polygon', [is1, is2, is3], {fillColor: '#3b82f6', fillOpacity: 0.2, borders: {strokeColor: '#3b82f6', strokeWidth: 3}});
    board.create('text', [7, -0.7, 'Isósceles'], {fontSize: 13, color: '#3b82f6', fixed: true, anchorX: 'middle'});
    
    // ESCALENO (derecha)
    var sc1 = board.create('point', [10, 0], {size: 2, color: '#f59e0b', fixed: true, name: '', withLabel: false});
    var sc2 = board.create('point', [14, 0], {size: 2, color: '#f59e0b', fixed: true, name: '', withLabel: false});
    var sc3 = board.create('point', [11, 2.5], {size: 2, color: '#f59e0b', fixed: true, name: '', withLabel: false});
    board.create('polygon', [sc1, sc2, sc3], {fillColor: '#f59e0b', fillOpacity: 0.2, borders: {strokeColor: '#f59e0b', strokeWidth: 3}});
    board.create('text', [12, -0.7, 'Escaleno'], {fontSize: 13, color: '#f59e0b', fixed: true, anchorX: 'middle'});
  }
});
</script>

> 💡 **Mnemotécnica:** **Equi**látero = lados **iguales**. **Iso**sceles = **dos** iguales. **Esca**leno = todos **diferentes**.

---

## 📖 Identificar el tipo de triángulo

### Procedimiento

1. Compara las longitudes de los tres lados
2. Si los tres son iguales → **Equilátero**
3. Si dos son iguales → **Isósceles**
4. Si todos son diferentes → **Escaleno**

### Ejemplo 1

Triángulo con lados 6, 6, 6 → **Equilátero** (tres iguales)

### Ejemplo 2

Triángulo con lados 5, 5, 8 → **Isósceles** (dos iguales)

### Ejemplo 3

Triángulo con lados 4, 6, 9 → **Escaleno** (todos diferentes)

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificar triángulos

Clasifica cada triángulo según sus lados:

| Lados | Tipo |
|-------|------|
| 8 cm, 8 cm, 8 cm | |
| 5 cm, 5 cm, 3 cm | |
| 4 cm, 7 cm, 10 cm | |
| 12 cm, 12 cm, 12 cm | |
| 6 cm, 9 cm, 6 cm | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Lados | Tipo |
|-------|------|
| 8 cm, 8 cm, 8 cm | Equilátero |
| 5 cm, 5 cm, 3 cm | Isósceles |
| 4 cm, 7 cm, 10 cm | Escaleno |
| 12 cm, 12 cm, 12 cm | Equilátero |
| 6 cm, 9 cm, 6 cm | Isósceles |

</details>

---

### Ejercicio 2: Ángulos del equilátero

Si un triángulo equilátero tiene todos sus ángulos iguales, ¿cuánto mide cada ángulo?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\text{Cada ángulo} = \frac{180°}{3} = 60°
$$

</details>

---

### Ejercicio 3: Triángulo isósceles

En un triángulo isósceles, los lados iguales miden 10 cm cada uno y la base mide 12 cm. Los ángulos de la base miden $50°$ cada uno. ¿Cuánto mide el ángulo del vértice?

<details>
<summary><strong>Ver respuesta</strong></summary>

La suma de ángulos es $180°$:

$$
50° + 50° + \text{ángulo del vértice} = 180°
$$

$$
\text{Ángulo del vértice} = 180° - 100° = 80°
$$

</details>

---

### Ejercicio 4: Verdadero o Falso

1. Un triángulo equilátero es también isósceles.
2. Un triángulo isósceles puede tener los tres lados iguales.
3. En un triángulo escaleno, al menos dos ángulos son iguales.
4. El triángulo equilátero tiene un solo eje de simetría.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero** - Tiene al menos dos lados iguales (de hecho, tiene tres)
2. **Verdadero** - Eso sería un equilátero (caso especial de isósceles)
3. **Falso** - Todos sus ángulos son diferentes
4. **Falso** - Tiene tres ejes de simetría

</details>

---
