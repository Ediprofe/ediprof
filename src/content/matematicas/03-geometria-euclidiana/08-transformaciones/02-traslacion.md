# Traslación

La **traslación** es el movimiento más simple: desplazar una figura una cierta distancia en una dirección determinada.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-traslacion-1" width="700" height="320" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-traslacion-1')) {
    var canvas = document.getElementById('roughjs-traslacion-1');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Traslación de un Triángulo', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    
    // Ejes coordenados
    rc.line(50, 250, 650, 250, {stroke: '#cbd5e1', strokeWidth: 1, roughness: 0.2});
    rc.line(100, 50, 100, 280, {stroke: '#cbd5e1', strokeWidth: 1, roughness: 0.2});
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.textAlign = 'center';
    ctx.fillText('x', 640, 265);
    ctx.fillText('y', 90, 60);
    
    // Triángulo ORIGINAL (azul)
    var A = [150, 200];
    var B = [250, 200];
    var C = [200, 120];
    rc.polygon([A, B, C], {fill: '#dbeafe', stroke: azul, strokeWidth: 2.5, roughness: 0.5});
    
    // Etiquetas originales
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = azul;
    ctx.fillText('A', A[0]-12, A[1]+15);
    ctx.fillText('B', B[0]+10, B[1]+15);
    ctx.fillText('C', C[0], C[1]-10);
    
    // Vector de traslación v = (200, -50)
    var vx = 200, vy = -50;
    
    // Triángulo IMAGEN (verde)
    var Ap = [A[0]+vx, A[1]+vy];
    var Bp = [B[0]+vx, B[1]+vy];
    var Cp = [C[0]+vx, C[1]+vy];
    rc.polygon([Ap, Bp, Cp], {fill: '#dcfce7', stroke: verde, strokeWidth: 2.5, roughness: 0.5});
    
    // Etiquetas imagen
    ctx.fillStyle = verde;
    ctx.fillText("A'", Ap[0]-12, Ap[1]+15);
    ctx.fillText("B'", Bp[0]+10, Bp[1]+15);
    ctx.fillText("C'", Cp[0], Cp[1]-10);
    
    // Vectores de traslación (flechas)
    rc.line(A[0], A[1], Ap[0], Ap[1], {stroke: '#f59e0b', strokeWidth: 2, roughness: 0.3});
    rc.line(B[0], B[1], Bp[0], Bp[1], {stroke: '#f59e0b', strokeWidth: 2, roughness: 0.3});
    rc.line(C[0], C[1], Cp[0], Cp[1], {stroke: '#f59e0b', strokeWidth: 2, roughness: 0.3});
    
    // Puntas de flecha (simples)
    ctx.fillStyle = '#f59e0b';
    ctx.beginPath();
    ctx.moveTo(Ap[0], Ap[1]);
    ctx.lineTo(Ap[0]-10, Ap[1]-5);
    ctx.lineTo(Ap[0]-10, Ap[1]+5);
    ctx.fill();
    
    // Etiqueta del vector
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.textAlign = 'center';
    ctx.fillText('v⃗ = (a, b)', 300, 100);
    
    // Leyenda
    rc.rectangle(180, 270, 340, 40, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = '12px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = azul;
    ctx.fillText('■ Original', 200, 295);
    ctx.fillStyle = verde;
    ctx.fillText('■ Imagen', 300, 295);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('→ Vector v⃗', 400, 295);
  }
});
</script>

---

## 📖 Definición

> **Definición:** Una traslación mueve todos los puntos de una figura la **misma distancia** y en la **misma dirección**.

### Vector de traslación

La traslación se define mediante un **vector** $\vec{v}$:

$$
\vec{v} = (a, b)
$$

- $a$ = desplazamiento horizontal
- $b$ = desplazamiento vertical

---

## 📖 Fórmula de traslación

Si el punto $P(x, y)$ se traslada con vector $\vec{v} = (a, b)$, la imagen es:

$$
P'(x', y') = (x + a, y + b)
$$

