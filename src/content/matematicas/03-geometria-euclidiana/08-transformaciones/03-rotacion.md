# Rotación

La **rotación** es el movimiento circular alrededor de un punto fijo. Es como girar una figura sobre un eje.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-rotacion-1" width="700" height="350" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-rotacion-1')) {
    var canvas = document.getElementById('roughjs-rotacion-1');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Rotación de 90° (antihorario)', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    
    // Centro de rotación (más visible y central)
    var cx = 300, cy = 180;
    
    // Centro de rotación - MÁS GRANDE Y VISIBLE
    rc.circle(cx, cy, 16, {fill: rojo, stroke: rojo, roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#fff';
    ctx.textAlign = 'center';
    ctx.fillText('O', cx, cy+5);
    
    // Triángulo ORIGINAL (azul) - CERCA del centro, tocando casi el centro
    // Un vértice cerca del centro para mostrar claramente la rotación
    var A = [cx+40, cy+10];
    var B = [cx+100, cy+10];
    var C = [cx+70, cy-50];
    rc.polygon([A, B, C], {fill: '#dbeafe', stroke: azul, strokeWidth: 2.5, roughness: 0.5});
    
    // Etiquetas originales
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = azul;
    ctx.textAlign = 'center';
    ctx.fillText('A', A[0], A[1]+18);
    ctx.fillText('B', B[0]+12, B[1]+5);
    ctx.fillText('C', C[0]+12, C[1]-5);
    
    // Rotación 90° antihorario alrededor de O
    // En SVG (Y hacia abajo): antihorario visual = (dx,dy) -> (dy, -dx)
    function rotar90(p) {
      var dx = p[0] - cx;
      var dy = p[1] - cy;
      return [cx + dy, cy - dx];
    }
    var Ap = rotar90(A);
    var Bp = rotar90(B);
    var Cp = rotar90(C);
    rc.polygon([Ap, Bp, Cp], {fill: '#dcfce7', stroke: verde, strokeWidth: 2.5, roughness: 0.5});
    
    // Etiquetas imagen
    ctx.fillStyle = verde;
    ctx.fillText("A'", Ap[0]+5, Ap[1]-10);
    ctx.fillText("B'", Bp[0]+5, Bp[1]-10);
    ctx.fillText("C'", Cp[0]-15, Cp[1]+5);
    
    // Líneas radiales desde O a los vértices (para mostrar que giran alrededor de O)
    rc.line(cx, cy, A[0], A[1], {stroke: '#94a3b8', strokeWidth: 1, roughness: 0.2});
    rc.line(cx, cy, Ap[0], Ap[1], {stroke: '#94a3b8', strokeWidth: 1, roughness: 0.2});
    
    // Arco de rotación desde A hasta A'
    var radioA = Math.sqrt(Math.pow(A[0]-cx, 2) + Math.pow(A[1]-cy, 2));
    var anguloA = Math.atan2(A[1]-cy, A[0]-cx);
    var anguloAp = Math.atan2(Ap[1]-cy, Ap[0]-cx);
    rc.arc(cx, cy, radioA*2, radioA*2, anguloAp, anguloA, false, {stroke: rojo, strokeWidth: 2.5, roughness: 0.3});
    
    // Flecha en el arco
    ctx.fillStyle = rojo;
    ctx.beginPath();
    ctx.moveTo(Ap[0]-5, Ap[1]+5);
    ctx.lineTo(Ap[0]+5, Ap[1]);
    ctx.lineTo(Ap[0]-2, Ap[1]-8);
    ctx.fill();
    
    // Etiqueta del ángulo
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = rojo;
    ctx.textAlign = 'center';
    ctx.fillText('90°', cx+60, cy-70);
    
    // Nota explicativa
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.textAlign = 'center';
    ctx.fillText('Cada punto gira 90° alrededor de O', 350, 280);
    ctx.fillText('manteniendo la misma distancia al centro', 350, 296);
    
    // Leyenda
    rc.rectangle(450, 120, 180, 90, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = '12px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = azul;
    ctx.fillText('■ Original', 470, 145);
    ctx.fillStyle = verde;
    ctx.fillText('■ Imagen', 470, 165);
    ctx.fillStyle = rojo;
    ctx.fillText('● Centro O', 470, 185);
    ctx.fillStyle = '#64748b';
    ctx.fillText('↺ Arco 90°', 470, 200);
  }
});
</script>

