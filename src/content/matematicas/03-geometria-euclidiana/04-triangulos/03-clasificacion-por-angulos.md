# Clasificación de Triángulos por sus Ángulos

Además de clasificar los triángulos por sus lados, podemos clasificarlos según la **medida de sus ángulos**. En esta lección estudiaremos tres tipos: acutángulos, rectángulos y obtusángulos.

---

## 📖 Tres tipos de triángulos según sus ángulos

| Tipo | Ángulo más grande | Característica |
|------|-------------------|----------------|
| Acutángulo | Menor de 90° | Todos los ángulos son agudos |
| Rectángulo | Igual a 90° | Tiene un ángulo recto |
| Obtusángulo | Mayor de 90° | Tiene un ángulo obtuso |

---

## 📖 Triángulo Acutángulo

Un triángulo es **acutángulo** cuando sus **tres ángulos son agudos** (menores de 90°).

$$
\angle A < 90°, \quad \angle B < 90°, \quad \angle C < 90°
$$

### Propiedades

- El triángulo **equilátero** siempre es acutángulo (sus ángulos son de 60°)
- Todos los ángulos miden entre 0° y 90°
- Ningún ángulo alcanza ni supera los 90°

### Ejemplos

Un triángulo con ángulos de $60°$, $60°$ y $60°$ es acutángulo (es equilátero).

Un triángulo con ángulos de $50°$, $60°$ y $70°$ es acutángulo (todos menores de 90°).

---

## 📖 Triángulo Rectángulo

Un triángulo es **rectángulo** cuando tiene **un ángulo recto** (exactamente 90°).

$$
\text{Uno de los ángulos} = 90°
$$

### Elementos especiales del triángulo rectángulo

| Elemento | Descripción |
|----------|-------------|
| **Ángulo recto** | El ángulo de 90° |
| **Hipotenusa** | El lado opuesto al ángulo recto (el más largo) |
| **Catetos** | Los dos lados que forman el ángulo recto |

### Propiedades

- Solo puede tener **un** ángulo recto
- Los otros dos ángulos son **agudos** y **complementarios** (suman 90°)
- La hipotenusa es siempre el lado **más largo**

### ¿Por qué los otros ángulos suman 90°?

Si un ángulo es de 90° y la suma total es 180°:

$$
90° + \angle A + \angle B = 180° \Rightarrow \angle A + \angle B = 90°
$$

### Ejemplos

Un triángulo con ángulos de $90°$, $45°$ y $45°$ es rectángulo (triángulo rectángulo isósceles).

Un triángulo con ángulos de $90°$, $30°$ y $60°$ es rectángulo.

### En la vida real

- Las esquinas de una hoja de papel
- Escuadras de dibujo técnico
- Muchas estructuras de construcción

---

## 📖 Triángulo Obtusángulo

Un triángulo es **obtusángulo** cuando tiene **un ángulo obtuso** (mayor de 90°).

$$
\text{Uno de los ángulos} > 90°
$$

### Propiedades

- Solo puede tener **un** ángulo obtuso
- Los otros dos ángulos son **agudos**
- El lado opuesto al ángulo obtuso es el **más largo**

### ¿Por qué solo un ángulo obtuso?

Si un ángulo es mayor de 90°, ya "consume" más de la mitad de los 180° disponibles. No queda espacio para otro ángulo obtuso.

### Ejemplo

Un triángulo con ángulos de $120°$, $35°$ y $25°$ es obtusángulo.

Verificación: $120° + 35° + 25° = 180°$ ✓

---

## 📖 Tabla Comparativa

| Tipo | Ángulo mayor | Los otros ángulos |
|------|--------------|-------------------|
| Acutángulo | $< 90°$ | Todos agudos |
| Rectángulo | $= 90°$ | Dos agudos que suman 90° |
| Obtusángulo | $> 90°$ | Dos agudos que suman menos de 90° |

