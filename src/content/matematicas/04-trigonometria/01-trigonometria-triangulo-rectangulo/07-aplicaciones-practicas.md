# **Aplicaciones Prácticas de Trigonometría**

¿Cómo calculan los ingenieros la altura de un edificio sin subir a él? ¿Cómo sabe un piloto a qué distancia está del aeropuerto? La trigonometría resuelve estos problemas usando **ángulos de elevación** y **ángulos de depresión**. ¡Vamos a descubrirlo!

---

## 🎯 ¿Qué vas a aprender?

- Qué es un ángulo de elevación y cuándo usarlo.
- Qué es un ángulo de depresión y cuándo usarlo.
- Cómo resolver problemas de alturas y distancias inaccesibles.
- Estrategias para plantear ecuaciones trigonométricas a partir de situaciones reales.

---

## 📋 Lo Esencial: Ángulos de Elevación y Depresión

| Concepto | Definición | Cuándo se usa |
|----------|------------|---------------|
| **Ángulo de elevación** | Ángulo desde la horizontal hacia ARRIBA | Cuando miras algo más alto que tú |
| **Ángulo de depresión** | Ángulo desde la horizontal hacia ABAJO | Cuando miras algo más bajo que tú |

> 💡 **Dato clave:** El ángulo de depresión desde A hacia B es **igual** al ángulo de elevación desde B hacia A (ángulos alternos internos).

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1.1rem;">🎨</span> <strong style="color: #1e293b;">Ángulo de elevación vs Ángulo de depresión</strong>
  </div>
  <div id="rough-elevacion-depresion" style="width: 100%; height: 280px;"></div>
</div>

<script type="module">
import rough from 'https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.esm.js';
document.addEventListener('DOMContentLoaded', function() {
  const container = document.getElementById('rough-elevacion-depresion');
  if (!container) return;
  
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('viewBox', '0 0 600 260');
  svg.style.width = '100%';
  svg.style.height = '100%';
  container.appendChild(svg);
  
  const rc = rough.svg(svg);
  
  // === LADO IZQUIERDO: ELEVACIÓN ===
  // Suelo
  svg.appendChild(rc.line(20, 200, 270, 200, { stroke: '#64748b', strokeWidth: 2 }));
  // Edificio
  svg.appendChild(rc.rectangle(200, 60, 50, 140, { fill: '#94a3b8', fillStyle: 'hachure', roughness: 1.2 }));
  // Persona
  svg.appendChild(rc.circle(60, 185, 25, { fill: '#3b82f6', fillStyle: 'solid' }));
  svg.appendChild(rc.line(60, 197, 60, 200, { stroke: '#1e293b', strokeWidth: 2 }));
  // Línea horizontal
  svg.appendChild(rc.line(60, 175, 200, 175, { stroke: '#94a3b8', strokeWidth: 1.5, strokeLineDash: [5,5] }));
  // Línea de visión (elevación)
  svg.appendChild(rc.line(60, 175, 225, 60, { stroke: '#22c55e', strokeWidth: 2.5 }));
  
  // === LADO DERECHO: DEPRESIÓN ===
  // Agua
  svg.appendChild(rc.line(330, 200, 580, 200, { stroke: '#60a5fa', strokeWidth: 3 }));
  // Torre/Faro
  svg.appendChild(rc.rectangle(350, 80, 35, 120, { fill: '#fef3c7', fillStyle: 'hachure', roughness: 1.2, stroke: '#f97316' }));
  // Barco
  svg.appendChild(rc.ellipse(520, 195, 50, 15, { fill: '#94a3b8', fillStyle: 'solid' }));
  // Línea horizontal desde torre
  svg.appendChild(rc.line(385, 90, 540, 90, { stroke: '#94a3b8', strokeWidth: 1.5, strokeLineDash: [5,5] }));
  // Línea de visión (depresión)
  svg.appendChild(rc.line(385, 90, 520, 185, { stroke: '#ef4444', strokeWidth: 2.5 }));
  
  // Textos
  const addText = (x, y, text, color, size = 12, bold = false) => {
    const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    t.setAttribute('x', x); t.setAttribute('y', y);
    t.textContent = text;
    t.style.fill = color; t.style.fontSize = size + 'px';
    if (bold) t.style.fontWeight = 'bold';
    svg.appendChild(t);
  };
  
  addText(80, 30, 'ELEVACIÓN', '#22c55e', 14, true);
  addText(100, 165, 'α', '#22c55e', 16, true);
  addText(420, 30, 'DEPRESIÓN', '#ef4444', 14, true);
  addText(400, 105, 'β', '#ef4444', 16, true);
  addText(40, 220, '👁 Observador', '#64748b', 11);
  addText(500, 220, '⛵ Barco', '#64748b', 11);
  addText(195, 55, '🏢', '#64748b', 16);
  addText(355, 75, '🔦', '#f97316', 14);
});
</script>

