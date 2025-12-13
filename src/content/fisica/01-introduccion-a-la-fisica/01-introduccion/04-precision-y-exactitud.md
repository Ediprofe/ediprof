# 🎯 **Precisión y Exactitud**

---

## ⚙️ **Conceptos básicos**

En toda medición pueden presentarse **errores**, por lo que es esencial distinguir entre dos cualidades fundamentales:

> **Exactitud** → cercanía al valor real  
> **Precisión** → consistencia entre mediciones repetidas

---

## 🎯 **Exactitud**

La **exactitud** indica **qué tan cerca** está una medición del **valor verdadero o aceptado**.

> Una medición es **exacta** si el valor obtenido está muy próximo al valor real.

**Ejemplo:**

Si la longitud real de una mesa es de $2.00\,\mathrm{m}$ y obtienes $1.99\,\mathrm{m}$,  
la medición es **exacta**, porque se aproxima mucho al valor verdadero.

---

## 📍 **Precisión**

La **precisión** mide **qué tan consistentes o cercanas entre sí** son varias mediciones de una misma magnitud.

> Una medición es **precisa** cuando se obtienen valores muy similares al repetir el experimento.

**Ejemplo:**

Si mides tres veces una mesa y obtienes  
$1.98\,\mathrm{m}$, $1.99\,\mathrm{m}$ y $2.00\,\mathrm{m}$,  
las mediciones son **precisas**, ya que presentan poca variación entre sí.

---

## ⚖️ **Diferencias clave**

| **Concepto** | **Se refiere a...** | **Ejemplo** |
|:--------------|:--------------------|:-------------|
| **Exactitud** | Cercanía al valor real | Una medición de $9.8\,\mathrm{m/s^2}$ para la gravedad (valor real: $9.81\,\mathrm{m/s^2}$) |
| **Precisión** | Repetibilidad y consistencia de resultados | Varias mediciones muy similares, aunque algo alejadas del valor real |

---

## 🎯 **Analogía del tiro al blanco**

Imagina que lanzas dardos hacia el centro de una diana. El **centro** representa el **valor real** y los **dardos** representan tus **mediciones**:

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 700px;">
  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 2rem;">
    <!-- Exacto y Preciso -->
    <div style="text-align: center;">
      <canvas id="rough-exacto-preciso" width="140" height="140"></canvas>
      <p style="font-size: 11px; color: #22c55e; font-weight: bold; margin-top: 5px;">✓ Exacto y Preciso</p>
    </div>
    <!-- Preciso, no Exacto -->
    <div style="text-align: center;">
      <canvas id="rough-preciso-no-exacto" width="140" height="140"></canvas>
      <p style="font-size: 11px; color: #f59e0b; font-weight: bold; margin-top: 5px;">Preciso, no Exacto</p>
    </div>
    <!-- Exacto, no Preciso -->
    <div style="text-align: center;">
      <canvas id="rough-exacto-no-preciso" width="140" height="140"></canvas>
      <p style="font-size: 11px; color: #3b82f6; font-weight: bold; margin-top: 5px;">Exacto, no Preciso</p>
    </div>
    <!-- Ni Exacto ni Preciso -->
    <div style="text-align: center;">
      <canvas id="rough-ni-ni" width="140" height="140"></canvas>
      <p style="font-size: 11px; color: #ef4444; font-weight: bold; margin-top: 5px;">✗ Ni Exacto ni Preciso</p>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined') {
    
    function drawTarget(canvasId, darts, dartColor) {
      if (!document.getElementById(canvasId)) return;
      var canvas = document.getElementById(canvasId);
      var rc = rough.canvas(canvas);
      var ctx = canvas.getContext('2d');
      var cx = canvas.width / 2;
      var cy = canvas.height / 2;
      
      // Diana
      rc.circle(cx, cy, 120, { stroke: '#475569', strokeWidth: 1.5, fill: '#f8fafc', fillStyle: 'solid', roughness: 0.5 });
      rc.circle(cx, cy, 90, { stroke: '#475569', strokeWidth: 1, fill: '#f1f5f9', fillStyle: 'solid', roughness: 0.5 });
      rc.circle(cx, cy, 60, { stroke: '#475569', strokeWidth: 1, fill: '#e2e8f0', fillStyle: 'solid', roughness: 0.5 });
      rc.circle(cx, cy, 30, { stroke: '#ef4444', strokeWidth: 1, fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 }); // Centro rojo
      
      // Dardos
      darts.forEach(function(pos) {
        // Ajustar coordenadas relativas a absolutas del canvas
        // Suponemos pos en rango [-1, 1] desde el centro
        var dx = cx + pos[0] * 50; 
        var dy = cy + pos[1] * 50;
        
        // Dibujar dardo (x)
        rc.line(dx-3, dy-3, dx+3, dy+3, { stroke: dartColor, strokeWidth: 2, roughness: 0.5 });
        rc.line(dx+3, dy-3, dx-3, dy+3, { stroke: dartColor, strokeWidth: 2, roughness: 0.5 });
      });
    }

    // Exacto y Preciso: Centro
    drawTarget('rough-exacto-preciso', [[0,0], [0.1, 0.1], [-0.1, -0.05], [0.05, -0.1], [-0.05, 0.05]], '#15803d'); // Verde oscuro
    
    // Preciso, no Exacto: Agrupados arriba izquierda
    drawTarget('rough-preciso-no-exacto', [[-0.8, -0.8], [-0.75, -0.85], [-0.7, -0.75], [-0.85, -0.8], [-0.8, -0.7]], '#b45309'); // Ámbar oscuro
    
    // Exacto, no Preciso: Dispersos alrededor del centro
    drawTarget('rough-exacto-no-preciso', [[0.6, 0.6], [-0.5, -0.6], [0.5, -0.5], [-0.6, 0.5], [0, 0]], '#1d4ed8'); // Azul oscuro
    
    // Ni Exacto ni Preciso: Muy dispersos y lejos
    drawTarget('rough-ni-ni', [[0.9, -0.9], [-0.8, 0.2], [0.5, 0.9], [-0.9, -0.8], [0.2, -1]], '#b91c1c'); // Rojo oscuro
  }
});
</script>

> 💡 **El centro rojo** representa el **valor real**. Los dardos agrupados = **precisión**. Dardos cerca del centro = **exactitud**.

---

## 💬 **Conclusión**

- La **exactitud** mide qué tan **correcto** es un resultado.  
- La **precisión** mide qué tan **repetible** es.  
- En física, se busca que las mediciones sean **precisas y exactas** para garantizar resultados **confiables y verificables**.

> 🔎 **Recordatorio:** toda medición implica un **margen de error**, pero aplicar buenas prácticas experimentales permite reducirlo significativamente.
