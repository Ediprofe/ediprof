# ⚛️ Isótopos

---

## 🧩 Definición

Los **isótopos** son **átomos del mismo elemento** que poseen **igual número de protones**, pero **diferente número de neutrones**.

---

## ⚖️ Consecuencia

Al tener distinta cantidad de neutrones:

* Presentan **diferente número másico (A)**.
* En consecuencia, **sus masas son distintas**, aunque sigan siendo el mismo elemento.

### 🎯 **Visualización: Isótopos del Hidrógeno**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-isotopos" width="600" height="220" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-isotopos')) {
    var canvas = document.getElementById('roughjs-isotopos');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título y Leyenda arriba
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Isótopos del Hidrógeno (mismo protón, diferentes neutrones)', 250, 18);
    
    ctx.font = '9px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('● Protón', 480, 12);
    ctx.fillStyle = '#6b7280';
    ctx.fillText('● Neutrón', 530, 12);
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('● e⁻', 480, 25);
    
    var x1 = 100, x2 = 300, x3 = 500;
    
    // PROTIO
    rc.circle(x1, 100, 60, { stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.8 });
    rc.circle(x1, 100, 20, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', roughness: 0.6 });
    rc.circle(x1, 100, 12, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1 + 28, 100, 8, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    ctx.font = 'bold 12px Inter, sans-serif'; ctx.textAlign = 'center';
    ctx.fillStyle = '#22c55e'; ctx.fillText('PROTIO', x1, 155);
    ctx.font = '10px Inter, sans-serif'; ctx.fillStyle = '#64748b';
    ctx.fillText('1p⁺ + 0n | A=1 | 99.98%', x1, 175);
    
    // DEUTERIO
    rc.circle(x2, 100, 60, { stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.8 });
    rc.circle(x2, 100, 25, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', roughness: 0.6 });
    rc.circle(x2 - 6, 100, 10, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2 + 6, 100, 10, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2 + 28, 100, 8, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b'; ctx.fillText('DEUTERIO', x2, 155);
    ctx.font = '10px Inter, sans-serif'; ctx.fillStyle = '#64748b';
    ctx.fillText('1p⁺ + 1n | A=2 | 0.02%', x2, 175);
    
    // TRITIO
    rc.circle(x3, 100, 60, { stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.8 });
    rc.circle(x3, 100, 30, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', roughness: 0.6 });
    rc.circle(x3, 92, 9, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x3 - 8, 105, 9, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x3 + 8, 105, 9, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x3 + 28, 100, 8, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#a855f7'; ctx.fillText('TRITIO', x3, 155);
    ctx.font = '10px Inter, sans-serif'; ctx.fillStyle = '#64748b';
    ctx.fillText('1p⁺ + 2n | A=3 | Radiactivo', x3, 175);
  }
});
</script>

## 🔬 Importancia

* Todos los isótopos **pertenecen al mismo elemento químico**.
* Se **distinguen únicamente por su masa**, no por sus propiedades químicas.

---

## 🧪 Ejemplos

### Hidrógeno

Todos sus átomos tienen **1 protón**, pero pueden diferir en neutrones:

* **Protio:** 0 neutrones → el más abundante
* **Deuterio:** 1 neutrón → menos abundante
* **Tritio:** 2 neutrones → radiactivo y muy escaso

### Carbono

Todos los átomos de carbono poseen **6 protones**:

* **Carbono-12:** 6 neutrones → muy abundante
* **Carbono-13:** 7 neutrones → menos abundante

---

## 🧮 Conclusión

Los **isótopos**:

* Son del **mismo elemento**.
* **Difieren en su número de neutrones**.
* Por ello, **tienen masas diferentes**.

---

## 💧 Isótopos del hidrógeno

| **Isótopo**  | **Protones** | **Neutrones** | **Número másico (A)** | **Notación**         | **Abundancia en la naturaleza** |
| ------------ | ------------ | ------------- | --------------------- | -------------------- | ------------------------------- |
| **Protio**   | 1            | 0             | **1**                 | $^{1}_{1}\mathrm{H}$ | 99,985 %                        |
| **Deuterio** | 1            | 1             | **2**                 | $^{2}_{1}\mathrm{H}$ | 0,015 %                         |
| **Tritio**   | 1            | 2             | **3**                 | $^{3}_{1}\mathrm{H}$ | Muy escaso (radiactivo)         |

---

## 🌿 Isótopos del carbono

### 🎯 **Visualización: Isótopos del Carbono**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-carbono" width="600" height="220" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-carbono')) {
    var canvas = document.getElementById('roughjs-carbono');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título y Leyenda
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Isótopos del Carbono (6 protones, diferentes neutrones)', 250, 18);
    
    ctx.font = '9px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('● 6 Protones', 480, 12);
    ctx.fillStyle = '#6b7280';
    ctx.fillText('● Neutrones', 480, 25);
    
    // --- CARBONO-12 (izquierda) ---
    var x1 = 180;
    // Órbitas
    rc.circle(x1, 105, 100, { stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.8 });
    rc.circle(x1, 105, 65, { stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.8 });
    // Núcleo grande para contener 12 partículas
    rc.circle(x1, 105, 50, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', strokeWidth: 2, roughness: 0.6 });
    // 6 protones (rojos) y 6 neutrones (grises) alternados en patrón compacto
    rc.circle(x1-10, 90, 6, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1+2, 90, 6, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1+14, 90, 6, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1-15, 102, 6, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1-3, 102, 6, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1+9, 102, 6, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1+18, 105, 6, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1-10, 114, 6, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1+2, 114, 6, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1+14, 114, 6, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1-4, 124, 5, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1+8, 124, 5, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    // Electrones (6 azules)
    rc.circle(x1+30, 105, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1-30, 105, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1+48, 105, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1-48, 105, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1, 55, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x1, 155, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    
    ctx.font = 'bold 14px Inter, sans-serif'; ctx.textAlign = 'center';
    ctx.fillStyle = '#22c55e'; ctx.fillText('CARBONO-12', x1, 180);
    ctx.font = '10px Inter, sans-serif'; ctx.fillStyle = '#64748b';
    ctx.fillText('6p⁺ + 6n | A=12 | 98.9%', x1, 198);
    
    // --- CARBONO-13 (derecha) ---
    var x2 = 420;
    // Órbitas
    rc.circle(x2, 105, 100, { stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.8 });
    rc.circle(x2, 105, 65, { stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.8 });
    // Núcleo ligeramente más grande para 13 partículas
    rc.circle(x2, 105, 52, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', strokeWidth: 2, roughness: 0.6 });
    // 6 protones (rojos) y 7 neutrones (grises, el extra en morado)
    rc.circle(x2-10, 88, 6, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2+2, 88, 6, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2+14, 88, 6, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2-15, 100, 6, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2-3, 100, 6, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2+9, 100, 6, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2+18, 103, 6, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2-10, 112, 6, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2+2, 112, 6, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2+14, 112, 6, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2-6, 122, 5, { fill: '#ef4444', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2+6, 122, 5, { fill: '#6b7280', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2, 130, 6, { fill: '#a855f7', fillStyle: 'solid', roughness: 0.5 }); // Neutrón extra (morado)
    // Electrones (6 azules)
    rc.circle(x2+30, 105, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2-30, 105, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2+48, 105, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2-48, 105, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2, 55, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    rc.circle(x2, 155, 6, { fill: '#3b82f6', fillStyle: 'solid', roughness: 0.5 });
    
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b'; ctx.fillText('CARBONO-13', x2, 180);
    ctx.font = '10px Inter, sans-serif'; ctx.fillStyle = '#64748b';
    ctx.fillText('6p⁺ + 7n | A=13 | 1.1%', x2, 198);
    
    // Indicador del neutrón extra
    ctx.font = '9px Inter, sans-serif';
    ctx.fillStyle = '#a855f7';
    ctx.fillText('● +1 neutrón', x2 + 30, 132);
  }
});
</script>

| **Isótopo**    | **Protones** | **Neutrones** | **Número másico (A)** | **Notación**          | **Abundancia en la naturaleza** |
| -------------- | ------------ | ------------- | --------------------- | --------------------- | ------------------------------- |
| **Carbono-12** | 6            | 6             | **12**                | $^{12}_{6}\mathrm{C}$ | ≈ 98,9 %                        |
| **Carbono-13** | 6            | 7             | **13**                | $^{13}_{6}\mathrm{C}$ | ≈ 1,1 %                         |

---

https://youtu.be/wG--J1nGOnU

[Ver en Tiktok](https://vt.tiktok.com/ZSBJP9GXT/)