# Clasificación de Ángulos por su Medida

Los ángulos se clasifican según su **amplitud** o **medida**. Esta clasificación es fundamental para identificar y describir ángulos en cualquier contexto geométrico.

---

## 📖 Clasificación principal

Existen seis tipos principales de ángulos según su medida:

| Tipo | Medida | Descripción |
|------|--------|-------------|
| Nulo | $0°$ | Sin abertura |
| Agudo | $0° < \alpha < 90°$ | Menor que un recto |
| Recto | $90°$ | Exactamente un cuarto de vuelta |
| Obtuso | $90° < \alpha < 180°$ | Mayor que recto, menor que llano |
| Llano | $180°$ | Exactamente media vuelta |
| Cóncavo | $180° < \alpha < 360°$ | Mayor que llano (también llamado reflejo) |
| Perigonal | $360°$ | Vuelta completa |

---

## 📖 Ángulo Nulo (0°)

Un **ángulo nulo** tiene medida de $0°$. Sus dos lados están superpuestos.

> Es como si el ángulo no existiera porque no hay abertura.

### Ejemplo

Las manecillas del reloj a las **12:00** forman un ángulo nulo.

---

## 📖 Ángulo Agudo

Un **ángulo agudo** mide más de $0°$ y menos de $90°$.

$$
0° < \alpha < 90°
$$

### Características

- Es "puntiagudo" o "afilado"
- Es menor que un ángulo recto

### Ejemplos en la vida real

| Ejemplo | Ángulo aproximado |
|---------|-------------------|
| La punta de una flecha | 30° - 45° |
| La pendiente de un techo | 25° - 35° |
| Tijeras poco abiertas | 20° - 40° |
| Un trozo de pizza | Aproximadamente 45° |

### Ejemplo numérico

Los ángulos de $15°$, $30°$, $45°$, $60°$, $75°$, $89°$ son todos **agudos**.

---

## 📖 Ángulo Recto (90°)

Un **ángulo recto** mide exactamente $90°$ (un cuarto de vuelta).

$$
\alpha = 90°
$$

### Símbolo especial

Se representa con un pequeño cuadrado en el vértice: ⌐

### Características

- Sus lados son **perpendiculares**
- Es la base de la perpendicularidad
- Divide el plano en cuatro partes iguales

### Ejemplos en la vida real

| Ejemplo |
|---------|
| Las esquinas de una habitación |
| Los ángulos de una hoja de papel |
| El cruce de calles perpendiculares |
| La letra "L" mayúscula |
| Las manecillas del reloj a las 3:00 |

---

## 📖 Ángulo Obtuso

Un **ángulo obtuso** mide más de $90°$ y menos de $180°$.

$$
90° < \alpha < 180°
$$

### Características

- Es "abierto" o "ancho"
- Es mayor que un ángulo recto pero menor que un llano

### Ejemplos en la vida real

| Ejemplo | Ángulo aproximado |
|---------|-------------------|
| Un libro abierto más de 90° | 120° |
| Una silla reclinada | 100° - 110° |
| Las manecillas a las 4:30 | Aproximadamente 135° |

### Ejemplo numérico

Los ángulos de $91°$, $100°$, $120°$, $135°$, $150°$, $179°$ son todos **obtusos**.

---

## 📖 Ángulo Llano (180°)

Un **ángulo llano** (o **plano**) mide exactamente $180°$ (media vuelta).

$$
\alpha = 180°
$$

### Características

- Sus lados forman una **línea recta**
- Divide el plano en dos semiplanos

### Ejemplos en la vida real

| Ejemplo |
|---------|
| Las manecillas del reloj a las 6:00 |
| Un abanico completamente abierto |
| El borde recto de una regla |

---

## 📖 Ángulo Cóncavo (Reflejo)

Un **ángulo cóncavo** (o **reflejo**) mide más de $180°$ y menos de $360°$.

$$
180° < \alpha < 360°
$$

### Características

- Es la parte "grande" de un ángulo
- También se llama **ángulo reflejo** o **cóncavo**
- Es el complemento de un ángulo convexo hasta 360°

### Ejemplo

Si abres un compás más de media vuelta, el ángulo interior es cóncavo.

### Relación con ángulos convexos

Si un ángulo convexo mide $\theta$, su ángulo cóncavo correspondiente mide:

$$
\text{Ángulo cóncavo} = 360° - \theta
$$

### Ejemplo numérico

Si el ángulo convexo es de $60°$, el ángulo cóncavo es:

$$
360° - 60° = 300°
$$

---

## 📖 Ángulo Perigonal (360°)

Un **ángulo perigonal** (o **completo**) mide exactamente $360°$ (vuelta completa).

