# Posiciones Relativas de Rectas

Cuando tenemos dos rectas en el mismo plano, estas pueden relacionarse de diferentes maneras. En esta lección aprenderemos a identificar y clasificar las **posiciones relativas** que pueden tener dos rectas entre sí.

---

## 📖 ¿Qué son las posiciones relativas?

Las **posiciones relativas** de dos rectas describen cómo se relacionan en el espacio. Dos rectas en un mismo plano pueden estar en una de tres posiciones:

1. **Rectas secantes** - Se cortan en un punto
2. **Rectas paralelas** - Nunca se cortan
3. **Rectas coincidentes** - Son la misma recta

Veamos cada una en detalle.

---

## 📖 Rectas Secantes

### ¿Qué son las rectas secantes?

Dos rectas son **secantes** cuando se cruzan en **exactamente un punto**. Ese punto se llama **punto de intersección**.

> **Definición:** Dos rectas son secantes si tienen un único punto en común.

### Características

- Tienen **diferentes direcciones** (no son paralelas)
- Se cortan en **un solo punto**
- Forman **ángulos** en el punto de intersección

### Ejemplos en la vida real

| Objeto | ¿Por qué son rectas secantes? |
|--------|------------------------------|
| Las tijeras abiertas | Dos "rectas" que se cruzan en el tornillo |
| Un cruce de calles | Dos calles que se encuentran en una esquina |
| Las aspas de un molino | Se cruzan en el centro |
| La letra X | Dos líneas que se cortan en un punto |

### Ejemplo 1

En un cruce de calles, la calle A y la calle B son rectas secantes. El cruce (la esquina) es el punto de intersección.

### Ejemplo 2

Las manecillas del reloj, cuando no marcan la misma hora, representan rectas secantes que se cortan en el centro del reloj.

### Ejemplo 3

Si dos cuerdas se cruzan formando una "X", son segmentos de rectas secantes.

---

## 📖 Rectas Paralelas

### ¿Qué son las rectas paralelas?

Dos rectas son **paralelas** cuando están en el mismo plano pero **nunca se cruzan**, sin importar cuánto las extendamos.

> **Definición:** Dos rectas son paralelas si están en el mismo plano y no tienen ningún punto en común.

### Notación

Se usa el símbolo $\parallel$ (dos barras verticales):

$$
l \parallel m \quad \text{se lee "la recta } l \text{ es paralela a la recta } m \text{"}
$$

### Características

- Tienen la **misma dirección**
- Mantienen **siempre la misma distancia** entre ellas
- **Nunca se cruzan**, ni siquiera en el infinito

### Ejemplos en la vida real

| Objeto | ¿Por qué son rectas paralelas? |
|--------|-------------------------------|
| Los rieles del tren | Siempre a la misma distancia, nunca se cruzan |
| Las líneas de un cuaderno | Equidistantes y sin cruzarse |
| Los bordes de una puerta | Paralelos entre sí |
| Las líneas de una cancha de fútbol | Las líneas laterales son paralelas |

### Ejemplo 1

Los rieles de un tren son el ejemplo clásico de rectas paralelas. Mantienen siempre la misma separación para que el tren pueda circular.

### Ejemplo 2

En un cuaderno rayado, todas las líneas horizontales son paralelas entre sí. No importa cuánto extiendas las líneas, nunca se cruzarían.

### Ejemplo 3

Los lados opuestos de un rectángulo son paralelos: el lado superior es paralelo al inferior, y el lado izquierdo es paralelo al derecho.

---

## 📖 Rectas Coincidentes

### ¿Qué son las rectas coincidentes?

Dos rectas son **coincidentes** cuando son **exactamente la misma recta**. Tienen todos sus puntos en común.

> **Definición:** Dos rectas son coincidentes si cada punto de una pertenece también a la otra. Es decir, son la misma recta descrita de dos formas diferentes.

### Características

- Tienen **infinitos puntos en común** (todos)
- Son **la misma recta** con diferente nombre o descripción
- Están completamente **superpuestas**

### Ejemplo

