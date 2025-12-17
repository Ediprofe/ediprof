# El Cubo

El **cubo** es el prisma más simétrico: todas sus caras son cuadrados iguales. Es uno de los cinco **sólidos platónicos**.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-cubo" width="700" height="280" style="width: 100%; height: auto; display: block;"></canvas>
  <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 0.75rem; font-size: 0.9rem; flex-wrap: wrap;">
    <span><strong style="color: #22c55e;">a</strong> = arista (lado)</span>
    <span><strong style="color: #a855f7;">D</strong> = diagonal espacial = a√3</span>
    <span><strong style="color: #64748b;">d</strong> = diagonal de cara = a√2</span>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-cubo')) {
    var canvas = document.getElementById('roughjs-cubo');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('El Cubo: Elementos y Fórmulas', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    var morado = '#a855f7';
    
    // Cubo isométrico grande
    var cx = 150, cy = 150;
    var a = 100; // arista
    var dx = a * 0.5, dy = a * 0.3; // desplazamiento isométrico
    
    // Vértices
    var v1 = [cx, cy];
    var v2 = [cx + a, cy];
    var v3 = [cx + a, cy + a];
    var v4 = [cx, cy + a];
    var v5 = [cx + dx, cy - dy];
    var v6 = [cx + a + dx, cy - dy];
    var v7 = [cx + a + dx, cy + a - dy];
    var v8 = [cx + dx, cy + a - dy];
    
    // Cara frontal
    rc.polygon([v1, v2, v3, v4], {fill: '#dbeafe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    // Cara superior
    rc.polygon([v1, v5, v6, v2], {fill: '#bfdbfe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    // Cara lateral derecha
    rc.polygon([v2, v6, v7, v3], {fill: '#93c5fd', stroke: azul, strokeWidth: 2, roughness: 0.5});
    
    // Arista etiquetada
    rc.line(v1[0], v1[1], v2[0], v2[1], {stroke: verde, strokeWidth: 3, roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('a', cx + a/2, cy + 20);
    
    // Diagonal espacial (punteada)
    ctx.setLineDash([5, 5]);
    ctx.strokeStyle = morado;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(v4[0], v4[1]);
    ctx.lineTo(v6[0], v6[1]);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = morado;
    ctx.font = '12px Inter, sans-serif';
    ctx.fillText('D = a√3', cx + a + 30, cy + 30);
    
    // Fórmulas
    rc.rectangle(380, 60, 290, 200, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Fórmulas del Cubo', 525, 90);
    
    ctx.font = '13px Inter, sans-serif';
    ctx.textAlign = 'left';
    
    ctx.fillStyle = verde;
    ctx.fillText('Arista:', 400, 120);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('a', 480, 120);
    
    ctx.fillStyle = azul;
    ctx.fillText('Área total:', 400, 150);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A = 6a²', 480, 150);
    
    ctx.fillStyle = rojo;
    ctx.fillText('Volumen:', 400, 180);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('V = a³', 480, 180);
    
    ctx.fillStyle = morado;
    ctx.fillText('Diagonal espacial:', 400, 210);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('D = a√3', 530, 210);
    
    ctx.fillStyle = '#64748b';
    ctx.fillText('Diagonal de cara:', 400, 240);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('d = a√2', 530, 240);
  }
});
</script>

---

## 📖 Definición

> **Definición:** Un cubo (o hexaedro regular) es un poliedro con **6 caras cuadradas iguales**, **12 aristas iguales** y **8 vértices**.

---

## 📖 Elementos del cubo

| Elemento | Cantidad | Descripción |
|----------|----------|-------------|
| Caras | 6 | Cuadrados iguales |
| Aristas | 12 | Todas de igual longitud |
| Vértices | 8 | Donde se unen 3 aristas |
| Diagonales de cara | 12 | 2 por cada cara |
| Diagonales espaciales | 4 | Unen vértices opuestos |

---

## 📖 Fórmulas del cubo

Sea $a$ el lado del cubo:

### Área de una cara

$$
A_{cara} = a^2
$$

### Área total (superficie)

$$
A_T = 6a^2
$$

### Volumen

$$
V = a^3
$$

### Diagonal de una cara

$$
d_{cara} = a\sqrt{2}
$$

### Diagonal espacial

$$
D = a\sqrt{3}
$$

---

## 📖 Ejemplos

### Ejemplo 1

Cubo de arista 5 cm:

$$
A_T = 6 \times 5^2 = 6 \times 25 = 150 \text{ cm}^2
$$

$$
V = 5^3 = 125 \text{ cm}^3
$$

$$
D = 5\sqrt{3} \approx 8.66 \text{ cm}
$$

### Ejemplo 2

Cubo de arista 10 cm:

$$
A_T = 6 \times 100 = 600 \text{ cm}^2
$$

$$
V = 1000 \text{ cm}^3 = 1 \text{ litro}
$$

---

## 📖 Encontrar la arista

### Conociendo el volumen

$$
a = \sqrt[3]{V}
$$

### Conociendo el área total

$$
a = \sqrt{\frac{A_T}{6}}
$$

---

## 📖 Propiedades especiales

### Simetría

El cubo tiene:
- 9 planos de simetría
- 13 ejes de simetría
- Es un poliedro regular (sólido platónico)

### Desarrollo plano

El cubo se puede desplegar en 11 formas diferentes (redes del cubo).

### Relación con el ortoedro

El cubo es un caso especial de ortoedro (prisma rectangular) donde todas las dimensiones son iguales.

---

## 📖 Aplicaciones

| Objeto | Uso del cubo |
|--------|--------------|
| Dados | Juegos |
| Cajas | Embalaje |
| Cubos de Rubik | Puzzles |
| Edificios | Arquitectura moderna |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Área y volumen

Calcula el área total y el volumen de cubos con arista:

1. 3 cm
2. 7 cm
3. 12 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A_T = 6 \times 9 = 54$ cm², $V = 27$ cm³
2. $A_T = 6 \times 49 = 294$ cm², $V = 343$ cm³
3. $A_T = 6 \times 144 = 864$ cm², $V = 1728$ cm³

</details>

---

### Ejercicio 2: Diagonal espacial

Calcula la diagonal espacial de cubos con arista:

1. 4 cm
2. 6 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $D = 4\sqrt{3} \approx 6.93$ cm
2. $D = 6\sqrt{3} \approx 10.39$ cm

</details>

---

### Ejercicio 3: Encontrar la arista

1. El volumen de un cubo es 64 cm³. ¿Cuál es la arista?
2. El área total de un cubo es 150 cm². ¿Cuál es la arista?

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $a = \sqrt[3]{64} = 4$ cm
2. $a = \sqrt{\frac{150}{6}} = \sqrt{25} = 5$ cm

</details>

---

### Ejercicio 4: Problema aplicado

Un tanque cúbico tiene arista de 2 m. ¿Cuántos litros de agua puede contener? (1 m³ = 1000 litros)

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
V = 2^3 = 8 \text{ m}^3 = 8 \times 1000 = 8000 \text{ litros}
$$

</details>

---

### Ejercicio 5: Comparación

Si duplicamos la arista de un cubo, ¿en cuánto se multiplica el volumen?

<details>
<summary><strong>Ver respuesta</strong></summary>

Arista original: $a$, Volumen: $a^3$

Arista doble: $2a$, Volumen: $(2a)^3 = 8a^3$

El volumen se multiplica por **8**.

</details>

---
