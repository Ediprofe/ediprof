# 📐 **Sistema Sexagesimal**

Ahora que sabemos qué es un ángulo, necesitamos aprender a **medirlo con precisión**. El sistema más común para medir ángulos es el **sistema sexagesimal**, que usa grados, minutos y segundos.

---

## 🎯 **¿Qué es el sistema sexagesimal?**

El **sistema sexagesimal** es un sistema de medición basado en el número **60**.

> 💡 **Idea clave:** Cada grado se divide en 60 partes (minutos), y cada minuto se divide en 60 partes (segundos). ¡Igual que el tiempo!

### ¿Por qué base 60?

Los **babilonios** (hace más de 4000 años) inventaron este sistema porque:

| Razón | Explicación |
|-------|-------------|
| **Muchos divisores** | 60 se puede dividir exactamente entre: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30 y 60 |
| **Facilita cálculos** | Dividir en tercios, cuartos, sextos es exacto (sin decimales) |
| **Astronomía** | Facilitaba medir posiciones de estrellas con precisión |

> 💡 **Dato curioso:** Este mismo sistema se usa para el tiempo: 1 hora = 60 minutos, 1 minuto = 60 segundos.

---

## 📖 **Las tres unidades del sistema sexagesimal**

**📊 Ilustración: Cómo se subdivide un grado**

<div style="background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-grado-subdivision" width="600" height="320" style="width: 100%; max-width: 600px; height: auto; display: block; margin: 0 auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-grado-subdivision')) {
    var canvas = document.getElementById('roughjs-grado-subdivision');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título
    ctx.font = 'bold 18px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Las 3 unidades del Sistema Sexagesimal', 300, 30);
    
    // --- GRADO (azul) ---
    rc.rectangle(50, 55, 160, 100, { stroke: '#3b82f6', strokeWidth: 3, fill: '#dbeafe', fillStyle: 'solid', roughness: 0.6 });
    ctx.font = 'bold 48px Inter, sans-serif';
    ctx.fillStyle = '#1e40af';
    ctx.fillText('°', 130, 115);
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillText('GRADO', 130, 145);
    
    // Flecha 1
    rc.line(220, 105, 270, 105, { stroke: '#64748b', strokeWidth: 3, roughness: 0.4 });
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('÷60', 245, 95);
    
    // --- MINUTO (verde) ---
    rc.rectangle(280, 55, 160, 100, { stroke: '#22c55e', strokeWidth: 3, fill: '#dcfce7', fillStyle: 'solid', roughness: 0.6 });
    ctx.font = 'bold 48px Inter, sans-serif';
    ctx.fillStyle = '#166534';
    ctx.fillText("'", 360, 115);
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillText('MINUTO', 360, 145);
    
    // Flecha 2
    rc.line(450, 105, 500, 105, { stroke: '#64748b', strokeWidth: 3, roughness: 0.4 });
    ctx.fillStyle = '#64748b';
    ctx.fillText('÷60', 475, 95);
    
    // --- SEGUNDO (naranja) ---
    rc.rectangle(510, 55, 80, 100, { stroke: '#f59e0b', strokeWidth: 3, fill: '#fef3c7', fillStyle: 'solid', roughness: 0.6 });
    ctx.font = 'bold 48px Inter, sans-serif';
    ctx.fillStyle = '#92400e';
    ctx.fillText("''", 550, 115);
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillText('SEGUNDO', 550, 145);
    
    // Barra de subdivisión visual
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#1e293b';
    ctx.fillText('Visualización:', 50, 195);
    
    // Barra 1 GRADO
    rc.rectangle(50, 210, 500, 30, { stroke: '#3b82f6', strokeWidth: 2, fill: '#dbeafe', fillStyle: 'solid', roughness: 0.4 });
    ctx.textAlign = 'center';
    ctx.fillStyle = '#1e40af';
    ctx.fillText('1°', 300, 232);
    
    // Barra 60 MINUTOS
    for (var i = 0; i < 12; i++) {
      rc.rectangle(50 + i * (500/12), 250, 500/12, 25, { stroke: '#22c55e', strokeWidth: 1, fill: '#dcfce7', fillStyle: 'solid', roughness: 0.3 });
    }
    ctx.fillStyle = '#166534';
    ctx.fillText("60' (minutos)", 300, 270);
    
    // Barra 3600 SEGUNDOS
    for (var i = 0; i < 60; i++) {
      rc.rectangle(50 + i * (500/60), 285, 500/60, 15, { stroke: '#f59e0b', strokeWidth: 0.5, fill: '#fef3c7', fillStyle: 'solid', roughness: 0.2 });
    }
    ctx.fillStyle = '#92400e';
    ctx.fillText("3600'' (segundos)", 300, 315);
  }
});
</script>