### Ejemplo 1

Trasladar $P(3, 5)$ con vector $\vec{v} = (4, -2)$:

$$
P' = (3 + 4, 5 + (-2)) = (7, 3)
$$

### Ejemplo 2

Trasladar $Q(-1, 2)$ con vector $\vec{v} = (5, 3)$:

$$
Q' = (-1 + 5, 2 + 3) = (4, 5)
$$

---

## 📖 Propiedades de la traslación

| Propiedad | ¿Se conserva? |
|-----------|---------------|
| Distancias | Sí |
| Ángulos | Sí |
| Paralelismo | Sí |
| Orientación | Sí |
| Área | Sí |

### La traslación es una isometría

Todas las distancias y ángulos se conservan.

### No hay puntos fijos

Ningún punto queda en su lugar (excepto si $\vec{v} = (0, 0)$).

### Los segmentos son paralelos

Si $\overline{AB}$ se traslada a $\overline{A'B'}$:
- $AA' \parallel BB'$
- $AA' = BB' = |\vec{v}|$
- $AB = A'B'$

---

## 📖 Traslación de figuras

Para trasladar una figura, trasladamos **cada vértice** con el mismo vector.

### Ejemplo

Trasladar el triángulo $ABC$ con vértices $A(1, 2)$, $B(4, 2)$, $C(2, 5)$ usando $\vec{v} = (3, -1)$:

$$
A' = (1 + 3, 2 - 1) = (4, 1)
$$

$$
B' = (4 + 3, 2 - 1) = (7, 1)
$$

$$
C' = (2 + 3, 5 - 1) = (5, 4)
$$

El triángulo $A'B'C'$ es la imagen.

---

## 📖 Composición de traslaciones

Dos traslaciones consecutivas equivalen a una sola traslación cuyo vector es la **suma de los vectores**:

$$
\vec{v}_1 + \vec{v}_2 = \vec{v}_{total}
$$

### Ejemplo

Si $\vec{v}_1 = (3, 2)$ y $\vec{v}_2 = (1, 5)$:

$$
\vec{v}_{total} = (3 + 1, 2 + 5) = (4, 7)
$$

---

## 📖 Traslación inversa

La traslación inversa tiene el **vector opuesto**:

$$
\vec{v}^{-1} = -\vec{v} = (-a, -b)
$$

Aplicar la traslación y luego su inversa devuelve el punto original.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Aplicar traslación

Traslada los puntos con el vector dado:

1. $P(2, 3)$ con $\vec{v} = (4, 5)$
2. $Q(-1, 4)$ con $\vec{v} = (3, -2)$
3. $R(0, 0)$ con $\vec{v} = (-2, 6)$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $P' = (2 + 4, 3 + 5) = (6, 8)$
2. $Q' = (-1 + 3, 4 - 2) = (2, 2)$
3. $R' = (0 - 2, 0 + 6) = (-2, 6)$

</details>

---

### Ejercicio 2: Encontrar el vector

¿Qué vector traslada $A(1, 2)$ a $A'(5, 7)$?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\vec{v} = (5 - 1, 7 - 2) = (4, 5)
$$

</details>

---

### Ejercicio 3: Trasladar un triángulo

Triángulo con vértices $A(0, 0)$, $B(4, 0)$, $C(2, 3)$. Traslada con $\vec{v} = (-1, 2)$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A' = (-1, 2)
$$

$$
B' = (3, 2)
$$

$$
C' = (1, 5)
$$

</details>

---

### Ejercicio 4: Composición

Se aplican dos traslaciones: $\vec{v}_1 = (2, -3)$ y $\vec{v}_2 = (-5, 1)$. ¿Cuál es el vector resultante?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\vec{v}_{total} = (2 - 5, -3 + 1) = (-3, -2)
$$

</details>

---

### Ejercicio 5: Traslación inversa

Si $\vec{v} = (7, -4)$, ¿cuál es el vector de la traslación inversa?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\vec{v}^{-1} = (-7, 4)
$$

</details>

---
