# Introducción a las Transformaciones Geométricas

Las **transformaciones geométricas** son operaciones que cambian la posición, tamaño u orientación de las figuras en el plano, preservando ciertas propiedades.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-intro-panorama" width="800" height="350" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-intro-panorama')) {
    var canvas = document.getElementById('roughjs-intro-panorama');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Las 4 Transformaciones Principales', 400, 25);
    
    // Colores
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    var morado = '#a855f7';
    
    // 1. TRASLACIÓN (arriba izquierda)
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = azul;
    ctx.fillText('TRASLACIÓN', 120, 60);
    
    // Triángulo original
    rc.polygon([[60,120], [100,120], [80,80]], {fill: '#dbeafe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    // Flecha
    rc.line(110, 100, 150, 100, {stroke: '#64748b', strokeWidth: 2, roughness: 0.3});
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('→', 155, 104);
    // Triángulo imagen
    rc.polygon([[140,120], [180,120], [160,80]], {fill: '#dcfce7', stroke: verde, strokeWidth: 2, roughness: 0.5});
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.textAlign = 'center';
    ctx.fillText('Misma dirección', 120, 145);
    ctx.fillText('y distancia', 120, 160);
    
    // 2. ROTACIÓN (arriba derecha)
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = rojo;
    ctx.textAlign = 'center';
    ctx.fillText('ROTACIÓN', 320, 60);
    
    // Triángulo original
    rc.polygon([[280,120], [320,120], [300,80]], {fill: '#dbeafe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    // Centro de rotación
    rc.circle(300, 120, 8, {fill: rojo, stroke: rojo, roughness: 0.3});
    // Arco de rotación
    rc.arc(300, 120, 60, 60, -Math.PI/2, 0, false, {stroke: rojo, strokeWidth: 1.5, roughness: 0.3});
    // Triángulo rotado
    rc.polygon([[300,100], [300,140], [340,120]], {fill: '#dcfce7', stroke: verde, strokeWidth: 2, roughness: 0.5});
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Giro alrededor', 320, 155);
    ctx.fillText('de un centro', 320, 170);
    
    // 3. REFLEXIÓN (abajo izquierda)
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = morado;
    ctx.fillText('REFLEXIÓN', 520, 60);
    
    // Eje de simetría
    rc.line(520, 70, 520, 150, {stroke: morado, strokeWidth: 2, roughness: 0.3});
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = morado;
    ctx.fillText('eje', 535, 80);
    // Triángulo original
    rc.polygon([[470,120], [510,120], [490,80]], {fill: '#dbeafe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    // Triángulo reflejado
    rc.polygon([[530,120], [570,120], [550,80]], {fill: '#dcfce7', stroke: verde, strokeWidth: 2, roughness: 0.5});
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Imagen espejo', 520, 165);
    
    // 4. HOMOTECIA (abajo derecha)
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('HOMOTECIA', 720, 60);
    
    // Centro
    rc.circle(680, 130, 8, {fill: '#f59e0b', stroke: '#f59e0b', roughness: 0.3});
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('O', 668, 135);
    // Triángulo pequeño (original)
    rc.polygon([[700,130], [720,130], [710,110]], {fill: '#dbeafe', stroke: azul, strokeWidth: 2, roughness: 0.5});
    // Triángulo grande (imagen)
    rc.polygon([[720,140], [760,140], [740,100]], {fill: '#dcfce7', stroke: verde, strokeWidth: 2, roughness: 0.5});
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.textAlign = 'center';
    ctx.fillText('Ampliación o', 720, 160);
    ctx.fillText('reducción', 720, 175);
    
    // Leyenda
    ctx.font = '12px Inter, sans-serif';
    ctx.textAlign = 'left';
    rc.rectangle(250, 200, 300, 60, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.fillStyle = azul;
    ctx.fillText('■ Original', 270, 225);
    ctx.fillStyle = verde;
    ctx.fillText('■ Imagen', 370, 225);
    ctx.fillStyle = '#64748b';
    ctx.fillText('Las isometrías conservan tamaño y forma', 270, 245);
  }
});
</script>

---

## 📖 ¿Qué es una transformación geométrica?

> **Definición:** Una transformación geométrica es una regla que asigna a cada punto del plano un nuevo punto, llamado su **imagen**.

Si el punto $P$ se transforma en $P'$:
- $P$ es el **original** (o preimagen)
- $P'$ es la **imagen**

---

## 📖 Tipos de transformaciones

### Por conservación de tamaño

| Tipo | ¿Conserva tamaño? | ¿Conserva forma? |
|------|-------------------|------------------|
| Isometría | Sí | Sí |
| Semejanza | No | Sí |
| Otras | No | No |

### Isometrías (movimientos rígidos)

Las **isometrías** conservan la forma y el tamaño de la figura:
- Traslación
- Rotación
- Reflexión (simetría)

### Semejanzas

Las **semejanzas** conservan solo la forma:
- Homotecia (ampliación/reducción)
- Composición de isometrías con homotecia

---

## 📖 Propiedades que conservan las isometrías

| Propiedad | ¿Se conserva? |
|-----------|---------------|
| Distancias | Sí |
| Ángulos | Sí |
| Paralelismo | Sí |
| Perpendicularidad | Sí |
| Área | Sí |
| Forma | Sí |

---

## 📖 Las cuatro transformaciones principales

### 1. Traslación

Mueve todos los puntos la **misma distancia** en la **misma dirección**.

### 2. Rotación

Gira todos los puntos alrededor de un **centro** un **cierto ángulo**.

### 3. Reflexión (Simetría)

Refleja los puntos respecto a una **recta eje** (como en un espejo).

### 4. Homotecia

Amplía o reduce la figura desde un **centro** con una **razón** dada.

---

## 📖 Notación

Para indicar que aplicamos una transformación $T$ a un punto $P$:

$$
T(P) = P'
$$

Para una figura $F$:

$$
T(F) = F'
$$

---

## 📖 Composición de transformaciones

Podemos aplicar una transformación después de otra. Si aplicamos $T_1$ y luego $T_2$:

$$
(T_2 \circ T_1)(P) = T_2(T_1(P))
$$

Se lee: "Primero $T_1$, luego $T_2$"

### Ejemplo

Rotar 90° y luego trasladar es diferente de trasladar y luego rotar 90°.

> **Nota:** En general, el orden importa.

---

## 📖 Elementos invariantes

Un **punto invariante** (o fijo) es un punto que no cambia con la transformación:

$$
T(P) = P
$$

### Ejemplos

- En una **rotación**: solo el centro es invariante
- En una **reflexión**: todos los puntos del eje son invariantes
- En una **traslación**: ningún punto es invariante (excepto si el vector es cero)

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificar transformaciones

¿Cuál transformación se aplicó?

1. Una figura se movió 5 cm a la derecha sin girar ni cambiar de tamaño
2. Una figura giró 90° alrededor de un punto
3. Una figura se ve como en un espejo
4. Una figura se amplió al doble de su tamaño

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Traslación**
2. **Rotación**
3. **Reflexión**
4. **Homotecia**

</details>

---

### Ejercicio 2: Isometría o no

Indica si cada transformación es una isometría:

1. Rotar 45°
2. Ampliar al triple
3. Trasladar 10 unidades
4. Reducir a la mitad

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Sí** (conserva tamaño y forma)
2. **No** (cambia el tamaño)
3. **Sí** (conserva tamaño y forma)
4. **No** (cambia el tamaño)

</details>

---

### Ejercicio 3: Verdadero o Falso

1. Todas las isometrías conservan las distancias.
2. La composición de dos traslaciones es siempre una traslación.
3. En una rotación, solo el centro permanece fijo.
4. Las transformaciones siempre se aplican en el mismo orden.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero** - Por definición de isometría
2. **Verdadero** - La suma de vectores da otro vector
3. **Verdadero** - El centro es el único punto fijo
4. **Falso** - El orden puede variar y afecta el resultado

</details>

---