> 💡 **Cada nivel es 60 veces más pequeño que el anterior.** Igual que en el tiempo: 1 hora = 60 minutos = 3600 segundos.

### 1. El Grado (°)

El **grado** es la unidad principal. Una vuelta completa tiene 360°.

$$
1 \text{ vuelta completa} = 360°
$$

### 2. El Minuto (')

El **minuto** es la sexagésima parte de un grado.

$$
\boxed{1° = 60'} \quad \text{(1 grado = 60 minutos)}
$$

### 3. El Segundo ('')

El **segundo** es la sexagésima parte de un minuto.

$$
\boxed{1' = 60''} \quad \text{(1 minuto = 60 segundos)}
$$

### Tabla de equivalencias completa

| De | A | Equivalencia | Cálculo |
|----|---|--------------|---------|
| 1 grado | minutos | 60' | 1° = 60' |
| 1 minuto | segundos | 60'' | 1' = 60'' |
| 1 grado | segundos | 3600'' | 60' × 60'' = 3600'' |

**📐 Ilustración: Un ángulo de 1° subdividido en minutos**

<div style="background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-angulo-subdiv" width="500" height="320" style="width: 100%; max-width: 500px; height: auto; display: block; margin: 0 auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-angulo-subdiv')) {
    var canvas = document.getElementById('roughjs-angulo-subdiv');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    var cx = 80, cy = 250;
    var R = 200;
    
    // Título
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('1° dividido en 60 minutos', 250, 25);
    
    // Lado horizontal
    rc.line(cx, cy, cx + R + 50, cy, { stroke: '#1e293b', strokeWidth: 2, roughness: 0.5 });
    
    // Lado del ángulo de 1°
    var anguloRad = 30 * Math.PI / 180; // Exagerado para verse
    var x2 = cx + (R + 50) * Math.cos(-anguloRad);
    var y2 = cy + (R + 50) * Math.sin(-anguloRad);
    rc.line(cx, cy, x2, y2, { stroke: '#1e293b', strokeWidth: 2, roughness: 0.5 });
    
    // Arco principal (1°) - en azul grueso
    rc.arc(cx, cy, R * 2, R * 2, 0, -anguloRad, false, { stroke: '#3b82f6', strokeWidth: 4, roughness: 0.3 });
    
    // Divisiones de minutos (6 líneas visibles = representando 10' cada una)
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 1;
    for (var i = 1; i < 6; i++) {
      var angulo = -anguloRad * (i / 6);
      var xStart = cx + (R - 15) * Math.cos(angulo);
      var yStart = cy + (R - 15) * Math.sin(angulo);
      var xEnd = cx + (R + 15) * Math.cos(angulo);
      var yEnd = cy + (R + 15) * Math.sin(angulo);
      ctx.beginPath();
      ctx.moveTo(xStart, yStart);
      ctx.lineTo(xEnd, yEnd);
      ctx.stroke();
    }
    
    // Etiquetas
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.textAlign = 'left';
    
    // 1° etiqueta
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('1°', cx + R + 10, cy - 30);
    
    // Etiqueta de minutos
    ctx.fillStyle = '#22c55e';
    ctx.fillText("= 60'", cx + R + 10, cy - 10);
    
    // Vértice
    rc.circle(cx, cy, 10, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.3 });
    
    // Leyenda
    ctx.font = '13px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.textAlign = 'center';
    ctx.fillText('Cada rayita verde = 10 minutos', 250, 300);
    ctx.fillText('(Hay 60 minutos en 1 grado)', 250, 318);
  }
});
</script>

---

## 📖 **Notación: Cómo escribir ángulos**

Los ángulos en sistema sexagesimal se escriben así:

<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0; text-align: center;">
  <div style="font-size: 2.5rem; font-weight: bold; font-family: monospace; color: #1e293b; letter-spacing: 3px;">
    45° 30' 25''
  </div>
  <div style="margin-top: 0.5rem; color: #166534;">
    Se lee: <strong>"45 grados, 30 minutos, 25 segundos"</strong>
  </div>
</div>

### Formas de escribir un ángulo

| Forma | Ejemplo | Cuándo usarla | Precisión |
|-------|---------|---------------|-----------|
| Solo grados | $90°$ | Ángulos redondos | Baja |
| Grados y minutos | $60° \, 15'$ | Uso común | Media |
| Completa | $45° \, 30' \, 25''$ | Navegación, astronomía | Alta |

