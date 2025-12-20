# 🚀 **Introducción a la Cinemática**

La **Mecánica** es la rama de la física encargada de estudiar el movimiento de los cuerpos y su evolución en el tiempo. Para su estudio, se divide principalmente en dos grandes áreas que, aunque están relacionadas, responden preguntas diferentes:

1.  **Cinemática:** Describe **cómo** se mueven los cuerpos sin atender a las causas.
2.  **Dinámica:** Estudia el **porqué** se mueven los cuerpos (las causas).

---

## 🆚 **Diferencias Clave: Cinemática vs. Dinámica**

Aunque ambas estudian el movimiento, se enfocan en variables distintas. Imaginemos un automóvil frenando ante un semáforo.

### **1. El enfoque de la Cinemática**
Se centra en la descripción geométrica y matemática del movimiento. Sus variables principales son:

* **Posición ($x$):** Dónde está el objeto.
* **Velocidad ($v$):** Qué tan rápido cambia de posición.
* **Aceleración ($a$):** Qué tan rápido cambia su velocidad.

> **En el ejemplo del auto:** La cinemática calcula la distancia que recorre hasta detenerse y cuánto tiempo tarda, basándose en su velocidad inicial y su desaceleración.

### **2. El enfoque de la Dinámica**
Se centra en las **fuerzas** y la **masa**, es decir, las interacciones que provocan el movimiento.

* **Fuerza ($F$):** La interacción que causa el cambio de estado.
* **Masa ($m$):** La resistencia del cuerpo a cambiar su movimiento.

