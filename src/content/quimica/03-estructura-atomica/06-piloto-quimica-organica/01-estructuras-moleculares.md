# 🧪 **Piloto: Representaciones Químicas**

Esta lección piloto demuestra las diferentes herramientas para representar estructuras químicas según su complejidad.

---

## 📖 **1. Fórmulas Químicas Simples (LaTeX)**

Para fórmulas moleculares y ecuaciones sencillas, usamos **LaTeX**:

| Compuesto | Fórmula | Tipo |
|-----------|---------|------|
| Agua | $H_2O$ | Inorgánico |
| Dióxido de carbono | $CO_2$ | Inorgánico |
| Ácido clorhídrico | $HCl$ | Inorgánico |
| Metano | $CH_4$ | Orgánico |
| Etanol | $C_2H_5OH$ | Orgánico |

### Ecuación química con LaTeX:

$$
2H_2 + O_2 \rightarrow 2H_2O
$$

$$
CH_4 + 2O_2 \rightarrow CO_2 + 2H_2O
$$

---

## 📖 **2. Moléculas Simples con Rough.js (Modelo de Lewis)**

Para moléculas inorgánicas donde queremos mostrar la **estructura visual** con enlaces, usamos **Rough.js**:

<div style="display: flex; flex-wrap: wrap; gap: 1.5rem; justify-content: center; margin: 1.5rem 0;">

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; text-align: center;">
  <canvas id="rough-agua" width="180" height="140"></canvas>
  <p style="margin: 0.5rem 0 0; font-weight: bold; color: #1e293b;">Molécula de Agua</p>
  <p style="margin: 0; font-size: 0.85rem; color: #64748b;">$H_2O$ - Enlace covalente</p>
</div>

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; text-align: center;">
  <canvas id="rough-co2" width="220" height="140"></canvas>
  <p style="margin: 0.5rem 0 0; font-weight: bold; color: #1e293b;">Dióxido de Carbono</p>
  <p style="margin: 0; font-size: 0.85rem; color: #64748b;">$CO_2$ - Enlaces dobles</p>
</div>

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; text-align: center;">
  <canvas id="rough-metano" width="180" height="160"></canvas>
  <p style="margin: 0.5rem 0 0; font-weight: bold; color: #1e293b;">Metano</p>
  <p style="margin: 0; font-size: 0.85rem; color: #64748b;">$CH_4$ - Tetraédrico</p>
</div>

