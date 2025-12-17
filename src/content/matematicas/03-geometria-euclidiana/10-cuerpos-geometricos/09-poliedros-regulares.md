# Poliedros Regulares

Los **poliedros regulares** (también llamados **sólidos platónicos**) son poliedros donde todas las caras son polígonos regulares iguales y en cada vértice se unen el mismo número de caras.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-poliedros" width="700" height="220" style="width: 100%; height: auto; display: block;"></canvas>
  <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 0.5rem; margin-top: 1rem; text-align: center; font-size: 0.85rem;">
    <div style="padding: 0.5rem; background: #dbeafe; border-radius: 8px; border: 2px solid #3b82f6;">
      <strong style="color: #3b82f6;">Tetraedro</strong><br>
      <span style="color: #64748b;">4 caras △</span><br>
      <span style="color: #64748b;">4 vértices</span><br>
      <span style="color: #64748b;">6 aristas</span>
    </div>
    <div style="padding: 0.5rem; background: #dcfce7; border-radius: 8px; border: 2px solid #22c55e;">
      <strong style="color: #22c55e;">Cubo</strong><br>
      <span style="color: #64748b;">6 caras □</span><br>
      <span style="color: #64748b;">8 vértices</span><br>
      <span style="color: #64748b;">12 aristas</span>
    </div>
    <div style="padding: 0.5rem; background: #fecaca; border-radius: 8px; border: 2px solid #ef4444;">
      <strong style="color: #ef4444;">Octaedro</strong><br>
      <span style="color: #64748b;">8 caras △</span><br>
      <span style="color: #64748b;">6 vértices</span><br>
      <span style="color: #64748b;">12 aristas</span>
    </div>
    <div style="padding: 0.5rem; background: #ede9fe; border-radius: 8px; border: 2px solid #a855f7;">
      <strong style="color: #a855f7;">Dodecaedro</strong><br>
      <span style="color: #64748b;">12 caras ⬠</span><br>
      <span style="color: #64748b;">20 vértices</span><br>
      <span style="color: #64748b;">30 aristas</span>
    </div>
    <div style="padding: 0.5rem; background: #fef3c7; border-radius: 8px; border: 2px solid #f59e0b;">
      <strong style="color: #f59e0b;">Icosaedro</strong><br>
      <span style="color: #64748b;">20 caras △</span><br>
      <span style="color: #64748b;">12 vértices</span><br>
      <span style="color: #64748b;">30 aristas</span>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-poliedros')) {
    var canvas = document.getElementById('roughjs-poliedros');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Los 5 Sólidos Platónicos', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    var morado = '#a855f7';
    var naranja = '#f59e0b';
    
    var y = 120; // altura común
    var spacing = 140; // espacio entre figuras
    
    // Tetraedro (4 caras triangulares)
    var tx = 70;
    rc.polygon([[tx, y+50], [tx+60, y+50], [tx+30, y-30]], {fill: '#dbeafe', stroke: azul, strokeWidth: 2.5, roughness: 0.5});
    rc.polygon([[tx+60, y+50], [tx+30, y-30], [tx+75, y+10]], {fill: '#bfdbfe', stroke: azul, strokeWidth: 2.5, roughness: 0.5});
    
    // Cubo (6 caras cuadradas)
    var cx = tx + spacing;
    var s = 50;
    rc.polygon([[cx, y], [cx+s, y], [cx+s, y+s], [cx, y+s]], {fill: '#dcfce7', stroke: verde, strokeWidth: 2.5, roughness: 0.5});
    rc.polygon([[cx, y], [cx+18, y-18], [cx+s+18, y-18], [cx+s, y]], {fill: '#bbf7d0', stroke: verde, strokeWidth: 2.5, roughness: 0.5});
    rc.polygon([[cx+s, y], [cx+s+18, y-18], [cx+s+18, y+s-18], [cx+s, y+s]], {fill: '#86efac', stroke: verde, strokeWidth: 2.5, roughness: 0.5});
    
    // Octaedro (8 caras triangulares)
    var ox = cx + spacing;
    rc.polygon([[ox+30, y-45], [ox, y+10], [ox+30, y+55], [ox+60, y+10]], {fill: '#fecaca', stroke: rojo, strokeWidth: 2.5, roughness: 0.5});
    rc.polygon([[ox+30, y-45], [ox+60, y+10], [ox+45, y-5]], {fill: '#fca5a5', stroke: rojo, strokeWidth: 2.5, roughness: 0.5});
    
    // Dodecaedro (12 caras pentagonales)
    var dx = ox + spacing;
    var pv = [];
    for (var i = 0; i < 5; i++) {
      var ang = (Math.PI * 2 / 5) * i - Math.PI / 2;
      pv.push([dx + 30 + 35 * Math.cos(ang), y + 10 + 35 * Math.sin(ang)]);
    }
    rc.polygon(pv, {fill: '#ede9fe', stroke: morado, strokeWidth: 2.5, roughness: 0.5});
    rc.polygon([[pv[0][0], pv[0][1]], [pv[1][0], pv[1][1]], [dx+20, y-45]], {fill: '#ddd6fe', stroke: morado, strokeWidth: 2, roughness: 0.5});
    rc.polygon([[pv[1][0], pv[1][1]], [pv[2][0], pv[2][1]], [dx-15, y+5]], {fill: '#c4b5fd', stroke: morado, strokeWidth: 2, roughness: 0.5});
    
    // Icosaedro (20 caras triangulares)
    var ix = dx + spacing;
    rc.polygon([[ix+30, y-45], [ix, y+10], [ix+30, y+55], [ix+60, y+10]], {fill: '#fef3c7', stroke: naranja, strokeWidth: 2.5, roughness: 0.5});
    rc.polygon([[ix+30, y-45], [ix+60, y+10], [ix+50, y-15]], {fill: '#fde68a', stroke: naranja, strokeWidth: 2, roughness: 0.5});
    rc.polygon([[ix+60, y+10], [ix+30, y+55], [ix+50, y+35]], {fill: '#fcd34d', stroke: naranja, strokeWidth: 2, roughness: 0.5});
    rc.polygon([[ix, y+10], [ix+30, y+55], [ix+10, y+35]], {fill: '#fef3c7', stroke: naranja, strokeWidth: 2, roughness: 0.5});
  }
});
</script>

