# **Atomos neutros e iones**

Los átomos pueden clasificarse **según su carga** en **neutro** o **iones**.

---

## Átomos neutros

Un átomo es **neutro** cuando tiene **igual número de protones y electrones**.
Esto hace que su **carga total sea 0**.

**Fórmula:**
**Carga = Protones − Electrones = 0**

### 🎯 **Comparación: Átomo Neutro vs Iones**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-iones" width="600" height="200" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-iones')) {
    var canvas = document.getElementById('roughjs-iones');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // --- ÁTOMO NEUTRO (izquierda) ---
    var x1 = 100;
    rc.circle(x1, 100, 70, { stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.8 });
    rc.circle(x1, 100, 25, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', roughness: 0.6 });
    // Protones
    rc.circle(x1 - 5, 95, 10, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1 + 5, 105, 10, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    // Electrones (2 = igual a protones)
    rc.circle(x1 + 33, 100, 8, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1 - 33, 100, 8, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('NEUTRO', x1, 155);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('2p⁺ = 2e⁻', x1, 170);
    ctx.fillText('Carga: 0', x1, 185);
    
    // --- CATIÓN (centro) ---
    var x2 = 300;
    rc.circle(x2, 100, 70, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.8 });
    rc.circle(x2, 100, 25, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', roughness: 0.6 });
    // Protones (2)
    rc.circle(x2 - 5, 95, 10, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2 + 5, 105, 10, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    // Electrón (1 - perdió uno)
    rc.circle(x2 + 33, 100, 8, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    // Electrón saliendo (con X)
    rc.circle(x2 - 45, 70, 8, { fill: '#94a3b8', fillStyle: 'solid', roughness: 0.5 });
    rc.line(x2 - 50, 65, x2 - 40, 75, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    rc.line(x2 - 40, 65, x2 - 50, 75, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.5 });
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('CATIÓN (+)', x2, 155);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('2p⁺ > 1e⁻', x2, 170);
    ctx.fillText('Carga: +1', x2, 185);
    
    // --- ANIÓN (derecha) ---
    var x3 = 500;
    rc.circle(x3, 100, 70, { stroke: '#3b82f6', strokeWidth: 2, roughness: 0.8 });
    rc.circle(x3, 100, 25, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', roughness: 0.6 });
    // Protones (2)
    rc.circle(x3 - 5, 95, 10, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x3 + 5, 105, 10, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    // Electrones (3 - ganó uno)
    rc.circle(x3 + 33, 100, 8, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x3 - 33, 100, 8, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x3, 65, 8, { fill: '#22c55e', fillStyle: 'solid', roughness: 0.5 }); // Extra electron
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('ANIÓN (−)', x3, 155);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('2p⁺ < 3e⁻', x3, 170);
    ctx.fillText('Carga: −1', x3, 185);
    
    // Título
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('⚡ Pierde e⁻', x2 - 70, 25);
    ctx.fillText('⚡ Gana e⁻', x3 - 70, 25);
  }
});
</script>

**Ejemplos:**

* Hidrógeno → 1p⁺ y 1e⁻
* Helio → 2p⁺ y 2e⁻
* Litio → 3p⁺ y 3e⁻
* Flúor → 9p⁺ y 9e⁻

El **elemento químico** siempre se identifica por la **cantidad de protones (Z)**.

---

## Iones

Los iones son átomos que **no tienen la misma cantidad de protones y electrones**, por lo tanto su **carga no es cero**.

**Fórmula:**
**Carga = Protones − Electrones**

---

## Cationes

Los cationes son **iones con carga positiva**.
Se forman cuando el átomo **pierde electrones**, quedando con **más protones que electrones**.

**Ejemplo:**

* Litio (Li): 3p⁺ y 2e⁻ → carga = +1

---

## Aniones

Los aniones son **iones con carga negativa**.
Se forman cuando el átomo **gana electrones**, quedando con **más electrones que protones**.

**Ejemplo:**

* Flúor (F): 9p⁺ y 10e⁻ → carga = −1

---

## Nota final

Un átomo puede **ganar o perder electrones** con facilidad, formando iones.
Sin embargo, **ganar o perder protones** ocurre solo en **reacciones nucleares**, que no son comunes en la vida cotidiana.

---

https://youtu.be/ruLNzfexcJs

[Ver en Tiktok](https://vt.tiktok.com/ZSBJPmqD9/)