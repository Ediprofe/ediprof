---
description: Guía para generar gráficos en lecciones educativas - ECharts, JSXGraph, Chart.js y Three.js
---

# 📊 Guía de Generación de Gráficos Educativos

Este documento define las buenas prácticas para generar gráficos en las lecciones de ediprofe.com.

---

## 🎯 REGLA DE ORO

> **ECharts es la PRIMERA opción** para cualquier gráfico de funciones, datos o visualizaciones estáticas.
> 
> Solo usar **JSXGraph cuando se requiera INTERACTIVIDAD** (arrastrar puntos, manipular vectores).

---

## ⚠️ REGLAS CRÍTICAS PARA ILUSTRACIONES GEOMÉTRICAS

### Regla 1: Figuras ESTÁTICAS por defecto

> **TODOS los puntos deben ser fijos** (`fixed: true`) a menos que el usuario solicite explícitamente interactividad.

La interactividad mal diseñada causa confusión cuando:
- Las etiquetas se separan de los puntos
- Los elementos se mueven de forma no intencional
- La figura pierde su significado geométrico

**✅ SIEMPRE agregar `fixed: true` a TODOS los puntos:**

```javascript
// Puntos visibles con etiquetas
board.create('point', [2, 3], {name: 'A', size: 6, fixed: true, color: '#3b82f6', label: {...}});

// Puntos invisibles (usados para definir rectas/segmentos)
board.create('point', [5, 5], {visible: false, fixed: true});

// Puntos sin nombre
board.create('point', [3, 2], {name: '', size: 5, fixed: true, color: '#22c55e'});
```

### Regla 2: Notaciones LaTeX FUERA del wrapper

> **Las notaciones matemáticas (LaTeX) deben ir ARRIBA del wrapper**, nunca dentro de la ilustración JSXGraph.

JSXGraph no puede renderizar LaTeX correctamente. Colocar las notaciones como texto en negrita **inmediatamente antes** del wrapper `<div>`:

**✅ CORRECTO:**

```markdown
**Representación del segmento $\overline{AB}$:**

<div style="background: #f1f5f9; ...">
  ...
</div>
```

**✅ Ejemplos de títulos con notación:**

| Concepto | Título LaTeX |
|----------|--------------|
| Segmento | `**Segmento $\overline{AB}$:**` |
| Recta | `**Recta $\overleftrightarrow{AB}$ (notación: $l$):**` |
| Rayo | `**Rayo $\overrightarrow{AB}$:**` |
| Ángulo | `**Ángulo $\angle ABC$:**` |
| Paralelas | `**Rectas paralelas ($l \parallel m$):**` |
| Complementarios | `**Ángulos complementarios ($\alpha + \beta = 90°$):**` |

**❌ INCORRECTO (dentro de JSXGraph):**

```javascript
// NO HACER: LaTeX no se renderiza correctamente dentro de JSXGraph
board.create('text', [5, 5, 'Segmento AB con barra'], {...});
```

---

## 📐 Estilo visual obligatorio para TODOS los gráficos

Todos los gráficos deben seguir este wrapper visual **100% responsive**:

```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="CHART-ID" style="width: 100%; height: 450px; min-height: 350px; border-radius: 8px;"></div>
</div>
```

### Especificaciones del wrapper:
| Propiedad | Valor | Descripción |
|-----------|-------|-------------|
| Fondo | `#f1f5f9` | Gris neutro claro |
| Borde | `1px solid #cbd5e1` | Borde sutil |
| Bordes redondeados | `12px` | Esquinas suaves |
| Padding | `1rem` | Espacio interno |
| Icono | `📊` solo | Sin texto adicional |
| **Ancho wrapper** | `width: 100%; box-sizing: border-box;` | **Ocupa TODO el ancho disponible** |
| **Ancho chart** | `width: 100%` | **Ocupa todo el wrapper** |
| **Alto chart** | `height: 450px; min-height: 350px` | Altura generosa con mínimo garantizado |

---

# SECCIÓN A: ECharts (Primera opción) ✨

## A.1 Cuándo usar ECharts