---

## ⚙️ **Ejemplos: Leer y escribir ángulos**

### Ejemplo 1: Ángulo recto

$$
90° = 90° \, 0' \, 0''
$$

**Lectura:** "Noventa grados exactos"

<div style="background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1rem 0;">
  <canvas id="roughjs-angulo-90" width="300" height="200" style="width: 100%; max-width: 300px; height: auto; display: block; margin: 0 auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-angulo-90')) {
    var canvas = document.getElementById('roughjs-angulo-90');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    var cx = 60, cy = 160, R = 100;
    
    // Lado horizontal
    rc.line(cx, cy, cx + R + 30, cy, { stroke: '#3b82f6', strokeWidth: 3, roughness: 0.5 });
    
    // Lado vertical (90°)
    rc.line(cx, cy, cx, cy - R - 30, { stroke: '#3b82f6', strokeWidth: 3, roughness: 0.5 });
    
    // Arco de 90°
    rc.arc(cx, cy, 60, 60, -Math.PI/2, 0, false, { stroke: '#f59e0b', strokeWidth: 3, roughness: 0.3 });
    
    // Cuadradito de ángulo recto
    rc.rectangle(cx, cy - 20, 20, 20, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.4 });
    
    // Vértice
    rc.circle(cx, cy, 8, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.3 });
    
    // Etiqueta
    ctx.font = 'bold 18px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('90°', cx + 35, cy - 35);
    
    // Título
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Ángulo Recto', 150, 20);
  }
});
</script>

---

### Ejemplo 2: Ángulo con minutos

$$
45° \, 30'
$$

**Lectura:** "Cuarenta y cinco grados y treinta minutos"

<div style="background: #f8fafc; border: 2px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1rem 0;">
  <canvas id="roughjs-angulo-45-30" width="300" height="200" style="width: 100%; max-width: 300px; height: auto; display: block; margin: 0 auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-angulo-45-30')) {
    var canvas = document.getElementById('roughjs-angulo-45-30');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    var cx = 60, cy = 160, R = 100;
    var angulo = 45.5 * Math.PI / 180; // 45° 30' = 45.5°
    
    // Lado horizontal
    rc.line(cx, cy, cx + R + 30, cy, { stroke: '#3b82f6', strokeWidth: 3, roughness: 0.5 });
    
    // Lado del ángulo
    var x2 = cx + (R + 30) * Math.cos(-angulo);
    var y2 = cy + (R + 30) * Math.sin(-angulo);
    rc.line(cx, cy, x2, y2, { stroke: '#3b82f6', strokeWidth: 3, roughness: 0.5 });
    
    // Arco
    rc.arc(cx, cy, 70, 70, -angulo, 0, false, { stroke: '#f59e0b', strokeWidth: 3, roughness: 0.3 });
    
    // Vértice
    rc.circle(cx, cy, 8, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.3 });
    
    // Etiqueta
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText("45° 30'", cx + 55, cy - 25);
    
    // Equivalencia
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('= 45.5°', cx + 65, cy - 10);
    
    // Título
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Ángulo Agudo', 150, 20);
  }
});
</script>

> 💡 **Nota:** 30' es medio grado (porque $30 \div 60 = 0.5$), entonces $45° \, 30' = 45.5°$

---

### Ejemplo 3: Ángulo completo

$$
72° \, 45' \, 18''
$$

**Lectura:** "Setenta y dos grados, cuarenta y cinco minutos, dieciocho segundos"

---

### Ejemplo 4: Convertir grados a minutos

**¿Cuántos minutos hay en 3°?**

$$
3° = 3 \times 60' = \boxed{180'}
$$

---

### Ejemplo 5: Convertir a segundos

**¿Cuántos segundos hay en 1° 30'?**

- $1° = 60' = 60 \times 60'' = 3600''$
- $30' = 30 \times 60'' = 1800''$
- **Total:** $3600 + 1800 = \boxed{5400''}$

---

## 🔗 **Conexión con la vida real: El Tiempo**

