# 🚀 **Movimiento Rectilíneo Uniformemente Acelerado (MRUA)**

Hasta ahora habíamos estudiado movimientos donde la velocidad nunca cambiaba (MRU). Pero en la vida real, lo más común es que los objetos arranquen, frenen o aumenten su rapidez.

El **MRUA** es aquel movimiento en línea recta donde la **velocidad cambia** de manera uniforme.

La clave para entender este movimiento es una nueva magnitud física: la **Aceleración ($a$)**.

---

## ⚡ **El Concepto de Aceleración**

La **Aceleración** nos dice **qué tan rápido cambia la velocidad** de un objeto.

* Si la velocidad se mantiene igual, la aceleración es **cero** ($a=0$).
* Si la velocidad aumenta o disminuye, existe una **aceleración** ($a \neq 0$).

### **¿Qué significa la unidad m/s²?**

La unidad de medida es **metros por segundo al cuadrado**. Aunque suena complejo, su significado es muy lógico si lo leemos así: **"Metros por segundo, cada segundo"**.

$$
a = \frac{\Delta v}{t} = \frac{\mathrm{m/s}}{\mathrm{s}} = \mathrm{m/s^2}
$$

> **La Regla de Oro:**
> Si un objeto tiene una aceleración de **$2\,\mathrm{m/s^2}$**, significa que su velocidad **aumenta en $2\,\mathrm{m/s}$ por cada segundo que pasa.**

---

## ✨ **Características del MRUA**

1.  **Trayectoria Rectilínea:** El objeto se mueve siempre en línea recta.
2.  **Velocidad Variable:** La velocidad no es fija; cambia instante a instante.
3.  **Aceleración Constante:** El ritmo al que cambia la velocidad es siempre el mismo (no cambia de golpe).

---

## ⚙️ **Ejercicio 1 — El Arranque de una Moto**

