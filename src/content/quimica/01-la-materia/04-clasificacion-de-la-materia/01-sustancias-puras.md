# Sustancias Puras

¿Es el agua del grifo una sustancia pura? ¿Y el oxígeno? ¿Y el aire? Para responder estas preguntas, necesitamos entender qué significa "puro" en química, que es diferente de lo que significa en la vida cotidiana.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una sustancia pura en química
- La diferencia entre elementos y compuestos
- Cómo reconocer una sustancia pura
- La Tabla Periódica como lista de elementos

---

## 📊 Mapa Conceptual: Clasificación de la Materia

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-mapa-materia" width="800" height="520" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-mapa-materia')) {
    var canvas = document.getElementById('roughjs-mapa-materia');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Función para dibujar caja con texto
    function drawBox(x, y, w, h, fill, stroke, title, subtitle) {
      rc.rectangle(x - w/2, y - h/2, w, h, { fill: fill, fillStyle: 'solid', stroke: stroke, strokeWidth: 2, roughness: 0.5 });
      ctx.font = 'bold 12px Inter, sans-serif';
      ctx.fillStyle = stroke;
      ctx.textAlign = 'center';
      ctx.fillText(title, x, y - 2);
      if (subtitle) {
        ctx.font = '10px Inter, sans-serif';
        ctx.fillStyle = '#64748b';
        ctx.fillText(subtitle, x, y + 12);
      }
    }
    
    // Función para dibujar línea conectora
    function drawLine(x1, y1, x2, y2) {
      rc.line(x1, y1, x2, y2, { stroke: '#94a3b8', strokeWidth: 2, roughness: 0.3 });
    }
    
    // Título
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Clasificación de la Materia', 400, 25);
    
    // === NIVEL 1: MATERIA ===
    drawBox(400, 60, 120, 40, '#e0e7ff', '#6366f1', 'MATERIA', '');
    
    // Líneas de MATERIA a nivel 2
    drawLine(400, 80, 400, 100);
    drawLine(200, 100, 600, 100);
    drawLine(200, 100, 200, 120);
    drawLine(600, 100, 600, 120);
    
    // === NIVEL 2: SUSTANCIAS PURAS y MEZCLAS ===
    drawBox(200, 145, 150, 50, '#dbeafe', '#3b82f6', 'SUSTANCIAS PURAS', '(composición fija)');
    drawBox(600, 145, 150, 50, '#dcfce7', '#22c55e', 'MEZCLAS', '(composición variable)');
    
    // Líneas de SUSTANCIAS PURAS a nivel 3
    drawLine(200, 170, 200, 195);
    drawLine(120, 195, 280, 195);
    drawLine(120, 195, 120, 215);
    drawLine(280, 195, 280, 215);
    
    // Líneas de MEZCLAS a nivel 3
    drawLine(600, 170, 600, 195);
    drawLine(500, 195, 700, 195);
    drawLine(500, 195, 500, 215);
    drawLine(700, 195, 700, 215);
    
    // === NIVEL 3: ELEMENTOS, COMPUESTOS, HOMOGÉNEAS, HETEROGÉNEAS ===
    drawBox(120, 250, 110, 55, '#fef3c7', '#f59e0b', 'ELEMENTOS', '(1 tipo de átomo)');
    drawBox(280, 250, 110, 55, '#fee2e2', '#ef4444', 'COMPUESTOS', '(2+ elementos)');
    drawBox(500, 250, 120, 55, '#d1fae5', '#10b981', 'HOMOGÉNEAS', '(uniformes)');
    drawBox(700, 250, 120, 55, '#fce7f3', '#ec4899', 'HETEROGÉNEAS', '(no uniformes)');
    
    // Líneas a nivel 4 (ejemplos)
    drawLine(120, 278, 120, 305);
    drawLine(280, 278, 280, 305);
    drawLine(500, 278, 500, 305);
    drawLine(700, 278, 700, 305);
    
    // === NIVEL 4: EJEMPLOS ===
    // Elementos - ejemplos
    rc.rectangle(60, 310, 120, 70, { fill: '#fffbeb', fillStyle: 'solid', stroke: '#f59e0b', strokeWidth: 1.5, roughness: 0.4 });
    ctx.font = 'bold 10px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('Ejemplos:', 120, 325);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Fe (hierro)', 120, 342);
    ctx.fillText('Au (oro)', 120, 356);
    ctx.fillText('O₂, N₂', 120, 370);
    
    // Compuestos - ejemplos
    rc.rectangle(220, 310, 120, 70, { fill: '#fef2f2', fillStyle: 'solid', stroke: '#ef4444', strokeWidth: 1.5, roughness: 0.4 });
    ctx.font = 'bold 10px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('Ejemplos:', 280, 325);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('H₂O (agua)', 280, 342);
    ctx.fillText('NaCl (sal)', 280, 356);
    ctx.fillText('CO₂, NH₃', 280, 370);
    
    // Homogéneas - subtipos
    rc.rectangle(435, 310, 130, 90, { fill: '#ecfdf5', fillStyle: 'solid', stroke: '#10b981', strokeWidth: 1.5, roughness: 0.4 });
    ctx.font = 'bold 10px Inter, sans-serif';
    ctx.fillStyle = '#10b981';
    ctx.fillText('Subtipos:', 500, 325);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• Soluciones', 500, 342);
    ctx.fillText('  (agua salada)', 500, 355);
    ctx.fillText('• Aleaciones', 500, 372);
    ctx.fillText('  (bronce, acero)', 500, 385);
    
    // Heterogéneas - subtipos
    rc.rectangle(635, 310, 130, 90, { fill: '#fdf2f8', fillStyle: 'solid', stroke: '#ec4899', strokeWidth: 1.5, roughness: 0.4 });
    ctx.font = 'bold 10px Inter, sans-serif';
    ctx.fillStyle = '#ec4899';
    ctx.fillText('Subtipos:', 700, 325);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('• Suspensiones', 700, 342);
    ctx.fillText('  (arena en agua)', 700, 355);
    ctx.fillText('• Coloides (leche)', 700, 372);
    ctx.fillText('• Emulsiones', 700, 385);
    
    // === LEYENDA DE SEPARACIÓN ===
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'left';
    ctx.fillText('¿Cómo se separan?', 50, 430);
    
    // Sustancias puras
    rc.rectangle(50, 440, 180, 35, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', strokeWidth: 1.5, roughness: 0.4 });
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Sustancias Puras:', 70, 455);
    ctx.fillStyle = '#64748b';
    ctx.fillText('Métodos químicos', 70, 468);
    
    // Mezclas
    rc.rectangle(250, 440, 180, 35, { fill: '#dcfce7', fillStyle: 'solid', stroke: '#22c55e', strokeWidth: 1.5, roughness: 0.4 });
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('Mezclas:', 270, 455);
    ctx.fillStyle = '#64748b';
    ctx.fillText('Métodos físicos', 270, 468);
    
    // Nota importante
    ctx.font = 'italic 10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.textAlign = 'center';
    ctx.fillText('💡 Los elementos NO se pueden descomponer. Los compuestos SÍ (por reacción química).', 400, 505);
  }
});
</script>

