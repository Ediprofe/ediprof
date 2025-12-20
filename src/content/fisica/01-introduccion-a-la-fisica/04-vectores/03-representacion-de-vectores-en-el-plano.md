# Representación de vectores en el plano

Los vectores pueden representarse **gráficamente** en un **plano cartesiano**, lo que permite visualizar su magnitud, dirección y sentido de manera precisa.

Un vector en el plano se puede ubicar a partir de dos puntos:

* **Punto de origen (cola):** donde empieza el vector.
* **Punta o extremo (cabeza):** hacia donde apunta.

Por ejemplo, si un vector $\vec{A}$ parte del punto $O(0,0)$ y llega hasta el punto $P(4,3)$, puede representarse así:

$$
\vec{A} = \overrightarrow{OP}
$$

Esto significa que el vector va desde el origen hasta el punto $(4,3)$.

---

## 1. Representación gráfica

En el plano cartesiano, el vector $\vec{A}$ se dibuja como una **flecha** desde $(0,0)$ hasta $(4,3)$:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-plano" class="jsxgraph-container" style="width: 100%; height: 380px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var isDark = document.documentElement.classList.contains('dark');
    var axisColor = isDark ? '#94a3b8' : '#888888';
    
    var board = JXG.JSXGraph.initBoard('jsxgraph-plano', {
      boundingbox: [-1, 7, 8, -1.5],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false },
      defaultAxes: {
        x: {strokeColor: axisColor, ticks: {strokeColor: axisColor}},
        y: {strokeColor: axisColor, ticks: {strokeColor: axisColor}}
      }
    });
    
    // Punto origen (fijo)
    var O = board.create('point', [0, 0], {name: 'O', size: 4, fixed: true, color: '#64748b', label: {offset: [-15, -15]}});
    
    // Punto final del vector (ARRASTRABLE - esto SÍ aporta)
    var P = board.create('point', [4, 3], {name: 'P', size: 4, color: '#3b82f6', label: {offset: [8, 8]}});
    
    // Vector A
    var vecA = board.create('arrow', [O, P], {strokeColor: '#3b82f6', strokeWidth: 3});
    
    // Etiqueta A - posición dinámica ARRIBA del vector
    board.create('text', [function() { return P.X()/2 - 0.5; }, function() { return P.Y()/2 + 0.8; }, 'A'], 
      {fontSize: 18, color: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Proyección sobre eje X (componente Ax)
    var projX = board.create('point', [function() { return P.X(); }, 0], {visible: false, fixed: true});
    board.create('segment', [P, projX], {strokeColor: '#ef4444', strokeWidth: 2, dash: 2});
    
    // Proyección sobre eje Y (componente Ay)  
    var projY = board.create('point', [0, function() { return P.Y(); }], {visible: false, fixed: true});
    board.create('segment', [P, projY], {strokeColor: '#22c55e', strokeWidth: 2, dash: 2});
    
    // Etiquetas de componentes - posiciones que no se superponen
    board.create('text', [function() { return P.X()/2; }, -0.8, function() { return 'Ax = ' + P.X().toFixed(1); }], 
      {fontSize: 12, color: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [-0.9, function() { return P.Y()/2; }, function() { return 'Ay = ' + P.Y().toFixed(1); }], 
      {fontSize: 12, color: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Ángulo
    board.create('angle', [projX, O, P], {
      radius: 0.7,
      name: 'θ',
      color: '#8b5cf6',
      fillColor: 'rgba(139, 92, 246, 0.2)'
    });
    
    // Magnitud (mostrar cálculo) - arriba a la derecha
    board.create('text', [5.5, 6, function() { 
      var mag = Math.sqrt(P.X()*P.X() + P.Y()*P.Y());
      return '|A| = ' + mag.toFixed(2); 
    }], {fontSize: 13, color: '#3b82f6', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Etiquetas de ejes
    board.create('text', [7.5, -0.5, 'x'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    board.create('text', [-0.5, 6.5, 'y'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    
    board.unsuspendUpdate();
  }
});
</script>

> 💡 **¡Interactivo!** Arrastra el punto **P** para ver cómo cambian las componentes $A_x$ (rojo) y $A_y$ (verde), así como la magnitud del vector.

* La **longitud de la flecha** representa la **magnitud**.
* La **inclinación** con respecto al eje $x$ muestra la **dirección**.
* La **punta** indica el **sentido**.

La magnitud del vector se calcula con el **teorema de Pitágoras**:

$$
|\vec{A}| = \sqrt{A_x^2 + A_y^2}
$$

donde $A_x$ y $A_y$ son las **componentes** del vector en los ejes $x$ y $y$.

---

## 2. Componentes de un vector

Todo vector en el plano puede descomponerse en dos **componentes perpendiculares**:

$$
\vec{A} = A_x\,\hat{i} + A_y\,\hat{j}
$$

donde:

* $A_x$ es la **proyección del vector sobre el eje $x$**,
* $A_y$ es la **proyección del vector sobre el eje $y$**,
* $\hat{i}$ y $\hat{j}$ son los **vectores unitarios** en las direcciones de los ejes $x$ y $y$ respectivamente.

Si el vector forma un ángulo $\theta$ con el eje $x$, entonces:

$$
A_x = |\vec{A}|\cos{\theta}
$$

$$
A_y = |\vec{A}|\sin{\theta}
$$

---

## 3. Ejemplo

Un vector $\vec{B}$ tiene una magnitud de $10\,\mathrm{m}$ y forma un ángulo de $37^\circ$ con el eje $x$.
Sus componentes son:

$$
B_x = 10\cos{37^\circ} = 8\,\mathrm{m}
$$

$$
B_y = 10\sin{37^\circ} = 6\,\mathrm{m}
$$

Por lo tanto:

$$
\vec{B} = 8\,\hat{i} + 6\,\hat{j}
$$

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div id="jsxgraph-ejemplo" class="jsxgraph-container" style="width: 100%; height: 350px; border-radius: 8px; overflow: hidden;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof JXG !== 'undefined') {
    var isDark = document.documentElement.classList.contains('dark');
    var axisColor = isDark ? '#94a3b8' : '#888888';
    
    var board2 = JXG.JSXGraph.initBoard('jsxgraph-ejemplo', {
      boundingbox: [-1, 8, 10, -1.5],
      axis: true,
      showCopyright: false,
      showNavigation: false,
      pan: { enabled: false },
      zoom: { enabled: false },
      defaultAxes: {
        x: {strokeColor: axisColor},
        y: {strokeColor: axisColor}
      }
    });
    
    // Punto origen (fijo)
    var O = board2.create('point', [0, 0], {name: 'O', size: 3, fixed: true, color: '#64748b', label: {offset: [-12, -12]}});
    
    // Vector B (8, 6) - punto FIJO, no interactivo
    var B = board2.create('point', [8, 6], {name: '', size: 3, fixed: true, color: '#3b82f6'});
    board2.create('arrow', [O, B], {strokeColor: '#3b82f6', strokeWidth: 3, fixed: true});
    
    // Etiqueta B - ARRIBA del vector para no superponerse
    board2.create('text', [3.2, 4.2, 'B = 10 m'], {fontSize: 13, color: '#3b82f6', cssStyle: 'font-weight: bold; font-style: italic;', fixed: true});
    
    // Componente X - flecha roja
    var Bx = board2.create('point', [8, 0], {visible: false, fixed: true});
    board2.create('arrow', [O, Bx], {strokeColor: '#ef4444', strokeWidth: 2, fixed: true});
    board2.create('text', [4, -0.8, 'Bx = 8 m'], {fontSize: 12, color: '#ef4444', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Componente Y - flecha verde (desde Bx hacia B)
    board2.create('arrow', [Bx, B], {strokeColor: '#22c55e', strokeWidth: 2, fixed: true});
    board2.create('text', [8.5, 3, 'By = 6 m'], {fontSize: 12, color: '#22c55e', cssStyle: 'font-weight: bold;', fixed: true});
    
    // Ángulo de 37°
    board2.create('angle', [Bx, O, B], {
      radius: 1.2,
      name: '37°',
      color: '#8b5cf6',
      fillColor: 'rgba(139, 92, 246, 0.2)',
      fixed: true
    });
    
    // Etiquetas de ejes
    board2.create('text', [9.5, -0.5, 'x'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    board2.create('text', [-0.5, 7.5, 'y'], {fontSize: 14, strokeColor: '#374151', cssStyle: 'font-weight: bold;', fixed: true});
    
    board2.unsuspendUpdate();
  }
});
</script>

Este vector puede representarse gráficamente con una flecha que parte del origen $(0,0)$ y llega al punto $(8,6)$.

---

## 4. Observaciones importantes

* Un vector **puede trasladarse** paralelamente sin cambiar su valor (solo importa su magnitud, dirección y sentido).
* Los vectores se **suman o restan** gráficamente utilizando sus componentes o con métodos geométricos (esto se estudiará en la siguiente sección).
* El sistema cartesiano facilita comparar, sumar y proyectar vectores con precisión.

---

> 📘 **En resumen:**
> En el plano, un vector se describe mediante sus componentes $(A_x, A_y)$ o mediante su magnitud y ángulo $(|\vec{A}|, \theta)$.
> Ambas formas representan la misma información: *cuánto mide, hacia dónde apunta y en qué dirección actúa*.