</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough === 'undefined') return;
  
  // === AGUA ===
  var canvasAgua = document.getElementById('rough-agua');
  if (canvasAgua) {
    var rc = rough.canvas(canvasAgua);
    var ctx = canvasAgua.getContext('2d');
    
    // Oxígeno (centro)
    rc.circle(90, 70, 40, { fill: '#dc2626', fillStyle: 'solid', stroke: '#991b1b', strokeWidth: 2, roughness: 0.5 });
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.textAlign = 'center';
    ctx.fillText('O', 90, 76);
    
    // Hidrógeno izquierdo
    rc.circle(40, 100, 28, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', strokeWidth: 2, roughness: 0.5 });
    ctx.fillStyle = '#ffffff';
    ctx.fillText('H', 40, 106);
    
    // Hidrógeno derecho
    rc.circle(140, 100, 28, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', strokeWidth: 2, roughness: 0.5 });
    ctx.fillText('H', 140, 106);
    
    // Enlaces
    rc.line(70, 80, 52, 90, { stroke: '#475569', strokeWidth: 3, roughness: 0.5 });
    rc.line(110, 80, 128, 90, { stroke: '#475569', strokeWidth: 3, roughness: 0.5 });
    
    // Ángulo
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('104.5°', 90, 45);
  }
  
  // === CO2 ===
  var canvasCO2 = document.getElementById('rough-co2');
  if (canvasCO2) {
    var rc = rough.canvas(canvasCO2);
    var ctx = canvasCO2.getContext('2d');
    
    // Oxígeno izquierdo
    rc.circle(45, 70, 36, { fill: '#dc2626', fillStyle: 'solid', stroke: '#991b1b', strokeWidth: 2, roughness: 0.5 });
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.textAlign = 'center';
    ctx.fillText('O', 45, 75);
    
    // Carbono (centro)
    rc.circle(110, 70, 36, { fill: '#1e293b', fillStyle: 'solid', stroke: '#0f172a', strokeWidth: 2, roughness: 0.5 });
    ctx.fillStyle = '#ffffff';
    ctx.fillText('C', 110, 75);
    
    // Oxígeno derecho
    rc.circle(175, 70, 36, { fill: '#dc2626', fillStyle: 'solid', stroke: '#991b1b', strokeWidth: 2, roughness: 0.5 });
    ctx.fillText('O', 175, 75);
    
    // Enlaces dobles (izquierda)
    rc.line(63, 62, 92, 62, { stroke: '#475569', strokeWidth: 3, roughness: 0.5 });
    rc.line(63, 78, 92, 78, { stroke: '#475569', strokeWidth: 3, roughness: 0.5 });
    
    // Enlaces dobles (derecha)
    rc.line(128, 62, 157, 62, { stroke: '#475569', strokeWidth: 3, roughness: 0.5 });
    rc.line(128, 78, 157, 78, { stroke: '#475569', strokeWidth: 3, roughness: 0.5 });
    
    // Etiqueta
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Lineal (180°)', 110, 115);
  }
  
  // === METANO ===
  var canvasMetano = document.getElementById('rough-metano');
  if (canvasMetano) {
    var rc = rough.canvas(canvasMetano);
    var ctx = canvasMetano.getContext('2d');
    
    // Carbono (centro)
    rc.circle(90, 80, 36, { fill: '#1e293b', fillStyle: 'solid', stroke: '#0f172a', strokeWidth: 2, roughness: 0.5 });
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.textAlign = 'center';
    ctx.fillText('C', 90, 85);
    
    // 4 Hidrógenos
    var hPositions = [
      {x: 40, y: 45}, {x: 140, y: 45}, {x: 40, y: 120}, {x: 140, y: 120}
    ];
    
    hPositions.forEach(function(pos) {
      rc.circle(pos.x, pos.y, 24, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', strokeWidth: 2, roughness: 0.5 });
      ctx.fillStyle = '#ffffff';
      ctx.fillText('H', pos.x, pos.y + 5);
    });
    
    // Enlaces
    rc.line(72, 65, 52, 55, { stroke: '#475569', strokeWidth: 3, roughness: 0.5 });
    rc.line(108, 65, 128, 55, { stroke: '#475569', strokeWidth: 3, roughness: 0.5 });
    rc.line(72, 95, 52, 110, { stroke: '#475569', strokeWidth: 3, roughness: 0.5 });
    rc.line(108, 95, 128, 110, { stroke: '#475569', strokeWidth: 3, roughness: 0.5 });
  }
});
</script>

---

## 📖 **3. Estructuras Orgánicas con SmilesDrawer**

Para moléculas orgánicas complejas, usamos **SmilesDrawer** con notación SMILES:

<style>
.mol-card {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-radius: 12px;
  padding: 1rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>

<div style="display: flex; flex-wrap: wrap; gap: 1.5rem; justify-content: center; margin: 1.5rem 0;">

<div class="mol-card" style="min-width: 200px;">
  <canvas id="mol-benceno" width="180" height="160"></canvas>
  <p style="margin: 0.5rem 0 0; font-weight: bold; color: #1e293b;">Benceno</p>
  <p style="margin: 0; font-size: 0.85rem; color: #64748b;">$C_6H_6$ - Aromático</p>
</div>

<div class="mol-card" style="min-width: 220px;">
  <canvas id="mol-acido-acetico" width="200" height="160"></canvas>
  <p style="margin: 0.5rem 0 0; font-weight: bold; color: #1e293b;">Ácido Acético</p>
  <p style="margin: 0; font-size: 0.85rem; color: #64748b;">$CH_3COOH$ - Ácido carboxílico</p>
</div>

<div class="mol-card" style="min-width: 280px;">
  <canvas id="mol-aspirina" width="260" height="180"></canvas>
  <p style="margin: 0.5rem 0 0; font-weight: bold; color: #1e293b;">Aspirina</p>
  <p style="margin: 0; font-size: 0.85rem; color: #64748b;">$C_9H_8O_4$ - Fármaco</p>
</div>

</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  setTimeout(function() {
    if (typeof SmilesDrawer === 'undefined') return;
    
    function drawMol(smiles, canvasId, w, h) {
      var drawer = new SmilesDrawer.Drawer({
        width: w, height: h,
        bondThickness: 1.5, bondLength: 20,
        terminalCarbons: true, explicitHydrogens: true,
        fontSizeLarge: 12, fontSizeSmall: 10,
        themes: { light: { C: '#1e293b', O: '#dc2626', N: '#2563eb', BACKGROUND: '#ffffff' } }
      });
      SmilesDrawer.parse(smiles, function(tree) { drawer.draw(tree, canvasId, 'light', false); });
    }
    
    drawMol('c1ccccc1', 'mol-benceno', 180, 160);
    drawMol('CC(=O)O', 'mol-acido-acetico', 200, 160);
    drawMol('CC(=O)Oc1ccccc1C(=O)O', 'mol-aspirina', 260, 180);
  }, 500);
});
</script>

