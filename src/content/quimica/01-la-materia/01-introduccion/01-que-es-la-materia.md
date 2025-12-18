# Qué es la Materia

¿Alguna vez te has preguntado de qué está hecho todo lo que puedes tocar, ver o incluso respirar? Desde el aire que llena tus pulmones hasta el teléfono en tu mano, todo tiene algo en común: es **materia**.

La química comienza con una pregunta fundamental: ¿qué es eso que ocupa espacio y tiene masa? Entender la materia es el primer paso para entender cómo funciona el universo.

---

## 🎯 ¿Qué vas a aprender?

- La definición científica de materia
- Las propiedades generales que toda materia posee
- Los tres estados de la materia y sus características
- Los cambios de estado y cómo ocurren

---

## 📊 Resumen: Estados de la Materia

| Estado | Forma | Volumen | Movimiento de partículas | Ejemplo |
|--------|-------|---------|--------------------------|---------|
| **Sólido** | Definida | Definido | Vibración en posición fija | Hielo, madera |
| **Líquido** | Variable (toma la del recipiente) | Definido | Deslizamiento | Agua, aceite |
| **Gaseoso** | Variable | Variable | Movimiento libre y rápido | Aire, vapor |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-materia-estados-1" width="750" height="280" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-materia-estados-1')) {
    var canvas = document.getElementById('roughjs-materia-estados-1');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Los Tres Estados de la Materia', 375, 25);
    
    // === SÓLIDO ===
    var x1 = 130;
    rc.rectangle(x1-55, 55, 110, 110, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5 });
    // Partículas ordenadas (4x4)
    for (var row = 0; row < 4; row++) {
      for (var col = 0; col < 4; col++) {
        rc.circle(x1-38 + col*25, 75 + row*22, 16, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1e40af', roughness: 0.4 });
      }
    }
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('SÓLIDO', x1, 185);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Partículas muy juntas', x1, 205);
    ctx.fillText('Solo vibran en su lugar', x1, 220);
    ctx.fillText('Forma definida', x1, 235);
    
    // === LÍQUIDO ===
    var x2 = 375;
    rc.rectangle(x2-55, 55, 110, 110, { fill: '#dcfce7', fillStyle: 'solid', stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    // Partículas más separadas y desordenadas
    var liqPos = [
      [x2-35, 70], [x2-10, 75], [x2+15, 68], [x2+38, 78],
      [x2-28, 98], [x2, 102], [x2+28, 95],
      [x2-35, 125], [x2-8, 130], [x2+20, 128], [x2+40, 135]
    ];
    liqPos.forEach(function(p) {
      rc.circle(p[0], p[1], 16, { fill: '#22c55e', fillStyle: 'solid', stroke: '#15803d', roughness: 0.5 });
    });
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('LÍQUIDO', x2, 185);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Partículas juntas pero móviles', x2, 205);
    ctx.fillText('Se deslizan unas sobre otras', x2, 220);
    ctx.fillText('Forma del recipiente', x2, 235);
    
    // === GAS ===
    var x3 = 620;
    rc.rectangle(x3-55, 55, 110, 110, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', strokeWidth: 2, roughness: 0.5 });
    // Partículas muy separadas
    var gasPos = [
      [x3-40, 65], [x3+30, 80], [x3-15, 105], [x3+40, 130], [x3-35, 145], [x3+10, 70], [x3+5, 140]
    ];
    gasPos.forEach(function(p) {
      rc.circle(p[0], p[1], 14, { fill: '#f59e0b', fillStyle: 'solid', stroke: '#d97706', roughness: 0.5 });
    });
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('GAS', x3, 185);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Partículas muy separadas', x3, 205);
    ctx.fillText('Movimiento libre y rápido', x3, 220);
    ctx.fillText('Llenan todo el espacio', x3, 235);
    
    // Flechas de energía
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.textAlign = 'left';
    ctx.fillText('+ Energía →', 200, 265);
    ctx.fillText('+ Energía →', 445, 265);
  }
});
</script>

---

## 📖 Definición de Materia

> La **materia** es todo aquello que tiene **masa** y ocupa un **lugar en el espacio** (volumen).

### 💡 Puntos clave:

- Todo lo que puedes tocar es materia
- El aire es materia (aunque no lo veas)
- La luz y el sonido **NO** son materia (son energía)
- Los pensamientos **NO** son materia

### ⚙️ Ejemplos de materia y no materia

| ✅ Es materia | ❌ No es materia |
|--------------|------------------|
| Agua | Luz |
| Aire | Sonido |
| Hierro | Calor |
| Plástico | Pensamientos |
| Humo | Sombras |

---

## 📖 Propiedades Generales de la Materia

Toda materia, sin importar de qué esté hecha, tiene estas propiedades:

| Propiedad | Definición | Ejemplo |
|-----------|------------|---------|
| **Masa** | Cantidad de materia en un objeto | Un libro tiene más masa que un lápiz |
| **Volumen** | Espacio que ocupa | Una pelota ocupa más espacio que una canica |
| **Inercia** | Resistencia a cambiar su estado de movimiento | Empujar un auto estacionado requiere fuerza |
| **Impenetrabilidad** | Dos cuerpos no pueden ocupar el mismo espacio simultáneamente | No puedes atravesar una pared |

---

## 📖 Estados de la Materia

La materia puede existir en tres estados principales, dependiendo de la energía (temperatura) que tenga.

### 💡 Estado Sólido

> En el estado **sólido**, las partículas están muy juntas y solo pueden vibrar en su posición.

**Características:**
- Forma definida
- Volumen definido
- Partículas muy ordenadas
- No se comprimen fácilmente

**Ejemplos:** Hielo, madera, metal, piedra, plástico

### 💡 Estado Líquido

> En el estado **líquido**, las partículas están juntas pero pueden deslizarse unas sobre otras.

**Características:**
- Forma variable (toman la forma del recipiente)
- Volumen definido
- Partículas con movimiento moderado
- Difíciles de comprimir

**Ejemplos:** Agua, aceite, leche, gasolina, mercurio

### 💡 Estado Gaseoso

> En el estado **gaseoso**, las partículas están muy separadas y se mueven libremente en todas direcciones.

**Características:**
- Forma variable
- Volumen variable (se expanden para llenar todo el espacio)
- Partículas con movimiento muy rápido
- Fáciles de comprimir

**Ejemplos:** Aire, oxígeno, vapor de agua, gas natural

---

## 📖 Cambios de Estado

Cuando la materia gana o pierde energía (generalmente calor), puede cambiar de un estado a otro.

### 📊 Diagrama de Cambios de Estado

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-materia-cambios-2" width="700" height="320" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-materia-cambios-2')) {
    var canvas = document.getElementById('roughjs-materia-cambios-2');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título
    ctx.font = 'bold 15px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Cambios de Estado de la Materia', 350, 22);
    
    // Posiciones de los estados
    var yCenter = 160;
    var x1 = 120, x2 = 350, x3 = 580;
    
    // === SÓLIDO ===
    rc.rectangle(x1-50, yCenter-40, 100, 80, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5 });
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('SÓLIDO', x1, yCenter+5);
    
    // === LÍQUIDO ===
    rc.rectangle(x2-50, yCenter-40, 100, 80, { fill: '#dcfce7', fillStyle: 'solid', stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
    ctx.fillStyle = '#22c55e';
    ctx.fillText('LÍQUIDO', x2, yCenter+5);
    
    // === GAS ===
    rc.rectangle(x3-50, yCenter-40, 100, 80, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', strokeWidth: 2, roughness: 0.5 });
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('GAS', x3, yCenter+5);
    
    // Función para dibujar flecha
    function drawArrow(x1, y1, x2, y2, color) {
      rc.line(x1, y1, x2, y2, { stroke: color, strokeWidth: 2, roughness: 0.3 });
      var angle = Math.atan2(y2-y1, x2-x1);
      var headLen = 10;
      rc.line(x2, y2, x2 - headLen*Math.cos(angle-Math.PI/6), y2 - headLen*Math.sin(angle-Math.PI/6), { stroke: color, strokeWidth: 2, roughness: 0.3 });
      rc.line(x2, y2, x2 - headLen*Math.cos(angle+Math.PI/6), y2 - headLen*Math.sin(angle+Math.PI/6), { stroke: color, strokeWidth: 2, roughness: 0.3 });
    }
    
    // Flechas entre estados (arriba: gana calor, abajo: pierde calor)
    // Sólido → Líquido (Fusión)
    drawArrow(x1+55, yCenter-20, x2-55, yCenter-20, '#ef4444');
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('Fusión', (x1+x2)/2, yCenter-30);
    ctx.font = '9px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('(+calor)', (x1+x2)/2, yCenter-42);
    
    // Líquido → Sólido (Solidificación)
    drawArrow(x2-55, yCenter+20, x1+55, yCenter+20, '#3b82f6');
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Solidificación', (x1+x2)/2, yCenter+35);
    ctx.font = '9px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('(-calor)', (x1+x2)/2, yCenter+48);
    
    // Líquido → Gas (Evaporación)
    drawArrow(x2+55, yCenter-20, x3-55, yCenter-20, '#ef4444');
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('Evaporación', (x2+x3)/2, yCenter-30);
    ctx.font = '9px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('(+calor)', (x2+x3)/2, yCenter-42);
    
    // Gas → Líquido (Condensación)
    drawArrow(x3-55, yCenter+20, x2+55, yCenter+20, '#3b82f6');
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Condensación', (x2+x3)/2, yCenter+35);
    ctx.font = '9px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('(-calor)', (x2+x3)/2, yCenter+48);
    
    // Sublimación (arco arriba)
    drawArrow(x1+50, yCenter-70, x3-50, yCenter-70, '#a855f7');
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#a855f7';
    ctx.fillText('Sublimación (+calor)', 350, yCenter-85);
    
    // Sublimación regresiva (Gas → Sólido)
    drawArrow(x3-50, yCenter+70, x1+50, yCenter+70, '#8b5cf6');
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#8b5cf6';
    ctx.fillText('Sublimación regresiva (-calor)', 350, yCenter+90);
    
    // Leyenda
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.textAlign = 'left';
    ctx.fillText('🔴 Gana calor (endotérmico)', 50, 300);
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('🔵 Pierde calor (exotérmico)', 280, 300);
  }
});
</script>