---

## 📖 Ángulo de elevación

> **Definición:** El ángulo de elevación es el ángulo formado entre la **línea horizontal** y la **línea de visión hacia arriba**.

Se usa cuando miramos hacia un objeto que está **más alto** que nosotros.

### Ejemplo

Cuando miras la cima de un edificio desde el suelo, formas un ángulo de elevación.

---

## 📖 Ángulo de depresión

> **Definición:** El ángulo de depresión es el ángulo formado entre la **línea horizontal** y la **línea de visión hacia abajo**.

Se usa cuando miramos hacia un objeto que está **más bajo** que nosotros.

### Propiedad importante

El ángulo de depresión desde un punto A hacia B es **igual** al ángulo de elevación desde B hacia A (por ser ángulos alternos internos).

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Altura de un edificio

Un observador está a 50 m de la base de un edificio. El ángulo de elevación a la cima es 32°. ¿Cuál es la altura del edificio?

<div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1.1rem;">🏢</span> <strong style="color: #166534;">Problema: Altura del edificio</strong>
  </div>
  <div id="rough-edificio" style="width: 100%; height: 260px;"></div>
</div>

<script type="module">
import rough from 'https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.esm.js';
document.addEventListener('DOMContentLoaded', function() {
  const container = document.getElementById('rough-edificio');
  if (!container) return;
  
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('viewBox', '0 0 500 240');
  svg.style.width = '100%'; svg.style.height = '100%';
  container.appendChild(svg);
  
  const rc = rough.svg(svg);
  
  // Suelo
  svg.appendChild(rc.line(30, 200, 350, 200, { stroke: '#64748b', strokeWidth: 2 }));
  // Edificio
  svg.appendChild(rc.rectangle(280, 50, 50, 150, { fill: '#94a3b8', fillStyle: 'hachure', roughness: 1.5 }));
  // Ventanas
  for (let y = 70; y < 190; y += 35) {
    svg.appendChild(rc.rectangle(290, y, 12, 18, { fill: '#bfdbfe', roughness: 0.5 }));
    svg.appendChild(rc.rectangle(308, y, 12, 18, { fill: '#bfdbfe', roughness: 0.5 }));
  }
  // Persona
  svg.appendChild(rc.circle(70, 185, 25, { fill: '#3b82f6', fillStyle: 'solid' }));
  // Línea horizontal
  svg.appendChild(rc.line(70, 175, 280, 175, { stroke: '#94a3b8', strokeWidth: 1.5, strokeLineDash: [5,5] }));
  // Línea de visión
  svg.appendChild(rc.line(70, 175, 305, 50, { stroke: '#22c55e', strokeWidth: 2.5 }));
  // Marca de ángulo recto
  svg.appendChild(rc.rectangle(268, 175, 12, 12, { stroke: '#64748b', fill: 'none', roughness: 0.3 }));
  
  // Textos
  const addText = (x, y, text, color, size = 12, bold = false) => {
    const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    t.setAttribute('x', x); t.setAttribute('y', y);
    t.textContent = text;
    t.style.fill = color; t.style.fontSize = size + 'px';
    if (bold) t.style.fontWeight = 'bold';
    svg.appendChild(t);
  };
  
  addText(150, 218, '50 m', '#3b82f6', 14, true);
  addText(340, 125, 'h = ?', '#ef4444', 14, true);
  addText(100, 165, '32°', '#22c55e', 14, true);
  addText(50, 220, '👤', '#64748b', 14);
  
  // Cuadro de solución
  svg.appendChild(rc.rectangle(370, 60, 120, 80, { fill: '#dcfce7', stroke: '#22c55e', roughness: 0.5 }));
  addText(385, 85, 'tan 32° = h/50', '#166534', 11);
  addText(385, 105, 'h = 50 × tan32°', '#166534', 11);
  addText(385, 130, 'h ≈ 31.2 m', '#15803d', 13, true);
});
</script>

