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

## 🔗 Relacionados

- [Árbol de decisión](../CLAUDE.md#-árbol-de-decisión)
- [Geometría exacta](./geometry-exact.md) - Para cuando NO usar ECharts