<div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 2px solid #f59e0b; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0;">
  <div style="text-align: center; font-size: 1.3rem; font-weight: bold; color: #92400e; margin-bottom: 1rem;">
    ⏰ El tiempo usa el MISMO sistema sexagesimal
  </div>
  <table style="width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden;">
    <tr style="background: #fef3c7;">
      <th style="padding: 0.75rem; border: 1px solid #fcd34d; text-align: center;">⏰ Tiempo</th>
      <th style="padding: 0.75rem; border: 1px solid #fcd34d; text-align: center;">📐 Ángulos</th>
    </tr>
    <tr>
      <td style="padding: 0.75rem; border: 1px solid #fcd34d; text-align: center;">1 hora = 60 minutos</td>
      <td style="padding: 0.75rem; border: 1px solid #fcd34d; text-align: center;">1° = 60'</td>
    </tr>
    <tr>
      <td style="padding: 0.75rem; border: 1px solid #fcd34d; text-align: center;">1 minuto = 60 segundos</td>
      <td style="padding: 0.75rem; border: 1px solid #fcd34d; text-align: center;">1' = 60''</td>
    </tr>
    <tr style="background: #fef3c7;">
      <td style="padding: 0.75rem; border: 1px solid #fcd34d; text-align: center; font-weight: bold;">2h 30min 45s</td>
      <td style="padding: 0.75rem; border: 1px solid #fcd34d; text-align: center; font-weight: bold;">2° 30' 45''</td>
    </tr>
  </table>
</div>

> 💡 **Si sabes leer "2 horas 30 minutos 45 segundos", ya sabes leer "2° 30' 45''"** ¡El formato es idéntico!

---

## ✏️ **Práctica: ¿Cómo se lee?**

<details>
<summary><strong>📝 1. ¿Cómo se lee 30° 15' 20''?</strong></summary>

> **"Treinta grados, quince minutos, veinte segundos"**

</details>

<details>
<summary><strong>📝 2. ¿Cómo se lee 180°?</strong></summary>

> **"Ciento ochenta grados"** (un ángulo llano)

</details>

<details>
<summary><strong>📝 3. ¿Cuántos minutos hay en 5°?</strong></summary>

