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

<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; margin: 1.5rem auto;">
  <div style="text-align: center;">
    <div id="target-exacto-preciso" style="width: 150px; height: 150px;"></div>
    <p style="font-size: 11px; color: #22c55e; font-weight: bold; margin-top: 0.25rem;">✓ Exacto y Preciso</p>
  </div>
  <div style="text-align: center;">
    <div id="target-preciso-no-exacto" style="width: 150px; height: 150px;"></div>
    <p style="font-size: 11px; color: #f59e0b; font-weight: bold; margin-top: 0.25rem;">Preciso, no Exacto</p>
  </div>
  <div style="text-align: center;">
    <div id="target-exacto-no-preciso" style="width: 150px; height: 150px;"></div>
    <p style="font-size: 11px; color: #3b82f6; font-weight: bold; margin-top: 0.25rem;">Exacto, no Preciso</p>
  </div>
  <div style="text-align: center;">
    <div id="target-ni-ni" style="width: 150px; height: 150px;"></div>
    <p style="font-size: 11px; color: #ef4444; font-weight: bold; margin-top: 0.25rem;">✗ Ni Exacto ni Preciso</p>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var createTarget = function(id, darts, dartColor) {
      if (!document.getElementById(id)) return;
      var board = JXG.JSXGraph.initBoard(id, {
        boundingbox: [-3, 3, 3, -3], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
      });
      // Círculos de diana
      board.create('circle', [[0,0], 2.5], {strokeColor: '#374151', strokeWidth: 1, fillColor: '#f3f4f6', fixed: true});
      board.create('circle', [[0,0], 1.8], {strokeColor: '#374151', strokeWidth: 1, fillColor: '#e5e7eb', fixed: true});
      board.create('circle', [[0,0], 1.1], {strokeColor: '#374151', strokeWidth: 1, fillColor: '#d1d5db', fixed: true});
      board.create('circle', [[0,0], 0.5], {strokeColor: '#374151', strokeWidth: 1, fillColor: '#ef4444', fixed: true});
      // Dardos
      for (var i = 0; i < darts.length; i++) {
        board.create('point', darts[i], {size: 4, color: dartColor, fixed: true, name: ''});
      }
      board.unsuspendUpdate();
    };
    
    // Exacto y Preciso: agrupados en el centro
    createTarget('target-exacto-preciso', [[0.1, 0.15], [-0.1, -0.05], [0.05, -0.1], [-0.05, 0.1], [0, 0.05]], '#22c55e');
    
    // Preciso, no Exacto: agrupados pero lejos del centro
    createTarget('target-preciso-no-exacto', [[-1.5, 1.6], [-1.6, 1.4], [-1.4, 1.5], [-1.55, 1.55], [-1.45, 1.45]], '#f59e0b');
    
    // Exacto, no Preciso: dispersos pero promedio cerca del centro
    createTarget('target-exacto-no-preciso', [[0.8, -0.9], [-0.7, 0.8], [0.1, 0.1], [-0.5, -0.6], [0.6, 0.5]], '#3b82f6');
    
    // Ni Exacto ni Preciso: dispersos y lejos
    createTarget('target-ni-ni', [[1.8, 0.5], [-0.5, -2], [2, -1.5], [-1.8, 1], [0.3, 2.2]], '#ef4444');
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