> **En el ejemplo del auto:** La dinámica estudia la fuerza de fricción entre los neumáticos y el asfalto que provoca que el auto se detenga.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <canvas id="rough-cinem-vs-dinam" width="600" height="280" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var canvas = document.getElementById('rough-cinem-vs-dinam');
  if (!canvas || typeof rough === 'undefined') return;
  
  var rc = rough.canvas(canvas);
  var ctx = canvas.getContext('2d');
  
  // === TÍTULO MECÁNICA (arriba, englobando ambas) ===
  rc.rectangle(120, 5, 360, 40, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', strokeWidth: 2, roughness: 1 });
  ctx.font = 'bold 18px Inter, sans-serif';
  ctx.fillStyle = '#b45309';
  ctx.textAlign = 'center';
  ctx.fillText('⚙️ MECÁNICA', 300, 32);
  
  // Flechas que conectan MECÁNICA con ambas ramas
  rc.line(200, 45, 135, 75, { stroke: '#f59e0b', strokeWidth: 2, roughness: 0.5 });
  rc.line(400, 45, 465, 75, { stroke: '#f59e0b', strokeWidth: 2, roughness: 0.5 });
  
  // === CINEMÁTICA (izquierda) ===
  rc.rectangle(15, 75, 220, 85, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', strokeWidth: 2, roughness: 1 });
  
  ctx.font = 'bold 15px Inter, sans-serif';
  ctx.fillStyle = '#1d4ed8';
  ctx.textAlign = 'center';
  ctx.fillText('CINEMÁTICA', 125, 98);
  
  ctx.font = '11px Inter, sans-serif';
  ctx.fillStyle = '#1e40af';
  ctx.fillText('¿CÓMO se mueve?', 125, 115);
  
  ctx.font = '11px Inter, sans-serif';
  ctx.fillStyle = '#1e293b';
  ctx.textAlign = 'left';
  ctx.fillText('• Posición (x)', 30, 135);
  ctx.fillText('• Velocidad (v)', 120, 135);
  ctx.fillText('• Aceleración (a)', 30, 150);
  
  // === DINÁMICA (derecha) ===
  rc.rectangle(365, 75, 220, 85, { fill: '#fee2e2', fillStyle: 'solid', stroke: '#ef4444', strokeWidth: 2, roughness: 1 });
  
  ctx.font = 'bold 15px Inter, sans-serif';
  ctx.fillStyle = '#dc2626';
  ctx.textAlign = 'center';
  ctx.fillText('DINÁMICA', 475, 98);
  
  ctx.font = '11px Inter, sans-serif';
  ctx.fillStyle = '#b91c1c';
  ctx.fillText('¿POR QUÉ se mueve?', 475, 115);
  
  ctx.font = '11px Inter, sans-serif';
  ctx.fillStyle = '#1e293b';
  ctx.textAlign = 'left';
  ctx.fillText('• Fuerza (F)', 380, 135);
  ctx.fillText('• Masa (m)', 480, 135);
  ctx.fillText('• Leyes de Newton', 380, 150);
  
  // === SITUACIÓN CONCRETA: Auto frenando ===
  ctx.font = 'bold 12px Inter, sans-serif';
  ctx.fillStyle = '#64748b';
  ctx.textAlign = 'center';
  ctx.fillText('📍 SITUACIÓN: Un auto frena ante un semáforo', 300, 180);
  
  // Carretera
  rc.rectangle(50, 205, 500, 25, { fill: '#94a3b8', fillStyle: 'solid', stroke: '#64748b', roughness: 0.5 });
  
  // Auto
  rc.rectangle(130, 185, 80, 35, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 1 });
  rc.rectangle(145, 165, 50, 22, { fill: '#60a5fa', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 1 });
  rc.circle(150, 222, 16, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
  rc.circle(195, 222, 16, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
  
  // Semáforo
  rc.rectangle(470, 175, 20, 50, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.8 });
  rc.circle(480, 185, 12, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
  rc.circle(480, 200, 12, { fill: '#fef3c7', fillStyle: 'solid', roughness: 0.5 });
  rc.circle(480, 215, 12, { fill: '#d1d5db', fillStyle: 'solid', roughness: 0.5 });
  
  // Flecha de velocidad (decreciente)
  rc.line(215, 195, 280, 195, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
  rc.line(270, 188, 280, 195, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
  rc.line(270, 202, 280, 195, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
  
  // Fuerza de fricción (hacia atrás)
  rc.line(130, 210, 80, 210, { stroke: '#ef4444', strokeWidth: 3, roughness: 0.5 });
  rc.line(90, 203, 80, 210, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
  rc.line(90, 217, 80, 210, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
  
  // Etiquetas
  ctx.font = 'bold 10px Inter, sans-serif';
  ctx.fillStyle = '#22c55e';
  ctx.fillText('v → (velocidad)', 230, 190);
  
  ctx.fillStyle = '#ef4444';
  ctx.fillText('← F (fricción)', 60, 255);
  
  // Cajas de análisis abajo
  rc.rectangle(50, 240, 170, 35, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', roughness: 0.8 });
  ctx.font = '10px Inter, sans-serif';
  ctx.fillStyle = '#1d4ed8';
  ctx.textAlign = 'center';
  ctx.fillText('CINEMÁTICA: ¿Cuánto', 135, 253);
  ctx.fillText('tarda en detenerse?', 135, 266);
  
  rc.rectangle(380, 240, 170, 35, { fill: '#fee2e2', fillStyle: 'solid', stroke: '#ef4444', roughness: 0.8 });
  ctx.fillStyle = '#dc2626';
  ctx.fillText('DINÁMICA: ¿Qué fuerza', 465, 253);
  ctx.fillText('lo detiene?', 465, 266);
});
</script>

---

## 🌍 **Cinemática en la vida cotidiana**

La cinemática está presente siempre que observamos un cambio de posición:

* **Deportes:** La trayectoria parabólica de un balón de fútbol al ser pateado.
* **Transporte:** Calcular el tiempo de llegada de un vuelo conociendo la distancia y la velocidad media de crucero.
* **Tecnología:** El acelerómetro de un celular que detecta el cambio de orientación de la pantalla.

---

## 📍 **El Modelo de Partícula**

En física, para simplificar el estudio del movimiento, a menudo utilizamos el **modelo de partícula**.

Este modelo consiste en considerar al cuerpo como si fuera **un solo punto geométrico** donde se concentra toda su masa, ignorando:
* Su tamaño real.
* Su forma.
* Su rotación interna.

$$
\text{Cuerpo real} \rightarrow \text{Punto másico} \, (x, y, z)
$$

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <canvas id="rough-particula" width="460" height="150" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var canvas = document.getElementById('rough-particula');
  if (!canvas || typeof rough === 'undefined') return;
  
  var rc = rough.canvas(canvas);
  var ctx = canvas.getContext('2d');
  
  // === CUERPO REAL (Auto a la izquierda) ===
  // Carrocería
  rc.rectangle(30, 50, 110, 50, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 1 });
  // Techo
  rc.rectangle(50, 20, 70, 35, { fill: '#60a5fa', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 1 });
  // Ruedas
  rc.circle(60, 105, 24, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
  rc.circle(110, 105, 24, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
  
  // Etiqueta
  ctx.font = 'bold 12px Inter, sans-serif';
  ctx.fillStyle = '#1e293b';
  ctx.textAlign = 'center';
  ctx.fillText('Cuerpo Real', 85, 140);
  
  // === FLECHA DE TRANSFORMACIÓN ===
  rc.line(165, 65, 255, 65, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
  rc.line(245, 55, 255, 65, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
  rc.line(245, 75, 255, 65, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
  
  ctx.font = '11px Inter, sans-serif';
  ctx.fillStyle = '#16a34a';
  ctx.fillText('Modelo de', 210, 50);
  ctx.fillText('Partícula', 210, 63);
  
  // === PUNTO MÁSICO (derecha) - Simple ===
  rc.circle(340, 65, 45, { fill: '#ef4444', fillStyle: 'solid', stroke: '#b91c1c', strokeWidth: 2, roughness: 0.5 });
  
  ctx.font = 'bold 22px Inter, sans-serif';
  ctx.fillStyle = '#ffffff';
  ctx.fillText('m', 340, 73);
  
  // Etiqueta del punto
  ctx.font = 'bold 12px Inter, sans-serif';
  ctx.fillStyle = '#1e293b';
  ctx.fillText('Punto Másico', 340, 115);
  
  // Nota pequeña
  ctx.font = '10px Inter, sans-serif';
  ctx.fillStyle = '#64748b';
  ctx.fillText('(toda la masa', 340, 130);
  ctx.fillText('en un solo punto)', 340, 142);
});
</script>


> ⚠️ **Nota:** Este modelo es válido cuando las dimensiones del objeto son despreciables comparadas con la distancia que recorre (ej: un avión viajando entre continentes se puede tratar como una partícula).

---

> 💡 **A continuación:** En la siguiente lección estudiaremos cómo describir la **posición** de una partícula usando un **marco de referencia**.