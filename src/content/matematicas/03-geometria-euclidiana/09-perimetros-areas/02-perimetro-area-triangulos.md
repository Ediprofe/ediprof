# Perímetro y Área de Triángulos

El triángulo es una de las figuras más importantes en geometría. Su área tiene varias fórmulas dependiendo de la información disponible.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-triangulo-area" width="700" height="280" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-triangulo-area')) {
    var canvas = document.getElementById('roughjs-triangulo-area');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Área del Triángulo: A = (b × h) / 2', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    
    // Triángulo
    var A = [100, 220];
    var B = [350, 220];
    var C = [200, 80];
    rc.polygon([A, B, C], {fill: '#dbeafe', fillStyle: 'solid', stroke: azul, strokeWidth: 2.5, roughness: 0.5});
    
    // Base (resaltada)
    rc.line(A[0], A[1], B[0], B[1], {stroke: verde, strokeWidth: 4, roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('b (base)', 225, 245);
    
    // Altura (perpendicular)
    rc.line(200, 220, 200, 80, {stroke: rojo, strokeWidth: 3, roughness: 0.3});
    // Símbolo de ángulo recto
    rc.rectangle(200, 205, 15, 15, {stroke: rojo, strokeWidth: 1.5, roughness: 0.2});
    ctx.fillStyle = rojo;
    ctx.fillText('h', 185, 150);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillText('(altura)', 175, 165);
    
    // Etiquetas de vértices
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = azul;
    ctx.fillText('A', A[0]-15, A[1]+5);
    ctx.fillText('B', B[0]+15, B[1]+5);
    ctx.fillText('C', C[0], C[1]-10);
    
    // Fórmula en recuadro
    rc.rectangle(420, 80, 250, 120, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Fórmula del Área', 545, 105);
    ctx.font = '20px Inter, sans-serif';
    ctx.fillText('A = b × h / 2', 545, 140);
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('La altura es PERPENDICULAR', 545, 170);
    ctx.fillText('a la base', 545, 185);
  }
});
</script>

---

## 📖 Perímetro del triángulo

El perímetro es la suma de los tres lados:

$$
P = a + b + c
$$

### Ejemplo

Triángulo con lados 5, 7 y 8 cm:

$$
P = 5 + 7 + 8 = 20 \text{ cm}
$$

---

## 📖 Área del triángulo (fórmula básica)

$$
A = \frac{b \times h}{2}
$$

Donde:
- $b$ = base (cualquier lado)
- $h$ = altura (perpendicular desde el vértice opuesto)

### Ejemplo

Triángulo con base 10 cm y altura 6 cm:

$$
A = \frac{10 \times 6}{2} = \frac{60}{2} = 30 \text{ cm}^2
$$

---

## 📖 Área según el tipo de triángulo

### Triángulo rectángulo

Los catetos pueden ser base y altura:

$$
A = \frac{c_1 \times c_2}{2}
$$

### Ejemplo

Triángulo rectángulo con catetos 3 y 4 cm:

$$
A = \frac{3 \times 4}{2} = 6 \text{ cm}^2
$$

---

### Triángulo equilátero

Si el lado mide $l$:

$$
A = \frac{l^2 \sqrt{3}}{4}
$$

### Ejemplo

Triángulo equilátero de lado 6 cm:

$$
A = \frac{6^2 \sqrt{3}}{4} = \frac{36\sqrt{3}}{4} = 9\sqrt{3} \approx 15.59 \text{ cm}^2
$$

---

## 📖 Fórmula de Herón

Cuando conocemos los tres lados pero no la altura.

### Semiperímetro

$$
s = \frac{a + b + c}{2}
$$

### Fórmula

$$
A = \sqrt{s(s-a)(s-b)(s-c)}
$$

### Ejemplo

Triángulo con lados 5, 6 y 7 cm:

$$
s = \frac{5 + 6 + 7}{2} = 9
$$

$$
A = \sqrt{9(9-5)(9-6)(9-7)} = \sqrt{9 \times 4 \times 3 \times 2} = \sqrt{216} \approx 14.7 \text{ cm}^2
$$

---

## 📖 Altura del triángulo

Si conocemos el área y la base:

$$
h = \frac{2A}{b}
$$

### Ejemplo

Si $A = 24$ cm² y $b = 8$ cm:

$$
h = \frac{2 \times 24}{8} = \frac{48}{8} = 6 \text{ cm}
$$

---

## 📖 Alturas de triángulos especiales

### Triángulo equilátero

$$
h = \frac{l\sqrt{3}}{2}
$$

### Triángulo isósceles

Altura sobre la base $b$, con lados iguales $a$:

$$
h = \sqrt{a^2 - \frac{b^2}{4}}
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Perímetros

Calcula el perímetro de triángulos con lados:

1. 4, 5, 6 cm
2. 8, 8, 10 cm
3. 5, 5, 5 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $P = 4 + 5 + 6 = 15$ cm
2. $P = 8 + 8 + 10 = 26$ cm
3. $P = 5 + 5 + 5 = 15$ cm

</details>

---

### Ejercicio 2: Área con base y altura

Calcula el área:

1. Base = 12 cm, altura = 5 cm
2. Base = 9 cm, altura = 8 cm
3. Base = 14 cm, altura = 7 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \frac{12 \times 5}{2} = 30$ cm²
2. $A = \frac{9 \times 8}{2} = 36$ cm²
3. $A = \frac{14 \times 7}{2} = 49$ cm²

</details>

---

### Ejercicio 3: Triángulo rectángulo

Catetos de 6 y 8 cm. Calcula:

1. El área
2. El perímetro (la hipotenusa es 10 cm)

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \frac{6 \times 8}{2} = 24$ cm²
2. $P = 6 + 8 + 10 = 24$ cm

</details>

---

### Ejercicio 4: Fórmula de Herón

Calcula el área de un triángulo con lados 8, 10 y 12 cm.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
s = \frac{8 + 10 + 12}{2} = 15
$$

$$
A = \sqrt{15(15-8)(15-10)(15-12)} = \sqrt{15 \times 7 \times 5 \times 3} = \sqrt{1575} \approx 39.7 \text{ cm}^2
$$

</details>

---

### Ejercicio 5: Encontrar la altura

Un triángulo tiene área 60 cm² y base 15 cm. ¿Cuál es la altura?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
h = \frac{2 \times 60}{15} = \frac{120}{15} = 8 \text{ cm}
$$

</details>

---
