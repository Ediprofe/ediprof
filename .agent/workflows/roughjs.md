---
description: Guía para generar diagramas ilustrativos con estilo "mano alzada" usando Rough.js globs: ["src/content/**/*.md"]
---

# ✏️ Workflow: Rough.js (Diagramas Ilustrativos)

Rough.js crea diagramas con un estilo **"dibujado a mano"** que es perfecto para ilustraciones conceptuales y situaciones físicas.

---

## ✅ Cuándo usar Rough.js

| Caso de uso | Usar Rough.js |
|-------------|---------------|
| Situaciones físicas (bloques, poleas, planos) | ✅ SÍ |
| Modelos atómicos, partículas | ✅ SÍ |
| Estados de la materia | ✅ SÍ |
| Equipos de laboratorio | ✅ SÍ |
| Diagramas de procesos (tamizado, filtración) | ✅ SÍ |
| Mapas conceptuales | ✅ SÍ |
| Organigramas, jerarquías | ✅ SÍ |
| Ciclos (método científico, agua) | ✅ SÍ |
| Comparaciones visuales | ✅ SÍ |

### ❌ NO usar Rough.js para:

- Geometría con propiedades exactas → **SVG** (GeometrySpec, CircleSpec)
- Gráficas de funciones matemáticas → **SVG** (CartesianSpec, GraphSpec)

---

## 🎨 Plantilla Estándar (ES Module - RECOMENDADA)

> **ESCALABILIDAD:** Este patrón ES module es auto-contenido. La librería solo se descarga cuando esta página específica se carga. Perfecto para escalar a miles de lecciones.

```html
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="rough-[LECCION]-[NUMERO]" width="800" height="400" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script type="module">
import rough from 'https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.esm.js';

const canvas = document.getElementById('rough-[LECCION]-[NUMERO]');
if (canvas) {
  const rc = rough.canvas(canvas);
  const ctx = canvas.getContext('2d');
  
  // Título (opcional)
  ctx.font = 'bold 14px Inter, sans-serif';
  ctx.fillStyle = '#1e293b';
  ctx.textAlign = 'center';
  ctx.fillText('Título del diagrama', 400, 25);
  
  // Dibujar elementos con rc...
  
}
</script>
```

### Ventajas del patrón ES Module:
- ✅ **Auto-contenido**: No depende de carga global
- ✅ **Escalable**: Solo descarga ~50KB en páginas que lo usan
- ✅ **Confiable**: Sin problemas de timing
- ✅ **Moderno**: Sintaxis más limpia

---

## 🎨 Plantilla Alternativa (Global - Legacy)

> Solo usar si necesitas compatibilidad con scripts existentes que usan `typeof rough`.

```html
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="rough-[LECCION]-[NUMERO]" width="800" height="400" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('rough-[LECCION]-[NUMERO]')) {
    var canvas = document.getElementById('rough-[LECCION]-[NUMERO]');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título (opcional)
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Título del diagrama', 400, 25);
    
    // Dibujar elementos con rc...
    
  }
});
</script>
```

---

## 🔧 API Básica de Rough.js

### Rectángulo

```javascript
rc.rectangle(x, y, width, height, {
  fill: '#dbeafe',
  fillStyle: 'solid',
  stroke: '#3b82f6',
  strokeWidth: 2,
  roughness: 0.5
});
```

### Círculo

```javascript
rc.circle(centerX, centerY, diameter, {
  fill: '#dcfce7',
  fillStyle: 'solid',
  stroke: '#22c55e',
  strokeWidth: 2,
  roughness: 0.5
});
```

### Línea

```javascript
rc.line(x1, y1, x2, y2, {
  stroke: '#3b82f6',
  strokeWidth: 2,
  roughness: 0.5
});
```

### Elipse

```javascript
rc.ellipse(centerX, centerY, width, height, {
  fill: '#fef3c7',
  stroke: '#f59e0b'
});
```

### Polígono

```javascript
rc.polygon([[x1,y1], [x2,y2], [x3,y3]], {
  fill: '#fee2e2',
  stroke: '#ef4444'
});
```

### Arco

```javascript
rc.arc(centerX, centerY, width, height, startAngle, endAngle, closed, {
  stroke: '#3b82f6'
});
```

---

