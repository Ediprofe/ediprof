# Rectas Perpendiculares

En geometría, una de las relaciones más importantes entre rectas es la **perpendicularidad**. Dos rectas perpendiculares forman ángulos rectos, y esta relación es fundamental en construcciones, arquitectura y diseño.

---

## 📖 ¿Qué son las rectas perpendiculares?

Dos rectas son **perpendiculares** cuando se cruzan formando un **ángulo recto** ($90°$).

$$
\boxed{\text{Rectas perpendiculares} \Leftrightarrow \text{forman ángulos de } 90°}
$$

### Símbolo

Se usa el símbolo $\perp$ (perpendicular):

$$
l \perp m
$$

Se lee: "la recta $l$ es perpendicular a la recta $m$"

---

## 📖 Características de las rectas perpendiculares

### 1. Forman cuatro ángulos rectos

Cuando dos rectas son perpendiculares, los cuatro ángulos que se forman son rectos ($90°$).

### 2. Todos los ángulos son iguales

A diferencia de otras rectas secantes (donde hay ángulos agudos y obtusos), las perpendiculares forman cuatro ángulos iguales.

### 3. La relación es simétrica

Si $l \perp m$, entonces también $m \perp l$.

### 📊 Ilustración: Rectas Perpendiculares

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <span>📊</span>
  <div id="jsxgraph-perpendiculares" style="width: 100%; height: 300px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-perpendiculares')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-perpendiculares', {
      boundingbox: [-5, 5, 5, -5],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Recta horizontal (l)
    board.create('line', [[-4, 0], [4, 0]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    
    // Recta vertical (m) - perpendicular
    board.create('line', [[0, -4], [0, 4]], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    
    // Ángulo recto (cuadradito)
    board.create('angle', [[1, 0], [0, 0], [0, 1]], {radius: 0.6, orthoType: 'square', orthoSensitivity: 1, fillColor: '#f59e0b', fillOpacity: 0.5});
    
    // Etiquetas
    board.create('text', [3.5, 0.5, 'l'], {fontSize: 16, color: '#3b82f6', fixed: true});
    board.create('text', [0.5, 3.5, 'm'], {fontSize: 16, color: '#22c55e', fixed: true});
    board.create('text', [0.8, 0.8, '90°'], {fontSize: 14, color: '#f59e0b', fixed: true});
    board.create('text', [0, -4.5, 'l ⊥ m'], {fontSize: 14, color: '#1e293b', fixed: true, anchorX: 'middle'});
  }
});
</script>

> 💡 **Observa:** El cuadradito amarillo indica que el ángulo es de **90°** (ángulo recto). La notación $l \perp m$ significa "l es perpendicular a m".

---

## 📖 Ejemplos en la vida real

| Ejemplo | Descripción |
|---------|-------------|
| Esquina de una habitación | Las paredes son perpendiculares al piso |
| Poste de luz | Perpendicular al suelo |
| Cuaderno | Los bordes laterales son perpendiculares a los bordes superior e inferior |
| Cruz (+) | Los dos brazos son perpendiculares |
| Coordenadas cartesianas | El eje X es perpendicular al eje Y |

### Ejemplo 1: Las esquinas de tu cuaderno

Los lados de una hoja de papel son perpendiculares entre sí. El lado superior es perpendicular a los lados izquierdo y derecho.

### Ejemplo 2: Un edificio

Las paredes de un edificio son perpendiculares al piso para que el edificio esté estable y no se incline.

### Ejemplo 3: Una cancha de fútbol

Las líneas laterales son perpendiculares a las líneas de fondo.

---

## 📖 Cómo trazar una recta perpendicular

### Método 1: Con escuadra

1. Coloca la escuadra de modo que un lado coincida con la recta dada
2. Traza una línea siguiendo el otro lado de la escuadra
3. Las líneas son perpendiculares

### Método 2: Con compás (método clásico)