### 📋 Tabla de Cambios de Estado

| Cambio | De → A | ¿Gana o pierde calor? | Ejemplo |
|--------|--------|----------------------|---------|
| **Fusión** | Sólido → Líquido | Gana calor | Hielo derritiéndose |
| **Solidificación** | Líquido → Sólido | Pierde calor | Agua congelándose |
| **Evaporación** | Líquido → Gas | Gana calor | Agua hirviendo |
| **Condensación** | Gas → Líquido | Pierde calor | Vapor en espejo frío |
| **Sublimación** | Sólido → Gas | Gana calor | Hielo seco (CO₂) |
| **Sublimación regresiva** | Gas → Sólido | Pierde calor | Escarcha formándose |

### ⚙️ Ejemplo 1: El ciclo del agua

El agua experimenta todos estos cambios de estado:

1. **Evaporación:** El sol calienta el océano → el agua líquida se vuelve vapor
2. **Condensación:** El vapor sube, se enfría → se forman nubes (gotitas)
3. **Solidificación:** En zonas muy frías → las gotas se vuelven granizo o nieve
4. **Fusión:** La nieve cae y se derrite → vuelve a ser agua líquida

### ⚙️ Ejemplo 2: Sublimación del hielo seco

El hielo seco (CO₂ sólido) a temperatura ambiente pasa directamente de sólido a gas, sin pasar por líquido. Por eso "humea" sin mojarse.

