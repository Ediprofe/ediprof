# Teorema de Pitágoras

El **Teorema de Pitágoras** es probablemente el teorema más famoso de las matemáticas. Relaciona los lados de un triángulo rectángulo y tiene incontables aplicaciones prácticas.

---

## 📖 Pitágoras de Samos

Pitágoras (570-495 a.C.) fue un matemático y filósofo griego. Aunque el teorema lleva su nombre, los babilonios y egipcios ya conocían esta relación siglos antes.

---

## 📖 Enunciado del teorema

> **Teorema de Pitágoras:** En todo triángulo rectángulo, el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos.

$$
\boxed{c^2 = a^2 + b^2}
$$

Donde:
- $c$ = **hipotenusa** (lado opuesto al ángulo recto, el más largo)
- $a$ y $b$ = **catetos** (los lados que forman el ángulo recto)

---

## 📖 Recordatorio: Partes del triángulo rectángulo

| Elemento | Descripción |
|----------|-------------|
| Ángulo recto | El ángulo de 90° |
| Catetos | Los dos lados que forman el ángulo recto |
| Hipotenusa | El lado opuesto al ángulo recto (siempre el más largo) |

### 📊 Ilustración: Teorema de Pitágoras

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <span>📊</span>
  <div id="jsxgraph-pitagoras" style="width: 100%; height: 350px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-pitagoras')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-pitagoras', {
      boundingbox: [-2, 7, 10, -4],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Triángulo 3-4-5
    var A = board.create('point', [0, 0], {size: 3, color: '#ef4444', fixed: true, name: '', withLabel: false});
    var B = board.create('point', [4, 0], {size: 3, color: '#ef4444', fixed: true, name: '', withLabel: false});
    var C = board.create('point', [0, 3], {size: 3, color: '#ef4444', fixed: true, name: '', withLabel: false});
    
    board.create('polygon', [A, B, C], {fillColor: '#e2e8f0', fillOpacity: 0.5, borders: {strokeColor: '#1e293b', strokeWidth: 3}});
    
    // Ángulo recto
    board.create('angle', [B, A, C], {radius: 0.4, orthoType: 'square', orthoSensitivity: 1, fillColor: '#ef4444', strokeColor: '#ef4444'});
    
    // Cuadrado sobre cateto a (vertical, lado = 3)
    board.create('polygon', [[0, 0], [-3, 0], [-3, 3], [0, 3]], {fillColor: '#22c55e', fillOpacity: 0.3, borders: {strokeColor: '#22c55e', strokeWidth: 2}});
    board.create('text', [-1.5, 1.5, 'a² = 9'], {fontSize: 12, color: '#166534', fixed: true, anchorX: 'middle'});
    
    // Cuadrado sobre cateto b (horizontal, lado = 4)
    board.create('polygon', [[0, 0], [0, -4], [4, -4], [4, 0]], {fillColor: '#3b82f6', fillOpacity: 0.3, borders: {strokeColor: '#3b82f6', strokeWidth: 2}});
    board.create('text', [2, -2, 'b² = 16'], {fontSize: 12, color: '#1e40af', fixed: true, anchorX: 'middle'});
    
    // Cuadrado sobre hipotenusa c (diagonal, lado = 5)
    board.create('polygon', [[4, 0], [7.2, 2.4], [4.2, 5.4], [1, 3]], {fillColor: '#f59e0b', fillOpacity: 0.3, borders: {strokeColor: '#f59e0b', strokeWidth: 2}});
    board.create('text', [5.5, 3], 'c² = 25'], {fontSize: 12, color: '#b45309', fixed: true, anchorX: 'middle'});
    
    // Etiquetas de lados
    board.create('text', [-0.5, 1.5, 'a=3'], {fontSize: 11, color: '#22c55e', fixed: true});
    board.create('text', [2, 0.3, 'b=4'], {fontSize: 11, color: '#3b82f6', fixed: true});
    board.create('text', [2.5, 2, 'c=5'], {fontSize: 11, color: '#f59e0b', fixed: true});
    
    // Fórmula
    board.create('text', [8, -2.5, 'a² + b² = c²'], {fontSize: 14, color: '#1e293b', fixed: true});
    board.create('text', [8, -3.3, '9 + 16 = 25 ✓'], {fontSize: 12, color: '#22c55e', fixed: true});
  }
});
</script>

> 💡 **Visual:** El área del cuadrado sobre la hipotenusa (amarillo, 25) es igual a la suma de las áreas de los cuadrados sobre los catetos (verde 9 + azul 16).

---

## 📖 Fórmulas derivadas

### Calcular la hipotenusa

$$
c = \sqrt{a^2 + b^2}
$$

### Calcular un cateto

$$
a = \sqrt{c^2 - b^2}
$$

$$
b = \sqrt{c^2 - a^2}
$$

---

## 📖 Ejemplo 1: Encontrar la hipotenusa

Un triángulo rectángulo tiene catetos de 3 cm y 4 cm. ¿Cuánto mide la hipotenusa?