> $5 \times 60 = \boxed{300'}$

</details>

<details>
<summary><strong>📝 4. ¿Cuántos segundos hay en 2'?</strong></summary>

> $2 \times 60 = \boxed{120''}$

</details>

<details>
<summary><strong>📝 5. Escribe "sesenta grados, cuarenta y cinco minutos" en notación</strong></summary>

> $\boxed{60° \, 45'}$

</details>

---

## 🌍 **Aplicación: Sistema de Coordenadas Geográficas**

Una de las aplicaciones más importantes del sistema sexagesimal es la **navegación** y **geografía**. Las coordenadas de cualquier lugar en la Tierra se expresan en grados, minutos y segundos.

Para ubicar cualquier punto en la Tierra necesitamos **dos ángulos**:

| Coordenada | ¿Qué mide? | Desde dónde | Rango |
|------------|------------|-------------|-------|
| **Latitud** | Norte ↔ Sur | El Ecuador | 0° a 90° N/S |
| **Longitud** | Este ↔ Oeste | Meridiano de Greenwich | 0° a 180° E/W |

---

### 📍 La Latitud: ¿Qué tan al Norte o Sur estás?

La **latitud** es el ángulo medido desde el **centro de la Tierra** entre el **ecuador** y el punto que queremos ubicar.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong>Arrastra el punto naranja ↑↓ para cambiar la latitud</strong>
  </div>
  <div id="jsxgraph-lat-nuevo" style="width: 100%; height: 380px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-lat-nuevo')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-lat-nuevo', {
      boundingbox: [-6, 5, 6, -5],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var R = 3.2;
    
    // Tierra (círculo)
    board.create('circle', [[0, 0], R], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true, fillColor: '#dbeafe', fillOpacity: 0.4});
    
    // Elipse que simula el ecuador en 3D
    board.create('ellipse', [[-R, 0], [R, 0], [0, 0.6]], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    
    // Eje (línea vertical punteada)
    board.create('segment', [[0, -R-0.4], [0, R+0.4]], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true});
    
    // Polos
    board.create('point', [0, R], {name: '', size: 5, fixed: true, color: '#dc2626'});
    board.create('text', [0.4, R+0.3, 'Polo Norte 90°N'], {fontSize: 10, color: '#dc2626', fixed: true});
    
    board.create('point', [0, -R], {name: '', size: 5, fixed: true, color: '#2563eb'});
    board.create('text', [0.4, -R-0.2, 'Polo Sur 90°S'], {fontSize: 10, color: '#2563eb', fixed: true});
    
    // Etiqueta Ecuador
    board.create('text', [R+0.4, 0.3, 'Ecuador 0°'], {fontSize: 10, color: '#22c55e', fixed: true});
    
    // Centro
    board.create('point', [0, 0], {name: '', size: 3, fixed: true, color: '#1e293b'});
    
    // Círculo del borde de la Tierra para que el punto esté EN LA SUPERFICIE
    var circuloLat = board.create('circle', [[0, 0], R], {visible: false});
    
    // Punto interactivo que se desliza por el BORDE del círculo (superficie)
    var punto = board.create('glider', [R*0.85, R*0.5, circuloLat], {
      name: '', size: 8, color: '#f59e0b'
    });
    
    // Línea referencia al ecuador (hasta el borde)
    board.create('segment', [[0, 0], [R, 0]], {strokeColor: '#22c55e', strokeWidth: 1, dash: 3, fixed: true});
    
    // Línea al punto
    board.create('segment', [[0, 0], punto], {strokeColor: '#f59e0b', strokeWidth: 2});
    
    // Arco del ángulo (referencia desde el ecuador en el borde)
    var pRef = board.create('point', [R, 0], {visible: false, fixed: true});
    board.create('angle', [pRef, [0, 0], punto], {
      radius: 0.7, fillColor: '#fef3c7', fillOpacity: 0.7, strokeColor: '#f59e0b', strokeWidth: 2, name: ''
    });
    
    // Texto dinámico
    board.create('text', [0, -4.3, function() {
      var y = punto.Y();
      var x = punto.X();
      var lat = Math.round(Math.atan2(y, x) * 180 / Math.PI);
      var hem = lat >= 0 ? 'Norte' : 'Sur';
      return '📍 LATITUD = ' + Math.abs(lat) + '° ' + hem;
    }], {fontSize: 15, fontWeight: 'bold', color: '#1e293b', anchorX: 'middle', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

**🏙️ Ejemplo: ¿Dónde está Bogotá en latitud?**

<div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); border: 2px solid #f59e0b; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0;">
  <div style="display: flex; align-items: center; gap: 1rem; flex-wrap: wrap;">
    <div style="font-size: 3rem;">🇨🇴</div>
    <div>
      <div style="font-weight: bold; font-size: 1.2rem; color: #92400e;">Bogotá, Colombia</div>
      <div style="font-size: 1.5rem; font-weight: bold; color: #1e293b; font-family: monospace;">Latitud: 4° 36' Norte</div>
      <div style="color: #78716c; font-size: 0.9rem;">Está a solo 4.6° al norte del Ecuador → ¡muy cerca de la línea ecuatorial!</div>
    </div>
  </div>
</div>

> 💡 **Interpretación:** Bogotá está en el **hemisferio norte** (N), pero muy cerca del ecuador. Si arrastras el punto naranja al gráfico hasta aproximadamente 5°, ¡esa es la latitud de Bogotá!

---

### 📍 La Longitud: ¿Qué tan al Este o al Oeste estás?

La **longitud** es el ángulo medido en el plano del ecuador, desde el **meridiano de Greenwich** (línea que pasa por Londres) hasta el meridiano del punto que queremos ubicar.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong>Vista desde arriba (Polo Norte) — Arrastra el punto ← → alrededor</strong>
  </div>
  <div id="jsxgraph-lon-nuevo" style="width: 100%; height: 380px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-lon-nuevo')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-lon-nuevo', {
      boundingbox: [-5.5, 5, 5.5, -5],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    var R = 3.2;
    
    // Círculo (vista desde arriba del Polo Norte)
    board.create('circle', [[0, 0], R], {strokeColor: '#3b82f6', strokeWidth: 2, fixed: true, fillColor: '#dbeafe', fillOpacity: 0.4});
    
    // Polo Norte (centro)
    board.create('point', [0, 0], {name: '', size: 5, fixed: true, color: '#dc2626'});
    board.create('text', [0.3, -0.3, 'Polo Norte'], {fontSize: 9, color: '#dc2626', fixed: true});
    
    // Greenwich (hacia arriba)
    board.create('segment', [[0, 0], [0, R]], {strokeColor: '#22c55e', strokeWidth: 3, fixed: true});
    board.create('text', [0.3, R+0.3, 'Greenwich 0°'], {fontSize: 10, color: '#22c55e', fixed: true});
    
    // Referencias
    board.create('segment', [[0, 0], [R, 0]], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true});
    board.create('text', [R+0.3, 0, '90°E'], {fontSize: 10, color: '#64748b', fixed: true});
    
    board.create('segment', [[0, 0], [-R, 0]], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true});
    board.create('text', [-R-0.5, 0, '90°W'], {fontSize: 10, color: '#64748b', fixed: true});
    
    board.create('segment', [[0, 0], [0, -R]], {strokeColor: '#94a3b8', strokeWidth: 1, dash: 2, fixed: true});
    board.create('text', [0, -R-0.3, '180°'], {fontSize: 10, color: '#64748b', anchorX: 'middle', fixed: true});
    
    // Punto interactivo EN EL BORDE del círculo (superficie)
    var circulo = board.create('circle', [[0, 0], R], {visible: false});
    var punto = board.create('glider', [-R * 0.7, R * 0.7, circulo], {
      name: '', size: 8, color: '#f59e0b'
    });
    
    // Línea al punto
    board.create('segment', [[0, 0], punto], {strokeColor: '#f59e0b', strokeWidth: 2});
    
    // Arco (referencia desde Greenwich)
    var pGreenwich = board.create('point', [0, R], {visible: false, fixed: true});
    board.create('angle', [pGreenwich, [0, 0], punto], {
      radius: 0.7, fillColor: '#fef3c7', fillOpacity: 0.7, strokeColor: '#f59e0b', strokeWidth: 2, name: ''
    });
    
    // Texto dinámico
    board.create('text', [0, -4.3, function() {
      var x = punto.X();
      var y = punto.Y();
      var angulo = Math.atan2(x, y) * 180 / Math.PI;
      var lon = Math.round(angulo);
      var dir = lon >= 0 ? 'Este (→)' : 'Oeste (←)';
      return '📍 LONGITUD = ' + Math.abs(lon) + '° ' + dir;
    }], {fontSize: 15, fontWeight: 'bold', color: '#1e293b', anchorX: 'middle', fixed: true});
    
    // Direcciones
    board.create('text', [4.5, 3, '→ ESTE'], {fontSize: 10, color: '#3b82f6', fixed: true});
    board.create('text', [-5, 3, 'OESTE ←'], {fontSize: 10, color: '#3b82f6', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

**🏙️ Ejemplo: ¿Dónde está Bogotá en longitud?**

<div style="background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%); border: 2px solid #3b82f6; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0;">
  <div style="display: flex; align-items: center; gap: 1rem; flex-wrap: wrap;">
    <div style="font-size: 3rem;">🇨🇴</div>
    <div>
      <div style="font-weight: bold; font-size: 1.2rem; color: #1e40af;">Bogotá, Colombia</div>
      <div style="font-size: 1.5rem; font-weight: bold; color: #1e293b; font-family: monospace;">Longitud: 74° 04' Oeste</div>
      <div style="color: #64748b; font-size: 0.9rem;">Está a 74° al <strong>oeste</strong> de Greenwich → en el continente americano</div>
    </div>
  </div>
</div>

> 💡 **Interpretación:** Bogotá está en el **hemisferio occidental** (W = Oeste). Si arrastras el punto naranja hacia la izquierda del gráfico hasta aproximadamente 74°, ¡esa es la longitud de Bogotá!

---

### 🌍 Coordenadas completas de Bogotá

<div style="background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); border: 2px solid #22c55e; border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0; text-align: center;">
  <div style="font-size: 2rem; margin-bottom: 0.5rem;">🇨🇴 Bogotá, Colombia</div>
  <div style="font-size: 2rem; font-weight: bold; color: #1e293b; font-family: monospace; letter-spacing: 2px;">
    4° 36' N &nbsp;&nbsp;•&nbsp;&nbsp; 74° 04' W
  </div>
  <div style="color: #64748b; margin-top: 0.5rem;">
    ↑ Latitud (Norte) &nbsp;&nbsp;&nbsp;&nbsp; ↑ Longitud (Oeste)
  </div>
</div>

**📍 Visualización: Bogotá en el Globo Terráqueo**

<div style="background: linear-gradient(135deg, #0f172a, #1e293b); border: 2px solid #475569; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-globo-3d" width="500" height="450" style="width: 100%; max-width: 500px; height: auto; display: block; margin: 0 auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-globo-3d')) {
    var canvas = document.getElementById('roughjs-globo-3d');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    var cx = 250, cy = 210, R = 160;
    
    // Fondo espacial
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, 500, 450);
    
    // Estrellas
    ctx.fillStyle = '#475569';
    for (var i = 0; i < 30; i++) {
      ctx.beginPath();
      ctx.arc(Math.random() * 500, Math.random() * 450, 1, 0, Math.PI * 2);
      ctx.fill();
    }
    
    // Globo terráqueo (esfera)
    rc.circle(cx, cy, R * 2, { stroke: '#60a5fa', strokeWidth: 2, fill: '#1e3a5f', fillStyle: 'solid', roughness: 0.3 });
    
    // Líneas de paralelos (latitudes)
    for (var lat = -60; lat <= 60; lat += 30) {
      var yOffset = R * Math.sin(lat * Math.PI / 180);
      var rParalelo = R * Math.cos(lat * Math.PI / 180);
      rc.ellipse(cx, cy + yOffset, rParalelo * 2, rParalelo * 0.3, { stroke: '#475569', strokeWidth: 0.5, roughness: 0.2 });
    }
    
    // Ecuador (destacado en verde)
    rc.ellipse(cx, cy, R * 2, R * 0.35, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.3 });
    
    // Meridiano de Greenwich (naranja)
    rc.ellipse(cx, cy, R * 0.35, R * 2, { stroke: '#f59e0b', strokeWidth: 3, roughness: 0.3 });
    
    // Polo Norte
    rc.circle(cx, cy - R, 14, { fill: '#ef4444', fillStyle: 'solid', stroke: '#7f1d1d', strokeWidth: 2, roughness: 0.3 });
    
    // Polo Sur
    rc.circle(cx, cy + R, 14, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1e40af', strokeWidth: 2, roughness: 0.3 });
    
    // Bogotá en el borde izquierdo
    var bogotaX = cx - R * 0.95;
    var bogotaY = cy - R * 0.08;
    
    rc.circle(bogotaX, bogotaY, 22, { fill: '#ef4444', fillStyle: 'solid', stroke: '#fcd34d', strokeWidth: 4, roughness: 0.3 });
    
    // Líneas de referencia
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(bogotaX, bogotaY);
    ctx.lineTo(cx, bogotaY);
    ctx.strokeStyle = '#22c55e';
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(bogotaX, bogotaY);
    ctx.lineTo(bogotaX, cy);
    ctx.strokeStyle = '#f59e0b';
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Etiquetas
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillStyle = '#f8fafc';
    ctx.fillText('🌍 Ubicación de Bogotá', cx, 30);
    
    ctx.font = '12px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('Polo Norte', cx, cy - R - 20);
    ctx.fillStyle = '#60a5fa';
    ctx.fillText('Polo Sur', cx, cy + R + 28);
    
    ctx.fillStyle = '#22c55e';
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillText('ECUADOR 0°', cx + R + 25, cy + 5);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('GREENWICH 0°', cx, cy - R - 35);
    
    // Etiqueta Bogotá
    ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
    ctx.fillRect(bogotaX - 80, bogotaY - 50, 70, 45);
    ctx.strokeStyle = '#fcd34d';
    ctx.lineWidth = 1;
    ctx.strokeRect(bogotaX - 80, bogotaY - 50, 70, 45);
    
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#fcd34d';
    ctx.fillText('BOGOTÁ', bogotaX - 45, bogotaY - 32);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText("4° 36' N", bogotaX - 45, bogotaY - 18);
    ctx.fillText("74° 04' W", bogotaX - 45, bogotaY - 5);
    
    // Leyenda
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('━━ Ecuador (0° lat)', 30, 415);
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('━━ Greenwich (0° lon)', 30, 433);
    ctx.fillStyle = '#ef4444';
    ctx.fillText('● Bogotá', 280, 415);
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('--- Líneas referencia', 280, 433);
  }
});
</script>
> 💡 **Observa:** Bogotá está **muy cerca del ecuador** (solo 4.6° al norte) y **74° al oeste** de Greenwich (en América del Sur).

