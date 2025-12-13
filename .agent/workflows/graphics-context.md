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

## 📐 Estilo visual obligatorio para TODOS los gráficos

Todos los gráficos deben seguir este wrapper visual:

```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="CHART-ID" style="width: 100%; height: 400px; border-radius: 8px;"></div>
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
| Ancho | `100%` | Responsive, ocupa todo el ancho |
| Alto | `400px` | Altura decente para visualización |

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

1. **Título descriptivo** con subtítulo de la función
2. **Cuadrícula visible** con color `#94a3b8`
3. **Nombres de ejes** en negrita
4. **Responsive** con resize listener
5. **Animación** de entrada

## A.3 Plantilla completa ECharts (COPIAR ESTA)

```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-NOMBRE" style="width: 100%; height: 400px; border-radius: 8px;"></div>
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

```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-NOMBRE" style="width: 100%; height: 400px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-NOMBRE')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-NOMBRE', {
      boundingbox: [-1, 7, 9, -1],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // ... elementos interactivos ...
    
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

# SECCIÓN C: Chart.js (Solo fracciones)

Mantener solo para gráficos de fracciones (pie charts) donde ya esté implementado.

---

# SECCIÓN D: Three.js (Solo 3D)

Usar para cubos, volúmenes y geometría espacial.

---

## ✅ Checklist obligatorio

Antes de generar cualquier gráfico:

- [ ] ¿Necesita interactividad con arrastre? → JSXGraph
- [ ] ¿Es visualización estática? → **ECharts** ✨
- [ ] ¿Tiene el wrapper con fondo `#f1f5f9` y borde redondeado?
- [ ] ¿Tiene icono 📊 solo (sin texto)?
- [ ] ¿Es responsive (width: 100%, height: 400px)?
- [ ] ¿Tiene título descriptivo?
- [ ] ¿Tiene cuadrícula visible (#94a3b8)?
- [ ] ¿Tiene nombres de ejes en negrita?
- [ ] ¿Tiene resize listener para responsive?