### 📋 Tabla Resumen

| Tipo | Definición | ¿Se puede descomponer? | Ejemplos |
|------|------------|------------------------|----------|
| **Elemento** | Un solo tipo de átomo | No (por métodos químicos) | Fe, Au, O₂, N₂ |
| **Compuesto** | Dos o más elementos unidos químicamente | Sí (por métodos químicos) | H₂O, NaCl, CO₂ |

---

## 📖 ¿Qué es una Sustancia Pura?

> Una **sustancia pura** tiene una composición definida y constante. Todas sus partículas son idénticas.

### 💡 Características de las sustancias puras:

- Composición **uniforme** y **constante**
- Propiedades físicas y químicas **definidas**
- Punto de fusión y ebullición **exactos**
- No pueden separarse por métodos físicos

### ⚙️ Ejemplo: Agua destilada vs Agua del grifo

| Propiedad | Agua destilada | Agua del grifo |
|-----------|---------------|----------------|
| Composición | 100% H₂O | H₂O + minerales + cloro |
| ¿Es sustancia pura? | **Sí** | No (es mezcla) |
| Punto de ebullición | Exactamente 100°C | Aproximadamente 100°C |

---

## 📖 Elementos

> Un **elemento** es una sustancia formada por un solo tipo de átomo. No puede descomponerse en sustancias más simples por métodos químicos.

