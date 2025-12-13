# **La materia y sus fases**

La **materia** es todo aquello que **tiene masa** y **ocupa un lugar en el espacio**.
Todo lo que podemos ver, tocar o medir está formado por algún tipo de materia, la cual puede presentarse en diferentes **fases** o **estados físicos**.

---

## **1. Fases de la materia**

La materia puede encontrarse en tres fases principales:

### **🔹 Sólido**

* Tiene **forma definida**.
* Tiene **volumen definido**.
* Sus partículas están muy unidas y solo vibran.

### **🔹 Líquido**

* Tiene **volumen definido**.
* **No tiene forma propia**: adopta la del recipiente.
* Sus partículas están más separadas y pueden deslizarse unas sobre otras.

### **🔹 Gas**

* **No tiene forma** ni **volumen definido**.
* Tiende a expandirse para ocupar todo el espacio disponible.
* Sus partículas están muy separadas y se mueven libremente.

### 🎯 **Visualización: Partículas en cada fase**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-fases" width="600" height="200" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-fases')) {
    var canvas = document.getElementById('roughjs-fases');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Distribución de partículas según la fase', 300, 18);
    
    // --- SÓLIDO ---
    var x1 = 100;
    rc.rectangle(x1-45, 50, 90, 90, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', strokeWidth: 2, roughness: 0.6 });
    // Partículas muy juntas en patrón ordenado
    for (var row = 0; row < 4; row++) {
      for (var col = 0; col < 4; col++) {
        rc.circle(x1 - 28 + col*19, 65 + row*19, 12, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.4 });
      }
    }
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('SÓLIDO', x1, 160);
    ctx.font = '9px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Partículas juntas', x1, 175);
    ctx.fillText('Solo vibran', x1, 188);
    
    // --- LÍQUIDO ---
    var x2 = 300;
    rc.rectangle(x2-45, 50, 90, 90, { fill: '#dcfce7', fillStyle: 'solid', stroke: '#22c55e', strokeWidth: 2, roughness: 0.6 });
    // Partículas más separadas, desordenadas
    var liqPos = [[x2-30,65], [x2-8,62], [x2+15,68], [x2+32,65], 
                  [x2-25,85], [x2-2,88], [x2+22,82], 
                  [x2-32,108], [x2-10,112], [x2+12,106], [x2+28,115]];
    for (var i = 0; i < liqPos.length; i++) {
      rc.circle(liqPos[i][0], liqPos[i][1], 12, { fill: '#22c55e', fillStyle: 'solid', roughness: 0.5 });
    }
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('LÍQUIDO', x2, 160);
    ctx.font = '9px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Partículas deslizantes', x2, 175);
    ctx.fillText('Forma del recipiente', x2, 188);
    
    // --- GAS ---
    var x3 = 500;
    rc.rectangle(x3-45, 50, 90, 90, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', strokeWidth: 2, roughness: 0.6 });
    // Partículas muy separadas, distribución aleatoria
    var gasPos = [[x3-30,60], [x3+25,70], [x3-15,95], [x3+30,100], [x3,130], [x3-35,125], [x3+15,58]];
    for (var i = 0; i < gasPos.length; i++) {
      rc.circle(gasPos[i][0], gasPos[i][1], 10, { fill: '#f59e0b', fillStyle: 'solid', roughness: 0.5 });
    }
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('GAS', x3, 160);
    ctx.font = '9px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Partículas libres', x3, 175);
    ctx.fillText('Se expanden', x3, 188);
  }
});
</script>

## **2. Cambios de fase**

Los cambios de fase son **procesos físicos** mediante los cuales la materia pasa de un estado a otro sin alterar su composición química.

### **Tabla de cambios de fase**

| **Estado inicial** | **Estado final** | **Nombre del cambio**   | **Descripción breve**                                  |
| ------------------ | ---------------- | ----------------------- | ------------------------------------------------------ |
| Sólido             | Líquido          | **Fusión**              | El sólido se derrite al aumentar la temperatura.       |
| Líquido            | Sólido           | **Solidificación**      | El líquido se congela al disminuir la temperatura.     |
| Líquido            | Gas              | **Ebullición**          | El líquido pasa a gas al calentarse hasta hervir.      |
| Gas                | Líquido          | **Condensación**        | El gas se enfría y se transforma en líquido.           |
| Sólido             | Gas              | **Sublimación**         | El sólido pasa directamente a gas sin hacerse líquido. |
| Gas                | Sólido           | **Sublimación inversa** | El gas pasa directamente a sólido.                     |

---

## **3. Ideas clave**

* La materia **ocupa espacio** y **tiene masa**.
* Los estados sólido, líquido y gas se diferencian por **cómo están dispuestas las partículas**.
* Los cambios de fase son **reversibles** y dependen principalmente de la **temperatura** y la **presión**.

--- 

https://youtu.be/kYNxFuNMGoI
[Ver en Tiktok](https://vt.tiktok.com/ZSPJXsmRU/)
