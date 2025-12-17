# Sector y Corona Circular

El **sector circular** y la **corona circular** son regiones parciales del círculo con fórmulas específicas para su área.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-sector-corona" width="700" height="300" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-sector-corona')) {
    var canvas = document.getElementById('roughjs-sector-corona');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Sector Circular y Corona Circular', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    var naranja = '#f59e0b';
    
    // === SECTOR CIRCULAR (izquierda) ===
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = azul;
    ctx.fillText('SECTOR CIRCULAR', 175, 55);
    
    var cx1 = 175, cy1 = 175;
    var r1 = 90;
    
    // Dibujar sector (como "rebanada de pizza")
    ctx.beginPath();
    ctx.moveTo(cx1, cy1);
    ctx.arc(cx1, cy1, r1, -Math.PI/3, Math.PI/6);
    ctx.closePath();
    ctx.fillStyle = '#dbeafe';
    ctx.fill();
    ctx.strokeStyle = azul;
    ctx.lineWidth = 2;
    ctx.stroke();
    
    // Radios
    rc.line(cx1, cy1, cx1 + r1*Math.cos(-Math.PI/3), cy1 + r1*Math.sin(-Math.PI/3), {stroke: verde, strokeWidth: 2.5, roughness: 0.3});
    rc.line(cx1, cy1, cx1 + r1*Math.cos(Math.PI/6), cy1 + r1*Math.sin(Math.PI/6), {stroke: verde, strokeWidth: 2.5, roughness: 0.3});
    
    // Centro
    rc.circle(cx1, cy1, 6, {fill: rojo, stroke: rojo, roughness: 0.3});
    
    // Etiquetas
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('r', cx1+50, cy1-30);
    ctx.fillStyle = naranja;
    ctx.fillText('θ', cx1+25, cy1+5);
    
    // Arco del ángulo
    ctx.beginPath();
    ctx.arc(cx1, cy1, 25, -Math.PI/3, Math.PI/6);
    ctx.strokeStyle = naranja;
    ctx.lineWidth = 2;
    ctx.stroke();
    
    // Fórmula
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A = (θ/360°) × πr²', 175, 280);
    
    // === CORONA CIRCULAR (derecha) ===
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = rojo;
    ctx.textAlign = 'center';
    ctx.fillText('CORONA CIRCULAR', 525, 55);
    
    var cx2 = 525, cy2 = 175;
    var R = 90, r2 = 50;
    
    // Círculo grande
    rc.circle(cx2, cy2, R*2, {fill: '#fecaca', fillStyle: 'solid', stroke: rojo, strokeWidth: 2, roughness: 0.5});
    // Círculo pequeño (hueco)
    rc.circle(cx2, cy2, r2*2, {fill: '#f8fafc', fillStyle: 'solid', stroke: rojo, strokeWidth: 2, roughness: 0.5});
    
    // Centro
    rc.circle(cx2, cy2, 6, {fill: rojo, stroke: rojo, roughness: 0.3});
    
    // Radios
    rc.line(cx2, cy2, cx2, cy2-R, {stroke: verde, strokeWidth: 2, roughness: 0.3});
    rc.line(cx2, cy2, cx2, cy2-r2, {stroke: azul, strokeWidth: 2, roughness: 0.3});
    
    // Etiquetas
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('R', cx2+10, cy2-65);
    ctx.fillStyle = azul;
    ctx.fillText('r', cx2+10, cy2-30);
    
    // Fórmula
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A = π(R² - r²)', 525, 280);
  }
});
</script>

---

## 📖 Sector circular

> **Definición:** Un sector circular es la región comprendida entre **dos radios** y el **arco** que los une. Es como una "rebanada de pizza".

### Elementos

| Elemento | Descripción |
|----------|-------------|
| Radio | Distancia del centro al arco |
| Ángulo central ($\theta$) | Ángulo entre los dos radios |
| Arco | Porción de la circunferencia |

---

## 📖 Área del sector circular

### Fórmula (ángulo en grados)

$$
A_{sector} = \frac{\theta}{360°} \times \pi r^2
$$

### Fórmula (ángulo en radianes)

$$
A_{sector} = \frac{1}{2} r^2 \theta
$$

### Ejemplo

Sector con radio 6 cm y ángulo de 60°:

$$
A = \frac{60°}{360°} \times \pi(6)^2 = \frac{1}{6} \times 36\pi = 6\pi \approx 18.85 \text{ cm}^2
$$

---

## 📖 Longitud del arco

### Fórmula (ángulo en grados)

$$
L_{arco} = \frac{\theta}{360°} \times 2\pi r
$$

### Fórmula (ángulo en radianes)

