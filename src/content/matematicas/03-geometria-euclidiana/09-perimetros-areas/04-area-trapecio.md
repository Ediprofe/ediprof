# Área del Trapecio

El trapecio tiene una fórmula especial para su área que involucra las dos bases y la altura.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-trapecio" width="700" height="280" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-trapecio')) {
    var canvas = document.getElementById('roughjs-trapecio');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Área del Trapecio', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    var naranja = '#f59e0b';
    
    // Trapecio
    var puntos = [[100, 200], [400, 200], [320, 80], [180, 80]];
    rc.polygon(puntos, {fill: '#dbeafe', fillStyle: 'solid', stroke: azul, strokeWidth: 2.5, roughness: 0.5});
    
    // Base mayor (B)
    rc.line(100, 200, 400, 200, {stroke: verde, strokeWidth: 4, roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('B (base mayor)', 250, 225);
    
    // Base menor (b)
    rc.line(180, 80, 320, 80, {stroke: naranja, strokeWidth: 4, roughness: 0.3});
    ctx.fillStyle = naranja;
    ctx.fillText('b (base menor)', 250, 70);
    
    // Altura (h)
    rc.line(250, 200, 250, 80, {stroke: rojo, strokeWidth: 3, roughness: 0.3});
    rc.rectangle(250, 185, 12, 12, {stroke: rojo, strokeWidth: 1.5, roughness: 0.2});
    ctx.fillStyle = rojo;
    ctx.fillText('h', 235, 145);
    
    // Fórmula en recuadro
    rc.rectangle(450, 70, 220, 130, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Fórmula del Área', 560, 95);
    ctx.font = '18px Inter, sans-serif';
    ctx.fillText('A = (B + b) × h', 560, 130);
    ctx.font = '24px Inter, sans-serif';
    ctx.fillText('─────────', 560, 145);
    ctx.font = '18px Inter, sans-serif';
    ctx.fillText('2', 560, 170);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Promedio de bases × altura', 560, 190);
  }
});
</script>

---

## 📖 Elementos del trapecio

| Elemento | Símbolo | Descripción |
|----------|---------|-------------|
| Base mayor | $B$ | El lado paralelo más largo |
| Base menor | $b$ | El lado paralelo más corto |
| Altura | $h$ | Distancia perpendicular entre las bases |
| Lados | $l_1, l_2$ | Los lados no paralelos |

---

## 📖 Perímetro del trapecio

$$
P = B + b + l_1 + l_2
$$

### Trapecio isósceles

Si $l_1 = l_2 = l$:

$$
P = B + b + 2l
$$

---

## 📖 Área del trapecio

> **Fórmula:** El área del trapecio es el promedio de las bases multiplicado por la altura.

$$
A = \frac{(B + b) \times h}{2}
$$

### Otra forma

$$
A = \frac{B + b}{2} \times h = m \times h
$$

Donde $m$ es la **base media**.

---

## 📖 ¿Por qué funciona la fórmula?

El trapecio puede verse como:
- Dos triángulos (uno grande y uno pequeño) donde se resta
- O como un rectángulo con triángulos en los extremos

La fórmula promedia las bases porque el trapecio es "intermedio" entre un rectángulo de base $B$ y uno de base $b$.

---

## 📖 Ejemplos

### Ejemplo 1

Trapecio con $B = 12$ cm, $b = 8$ cm, $h = 5$ cm:

$$
A = \frac{(12 + 8) \times 5}{2} = \frac{20 \times 5}{2} = \frac{100}{2} = 50 \text{ cm}^2
$$

### Ejemplo 2

Trapecio con $B = 15$ cm, $b = 9$ cm, $h = 6$ cm:

$$
A = \frac{(15 + 9) \times 6}{2} = \frac{24 \times 6}{2} = \frac{144}{2} = 72 \text{ cm}^2
$$

---

## 📖 Encontrar elementos desconocidos

### Encontrar la altura

$$
h = \frac{2A}{B + b}
$$

### Encontrar una base

$$
B = \frac{2A}{h} - b
$$

$$
b = \frac{2A}{h} - B
$$

---

## 📖 Altura del trapecio isósceles

Si conocemos las bases y los lados:

$$
h = \sqrt{l^2 - \left(\frac{B-b}{2}\right)^2}
$$

### Ejemplo

Trapecio isósceles con $B = 16$ cm, $b = 10$ cm, $l = 5$ cm:

$$
h = \sqrt{5^2 - \left(\frac{16-10}{2}\right)^2} = \sqrt{25 - 9} = \sqrt{16} = 4 \text{ cm}
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular área

Encuentra el área de cada trapecio:

1. $B = 10$ cm, $b = 6$ cm, $h = 4$ cm
2. $B = 14$ cm, $b = 8$ cm, $h = 5$ cm
3. $B = 20$ cm, $b = 12$ cm, $h = 7$ cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \frac{(10+6) \times 4}{2} = 32$ cm²
2. $A = \frac{(14+8) \times 5}{2} = 55$ cm²
3. $A = \frac{(20+12) \times 7}{2} = 112$ cm²

</details>

---

### Ejercicio 2: Encontrar la altura

El área de un trapecio es 60 cm². Si $B = 14$ cm y $b = 6$ cm, ¿cuál es la altura?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
h = \frac{2 \times 60}{14 + 6} = \frac{120}{20} = 6 \text{ cm}
$$

</details>

---

### Ejercicio 3: Encontrar una base

Un trapecio tiene área 84 cm², altura 7 cm y base mayor 16 cm. ¿Cuánto mide la base menor?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
b = \frac{2 \times 84}{7} - 16 = 24 - 16 = 8 \text{ cm}
$$

</details>

---

### Ejercicio 4: Perímetro

Trapecio con $B = 12$ cm, $b = 8$ cm y lados no paralelos de 4 y 5 cm. Calcula el perímetro.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
P = 12 + 8 + 4 + 5 = 29 \text{ cm}
$$

</details>

---

### Ejercicio 5: Trapecio isósceles

Un trapecio isósceles tiene $B = 18$ cm, $b = 10$ cm y lados laterales de 5 cm. Calcula:

1. La altura
2. El área

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $h = \sqrt{5^2 - \left(\frac{18-10}{2}\right)^2} = \sqrt{25 - 16} = \sqrt{9} = 3$ cm

2. $A = \frac{(18+10) \times 3}{2} = 42$ cm²

</details>

---