**Razonamiento:**

Queremos calcular el cateto opuesto ($h$) y tenemos el cateto adyacente ($50$) y el ángulo ($32°$). La función que relaciona estos datos es la tangente.

$$
\tan(32°) = \frac{\text{Opuesto}}{\text{Adyacente}} = \frac{h}{50}
$$

Despejamos $h$:

$$
h = 50 \times \tan(32°)
$$

Calculamos:

$$
h = 50 \times 0.625 \approx 31.2
$$

**Resultado:**

$$
\boxed{31.2 \text{ m}}
$$

---

### Ejemplo 2: Distancia a un avión

Desde el suelo, un observador ve un avión con un ángulo de elevación de 28°. El avión está a 5,000 m de altura. ¿A qué distancia horizontal está?

**Datos:**
- Ángulo de elevación: $28°$
- Cateto opuesto (altura): $5000 \text{ m}$
- Cateto adyacente (distancia horizontal $d$): ¿?

**Razonamiento:**

Usamos nuevamente la tangente, pero esta vez la incógnita está en el denominador.

$$
\tan(28°) = \frac{5000}{d}
$$

Despejamos $d$ intercambiando con la tangente:

$$
d = \frac{5000}{\tan(28°)}
$$

$$
d = \frac{5000}{0.5317}
$$

**Resultado:**

$$
\boxed{9405 \text{ m}}
$$

---

### Ejemplo 3: Ángulo de depresión

Desde la cima de un faro de 40 m de altura, el ángulo de depresión hacia un barco es 15°. ¿A qué distancia de la base del faro está el barco?

<div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1.1rem;">🔦</span> <strong style="color: #991b1b;">Problema: Distancia al barco</strong>
  </div>
  <div id="rough-faro" style="width: 100%; height: 260px;"></div>
</div>

<script type="module">
import rough from 'https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.esm.js';
document.addEventListener('DOMContentLoaded', function() {
  const container = document.getElementById('rough-faro');
  if (!container) return;
  
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('viewBox', '0 0 500 240');
  svg.style.width = '100%'; svg.style.height = '100%';
  container.appendChild(svg);
  
  const rc = rough.svg(svg);
  
  // Agua
  svg.appendChild(rc.line(30, 200, 450, 200, { stroke: '#60a5fa', strokeWidth: 4 }));
  // Olas
  for (let x = 50; x < 440; x += 40) {
    svg.appendChild(rc.arc(x, 200, 20, 10, 0, Math.PI, false, { stroke: '#93c5fd', roughness: 0.8 }));
  }
  // Faro
  svg.appendChild(rc.rectangle(60, 50, 40, 150, { fill: '#fef3c7', fillStyle: 'hachure', stroke: '#f97316', roughness: 1.2 }));
  svg.appendChild(rc.rectangle(55, 40, 50, 15, { fill: '#fbbf24', roughness: 0.8 }));
  // Barco
  svg.appendChild(rc.ellipse(380, 195, 60, 18, { fill: '#64748b', fillStyle: 'solid', roughness: 1 }));
  svg.appendChild(rc.line(380, 180, 380, 150, { stroke: '#1e293b', strokeWidth: 2 }));
  svg.appendChild(rc.polygon([[380, 150], [380, 175], [400, 165]], { fill: '#f8fafc', roughness: 0.8 }));
  // Línea horizontal desde faro
  svg.appendChild(rc.line(100, 55, 400, 55, { stroke: '#94a3b8', strokeWidth: 1.5, strokeLineDash: [5,5] }));
  // Línea de visión (depresión)
  svg.appendChild(rc.line(100, 55, 380, 185, { stroke: '#ef4444', strokeWidth: 2.5 }));
  
  // Textos
  const addText = (x, y, text, color, size = 12, bold = false) => {
    const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    t.setAttribute('x', x); t.setAttribute('y', y);
    t.textContent = text;
    t.style.fill = color; t.style.fontSize = size + 'px';
    if (bold) t.style.fontWeight = 'bold';
    svg.appendChild(t);
  };
  
  addText(25, 125, '40 m', '#f97316', 13, true);
  addText(200, 218, 'd = ?', '#3b82f6', 14, true);
  addText(120, 70, '15°', '#ef4444', 14, true);
  addText(65, 35, '🔦', '#f97316', 14);
  addText(365, 225, '⛵', '#64748b', 14);
  
  // Cuadro de solución
  svg.appendChild(rc.rectangle(350, 50, 130, 80, { fill: '#fee2e2', stroke: '#ef4444', roughness: 0.5 }));
  addText(360, 75, 'tan 15° = 40/d', '#991b1b', 11);
  addText(360, 95, 'd = 40/tan15°', '#991b1b', 11);
  addText(360, 120, 'd ≈ 149.3 m', '#dc2626', 13, true);
});
</script>

