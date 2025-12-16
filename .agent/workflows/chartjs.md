---
description: Guía para visualizar fracciones con gráficos de pastel usando Chart.js globs: ["src/content/**/*.md"]
---

# 🥧 Workflow: Chart.js (Fracciones)

Chart.js se usa **exclusivamente** para visualizar fracciones como gráficos de pastel (pie charts).

---

## ✅ Cuándo usar Chart.js

| Caso de uso | Usar Chart.js |
|-------------|---------------|
| Fracción 3/4 como pastel | ✅ SÍ |
| Comparar fracciones visualmente | ✅ SÍ |
| Porcentajes como sectores | ✅ SÍ |

### ❌ NO usar Chart.js para:

- Gráficas de funciones → ECharts
- Histogramas, barras → ECharts
- Diagramas ilustrativos → Rough.js

---

## 🎨 Plantilla Estándar

```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; max-width: 300px;">
  <canvas id="chartjs-[LECCION]-[NUMERO]"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined' && document.getElementById('chartjs-[LECCION]-[NUMERO]')) {
    var ctx = document.getElementById('chartjs-[LECCION]-[NUMERO]').getContext('2d');
    new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ['Parte tomada', 'Parte restante'],
        datasets: [{
          data: [3, 1],  // 3/4 = 3 partes de 4
          backgroundColor: ['#3b82f6', '#e2e8f0'],
          borderColor: ['#2563eb', '#cbd5e1'],
          borderWidth: 2
        }]
      },
      options: {
        responsive: true,
        plugins: {
          title: {
            display: true,
            text: 'Fracción 3/4',
            font: { size: 16, weight: 'bold' }
          },
          legend: {
            position: 'bottom'
          }
        }
      }
    });
  }
});
</script>
```

---

## 📐 Ejemplos

### Fracción Simple (3/4)

```javascript
data: {
  labels: ['3 partes', '1 parte'],
  datasets: [{
    data: [3, 1],
    backgroundColor: ['#3b82f6', '#e2e8f0']
  }]
}
```

### Comparar Fracciones

```html
<div style="display: flex; gap: 1rem; flex-wrap: wrap;">
  <div style="background: #f1f5f9; border-radius: 12px; padding: 1rem; width: 200px;">
    <canvas id="chartjs-fraccion-1"></canvas>
  </div>
  <div style="background: #f1f5f9; border-radius: 12px; padding: 1rem; width: 200px;">
    <canvas id="chartjs-fraccion-2"></canvas>
  </div>
</div>
```

### Porcentajes

```javascript
data: {
  labels: ['Aprobados (75%)', 'Reprobados (25%)'],
  datasets: [{
    data: [75, 25],
    backgroundColor: ['#22c55e', '#ef4444']
  }]
}
```

---

## 🎨 Paleta de Colores

| Uso | Color | Hex |
|-----|-------|-----|
| Parte principal | Azul | `#3b82f6` |
| Parte secundaria | Gris claro | `#e2e8f0` |
| Positivo/Aprobado | Verde | `#22c55e` |
| Negativo/Reprobado | Rojo | `#ef4444` |

---

## ✅ Checklist

- [ ] ID único: `chartjs-[leccion]-[numero]`
- [ ] Wrapper con fondo `#f1f5f9`
- [ ] `max-width: 300px` (pie charts no deben ser muy grandes)
- [ ] `DOMContentLoaded` wrapper
- [ ] Verificación: `if (typeof Chart !== 'undefined')`
- [ ] Título descriptivo
- [ ] Leyenda en `position: 'bottom'`

---

## 🔗 Relacionados

- [ECharts](./echarts.md) - Para otros tipos de gráficos
- [Árbol de decisión](./illustration-decision.md)