---

### 📊 Ejemplo: Ubicación de ciudades

| Ciudad | Latitud | Longitud |
|--------|---------|----------|
| Bogotá, Colombia | 4° 36' Norte | 74° 04' Oeste |
| Ciudad de México | 19° 26' Norte | 99° 07' Oeste |
| Buenos Aires | 34° 36' Sur | 58° 22' Oeste |
| Madrid, España | 40° 25' Norte | 3° 42' Oeste |

> 💡 **¿Por qué se usa el sistema sexagesimal aquí?** Porque permite ubicar cualquier punto en la Tierra con una precisión de **metros** (usando segundos de arco).

### ¿Cuánto mide un segundo de arco en la superficie terrestre?

$$
1'' \approx 31 \text{ metros}
$$

¡Esto permite ubicar una casa específica en cualquier parte del mundo!

---

## ⚙️ **Ejemplo 1 — Ángulo recto en notación completa**

**Problema:** Expresa un ángulo recto en notación completa.

**Solución:**

$$
90° = 90° \, 0' \, 0''
$$

> ✅ Se lee: "Noventa grados, cero minutos, cero segundos"

---

## ⚙️ **Ejemplo 2 — Interpretar coordenadas**

**Problema:** La latitud de Bogotá es $4° \, 36'$ Norte. ¿Qué significa esto?