**Razonamiento:**
El ángulo de depresión es igual al ángulo de elevación desde el barco (alternos internos). Entonces, tenemos un triángulo rectángulo con ángulo de 15°, cateto opuesto de 40 m y buscamos el adyacente.

$$
\tan(15°) = \frac{40}{d}
$$

$$
d = \frac{40}{\tan(15°)} = \frac{40}{0.2679}
$$

**Resultado:**

$$
\boxed{149.3 \text{ m}}
$$

---

### Ejemplo 4: Escalera apoyada

Una escalera de 6 m se apoya contra una pared formando un ángulo de 70° con el suelo. ¿A qué altura llega?

<div style="background: #fefce8; border: 1px solid #fef08a; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1.1rem;">🪜</span> <strong style="color: #a16207;">Problema: Escalera apoyada</strong>
  </div>
  <div id="rough-escalera" style="width: 100%; height: 260px;"></div>
</div>

<script type="module">
import rough from 'https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.esm.js';
document.addEventListener('DOMContentLoaded', function() {
  const container = document.getElementById('rough-escalera');
  if (!container) return;
  
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  svg.setAttribute('viewBox', '0 0 400 240');
  svg.style.width = '100%'; svg.style.height = '100%';
  container.appendChild(svg);
  
  const rc = rough.svg(svg);
  
  // Pared
  svg.appendChild(rc.rectangle(200, 30, 15, 180, { fill: '#cbd5e1', fillStyle: 'hachure', roughness: 1.5 }));
  // Suelo
  svg.appendChild(rc.line(50, 210, 300, 210, { stroke: '#64748b', strokeWidth: 2 }));
  // Escalera
  svg.appendChild(rc.line(100, 210, 200, 55, { stroke: '#f97316', strokeWidth: 5, roughness: 1.2 }));
  // Peldaños
  for (let i = 1; i < 6; i++) {
    const x1 = 100 + (100 * i / 6);
    const y1 = 210 - (155 * i / 6);
    const x2 = x1 + 8;
    const y2 = y1 - 6;
    svg.appendChild(rc.line(x1 - 5, y1, x2, y2, { stroke: '#ea580c', strokeWidth: 2 }));
  }
  // Marca de ángulo recto
  svg.appendChild(rc.rectangle(188, 198, 12, 12, { stroke: '#64748b', fill: 'none', roughness: 0.3 }));
  
  // Textos
  const addText = (x, y, text, color, size = 12, bold = false) => {
    const t = document.createElementNS('http://www.w3.org/2000/svg', 'text');
    t.setAttribute('x', x); t.setAttribute('y', y);
    t.textContent = text;
    t.style.fill = color; t.style.fontSize = size + 'px';
    if (bold) t.style.fontWeight = 'bold';
    svg.appendChild(t);
  };
  
  addText(120, 120, '6 m', '#f97316', 14, true);
  addText(220, 130, 'h = ?', '#ef4444', 14, true);
  addText(105, 195, '70°', '#8b5cf6', 14, true);
  addText(220, 25, 'Pared', '#64748b', 11);
  addText(130, 225, 'Suelo', '#64748b', 11);
  
  // Cuadro de solución
  svg.appendChild(rc.rectangle(260, 50, 120, 80, { fill: '#fef9c3', stroke: '#eab308', roughness: 0.5 }));
  addText(270, 75, 'sin 70° = h/6', '#a16207', 11);
  addText(270, 95, 'h = 6 × sin70°', '#a16207', 11);
  addText(270, 120, 'h ≈ 5.6 m', '#ca8a04', 13, true);
});
</script>

