# **Tamizado**

## Aplicación

El tamizado se utiliza para **separar mezclas heterogéneas de sólidos**, especialmente cuando los componentes tienen **diferentes tamaños de partícula**.

---

## Principio de separación

Este método funciona gracias a la **diferencia en la granulometría** de los materiales.
Permite **clasificar o separar** los sólidos según su tamaño.

---

## Herramienta utilizada

Para realizar este proceso se emplea un **tamiz o colador**, cuyo material puede variar según la mezcla (metal, plástico, malla fina, etc.).

---

## Proceso

* Las **partículas pequeñas** atraviesan los orificios del tamiz.
* Las **partículas grandes** permanecen **retenidas** en la parte superior.

### 🎯 **Visualización del tamizado**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-tamizado" width="500" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-tamizado')) {
    var canvas = document.getElementById('roughjs-tamizado');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Separación por tamaño de partícula', 250, 15);
    
    // Tamiz (rectángulo con líneas horizontales)
    rc.rectangle(100, 70, 200, 60, { stroke: '#64748b', strokeWidth: 2, roughness: 0.7 });
    // Malla del tamiz
    for (var i = 0; i < 8; i++) {
      rc.line(110 + i*25, 100, 110 + i*25, 100, { stroke: '#94a3b8', strokeWidth: 1, roughness: 0.3 });
    }
    rc.line(100, 100, 300, 100, { stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
    
    // Partículas grandes (arriba del tamiz - retenidas)
    rc.circle(130, 85, 16, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.6 });
    rc.circle(170, 82, 18, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.6 });
    rc.circle(210, 88, 14, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.6 });
    rc.circle(250, 85, 16, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.6 });
    
    // Partículas pequeñas (cayendo y abajo)
    rc.circle(140, 115, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(180, 118, 5, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(220, 112, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(135, 145, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(165, 150, 5, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(200, 148, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(240, 155, 5, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(270, 145, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    
    // Leyenda
    ctx.font = '10px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('● Partículas grandes', 350, 80);
    ctx.fillText('   (retenidas)', 350, 93);
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('● Partículas pequeñas', 350, 115);
    ctx.fillText('   (atraviesan)', 350, 128);
    
    // Flecha indicando dirección
    ctx.font = '9px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.textAlign = 'center';
    ctx.fillText('↓ Caen por gravedad', 200, 170);
  }
});
</script>

[Ver en Tiktok](https://vt.tiktok.com/ZSBJDCbPR/)