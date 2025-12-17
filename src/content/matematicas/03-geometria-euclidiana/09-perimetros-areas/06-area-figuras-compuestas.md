# Área de Figuras Compuestas

Las **figuras compuestas** son aquellas formadas por la unión o diferencia de figuras simples. Para calcular su área, las descomponemos en partes conocidas.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-figuras-compuestas" width="700" height="300" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-figuras-compuestas')) {
    var canvas = document.getElementById('roughjs-figuras-compuestas');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Figuras Compuestas: Suma y Resta de Áreas', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    
    // === FIGURA EN L (SUMA) - izquierda ===
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('SUMA DE ÁREAS', 150, 55);
    
    // Rectángulo vertical
    rc.rectangle(80, 70, 60, 150, {fill: '#dcfce7', fillStyle: 'solid', stroke: verde, strokeWidth: 2, roughness: 0.5});
    // Rectángulo horizontal
    rc.rectangle(80, 160, 140, 60, {fill: '#bbf7d0', fillStyle: 'solid', stroke: verde, strokeWidth: 2, roughness: 0.5});
    
    // Etiquetas
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('A₁', 110, 115);
    ctx.fillText('A₂', 180, 195);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('A = A₁ + A₂', 150, 255);
    
    // === CORONA CIRCULAR (RESTA) - derecha ===
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = rojo;
    ctx.textAlign = 'center';
    ctx.fillText('RESTA DE ÁREAS', 530, 55);
    
    // Círculo grande
    rc.circle(530, 160, 140, {fill: '#fecaca', fillStyle: 'solid', stroke: rojo, strokeWidth: 2, roughness: 0.5});
    // Círculo pequeño (hueco) - simulado con blanco
    rc.circle(530, 160, 70, {fill: '#f8fafc', fillStyle: 'solid', stroke: rojo, strokeWidth: 2, roughness: 0.5});
    
    // Etiquetas
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('R', 530, 100);
    ctx.fillText('r', 530, 140);
    
    // Líneas de radio
    rc.line(530, 160, 530, 90, {stroke: rojo, strokeWidth: 1.5, roughness: 0.3});
    rc.line(530, 160, 530, 125, {stroke: '#64748b', strokeWidth: 1.5, roughness: 0.3});
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = rojo;
    ctx.fillText('A = πR² - πr²', 530, 255);
    
    // === Fórmula central ===
    rc.rectangle(280, 100, 140, 80, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Estrategia', 350, 125);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = verde;
    ctx.fillText('Unión → SUMAR', 350, 150);
    ctx.fillStyle = rojo;
    ctx.fillText('Hueco → RESTAR', 350, 170);
  }
});
</script>

---

## 📖 ¿Qué es una figura compuesta?

Una figura compuesta está formada por:
- **Unión** de figuras simples (suma de áreas)
- **Diferencia** de figuras (resta de áreas)
- Combinación de ambas operaciones

---

## 📖 Estrategia general

### Paso 1: Identificar las figuras simples
Reconocer qué figuras básicas componen la figura total.

### Paso 2: Calcular áreas individuales
Usar las fórmulas correspondientes para cada figura.

### Paso 3: Sumar o restar
- Si las figuras están **unidas**: sumar
- Si una figura está **recortada** de otra: restar

---

## 📖 Figuras por adición (suma)

Cuando una figura se forma **uniendo** varias figuras.

### Ejemplo 1: L invertida

Una figura en forma de L se puede ver como dos rectángulos unidos:

$$
A_{total} = A_{rectángulo 1} + A_{rectángulo 2}
$$

### Ejemplo 2: Casa

Una casa se puede ver como un rectángulo (cuerpo) + triángulo (techo):

$$
A_{casa} = A_{rectángulo} + A_{triángulo}
$$

---

## 📖 Figuras por sustracción (resta)

Cuando una figura se forma **recortando** una figura de otra.

### Ejemplo 1: Arandela

Un anillo (corona circular):

$$
A_{anillo} = A_{círculo grande} - A_{círculo pequeño} = \pi R^2 - \pi r^2
$$

### Ejemplo 2: Marco de cuadro

$$
A_{marco} = A_{rectángulo exterior} - A_{rectángulo interior}
$$

---

## 📖 Ejemplos resueltos

### Ejemplo 1: Figura en L

Una L con medidas: parte vertical 8×3 cm, parte horizontal 6×3 cm, con superposición de 3×3 cm.

**Método 1 (Suma sin superposición):**

$$
A = (8 \times 3) + (6 \times 3) - (3 \times 3) = 24 + 18 - 9 = 33 \text{ cm}^2
$$

**Método 2 (Dividir en dos rectángulos sin superposición):**

Parte vertical: 8 × 3 = 24 cm²
Parte horizontal: (6-3) × 3 = 9 cm²

$$
A = 24 + 9 = 33 \text{ cm}^2
$$

### Ejemplo 2: Rectángulo con semicírculo

Rectángulo de 10 × 6 cm con un semicírculo de radio 3 cm añadido en un lado:

$$
A = (10 \times 6) + \frac{\pi \times 3^2}{2} = 60 + \frac{9\pi}{2} \approx 60 + 14.14 = 74.14 \text{ cm}^2
$$

### Ejemplo 3: Cuadrado con agujero circular

Cuadrado de lado 10 cm con un círculo de radio 2 cm recortado:

$$
A = 10^2 - \pi \times 2^2 = 100 - 4\pi \approx 100 - 12.57 = 87.43 \text{ cm}^2
$$

---

## 📖 Consejos prácticos

1. **Dibuja** la figura y marca las dimensiones
2. **Divide** la figura en partes reconocibles
3. **Verifica** que no cuentes áreas dobles
4. **Revisa** si debes sumar o restar

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Figura en T

Una T formada por:
- Parte horizontal: 12 × 3 cm
- Parte vertical: 8 × 4 cm (centrada debajo)

Calcula el área total (sin superposición de 3×4).

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A = (12 \times 3) + (8 \times 4) - (3 \times 4) = 36 + 32 - 12 = 56 \text{ cm}^2
$$

O dividiendo correctamente: Horizontal completa + vertical (8-3)×4

$$
A = 36 + 20 = 56 \text{ cm}^2
$$

</details>

---

### Ejercicio 2: Corona circular

Círculo exterior de radio 8 cm con agujero circular de radio 5 cm.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A = \pi(8^2) - \pi(5^2) = \pi(64 - 25) = 39\pi \approx 122.5 \text{ cm}^2
$$

</details>

---

### Ejercicio 3: Marco rectangular

Rectángulo exterior de 20 × 15 cm con rectángulo interior de 16 × 11 cm.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A = (20 \times 15) - (16 \times 11) = 300 - 176 = 124 \text{ cm}^2
$$

</details>

---

### Ejercicio 4: Casa

Rectángulo de 8 × 6 m con triángulo encima (base 8 m, altura 3 m).

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A = (8 \times 6) + \frac{8 \times 3}{2} = 48 + 12 = 60 \text{ m}^2
$$

</details>

---

### Ejercicio 5: Estadio

Rectángulo de 100 × 60 m con semicírculos en los extremos (radio 30 m cada uno).

<details>
<summary><strong>Ver respuesta</strong></summary>

Los dos semicírculos forman un círculo completo de radio 30 m.

$$
A = (100 \times 60) + \pi(30)^2 = 6000 + 900\pi \approx 6000 + 2827 = 8827 \text{ m}^2
$$

</details>

---