---

## 📖 Definición

> **Definición:** Un poliedro regular es aquel en el que:
> 1. Todas las **caras** son polígonos regulares idénticos
> 2. En cada **vértice** se unen el mismo número de caras

---

## 📖 Solo existen 5 poliedros regulares

Por razones geométricas, solo pueden existir **exactamente 5** poliedros regulares:

| Nombre | Caras | Tipo de cara | Vértices | Aristas |
|--------|-------|--------------|----------|---------|
| Tetraedro | 4 | Triángulo | 4 | 6 |
| Hexaedro (Cubo) | 6 | Cuadrado | 8 | 12 |
| Octaedro | 8 | Triángulo | 6 | 12 |
| Dodecaedro | 12 | Pentágono | 20 | 30 |
| Icosaedro | 20 | Triángulo | 12 | 30 |

---

## 📖 El Tetraedro

- **Caras:** 4 triángulos equiláteros
- **Vértices:** 4
- **Aristas:** 6
- **Caras por vértice:** 3

### Fórmulas (arista $a$)

$$
A = a^2\sqrt{3}
$$

$$
V = \frac{a^3\sqrt{2}}{12}
$$

---

## 📖 El Cubo (Hexaedro)

- **Caras:** 6 cuadrados
- **Vértices:** 8
- **Aristas:** 12
- **Caras por vértice:** 3

### Fórmulas (arista $a$)

$$
A = 6a^2
$$

$$
V = a^3
$$

---

## 📖 El Octaedro

- **Caras:** 8 triángulos equiláteros
- **Vértices:** 6
- **Aristas:** 12
- **Caras por vértice:** 4

### Fórmulas (arista $a$)

$$
A = 2a^2\sqrt{3}
$$

$$
V = \frac{a^3\sqrt{2}}{3}
$$

---

## 📖 El Dodecaedro

- **Caras:** 12 pentágonos regulares
- **Vértices:** 20
- **Aristas:** 30
- **Caras por vértice:** 3

Es el poliedro regular más cercano a una esfera.

---

## 📖 El Icosaedro

- **Caras:** 20 triángulos equiláteros
- **Vértices:** 12
- **Aristas:** 30
- **Caras por vértice:** 5

Es el poliedro regular con más caras.

---

## 📖 Verificación con fórmula de Euler

Para todos los poliedros regulares:

$$
V - A + C = 2
$$

| Poliedro | V | A | C | V - A + C |
|----------|---|---|---|-----------|
| Tetraedro | 4 | 6 | 4 | 2 ✓ |
| Cubo | 8 | 12 | 6 | 2 ✓ |
| Octaedro | 6 | 12 | 8 | 2 ✓ |
| Dodecaedro | 20 | 30 | 12 | 2 ✓ |
| Icosaedro | 12 | 30 | 20 | 2 ✓ |

---

## 📖 Poliedros duales

Cada poliedro regular tiene un **dual**:

| Poliedro | Dual |
|----------|------|
| Tetraedro | Tetraedro (auto-dual) |
| Cubo | Octaedro |
| Octaedro | Cubo |
| Dodecaedro | Icosaedro |
| Icosaedro | Dodecaedro |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar

¿Qué poliedro regular tiene...?

1. 4 caras triangulares
2. 6 caras cuadradas
3. 20 caras triangulares
4. 12 caras pentagonales

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Tetraedro**
2. **Cubo**
3. **Icosaedro**
4. **Dodecaedro**

</details>

---

### Ejercicio 2: Fórmula de Euler

Verifica la fórmula de Euler para el dodecaedro (20 vértices, 30 aristas, 12 caras).

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
V - A + C = 20 - 30 + 12 = 2 \quad ✓
$$

</details>

---

### Ejercicio 3: Cubo

Un cubo tiene arista de 4 cm. Calcula:

1. Área total
2. Volumen

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = 6(16) = 96$ cm²
2. $V = 64$ cm³

</details>

---

### Ejercicio 4: Contar elementos

El octaedro tiene 8 caras y 6 vértices. ¿Cuántas aristas tiene?

<details>
<summary><strong>Ver respuesta</strong></summary>

Usando $V - A + C = 2$:

$$
6 - A + 8 = 2
$$

$$
A = 12 \text{ aristas}
$$

</details>

---

### Ejercicio 5: Verdadero o Falso

1. Existen infinitos poliedros regulares.
2. El tetraedro es su propio dual.
3. El cubo y el octaedro tienen el mismo número de aristas.
4. El icosaedro tiene todas sus caras triangulares.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** - Solo existen 5
2. **Verdadero**
3. **Verdadero** - Ambos tienen 12 aristas
4. **Verdadero**

</details>

---