| Tipo de Gráfico | Usar ECharts |
|-----------------|--------------|
| Funciones lineales (f(x) = mx + b) | ✅ SÍ |
| Gráficas de datos (series, líneas) | ✅ SÍ |
| Comparativos (múltiples funciones) | ✅ SÍ |
| Estadística (barras, histogramas) | ✅ SÍ |
| Cualquier visualización estática | ✅ SÍ |

## A.2 Configuración obligatoria ECharts

Cada gráfico ECharts DEBE incluir:

1. **Título descriptivo**
2. **Cuadrícula visible** con color `#94a3b8`
3. **Nombres de ejes** en negrita
4. **Responsive** con resize listener
5. **Animación** de entrada

## A.3 Plantilla completa ECharts (COPIAR ESTA)

```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-NOMBRE" style="width: 100%; height: 450px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-NOMBRE')) {
    var chart = echarts.init(document.getElementById('echarts-NOMBRE'));
    
    var option = {
      title: {
        text: 'TÍTULO DESCRIPTIVO DEL GRÁFICO',
        subtext: 'f(x) = expresión',
        left: 'center',
        textStyle: { fontSize: 16, fontWeight: 'bold', color: '#1e293b' },
        subtextStyle: { fontSize: 13, color: '#3b82f6', fontWeight: 'bold' }
      },
      animation: true,
      animationDuration: 1000,
      grid: { 
        left: '15%', 
        right: '8%', 
        top: '18%', 
        bottom: '18%', 
        show: true, 
        borderColor: '#cbd5e1' 
      },
      xAxis: {
        type: 'value',
        name: 'Nombre eje X (x)',
        nameLocation: 'middle',
        nameGap: 32,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: 0,
        max: 10,
        axisLine: { lineStyle: { color: '#64748b' } },
        splitLine: { show: true, lineStyle: { type: 'solid', color: '#94a3b8', width: 1 } }
      },
      yAxis: {
        type: 'value',
        name: 'Nombre eje Y',
        nameLocation: 'middle',
        nameGap: 50,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: 0,
        max: 30,
        axisLine: { lineStyle: { color: '#64748b' } },
        splitLine: { show: true, lineStyle: { type: 'solid', color: '#94a3b8', width: 1 } }
      },
      series: [
        {
          name: 'Función',
          type: 'line',
          smooth: true,
          symbol: 'none',
          lineStyle: { width: 3, color: '#3b82f6' },
          areaStyle: {
            color: {
              type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
              colorStops: [
                { offset: 0, color: 'rgba(59, 130, 246, 0.3)' },
                { offset: 1, color: 'rgba(59, 130, 246, 0.05)' }
              ]
            }
          },
          data: [[0, 0], [2, 6], [4, 12], [6, 18], [8, 24], [10, 30]]
        },
        {
          name: 'Puntos',
          type: 'scatter',
          symbolSize: 12,
          itemStyle: { color: '#22c55e', borderColor: '#fff', borderWidth: 2 },
          label: { 
            show: true, 
            formatter: function(p) { return '(' + p.data[0] + ', ' + p.data[1] + ')'; }, 
            position: 'top', 
            fontSize: 10 
          },
          data: [[0, 0], [5, 15], [10, 30]]
        }
      ],
      tooltip: { trigger: 'axis' }
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>
```

## A.4 Paleta de colores ECharts

| Color | Hex | Uso |
|-------|-----|-----|
| Azul | `#3b82f6` | Función principal |
| Rojo | `#ef4444` | Función secundaria |
| Verde | `#22c55e` | Puntos destacados |
| Naranja | `#f97316` | Interceptos, marcas especiales |
| Gris cuadrícula | `#94a3b8` | Líneas de cuadrícula |
| Gris eje | `#64748b` | Líneas de ejes |

## A.5 IMPORTANTE: Colores en leyendas

> ⚠️ **REGLA CRÍTICA**: Cuando una serie tiene un color específico, SIEMPRE incluir `itemStyle` con el MISMO color que `lineStyle`. Esto asegura que la leyenda muestre el color correcto.

