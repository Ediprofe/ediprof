# Pirámides

Una **pirámide** es un poliedro con una base poligonal y caras laterales triangulares que convergen en un vértice llamado **cúspide** o **ápice**.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-piramide" width="700" height="280" style="width: 100%; height: auto; display: block;"></canvas>
  <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 0.75rem; font-size: 0.9rem; flex-wrap: wrap;">
    <span><strong style="color: #ef4444;">h</strong> = altura (perpendicular a la base)</span>
    <span><strong style="color: #f59e0b;">aₚ</strong> = apotema de la pirámide (altura de cara lateral)</span>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-piramide')) {
    var canvas = document.getElementById('roughjs-piramide');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Pirámide Cuadrangular: Elementos', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    var naranja = '#f59e0b';
    
    // Pirámide cuadrangular
    // Base (cuadrado en perspectiva)
    var b1 = [120, 230], b2 = [260, 250], b3 = [300, 200], b4 = [160, 180];
    // Cúspide
    var apex = [210, 70];
    
    // Base
    rc.polygon([b1, b2, b3, b4], {fill: '#dbeafe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    
    // Caras laterales
    rc.polygon([b1, b2, apex], {fill: '#bfdbfe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    rc.polygon([b2, b3, apex], {fill: '#93c5fd', stroke: azul, strokeWidth: 2, roughness: 0.5});
    rc.polygon([b3, b4, apex], {fill: '#dbeafe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    rc.polygon([b4, b1, apex], {fill: '#bfdbfe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    
    // Centro de la base
    var centroX = (b1[0] + b2[0] + b3[0] + b4[0]) / 4;
    var centroY = (b1[1] + b2[1] + b3[1] + b4[1]) / 4;
    
    // Altura (línea vertical desde centro de base a cúspide)
    rc.line(centroX, centroY, apex[0], apex[1], {stroke: rojo, strokeWidth: 2.5, roughness: 0.3});
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = rojo;
    ctx.fillText('h', centroX + 15, 150);
    
    // Apotema de la pirámide (altura de cara lateral)
    var midBase = [(b1[0] + b2[0])/2, (b1[1] + b2[1])/2];
    rc.line(midBase[0], midBase[1], apex[0], apex[1], {stroke: naranja, strokeWidth: 2, roughness: 0.3});
    ctx.fillStyle = naranja;
    ctx.fillText('aₚ', midBase[0] - 20, midBase[1] - 40);
    
    // Cúspide
    rc.circle(apex[0], apex[1], 8, {fill: verde, stroke: verde, roughness: 0.3});
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('Cúspide', apex[0] + 20, apex[1]);
    
    // Fórmulas
    rc.rectangle(380, 60, 290, 200, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Fórmulas de la Pirámide', 525, 90);
    
    ctx.font = '13px Inter, sans-serif';
    ctx.textAlign = 'left';
    
    ctx.fillStyle = naranja;
    ctx.fillText('Área lateral:', 400, 120);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A_L = (P × aₚ) / 2', 400, 140);
    
    ctx.fillStyle = azul;
    ctx.fillText('Área total:', 400, 170);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A_T = A_L + A_base', 400, 190);
    
    ctx.fillStyle = rojo;
    ctx.fillText('Volumen:', 400, 220);
    ctx.fillStyle = '#1e293b';
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillText('V = (A_base × h) / 3', 400, 245);
  }
});
</script>

---

## 📖 Definición

> **Definición:** Una pirámide es un poliedro que tiene una **base poligonal** y **caras laterales triangulares** que se unen en un punto común llamado **vértice** o **cúspide**.

---

## 📖 Elementos de la pirámide

| Elemento | Descripción |
|----------|-------------|
| Base | Polígono en el que se apoya |
| Cúspide (vértice) | Punto donde se unen las caras laterales |
| Caras laterales | Triángulos que unen la base con la cúspide |
| Aristas básicas | Lados de la base |
| Aristas laterales | Unen los vértices de la base con la cúspide |
| Altura ($h$) | Distancia perpendicular de la base a la cúspide |
| Apotema ($a_p$) | Altura de una cara lateral (en pirámides regulares) |

---

## 📖 Clasificación de pirámides

### Por el polígono de la base

| Base | Nombre | Caras laterales |
|------|--------|-----------------|
| Triángulo | Pirámide triangular (tetraedro) | 3 |
| Cuadrado | Pirámide cuadrangular | 4 |
| Pentágono | Pirámide pentagonal | 5 |
| Hexágono | Pirámide hexagonal | 6 |

### Por la regularidad

| Tipo | Descripción |
|------|-------------|
| Regular | Base es polígono regular, cúspide sobre el centro |
| Irregular | Base irregular o cúspide descentrada |

---

## 📖 Área de la pirámide

### Área lateral

$$
A_L = \frac{P_{base} \times a_p}{2}
$$

Donde $a_p$ es el apotema de la pirámide (altura de las caras triangulares).

### Área total

$$
A_T = A_L + A_{base}
$$

---

## 📖 Volumen de la pirámide

$$
V = \frac{A_{base} \times h}{3}
$$

> El volumen de una pirámide es **un tercio** del volumen de un prisma con la misma base y altura.

---

## 📖 Elementos por tipo de pirámide

| Pirámide | Caras | Aristas | Vértices |
|----------|-------|---------|----------|
| Triangular | 4 | 6 | 4 |
| Cuadrangular | 5 | 8 | 5 |
| Pentagonal | 6 | 10 | 6 |
| Hexagonal | 7 | 12 | 7 |

### Fórmulas generales (base de n lados)

- Caras: $n + 1$
- Aristas: $2n$
- Vértices: $n + 1$

---

## 📖 Ejemplos

### Ejemplo 1: Pirámide cuadrangular

Base cuadrada de 6 cm, altura 8 cm:

$$
A_{base} = 6^2 = 36 \text{ cm}^2
$$

$$
V = \frac{36 \times 8}{3} = \frac{288}{3} = 96 \text{ cm}^3
$$

### Ejemplo 2: Pirámide triangular regular (tetraedro)

Base triangular equilátera de lado 4 cm, altura del triángulo ≈ 3.46 cm:

$$
A_{base} = \frac{4 \times 3.46}{2} \approx 6.93 \text{ cm}^2
$$

Si la altura de la pirámide es 5 cm:

$$
V = \frac{6.93 \times 5}{3} \approx 11.55 \text{ cm}^3
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Volumen

Calcula el volumen de pirámides con:

1. Base cuadrada de 9 cm², altura 12 cm
2. Base triangular de 24 cm², altura 10 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $V = \frac{9 \times 12}{3} = 36$ cm³
2. $V = \frac{24 \times 10}{3} = 80$ cm³

</details>

---

### Ejercicio 2: Pirámide cuadrada

Una pirámide tiene base cuadrada de lado 10 cm y altura 12 cm. Calcula:

1. Área de la base
2. Volumen

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A_{base} = 100$ cm²
2. $V = \frac{100 \times 12}{3} = 400$ cm³

</details>

---

### Ejercicio 3: Problema inverso

El volumen de una pirámide de base cuadrada es 200 cm³. Si la altura es 12 cm, ¿cuánto mide el lado de la base?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A_{base} = \frac{3 \times 200}{12} = 50 \text{ cm}^2
$$

$$
\text{Lado} = \sqrt{50} \approx 7.07 \text{ cm}
$$

</details>

---

### Ejercicio 4: Comparación

Una pirámide y un prisma tienen la misma base y la misma altura. ¿Cuántas pirámides caben en el prisma?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\frac{V_{prisma}}{V_{pirámide}} = \frac{A_b \times h}{\frac{A_b \times h}{3}} = 3
$$

Caben **3 pirámides**.

</details>

---

### Ejercicio 5: Elementos

¿Cuántas caras, aristas y vértices tiene una pirámide hexagonal?

<details>
<summary><strong>Ver respuesta</strong></summary>

- Caras: $6 + 1 = 7$
- Aristas: $2 \times 6 = 12$
- Vértices: $6 + 1 = 7$

</details>

---
