# Prismas

Un **prisma** es un poliedro formado por dos bases paralelas e iguales, unidas por caras laterales rectangulares.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-prisma" width="700" height="280" style="width: 100%; height: auto; display: block;"></canvas>
  <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 0.75rem; font-size: 0.9rem; flex-wrap: wrap;">
    <span><strong style="color: #ef4444;">h</strong> = altura del prisma</span>
    <span><strong style="color: #3b82f6;">Base</strong> = polígono (triángulo, cuadrado, etc.)</span>
    <span><strong style="color: #64748b;">P</strong> = perímetro de la base</span>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-prisma')) {
    var canvas = document.getElementById('roughjs-prisma');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Prisma Triangular: Elementos', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    
    // Prisma triangular isométrico
    // Base inferior (triángulo)
    var b1 = [150, 220], b2 = [280, 240], b3 = [200, 260];
    // Base superior (triángulo)
    var t1 = [150, 100], t2 = [280, 120], t3 = [200, 140];
    
    // Caras laterales
    rc.polygon([b1, b2, t2, t1], {fill: '#dbeafe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    rc.polygon([b2, b3, t3, t2], {fill: '#bfdbfe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    rc.polygon([b3, b1, t1, t3], {fill: '#93c5fd', stroke: azul, strokeWidth: 2, roughness: 0.5});
    
    // Base superior (visible)
    rc.polygon([t1, t2, t3], {fill: '#dbeafe', stroke: azul, strokeWidth: 2.5, roughness: 0.5});
    
    // Altura (línea vertical)
    rc.line(215, 250, 215, 130, {stroke: rojo, strokeWidth: 2.5, roughness: 0.3});
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = rojo;
    ctx.fillText('h', 230, 190);
    
    // Etiquetas
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = azul;
    ctx.fillText('Base', 215, 280);
    ctx.fillText('superior', 215, 90);
    ctx.fillStyle = '#64748b';
    ctx.fillText('Cara lateral', 300, 180);
    
    // Fórmulas
    rc.rectangle(400, 80, 270, 180, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Fórmulas del Prisma', 535, 110);
    
    ctx.font = '13px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = verde;
    ctx.fillText('Área lateral:', 420, 140);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A_L = Perímetro_base × h', 420, 160);
    
    ctx.fillStyle = azul;
    ctx.fillText('Área total:', 420, 190);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A_T = A_L + 2 × A_base', 420, 210);
    
    ctx.fillStyle = rojo;
    ctx.fillText('Volumen:', 420, 240);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('V = A_base × h', 420, 260);
  }
});
</script>

---

## 📖 Definición

> **Definición:** Un prisma es un poliedro con dos **bases congruentes y paralelas** unidas por caras laterales que son **paralelogramos** (generalmente rectángulos).

---

## 📖 Elementos del prisma

| Elemento | Descripción |
|----------|-------------|
| Bases | Las dos caras iguales y paralelas |
| Caras laterales | Rectángulos que unen las bases |
| Aristas básicas | Lados de las bases |
| Aristas laterales | Unen las bases (son todas iguales y paralelas) |
| Altura ($h$) | Distancia entre las bases |

---

## 📖 Clasificación de prismas

### Por el polígono de la base

| Base | Nombre del prisma | Caras laterales |
|------|-------------------|-----------------|
| Triángulo | Prisma triangular | 3 |
| Cuadrado | Prisma cuadrangular | 4 |
| Pentágono | Prisma pentagonal | 5 |
| Hexágono | Prisma hexagonal | 6 |

### Por la posición de las aristas laterales

| Tipo | Descripción |
|------|-------------|
| Prisma recto | Aristas laterales perpendiculares a las bases |
| Prisma oblicuo | Aristas laterales inclinadas |

---

## 📖 Área del prisma

### Área lateral

$$
A_L = P_{base} \times h
$$

(Perímetro de la base × altura)

### Área total

$$
A_T = A_L + 2 \times A_{base} = P_{base} \times h + 2 \times A_{base}
$$

---

## 📖 Volumen del prisma

$$
V = A_{base} \times h
$$

> El volumen de cualquier prisma es el **área de la base por la altura**.

---

## 📖 Ejemplos

### Ejemplo 1: Prisma triangular

Base: triángulo de base 6 cm y altura 4 cm. Altura del prisma: 10 cm.

$$
A_{base} = \frac{6 \times 4}{2} = 12 \text{ cm}^2
$$

$$
V = 12 \times 10 = 120 \text{ cm}^3
$$

### Ejemplo 2: Prisma rectangular (ortoedro)

Dimensiones: 5 × 3 × 8 cm.

$$
A_{base} = 5 \times 3 = 15 \text{ cm}^2
$$

$$
V = 15 \times 8 = 120 \text{ cm}^3
$$

Alternativamente: $V = 5 \times 3 \times 8 = 120$ cm³

---

## 📖 Elementos por tipo de prisma

| Prisma | Caras | Aristas | Vértices |
|--------|-------|---------|----------|
| Triangular | 5 | 9 | 6 |
| Cuadrangular | 6 | 12 | 8 |
| Pentagonal | 7 | 15 | 10 |
| Hexagonal | 8 | 18 | 12 |

### Fórmulas generales (para base de n lados)

- Caras: $n + 2$
- Aristas: $3n$
- Vértices: $2n$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Volumen

Calcula el volumen de prismas con:

1. Base cuadrada de 4 cm, altura del prisma 10 cm
2. Base triangular (área = 15 cm²), altura del prisma 8 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A_{base} = 16$ cm², $V = 16 \times 10 = 160$ cm³
2. $V = 15 \times 8 = 120$ cm³

</details>

---

### Ejercicio 2: Área total

Un prisma rectangular mide 6 × 4 × 5 cm. Calcula:

1. Área de las bases
2. Área lateral
3. Área total

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A_{base} = 6 \times 4 = 24$ cm², dos bases = 48 cm²
2. $P_{base} = 2(6+4) = 20$ cm, $A_L = 20 \times 5 = 100$ cm²
3. $A_T = 100 + 48 = 148$ cm²

</details>

---

### Ejercicio 3: Problema inverso

El volumen de un prisma de base cuadrada es 180 cm³. Si la altura es 5 cm, ¿cuánto mide el lado de la base?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A_{base} = \frac{180}{5} = 36 \text{ cm}^2
$$

$$
\text{Lado} = \sqrt{36} = 6 \text{ cm}
$$

</details>

---

### Ejercicio 4: Prisma hexagonal regular

Un prisma tiene base hexagonal regular con lado 4 cm y apotema ≈ 3.46 cm. Altura del prisma: 12 cm.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A_{base} = \frac{P \times a}{2} = \frac{24 \times 3.46}{2} \approx 41.5 \text{ cm}^2
$$

$$
V \approx 41.5 \times 12 = 498 \text{ cm}^3
$$

</details>

---

### Ejercicio 5: Elementos

¿Cuántas caras, aristas y vértices tiene un prisma pentagonal?

<details>
<summary><strong>Ver respuesta</strong></summary>

- Caras: $5 + 2 = 7$
- Aristas: $3 \times 5 = 15$
- Vértices: $2 \times 5 = 10$

</details>

---
