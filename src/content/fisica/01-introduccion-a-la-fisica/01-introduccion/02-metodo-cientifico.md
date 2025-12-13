# **Método Científico**

## 🔬 **Definición**

El **método científico** es un proceso ordenado que permite  
> **investigar fenómenos naturales**, formular **explicaciones comprobables** y obtener **conocimiento confiable**.

## ⚙️ **Etapas del método científico**

1. **Observación:** notar un fenómeno o situación que despierta curiosidad.  
2. **Planteamiento del problema:** formular una pregunta clara.  
3. **Hipótesis:** proponer una posible explicación o respuesta.  
4. **Experimentación:** realizar pruebas controladas para comprobar la hipótesis.  
5. **Análisis de resultados:** organizar los datos y buscar patrones.  
6. **Conclusión:** aceptar, rechazar o modificar la hipótesis según la evidencia.  
7. **Comunicación:** compartir los resultados con la comunidad científica.

### 🎯 **Visualización: El ciclo del Método Científico**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-metodo" width="600" height="400" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-metodo')) {
    var canvas = document.getElementById('roughjs-metodo');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Coordenadas para los pasos (en forma de ciclo/U)
    var step1 = {x: 100, y: 50, color: '#f59e0b', text: '1. Observación'};
    var step2 = {x: 300, y: 50, color: '#ef4444', text: '2. Pregunta'};
    var step3 = {x: 500, y: 50, color: '#a855f7', text: '3. Hipótesis'};
    var step4 = {x: 500, y: 150, color: '#3b82f6', text: '4. Experimento'};
    var step5 = {x: 300, y: 150, color: '#10b981', text: '5. Análisis'};
    var step6 = {x: 100, y: 150, color: '#6366f1', text: '6. Conclusión'};
    
    function drawStep(step) {
      rc.rectangle(step.x - 70, step.y - 20, 140, 40, { fill: step.color, fillStyle: 'solid', fillWeight: 3, roughness: 0.5, stroke: '#1e293b' });
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText(step.text, step.x, step.y + 5);
    }
    
    // Dibujar pasos
    drawStep(step1);
    drawStep(step2);
    drawStep(step3);
    drawStep(step4);
    drawStep(step5);
    drawStep(step6);
    
    // Flechas conectoras
    function drawArrow(x1, y1, x2, y2) {
      rc.line(x1, y1, x2, y2, { stroke: '#475569', strokeWidth: 2, roughness: 0.5 });
      // Punta de flecha simple
      var angle = Math.atan2(y2-y1, x2-x1);
      rc.line(x2, y2, x2 - 10 * Math.cos(angle - Math.PI/6), y2 - 10 * Math.sin(angle - Math.PI/6), { stroke: '#475569', strokeWidth: 2 });
      rc.line(x2, y2, x2 - 10 * Math.cos(angle + Math.PI/6), y2 - 10 * Math.sin(angle + Math.PI/6), { stroke: '#475569', strokeWidth: 2 });
    }
    
    drawArrow(170, 50, 230, 50); // 1->2
    drawArrow(370, 50, 430, 50); // 2->3
    drawArrow(500, 70, 500, 130); // 3->4 (bajada)
    drawArrow(430, 150, 370, 150); // 4->5 (izquierda)
    drawArrow(230, 150, 170, 150); // 5->6 (izquierda)
    
    // Ciclo de retroalimentación (si la hipótesis falla)
    rc.path('M 300 130 C 300 100, 450 100, 480 70', { stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.5, strokeLineDash: [5, 5] });
    ctx.fillStyle = '#64748b';
    ctx.font = '10px Inter, sans-serif';
    ctx.fillText('↺ Replantear', 390, 105);
    
    // Paso 7: Comunicación (abajo al centro)
    var step7 = {x: 300, y: 250, color: '#ec4899', text: '7. Comunicación'};
    drawStep(step7);
    drawArrow(100, 170, 100, 250); // 6->abajo
    drawArrow(100, 250, 230, 250); // derecha a 7
  }
});
</script>

> 🔁 Estas etapas no siempre son lineales: en la práctica, pueden repetirse o ajustarse según los hallazgos.

---

## 🧪 **Ejemplo aplicado a la física**

> **Situación:** una pelota se detiene después de rodar.  
> **Pregunta:** ¿por qué se detiene?  
> **Hipótesis:** “porque hay fricción con el suelo.”  
> **Experimento:** hacer rodar pelotas sobre distintas superficies.  
> **Resultado:** la pelota se detiene más rápido en superficies rugosas que en lisas.  
> **Conclusión:** la **fricción** se opone al movimiento y disipa energía.

---

## 🔎 **Características del método científico**

| **Propiedad** | **Descripción** |
|:---------------|:----------------|
| **Sistemático** | Sigue un conjunto de pasos ordenados. |
| **Objetivo** | Se basa en hechos observables, no en opiniones. |
| **Reproducible** | Los resultados pueden repetirse por otros investigadores. |
| **Perfectible** | Sus conclusiones pueden cambiar con nueva evidencia. |

---

## 📚 **Aplicación en la física**

La física emplea el método científico para:

- Formular **leyes y teorías** basadas en observaciones y experimentos.  
- Explicar **cómo y por qué** ocurren los fenómenos naturales.  
- Predecir **nuevos comportamientos** de la materia y la energía.

> 💬 En otras palabras, la física **no solo describe**, sino que **explica y predice** los fenómenos con base en la evidencia.

---

### 💡 **Conclusión**

> El método científico es la **base del conocimiento en física**,  
> pues permite **comprobar ideas con evidencia**  
> y construir **leyes universales** que describen la naturaleza.