### 💡 Datos clave sobre los elementos:

- Hay **118 elementos** conocidos (92 naturales, 26 sintéticos)
- Están organizados en la **Tabla Periódica**
- Cada elemento tiene un **símbolo** único
- Son los "ladrillos" básicos de toda la materia

### 📋 Ejemplos de Elementos

| Elemento | Símbolo | Tipo | Presente en |
|----------|---------|------|-------------|
| Hidrógeno | H | No metal | Agua, combustibles |
| Oxígeno | O | No metal | Aire, agua, rocas |
| Carbono | C | No metal | Seres vivos, diamantes |
| Hierro | Fe | Metal | Herramientas, sangre |
| Oro | Au | Metal | Joyería, electrónica |
| Nitrógeno | N | No metal | Aire (78%) |

### 💡 ¿Por qué algunos símbolos no coinciden con el nombre?

Muchos símbolos vienen del **latín**:

| Elemento | Símbolo | Origen latín |
|----------|---------|--------------|
| Hierro | Fe | *Ferrum* |
| Oro | Au | *Aurum* |
| Plata | Ag | *Argentum* |
| Sodio | Na | *Natrium* |
| Potasio | K | *Kalium* |
| Cobre | Cu | *Cuprum* |

---

## 📖 Compuestos

> Un **compuesto** es una sustancia formada por dos o más elementos combinados químicamente en proporciones fijas.

### 💡 Características de los compuestos:

- Los elementos están unidos por **enlaces químicos**
- Tienen propiedades **diferentes** a las de sus elementos
- Se representan con **fórmulas químicas**
- Solo pueden separarse por **métodos químicos** (reacciones)

### 📋 Ejemplos de Compuestos

| Compuesto | Fórmula | Elementos | Proporción |
|-----------|---------|-----------|------------|
| Agua | H₂O | H, O | 2:1 |
| Sal de mesa | NaCl | Na, Cl | 1:1 |
| Dióxido de carbono | CO₂ | C, O | 1:2 |
| Glucosa | C₆H₁₂O₆ | C, H, O | 6:12:6 |
| Amoníaco | NH₃ | N, H | 1:3 |

### ⚙️ Ejemplo: El agua (H₂O) tiene propiedades diferentes a sus elementos

| Componente | Estado | Propiedad característica |
|------------|--------|-------------------------|
| Hidrógeno (H₂) | Gas | Muy inflamable, explota |
| Oxígeno (O₂) | Gas | Alimenta la combustión |
| **Agua (H₂O)** | **Líquido** | **¡Apaga el fuego!** |

El compuesto tiene propiedades completamente diferentes a sus elementos.

### 💡 Ley de las Proporciones Definidas

> Un compuesto siempre tiene la **misma proporción** de elementos, sin importar su origen.

El agua, venga del océano, de la lluvia o de un laboratorio, siempre es:
- 11.1% hidrógeno
- 88.9% oxígeno

En masa: por cada 1 g de H, hay 8 g de O.

---

## 📖 ¿Cómo Distinguir Elementos de Compuestos?

### 💡 Pregunta clave

¿Se puede descomponer en sustancias más simples por métodos químicos?

| Respuesta | Entonces es... |
|-----------|----------------|
| **No** | Elemento |
| **Sí** | Compuesto |

### ⚙️ Ejemplo: La electrólisis del agua

El agua puede descomponerse en hidrógeno y oxígeno usando electricidad:

$$
2\text{H}_2\text{O} \xrightarrow{\text{electricidad}} 2\text{H}_2 + \text{O}_2
$$