**Solución:**

$$
c^2 = 3^2 + 4^2 = 9 + 16 = 25
$$

$$
c = \sqrt{25} = 5 \text{ cm}
$$

---

## 📖 Ejemplo 2: Encontrar un cateto

Un triángulo rectángulo tiene hipotenusa de 13 cm y un cateto de 5 cm. ¿Cuánto mide el otro cateto?

**Solución:**

$$
a^2 = c^2 - b^2 = 13^2 - 5^2 = 169 - 25 = 144
$$

$$
a = \sqrt{144} = 12 \text{ cm}
$$

---

## 📖 Ternas pitagóricas

Una **terna pitagórica** es un conjunto de tres números enteros que satisfacen el Teorema de Pitágoras.

### Ternas más conocidas

| Terna | Verificación |
|-------|--------------|
| (3, 4, 5) | $9 + 16 = 25$ |
| (5, 12, 13) | $25 + 144 = 169$ |
| (8, 15, 17) | $64 + 225 = 289$ |
| (7, 24, 25) | $49 + 576 = 625$ |

### Propiedad

Si $(a, b, c)$ es una terna pitagórica, entonces $(ka, kb, kc)$ también lo es para cualquier $k$ entero.

### Ejemplo

$(3, 4, 5) \times 2 = (6, 8, 10)$ también es una terna pitagórica:

$$
6^2 + 8^2 = 36 + 64 = 100 = 10^2 \quad ✓
$$

---

## 📖 Aplicaciones prácticas

### Ejemplo 1: Escalera apoyada en pared

Una escalera de 5 m está apoyada en una pared. Su base está a 3 m de la pared. ¿A qué altura llega la escalera?

$$
h^2 = 5^2 - 3^2 = 25 - 9 = 16
$$

$$
h = 4 \text{ m}
$$

### Ejemplo 2: Diagonal de un rectángulo

Un rectángulo mide 6 m de largo y 8 m de ancho. ¿Cuánto mide su diagonal?

$$
d = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10 \text{ m}
$$

### Ejemplo 3: Distancia entre dos puntos

La distancia entre los puntos $(1, 2)$ y $(4, 6)$ se calcula con Pitágoras:

$$
d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

---

## 📖 El recíproco

El teorema también funciona al revés:

> Si en un triángulo se cumple que $c^2 = a^2 + b^2$, entonces el triángulo es rectángulo.

### Ejemplo

Un triángulo tiene lados 6, 8 y 10. ¿Es rectángulo?

$$
6^2 + 8^2 = 36 + 64 = 100 = 10^2 \quad ✓
$$

Sí, es un triángulo rectángulo.

---

## 📖 Clasificación por la relación pitagórica

| Condición | Tipo de triángulo |
|-----------|-------------------|
| $c^2 = a^2 + b^2$ | Rectángulo |
| $c^2 < a^2 + b^2$ | Acutángulo |
| $c^2 > a^2 + b^2$ | Obtusángulo |

### Ejemplo

Triángulo con lados 4, 5, 6:
- Mayor lado: 6
- $6^2 = 36$
- $4^2 + 5^2 = 16 + 25 = 41$
- $36 < 41$, entonces es **acutángulo**

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular hipotenusa

Encuentra la hipotenusa de triángulos con estos catetos:

1. $a = 6$, $b = 8$
2. $a = 5$, $b = 12$
3. $a = 8$, $b = 15$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $c = \sqrt{36 + 64} = \sqrt{100} = 10$
2. $c = \sqrt{25 + 144} = \sqrt{169} = 13$
3. $c = \sqrt{64 + 225} = \sqrt{289} = 17$

</details>

---

### Ejercicio 2: Calcular cateto

Encuentra el cateto faltante:

1. $c = 10$, $b = 6$, $a = ?$
2. $c = 25$, $a = 7$, $b = ?$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $a = \sqrt{100 - 36} = \sqrt{64} = 8$
2. $b = \sqrt{625 - 49} = \sqrt{576} = 24$

</details>

---

### Ejercicio 3: ¿Es triángulo rectángulo?

Determina si estos triángulos son rectángulos:

1. Lados: 9, 12, 15
2. Lados: 5, 7, 9
3. Lados: 20, 21, 29

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $15^2 = 225$, $9^2 + 12^2 = 81 + 144 = 225$ → **Sí es rectángulo**
2. $9^2 = 81$, $5^2 + 7^2 = 25 + 49 = 74$ → $81 \neq 74$, **No es rectángulo**
3. $29^2 = 841$, $20^2 + 21^2 = 400 + 441 = 841$ → **Sí es rectángulo**

</details>

---

### Ejercicio 4: Problema aplicado

Un campo de fútbol mide 100 m de largo y 64 m de ancho. Un jugador quiere correr en diagonal de una esquina a la opuesta. ¿Qué distancia recorrerá?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
d = \sqrt{100^2 + 64^2} = \sqrt{10000 + 4096} = \sqrt{14096} \approx 118.7 \text{ m}
$$

</details>

---