Si la recta $l$ pasa por los puntos $A$ y $B$, y la recta $m$ también pasa por los puntos $A$ y $B$, entonces:

$$
l = m \quad \text{(son coincidentes)}
$$

Esto se debe al axioma: "Por dos puntos pasa una única recta".

---

## 📖 Resumen Visual

| Posición | Puntos en común | Símbolo | Ejemplo cotidiano |
|----------|-----------------|---------|-------------------|
| Secantes | 1 punto | Se cruzan | Cruce de calles |
| Paralelas | 0 puntos | $\parallel$ | Rieles del tren |
| Coincidentes | Infinitos | $=$ | Misma recta con dos nombres |

**Rectas secantes, paralelas ($l \parallel m$) y coincidentes ($l = m$):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-posiciones-rectas" style="width: 100%; height: 380px; min-height: 320px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-posiciones-rectas')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-posiciones-rectas', {
      boundingbox: [-1, 9, 12, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    board.create('text', [5.5, 8.3, 'Posiciones Relativas de Dos Rectas'], {fontSize: 14, fontWeight: 'bold', color: '#1e293b', anchorX: 'middle'});
    
    // RECTAS SECANTES (izquierda)
    board.create('text', [2, 7, 'SECANTES'], {fontSize: 12, fontWeight: 'bold', color: '#ef4444', anchorX: 'middle'});
    var sec1a = board.create('point', [0.5, 4], {visible: false, fixed: true});
    var sec1b = board.create('point', [3.5, 6], {visible: false, fixed: true});
    var sec2a = board.create('point', [0.5, 6], {visible: false, fixed: true});
    var sec2b = board.create('point', [3.5, 4], {visible: false, fixed: true});
    board.create('line', [sec1a, sec1b], {strokeColor: '#ef4444', strokeWidth: 2, straightFirst: false, straightLast: false});
    board.create('line', [sec2a, sec2b], {strokeColor: '#ef4444', strokeWidth: 2, straightFirst: false, straightLast: false});
    // Punto de intersección
    board.create('point', [2, 5], {name: 'P', size: 5, fixed: true, color: '#1e293b', label: {fontSize: 10, color: '#1e293b', offset: [8, 5]}});
    board.create('text', [2, 3.3, '1 punto común'], {fontSize: 10, color: '#64748b', anchorX: 'middle'});
    
    // RECTAS PARALELAS (centro)
    board.create('text', [5.5, 7, 'PARALELAS'], {fontSize: 12, fontWeight: 'bold', color: '#22c55e', anchorX: 'middle'});
    var par1a = board.create('point', [4, 5.5], {visible: false, fixed: true});
    var par1b = board.create('point', [7, 5.5], {visible: false, fixed: true});
    var par2a = board.create('point', [4, 4.5], {visible: false, fixed: true});
    var par2b = board.create('point', [7, 4.5], {visible: false, fixed: true});
    board.create('segment', [par1a, par1b], {strokeColor: '#22c55e', strokeWidth: 2});
    board.create('segment', [par2a, par2b], {strokeColor: '#22c55e', strokeWidth: 2});
    board.create('text', [7.3, 5.5, 'l'], {fontSize: 11, fontStyle: 'italic', color: '#22c55e'});
    board.create('text', [7.3, 4.5, 'm'], {fontSize: 11, fontStyle: 'italic', color: '#22c55e'});
    board.create('text', [5.5, 3.8, 'l ∥ m'], {fontSize: 11, color: '#22c55e', anchorX: 'middle'});
    board.create('text', [5.5, 3.3, '0 puntos comunes'], {fontSize: 10, color: '#64748b', anchorX: 'middle'});
    
    // RECTAS COINCIDENTES (derecha)
    board.create('text', [9.5, 7, 'COINCIDENTES'], {fontSize: 12, fontWeight: 'bold', color: '#3b82f6', anchorX: 'middle'});
    var coi1a = board.create('point', [8, 5], {visible: false, fixed: true});
    var coi1b = board.create('point', [11, 5], {visible: false, fixed: true});
    board.create('segment', [coi1a, coi1b], {strokeColor: '#3b82f6', strokeWidth: 4});
    board.create('text', [11.2, 5.3, 'l = m'], {fontSize: 11, color: '#3b82f6'});
    board.create('text', [9.5, 3.3, '∞ puntos comunes'], {fontSize: 10, color: '#64748b', anchorX: 'middle'});
    
    // Leyenda inferior
    board.create('text', [5.5, 1.5, '¡Observa cómo se relacionan las rectas en cada caso!'], {fontSize: 11, color: '#475569', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 ¿Cómo identificar la posición relativa?

Para determinar qué relación tienen dos rectas, sigue estos pasos:

### Paso 1: Observa si se cruzan

- **Sí se cruzan** → Son **secantes**
- **No se cruzan** → Pasa al paso 2

### Paso 2: Si no se cruzan, ¿son la misma recta?

- **Sí, son la misma** → Son **coincidentes**
- **No, son diferentes** → Son **paralelas**

### Ejemplo aplicado

En la fachada de una casa:
- Las ventanas de arriba y abajo están en líneas **paralelas**
- El marco de cada ventana tiene lados que se cruzan: son **secantes**
- La línea superior del techo es una sola recta, aunque la describamos de diferentes formas: **coincidente** consigo misma

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificación

Clasifica cada par de rectas como **secantes**, **paralelas** o **coincidentes**:

| Par de rectas | Clasificación |
|---------------|---------------|
| Las dos hojas de una tijera abierta | |
| Los lados largos de tu escritorio | |
| Los brazos de una "X" | |
| Las líneas horizontales de tu cuaderno | |
| Una recta y ella misma | |
| Los bordes superior e inferior de la pizarra | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Par de rectas | Clasificación |
|---------------|---------------|
| Las dos hojas de una tijera abierta | Secantes |
| Los lados largos de tu escritorio | Paralelas |
| Los brazos de una "X" | Secantes |
| Las líneas horizontales de tu cuaderno | Paralelas |
| Una recta y ella misma | Coincidentes |
| Los bordes superior e inferior de la pizarra | Paralelas |

</details>

---

### Ejercicio 2: Completar con símbolo

Completa con el símbolo correcto ($\parallel$ para paralelas, o "secantes" si se cortan):

1. En un cuadrado, el lado $AB$ ______ el lado $CD$ (lados opuestos)
2. En un cuadrado, el lado $AB$ ______ el lado $BC$ (lados consecutivos)
3. En un rectángulo, las diagonales son ______

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $AB \parallel CD$ (paralelas)
2. $AB$ y $BC$ son secantes (se cruzan en $B$)
3. Secantes (se cruzan en el centro)

</details>

---

### Ejercicio 3: Observación del entorno

Mira a tu alrededor y encuentra:

1. **Dos objetos** que representen rectas paralelas
2. **Dos objetos** que representen rectas secantes
3. ¿Puedes encontrar un ejemplo de rectas coincidentes en el mundo real?

<details>
<summary><strong>Ver ejemplos de respuestas</strong></summary>

1. Paralelas: bordes de una mesa, líneas de una hoja rayada, rieles de escalera
2. Secantes: esquinas de la habitación, marco de ventana, tijeras abiertas
3. Coincidentes: es difícil en el mundo real porque una recta coincidente es la misma recta. Ejemplo abstracto: "la recta que une mi casa con tu casa" y "la recta que une tu casa con mi casa" son coincidentes.

</details>

---

### Ejercicio 4: Problema de razonamiento

Un arquitecto dibuja el plano de una casa. Traza dos paredes representadas por las rectas $l$ y $m$.

1. Si las paredes forman una esquina, ¿qué tipo de rectas son $l$ y $m$?
2. Si las paredes son los lados de un pasillo largo, ¿qué tipo de rectas son $l$ y $m$?

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Si forman esquina → **Secantes** (se cruzan en la esquina)
2. Si son lados de un pasillo → **Paralelas** (el pasillo mantiene el mismo ancho)

</details>

---