## 📝 Texto con Canvas Nativo

Rough.js no dibuja texto. Usa el contexto 2D del canvas:

```javascript
var ctx = canvas.getContext('2d');

// Título centrado
ctx.font = 'bold 14px Inter, sans-serif';
ctx.fillStyle = '#1e293b';
ctx.textAlign = 'center';
ctx.fillText('Título', 400, 25);

// Etiqueta alineada a la izquierda
ctx.font = '12px Inter, sans-serif';
ctx.fillStyle = '#64748b';
ctx.textAlign = 'left';
ctx.fillText('Etiqueta', 100, 100);

// Subíndices (simular)
ctx.fillText('H₂O', x, y);  // Usar caracteres Unicode
```

---

## 🎨 Paleta de Colores

### Colores principales (bordes/líneas)

| Uso | Color | Hex |
|-----|-------|-----|
| Azul | Elementos principales, agua | `#3b82f6` |
| Rojo | Alertas, calor, peligro | `#ef4444` |
| Verde | Positivo, naturaleza | `#22c55e` |
| Naranja | Energía, advertencia | `#f59e0b` |
| Morado | Especial, destacado | `#a855f7` |
| Gris | Neutro, estructuras | `#64748b` |

### Colores de fondo (rellenos)

| Uso | Color | Hex |
|-----|-------|-----|
| Azul claro | Agua, líquidos | `#dbeafe` |
| Rojo claro | Calor, peligro | `#fee2e2` |
| Verde claro | Éxito, plantas | `#dcfce7` |
| Amarillo claro | Aceite, advertencia | `#fef3c7` |
| Gris claro | Neutro, sólidos | `#f1f5f9` |

### Partículas (química/física)

| Partícula | Color | Hex |
|-----------|-------|-----|
| Protón | Rojo | `#ef4444` |
| Neutrón | Gris | `#6b7280` |
| Electrón | Azul | `#3b82f6` |
| Núcleo | Naranja | `#fbbf24` |

---

## ⚙️ Parámetros de Estilo

### roughness (rugosidad)

```javascript
roughness: 0.3  // Más limpio, técnico
roughness: 0.5  // Balance (DEFAULT)
roughness: 0.8  // Más "a mano"
roughness: 1.2  // Muy artístico
```

### fillStyle (estilo de relleno)

```javascript
fillStyle: 'solid'       // Relleno sólido (más común)
fillStyle: 'hachure'     // Rayado diagonal
fillStyle: 'zigzag'      // Zigzag
fillStyle: 'cross-hatch' // Rayado cruzado
fillStyle: 'dots'        // Puntos
```

### strokeWidth (grosor de línea)

```javascript
strokeWidth: 1  // Líneas finas, detalles
strokeWidth: 2  // Normal (DEFAULT)
strokeWidth: 3  // Gruesas, énfasis
```

---

## 📐 Ejemplos por Tipo

### Estados de la Materia

```javascript
// SÓLIDO - partículas muy juntas
var x1 = 100;
rc.rectangle(x1-45, 50, 90, 90, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', roughness: 0.5 });
for (var row = 0; row < 4; row++) {
  for (var col = 0; col < 4; col++) {
    rc.circle(x1-28 + col*19, 65 + row*19, 12, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.4 });
  }
}
ctx.font = 'bold 12px Inter';
ctx.fillStyle = '#3b82f6';
ctx.textAlign = 'center';
ctx.fillText('SÓLIDO', x1, 160);

// LÍQUIDO - partículas más separadas
var x2 = 300;
rc.rectangle(x2-45, 50, 90, 90, { fill: '#dcfce7', fillStyle: 'solid', stroke: '#22c55e', roughness: 0.5 });
var liqPos = [[x2-25,65], [x2,70], [x2+25,63], [x2-20,90], [x2+5,95], [x2+25,88], [x2-15,115], [x2+10,118]];
liqPos.forEach(function(p) {
  rc.circle(p[0], p[1], 12, { fill: '#22c55e', fillStyle: 'solid', roughness: 0.5 });
});

// GAS - partículas muy separadas
var x3 = 500;
rc.rectangle(x3-45, 50, 90, 90, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', roughness: 0.5 });
var gasPos = [[x3-30,60], [x3+25,75], [x3-10,100], [x3+30,120], [x3-25,125]];
gasPos.forEach(function(p) {
  rc.circle(p[0], p[1], 12, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.5 });
});
```

