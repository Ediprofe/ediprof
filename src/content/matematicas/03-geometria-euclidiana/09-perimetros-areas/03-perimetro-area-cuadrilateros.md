# Perímetro y Área de Cuadriláteros

Los cuadriláteros tienen fórmulas específicas para calcular su perímetro y área, dependiendo del tipo.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-cuadrilateros" width="750" height="320" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-cuadrilateros')) {
    var canvas = document.getElementById('roughjs-cuadrilateros');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Fórmulas de Área de Cuadriláteros', 375, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var morado = '#a855f7';
    var naranja = '#f59e0b';
    
    // === CUADRADO ===
    rc.rectangle(40, 60, 100, 100, {fill: '#dbeafe', fillStyle: 'solid', stroke: azul, strokeWidth: 2, roughness: 0.5});
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = azul;
    ctx.fillText('CUADRADO', 90, 55);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('l', 90, 115);
    ctx.fillText('l', 25, 110);
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('A = l²', 90, 185);
    
    // === RECTÁNGULO ===
    rc.rectangle(180, 70, 130, 80, {fill: '#dcfce7', fillStyle: 'solid', stroke: verde, strokeWidth: 2, roughness: 0.5});
    ctx.fillStyle = verde;
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('RECTÁNGULO', 245, 55);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('a', 245, 165);
    ctx.fillText('b', 165, 110);
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('A = a × b', 245, 185);
    
    // === PARALELOGRAMO ===
    rc.polygon([[360,150], [490,150], [520,70], [390,70]], {fill: '#fef3c7', fillStyle: 'solid', stroke: naranja, strokeWidth: 2, roughness: 0.5});
    // Altura
    rc.line(450, 150, 450, 70, {stroke: '#ef4444', strokeWidth: 2, roughness: 0.3});
    rc.rectangle(450, 135, 10, 10, {stroke: '#ef4444', strokeWidth: 1, roughness: 0.2});
    ctx.fillStyle = naranja;
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('PARALELOGRAMO', 440, 55);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('b', 425, 165);
    ctx.fillStyle = '#ef4444';
    ctx.fillText('h', 460, 115);
    ctx.fillStyle = naranja;
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('A = b × h', 440, 185);
    
    // === ROMBO ===
    rc.polygon([[640,60], [700,110], [640,160], [580,110]], {fill: '#ede9fe', fillStyle: 'solid', stroke: morado, strokeWidth: 2, roughness: 0.5});
    // Diagonales
    rc.line(580, 110, 700, 110, {stroke: morado, strokeWidth: 1.5, roughness: 0.3});
    rc.line(640, 60, 640, 160, {stroke: morado, strokeWidth: 1.5, roughness: 0.3});
    ctx.fillStyle = morado;
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillText('ROMBO', 640, 50);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('d₁', 640, 175);
    ctx.fillText('d₂', 710, 115);
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('A = d₁×d₂/2', 640, 195);
    
    // Leyenda
    rc.rectangle(200, 220, 350, 80, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Resumen de Fórmulas', 375, 245);
    ctx.font = '12px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = azul;
    ctx.fillText('Cuadrado: l²', 220, 270);
    ctx.fillStyle = verde;
    ctx.fillText('Rectángulo: a×b', 220, 290);
    ctx.fillStyle = naranja;
    ctx.fillText('Paralelogramo: b×h', 380, 270);
    ctx.fillStyle = morado;
    ctx.fillText('Rombo: d₁×d₂/2', 380, 290);
  }
});
</script>

---

## 📖 Cuadrado

### Perímetro

$$
P = 4l
$$

### Área

$$
A = l^2
$$

### Ejemplo

Cuadrado de lado 5 cm:

$$
P = 4 \times 5 = 20 \text{ cm}
$$

$$
A = 5^2 = 25 \text{ cm}^2
$$

---

## 📖 Rectángulo

### Perímetro

$$
P = 2(a + b)
$$

### Área

$$
A = a \times b
$$

(largo × ancho)

### Ejemplo

Rectángulo de 8 cm × 5 cm:

