# Conceptos Básicos de Perímetro y Área

El **perímetro** y el **área** son dos medidas fundamentales de las figuras geométricas. Aunque pueden confundirse, miden cosas muy diferentes.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-perimetro-area" width="700" height="300" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-perimetro-area')) {
    var canvas = document.getElementById('roughjs-perimetro-area');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Perímetro vs Área', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    
    // === PERÍMETRO (izquierda) ===
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = azul;
    ctx.fillText('PERÍMETRO', 175, 55);
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('= Longitud del contorno', 175, 72);
    
    // Rectángulo con borde grueso (perímetro)
    rc.rectangle(75, 90, 200, 120, {fill: 'transparent', stroke: azul, strokeWidth: 6, roughness: 0.5});
    
    // Etiquetas de lados
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = azul;
    ctx.fillText('5 m', 175, 85);
    ctx.fillText('5 m', 175, 225);
    ctx.fillText('3 m', 60, 150);
    ctx.fillText('3 m', 290, 150);
    
    // Fórmula
    ctx.font = '13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('P = 5 + 3 + 5 + 3 = 16 m', 175, 255);
    
    // Analogía
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('📏 Como la cerca del jardín', 175, 280);
    
    // === ÁREA (derecha) ===
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.textAlign = 'center';
    ctx.fillText('ÁREA', 525, 55);
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('= Superficie interior', 525, 72);
    
    // Rectángulo relleno (área)
    rc.rectangle(425, 90, 200, 120, {fill: '#dcfce7', fillStyle: 'solid', stroke: verde, strokeWidth: 2, roughness: 0.5});
    
    // Cuadrícula interior para mostrar unidades cuadradas
    for (var i = 0; i < 5; i++) {
      for (var j = 0; j < 3; j++) {
        rc.rectangle(425 + i*40, 90 + j*40, 40, 40, {stroke: '#86efac', strokeWidth: 1, roughness: 0.2});
      }
    }
    
    // Etiquetas
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('5 m', 525, 85);
    ctx.fillText('3 m', 410, 150);
    
    // Fórmula
    ctx.font = '13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A = 5 × 3 = 15 m²', 525, 255);
    
    // Analogía
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('🌿 Como el césped del jardín', 525, 280);
  }
});
</script>

---

## 📖 ¿Qué es el perímetro?

> **Definición:** El perímetro es la **longitud total del contorno** de una figura. Es la suma de todos sus lados.

### Unidades

El perímetro se mide en unidades de **longitud**:
- Centímetros (cm)
- Metros (m)
- Kilómetros (km)

### Ejemplo

Un rectángulo con lados de 5 m y 3 m:

$$
P = 5 + 3 + 5 + 3 = 16 \text{ m}
$$

---

## 📖 ¿Qué es el área?

> **Definición:** El área es la **cantidad de superficie** que ocupa una figura. Es la medida de la región interior.

### Unidades

El área se mide en unidades de **superficie** (unidades al cuadrado):
- Centímetros cuadrados (cm²)
- Metros cuadrados (m²)
- Kilómetros cuadrados (km²)

### Ejemplo

Un cuadrado de lado 4 cm:

$$
A = 4 \times 4 = 16 \text{ cm}^2
$$

---

## 📖 Diferencia entre perímetro y área

| Característica | Perímetro | Área |
|----------------|-----------|------|
| ¿Qué mide? | Contorno (borde) | Superficie (interior) |
| Dimensión | Longitud (1D) | Superficie (2D) |
| Unidades | cm, m, km | cm², m², km² |
| Analogía | Longitud de cerca | Pasto del jardín |

### Analogía del jardín

Imagina un jardín rectangular:
- **Perímetro** = longitud de la cerca que lo rodea
- **Área** = cantidad de césped dentro del jardín

---

## 📖 Conversión de unidades de longitud

| De | A | Operación |
|----|---|-----------|
| km | m | × 1,000 |
| m | cm | × 100 |
| cm | mm | × 10 |
| m | km | ÷ 1,000 |
| cm | m | ÷ 100 |

### Ejemplo

5 km = 5 × 1,000 = 5,000 m

---

## 📖 Conversión de unidades de área

| De | A | Operación |
|----|---|-----------|
| km² | m² | × 1,000,000 |
| m² | cm² | × 10,000 |
| cm² | mm² | × 100 |
| m² | km² | ÷ 1,000,000 |
| cm² | m² | ÷ 10,000 |

### ¿Por qué se eleva al cuadrado?

Si 1 m = 100 cm, entonces:

$$
1 \text{ m}^2 = (100 \text{ cm})^2 = 10,000 \text{ cm}^2
$$

### Ejemplo

3 m² = 3 × 10,000 = 30,000 cm²

---

## 📖 Unidades especiales de área

| Unidad | Equivalencia |
|--------|--------------|
| 1 hectárea (ha) | 10,000 m² |
| 1 km² | 100 hectáreas |
| 1 área (a) | 100 m² |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar

¿Se refiere al perímetro o al área?

1. La cantidad de pintura para cubrir una pared
2. La longitud de cinta para envolver un regalo
3. El tamaño de un terreno para construir
4. La cerca para rodear un jardín

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Área**
2. **Perímetro**
3. **Área**
4. **Perímetro**

</details>

---

### Ejercicio 2: Unidades correctas

Indica las unidades correctas:

1. El perímetro de una mesa es 240 ___
2. El área de una cancha es 1,500 ___
3. El contorno de un libro es 80 ___

<details>
<summary><strong>Ver respuestas</strong></summary>

1. 240 **cm** (o m, pero no cm²)
2. 1,500 **m²** (o cm², pero no m)
3. 80 **cm** (o mm)

</details>

---

### Ejercicio 3: Conversiones de longitud

Convierte:

1. 2.5 km a metros
2. 350 cm a metros
3. 4,500 m a kilómetros

<details>
<summary><strong>Ver respuestas</strong></summary>

1. 2.5 × 1,000 = **2,500 m**
2. 350 ÷ 100 = **3.5 m**
3. 4,500 ÷ 1,000 = **4.5 km**

</details>

---

### Ejercicio 4: Conversiones de área

Convierte:

1. 5 m² a cm²
2. 80,000 cm² a m²
3. 2 hectáreas a m²

<details>
<summary><strong>Ver respuestas</strong></summary>

1. 5 × 10,000 = **50,000 cm²**
2. 80,000 ÷ 10,000 = **8 m²**
3. 2 × 10,000 = **20,000 m²**

</details>

---

### Ejercicio 5: Verdadero o Falso

1. El perímetro se mide en metros cuadrados.
2. 1 m² = 100 cm².
3. El área mide la superficie interior de una figura.
4. Una hectárea equivale a 10,000 m².

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** - Se mide en metros (sin cuadrado)
2. **Falso** - 1 m² = 10,000 cm²
3. **Verdadero**
4. **Verdadero**

</details>

---