### Flecha con Punta

```javascript
function drawArrow(rc, x1, y1, x2, y2, color) {
  // Línea principal
  rc.line(x1, y1, x2, y2, { stroke: color, strokeWidth: 2, roughness: 0.5 });
  
  // Punta de flecha
  var angle = Math.atan2(y2-y1, x2-x1);
  var headLen = 15;
  rc.line(x2, y2, x2 - headLen*Math.cos(angle-Math.PI/6), y2 - headLen*Math.sin(angle-Math.PI/6), { stroke: color, strokeWidth: 2, roughness: 0.5 });
  rc.line(x2, y2, x2 - headLen*Math.cos(angle+Math.PI/6), y2 - headLen*Math.sin(angle+Math.PI/6), { stroke: color, strokeWidth: 2, roughness: 0.5 });
}

drawArrow(rc, 100, 200, 300, 200, '#22c55e');
```

### Modelo Atómico Simple

```javascript
// Núcleo
rc.circle(300, 200, 40, { fill: '#fbbf24', fillStyle: 'solid', stroke: '#f59e0b', roughness: 0.5 });

// Órbitas
rc.ellipse(300, 200, 120, 60, { stroke: '#94a3b8', roughness: 0.3 });
rc.ellipse(300, 200, 180, 90, { stroke: '#94a3b8', roughness: 0.3 });

// Electrones
rc.circle(360, 200, 12, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.4 });
rc.circle(210, 200, 12, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.4 });

// Etiquetas
ctx.font = '10px Inter';
ctx.fillStyle = '#64748b';
ctx.fillText('e⁻', 370, 205);
ctx.fillText('Núcleo', 300, 205);
```

### Ciclo/Proceso

```javascript
// Cajas del proceso
var steps = [
  { x: 100, y: 50, text: '1. Observación', color: '#f59e0b' },
  { x: 300, y: 50, text: '2. Hipótesis', color: '#ef4444' },
  { x: 500, y: 50, text: '3. Experimento', color: '#3b82f6' },
  { x: 500, y: 150, text: '4. Análisis', color: '#22c55e' },
  { x: 300, y: 150, text: '5. Conclusión', color: '#a855f7' }
];

steps.forEach(function(step) {
  rc.rectangle(step.x-50, step.y-20, 100, 40, { fill: step.color + '20', stroke: step.color, roughness: 0.5 });
  ctx.font = 'bold 11px Inter';
  ctx.fillStyle = step.color;
  ctx.textAlign = 'center';
  ctx.fillText(step.text, step.x, step.y+5);
});

// Flechas conectando
drawArrow(rc, 150, 50, 250, 50, '#64748b');
drawArrow(rc, 350, 50, 450, 50, '#64748b');
// ...etc
```

---

## ✅ Checklist

- [ ] ID único: `roughjs-[leccion]-[numero]`
- [ ] Wrapper con fondo `#f8fafc`
- [ ] Canvas con `width="800" height="400"` (o proporcional)
- [ ] Canvas style: `width: 100%; height: auto; display: block;`
- [ ] `DOMContentLoaded` wrapper
- [ ] Verificación: `if (typeof rough !== 'undefined')`
- [ ] `roughness` consistente (0.5 por defecto)
- [ ] Texto con `ctx` (canvas nativo), no con Rough.js
- [ ] Leyenda si hay múltiples colores/símbolos

---

## ⚠️ Buenas Prácticas

1. **Verificar disponibilidad**: Siempre `if (typeof rough !== 'undefined')`
2. **Roughness consistente**: 0.5 es buen default
3. **Combinar con canvas nativo**: Rough.js para formas, ctx para texto
4. **Variables para coordenadas**: Facilita ajustes
5. **Leyendas claras**: Explicar colores y símbolos
6. **Responsive**: `style="width: 100%; height: auto;"`

---

## 🔗 Relacionados

- [Árbol de decisión](../CLAUDE.md#-árbol-de-decisión)
- [GeometrySpec](./geometry-exact.md) - Para geometría exacta (NO usar Rough.js)
- [ECharts](./echarts.md) - Para funciones y datos