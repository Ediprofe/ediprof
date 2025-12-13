# **Decantación**

## Aplicación

La decantación se utiliza para **separar líquidos inmiscibles**, es decir, aquellos que **no se mezclan entre sí** y permanecen en capas diferentes dentro del recipiente.

---

## Líquidos inmiscibles

Los líquidos inmiscibles **no se disuelven uno en el otro**, por lo que forman una **mezcla heterogénea** en la que sus componentes son claramente **visibles**.
Un ejemplo común es **agua y aceite**.

---

## Principio de separación

La separación se realiza gracias a la **diferencia de densidades** entre los líquidos.
Cada uno se acomoda según su densidad: el más denso abajo y el menos denso arriba.

---

## Comportamiento de los líquidos

* El **líquido menos denso** queda **arriba**.
* El **líquido más denso** queda **abajo**.

---

## Instrumento utilizado

Para realizar la decantación se utiliza un **embudo de decantación**, que permite separar los líquidos de manera controlada.

---

## Mecanismo

* Se **agregan los líquidos** en el embudo de decantación.
* Se **abre la válvula inferior** para dejar salir únicamente el **líquido más denso**.
* El **líquido menos denso** permanece en el embudo hasta que sea el momento de separarlo.

### 🎯 **Visualización de la decantación**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-decantacion" width="500" height="220" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-decantacion')) {
    var canvas = document.getElementById('roughjs-decantacion');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Embudo de decantación: Separación por densidad', 250, 15);
    
    // Embudo de decantación (forma de pera)
    rc.line(120, 35, 180, 140, { stroke: '#64748b', strokeWidth: 2, roughness: 0.7 });
    rc.line(280, 35, 220, 140, { stroke: '#64748b', strokeWidth: 2, roughness: 0.7 });
    rc.line(120, 35, 280, 35, { stroke: '#64748b', strokeWidth: 2, roughness: 0.7 });
    
    // Líquido menos denso (arriba - amarillo/aceite)
    rc.rectangle(125, 40, 150, 50, { fill: '#fef3c7', fillStyle: 'solid', stroke: 'transparent', roughness: 0.3 });
    
    // Líquido más denso (abajo - azul/agua)
    rc.rectangle(155, 90, 90, 50, { fill: '#dbeafe', fillStyle: 'solid', stroke: 'transparent', roughness: 0.3 });
    
    // Válvula
    rc.rectangle(192, 140, 16, 15, { fill: '#6b7280', fillStyle: 'solid', stroke: '#374151', roughness: 0.5 });
    
    // Tubo de salida
    rc.rectangle(192, 155, 16, 30, { stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
    
    // Gotas del líquido denso saliendo
    rc.circle(200, 175, 5, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.4 });
    rc.circle(200, 190, 5, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.4 });
    
    // Recipiente
    rc.rectangle(170, 200, 60, 15, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#64748b', strokeWidth: 2, roughness: 0.6 });
    
    // Leyenda
    ctx.font = '10px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('🟡 Aceite (menos denso)', 340, 50);
    ctx.fillText('    → Queda arriba', 340, 65);
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('💧 Agua (más densa)', 340, 95);
    ctx.fillText('    → Sale primero', 340, 110);
    ctx.fillStyle = '#6b7280';
    ctx.fillText('🔧 Válvula de control', 340, 135);
    
    // Flechas indicando capas
    ctx.font = '9px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.textAlign = 'center';
    ctx.fillText('↑ Menos denso', 90, 60);
    ctx.fillText('↓ Más denso', 90, 120);
  }
});
</script>