Una motocicleta está detenida frente a un semáforo en rojo. Cuando cambia a verde, el conductor acelera con $a = 5\,\mathrm{m/s^2}$ durante 4 segundos.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-moto" class="jsxgraph-container" style="width: 100%; height: 200px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-moto')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-moto', {
      boundingbox: [-0.8, 25, 5.5, -4], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Ejes manuales
    board.create('axis', [[0, 0], [1, 0]], {ticks: {insertTicks: false, ticksDistance: 1, label: {offset: [0, -12]}}});
    board.create('axis', [[0, 0], [0, 1]], {ticks: {insertTicks: false, ticksDistance: 5, label: {offset: [-15, 0]}}});
    board.create('text', [5.2, -1.5, 't (s)'], {fontSize: 12, strokeColor: '#374151', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.6, 23, 'v (m/s)'], {fontSize: 12, strokeColor: '#374151', fixed: true, cssStyle: 'font-weight: bold;'});
    // Línea principal
    board.create('segment', [[0, 0], [4, 20]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    // Puntos con etiquetas de velocidad
    board.create('point', [0, 0], {size: 5, fixed: true, color: '#22c55e', name: '0', label: {offset: [-15, -5], strokeColor: '#22c55e', fontSize: 11}});
    board.create('point', [1, 5], {size: 5, fixed: true, color: '#3b82f6', name: '', withLabel: false});
    board.create('point', [2, 10], {size: 5, fixed: true, color: '#3b82f6', name: '', withLabel: false});
    board.create('point', [3, 15], {size: 5, fixed: true, color: '#3b82f6', name: '', withLabel: false});
    board.create('point', [4, 20], {size: 5, fixed: true, color: '#ef4444', name: '20 m/s', label: {offset: [8, 5], strokeColor: '#ef4444', fontSize: 12, cssStyle: 'font-weight: bold;'}});
    // Etiqueta de aceleración
    board.create('text', [2.5, 6, 'a = 5 m/s²'], {fontSize: 13, strokeColor: '#f59e0b', fixed: true, cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 El gráfico muestra cómo la velocidad aumenta **+5 m/s cada segundo** (pendiente constante = aceleración constante).

### **✅ Análisis**

$a = 5\,\mathrm{m/s^2}$ significa: **"Cada segundo, la moto suma 5 m/s a su velocidad"**.

| Tiempo | Operación | Velocidad |
|--------|-----------|-----------|
| $0\,\mathrm{s}$ | — | $0\,\mathrm{m/s}$ |
| $1\,\mathrm{s}$ | $0 + 5$ | $5\,\mathrm{m/s}$ |
| $2\,\mathrm{s}$ | $5 + 5$ | $10\,\mathrm{m/s}$ |
| $3\,\mathrm{s}$ | $10 + 5$ | $15\,\mathrm{m/s}$ |
| $4\,\mathrm{s}$ | $15 + 5$ | $\boxed{20\,\mathrm{m/s}}$ |

---

## ⚙️ **Ejercicio 2 — Caída Libre (La Gravedad)**

Un estudiante deja caer una piedra desde la azotea de un edificio alto. La **Caída Libre** es MRUA donde la aceleración es la **Gravedad**: $g = 9.8\,\mathrm{m/s^2}$.

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-caida" class="jsxgraph-container" style="width: 100%; height: 220px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined' && document.getElementById('jsxgraph-caida')) {
    var board = JXG.JSXGraph.initBoard('jsxgraph-caida', {
      boundingbox: [-0.8, 35, 4.8, -5], axis: false, showCopyright: false, showNavigation: false, pan: {enabled: false}, zoom: {enabled: false}
    });
    // Ejes manuales
    board.create('axis', [[0, 0], [1, 0]], {ticks: {insertTicks: false, ticksDistance: 1, label: {offset: [0, -12]}}});
    board.create('axis', [[0, 0], [0, 1]], {ticks: {insertTicks: false, ticksDistance: 10, label: {offset: [-15, 0]}}});
    board.create('text', [4.5, -2, 't (s)'], {fontSize: 12, strokeColor: '#374151', fixed: true, cssStyle: 'font-weight: bold;'});
    board.create('text', [-0.6, 32, 'v (m/s)'], {fontSize: 12, strokeColor: '#374151', fixed: true, cssStyle: 'font-weight: bold;'});
    // Línea principal
    board.create('segment', [[0, 0], [3, 29.4]], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    // Puntos con etiquetas de velocidad
    board.create('point', [0, 0], {size: 5, fixed: true, color: '#22c55e', name: '0', label: {offset: [-15, -5], strokeColor: '#22c55e', fontSize: 11}});
    board.create('point', [1, 9.8], {size: 5, fixed: true, color: '#3b82f6', name: '', withLabel: false});
    board.create('point', [2, 19.6], {size: 5, fixed: true, color: '#3b82f6', name: '', withLabel: false});
    board.create('point', [3, 29.4], {size: 5, fixed: true, color: '#ef4444', name: '29.4 m/s', label: {offset: [8, 5], strokeColor: '#ef4444', fontSize: 12, cssStyle: 'font-weight: bold;'}});
    // Etiqueta de aceleración (gravedad)
    board.create('text', [1.8, 8, 'g = 9.8 m/s²'], {fontSize: 13, strokeColor: '#f59e0b', fixed: true, cssStyle: 'font-weight: bold;'});
    board.unsuspendUpdate();
  }
});
</script>

> 💡 La gravedad actúa como una "tasa de recarga" constante de velocidad: **+9.8 m/s cada segundo**.

### **✅ Análisis**

$g = 9.8\,\mathrm{m/s^2}$ significa: **"Cada segundo, la piedra suma 9.8 m/s a su velocidad"**.

| Tiempo | Operación | Velocidad |
|--------|-----------|-----------|
| $0\,\mathrm{s}$ | Se suelta | $0\,\mathrm{m/s}$ |
| $1\,\mathrm{s}$ | $0 + 9.8$ | $9.8\,\mathrm{m/s}$ |
| $2\,\mathrm{s}$ | $9.8 + 9.8$ | $19.6\,\mathrm{m/s}$ |
| $3\,\mathrm{s}$ | $19.6 + 9.8$ | $\boxed{29.4\,\mathrm{m/s}}$ |

> 💡 Sin usar fórmulas complejas, sabemos que a los 3 segundos la piedra viaja a 29.4 m/s. La caída libre es simplemente un MRUA donde la aceleración está definida por la naturaleza.