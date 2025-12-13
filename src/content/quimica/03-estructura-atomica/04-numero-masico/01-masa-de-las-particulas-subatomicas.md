# Masa de las partículas subatómicas

---

## 🧩 Clasificación

Las **partículas subatómicas** que conforman el átomo son:

* **Protones:** tienen **carga positiva (+)**.
* **Neutrones:** poseen **carga neutra (0)**.
* **Electrones:** presentan **carga negativa (−)**.

---

## ⚖️ Concentración de la masa

La **masa del átomo se encuentra principalmente en el núcleo**, ya que está formado por **protones y neutrones**, que son las partículas más pesadas.
Los **electrones**, ubicados alrededor del núcleo, poseen una **masa tan pequeña** que se considera **despreciable**.

---

## ⚙️ Comparación de masas

El **protón** y el **neutrón** tienen **masas muy similares**, aunque el **neutrón es ligeramente más pesado**.
En cambio, la masa del electrón es mínima en comparación.

### 🎯 **Visualización de masas relativas**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-masas" width="600" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-masas')) {
    var canvas = document.getElementById('roughjs-masas');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Comparación de masas (escala visual)', 300, 20);
    
    // PROTÓN - Grande
    rc.circle(100, 90, 70, { fill: '#ef4444', fillStyle: 'solid', stroke: '#b91c1c', strokeWidth: 2, roughness: 0.7 });
    ctx.font = 'bold 20px Inter, sans-serif';
    ctx.fillStyle = '#fff';
    ctx.fillText('+', 100, 98);
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('PROTÓN', 100, 145);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('≈ 1 uma', 100, 160);
    
    // NEUTRÓN - Grande (igual que protón)
    rc.circle(250, 90, 70, { fill: '#6b7280', fillStyle: 'solid', stroke: '#374151', strokeWidth: 2, roughness: 0.7 });
    ctx.font = 'bold 20px Inter, sans-serif';
    ctx.fillStyle = '#fff';
    ctx.fillText('0', 250, 98);
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#6b7280';
    ctx.fillText('NEUTRÓN', 250, 145);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('≈ 1 uma', 250, 160);
    
    // ELECTRÓN - Muy pequeño
    rc.circle(400, 90, 10, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', strokeWidth: 2, roughness: 0.6 });
    ctx.font = 'bold 8px Inter, sans-serif';
    ctx.fillStyle = '#fff';
    ctx.fillText('−', 400, 93);
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('ELECTRÓN', 400, 145);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('≈ 0 uma', 400, 160);
    
    // Nota explicativa
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.textAlign = 'left';
    ctx.fillText('El electrón es ~1836 veces', 470, 80);
    ctx.fillText('más liviano que el protón', 470, 95);
    ctx.fillText('→ su masa es despreciable', 470, 110);
  }
});
</script>

## 🔢 Valores aproximados de masa

* **Protón:** 1,6 × 10⁻²⁷ kg → aproximadamente **1 uma**.
* **Neutrón:** 1,6 × 10⁻²⁷ kg → aproximadamente **1 uma**.
* **Electrón:** 9,1 × 10⁻³¹ kg → aproximadamente **0 uma**, debido a su masa casi despreciable.

---

https://youtu.be/DfW2qM_bGjw

[Ver en Tiktok](https://vt.tiktok.com/ZSBJPHrqp/)

---