1. Desde un punto $P$ en la recta, traza arcos iguales a ambos lados
2. Desde los puntos de corte, traza arcos que se crucen arriba
3. Une ese punto con $P$
4. Esa línea es perpendicular a la recta original

---

## 📖 Distancia de un punto a una recta

La **distancia de un punto a una recta** es la longitud del segmento **perpendicular** desde el punto hasta la recta.

### Propiedad

> La perpendicular es el camino más corto desde un punto hasta una recta.

### Ejemplo

Si un punto $P$ está a cierta altura sobre una recta $l$, la distancia más corta es "bajar en línea recta" (perpendicular), no en diagonal.

---

## 📖 Propiedades importantes

### Propiedad 1: Unicidad

Por un punto exterior a una recta, pasa **una única recta perpendicular** a ella.

### Propiedad 2: Ángulos

Si $l \perp m$, entonces:
- Los cuatro ángulos formados son de $90°$
- Cualquier ángulo adyacente también es de $90°$

### Propiedad 3: Simetría respecto a perpendicular

Una recta perpendicular a otra puede actuar como eje de simetría.

---

## 📖 Rectas perpendiculares en el plano cartesiano

En geometría analítica, dos rectas son perpendiculares si sus pendientes $m_1$ y $m_2$ cumplen:

$$
m_1 \times m_2 = -1
$$

### Ejemplo

Si una recta tiene pendiente $m_1 = 2$, una recta perpendicular a ella tiene pendiente:

$$
m_2 = -\frac{1}{2}
$$

Verificación: $2 \times (-\frac{1}{2}) = -1$ ✓

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar perpendiculares

¿Cuáles de las siguientes parejas representan rectas perpendiculares?

1. Las dos agujas del reloj a las 3:00
2. Los lados de un triángulo equilátero
3. Las diagonales de un cuadrado
4. Las paredes de una habitación y el techo
5. Los brazos de la letra T

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Sí** - A las 3:00 forman 90°
2. **No** - Forman ángulos de 60°
3. **Sí** - Las diagonales del cuadrado son perpendiculares
4. **Sí** - Las paredes son perpendiculares al techo
5. **Sí** - La barra vertical es perpendicular a la horizontal

</details>

---

### Ejercicio 2: Completar

Si la recta $a$ es perpendicular a la recta $b$, y la recta $b$ es perpendicular a la recta $c$, ¿qué relación hay entre $a$ y $c$?

<details>
<summary><strong>Ver respuesta</strong></summary>

Las rectas $a$ y $c$ son **paralelas** (si están en el mismo plano).

Esto se debe a que ambas son perpendiculares a la misma recta $b$, por lo que tienen la misma dirección.

</details>

---

### Ejercicio 3: Problema de ángulos

Dos rectas perpendiculares se cruzan en el punto $O$. Si tomamos un punto $P$ en una de las rectas, ¿cuánto mide el ángulo que forma $\overrightarrow{OP}$ con cada una de las semirrectas de la otra recta?

<details>
<summary><strong>Ver respuesta</strong></summary>

El rayo $\overrightarrow{OP}$ forma ángulos de $90°$ con cada una de las dos semirrectas de la otra recta (una forma $90°$ y la otra, al ser prolongación, también forma $90°$ por el otro lado).

</details>

---

### Ejercicio 4: Verdadero o Falso

1. Dos rectas perpendiculares siempre se cruzan.
2. Si $a \perp b$ y $b \perp c$, entonces $a \perp c$.
3. Las diagonales de un rectángulo son perpendiculares.
4. Por un punto pueden pasar infinitas rectas perpendiculares a una recta dada.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero** - Deben cruzarse para formar el ángulo recto
2. **Falso** - $a$ y $c$ serían paralelas, no perpendiculares
3. **Falso** - Solo en el cuadrado las diagonales son perpendiculares
4. **Falso** - Solo pasa una única recta perpendicular

</details>

---
