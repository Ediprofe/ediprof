# Punto, Recta y Plano

En geometría, antes de estudiar figuras complejas como triángulos o círculos, debemos conocer los **tres elementos fundamentales** que son la base de todo: el punto, la recta y el plano. Estos se llaman **conceptos primitivos** porque no pueden definirse con otros más simples.

---

## 📖 El Punto

### ¿Qué es un punto?

Un **punto** indica una **posición** en el espacio, pero no tiene tamaño. No tiene largo, ni ancho, ni alto. Es la unidad más pequeña de la geometría.

> **Definición:** Un punto es un objeto geométrico sin dimensiones que representa únicamente una ubicación.

### Cómo representar un punto

- Se representa con un **pequeño círculo** o marca
- Se nombra con **letras mayúsculas**: $A$, $B$, $P$, $Q$

**Representación de los puntos $A$, $B$ y $P$:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-punto" style="width: 100%; height: 220px; min-height: 200px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-punto')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-punto', {
      boundingbox: [-1, 4, 10, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Múltiples puntos con diferentes nombres
    board.create('point', [1.5, 2], {name: 'A', size: 6, fixed: true, color: '#3b82f6', label: {fontSize: 16, color: '#3b82f6', offset: [12, 5]}});
    board.create('point', [4.5, 2], {name: 'B', size: 6, fixed: true, color: '#22c55e', label: {fontSize: 16, color: '#22c55e', offset: [12, 5]}});
    board.create('point', [7.5, 2], {name: 'P', size: 6, fixed: true, color: '#f59e0b', label: {fontSize: 16, color: '#f59e0b', offset: [12, 5]}});
    
    board.create('text', [4.5, 0.5, 'Se nombran con letras MAYÚSCULAS'], {fontSize: 11, color: '#64748b', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

### Ejemplos de puntos en la vida real

Aunque un punto matemático no tiene tamaño, podemos asociarlo con objetos muy pequeños:

| Objeto | ¿Por qué representa un punto? |
|--------|------------------------------|
| La punta de un alfiler | Muy pequeña, indica posición |
| Una estrella lejana en el cielo | Desde lejos parece un punto de luz |
| La intersección de dos calles | Marca una ubicación exacta |
| Un pixel en la pantalla | Mínima unidad visible |

### Ejemplo 1

Si queremos marcar la ubicación de una ciudad en un mapa, usamos un punto. El punto no representa el tamaño de la ciudad, solo su **posición**.

### Ejemplo 2

En un juego de "hundir la flota" o "batalla naval", cada casilla se identifica por un punto determinado por coordenadas (por ejemplo, B-4).

---

## 📖 La Recta

### ¿Qué es una recta?

Una **recta** es una sucesión infinita de puntos alineados en una misma dirección. Se extiende infinitamente en ambos sentidos.

> **Definición:** Una recta es un conjunto infinito de puntos que se extienden sin fin en dos direcciones opuestas, sin curvas ni quiebres.

### Propiedades de la recta

- Tiene **una sola dimensión**: longitud (pero infinita)
- No tiene **ancho** ni **grosor**
- Es **completamente derecha** (sin curvas)
- Se extiende **infinitamente** en ambas direcciones

### Cómo representar una recta

Se puede nombrar de dos formas:

1. **Con una letra minúscula**: $l$, $m$, $r$
2. **Con dos puntos que pertenecen a ella**: $\overleftrightarrow{AB}$ (se lee "recta AB")

Las flechas en ambos extremos indican que continúa infinitamente.

**Representación de la recta $\overleftrightarrow{AB}$ (también notada como $l$):**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-recta" style="width: 100%; height: 220px; min-height: 200px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-recta')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-recta', {
      boundingbox: [-1, 4, 12, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Puntos A y B sobre la recta
    var pA = board.create('point', [2, 2], {name: 'A', size: 5, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [0, 12]}});
    var pB = board.create('point', [9, 2], {name: 'B', size: 5, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [0, 12]}});
    
    // Recta que pasa por A y B (se extiende infinitamente)
    board.create('line', [pA, pB], {strokeColor: '#22c55e', strokeWidth: 3});
    
    // Flechas indicativas
    board.create('text', [-0.2, 2, '←'], {fontSize: 18, color: '#22c55e'});
    board.create('text', [11, 2, '→'], {fontSize: 18, color: '#22c55e'});
    
    board.create('text', [5.5, 0.5, 'Se extiende INFINITAMENTE en ambas direcciones'], {fontSize: 11, color: '#64748b', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

### Ejemplos de rectas en la vida real

| Objeto | ¿Por qué representa una recta? |
|--------|-------------------------------|
| El horizonte | Parece extenderse infinitamente |
| Un rayo de luz láser | Viaja en línea recta |
| El borde de una regla (extendido) | Si lo imaginamos infinito |
| Una cuerda tensa (extendida) | Perfectamente recta |

### Ejemplo 1

Imagina un riel de tren perfectamente recto. Si lo extendemos mentalmente hasta el infinito en ambas direcciones, representa una recta.

### Ejemplo 2

Un rayo de luz láser que viaja en el espacio. Si no hubiera obstáculos, viajaría indefinidamente en línea recta.

---

## 📖 El Plano

### ¿Qué es un plano?

Un **plano** es una superficie infinita, perfectamente lisa, sin grosor, que se extiende en todas direcciones.

> **Definición:** Un plano es una superficie de dos dimensiones (largo y ancho) que se extiende indefinidamente sin bordes ni curvaturas.

### Propiedades del plano

- Tiene **dos dimensiones**: largo y ancho
- No tiene **grosor** (espesor)
- Es **completamente liso** (sin curvas ni ondulaciones)
- Se extiende **infinitamente** en todas direcciones

### Cómo representar un plano

- Se representa usualmente como un **paralelogramo** (romboide)
- Se nombra con **letras griegas**: $\alpha$, $\beta$, $\pi$ (alfa, beta, pi)

**Representación del plano $\alpha$:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-plano" style="width: 100%; height: 240px; min-height: 200px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-plano')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-plano', {
      boundingbox: [-1, 5, 12, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Plano como paralelogramo
    var p1 = board.create('point', [1, 1], {visible: false, fixed: true});
    var p2 = board.create('point', [3, 3.5], {visible: false, fixed: true});
    var p3 = board.create('point', [10, 3.5], {visible: false, fixed: true});
    var p4 = board.create('point', [8, 1], {visible: false, fixed: true});
    
    board.create('polygon', [p1, p2, p3, p4], {
      fillColor: '#dbeafe',
      fillOpacity: 0.6,
      borders: {strokeColor: '#3b82f6', strokeWidth: 2}
    });
    
    // Letra griega alfa
    board.create('text', [5.5, 2.3, 'α'], {fontSize: 28, fontStyle: 'italic', color: '#3b82f6', anchorX: 'middle'});
    
    board.create('text', [5.5, 0.3, 'Se extiende infinitamente en todas direcciones'], {fontSize: 11, color: '#64748b', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

### Ejemplos de planos en la vida real

| Objeto | ¿Por qué representa un plano? |
|--------|------------------------------|
| La superficie de una mesa lisa | Si la extendemos infinitamente |
| Una pared completamente lisa | Superficie en dos dimensiones |
| La superficie del agua en calma | Perfectamente horizontal |
| Una hoja de papel infinita | Sin grosor, solo largo y ancho |

### Ejemplo 1

La superficie de un lago en calma perfecta. Si imaginamos que esa superficie se extiende hasta el infinito en todas direcciones, representa un plano.

### Ejemplo 2

Una pizarra o tablero. La superficie donde escribimos representa un plano, aunque en la realidad tiene límites (bordes).

---

## 📖 Axioma Fundamental

Existe un principio básico que relaciona estos tres elementos:

$$
\text{Por dos puntos distintos pasa una única recta}
$$

Este es el **primer postulado de Euclides** y es fundamental en geometría.

### Ejemplo

Si tienes dos clavos en una pared (puntos $A$ y $B$), solo puedes tensar una cuerda (recta) de una única manera entre ellos.

**Por dos puntos $A$ y $B$ pasa una única recta $l$:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-axioma" style="width: 100%; height: 280px; min-height: 250px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-axioma')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-axioma', {
      boundingbox: [-1, 5, 12, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Puntos A y B
    var pA = board.create('point', [2, 2.5], {name: 'A', size: 6, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [-15, 10]}});
    var pB = board.create('point', [9, 2.5], {name: 'B', size: 6, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [10, 10]}});
    
    // Única recta que pasa por A y B
    board.create('line', [pA, pB], {strokeColor: '#22c55e', strokeWidth: 3});
    
    // Etiqueta de la recta
    board.create('text', [10.5, 3, 'l'], {fontSize: 14, fontStyle: 'italic', color: '#22c55e'});
    
    board.create('text', [5.5, 0.8, '¡Solo existe UNA recta que pasa por ambos puntos!'], {fontSize: 11, color: '#64748b', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Tabla Resumen

| Elemento | Dimensiones | Notación | Representación |
|----------|-------------|----------|----------------|
| Punto | 0 (sin dimensión) | $A$, $B$, $P$ | Pequeño círculo |
| Recta | 1 (longitud infinita) | $l$, $\overleftrightarrow{AB}$ | Línea con flechas |
| Plano | 2 (largo y ancho infinitos) | $\alpha$, $\pi$ | Paralelogramo |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificación

Para cada objeto, indica si representa mejor un **punto**, una **recta** o un **plano**:

| Objeto | ¿Punto, Recta o Plano? |
|--------|------------------------|
| Un grano de arena visto desde lejos | |
| El filo de un cuchillo (extendido infinitamente) | |
| La superficie del escritorio | |
| La esquina de una caja | |
| El cable del tendedero (extendido) | |
| El techo de una habitación | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Objeto | Respuesta |
|--------|-----------|
| Un grano de arena visto desde lejos | Punto |
| El filo de un cuchillo (extendido) | Recta |
| La superficie del escritorio | Plano |
| La esquina de una caja | Punto |
| El cable del tendedero (extendido) | Recta |
| El techo de una habitación | Plano |

</details>

---

### Ejercicio 2: Notación correcta

Escribe la notación correcta para cada caso:

1. Un punto ubicado en la esquina de un triángulo, llamado "A": ______
2. Una recta que pasa por los puntos M y N: ______
3. Un plano identificado con la letra griega alfa: ______

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A$
2. $\overleftrightarrow{MN}$
3. $\alpha$

</details>

---

### Ejercicio 3: Axioma fundamental

Si tenemos tres puntos $A$, $B$ y $C$ que no están en la misma recta, ¿cuántas rectas diferentes podemos trazar usando pares de estos puntos?

<details>
<summary><strong>Ver respuesta</strong></summary>

Podemos trazar **3 rectas diferentes**:
- $\overleftrightarrow{AB}$
- $\overleftrightarrow{AC}$
- $\overleftrightarrow{BC}$

Esto se debe a que por cada par de puntos pasa una única recta.

</details>

---
