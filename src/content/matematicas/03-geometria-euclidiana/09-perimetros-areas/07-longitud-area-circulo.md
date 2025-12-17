# Longitud y Área del Círculo

Consolidamos las fórmulas de la circunferencia y el círculo en el contexto de perímetros y áreas.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-circulo-area" width="700" height="300" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-circulo-area')) {
    var canvas = document.getElementById('roughjs-circulo-area');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Longitud y Área del Círculo', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    
    // Círculo principal
    var cx = 200, cy = 165;
    var r = 100;
    rc.circle(cx, cy, r*2, {fill: '#dbeafe', fillStyle: 'solid', stroke: azul, strokeWidth: 3, roughness: 0.5});
    
    // Centro
    rc.circle(cx, cy, 8, {fill: rojo, stroke: rojo, roughness: 0.3});
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = rojo;
    ctx.fillText('O', cx-15, cy+5);
    
    // Radio
    rc.line(cx, cy, cx+r, cy, {stroke: verde, strokeWidth: 3, roughness: 0.3});
    ctx.fillStyle = verde;
    ctx.fillText('r', cx+50, cy-10);
    
    // Diámetro (línea punteada)
    rc.line(cx-r, cy, cx+r, cy, {stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.3});
    ctx.fillStyle = '#64748b';
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('d = 2r', cx, cy+20);
    
    // Circunferencia resaltada (arco)
    ctx.strokeStyle = azul;
    ctx.lineWidth = 4;
    ctx.setLineDash([8, 4]);
    ctx.beginPath();
    ctx.arc(cx, cy, r, 0, Math.PI * 0.7);
    ctx.stroke();
    ctx.setLineDash([]);
    
    ctx.fillStyle = azul;
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('C = 2πr', cx+80, cy-80);
    
    // Fórmulas en recuadro
    rc.rectangle(380, 50, 290, 200, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Fórmulas del Círculo', 525, 80);
    
    ctx.font = '13px Inter, sans-serif';
    ctx.textAlign = 'left';
    
    // Longitud
    ctx.fillStyle = azul;
    ctx.fillText('Longitud (perímetro):', 400, 110);
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('C = 2πr = πd', 400, 135);
    
    // Área
    ctx.font = '13px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('Área:', 400, 165);
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A = πr²', 400, 190);
    
    // Valor de pi
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('π ≈ 3.14159...', 400, 220);
    ctx.fillText('r = radio, d = diámetro', 400, 240);
  }
});
</script>

---

## 📖 Longitud de la circunferencia (perímetro del círculo)

La longitud de la circunferencia es el "perímetro" del círculo:

$$
C = 2\pi r = \pi d
$$

Donde:
- $r$ = radio
- $d$ = diámetro ($d = 2r$)
- $\pi \approx 3.14159...$

### Ejemplos

| Radio | Diámetro | Longitud |
|-------|----------|----------|
| 5 cm | 10 cm | $10\pi \approx 31.42$ cm |
| 7 cm | 14 cm | $14\pi \approx 43.98$ cm |
| 10 cm | 20 cm | $20\pi \approx 62.83$ cm |

---

## 📖 Área del círculo

$$
A = \pi r^2
$$

### Ejemplos

| Radio | Área |
|-------|------|
| 3 cm | $9\pi \approx 28.27$ cm² |
| 5 cm | $25\pi \approx 78.54$ cm² |
| 10 cm | $100\pi \approx 314.16$ cm² |

---

## 📖 Relación entre longitud y área

Si conocemos la longitud $C$:

$$
r = \frac{C}{2\pi}
$$

$$
A = \pi \left(\frac{C}{2\pi}\right)^2 = \frac{C^2}{4\pi}
$$

---

## 📖 Semicírculo

### Perímetro del semicírculo

$$
P = \pi r + 2r = r(\pi + 2)
$$

(Mitad de la circunferencia + diámetro)

### Área del semicírculo

$$
A = \frac{\pi r^2}{2}
$$

### Ejemplo

Semicírculo de radio 6 cm:

$$
P = 6(\pi + 2) \approx 6(5.14) = 30.85 \text{ cm}
$$

$$
A = \frac{\pi \times 36}{2} = 18\pi \approx 56.55 \text{ cm}^2
$$

---

## 📖 Cuadrante (cuarto de círculo)

### Perímetro

$$
P = \frac{2\pi r}{4} + 2r = \frac{\pi r}{2} + 2r
$$

### Área

$$
A = \frac{\pi r^2}{4}
$$

---

## 📖 Encontrar elementos desconocidos

### Conociendo el área

$$
r = \sqrt{\frac{A}{\pi}}
$$

### Conociendo la longitud

$$
r = \frac{C}{2\pi}
$$

---

## 📖 Comparación: Cuadrado vs Círculo

Para un cuadrado **inscrito** en un círculo de radio $r$:

$$
\text{Lado del cuadrado} = r\sqrt{2}
$$

$$
\text{Área del cuadrado} = 2r^2
$$

La razón de áreas:

$$
\frac{A_{círculo}}{A_{cuadrado inscrito}} = \frac{\pi r^2}{2r^2} = \frac{\pi}{2} \approx 1.57
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Longitud y área

Calcula la longitud de la circunferencia y el área del círculo:

1. Radio = 4 cm
2. Radio = 9 cm
3. Diámetro = 16 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $C = 8\pi \approx 25.13$ cm, $A = 16\pi \approx 50.27$ cm²
2. $C = 18\pi \approx 56.55$ cm, $A = 81\pi \approx 254.47$ cm²
3. $r = 8$, $C = 16\pi \approx 50.27$ cm, $A = 64\pi \approx 201.06$ cm²

</details>

---

### Ejercicio 2: Semicírculo

Calcula el perímetro y área de un semicírculo de radio 10 cm.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
P = 10\pi + 20 = 10\pi + 20 \approx 51.42 \text{ cm}
$$

$$
A = \frac{\pi \times 100}{2} = 50\pi \approx 157.08 \text{ cm}^2
$$

</details>

---

### Ejercicio 3: Encontrar el radio

1. El área de un círculo es 154 cm². ¿Cuál es el radio? (usa $\pi = \frac{22}{7}$)
2. La longitud de una circunferencia es 31.4 cm. ¿Cuál es el radio?

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $r = \sqrt{\frac{154 \times 7}{22}} = \sqrt{49} = 7$ cm
2. $r = \frac{31.4}{2\pi} = \frac{31.4}{6.28} = 5$ cm

</details>

---

### Ejercicio 4: Problema aplicado

Una pizza circular tiene diámetro de 40 cm. Calcula:

1. El área total de la pizza
2. El área de una porción si se corta en 8 partes iguales

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $r = 20$ cm, $A = \pi(20)^2 = 400\pi \approx 1256.64$ cm²
2. Cada porción = $\frac{400\pi}{8} = 50\pi \approx 157.08$ cm²

</details>

---

### Ejercicio 5: Comparación

¿Qué tiene mayor área: un cuadrado de lado 10 cm o un círculo de diámetro 10 cm?

<details>
<summary><strong>Ver respuesta</strong></summary>

Cuadrado: $A = 100$ cm²

Círculo: $r = 5$, $A = 25\pi \approx 78.54$ cm²

El **cuadrado** tiene mayor área.

</details>

---
