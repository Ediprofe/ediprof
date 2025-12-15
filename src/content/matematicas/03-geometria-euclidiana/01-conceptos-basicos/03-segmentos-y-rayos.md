# Segmentos y Rayos

Ahora que conocemos los conceptos de punto y recta, vamos a estudiar dos elementos que se derivan de ellos: el **segmento** y el **rayo**. Estos son fundamentales para medir distancias y construir figuras geométricas.

---

## 📖 El Segmento

### ¿Qué es un segmento?

Un **segmento** es la porción de una recta comprendida entre dos puntos llamados **extremos**.

> **Definición:** Un segmento es el conjunto de puntos de una recta que están entre dos puntos dados, incluyendo esos dos puntos extremos.

### Diferencia con la recta

| Característica | Recta | Segmento |
|---------------|-------|----------|
| Extensión | Infinita en ambas direcciones | Limitada entre dos puntos |
| Extremos | No tiene | Tiene dos extremos |
| Se puede medir | No (es infinita) | Sí, tiene longitud finita |

### Notación del segmento

Se nombra de varias formas:

- $\overline{AB}$ (con barra encima, se lee "segmento AB")
- Segmento $AB$

Los puntos $A$ y $B$ son los **extremos** del segmento.

### Ejemplos en la vida real

| Objeto | ¿Por qué es un segmento? |
|--------|-------------------------|
| Un lápiz | Tiene inicio y fin |
| El lado de una mesa | Longitud definida entre dos esquinas |
| Una cuerda entre dos postes | Extremo en cada poste |
| El borde de un libro | Limitado por las esquinas |

### Ejemplo 1

Un lápiz nuevo mide aproximadamente 19 cm. Podemos representarlo como un segmento con dos extremos: la punta y el borrador.

### Ejemplo 2

El larguero de una portería de fútbol es un segmento: tiene una longitud exacta (7.32 metros en canchas oficiales) con extremos en cada poste.