Por lo tanto, el agua es un **compuesto**.

Pero el hidrógeno (H₂) y el oxígeno (O₂) no pueden descomponerse más → son **elementos**.

---

## 📖 Moléculas de Elementos

Algunos elementos existen como **moléculas** (grupos de átomos del mismo elemento):

| Elemento | Fórmula molecular | Estado natural |
|----------|-------------------|----------------|
| Hidrógeno | H₂ | Gas diatómico |
| Oxígeno | O₂ | Gas diatómico |
| Nitrógeno | N₂ | Gas diatómico |
| Cloro | Cl₂ | Gas diatómico |
| Ozono | O₃ | Gas triatómico |
| Azufre | S₈ | Sólido (8 átomos) |

Aunque son moléculas, siguen siendo **elementos** porque solo tienen un tipo de átomo.

---

## 🔑 Resumen

| Concepto | Definición | Ejemplo |
|----------|------------|---------|
| **Sustancia pura** | Composición definida y constante | H₂O, NaCl, Fe |
| **Elemento** | Un solo tipo de átomo, no descomponible | Fe, Au, O₂ |
| **Compuesto** | Elementos unidos químicamente en proporción fija | H₂O, CO₂ |
| **Ley de proporciones definidas** | Los compuestos siempre tienen la misma proporción | Agua: siempre 2H:1O |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Clasifica cada sustancia como **elemento (E)** o **compuesto (C)**:

a) Oro (Au)
b) Sal de mesa (NaCl)
c) Oxígeno (O₂)
d) Dióxido de carbono (CO₂)
e) Diamante (C)
f) Agua (H₂O)

<details>
<summary>Ver solución</summary>

a) **E** - Elemento (solo átomos de oro)
b) **C** - Compuesto (sodio + cloro unidos)
c) **E** - Elemento (solo átomos de oxígeno)
d) **C** - Compuesto (carbono + oxígeno unidos)
e) **E** - Elemento (solo átomos de carbono)
f) **C** - Compuesto (hidrógeno + oxígeno unidos)

</details>

### Ejercicio 2
¿Por qué el O₂ es un elemento y el CO₂ es un compuesto?

<details>
<summary>Ver solución</summary>

**O₂ es un elemento porque:**
- Solo contiene átomos de un mismo elemento: oxígeno
- Aunque hay dos átomos unidos (molécula), son del mismo tipo
- No puede descomponerse en sustancias más simples

**CO₂ es un compuesto porque:**
- Contiene átomos de dos elementos diferentes: carbono y oxígeno
- Estos átomos están unidos químicamente
- Puede descomponerse en carbono y oxígeno por métodos químicos

</details>

### Ejercicio 3
El agua siempre contiene 11.1% de hidrógeno y 88.9% de oxígeno en masa. Si tienes 45 g de agua, ¿cuántos gramos de cada elemento hay?

<details>
<summary>Ver solución</summary>

**Hidrógeno:**
$$
m_H = 45 \text{ g} \times 0.111 = \boxed{5.0 \text{ g}}
$$

**Oxígeno:**
$$
m_O = 45 \text{ g} \times 0.889 = \boxed{40.0 \text{ g}}
$$

**Verificación:** 5.0 + 40.0 = 45.0 g ✓

</details>

### Ejercicio 4
Un estudiante afirma que el bronce es un compuesto porque está hecho de cobre y estaño. ¿Tiene razón? Explica.

<details>
<summary>Ver solución</summary>

**No tiene razón.** El bronce es una **mezcla** (aleación), no un compuesto.

**Razones:**
1. El bronce tiene composición **variable** (puede tener diferentes proporciones de Cu y Sn)
2. Los metales no están unidos por enlaces químicos específicos, solo están mezclados
3. Los componentes pueden separarse por métodos físicos (fundición selectiva)

Un compuesto tendría:
- Proporción fija (ej: H₂O siempre es 2:1)
- Enlaces químicos definidos
- Propiedades diferentes a sus elementos

</details>
