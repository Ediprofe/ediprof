# **Filtración**

## Aplicación

La filtración se utiliza para **separar un sólido insoluble de un líquido**, formando una mezcla heterogénea donde el sólido no se disuelve.

---

## Principio de separación

Este método se basa en la **diferencia de tamaño de partículas**.
El **filtro** permite el paso del **líquido** (partículas pequeñas) y **retiene el sólido** (partículas grandes).

---

## Herramienta utilizada

Para realizar la filtración se emplea un **filtro** elaborado con **papel, tela o cualquier material poroso** que permita el paso del líquido pero detenga al sólido.

---

## Proceso

* El **líquido** atraviesa el filtro y se recoge en un recipiente.
* El **sólido** queda **retenido** en el material filtrante.

### 🎯 **Visualización de la filtración**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-filtracion" width="500" height="200" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-filtracion')) {
    var canvas = document.getElementById('roughjs-filtracion');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Embudo (triángulo invertido)
    rc.line(120, 40, 180, 120, { stroke: '#64748b', strokeWidth: 2, roughness: 0.7 });
    rc.line(280, 40, 220, 120, { stroke: '#64748b', strokeWidth: 2, roughness: 0.7 });
    rc.line(120, 40, 280, 40, { stroke: '#64748b', strokeWidth: 2, roughness: 0.7 });
    
    // Filtro (papel dentro del embudo)
    rc.line(140, 55, 200, 110, { stroke: '#f59e0b', strokeWidth: 2, roughness: 0.5 });
    rc.line(260, 55, 200, 110, { stroke: '#f59e0b', strokeWidth: 2, roughness: 0.5 });
    rc.line(140, 55, 260, 55, { stroke: '#f59e0b', strokeWidth: 2, roughness: 0.5 });
    
    // Sólido retenido en el filtro
    rc.circle(170, 75, 8, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(190, 80, 7, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(210, 72, 8, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(230, 78, 7, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(200, 90, 6, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    
    // Tubo del embudo
    rc.rectangle(192, 120, 16, 40, { stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
    
    // Gotas de líquido cayendo
    rc.circle(200, 130, 4, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.4 });
    rc.circle(200, 145, 4, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.4 });
    
    // Recipiente (vaso de precipitados)
    rc.rectangle(160, 165, 80, 30, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#64748b', strokeWidth: 2, roughness: 0.6 });
    
    // Leyenda
    ctx.font = '10px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('📄 Filtro (papel)', 340, 60);
    ctx.fillStyle = '#6b7280';
    ctx.fillText('● Sólido retenido', 340, 85);
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('💧 Líquido filtrado', 340, 110);
    
    // Etiquetas
    ctx.font = 'bold 10px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Embudo', 200, 35);
    ctx.fillText('Recipiente', 200, 180);
  }
});
</script>

[Ver en Tiktok](https://vt.tiktok.com/ZSBJDkqwh/)