### ❌ INCORRECTO (confunde en la leyenda):
```javascript
series: [
  { 
    name: 'a = 1', 
    type: 'line', 
    lineStyle: { color: '#3b82f6' }, 
    data: data1 
  }
]
```

### ✅ CORRECTO (leyenda muestra color correcto):
```javascript
series: [
  { 
    name: 'a = 1', 
    type: 'line', 
    lineStyle: { width: 3, color: '#3b82f6' }, 
    itemStyle: { color: '#3b82f6' },  // ← SIEMPRE AGREGAR ESTO
    data: data1 
  }
]
```

**Razón**: Sin `itemStyle`, la leyenda puede mostrar un color predeterminado diferente al de la línea, causando confusión visual.

---

# SECCIÓN B: JSXGraph (Solo para interactividad)

## B.1 Cuándo usar JSXGraph

| Necesidad | Librería |
|-----------|----------|
| Arrastrar puntos | JSXGraph |
| Vectores interactivos | JSXGraph |
| Explorar construcciones | JSXGraph |
| Visualizar función SIN interacción | ECharts ✨ |

## B.2 Plantilla JSXGraph con wrapper

> ⚠️ **IMPORTANTE**: Por defecto, TODOS los puntos deben tener `fixed: true` (ver Regla 1 arriba). Solo si el usuario solicita explícitamente interactividad, omitir `fixed: true` en los puntos que deban moverse.

**Título LaTeX ARRIBA del wrapper (Regla 2):**

```markdown
**Representación del segmento $\overline{AB}$:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-NOMBRE" style="width: 100%; height: 450px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-NOMBRE')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-NOMBRE', {
      boundingbox: [-1, 7, 9, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Puntos SIEMPRE con fixed: true (a menos que se solicite interactividad)
    var pA = board.create('point', [2, 3], {name: 'A', size: 6, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [10, 10]}});
    var pB = board.create('point', [7, 3], {name: 'B', size: 6, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [10, 10]}});
    
    // Puntos invisibles también con fixed: true
    var pHidden = board.create('point', [5, 5], {visible: false, fixed: true});
    
    // Segmento/recta usando los puntos
    board.create('segment', [pA, pB], {strokeColor: '#22c55e', strokeWidth: 3});
    
    board.unsuspendUpdate();
  }
});
</script>
```

## B.3 Paleta de colores JSXGraph

| Color | Hex | Uso |
|-------|-----|-----|
| Azul | `#3b82f6` | Vector A |
| Rojo | `#ef4444` | Vector B |
| Verde | `#22c55e` | Resultante |
| Naranja | `#f97316` | Auxiliares |
| Gris | `#94a3b8` | Líneas punteadas |

---

# SECCIÓN C: Rough.js (Diagramas ilustrativos y esquemáticos)

## C.1 Cuándo usar Rough.js

| Tipo de Diagrama | Usar Rough.js |
|------------------|---------------|
| Ilustraciones de situaciones físicas | ✅ SÍ |
| Diagramas de partículas/átomos | ✅ SÍ |
| Esquemas de equipos de laboratorio | ✅ SÍ |
| Diagramas de procesos (tamizado, filtración) | ✅ SÍ |
| Dianas, targets, comparaciones visuales | ✅ SÍ |
| Mapas mentales/conceptuales | ✅ SÍ |
| Diagramas de flujo de procesos | ✅ SÍ |
| Organigramas y jerarquías (ej: ramas de la física) | ✅ SÍ |

> **REGLA:** Rough.js para **TODOS los diagramas ilustrativos y conceptuales**. Mantiene el estilo "mano alzada" unificado en toda la plataforma.

## C.2 Estilo visual obligatorio para Rough.js

Todos los diagramas Rough.js deben seguir este wrapper **100% responsive**:

```html
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-NOMBRE" width="800" height="400" style="width: 100%; height: auto; display: block;"></canvas>
</div>
```