**Razonamiento:**
Conocemos la hipotenusa (largo de la escalera, 6m) y el ángulo (70°). Queremos la altura (cateto opuesto).

$$
\sin(70°) = \frac{h}{6}
$$

$$
h = 6 \times \sin(70°)
$$

$$
h = 6 \times 0.9397 \approx 5.64
$$

**Resultado:**

$$
\boxed{5.64 \text{ m}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Un observador está a 25 m de la base de un árbol. El ángulo de elevación a la cima es 40°. ¿Cuál es la altura del árbol?

<details>
<summary>Ver solución</summary>

**Datos:**
- Adyacente = 25 m
- Ángulo = 40°
- Opuesto (altura) = ?

**Razonamiento:**
Usamos tangente: $\tan(40°) = h/25 \rightarrow h = 25 \times \tan(40°)$

**Resultado:**

$$
\boxed{21 \text{ m}}
$$

</details>

---

### Ejercicio 2
Una torre proyecta una sombra de 30 m cuando el ángulo de elevación del sol es 55°. ¿Cuál es la altura de la torre?

<details>
<summary>Ver solución</summary>

**Datos:**
- Adyacente (sombra) = 30 m
- Ángulo = 55°
- Opuesto (altura) = ?

**Razonamiento:**
Usamos tangente: $\tan(55°) = h/30$.

$$
h = 30 \times \tan(55°) = 30 \times 1.428
$$

**Resultado:**

$$
\boxed{42.8 \text{ m}}
$$

</details>

---

### Ejercicio 3
Un avión vuela a 8,000 m de altura. Un observador en tierra lo ve con un ángulo de elevación de 35°. ¿Cuál es la distancia en línea recta del observador al avión?

<details>
<summary>Ver solución</summary>

**Datos:**
- Opuesto (altura) = 8000 m
- Ángulo = 35°
- Hipotenusa (distancia) = ?

**Razonamiento:**
Usamos seno, porque involucra opuesto e hipotenusa: $\sin(35°) = 8000/d$.
Despejando d: $d = 8000 / \sin(35°)$.

**Resultado:**

$$
\boxed{13\,948 \text{ m}}
$$

</details>

---

### Ejercicio 4
Desde un faro de 50 m de altura, un guardacostas ve un bote con un ángulo de depresión de 12°. ¿A qué distancia está el bote de la base del faro?

<details>
<summary>Ver solución</summary>

**Datos:**
- Opuesto = 50 m
- Ángulo = 12°
- Adyacente (distancia) = ?

**Razonamiento:**
Usamos tangente: $\tan(12°) = 50/d$.
Despejando d: $d = 50 / \tan(12°)$.

**Resultado:**

$$
\boxed{235 \text{ m}}
$$

</details>

---

### Ejercicio 5
Una rampa de acceso debe tener un ángulo de inclinación máximo de 8°. Si la rampa debe subir 60 cm, ¿cuál es la longitud mínima de la rampa (hipotenusa)?

<details>
<summary>Ver solución</summary>

**Datos:**
- Opuesto = 60 cm
- Ángulo = 8°
- Hipotenusa = ?

**Razonamiento:**
Usamos seno: $\sin(8°) = 60/L$.
Despejando L: $L = 60/ \sin(8°)$.

**Resultado:**

$$
\boxed{431 \text{ cm}}
$$

</details>

---

### Ejercicio 6
Un niño vuela una cometa soltando 50 m de hilo. Si el hilo está tenso y forma un ángulo de 60° con el suelo, ¿a qué altura está la cometa?

<details>
<summary>Ver solución</summary>

**Datos:**
- Hipotenusa = 50 m
- Ángulo = 60°
- Opuesto (altura) = ?

**Razonamiento:**
Usamos seno: $\sin(60°) = h/50$.
$h = 50 \times \sin(60°) = 50 \times 0.866$.

**Resultado:**

$$
\boxed{43.3 \text{ m}}
$$

</details>

---

### Ejercicio 7
Un poste vertical de 5 metros de altura proyecta una sombra de 5 metros. ¿Cuál es el ángulo de elevación del sol?

<details>
<summary>Ver solución</summary>

**Datos:**
- Opuesto = 5 m
- Adyacente = 5 m
- Ángulo = ?

**Razonamiento:**
$\tan(\alpha) = 5/5 = 1$.
El ángulo cuya tangente es 1 es 45°.

**Resultado:**

$$
\boxed{45°}
$$

</details>

---

### Ejercicio 8
Una carretera sube de forma constante. Si por cada 100 metros que avanzas horizontalmente subes 10 metros, ¿cuál es el ángulo de inclinación de la carretera?

<details>
<summary>Ver solución</summary>

**Datos:**
- Opuesto = 10 m
- Adyacente = 100 m
- Ángulo = ?

**Razonamiento:**
$\tan(\alpha) = 10/100 = 0.1$.
Calculamos arco tangente: $\alpha = \arctan(0.1)$.

**Resultado:**

$$
\boxed{5.7°}
$$

</details>

---

### Ejercicio 9
Una escalera de 10 metros se apoya en una pared. Si el pie de la escalera está a 3 metros de la pared, ¿qué ángulo forma la escalera con el suelo?

<details>
<summary>Ver solución</summary>

**Datos:**
- Hipotenusa = 10 m
- Adyacente = 3 m
- Ángulo = ?

**Razonamiento:**
Usamos coseno: $\cos(\alpha) = 3/10 = 0.3$.
Calculamos arco coseno: $\alpha = \arccos(0.3)$.

**Resultado:**

$$
\boxed{72.5°}
$$

</details>

---

### Ejercicio 10
Un tobogán tiene una longitud de 4 metros y la altura desde donde se lanza es de 2 metros. ¿Cuál es el ángulo de inclinación del tobogán con respecto al suelo?

<details>
<summary>Ver solución</summary>

**Datos:**
- Hipotenusa = 4 m
- Opuesto = 2 m
- Ángulo = ?

**Razonamiento:**
Usamos seno: $\sin(\alpha) = 2/4 = 0.5$.
El ángulo cuyo seno es 0.5 es 30°.

**Resultado:**

$$
\boxed{30°}
$$

</details>

---

## 🔑 Resumen

| Situación | Datos conocidos | Incógnita | Razón sugerida |
|-----------|-----------------|-----------|----------------|
| **Altura, dada la sombra** | Cateto Ady, Ángulo | Cateto Op | **Tangente** |
| **Sombra, dada la altura** | Cateto Op, Ángulo | Cateto Ady | **Tangente** |
| **Longitud escalera/rampa** | Altura, Ángulo | Hipotenusa | **Seno** |
| **Distancia horizontal rampa** | Longitud, Ángulo | Cateto Ady | **Coseno** |

> **Conclusión:** La clave para resolver estos problemas es identificar correctamente el triángulo rectángulo, ubicar qué lado tienes y qué lado buscas, y elegir la razón trigonométrica (SOH-CAH-TOA) que los relacione.