### 📊 Ilustración: Los tres tipos de triángulos por ángulos

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <span>📊</span>
  <div id="jsxgraph-tipos-angulos" style="width: 100%; height: 280px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-tipos-angulos')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-tipos-angulos', {
      boundingbox: [-1, 4, 15, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // ACUTÁNGULO (izquierda) - todos ángulos < 90°
    var ac1 = board.create('point', [0, 0], {size: 2, color: '#22c55e', fixed: true, name: '', withLabel: false});
    var ac2 = board.create('point', [3, 0], {size: 2, color: '#22c55e', fixed: true, name: '', withLabel: false});
    var ac3 = board.create('point', [1.5, 2.5], {size: 2, color: '#22c55e', fixed: true, name: '', withLabel: false});
    board.create('polygon', [ac1, ac2, ac3], {fillColor: '#22c55e', fillOpacity: 0.2, borders: {strokeColor: '#22c55e', strokeWidth: 3}});
    board.create('text', [1.5, -0.7, 'Acutángulo'], {fontSize: 12, color: '#22c55e', fixed: true, anchorX: 'middle'});
    board.create('text', [1.5, 1, '< 90°'], {fontSize: 10, color: '#22c55e', fixed: true, anchorX: 'middle'});
    
    // RECTÁNGULO (centro) - un ángulo = 90°
    var re1 = board.create('point', [5, 0], {size: 2, color: '#3b82f6', fixed: true, name: '', withLabel: false});
    var re2 = board.create('point', [9, 0], {size: 2, color: '#3b82f6', fixed: true, name: '', withLabel: false});
    var re3 = board.create('point', [5, 3], {size: 2, color: '#3b82f6', fixed: true, name: '', withLabel: false});
    board.create('polygon', [re1, re2, re3], {fillColor: '#3b82f6', fillOpacity: 0.2, borders: {strokeColor: '#3b82f6', strokeWidth: 3}});
    board.create('angle', [re2, re1, re3], {radius: 0.4, orthoType: 'square', orthoSensitivity: 1, fillColor: '#ef4444', strokeColor: '#ef4444'});
    board.create('text', [7, -0.7, 'Rectángulo'], {fontSize: 12, color: '#3b82f6', fixed: true, anchorX: 'middle'});
    board.create('text', [5.5, 1.5, '90°'], {fontSize: 10, color: '#ef4444', fixed: true});
    
    // OBTUSÁNGULO (derecha) - un ángulo > 90°
    // Base 10->13. Apex (9, 2.5).
    // Vector 1->2: (3,0). Vector 1->3: (-1, 2.5). Dot product < 0 -> Obtuse at 1.
    var ob1 = board.create('point', [10, 0], {size: 2, color: '#f59e0b', fixed: true, name: '', withLabel: false});
    var ob2 = board.create('point', [13, 0], {size: 2, color: '#f59e0b', fixed: true, name: '', withLabel: false});
    var ob3 = board.create('point', [9, 2.5], {size: 2, color: '#f59e0b', fixed: true, name: '', withLabel: false});
    
    board.create('polygon', [ob1, ob2, ob3], {fillColor: '#f59e0b', fillOpacity: 0.2, borders: {strokeColor: '#f59e0b', strokeWidth: 3}});
    
    // Marcar el ángulo obtuso
    board.create('angle', [ob2, ob1, ob3], {radius: 0.4, fillColor: '#f59e0b', strokeColor: '#f59e0b', fillOpacity: 0.3});
    
    board.create('text', [12.2, -0.7, 'Obtusángulo'], {fontSize: 12, color: '#f59e0b', fixed: true, anchorX: 'middle'});
    board.create('text', [10.5, 0.4, '> 90°'], {fontSize: 10, color: '#f59e0b', fixed: true, anchorX: 'left'});
  }
});
</script>

> 💡 **Clave:** Mira el ángulo **más grande**. Si es menor de 90° → Acutángulo. Si es exactamente 90° → Rectángulo. Si es mayor de 90° → Obtusángulo.

---

## 📖 Identificar el tipo de triángulo

### Procedimiento

1. Identifica el **ángulo más grande** del triángulo
2. Si es **menor de 90°** → **Acutángulo**
3. Si es **igual a 90°** → **Rectángulo**
4. Si es **mayor de 90°** → **Obtusángulo**

### Ejemplo 1

Ángulos: 70°, 80°, 30°

El mayor es 80° (< 90°) → **Acutángulo**

### Ejemplo 2

Ángulos: 90°, 50°, 40°

El mayor es 90° → **Rectángulo**

### Ejemplo 3

Ángulos: 110°, 40°, 30°

El mayor es 110° (> 90°) → **Obtusángulo**

---

## 📖 Clasificación doble

Un triángulo puede clasificarse **por lados** Y **por ángulos** al mismo tiempo.

| Ejemplo | Por lados | Por ángulos |
|---------|-----------|-------------|
| Lados: 5, 5, 5 y Ángulos: 60°, 60°, 60° | Equilátero | Acutángulo |
| Lados: 3, 4, 5 y Ángulos: 90°, 53°, 37° | Escaleno | Rectángulo |
| Lados: 5, 5, 7 y Ángulos: 90°, 45°, 45° | Isósceles | Rectángulo |

### Ejemplo: Triángulo rectángulo isósceles

Un triángulo con ángulos 90°, 45°, 45° es:
- **Rectángulo** (tiene un ángulo de 90°)
- **Isósceles** (los dos catetos son iguales)

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificar triángulos

Clasifica cada triángulo según sus ángulos:

| Ángulos | Tipo |
|---------|------|
| 60°, 60°, 60° | |
| 90°, 60°, 30° | |
| 100°, 50°, 30° | |
| 80°, 70°, 30° | |
| 90°, 45°, 45° | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Ángulos | Tipo |
|---------|------|
| 60°, 60°, 60° | Acutángulo |
| 90°, 60°, 30° | Rectángulo |
| 100°, 50°, 30° | Obtusángulo |
| 80°, 70°, 30° | Acutángulo |
| 90°, 45°, 45° | Rectángulo |

</details>

---

### Ejercicio 2: Encontrar el tercer ángulo

Un triángulo tiene ángulos de 40° y 50°. ¿Cuánto mide el tercer ángulo? ¿Qué tipo de triángulo es?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\text{Tercer ángulo} = 180° - 40° - 50° = 90°
$$

Es un triángulo **rectángulo**.

</details>

---

### Ejercicio 3: Clasificación doble

Un triángulo tiene lados de 6 cm, 6 cm, 6 cm y ángulos de 60° cada uno. Clasifícalo:

1. Por sus lados
2. Por sus ángulos

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Por sus lados: **Equilátero** (tres lados iguales)
2. Por sus ángulos: **Acutángulo** (todos los ángulos menores de 90°)

</details>

---

### Ejercicio 4: Verdadero o Falso

1. Un triángulo puede tener dos ángulos rectos.
2. Todo triángulo equilátero es acutángulo.
3. Un triángulo rectángulo puede ser equilátero.
4. En un triángulo obtusángulo, el ángulo obtuso es siempre el mayor.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** - Dos ángulos rectos sumarían 180°, sin dejar espacio para el tercero
2. **Verdadero** - Sus tres ángulos miden 60° (todos agudos)
3. **Falso** - Si fuera equilátero, todos los ángulos serían 60°, no habría ángulo recto
4. **Verdadero** - Por definición, el ángulo obtuso (> 90°) es el mayor

</details>

---
