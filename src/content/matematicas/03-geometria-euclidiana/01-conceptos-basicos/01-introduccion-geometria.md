# Introducción a la Geometría

La geometría está presente en todo lo que nos rodea: en las formas de los edificios, en el diseño de los muebles, en los campos deportivos y hasta en la naturaleza. En esta lección descubriremos qué es la geometría y por qué es tan importante.

---

## 📖 ¿Qué es la geometría?

La palabra **geometría** viene del griego:
- **Geo** = tierra
- **Metría** = medida

Literalmente significa **"medir la tierra"**. Los antiguos egipcios la usaban para medir terrenos después de las inundaciones del río Nilo.

> **Definición:** La geometría es la rama de las matemáticas que estudia las **formas**, los **tamaños**, las **posiciones** y las **propiedades** de las figuras en el espacio.

---

## 📖 ¿Para qué sirve la geometría?

La geometría tiene aplicaciones en la vida cotidiana y en muchas profesiones. Veamos algunos ejemplos:

### Ejemplo 1: Arquitectura y construcción

Un arquitecto necesita geometría para diseñar casas con paredes rectas, ángulos precisos y espacios bien distribuidos. Sin geometría, las construcciones se caerían.

### Ejemplo 2: Carpintería

Un carpintero usa geometría para cortar madera en las medidas exactas, crear muebles con ángulos perfectos y asegurarse de que las piezas encajen correctamente.

### Ejemplo 3: Deportes

Las canchas de fútbol, las piscinas olímpicas y las pistas de atletismo tienen medidas geométricas precisas. ¡Incluso el balón de fútbol es un poliedro llamado icosaedro truncado!

### Ejemplo 4: Navegación

Los pilotos y capitanes de barcos usan geometría para trazar rutas, calcular distancias y encontrar la ruta más corta entre dos puntos.

### Ejemplo 5: Arte y diseño

Artistas y diseñadores gráficos usan proporciones, simetrías y formas geométricas para crear obras visualmente atractivas.

---

## 📖 Breve historia de la geometría

### Los egipcios (hace 4000 años)

Los agrimensores egipcios medían terrenos usando cuerdas y estacas. Después de cada inundación del Nilo, debían redibujar los límites de las tierras de cultivo.

### Los griegos (hace 2500 años)

Los griegos transformaron estas técnicas prácticas en una ciencia formal. El matemático más importante fue **Euclides**, quien escribió "Los Elementos", un libro que organizó todo el conocimiento geométrico de su época.

> **Dato:** La geometría que estudiaremos se llama **Geometría Euclidiana** en honor a Euclides.

### Euclides y sus postulados

Euclides estableció 5 principios básicos (postulados) que son el fundamento de toda la geometría:

1. Por dos puntos pasa una única recta
2. Un segmento puede extenderse indefinidamente
3. Se puede trazar una circunferencia con cualquier centro y radio
4. Todos los ángulos rectos son iguales
5. Por un punto exterior a una recta pasa una única recta paralela

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-postulado1" style="width: 100%; height: 300px; min-height: 250px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-postulado1')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-postulado1', {
      boundingbox: [-1, 6, 12, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // Título
    board.create('text', [5.5, 5.2, 'Primer Postulado de Euclides'], {fontSize: 14, fontWeight: 'bold', color: '#1e293b', anchorX: 'middle'});
    board.create('text', [5.5, 4.5, '"Por dos puntos pasa una única recta"'], {fontSize: 12, fontStyle: 'italic', color: '#64748b', anchorX: 'middle'});
    
    // Puntos A y B
    var pA = board.create('point', [2, 2], {name: 'A', size: 5, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [-15, 10]}});
    var pB = board.create('point', [9, 2], {name: 'B', size: 5, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [10, 10]}});
    
    // Única recta que pasa por A y B
    board.create('line', [pA, pB], {strokeColor: '#22c55e', strokeWidth: 3});
    
    // Etiqueta de la recta
    board.create('text', [10.5, 2.8, 'l'], {fontSize: 14, fontStyle: 'italic', color: '#22c55e'});
    
    // Nota explicativa
    board.create('text', [5.5, 0.3, '¡Solo existe una recta que pasa por ambos puntos!'], {fontSize: 11, color: '#475569', anchorX: 'middle'});
    
    board.unsuspendUpdate();
  }
});
</script>

---

## 📖 Los elementos fundamentales de la geometría

Antes de estudiar figuras complejas, necesitamos conocer los **tres elementos básicos** que son la base de toda la geometría:

| Elemento | Símbolo | Característica principal |
|----------|---------|-------------------------|
| Punto | $A$, $B$, $P$ | No tiene dimensiones (ni largo, ni ancho, ni alto) |
| Recta | $l$, $\overleftrightarrow{AB}$ | Tiene solo longitud (infinita en ambas direcciones) |
| Plano | $\pi$, $\alpha$ | Tiene largo y ancho (infinito en todas direcciones) |

Estos elementos se llaman **conceptos primitivos** porque no se pueden definir con otros más simples, solo se pueden describir.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-elementos-fundamentales" style="width: 100%; height: 350px; min-height: 300px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-elementos-fundamentales')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-elementos-fundamentales', {
      boundingbox: [-1, 8, 14, -1],
      axis: false,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false }
    });
    
    // PUNTO
    board.create('text', [1.5, 7, 'PUNTO'], {fontSize: 14, fontWeight: 'bold', color: '#1e293b'});
    board.create('point', [1.5, 5.5], {name: 'A', size: 5, fixed: true, color: '#3b82f6', label: {fontSize: 14, color: '#3b82f6', offset: [10, 5]}});
    board.create('text', [1.5, 4, 'Sin dimensiones'], {fontSize: 11, color: '#64748b', anchorX: 'middle'});
    board.create('text', [1.5, 3.3, '(solo posición)'], {fontSize: 10, color: '#94a3b8', anchorX: 'middle'});
    
    // RECTA
    board.create('text', [7, 7, 'RECTA'], {fontSize: 14, fontWeight: 'bold', color: '#1e293b'});
    var p1 = board.create('point', [5, 5.5], {visible: false, fixed: true});
    var p2 = board.create('point', [9, 5.5], {visible: false, fixed: true});
    board.create('line', [p1, p2], {strokeColor: '#22c55e', strokeWidth: 3, straightFirst: true, straightLast: true});
    board.create('text', [7, 7.3, 'l'], {fontSize: 14, fontStyle: 'italic', color: '#22c55e', anchorX: 'middle'});
    board.create('text', [7, 4, '1 dimensión'], {fontSize: 11, color: '#64748b', anchorX: 'middle'});
    board.create('text', [7, 3.3, '(longitud infinita)'], {fontSize: 10, color: '#94a3b8', anchorX: 'middle'});
    
    // PLANO
    board.create('text', [12, 7, 'PLANO'], {fontSize: 14, fontWeight: 'bold', color: '#1e293b'});
    var planoPoints = [[10, 4.5], [11.5, 6], [14, 6], [12.5, 4.5]];
    board.create('polygon', planoPoints.map(function(p) { return board.create('point', p, {visible: false, fixed: true}); }), {
      fillColor: '#fef3c7', 
      fillOpacity: 0.6, 
      borders: {strokeColor: '#f59e0b', strokeWidth: 2}
    });
    board.create('text', [12.2, 5.2, 'α'], {fontSize: 16, fontStyle: 'italic', color: '#f59e0b'});
    board.create('text', [12, 3.3, '2 dimensiones'], {fontSize: 11, color: '#64748b', anchorX: 'middle'});
    board.create('text', [12, 2.6, '(largo y ancho)'], {fontSize: 10, color: '#94a3b8', anchorX: 'middle'});
    
    // Leyenda inferior
    board.create('text', [7, 1, 'Los tres elementos fundamentales de la geometría'], {fontSize: 12, color: '#475569', anchorX: 'middle', fontWeight: 'bold'});
    
    board.unsuspendUpdate();
  }
});
</script>

> En las próximas lecciones estudiaremos cada uno de estos elementos en detalle.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Aplicaciones de la geometría

Observa tu entorno (tu casa, tu colegio, la calle) y escribe **5 ejemplos** donde se aplique la geometría. Para cada uno, indica qué forma geométrica identificas.

**Ejemplo de respuesta:**
- La pantalla del celular tiene forma de rectángulo
- Las ruedas del carro son circunferencias

---

### Ejercicio 2: Elementos fundamentales

Relaciona cada objeto con el elemento geométrico que mejor lo representa:

| Objeto | ¿Punto, Recta o Plano? |
|--------|------------------------|
| La punta de un alfiler | |
| El riel de un tren (imaginándolo infinito) | |
| La superficie de una mesa (imaginándola infinita) | |
| Una estrella lejana en el cielo | |
| Un rayo de luz láser | |

<details>
<summary><strong>Ver respuestas</strong></summary>

| Objeto | Respuesta |
|--------|-----------|
| La punta de un alfiler | Punto |
| El riel de un tren | Recta |
| La superficie de una mesa | Plano |
| Una estrella lejana en el cielo | Punto |
| Un rayo de luz láser | Recta |

</details>

---