$$
P = 2(8 + 5) = 2 \times 13 = 26 \text{ cm}
$$

$$
A = 8 \times 5 = 40 \text{ cm}^2
$$

---

## 📖 Paralelogramo

### Perímetro

$$
P = 2(a + b)
$$

(suma de lados diferentes, multiplicada por 2)

### Área

$$
A = b \times h
$$

(base × altura perpendicular)

### Ejemplo

Paralelogramo con base 10 cm, altura 6 cm, lados 10 y 7 cm:

$$
P = 2(10 + 7) = 34 \text{ cm}
$$

$$
A = 10 \times 6 = 60 \text{ cm}^2
$$

---

## 📖 Rombo

### Perímetro

$$
P = 4l
$$

(cuatro lados iguales)

### Área

$$
A = \frac{d_1 \times d_2}{2}
$$

(producto de diagonales dividido entre 2)

### Ejemplo

Rombo con lado 5 cm, diagonales 6 y 8 cm:

$$
P = 4 \times 5 = 20 \text{ cm}
$$

$$
A = \frac{6 \times 8}{2} = 24 \text{ cm}^2
$$

---

## 📖 Tabla resumen

| Cuadrilátero | Perímetro | Área |
|--------------|-----------|------|
| Cuadrado | $4l$ | $l^2$ |
| Rectángulo | $2(a+b)$ | $a \times b$ |
| Paralelogramo | $2(a+b)$ | $b \times h$ |
| Rombo | $4l$ | $\frac{d_1 \times d_2}{2}$ |

---

## 📖 Diagonal del cuadrado

$$
d = l\sqrt{2}
$$

### Área a partir de la diagonal

$$
A = \frac{d^2}{2}
$$

### Ejemplo

Si la diagonal mide 10 cm:

$$
A = \frac{10^2}{2} = \frac{100}{2} = 50 \text{ cm}^2
$$

---

## 📖 Diagonal del rectángulo

$$
d = \sqrt{a^2 + b^2}
$$

(Teorema de Pitágoras)

### Ejemplo

Rectángulo de 3 × 4:

$$
d = \sqrt{9 + 16} = \sqrt{25} = 5
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Cuadrado

Un cuadrado tiene lado 9 cm. Calcula:

1. Perímetro
2. Área
3. Diagonal

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $P = 4 \times 9 = 36$ cm
2. $A = 9^2 = 81$ cm²
3. $d = 9\sqrt{2} \approx 12.73$ cm

</details>

---

### Ejercicio 2: Rectángulo

Un rectángulo mide 12 cm × 5 cm. Calcula:

1. Perímetro
2. Área
3. Diagonal

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $P = 2(12 + 5) = 34$ cm
2. $A = 12 \times 5 = 60$ cm²
3. $d = \sqrt{144 + 25} = \sqrt{169} = 13$ cm

</details>

---

### Ejercicio 3: Paralelogramo

Paralelogramo con lados 8 y 6 cm, altura 5 cm (sobre el lado de 8 cm). Calcula perímetro y área.

<details>
<summary><strong>Ver respuestas</strong></summary>

$$
P = 2(8 + 6) = 28 \text{ cm}
$$

$$
A = 8 \times 5 = 40 \text{ cm}^2
$$

</details>

---

### Ejercicio 4: Rombo

Un rombo tiene diagonales de 10 y 24 cm. La relación de Pitágoras da lado = 13 cm. Calcula perímetro y área.

<details>
<summary><strong>Ver respuestas</strong></summary>

$$
P = 4 \times 13 = 52 \text{ cm}
$$

$$
A = \frac{10 \times 24}{2} = 120 \text{ cm}^2
$$

</details>

---

### Ejercicio 5: Problema inverso

El área de un rectángulo es 72 cm² y un lado mide 8 cm. ¿Cuánto mide el otro lado y el perímetro?

<details>
<summary><strong>Ver respuestas</strong></summary>

$$
\text{Otro lado} = \frac{72}{8} = 9 \text{ cm}
$$

$$
P = 2(8 + 9) = 34 \text{ cm}
$$

</details>

---
