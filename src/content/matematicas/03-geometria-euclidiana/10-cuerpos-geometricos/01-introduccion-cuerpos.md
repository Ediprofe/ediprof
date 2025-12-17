# Introducción a los Cuerpos Geométricos

Los **cuerpos geométricos** son figuras tridimensionales (3D). A diferencia de las figuras planas que tienen largo y ancho, los cuerpos tienen también **profundidad** (o altura).

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-cuerpos-intro" width="700" height="280" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-cuerpos-intro')) {
    var canvas = document.getElementById('roughjs-cuerpos-intro');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Poliedros vs Cuerpos Redondos', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    
    // === POLIEDROS (izquierda) ===
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = azul;
    ctx.fillText('POLIEDROS', 175, 55);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('(caras planas)', 175, 70);
    
    // Cubo isométrico (3 caras visibles)
    var cx = 100, cy = 130;
    var s = 55;
    var dx = 25, dy = 15; // desplazamiento isométrico
    
    // Vértices del cubo
    var v1 = [cx, cy];           // frontal izq arriba
    var v2 = [cx + s, cy];       // frontal der arriba
    var v3 = [cx + s, cy + s];   // frontal der abajo
    var v4 = [cx, cy + s];       // frontal izq abajo
    var v5 = [cx + dx, cy - dy];         // trasero izq arriba
    var v6 = [cx + s + dx, cy - dy];     // trasero der arriba
    var v7 = [cx + s + dx, cy + s - dy]; // trasero der abajo
    
    // Cara frontal
    rc.polygon([v1, v2, v3, v4], {fill: '#dbeafe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    // Cara superior
    rc.polygon([v1, v5, v6, v2], {fill: '#bfdbfe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    // Cara lateral derecha
    rc.polygon([v2, v6, v7, v3], {fill: '#93c5fd', stroke: azul, strokeWidth: 2, roughness: 0.5});
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = azul;
    ctx.fillText('Cubo', 130, 235);
    
    // Pirámide isométrica
    var px = 230, py = 200;
    // Base
    rc.polygon([[px, py], [px+40, py-15], [px+60, py+10], [px+20, py+25]], {fill: '#dbeafe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    // Caras laterales
    rc.polygon([[px, py], [px+30, py-60], [px+40, py-15]], {fill: '#bfdbfe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    rc.polygon([[px+40, py-15], [px+30, py-60], [px+60, py+10]], {fill: '#93c5fd', stroke: azul, strokeWidth: 2, roughness: 0.5});
    rc.polygon([[px+60, py+10], [px+30, py-60], [px+20, py+25]], {fill: '#dbeafe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    ctx.fillText('Pirámide', 250, 235);
    
    // === CUERPOS REDONDOS (derecha) ===
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('CUERPOS REDONDOS', 525, 55);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('(superficies curvas)', 525, 70);
    
    // Cilindro
    var clx = 420, cly = 150;
    // Cuerpo
    rc.rectangle(clx, cly, 60, 80, {fill: '#dcfce7', stroke: verde, strokeWidth: 2, roughness: 0.5});
    // Tapa superior (elipse)
    rc.ellipse(clx+30, cly, 60, 20, {fill: '#bbf7d0', stroke: verde, strokeWidth: 2, roughness: 0.5});
    // Tapa inferior (elipse)
    rc.ellipse(clx+30, cly+80, 60, 20, {fill: '#dcfce7', stroke: verde, strokeWidth: 2, roughness: 0.5});
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('Cilindro', 450, 255);
    
    // Esfera
    rc.circle(570, 170, 80, {fill: '#dcfce7', stroke: verde, strokeWidth: 2, roughness: 0.5});
    // Línea ecuatorial
    rc.ellipse(570, 170, 80, 25, {stroke: verde, strokeWidth: 1, roughness: 0.3});
    ctx.fillText('Esfera', 570, 255);
    
    // Cono
    var cox = 630, coy = 200;
    // Cuerpo del cono
    rc.polygon([[cox, coy], [cox+30, coy-80], [cox+60, coy]], {fill: '#dcfce7', stroke: verde, strokeWidth: 2, roughness: 0.5});
    // Base elíptica
    rc.ellipse(cox+30, coy, 60, 18, {fill: '#bbf7d0', stroke: verde, strokeWidth: 2, roughness: 0.5});
    ctx.fillText('Cono', 660, 255);
  }
});
</script>

---

## 📖 ¿Qué es un cuerpo geométrico?

> **Definición:** Un cuerpo geométrico es una figura que ocupa un lugar en el espacio y tiene tres dimensiones: **largo**, **ancho** y **alto** (o profundidad).

### Diferencia con figuras planas

| Característica | Figura plana | Cuerpo geométrico |
|----------------|--------------|-------------------|
| Dimensiones | 2 (largo, ancho) | 3 (largo, ancho, alto) |
| Medidas | Perímetro, área | Área superficial, volumen |
| Ejemplos | Cuadrado, círculo | Cubo, esfera |

---

## 📖 Clasificación de cuerpos geométricos

### Poliedros

Cuerpos limitados por **superficies planas** (caras poligonales).

- Caras: polígonos
- Aristas: segmentos donde se unen las caras
- Vértices: puntos donde se unen las aristas

**Ejemplos:** cubo, pirámide, prisma

### Cuerpos redondos (o de revolución)

Cuerpos que tienen **superficies curvas**.

**Ejemplos:** esfera, cilindro, cono

---

## 📖 Elementos de los cuerpos geométricos

| Elemento | Descripción |
|----------|-------------|
| Caras | Superficies que limitan el cuerpo |
| Aristas | Líneas donde se unen dos caras |
| Vértices | Puntos donde se unen tres o más aristas |
| Base | Cara(s) sobre la(s) que se apoya el cuerpo |
| Altura | Distancia perpendicular entre bases o desde la base al vértice |

---

## 📖 Fórmula de Euler para poliedros

Para cualquier poliedro convexo:

$$
V - A + C = 2
$$

Donde:
- $V$ = número de vértices
- $A$ = número de aristas
- $C$ = número de caras

### Ejemplo: Cubo

- Vértices: 8
- Aristas: 12
- Caras: 6

$$
8 - 12 + 6 = 2 \quad ✓
$$

---

## 📖 Medidas de los cuerpos geométricos

### Área superficial

La **superficie total** del cuerpo (la "piel" que lo recubre).

$$
\text{Área superficial} = \text{suma de las áreas de todas las caras}
$$

### Volumen

El **espacio interior** que ocupa el cuerpo.

Se mide en unidades cúbicas: cm³, m³, etc.

---

## 📖 Cuerpos geométricos comunes

| Cuerpo | Tipo | Características |
|--------|------|-----------------|
| Cubo | Poliedro | 6 caras cuadradas iguales |
| Prisma | Poliedro | 2 bases iguales, caras laterales rectangulares |
| Pirámide | Poliedro | 1 base, caras laterales triangulares |
| Cilindro | Redondo | 2 bases circulares |
| Cono | Redondo | 1 base circular, vértice |
| Esfera | Redondo | Superficie curva uniforme |

---

## 📖 Desarrollos planos

El **desarrollo** de un cuerpo es la figura plana que se obtiene al "abrirlo" o "desplegarlo".

### Ejemplo: Cubo

El desarrollo de un cubo son 6 cuadrados dispuestos en forma de cruz (u otra configuración equivalente).

### Utilidad

- Calcular el área superficial
- Construir maquetas

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificar

Clasifica cada cuerpo como poliedro o cuerpo redondo:

1. Pirámide
2. Esfera
3. Prisma hexagonal
4. Cono
5. Cubo

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Poliedro**
2. **Cuerpo redondo**
3. **Poliedro**
4. **Cuerpo redondo**
5. **Poliedro**

</details>

---

### Ejercicio 2: Fórmula de Euler

Verifica la fórmula de Euler para:

1. Tetraedro (4 caras, 6 aristas, 4 vértices)
2. Pirámide cuadrada (5 caras, 8 aristas, 5 vértices)

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $V - A + C = 4 - 6 + 4 = 2$ ✓
2. $V - A + C = 5 - 8 + 5 = 2$ ✓

</details>

---

### Ejercicio 3: Identificar elementos

¿Cuántas caras, aristas y vértices tiene un prisma triangular?

<details>
<summary><strong>Ver respuesta</strong></summary>

- **Caras:** 5 (2 triángulos + 3 rectángulos)
- **Aristas:** 9
- **Vértices:** 6

Verificación: $6 - 9 + 5 = 2$ ✓

</details>

---

### Ejercicio 4: Verdadero o Falso

1. El cilindro es un poliedro.
2. El cubo tiene 8 vértices.
3. La esfera no tiene vértices ni aristas.
4. La pirámide tiene dos bases.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** - Es un cuerpo redondo
2. **Verdadero**
3. **Verdadero** - Es completamente curva
4. **Falso** - Tiene una sola base

</details>

---