### Especificaciones del wrapper:
| Propiedad | Valor | Descripción |
|-----------|-------|-------------|
| Fondo | `#f8fafc` | Gris muy claro (más claro que ECharts) |
| Borde | `1px solid #cbd5e1` | Borde sutil |
| Bordes redondeados | `12px` | Esquinas suaves |
| Padding | `1rem` | Espacio interno |
| **Ancho wrapper** | `width: 100%; box-sizing: border-box;` | **Ocupa TODO el ancho disponible** |
| **Canvas width** | `800` (base para resolución) | Ancho base para la resolución del canvas |
| **Canvas height** | `400` (base proporcional) | Altura base para la resolución del canvas |
| **Canvas style** | `width: 100%; height: auto; display: block;` | **Escala manteniendo proporción** |

## C.3 Plantilla completa Rough.js (COPIAR ESTA)

```html
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-ejemplo" width="800" height="400" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-ejemplo')) {
    var canvas = document.getElementById('roughjs-ejemplo');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título (opcional, usar ctx para texto)
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Título del diagrama', 300, 20);
    
    // Dibujar elementos con Rough.js
    // Ejemplo: Rectángulo
    rc.rectangle(100, 50, 200, 100, { 
      fill: '#dbeafe', 
      fillStyle: 'solid', 
      stroke: '#3b82f6', 
      strokeWidth: 2, 
      roughness: 0.5 
    });
    
    // Ejemplo: Círculo
    rc.circle(300, 200, 80, { 
      fill: '#fef3c7', 
      fillStyle: 'solid', 
      stroke: '#f59e0b', 
      strokeWidth: 2, 
      roughness: 0.5 
    });
    
    // Ejemplo: Línea/Flecha
    rc.line(100, 150, 250, 150, { 
      stroke: '#22c55e', 
      strokeWidth: 3, 
      roughness: 0.5 
    });
    
    // Etiquetas con canvas nativo
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.textAlign = 'left';
    ctx.fillText('Etiqueta', 110, 100);
  }
});
</script>
```

## C.4 Paleta de colores Rough.js

### Colores principales (para elementos destacados)
| Color | Hex | Uso |
|-------|-----|-----|
| Azul | `#3b82f6` | Elementos principales, líquidos |
| Rojo | `#ef4444` | Alertas, calor, partículas grandes |
| Verde | `#22c55e` | Positivo, resultados, vectores |
| Amarillo/Ámbar | `#f59e0b` | Advertencia, energía, filtros |
| Morado | `#a855f7` | Elementos especiales, destacados |

### Colores de fondo (para rellenos)
| Color | Hex | Uso |
|-------|-----|-----|
| Azul claro | `#dbeafe` | Fondo de agua, líquidos |
| Rojo claro | `#fee2e2` | Fondo de calor, peligro |
| Verde claro | `#dcfce7` | Fondo de éxito, naturaleza |
| Amarillo claro | `#fef3c7` | Fondo de aceite, advertencia |
| Gris claro | `#f1f5f9` | Fondo neutro, sólidos |

### Colores de partículas (química/física)
| Partícula | Color | Hex |
|-----------|-------|-----|
| Protón | Rojo | `#ef4444` |
| Neutrón | Gris | `#6b7280` |
| Electrón | Azul | `#3b82f6` |
| Núcleo | Amarillo/Naranja | `#fbbf24` |

### Colores de estructura
| Elemento | Color | Hex |
|----------|-------|-----|
| Bordes/Líneas | Gris oscuro | `#475569` |
| Líneas punteadas | Gris medio | `#94a3b8` |
| Texto principal | Gris muy oscuro | `#1e293b` |
| Texto secundario | Gris | `#64748b` |

## C.5 Parámetros de Rough.js

### Roughness (rugosidad)
- `0.3-0.5`: Diagramas técnicos, precisos
- `0.6-0.8`: Diagramas ilustrativos, naturales
- `0.9-1.2`: Diagramas muy artísticos, sueltos

### FillStyle (estilo de relleno)
- `'solid'`: Relleno sólido (más común)
- `'hachure'`: Rayado diagonal
- `'zigzag'`: Zigzag
- `'cross-hatch'`: Rayado cruzado
- `'dots'`: Puntos

