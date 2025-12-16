---
description: Guía para generar gráficas de funciones, datos y estadísticas con ECharts globs: ["src/content/**/*.md"]
---

# 📊 Workflow: ECharts (Funciones y Datos)

ECharts es la **primera opción** para cualquier gráfica de funciones matemáticas, series de datos o visualizaciones estadísticas.

---

## ✅ Cuándo usar ECharts

| Caso de uso | Usar ECharts |
|-------------|--------------|
| Función lineal $f(x) = mx + b$ | ✅ SÍ |
| Función cuadrática $f(x) = ax^2 + bx + c$ | ✅ SÍ |
| Comparar múltiples funciones | ✅ SÍ |
| Gráfica con puntos destacados | ✅ SÍ |
| Histograma, barras | ✅ SÍ |
| Series de datos (tiempo, valores) | ✅ SÍ |
| Plano cartesiano con ejes | ✅ SÍ |
| Estadísticas descriptivas | ✅ SÍ |

---

## 🎨 Plantilla Estándar

```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="echarts-[LECCION]-[NUMERO]" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-[LECCION]-[NUMERO]')) {
    var chart = echarts.init(document.getElementById('echarts-[LECCION]-[NUMERO]'));
    
    var option = {
      title: {
        text: 'TÍTULO DEL GRÁFICO',
        subtext: 'f(x) = expresión',
        left: 'center',
        textStyle: { fontSize: 16, fontWeight: 'bold', color: '#1e293b' },
        subtextStyle: { fontSize: 13, color: '#3b82f6', fontWeight: 'bold' }
      },
      animation: true,
      animationDuration: 1000,
      grid: { 
        left: '12%', right: '8%', top: '18%', bottom: '15%',
        show: true, borderColor: '#cbd5e1'
      },
      xAxis: {
        type: 'value',
        name: 'x',
        nameLocation: 'middle',
        nameGap: 28,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: -5, max: 5,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } }
      },
      yAxis: {
        type: 'value',
        name: 'y',
        nameLocation: 'middle',
        nameGap: 35,
        nameTextStyle: { fontSize: 13, fontWeight: 'bold', color: '#374151' },
        min: -5, max: 10,
        axisLine: { onZero: true, lineStyle: { color: '#374151', width: 2 } },
        splitLine: { show: true, lineStyle: { color: '#94a3b8', type: 'dashed' } }
      },
      series: [
        {
          name: 'f(x)',
          type: 'line',
          smooth: true,
          symbol: 'none',
          lineStyle: { width: 3, color: '#3b82f6' },
          itemStyle: { color: '#3b82f6' },  // IMPORTANTE para leyenda
          data: [/* puntos */]
        }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>
```

---

## 📐 Ejemplos por Tipo

### Función Lineal

```javascript
// f(x) = 2x + 1
// Generar puntos
var data = [];
for (var x = -5; x <= 5; x += 0.5) {
  data.push([x, 2*x + 1]);
}

series: [{
  type: 'line',
  symbol: 'none',
  lineStyle: { width: 3, color: '#3b82f6' },
  itemStyle: { color: '#3b82f6' },
  data: data
}]
```

### Función Cuadrática

```javascript
// f(x) = x² - 4
var data = [];
for (var x = -4; x <= 4; x += 0.2) {
  data.push([x, x*x - 4]);
}

series: [{
  type: 'line',
  smooth: true,
  symbol: 'none',
  lineStyle: { width: 3, color: '#ef4444' },
  itemStyle: { color: '#ef4444' },
  data: data
}]
```

### Comparación de Funciones

```javascript
// y = x, y = 2x, y = 0.5x
var data1 = [], data2 = [], data3 = [];
for (var x = -5; x <= 5; x += 0.5) {
  data1.push([x, x]);
  data2.push([x, 2*x]);
  data3.push([x, 0.5*x]);
}

legend: {
  data: ['y = x', 'y = 2x', 'y = 0.5x'],
  top: 30
},
series: [
  { name: 'y = x', type: 'line', lineStyle: { color: '#3b82f6' }, itemStyle: { color: '#3b82f6' }, data: data1 },
  { name: 'y = 2x', type: 'line', lineStyle: { color: '#ef4444' }, itemStyle: { color: '#ef4444' }, data: data2 },
  { name: 'y = 0.5x', type: 'line', lineStyle: { color: '#22c55e' }, itemStyle: { color: '#22c55e' }, data: data3 }
]
```

### Puntos Destacados