**Representación del segmento $\overline{AB}$:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-segmento" style="width: 100%; height: 280px; min-height: 250px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-segmento')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-segmento', {
      boundingbox: [-1, 5, 12, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Extremos del segmento
    var pA = board.create('point', [2, 2.5], {name: 'A', size: 6, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [-15, 10]}});
    var pB = board.create('point', [9, 2.5], {name: 'B', size: 6, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [10, 10]}});
    
    // Segmento (NO es recta infinita)
    board.create('segment', [pA, pB], {strokeColor: '#22c55e', strokeWidth: 4});
    
    board.create('text', [5.5, 0.8, 'Un segmento tiene DOS EXTREMOS (puntos A y B)'], {fontSize: 11, color: '#64748b', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Longitud de un Segmento

### ¿Qué es la longitud?

La **longitud** de un segmento es la distancia entre sus dos extremos. Es lo que medimos con una regla.

### Notación de la longitud

Se puede expresar de dos formas:

- $|\overline{AB}|$ (valor absoluto del segmento)
- Simplemente $AB$ (cuando es claro que hablamos de la medida)

### Ejemplo 1

Si el segmento $\overline{PQ}$ mide 5 cm, escribimos:

$$
|\overline{PQ}| = 5 \text{ cm} \quad \text{o simplemente} \quad PQ = 5 \text{ cm}
$$

### Ejemplo 2

Si la distancia entre las ciudades $A$ y $B$ es de 120 km (en línea recta), podemos escribir:

$$
AB = 120 \text{ km}
$$

---

## 📖 Punto Medio de un Segmento

### ¿Qué es el punto medio?

El **punto medio** de un segmento es el punto que lo divide en dos partes **iguales**.

> **Definición:** $M$ es punto medio de $\overline{AB}$ si y solo si $M$ está entre $A$ y $B$, y además $AM = MB$.

### Propiedades del punto medio

Si $M$ es el punto medio de $\overline{AB}$:

$$
AM = MB = \frac{AB}{2}
$$

### Ejemplo 1

Si un segmento $\overline{AB}$ mide 10 cm, y $M$ es su punto medio:

$$
AM = MB = \frac{10}{2} = 5 \text{ cm}
$$

### Ejemplo 2

Una cuerda de 8 metros está atada entre dos árboles. El punto medio de la cuerda está exactamente a 4 metros de cada árbol.

### Ejemplo 3

Encontrar el punto medio es útil para:
- Dividir un terreno en dos partes iguales
- Encontrar el centro de una pared para colgar un cuadro
- Doblar una hoja de papel exactamente a la mitad

**Punto medio $M$ del segmento $\overline{AB}$ donde $AM = MB$:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-puntomedio" style="width: 100%; height: 280px; min-height: 250px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-puntomedio')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-puntomedio', {
      boundingbox: [-1, 5, 12, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Extremos del segmento
    var pA = board.create('point', [1, 2.5], {name: 'A', size: 6, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [-15, 10]}});
    var pB = board.create('point', [10, 2.5], {name: 'B', size: 6, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [10, 10]}});
    
    // Punto medio M
    var pM = board.create('midpoint', [pA, pB], {name: 'M', size: 7, fixed: true, color: '#f59e0b', label: {fontSize: 14, color: '#f59e0b', offset: [0, 15]}});
    
    // Segmento completo
    board.create('segment', [pA, pB], {strokeColor: '#22c55e', strokeWidth: 3});
    
    board.create('text', [5.5, 0.8, 'El punto M divide al segmento en dos partes IGUALES'], {fontSize: 11, color: '#64748b', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 El Rayo (o Semirrecta)

### ¿Qué es un rayo?

Un **rayo** es una porción de recta que tiene un punto de inicio (llamado **origen**) y se extiende infinitamente en una sola dirección.

> **Definición:** Un rayo es el conjunto de puntos de una recta que comienza en un punto origen y se extiende indefinidamente en una dirección.

### Diferencia con recta y segmento

| Característica | Recta | Segmento | Rayo |
|---------------|-------|----------|------|
| Inicio | No tiene | Sí (extremo) | Sí (origen) |
| Fin | No tiene | Sí (extremo) | No tiene |
| Extensión | Infinita en ambos lados | Finita | Infinita en un lado |

### Notación del rayo

Se escribe: $\overrightarrow{AB}$

- El **primer punto** ($A$) es el **origen** (donde comienza)
- El **segundo punto** ($B$) indica la **dirección** hacia donde se extiende

> ⚠️ **Importante:** $\overrightarrow{AB}$ y $\overrightarrow{BA}$ son rayos **diferentes** porque tienen origen distinto.

### Ejemplos en la vida real

| Objeto | ¿Por qué es un rayo? |
|--------|---------------------|
| Un rayo de sol | Sale del sol y viaja "infinitamente" |
| La luz de una linterna | Origen en la linterna, se extiende lejos |
| Una flecha disparada | Origen en el arco, viaja en una dirección |
| Un láser apuntando | Origen en el dispositivo, se extiende |

### Ejemplo 1

Un rayo de luz láser que sale de un puntero. El origen es el puntero, y la luz viaja en línea recta hasta donde alcance (teóricamente, al infinito en el espacio).

### Ejemplo 2

Si estás parado en un punto $A$ mirando hacia un punto $B$, la dirección de tu mirada representa el rayo $\overrightarrow{AB}$.

**Representación del rayo $\overrightarrow{AB}$:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-rayo" style="width: 100%; height: 280px; min-height: 250px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-rayo')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-rayo', {
      boundingbox: [-1, 6, 12, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    board.create('text', [5.5, 5.2, 'El Rayo (Semirrecta)'], {fontSize: 14, fontWeight: 'bold', color: '#1e293b', anchorX: 'middle'});
    
    // Origen del rayo
    var pA = board.create('point', [2, 3], {name: 'A', size: 7, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [-15, 10]}});
    var pB = board.create('point', [6, 3], {name: 'B', size: 5, fixed: true, color: '#94a3b8', label: {fontSize: 14, color: '#94a3b8', offset: [0, 15]}});
    
    // Rayo (desde A, pasando por B, hacia el infinito)
    board.create('line', [pA, pB], {strokeColor: '#ef4444', strokeWidth: 3, straightFirst: false, straightLast: true});
    
    // Etiqueta del rayo
    board.create('text', [10.5, 3.5, '→ AB'], {fontSize: 12, color: '#ef4444'});
    
    // Flecha indicativa
    board.create('text', [11, 3, '→'], {fontSize: 20, color: '#ef4444'});
    
    // Punto de origen destacado
    board.create('text', [2, 1.8, 'ORIGEN'], {fontSize: 10, color: '#3b82f6', anchorX: 'middle'});
    
    board.create('text', [5.5, 1, 'Un rayo tiene UN ORIGEN y se extiende infinitamente en UNA dirección'], {fontSize: 11, color: '#64748b', anchorX: 'middle'});
    board.create('text', [5.5, 0.3, 'Notación: →AB (flecha sobre AB)'], {fontSize: 11, color: '#94a3b8', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

**Comparativa: Recta $\overleftrightarrow{AB}$ vs Segmento $\overline{AB}$ vs Rayo $\overrightarrow{AB}$:**

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-comparativa" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-comparativa')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-comparativa', {
      boundingbox: [-1, 7, 12, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // RECTA (arriba)
    board.create('text', [0.5, 5.5, 'RECTA'], {fontSize: 12, fontWeight: 'bold', color: '#22c55e'});
    var r1 = board.create('point', [2, 5.5], {visible: false, fixed: true});
    var r2 = board.create('point', [10, 5.5], {visible: false, fixed: true});
    board.create('line', [r1, r2], {strokeColor: '#22c55e', strokeWidth: 3});
    board.create('text', [1, 5.5, '←'], {fontSize: 16, color: '#22c55e'});
    board.create('text', [11, 5.5, '→'], {fontSize: 16, color: '#22c55e'});
    
    // SEGMENTO (medio)
    board.create('text', [0.2, 3.5, 'SEGMENTO'], {fontSize: 12, fontWeight: 'bold', color: '#3b82f6'});
    var s1 = board.create('point', [3, 3.5], {name: '', size: 5, fixed: true, color: '#3b82f6'});
    var s2 = board.create('point', [9, 3.5], {name: '', size: 5, fixed: true, color: '#3b82f6'});
    board.create('segment', [s1, s2], {strokeColor: '#3b82f6', strokeWidth: 3});
    board.create('text', [3, 2.7, 'A'], {fontSize: 11, color: '#3b82f6', anchorX: 'middle'});
    board.create('text', [9, 2.7, 'B'], {fontSize: 11, color: '#3b82f6', anchorX: 'middle'});
    
    // RAYO (abajo)
    board.create('text', [0.5, 1.5, 'RAYO'], {fontSize: 12, fontWeight: 'bold', color: '#ef4444'});
    var y1 = board.create('point', [3, 1.5], {name: '', size: 5, fixed: true, color: '#ef4444'});
    var y2 = board.create('point', [9, 1.5], {visible: false, fixed: true});
    board.create('line', [y1, y2], {strokeColor: '#ef4444', strokeWidth: 3, straightFirst: false, straightLast: true});
    board.create('text', [3, 0.7, 'A'], {fontSize: 11, color: '#ef4444', anchorX: 'middle'});
    board.create('text', [11, 1.5, '→'], {fontSize: 16, color: '#ef4444'});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Tabla Comparativa Final

| Elemento | Origen | Fin | Longitud | Notación | Representación |
|----------|--------|-----|----------|----------|----------------|
| Recta | No | No | Infinita | $\overleftrightarrow{AB}$, $l$ | ←————→ |
| Segmento | Sí | Sí | Finita | $\overline{AB}$ | ●————● |
| Rayo | Sí | No | Infinita en una dirección | $\overrightarrow{AB}$ | ●————→ |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificación

Clasifica cada objeto como **recta**, **segmento** o **rayo**:

| Objeto | Clasificación |
|--------|---------------|
| El borde de tu cuaderno | |
| Un rayo de luz del sol | |
| El horizonte (imaginado infinito) | |
| Una cuerda entre dos clavos | |
| La trayectoria de una bala disparada | |
| El riel del tren extendido infinitamente | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Objeto | Clasificación |
|--------|---------------|
| El borde de tu cuaderno | Segmento |
| Un rayo de luz del sol | Rayo |
| El horizonte (imaginado infinito) | Recta |
| Una cuerda entre dos clavos | Segmento |
| La trayectoria de una bala disparada | Rayo |
| El riel del tren extendido infinitamente | Recta |

</details>

---

### Ejercicio 2: Longitud y punto medio

El segmento $\overline{AB}$ mide 16 cm. Si $M$ es el punto medio:

1. ¿Cuánto mide $\overline{AM}$?
2. ¿Cuánto mide $\overline{MB}$?

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $AM = \frac{16}{2} = 8$ cm
2. $MB = \frac{16}{2} = 8$ cm

</details>

---

### Ejercicio 3: Notación de rayos

Dados los puntos $P$, $Q$ y $R$ en una recta (en ese orden), indica si las siguientes afirmaciones son verdaderas o falsas:

1. $\overrightarrow{PQ}$ y $\overrightarrow{PR}$ son el mismo rayo
2. $\overrightarrow{QP}$ y $\overrightarrow{QR}$ son el mismo rayo
3. $\overrightarrow{RP}$ y $\overrightarrow{RQ}$ son el mismo rayo

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero** - Ambos comienzan en $P$ y van en la misma dirección
2. **Falso** - Tienen el mismo origen ($Q$) pero van en direcciones opuestas
3. **Verdadero** - Ambos comienzan en $R$ y van hacia la izquierda (hacia $P$ y $Q$)

</details>

---

### Ejercicio 4: Problema aplicado

Un cable eléctrico une dos postes separados por 24 metros. Un electricista necesita instalar una caja de conexiones exactamente en el punto medio del cable.

1. ¿A qué distancia de cada poste debe instalar la caja?
2. Si ya instaló la caja y ahora debe poner otra a la mitad entre el primer poste y la caja, ¿a qué distancia del primer poste irá?

<details>
<summary><strong>Ver respuestas</strong></summary>

1. A $\frac{24}{2} = 12$ metros de cada poste
2. A $\frac{12}{2} = 6$ metros del primer poste

</details>

---