### StrokeWidth (grosor de línea)
- `1`: Líneas finas, detalles
- `2`: Líneas normales (más común)
- `3`: Líneas gruesas, énfasis

## C.6 Ejemplos de uso común

### Ejemplo 1: Partículas en diferentes fases
```javascript
// Sólido: partículas juntas
for (var row = 0; row < 4; row++) {
  for (var col = 0; col < 4; col++) {
    rc.circle(50 + col*20, 50 + row*20, 12, { 
      fill: '#3b82f6', 
      fillStyle: 'solid', 
      roughness: 0.4 
    });
  }
}

// Líquido: partículas dispersas
var positions = [[150,60], [170,65], [190,58], [210,63]];
positions.forEach(function(pos) {
  rc.circle(pos[0], pos[1], 12, { 
    fill: '#22c55e', 
    fillStyle: 'solid', 
    roughness: 0.5 
  });
});
```

### Ejemplo 2: Flecha con punta
```javascript
// Línea principal
rc.line(x1, y1, x2, y2, { stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5 });

// Punta de flecha
var angle = Math.atan2(y2-y1, x2-x1);
var headLen = 15;
rc.line(x2, y2, x2 - headLen * Math.cos(angle - Math.PI/6), y2 - headLen * Math.sin(angle - Math.PI/6), 
  { stroke: '#3b82f6', strokeWidth: 2 });
rc.line(x2, y2, x2 - headLen * Math.cos(angle + Math.PI/6), y2 - headLen * Math.sin(angle + Math.PI/6), 
  { stroke: '#3b82f6', strokeWidth: 2 });
```

### Ejemplo 3: Texto con canvas nativo
```javascript
ctx.font = 'bold 14px Inter, sans-serif';
ctx.fillStyle = '#1e293b';
ctx.textAlign = 'center';
ctx.fillText('Texto centrado', x, y);

ctx.textAlign = 'left';
ctx.fillText('Texto izquierda', x, y);

ctx.textAlign = 'right';
ctx.fillText('Texto derecha', x, y);
```

## C.7 Buenas prácticas Rough.js

1. **Siempre verificar disponibilidad**: `if (typeof rough !== 'undefined' && document.getElementById('id'))`
2. **Usar roughness consistente**: 0.5 es un buen valor por defecto
3. **Combinar Rough.js con canvas nativo**: Rough.js para formas, canvas para texto
4. **Mantener proporciones**: Usar variables para coordenadas relativas
5. **Añadir leyendas**: Siempre explicar colores y símbolos
6. **Responsive**: `style="width: 100%; height: auto;"` en el canvas

---

# SECCIÓN D: Chart.js (Solo fracciones)

Mantener solo para gráficos de fracciones (pie charts) donde ya esté implementado.

---

# SECCIÓN E: Three.js (Solo 3D)

Usar para cubos, volúmenes y geometría espacial.

---

## ✅ Checklist obligatorio

Antes de generar cualquier gráfico:

### Para gráficos de datos/funciones:
- [ ] ¿Necesita interactividad con arrastre? → JSXGraph
- [ ] ¿Es visualización estática? → **ECharts** ✨
- [ ] ¿Tiene el wrapper con fondo `#f1f5f9` y borde redondeado?
- [ ] ¿Tiene icono 📊 solo (sin texto)?
- [ ] ¿Es responsive (width: 100%, height: 400px)?
- [ ] ¿Tiene título descriptivo?
- [ ] ¿Tiene cuadrícula visible (#94a3b8)?
- [ ] ¿Tiene nombres de ejes en negrita?
- [ ] ¿Tiene resize listener para responsive?

### Para diagramas ilustrativos/conceptuales (Rough.js):
- [ ] ¿Es un diagrama de situación física, partículas, equipos, mapa conceptual o jerarquía? → **Rough.js** ✨
- [ ] ¿Tiene el wrapper con fondo `#f8fafc`?
- [ ] ¿El canvas es responsive (`width: 100%; height: auto;`)?
- [ ] ¿Usa la paleta de colores correcta?
- [ ] ¿Tiene leyenda explicativa si aplica?
- [ ] ¿Verifica disponibilidad de `rough`?