---

## 📖 Definición

> **Definición:** Una rotación gira todos los puntos de una figura alrededor de un punto fijo llamado **centro**, a través de un **ángulo** determinado.

### Elementos de la rotación

| Elemento | Descripción |
|----------|-------------|
| Centro | Punto fijo alrededor del cual se gira |
| Ángulo | Cantidad de giro (en grados) |
| Sentido | Antihorario (+) o horario (−) |

---

## 📖 Notación

$$
R_{O,\theta}
$$

- $O$ = centro de rotación
- $\theta$ = ángulo de rotación

### Convención de signos

- $\theta > 0$: sentido **antihorario** (contrario a las agujas del reloj)
- $\theta < 0$: sentido **horario** (en el sentido de las agujas del reloj)

---

## 📖 Fórmula de rotación

Para rotar el punto $P(x, y)$ alrededor del **origen** un ángulo $\theta$:

$$
x' = x \cos\theta - y \sin\theta
$$

$$
y' = x \sin\theta + y \cos\theta
$$

### En forma matricial

$$
\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}
$$

---

## 📖 Rotaciones especiales (centro en origen)

### Rotación de 90° (antihorario)

$$
P(x, y) \to P'(-y, x)
$$

### Rotación de 180°

$$
P(x, y) \to P'(-x, -y)
$$

### Rotación de 270° (o −90°)

$$
P(x, y) \to P'(y, -x)
$$

### Rotación de 360°

$$
P(x, y) \to P(x, y)
$$

(Vuelve a la posición original)

---

## 📖 Ejemplos

### Ejemplo 1: Rotación de 90°

Rotar $P(3, 2)$ un ángulo de 90° alrededor del origen:

$$
P' = (-2, 3)
$$

### Ejemplo 2: Rotación de 180°

Rotar $P(4, -1)$ un ángulo de 180° alrededor del origen:

$$
P' = (-4, 1)
$$

---

## 📖 Propiedades de la rotación

| Propiedad | ¿Se conserva? |
|-----------|---------------|
| Distancias | Sí |
| Ángulos | Sí |
| Área | Sí |
| Forma | Sí |
| Orientación | Sí |

### La rotación es una isometría

Conserva todas las distancias y ángulos.

### Punto fijo

Solo el **centro** de rotación queda fijo (excepto si $\theta = 0°$ o múltiplo de 360°).

---

## 📖 Rotación con centro fuera del origen

Si el centro es $C(h, k)$:

1. Trasladar para que $C$ quede en el origen
2. Rotar
3. Trasladar de vuelta

$$
x' = (x - h)\cos\theta - (y - k)\sin\theta + h
$$

$$
y' = (x - h)\sin\theta + (y - k)\cos\theta + k
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Rotaciones especiales

Aplica cada rotación al punto $P(4, 1)$ alrededor del origen:

1. Rotación de 90°
2. Rotación de 180°
3. Rotación de 270°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $P' = (-1, 4)$
2. $P' = (-4, -1)$
3. $P' = (1, -4)$

</details>

---

### Ejercicio 2: Rotación de 180°

Rota el punto $Q(-2, 5)$ un ángulo de 180° alrededor del origen.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
Q' = (2, -5)
$$

</details>

---

### Ejercicio 3: Identificar la rotación

El punto $A(3, 0)$ se transforma en $A'(0, 3)$. ¿Cuál fue el ángulo de rotación?

<details>
<summary><strong>Ver respuesta</strong></summary>

Era $(3, 0) \to (0, 3)$, que corresponde a una **rotación de 90°** antihorario.

</details>

---

### Ejercicio 4: Triángulo

Rota el triángulo con vértices $A(1, 0)$, $B(3, 0)$, $C(2, 2)$ un ángulo de 180° alrededor del origen.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A' = (-1, 0)
$$

$$
B' = (-3, 0)
$$

$$
C' = (-2, -2)
$$

</details>

---

### Ejercicio 5: Verdadero o Falso

1. En una rotación de 360°, todos los puntos son fijos.
2. El centro de rotación es el único punto fijo en una rotación no nula.
3. Una rotación de −90° es igual a una rotación de 270°.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero**
2. **Verdadero**
3. **Verdadero** (ambas dan el mismo resultado)

</details>

---