---

## 📖 **4. Mecanismo de Reacción con Rough.js**

Para mecanismos de reacción donde necesitamos control total, usamos **Rough.js**:

### Reacción de esterificación: Ácido + Alcohol → Éster + Agua

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="rough-reaccion" width="700" height="200" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var canvas = document.getElementById('rough-reaccion');
  if (!canvas || typeof rough === 'undefined') return;
  
  var rc = rough.canvas(canvas);
  var ctx = canvas.getContext('2d');
  
  // === REACTIVO 1: Ácido Acético ===
  // Grupo CH3
  rc.rectangle(20, 80, 50, 40, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', roughness: 0.5 });
  ctx.font = 'bold 14px Inter, sans-serif';
  ctx.fillStyle = '#1e40af';
  ctx.textAlign = 'center';
  ctx.fillText('CH₃', 45, 105);
  
  // --- enlace
  rc.line(70, 100, 90, 100, { stroke: '#475569', strokeWidth: 2, roughness: 0.5 });
  
  // Grupo C=O
  rc.rectangle(90, 70, 40, 30, { fill: '#fee2e2', fillStyle: 'solid', stroke: '#dc2626', roughness: 0.5 });
  ctx.fillStyle = '#991b1b';
  ctx.fillText('C=O', 110, 90);
  
  // OH
  rc.rectangle(90, 100, 40, 30, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', roughness: 0.5 });
  ctx.fillStyle = '#b45309';
  ctx.fillText('OH', 110, 120);
  
  // Etiqueta
  ctx.font = '11px Inter, sans-serif';
  ctx.fillStyle = '#64748b';
  ctx.fillText('Ácido Acético', 75, 160);
  
  // === SIGNO + ===
  ctx.font = 'bold 28px Inter, sans-serif';
  ctx.fillStyle = '#1e293b';
  ctx.fillText('+', 170, 105);
  
  // === REACTIVO 2: Etanol ===
  // CH3-CH2
  rc.rectangle(210, 80, 60, 40, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', roughness: 0.5 });
  ctx.font = 'bold 12px Inter, sans-serif';
  ctx.fillStyle = '#1e40af';
  ctx.fillText('CH₃CH₂', 240, 105);
  
  // OH
  rc.rectangle(270, 80, 35, 40, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', roughness: 0.5 });
  ctx.fillStyle = '#b45309';
  ctx.fillText('OH', 287, 105);
  
  // Etiqueta
  ctx.font = '11px Inter, sans-serif';
  ctx.fillStyle = '#64748b';
  ctx.fillText('Etanol', 260, 160);
  
  // === FLECHA DE REACCIÓN ===
  rc.line(330, 100, 410, 100, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
  // Punta de flecha
  rc.line(400, 90, 410, 100, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
  rc.line(400, 110, 410, 100, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
  
  // Catalizador
  ctx.font = '10px Inter, sans-serif';
  ctx.fillStyle = '#16a34a';
  ctx.fillText('H₂SO₄ (cat.)', 370, 85);
  ctx.fillText('Δ', 370, 130);
  
  // === PRODUCTO 1: Éster ===
  // CH3
  rc.rectangle(430, 80, 45, 40, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', roughness: 0.5 });
  ctx.font = 'bold 12px Inter, sans-serif';
  ctx.fillStyle = '#1e40af';
  ctx.fillText('CH₃', 452, 105);
  
  // C=O
  rc.rectangle(475, 70, 35, 30, { fill: '#fee2e2', fillStyle: 'solid', stroke: '#dc2626', roughness: 0.5 });
  ctx.fillStyle = '#991b1b';
  ctx.fillText('C=O', 492, 90);
  
  // O-CH2-CH3
  rc.rectangle(475, 100, 80, 30, { fill: '#dcfce7', fillStyle: 'solid', stroke: '#22c55e', roughness: 0.5 });
  ctx.fillStyle = '#166534';
  ctx.fillText('O-CH₂CH₃', 515, 120);
  
  // Etiqueta
  ctx.font = '11px Inter, sans-serif';
  ctx.fillStyle = '#64748b';
  ctx.fillText('Acetato de Etilo', 495, 160);
  ctx.fillText('(Éster)', 495, 175);
  
  // === SIGNO + ===
  ctx.font = 'bold 24px Inter, sans-serif';
  ctx.fillStyle = '#1e293b';
  ctx.fillText('+', 580, 105);
  
  // === PRODUCTO 2: Agua ===
  rc.circle(640, 100, 45, { fill: '#bfdbfe', fillStyle: 'solid', stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5 });
  ctx.font = 'bold 16px Inter, sans-serif';
  ctx.fillStyle = '#1e40af';
  ctx.fillText('H₂O', 640, 105);
  
  // Etiqueta
  ctx.font = '11px Inter, sans-serif';
  ctx.fillStyle = '#64748b';
  ctx.fillText('Agua', 640, 160);
  
  // === TÍTULO ===
  ctx.font = 'bold 14px Inter, sans-serif';
  ctx.fillStyle = '#1e293b';
  ctx.fillText('Esterificación de Fischer', 350, 25);
});
</script>

### Ecuación resumida:

$$
CH_3COOH + C_2H_5OH \xrightarrow{H_2SO_4, \Delta} CH_3COOC_2H_5 + H_2O
$$

---

## 📖 **5. Estructuras 3D Interactivas (MolView)**

Para visualización **3D interactiva** donde el estudiante puede rotar y hacer zoom, usamos **iframes de MolView.org**:

<div style="display: flex; flex-wrap: wrap; gap: 1.5rem; justify-content: center; margin: 1.5rem 0;">

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; text-align: center;">
  <iframe style="width: 300px; height: 280px; border: 1px solid #e2e8f0; border-radius: 8px;" src="https://embed.molview.org/v1/?mode=balls&cid=2519"></iframe>
  <p style="margin: 0.5rem 0 0; font-weight: bold; color: #1e293b;">☕ Cafeína</p>
  <p style="margin: 0; font-size: 0.85rem; color: #64748b;">Arrastra para rotar • Scroll para zoom</p>
</div>

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; text-align: center;">
  <iframe style="width: 300px; height: 280px; border: 1px solid #e2e8f0; border-radius: 8px;" src="https://embed.molview.org/v1/?mode=balls&cid=241"></iframe>
  <p style="margin: 0.5rem 0 0; font-weight: bold; color: #1e293b;">🔥 Benceno</p>
  <p style="margin: 0; font-size: 0.85rem; color: #64748b;">Anillo aromático C₆H₆</p>
</div>

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; text-align: center;">
  <iframe style="width: 300px; height: 280px; border: 1px solid #e2e8f0; border-radius: 8px;" src="https://embed.molview.org/v1/?mode=stick&cid=702"></iframe>
  <p style="margin: 0.5rem 0 0; font-weight: bold; color: #1e293b;">🍷 Etanol</p>
  <p style="margin: 0; font-size: 0.85rem; color: #64748b;">C₂H₅OH (Alcohol)</p>
</div>

</div>

> 💡 **Interactividad**: Puedes arrastrar las moléculas para rotarlas y usar el scroll para acercar/alejar. ¡Explora su estructura 3D!

---

## 📋 **Resumen: ¿Cuándo usar cada herramienta?**

| Situación | Herramienta | Ejemplo |
|-----------|-------------|---------|
| Fórmulas moleculares | **LaTeX** | $H_2O$, $C_6H_{12}O_6$ |
| Ecuaciones químicas | **LaTeX** | $A + B \rightarrow C$ |
| Moléculas simples (Lewis) | **Rough.js** | Agua, CO₂, Metano |
| Estructuras orgánicas 2D | **SmilesDrawer** | Benceno, Aspirina |
| Mecanismos de reacción | **Rough.js** | Esterificación, Hidrólisis |
| Diagramas de partículas | **Rough.js** | Átomos, Iones |
| **Estructuras 3D interactivas** | **MolView iframe** ⭐ | Cafeína, Benceno |
