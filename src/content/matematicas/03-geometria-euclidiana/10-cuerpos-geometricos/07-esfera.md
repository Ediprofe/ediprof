# Esfera

La **esfera** es el cuerpo geométrico más simétrico. Todos sus puntos superficiales están a la misma distancia del centro.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-esfera" width="700" height="280" style="width: 100%; height: auto; display: block;"></canvas>
  <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 0.75rem; font-size: 0.9rem; flex-wrap: wrap;">
    <span><strong style="color: #ef4444;">O</strong> = centro de la esfera</span>
    <span><strong style="color: #22c55e;">r</strong> = radio</span>
    <span><strong style="color: #64748b;">d</strong> = diámetro = 2r</span>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-esfera')) {
    var canvas = document.getElementById('roughjs-esfera');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Esfera: Elementos y Fórmulas', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    
    // Esfera
    var cx = 180, cy = 160;
    var r = 100;
    
    // Círculo principal
    rc.circle(cx, cy, r * 2, {fill: '#dbeafe', stroke: azul, strokeWidth: 2.5, roughness: 0.5});
    
    // Ecuador (elipse horizontal)
    rc.ellipse(cx, cy, r * 2, 40, {stroke: azul, strokeWidth: 1.5, roughness: 0.3});
    
    // Meridiano (elipse vertical - parte visible)
    ctx.strokeStyle = azul;
    ctx.lineWidth = 1.5;
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.ellipse(cx, cy, 30, r, 0, 0, Math.PI * 2);
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Centro
    rc.circle(cx, cy, 8, {fill: rojo, stroke: rojo, roughness: 0.3});
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = rojo;
    ctx.fillText('O', cx - 15, cy + 5);
    
    // Radio
    rc.line(cx, cy, cx + r, cy, {stroke: verde, strokeWidth: 3, roughness: 0.3});
    ctx.fillStyle = verde;
    ctx.fillText('r', cx + r/2, cy - 10);
    
    // Diámetro (punteado)
    ctx.setLineDash([5, 5]);
    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(cx - r, cy);
    ctx.lineTo(cx + r, cy);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('d = 2r', cx, cy + 25);
    
    // Fórmulas
    rc.rectangle(380, 50, 290, 220, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Fórmulas de la Esfera', 525, 80);
    
    ctx.font = '13px Inter, sans-serif';
    ctx.textAlign = 'left';
    
    ctx.fillStyle = verde;
    ctx.fillText('Radio:', 400, 110);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('r', 480, 110);
    
    ctx.fillStyle = azul;
    ctx.fillText('Área superficial:', 400, 145);
    ctx.fillStyle = '#1e293b';
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillText('A = 4πr²', 400, 170);
    
    ctx.font = '13px Inter, sans-serif';
    ctx.fillStyle = rojo;
    ctx.fillText('Volumen:', 400, 205);
    ctx.fillStyle = '#1e293b';
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillText('V = (4/3)πr³', 400, 230);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('El área es 4 veces el área', 400, 255);
    ctx.fillText('del círculo máximo', 400, 270);
  }
});
</script>

---

## 📖 Definición

> **Definición:** Una esfera es el conjunto de todos los puntos del espacio que están a la **misma distancia** de un punto fijo llamado **centro**.

La esfera es la versión 3D del círculo.

---

## 📖 Elementos de la esfera

| Elemento | Descripción |
|----------|-------------|
| Centro | Punto equidistante de toda la superficie |
| Radio ($r$) | Distancia del centro a cualquier punto de la superficie |
| Diámetro ($d$) | Mayor distancia entre dos puntos de la esfera ($d = 2r$) |

---

## 📖 Diferencia esfera y bola

| Concepto | Descripción |
|----------|-------------|
| Esfera | Solo la **superficie** (cáscara) |
| Bola | La esfera más su **interior** |

Similar a: circunferencia vs círculo

---

## 📖 Área de la esfera

$$
A = 4\pi r^2
$$

### ¿Por qué 4πr²?

El área de la esfera es exactamente **4 veces** el área del círculo con el mismo radio.

### Ejemplo

Esfera de radio 5 cm:

$$
A = 4\pi(25) = 100\pi \approx 314.16 \text{ cm}^2
$$

---

## 📖 Volumen de la esfera

$$
V = \frac{4}{3}\pi r^3
$$

### Ejemplo

Esfera de radio 6 cm:

$$
V = \frac{4}{3}\pi(216) = 288\pi \approx 904.78 \text{ cm}^3
$$

---

## 📖 Relación con el cilindro circunscrito

Arquímedes descubrió que una esfera inscrita en un cilindro:

- Tiene **2/3 del volumen** del cilindro
- Tiene **2/3 del área superficial** del cilindro

$$
\frac{V_{esfera}}{V_{cilindro}} = \frac{\frac{4}{3}\pi r^3}{2\pi r^3} = \frac{2}{3}
$$

---

## 📖 Encontrar el radio

### Conociendo el área

$$
r = \sqrt{\frac{A}{4\pi}}
$$

### Conociendo el volumen

$$
r = \sqrt[3]{\frac{3V}{4\pi}}
$$

---

## 📖 Secciones de la esfera

### Hemisferio

Mitad de la esfera:

$$
V_{hemisferio} = \frac{2}{3}\pi r^3
$$

### Casquete esférico

Porción cortada por un plano.

### Zona esférica

Región entre dos planos paralelos.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Área y volumen

Calcula el área y volumen de esferas con radio:

1. 3 cm
2. 7 cm
3. 10 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = 36\pi \approx 113.1$ cm², $V = 36\pi \approx 113.1$ cm³
2. $A = 196\pi \approx 615.75$ cm², $V = \frac{1372\pi}{3} \approx 1436.76$ cm³
3. $A = 400\pi \approx 1256.64$ cm², $V = \frac{4000\pi}{3} \approx 4188.79$ cm³

</details>

---

### Ejercicio 2: Encontrar el radio

1. El área de una esfera es 314 cm². ¿Cuál es el radio? (usa $\pi \approx 3.14$)
2. El volumen de una esfera es 904.78 cm³. ¿Cuál es el radio?

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $r = \sqrt{\frac{314}{4 \times 3.14}} = \sqrt{25} = 5$ cm
2. $r = \sqrt[3]{\frac{3 \times 904.78}{4 \times 3.14}} = \sqrt[3]{216} = 6$ cm

</details>

---

### Ejercicio 3: Comparación

Si duplicamos el radio de una esfera, ¿en cuánto se multiplican el área y el volumen?

<details>
<summary><strong>Ver respuesta</strong></summary>

- Área: Se multiplica por $2^2 = 4$
- Volumen: Se multiplica por $2^3 = 8$

</details>

---

### Ejercicio 4: Hemisferio

Calcula el volumen de un hemisferio de radio 9 cm.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
V = \frac{2}{3}\pi(729) = 486\pi \approx 1526.81 \text{ cm}^3
$$

</details>

---

### Ejercicio 5: Problema aplicado

Una pelota de fútbol tiene diámetro 22 cm. Calcula su área superficial.

<details>
<summary><strong>Ver respuesta</strong></summary>

$r = 11$ cm

$$
A = 4\pi(121) = 484\pi \approx 1520.53 \text{ cm}^2
$$

</details>

---