---

## 📖 Puntos de Fusión y Ebullición

Cada sustancia tiene temperaturas específicas a las cuales cambia de estado:

| Sustancia | Punto de Fusión | Punto de Ebullición |
|-----------|-----------------|---------------------|
| Agua | 0°C | 100°C |
| Alcohol etílico | -114°C | 78°C |
| Hierro | 1,538°C | 2,862°C |
| Oxígeno | -219°C | -183°C |
| Oro | 1,064°C | 2,856°C |

### 💡 ¿Por qué son importantes estos puntos?

- Nos ayudan a **identificar sustancias**
- Son **propiedades intensivas** (no dependen de la cantidad)
- Son constantes para cada sustancia pura a presión normal

---

## 🔑 Resumen

| Concepto | Definición Clave |
|----------|-----------------|
| **Materia** | Todo lo que tiene masa y ocupa espacio |
| **Estados** | Sólido (forma fija), Líquido (forma variable), Gas (expande) |
| **Cambio de estado** | Transformación entre estados por ganancia/pérdida de calor |
| **Fusión** | Sólido → Líquido |
| **Evaporación** | Líquido → Gas |
| **Sublimación** | Sólido → Gas (directo) |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Clasifica los siguientes como **materia (M)** o **no materia (N)**:
a) Humo
b) Luz solar
c) Vapor de agua
d) Sombra de un árbol
e) Aire comprimido

<details>
<summary>Ver solución</summary>

a) **M** - El humo son partículas sólidas suspendidas en gas
b) **N** - La luz es energía, no tiene masa
c) **M** - El vapor es agua en estado gaseoso
d) **N** - La sombra es ausencia de luz, no es materia
e) **M** - El aire comprimido sigue siendo materia (gases)

</details>

### Ejercicio 2
Identifica el cambio de estado en cada situación:

a) Se forma hielo en el congelador
b) La ropa mojada se seca al sol
c) Aparece rocío en las plantas por la mañana
d) Una vela se derrite cerca de una llama

<details>
<summary>Ver solución</summary>

a) **Solidificación** (líquido → sólido)
b) **Evaporación** (líquido → gas)
c) **Condensación** (gas → líquido)
d) **Fusión** (sólido → líquido)

</details>

### Ejercicio 3
¿Por qué el alcohol se evapora más rápido que el agua a temperatura ambiente?

<details>
<summary>Ver solución</summary>

El alcohol se evapora más rápido porque tiene un **punto de ebullición más bajo** que el agua:

- Alcohol etílico: 78°C
- Agua: 100°C

Esto significa que las partículas de alcohol necesitan menos energía para pasar al estado gaseoso. A temperatura ambiente (≈25°C), el alcohol ya está más cerca de su punto de ebullición.

</details>

### Ejercicio 4
Observas que en invierno, la ropa mojada colgada afuera se "seca" aunque esté bajo cero. ¿Qué cambio de estado ocurrió?

<details>
<summary>Ver solución</summary>

Ocurrió una **sublimación**.

**Proceso:**
1. El agua en la ropa primero se congela (solidificación)
2. El hielo en la ropa pasa directamente a vapor (sublimación)
3. No hay etapa líquida intermedia

Esto es posible porque el hielo puede sublimarse lentamente incluso a temperaturas bajo cero, especialmente si el aire es seco.

</details>
