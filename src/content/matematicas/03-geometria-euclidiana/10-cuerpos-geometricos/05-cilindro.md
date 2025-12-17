# Cilindro

El **cilindro** es un cuerpo de revolución formado por dos bases circulares paralelas unidas por una superficie lateral curva.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-cilindro" width="700" height="280" style="width: 100%; height: auto; display: block;"></canvas>
  <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 0.75rem; font-size: 0.9rem; flex-wrap: wrap;">
    <span><strong style="color: #22c55e;">r</strong> = radio de la base</span>
    <span><strong style="color: #ef4444;">h</strong> = altura del cilindro</span>
    <span><strong style="color: #64748b;">g</strong> = generatriz (en cilindro recto: g = h)</span>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-cilindro')) {
    var canvas = document.getElementById('roughjs-cilindro');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Cilindro: Elementos y Fórmulas', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    
    // Cilindro
    var cx = 180, cy = 80;
    var w = 120, h = 150;
    
    // Cuerpo del cilindro
    rc.line(cx - w/2, cy, cx - w/2, cy + h, {stroke: azul, strokeWidth: 2, roughness: 0.5});
    rc.line(cx + w/2, cy, cx + w/2, cy + h, {stroke: azul, strokeWidth: 2, roughness: 0.5});
    
    // Relleno del cuerpo
    ctx.fillStyle = '#dbeafe';
    ctx.fillRect(cx - w/2, cy, w, h);
    
    // Tapa superior (elipse)
    rc.ellipse(cx, cy, w, 35, {fill: '#bfdbfe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    
    // Tapa inferior (elipse - solo parte visible)
    rc.ellipse(cx, cy + h, w, 35, {fill: '#dbeafe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    
    // Radio
    rc.line(cx, cy, cx + w/2, cy, {stroke: verde, strokeWidth: 3, roughness: 0.3});
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('r', cx + w/4, cy - 10);
    
    // Altura
    rc.line(cx + w/2 + 20, cy, cx + w/2 + 20, cy + h, {stroke: rojo, strokeWidth: 2.5, roughness: 0.3});
    // Flechas
    ctx.fillStyle = rojo;
    ctx.beginPath();
    ctx.moveTo(cx + w/2 + 20, cy);
    ctx.lineTo(cx + w/2 + 15, cy + 10);
    ctx.lineTo(cx + w/2 + 25, cy + 10);
    ctx.fill();
    ctx.beginPath();
    ctx.moveTo(cx + w/2 + 20, cy + h);
    ctx.lineTo(cx + w/2 + 15, cy + h - 10);
    ctx.lineTo(cx + w/2 + 25, cy + h - 10);
    ctx.fill();
    ctx.fillText('h', cx + w/2 + 35, cy + h/2);
    
    // Fórmulas
    rc.rectangle(380, 50, 290, 220, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Fórmulas del Cilindro', 525, 80);
    
    ctx.font = '13px Inter, sans-serif';
    ctx.textAlign = 'left';
    
    ctx.fillStyle = verde;
    ctx.fillText('Área lateral:', 400, 110);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A_L = 2πrh', 400, 130);
    
    ctx.fillStyle = azul;
    ctx.fillText('Área de bases:', 400, 160);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A_bases = 2πr²', 400, 180);
    
    ctx.fillStyle = '#64748b';
    ctx.fillText('Área total:', 400, 210);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A_T = 2πr(h + r)', 400, 230);
    
    ctx.fillStyle = rojo;
    ctx.fillText('Volumen:', 400, 260);
    ctx.fillStyle = '#1e293b';
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillText('V = πr²h', 480, 260);
  }
});
</script>

---

## 📖 Definición

> **Definición:** Un cilindro recto es un cuerpo geométrico limitado por dos **círculos paralelos e iguales** (bases) y una **superficie lateral curva**.

---

## 📖 Elementos del cilindro

| Elemento | Descripción |
|----------|-------------|
| Bases | Dos círculos iguales y paralelos |
| Radio ($r$) | Radio de las bases |
| Altura ($h$) | Distancia entre las bases |
| Generatriz ($g$) | Segmento que une las circunferencias de las bases |
| Eje | Segmento que une los centros de las bases |

En el cilindro recto: $g = h$

---

## 📖 Desarrollo plano

Al "desenrollar" un cilindro se obtiene:
- Un **rectángulo** (la superficie lateral)
- Dos **círculos** (las bases)

Las dimensiones del rectángulo:
- Largo = circunferencia de la base = $2\pi r$
- Ancho = altura = $h$

---

## 📖 Área del cilindro

### Área lateral

$$
A_L = 2\pi r \times h
$$

(Circunferencia de la base × altura)

### Área de las bases

$$
A_{bases} = 2\pi r^2
$$

### Área total

$$
A_T = A_L + A_{bases} = 2\pi r h + 2\pi r^2 = 2\pi r(h + r)
$$

---

## 📖 Volumen del cilindro

$$
V = \pi r^2 \times h = A_{base} \times h
$$

(Área del círculo × altura)

---

## 📖 Ejemplos

### Ejemplo 1

Cilindro con radio 5 cm y altura 10 cm:

$$
A_L = 2\pi(5)(10) = 100\pi \approx 314.16 \text{ cm}^2
$$

$$
A_T = 2\pi(5)(10 + 5) = 150\pi \approx 471.24 \text{ cm}^2
$$

$$
V = \pi(5)^2(10) = 250\pi \approx 785.4 \text{ cm}^3
$$

### Ejemplo 2

Cilindro con radio 3 cm y altura 8 cm:

$$
V = \pi(9)(8) = 72\pi \approx 226.19 \text{ cm}^3
$$

---

## 📖 Encontrar elementos desconocidos

### Conociendo el volumen y la altura

$$
r = \sqrt{\frac{V}{\pi h}}
$$

### Conociendo el volumen y el radio

$$
h = \frac{V}{\pi r^2}
$$

---

## 📖 Relación con el prisma

El cilindro es como un "prisma de infinitos lados" con base circular.

$$
V_{cilindro} = A_{base} \times h
$$

(Misma fórmula que el prisma)

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Área y volumen

Calcula el área lateral, área total y volumen:

1. Radio = 4 cm, altura = 10 cm
2. Radio = 7 cm, altura = 5 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

**1.** 
- $A_L = 2\pi(4)(10) = 80\pi \approx 251.33$ cm²
- $A_T = 2\pi(4)(14) = 112\pi \approx 351.86$ cm²
- $V = \pi(16)(10) = 160\pi \approx 502.65$ cm³

**2.**
- $A_L = 2\pi(7)(5) = 70\pi \approx 219.91$ cm²
- $A_T = 2\pi(7)(12) = 168\pi \approx 527.79$ cm²
- $V = \pi(49)(5) = 245\pi \approx 769.69$ cm³

</details>

---

### Ejercicio 2: Encontrar la altura

El volumen de un cilindro es 314 cm³ y el radio es 5 cm. ¿Cuál es la altura? (Usa $\pi \approx 3.14$)

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
h = \frac{314}{3.14 \times 25} = \frac{314}{78.5} = 4 \text{ cm}
$$

</details>

---

### Ejercicio 3: Encontrar el radio

El volumen de un cilindro es 628 cm³ y la altura es 8 cm. ¿Cuál es el radio?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
r^2 = \frac{628}{3.14 \times 8} = \frac{628}{25.12} = 25
$$

$$
r = 5 \text{ cm}
$$

</details>

---

### Ejercicio 4: Problema aplicado

Un tanque cilíndrico tiene radio 2 m y altura 3 m. ¿Cuántos litros cabe? (1 m³ = 1000 L)

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
V = \pi(4)(3) = 12\pi \approx 37.7 \text{ m}^3
$$

$$
= 37,700 \text{ litros}
$$

</details>

---

### Ejercicio 5: Comparación

Si duplicamos el radio de un cilindro (manteniendo la altura), ¿en cuánto se multiplica el volumen?

<details>
<summary><strong>Ver respuesta</strong></summary>

$V_{original} = \pi r^2 h$

$V_{nuevo} = \pi (2r)^2 h = 4\pi r^2 h$

El volumen se multiplica por **4**.

</details>

---