**Solución:**

- Bogotá está a **4 grados y 36 minutos** al NORTE del ecuador
- Esto es un ángulo muy pequeño (cerca del ecuador)
- Colombia está cerca de la línea ecuatorial, por eso tiene clima tropical

> ✅ La posición se mide como un **ángulo** desde el centro de la Tierra.

---

## ⚙️ **Ejemplo 3 — Ángulo preciso de topografía**

**Problema:** Un topógrafo mide un ángulo de terreno y obtiene $47° \, 23' \, 15''$. ¿Cómo se lee?

**Solución:**

Se lee: **"Cuarenta y siete grados, veintitrés minutos, quince segundos"**

Esto significa:
- 47 grados completos
- más 23/60 de grado adicional
- más 15/3600 de grado adicional

> ✅ Los topógrafos usan segundos para mediciones muy precisas.

---

## ⚙️ **Ejemplo 4 — Comparación tiempo vs ángulos**

**Problema:** Si 2 horas 45 minutos es un tiempo válido, ¿cuál sería el ángulo equivalente?

**Solución:**

$$
2 \text{ horas } 45 \text{ min} \rightarrow 2° \, 45'
$$

Se lee: "Dos grados, cuarenta y cinco minutos"

> ✅ La estructura es idéntica: horas-minutos-segundos = grados-minutos-segundos.