```javascript
// Función con puntos marcados
series: [
  {
    name: 'Función',
    type: 'line',
    data: functionData
  },
  {
    name: 'Puntos clave',
    type: 'scatter',
    symbolSize: 12,
    itemStyle: { color: '#ef4444', borderColor: '#fff', borderWidth: 2 },
    label: {
      show: true,
      formatter: function(p) { return '(' + p.data[0] + ', ' + p.data[1] + ')'; },
      position: 'top',
      fontSize: 11,
      fontWeight: 'bold'
    },
    data: [[0, 1], [2, 5], [-1, -1]]  // Puntos a destacar
  }
]
```

### Histograma

```javascript
xAxis: {
  type: 'category',
  data: ['0-10', '10-20', '20-30', '30-40', '40-50']
},
yAxis: {
  type: 'value',
  name: 'Frecuencia'
},
series: [{
  type: 'bar',
  data: [5, 12, 8, 15, 10],
  itemStyle: { color: '#3b82f6' }
}]
```

---

## 🎨 Paleta de Colores

| Uso | Color | Hex |
|-----|-------|-----|
| Función principal | Azul | `#3b82f6` |
| Función secundaria | Rojo | `#ef4444` |
| Función terciaria | Verde | `#22c55e` |
| Puntos destacados | Naranja | `#f97316` |
| Cuadrícula | Gris | `#94a3b8` |
| Ejes | Gris oscuro | `#374151` |

---

## ⚠️ Regla Crítica: itemStyle

> **SIEMPRE** incluir `itemStyle` con el mismo color que `lineStyle` para que la leyenda muestre el color correcto.

```javascript
// ❌ INCORRECTO (leyenda con color incorrecto)
{ lineStyle: { color: '#3b82f6' }, data: data }

// ✅ CORRECTO
{ lineStyle: { color: '#3b82f6' }, itemStyle: { color: '#3b82f6' }, data: data }
```

---

## ✅ Checklist

- [ ] ID único: `echarts-[leccion]-[numero]`
- [ ] Wrapper con fondo `#f1f5f9`
- [ ] Icono 📊 sin texto adicional
- [ ] `DOMContentLoaded` wrapper
- [ ] Verificación: `if (typeof echarts !== 'undefined')`
- [ ] Título descriptivo
- [ ] Nombres de ejes
- [ ] Cuadrícula visible (`splitLine.show: true`)
- [ ] `itemStyle` igual que `lineStyle`
- [ ] Resize listener

---

## 📐 Triángulos con Etiquetas (IMPORTANTE)

> **PROBLEMA COMÚN:** Las etiquetas se superponen con las líneas del triángulo y no se leen bien.

### ✅ Solución: Etiquetas con fondo y offset

Las etiquetas deben tener:
1. **Fondo blanco/claro** para destacarse de las líneas
2. **Offset calculado** para alejarse del centro de cada lado
3. **Bordes redondeados** para mejor legibilidad

### Plantilla de Triángulo con Etiquetas Claras