$$
\alpha = 360°
$$

### Características

- Es una **vuelta completa** alrededor del vértice
- Los dos lados vuelven a coincidir

### Ejemplo

Una rueda que da una vuelta completa gira $360°$.

---

## 📖 Resumen Visual

| Ángulo | Rango | Representación |
|--------|-------|----------------|
| Nulo | $0°$ | Lados superpuestos |
| Agudo | $0° - 90°$ | Puntiagudo |
| Recto | $90°$ | Con cuadradito |
| Obtuso | $90° - 180°$ | Abierto |
| Llano | $180°$ | Línea recta |
| Cóncavo | $180° - 360°$ | Más de media vuelta |
| Perigonal | $360°$ | Vuelta completa |

**Ángulos: nulo ($0°$), agudo ($0° < \alpha < 90°$), recto ($90°$), obtuso ($90° < \alpha < 180°$), llano ($180°$):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-tipos-angulos" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-tipos-angulos')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-tipos-angulos', {
      boundingbox: [-1, 10, 15, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    board.create('text', [7, 9.3, 'Clasificación de Ángulos por su Medida'], {fontSize: 14, fontWeight: 'bold', color: '#1e293b', anchorX: 'middle'});
    
    // Función para crear un ángulo con etiqueta
    function crearAngulo(cx, cy, angGrados, nombre, color) {
      var rad = angGrados * Math.PI / 180;
      var r = 1.2;
      
      // Lados del ángulo
      var p1 = board.create('point', [cx + r, cy], {visible: false, fixed: true});
      var p2 = board.create('point', [cx + r * Math.cos(rad), cy + r * Math.sin(rad)], {visible: false, fixed: true});
      var v = board.create('point', [cx, cy], {name: '', size: 4, fixed: true, color: color});
      
      board.create('segment', [v, p1], {strokeColor: color, strokeWidth: 2});
      board.create('segment', [v, p2], {strokeColor: color, strokeWidth: 2});
      
      // Arco
      if (angGrados > 0 && angGrados < 360) {
        board.create('arc', [v, p1, p2], {strokeColor: color, strokeWidth: 2});
      }
      
      // Etiquetas
      board.create('text', [cx, cy - 1.5, nombre + ' (' + angGrados + '°)'], {fontSize: 10, color: color, anchorX: 'middle'});
    }
    
    // FILA 1: Nulo, Agudo, Recto
    crearAngulo(2, 6.5, 0, 'NULO', '#94a3b8');
    crearAngulo(6, 6.5, 45, 'AGUDO', '#22c55e');
    crearAngulo(10, 6.5, 90, 'RECTO', '#3b82f6');
    
    // Cuadradito para ángulo recto
    board.create('polygon', [[10.3, 6.5], [10.3, 6.8], [10, 6.8]], {
      fillColor: 'transparent',
      borders: {strokeColor: '#3b82f6', strokeWidth: 1}
    });
    
    // FILA 2: Obtuso, Llano
    crearAngulo(4, 2.5, 135, 'OBTUSO', '#f59e0b');
    crearAngulo(9, 2.5, 180, 'LLANO', '#ef4444');
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificar ángulos

Clasifica cada ángulo según su medida:

| Ángulo | Clasificación |
|--------|---------------|
| 45° | |
| 90° | |
| 135° | |
| 180° | |
| 270° | |
| 360° | |
| 15° | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Ángulo | Clasificación |
|--------|---------------|
| 45° | Agudo |
| 90° | Recto |
| 135° | Obtuso |
| 180° | Llano |
| 270° | Cóncavo |
| 360° | Perigonal |
| 15° | Agudo |

</details>

---

### Ejercicio 2: Identificar en el reloj

¿Qué tipo de ángulo forman las manecillas del reloj a cada hora?

| Hora | Tipo de ángulo |
|------|----------------|
| 3:00 | |
| 6:00 | |
| 12:00 | |
| 4:00 | |
| 10:30 | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Hora | Tipo de ángulo |
|------|----------------|
| 3:00 | Recto (90°) |
| 6:00 | Llano (180°) |
| 12:00 | Nulo (0°) |
| 4:00 | Obtuso (≈120°) |
| 10:30 | Obtuso (≈135°) |

</details>

---

### Ejercicio 3: Calcular el ángulo cóncavo

Si el ángulo convexo mide lo indicado, ¿cuánto mide su ángulo cóncavo correspondiente?

1. Convexo = 30°
2. Convexo = 90°
3. Convexo = 150°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Cóncavo = $360° - 30° = 330°$
2. Cóncavo = $360° - 90° = 270°$
3. Cóncavo = $360° - 150° = 210°$

</details>

---
