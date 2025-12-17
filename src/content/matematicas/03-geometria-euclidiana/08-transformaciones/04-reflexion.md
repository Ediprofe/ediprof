# Reflexión (Simetría Axial)

La **reflexión** produce la imagen espejo de una figura respecto a una recta llamada eje de simetría.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-reflexion-1" width="700" height="320" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-reflexion-1')) {
    var canvas = document.getElementById('roughjs-reflexion-1');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Reflexión respecto al Eje Y', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var morado = '#a855f7';
    
    // Centro de coordenadas
    var cx = 350, cy = 170;
    
    // Ejes coordenados
    rc.line(100, cy, 600, cy, {stroke: '#e2e8f0', strokeWidth: 1, roughness: 0.2});
    rc.line(cx, 50, cx, 280, {stroke: morado, strokeWidth: 3, roughness: 0.3}); // Eje Y como eje de reflexión
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('x', 590, cy+15);
    ctx.fillStyle = morado;
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('Eje Y', cx+20, 60);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('O', cx-12, cy+15);
    
    // Triángulo ORIGINAL (azul) - a la derecha del eje
    var A = [cx+60, cy+40];
    var B = [cx+140, cy+40];
    var C = [cx+100, cy-40];
    rc.polygon([A, B, C], {fill: '#dbeafe', stroke: azul, strokeWidth: 2.5, roughness: 0.5});
    
    // Etiquetas originales
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = azul;
    ctx.fillText('A', A[0]-5, A[1]+15);
    ctx.fillText('B', B[0]+8, B[1]+15);
    ctx.fillText('C', C[0]+10, C[1]);
    
    // Triángulo IMAGEN (verde) - reflejado respecto al eje Y
    // Reflexión eje Y: (x,y) -> (-x, y) respecto al centro
    function reflejarY(p) {
      var dx = p[0] - cx;
      return [cx - dx, p[1]];
    }
    var Ap = reflejarY(A);
    var Bp = reflejarY(B);
    var Cp = reflejarY(C);
    rc.polygon([Ap, Bp, Cp], {fill: '#dcfce7', stroke: verde, strokeWidth: 2.5, roughness: 0.5});
    
    // Etiquetas imagen
    ctx.fillStyle = verde;
    ctx.fillText("A'", Ap[0], Ap[1]+15);
    ctx.fillText("B'", Bp[0]-18, Bp[1]+15);
    ctx.fillText("C'", Cp[0]-18, Cp[1]);
    
    // Líneas de correspondencia (punteadas)
    rc.line(A[0], A[1], Ap[0], Ap[1], {stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.2});
    rc.line(B[0], B[1], Bp[0], Bp[1], {stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.2});
    rc.line(C[0], C[1], Cp[0], Cp[1], {stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.2});
    
    // Leyenda
    rc.rectangle(180, 270, 340, 40, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = '12px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = azul;
    ctx.fillText('■ Original', 200, 295);
    ctx.fillStyle = verde;
    ctx.fillText('■ Imagen', 300, 295);
    ctx.fillStyle = morado;
    ctx.fillText('│ Eje de reflexión', 400, 295);
  }
});
</script>

---

## 📖 Definición

> **Definición:** Una reflexión transforma cada punto $P$ en su imagen $P'$ tal que el **eje de simetría** es la **mediatriz** del segmento $\overline{PP'}$.

### Propiedades del punto y su imagen

- $P$ y $P'$ están a la **misma distancia** del eje
- El segmento $\overline{PP'}$ es **perpendicular** al eje
- El eje pasa por el **punto medio** de $\overline{PP'}$

---

## 📖 Tipos de reflexión según el eje

### Reflexión respecto al eje X

$$
P(x, y) \to P'(x, -y)
$$

La coordenada $y$ cambia de signo.

### Reflexión respecto al eje Y

$$
P(x, y) \to P'(-x, y)
$$

La coordenada $x$ cambia de signo.

### Reflexión respecto al origen

$$
P(x, y) \to P'(-x, -y)
$$

Ambas coordenadas cambian de signo. (Equivale a rotación de 180°)

### Reflexión respecto a la recta y = x

$$
P(x, y) \to P'(y, x)
$$

Se intercambian las coordenadas.

---

## 📖 Ejemplos

### Ejemplo 1: Reflexión respecto al eje X

Reflejar $P(3, 5)$ respecto al eje X:

$$
P' = (3, -5)
$$

### Ejemplo 2: Reflexión respecto al eje Y

Reflejar $Q(-2, 4)$ respecto al eje Y:

$$
Q' = (2, 4)
$$

### Ejemplo 3: Reflexión respecto a y = x

Reflejar $R(1, 7)$ respecto a la recta $y = x$:

$$
R' = (7, 1)
$$

---

## 📖 Propiedades de la reflexión

| Propiedad | ¿Se conserva? |
|-----------|---------------|
| Distancias | Sí |
| Ángulos | Sí |
| Área | Sí |
| Forma | Sí |
| Orientación | **No** (se invierte) |

### La reflexión es una isometría

Conserva distancias y ángulos, pero **invierte la orientación** (como en un espejo).

### Puntos fijos

Todos los puntos **sobre el eje** son fijos.

---

## 📖 Reflexión respecto a una recta general

Para reflejar respecto a una recta $y = mx + b$:

1. Encontrar la perpendicular desde $P$ hasta la recta
2. Encontrar el punto de intersección $M$
3. $P'$ está a la misma distancia de $M$ que $P$, pero al otro lado

---

## 📖 Composición de reflexiones

### Dos reflexiones sobre ejes paralelos

Equivalen a una **traslación**.

### Dos reflexiones sobre ejes que se cortan

Equivalen a una **rotación** con ángulo igual al doble del ángulo entre los ejes.

---

## 📖 Figuras con simetría axial

Una figura tiene **simetría axial** si existe una recta (eje) que la divide en dos partes que son imagen espejo.

### Ejemplos

| Figura | Ejes de simetría |
|--------|-----------------|
| Cuadrado | 4 |
| Rectángulo | 2 |
| Triángulo equilátero | 3 |
| Triángulo isósceles | 1 |
| Círculo | Infinitos |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Reflexión respecto a ejes

Encuentra la imagen de $P(4, -3)$:

1. Reflexión respecto al eje X
2. Reflexión respecto al eje Y
3. Reflexión respecto al origen

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $P' = (4, 3)$
2. $P' = (-4, -3)$
3. $P' = (-4, 3)$

</details>

---

### Ejercicio 2: Reflexión respecto a y = x

Reflejar los puntos respecto a la recta $y = x$:

1. $A(2, 5)$
2. $B(-1, 3)$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A' = (5, 2)$
2. $B' = (3, -1)$

</details>

---

### Ejercicio 3: Identificar el eje

El punto $A(3, 7)$ se refleja en $A'(3, -7)$. ¿Cuál es el eje de reflexión?

<details>
<summary><strong>Ver respuesta</strong></summary>

Solo la coordenada $y$ cambió de signo, entonces el eje es el **eje X**.

</details>

---

### Ejercicio 4: Triángulo

Refleja el triángulo con vértices $A(1, 2)$, $B(4, 2)$, $C(2, 5)$ respecto al eje Y.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A' = (-1, 2)
$$

$$
B' = (-4, 2)
$$

$$
C' = (-2, 5)
$$

</details>

---

### Ejercicio 5: Ejes de simetría

¿Cuántos ejes de simetría tiene cada figura?

1. Cuadrado
2. Rombo
3. Hexágono regular

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **4** ejes
2. **2** ejes (las diagonales)
3. **6** ejes

</details>

---