```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📐</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Triángulo rectángulo con razones</strong>
  </div>
  <div id="echarts-triangulo-ejemplo" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-triangulo-ejemplo')) {
    var chart = echarts.init(document.getElementById('echarts-triangulo-ejemplo'));
    
    // Coordenadas del triángulo rectángulo 3-4-5
    var A = [50, 280];   // Vértice inferior izquierdo (ángulo θ)
    var B = [290, 280];  // Vértice inferior derecho (ángulo recto)
    var C = [290, 100];  // Vértice superior (opuesto a θ)
    
    // CÁLCULO DE POSICIONES DE ETIQUETAS (offset hacia afuera)
    // Lado horizontal (Adyacente): centro + offset hacia abajo
    var labelAdyX = (A[0] + B[0]) / 2;
    var labelAdyY = A[1] + 35;  // 35px debajo de la línea
    
    // Lado vertical (Opuesto): centro + offset hacia la derecha
    var labelOpX = B[0] + 40;   // 40px a la derecha de la línea
    var labelOpY = (B[1] + C[1]) / 2;
    
    // Hipotenusa: centro + offset hacia arriba-izquierda
    var labelHipX = (A[0] + C[0]) / 2 - 50;  // 50px a la izquierda
    var labelHipY = (A[1] + C[1]) / 2 - 20;  // 20px arriba
    
    var option = {
      title: {
        text: 'Triángulo 3-4-5: Las 6 razones respecto a θ',
        left: 'center',
        top: 10,
        textStyle: { fontSize: 15, fontWeight: 'bold', color: '#1e293b' }
      },
      grid: { show: false },
      xAxis: { show: false, min: 0, max: 400 },
      yAxis: { show: false, min: 0, max: 350 },
      series: [{
        type: 'line',
        data: [A, B, C, A],
        lineStyle: { color: '#1e293b', width: 3 },
        symbol: 'circle',
        symbolSize: 10,
        itemStyle: { color: '#1e293b' }
      }],
      graphic: [
        // ===== ETIQUETAS CON FONDO (CLAVE DEL ÉXITO) =====
        
        // Lado Adyacente (horizontal, abajo)
        {
          type: 'text',
          left: labelAdyX - 60,
          top: labelAdyY,
          style: {
            text: '4 (Adyacente)',
            fontSize: 14,
            fontWeight: 'bold',
            fill: '#22c55e',
            backgroundColor: '#ffffff',
            padding: [4, 8],
            borderRadius: 4,
            shadowColor: 'rgba(0,0,0,0.1)',
            shadowBlur: 3
          }
        },
        // Lado Opuesto (vertical, a la derecha)
        {
          type: 'text',
          left: labelOpX,
          top: labelOpY - 10,
          style: {
            text: '3\n(Opuesto)',
            fontSize: 14,
            fontWeight: 'bold',
            fill: '#ef4444',
            backgroundColor: '#ffffff',
            padding: [4, 8],
            borderRadius: 4,
            shadowColor: 'rgba(0,0,0,0.1)',
            shadowBlur: 3
          }
        },
        // Hipotenusa (diagonal, arriba-izquierda)
        {
          type: 'text',
          left: labelHipX,
          top: labelHipY,
          style: {
            text: '5 (Hip)',
            fontSize: 14,
            fontWeight: 'bold',
            fill: '#3b82f6',
            backgroundColor: '#ffffff',
            padding: [4, 8],
            borderRadius: 4,
            shadowColor: 'rgba(0,0,0,0.1)',
            shadowBlur: 3
          }
        },
        // Ángulo θ
        {
          type: 'text',
          left: A[0] + 25,
          top: A[1] - 45,
          style: {
            text: 'θ',
            fontSize: 20,
            fontWeight: 'bold',
            fill: '#3b82f6'
          }
        },
        // Símbolo de ángulo recto
        {
          type: 'rect',
          shape: { x: B[0] - 20, y: B[1] - 20, width: 18, height: 18 },
          style: { stroke: '#64748b', fill: 'transparent', lineWidth: 2 }
        }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>
```

### Reglas de Posicionamiento de Etiquetas

| Lado del triángulo | Posición del offset | Dirección |
|--------------------|---------------------|-----------|
| Horizontal (base) | Centro del lado + 30-40px hacia ABAJO | `top: centroY + 35` |
| Vertical | Centro del lado + 35-45px hacia la DERECHA | `left: centroX + 40` |
| Diagonal/Hipotenusa | Centro + offset hacia el EXTERIOR (opuesto al ángulo recto) | Calcular dirección normal |

### Propiedades clave del `style` para etiquetas

```javascript
{
  type: 'text',
  style: {
    text: 'Etiqueta',
    fontSize: 14,
    fontWeight: 'bold',
    fill: '#color',
    // ⬇️ ESTAS 4 PROPIEDADES SON CLAVE ⬇️
    backgroundColor: '#ffffff',  // Fondo blanco
    padding: [4, 8],             // Espacio interno
    borderRadius: 4,             // Bordes redondeados
    shadowColor: 'rgba(0,0,0,0.1)',
    shadowBlur: 3                // Sombra sutil
  }
}
```

### ❌ Error común vs ✅ Correcto

```javascript
// ❌ INCORRECTO: Etiqueta sin fondo, se superpone
{
  type: 'text',
  left: '45%',  // Porcentaje impreciso
  top: '50%',
  style: { text: '3', fill: '#ef4444' }
}

// ✅ CORRECTO: Etiqueta con fondo y offset calculado
{
  type: 'text',
  left: B[0] + 40,  // Offset desde vértice
  top: (B[1] + C[1]) / 2 - 10,  // Centro del lado + ajuste
  style: {
    text: '3 (Opuesto)',
    fill: '#ef4444',
    backgroundColor: '#ffffff',
    padding: [4, 8],
    borderRadius: 4
  }
}
```

---

## 🔗 Relacionados

- [Árbol de decisión](../CLAUDE.md#-árbol-de-decisión)
- [Geometría exacta](./geometry-exact.md) - Para cuando NO usar ECharts