---

## ⚙️ **Ejemplo 5 — Convertir grados a minutos**

**Problema:** ¿Cuántos minutos hay en 3°?

**Solución:**

$$
3° = 3 \times 60' = \boxed{180'}
$$

> ✅ Multiplicamos por 60 porque 1° = 60'.

---

## 📋 **Resumen del Sistema Sexagesimal**

| Unidad | Símbolo | Equivalencia |
|--------|---------|--------------|
| Grado | ° | Unidad base |
| Minuto | ' | 1° = 60' |
| Segundo | '' | 1' = 60'' |

| Aplicación | Uso del sistema sexagesimal |
|------------|----------------------------|
| **Ángulos** | Medir ángulos con precisión |
| **Tiempo** | Horas, minutos, segundos |
| **Geografía** | Latitud y longitud |
| **Astronomía** | Posición de estrellas y planetas |

---

## 📝 **Ejercicios de práctica**

### Ejercicio 1

Escribe los siguientes ángulos en notación completa (grados, minutos, segundos):

1. Un ángulo recto
2. Un ángulo llano
3. Un ángulo de vuelta completa

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $90° \, 0' \, 0''$
2. $180° \, 0' \, 0''$
3. $360° \, 0' \, 0''$

</details>

---

### Ejercicio 2

Completa las equivalencias:

| Conversión | Resultado |
|------------|-----------|
| 1° = ______ minutos | |
| 1' = ______ segundos | |
| 1° = ______ segundos | |
| 2° = ______ minutos | |
| 5' = ______ segundos | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Conversión | Resultado |
|------------|-----------|
| 1° = 60' | |
| 1' = 60'' | |
| 1° = 3600'' | |
| 2° = 120' | |
| 5' = 300'' | |

</details>

---

### Ejercicio 3

Lee correctamente los siguientes ángulos:

1. $25° \, 40' \, 10''$
2. $90° \, 0' \, 0''$
3. $180°$
4. $12° \, 30'$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. "Veinticinco grados, cuarenta minutos, diez segundos"
2. "Noventa grados" (ángulo recto)
3. "Ciento ochenta grados" (ángulo llano)
4. "Doce grados, treinta minutos"

</details>

---

### Ejercicio 4

La latitud de Ciudad de México es $19° \, 26'$ Norte. ¿Qué significa esto?

<details>
<summary><strong>Ver respuesta</strong></summary>

Ciudad de México está a **19 grados y 26 minutos** al norte del ecuador. Es una latitud más alta que Bogotá (4° 36' N), por lo que está más alejada del ecuador.

</details>

---

### Ejercicio 5

¿Cuántos segundos de arco hay en medio grado (0.5°)?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
0.5° = 0.5 \times 60' = 30'
$$

$$
30' = 30 \times 60'' = \boxed{1800''}
$$

En medio grado hay **1800 segundos** de arco.

</details>

---