$$
L_{arco} = r \theta
$$

### Ejemplo

Arco con radio 10 cm y ángulo de 45°:

$$
L = \frac{45°}{360°} \times 2\pi(10) = \frac{1}{8} \times 20\pi = 2.5\pi \approx 7.85 \text{ cm}
$$

---

## 📖 Perímetro del sector

$$
P_{sector} = 2r + L_{arco}
$$

(Dos radios + la longitud del arco)

---

## 📖 Corona circular

> **Definición:** Una corona circular es la región entre **dos circunferencias concéntricas** (mismo centro, radios diferentes).

### Elementos

| Elemento | Símbolo |
|----------|---------|
| Radio exterior | $R$ |
| Radio interior | $r$ |
| Ancho de la corona | $R - r$ |

---

## 📖 Área de la corona circular

$$
A_{corona} = \pi R^2 - \pi r^2 = \pi(R^2 - r^2)
$$

También se puede escribir como:

$$
A_{corona} = \pi(R + r)(R - r)
$$

### Ejemplo

Corona con $R = 10$ cm y $r = 6$ cm:

$$
A = \pi(100 - 36) = 64\pi \approx 201.06 \text{ cm}^2
$$

---

## 📖 Sector de corona circular

Es la porción de una corona limitada por un ángulo central.

$$
A = \frac{\theta}{360°} \times \pi(R^2 - r^2)
$$

### Ejemplo

Sector de corona con $R = 8$ cm, $r = 5$ cm, $\theta = 90°$:

$$
A = \frac{90°}{360°} \times \pi(64 - 25) = \frac{1}{4} \times 39\pi = 9.75\pi \approx 30.63 \text{ cm}^2
$$

---

## 📖 Segmento circular

> **Definición:** Un segmento circular es la región entre una **cuerda** y su **arco**.

$$
A_{segmento} = A_{sector} - A_{triángulo}
$$

### Área del triángulo (formado por los dos radios)

$$
A_{triángulo} = \frac{1}{2}r^2 \sin\theta
$$

### Área del segmento

$$
A_{segmento} = \frac{1}{2}r^2(\theta - \sin\theta)
$$

(con $\theta$ en radianes)

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Área del sector

Calcula el área del sector con:

1. Radio = 8 cm, ángulo = 90°
2. Radio = 12 cm, ángulo = 60°
3. Radio = 10 cm, ángulo = 120°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \frac{90°}{360°} \times \pi(64) = \frac{1}{4} \times 64\pi = 16\pi \approx 50.27$ cm²
2. $A = \frac{60°}{360°} \times \pi(144) = \frac{1}{6} \times 144\pi = 24\pi \approx 75.4$ cm²
3. $A = \frac{120°}{360°} \times \pi(100) = \frac{1}{3} \times 100\pi = \frac{100\pi}{3} \approx 104.72$ cm²

</details>

---

### Ejercicio 2: Longitud de arco

Calcula la longitud del arco con:

1. Radio = 6 cm, ángulo = 120°
2. Radio = 15 cm, ángulo = 45°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $L = \frac{120°}{360°} \times 2\pi(6) = \frac{1}{3} \times 12\pi = 4\pi \approx 12.57$ cm
2. $L = \frac{45°}{360°} \times 2\pi(15) = \frac{1}{8} \times 30\pi = 3.75\pi \approx 11.78$ cm

</details>

---

### Ejercicio 3: Corona circular

Calcula el área de coronas con:

1. $R = 12$ cm, $r = 8$ cm
2. $R = 15$ cm, $r = 10$ cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \pi(144 - 64) = 80\pi \approx 251.33$ cm²
2. $A = \pi(225 - 100) = 125\pi \approx 392.7$ cm²

</details>

---

### Ejercicio 4: Sector de corona

Corona con $R = 10$ cm, $r = 6$ cm. Calcula el área del sector de corona con ángulo 60°.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A = \frac{60°}{360°} \times \pi(100 - 36) = \frac{1}{6} \times 64\pi = \frac{64\pi}{6} \approx 33.51 \text{ cm}^2
$$

</details>

---

### Ejercicio 5: Problema aplicado

Un limpiaparabrisas recorre un ángulo de 120° con longitudes de brazo entre 30 y 60 cm. ¿Qué área limpia?

<details>
<summary><strong>Ver respuesta</strong></summary>

Es un sector de corona con $R = 60$ cm, $r = 30$ cm, $\theta = 120°$:

$$
A = \frac{120°}{360°} \times \pi(3600 - 900) = \frac{1}{3} \times 2700\pi = 900\pi \approx 2827.43 \text{ cm}^2
$$

</details>

---
