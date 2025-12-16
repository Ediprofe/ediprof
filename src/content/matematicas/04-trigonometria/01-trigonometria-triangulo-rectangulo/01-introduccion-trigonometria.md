# Introducción a la Trigonometría

¿Te has preguntado cómo los arquitectos calculan la altura de un edificio sin subir a él? ¿O cómo los navegantes antiguos determinaban su posición en el océano mirando las estrellas? La respuesta está en una de las ramas más poderosas de las matemáticas: la **trigonometría**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la trigonometría y por qué es tan importante
- Los elementos del triángulo rectángulo
- La nomenclatura estándar (opuesto, adyacente, hipotenusa)
- Cómo identificar los lados respecto a un ángulo de referencia

---

## 📋 Lo Esencial

| Concepto | Descripción |
|----------|-------------|
| **Trigonometría** | Estudio de las relaciones entre lados y ángulos de triángulos |
| **Triángulo rectángulo** | Base de toda la trigonometría (tiene un ángulo de 90°) |
| **Hipotenusa** | El lado más largo, opuesto al ángulo recto |
| **Catetos** | Los dos lados que forman el ángulo recto |
| **Opuesto** | El cateto que está "enfrente" del ángulo de referencia |
| **Adyacente** | El cateto que "toca" el ángulo de referencia |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">El triángulo rectángulo y sus elementos</strong>
  </div>
  <div id="echarts-trig-intro-elementos" style="width: 100%; height: 400px; min-height: 350px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-trig-intro-elementos')) {
    var chart = echarts.init(document.getElementById('echarts-trig-intro-elementos'));
    
    var option = {
      animation: true,
      animationDuration: 1000,
      title: {
        text: 'Triángulo rectángulo con ángulo θ',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 14, fontWeight: 'bold', color: '#1e293b' }
      },
      grid: { left: '8%', right: '8%', top: '12%', bottom: '8%' },
      xAxis: { type: 'value', min: 0, max: 10, show: false },
      yAxis: { type: 'value', min: 0, max: 8, show: false },
      series: [
        // Triángulo
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#1e293b' },
          data: [[1, 1], [8, 1], [8, 6], [1, 1]]
        },
        // Marca de ángulo recto
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#64748b' },
          data: [[7.5, 1], [7.5, 1.5], [8, 1.5]]
        },
        // Arco para ángulo theta
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#3b82f6' },
          smooth: true,
          data: (function() {
            var arc = [];
            for (var i = 0; i <= 35; i++) {
              var angle = i * Math.PI / 180;
              arc.push([1 + 1.2*Math.cos(angle), 1 + 1.2*Math.sin(angle)]);
            }
            return arc;
          })()
        },
        // Vértices
        {
          type: 'scatter',
          symbolSize: 10,
          itemStyle: { color: '#1e293b' },
          data: [[1, 1], [8, 1], [8, 6]]
        }
      ],
      graphic: [
        // Etiquetas de vértices
        { type: 'text', left: '8%', top: '78%', style: { text: 'A', fontSize: 16, fontWeight: 'bold', fill: '#1e293b' } },
        { type: 'text', left: '78%', top: '78%', style: { text: 'B', fontSize: 16, fontWeight: 'bold', fill: '#1e293b' } },
        { type: 'text', left: '78%', top: '22%', style: { text: 'C', fontSize: 16, fontWeight: 'bold', fill: '#1e293b' } },
        // Etiqueta del ángulo
        { type: 'text', left: '16%', top: '68%', style: { text: 'θ', fontSize: 18, fontWeight: 'bold', fill: '#3b82f6' } },
        // Etiqueta ángulo recto
        { type: 'text', left: '73%', top: '68%', style: { text: '90°', fontSize: 12, fill: '#64748b' } },
        // Etiquetas de lados
        { type: 'text', left: '42%', top: '85%', style: { text: 'Adyacente (a)', fontSize: 13, fontWeight: 'bold', fill: '#22c55e' } },
        { type: 'text', left: '82%', top: '48%', style: { text: 'Opuesto (b)', fontSize: 13, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '35%', top: '42%', style: { text: 'Hipotenusa (c)', fontSize: 13, fontWeight: 'bold', fill: '#8b5cf6' } }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **Tip fundamental:** Respecto al ángulo θ: el lado **opuesto** está "enfrente" del ángulo, el **adyacente** "toca" el ángulo (sin ser la hipotenusa), y la **hipotenusa** siempre es el lado más largo.

---

## 📖 ¿Qué es la Trigonometría?

> **Definición:** La trigonometría es la rama de las matemáticas que estudia las **relaciones entre los lados y ángulos** de los triángulos.

El nombre viene del griego:
- *trigonon* = triángulo
- *metron* = medida

Es decir, literalmente significa "medición de triángulos".

---

## 📖 ¿Para qué sirve?

La trigonometría está en todas partes, aunque no la veas:

| Campo | Aplicación |
|-------|------------|
| 🏗️ **Arquitectura** | Calcular alturas, diseñar estructuras |
| 🚀 **Física** | Proyectiles, ondas, fuerzas |
| ✈️ **Navegación** | GPS, aviación, náutica |
| 🎮 **Videojuegos** | Gráficos 3D, movimiento de personajes |
| 🎵 **Música** | Ondas sonoras, síntesis de audio |
| 🏥 **Medicina** | Tomografías, ultrasonidos |
| 📡 **Telecomunicaciones** | Señales, antenas |

---

## 📖 El Triángulo Rectángulo

En este capítulo nos enfocaremos en el **triángulo rectángulo** porque es la base de toda la trigonometría.

### ¿Qué lo hace especial?

Un triángulo rectángulo tiene:
- **Un ángulo de 90°** (el ángulo recto)
- **Dos ángulos agudos** (menores a 90°) que suman exactamente 90°
- **Tres lados** con nombres específicos

### Los elementos

| Elemento | Descripción |
|----------|-------------|
| **Ángulo recto** | El ángulo de 90°, marcado con un cuadradito |
| **Catetos** | Los dos lados que forman el ángulo recto |
| **Hipotenusa** | El lado opuesto al ángulo recto (siempre el más largo) |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">Comparación: triángulo rectángulo con ángulos de 90°, 53° y 37°</strong>
  </div>
  <div id="echarts-trig-intro-pitagoras" style="width: 100%; height: 380px; min-height: 340px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-trig-intro-pitagoras')) {
    var chart = echarts.init(document.getElementById('echarts-trig-intro-pitagoras'));
    
    var option = {
      animation: true,
      title: {
        text: 'Triángulo 3-4-5 (triángulo pitagórico clásico)',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' }
      },
      grid: { left: '10%', right: '10%', top: '15%', bottom: '10%' },
      xAxis: { type: 'value', min: 0, max: 8, show: false },
      yAxis: { type: 'value', min: 0, max: 6, show: false },
      series: [
        // Triángulo 3-4-5
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#1e293b' },
          areaStyle: { color: 'rgba(59, 130, 246, 0.1)' },
          data: [[1, 1], [5, 1], [5, 4], [1, 1]]
        },
        // Marca de ángulo recto
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#64748b' },
          data: [[4.6, 1], [4.6, 1.4], [5, 1.4]]
        },
        // Vértices
        {
          type: 'scatter',
          symbolSize: 12,
          itemStyle: { color: '#3b82f6' },
          data: [[1, 1], [5, 1], [5, 4]]
        }
      ],
      graphic: [
        // Medidas de lados
        { type: 'text', left: '35%', top: '78%', style: { text: '4 (cateto)', fontSize: 14, fontWeight: 'bold', fill: '#22c55e' } },
        { type: 'text', left: '62%', top: '52%', style: { text: '3', fontSize: 14, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '60%', top: '48%', style: { text: '(cateto)', fontSize: 11, fill: '#ef4444' } },
        { type: 'text', left: '25%', top: '48%', style: { text: '5 (hipotenusa)', fontSize: 14, fontWeight: 'bold', fill: '#8b5cf6' } },
        // Ángulos
        { type: 'text', left: '17%', top: '68%', style: { text: '≈37°', fontSize: 12, fill: '#3b82f6' } },
        { type: 'text', left: '57%', top: '30%', style: { text: '≈53°', fontSize: 12, fill: '#3b82f6' } },
        { type: 'text', left: '56%', top: '68%', style: { text: '90°', fontSize: 11, fill: '#64748b' } },
        // Teorema de Pitágoras
        { type: 'text', left: '28%', top: '90%', style: { text: '3² + 4² = 9 + 16 = 25 = 5²  ✓', fontSize: 13, fontWeight: 'bold', fill: '#1e293b' } }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 📖 Lados Relativos al Ángulo de Referencia

Aquí viene lo más importante: **los nombres "opuesto" y "adyacente" dependen del ángulo que estemos considerando**.

### El ángulo de referencia

Cuando trabajamos con trigonometría, elegimos uno de los dos ángulos agudos como nuestro **ángulo de referencia** (lo llamamos θ, alpha, o simplemente "el ángulo").

### Los lados cambian según el ángulo

| Respecto al ángulo θ | Definición |
|---------------------|------------|
| **Opuesto** | El cateto que está "enfrente" del ángulo |
| **Adyacente** | El cateto que "toca" el ángulo (que no es la hipotenusa) |
| **Hipotenusa** | Siempre es el mismo: el lado más largo |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span> <strong style="color: #1e293b;">¡Los nombres cambian según el ángulo de referencia!</strong>
  </div>
  <div id="echarts-trig-intro-cambio" style="width: 100%; height: 450px; min-height: 400px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-trig-intro-cambio')) {
    var chart = echarts.init(document.getElementById('echarts-trig-intro-cambio'));
    
    var option = {
      animation: true,
      title: {
        text: 'Mismo triángulo, diferente ángulo de referencia',
        left: 'center',
        top: 5,
        textStyle: { fontSize: 13, fontWeight: 'bold', color: '#1e293b' }
      },
      grid: { left: '5%', right: '5%', top: '12%', bottom: '5%' },
      xAxis: { type: 'value', min: 0, max: 20, show: false },
      yAxis: { type: 'value', min: 0, max: 10, show: false },
      series: [
        // Triángulo izquierdo (respecto a θ)
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#1e293b' },
          areaStyle: { color: 'rgba(59, 130, 246, 0.1)' },
          data: [[1, 2], [6, 2], [6, 7], [1, 2]]
        },
        // Arco theta izquierdo
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#3b82f6' },
          smooth: true,
          data: (function() {
            var arc = [];
            for (var i = 0; i <= 45; i++) {
              var angle = i * Math.PI / 180;
              arc.push([1 + 0.8*Math.cos(angle), 2 + 0.8*Math.sin(angle)]);
            }
            return arc;
          })()
        },
        // Triángulo derecho (respecto a α)
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 3, color: '#1e293b' },
          areaStyle: { color: 'rgba(239, 68, 68, 0.1)' },
          data: [[11, 2], [16, 2], [16, 7], [11, 2]]
        },
        // Arco alpha derecho (en la esquina superior)
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#ef4444' },
          smooth: true,
          data: (function() {
            var arc = [];
            for (var i = 225; i <= 270; i++) {
              var angle = i * Math.PI / 180;
              arc.push([16 + 0.8*Math.cos(angle), 7 + 0.8*Math.sin(angle)]);
            }
            return arc;
          })()
        },
        // Marcas de ángulo recto
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#64748b' },
          data: [[5.6, 2], [5.6, 2.4], [6, 2.4]]
        },
        {
          type: 'line',
          symbol: 'none',
          lineStyle: { width: 2, color: '#64748b' },
          data: [[15.6, 2], [15.6, 2.4], [16, 2.4]]
        }
      ],
      graphic: [
        // IZQUIERDA - Respecto a θ
        { type: 'text', left: '16%', top: '20%', style: { text: 'Respecto a θ', fontSize: 14, fontWeight: 'bold', fill: '#3b82f6' } },
        { type: 'text', left: '8%', top: '62%', style: { text: 'θ', fontSize: 16, fontWeight: 'bold', fill: '#3b82f6' } },
        { type: 'text', left: '17%', top: '80%', style: { text: 'Adyacente', fontSize: 12, fontWeight: 'bold', fill: '#22c55e' } },
        { type: 'text', left: '32%', top: '50%', style: { text: 'Opuesto', fontSize: 12, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '10%', top: '38%', style: { text: 'Hipotenusa', fontSize: 12, fontWeight: 'bold', fill: '#8b5cf6' } },
        
        // DERECHA - Respecto a α
        { type: 'text', left: '66%', top: '20%', style: { text: 'Respecto a α', fontSize: 14, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '78%', top: '30%', style: { text: 'α', fontSize: 16, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '67%', top: '80%', style: { text: 'Opuesto', fontSize: 12, fontWeight: 'bold', fill: '#ef4444' } },
        { type: 'text', left: '82%', top: '50%', style: { text: 'Adyacente', fontSize: 12, fontWeight: 'bold', fill: '#22c55e' } },
        { type: 'text', left: '60%', top: '38%', style: { text: 'Hipotenusa', fontSize: 12, fontWeight: 'bold', fill: '#8b5cf6' } },
        
        // Nota
        { type: 'text', left: '22%', top: '93%', style: { text: '¡Los catetos intercambian nombres! La hipotenusa siempre es la misma.', fontSize: 12, fill: '#64748b' } }
      ]
    };
    
    chart.setOption(option);
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

> 💡 **Importante:** La **hipotenusa** nunca cambia de nombre porque siempre es el lado opuesto al ángulo de 90°. ¡Pero los catetos sí intercambian nombres dependiendo de qué ángulo estés mirando!

---

## 📖 Recuerdo: Teorema de Pitágoras

Antes de continuar con trigonometría, recuerda el teorema más famoso:

$$
a^2 + b^2 = c^2
$$

Donde:
- $a$ y $b$ son los catetos
- $c$ es la hipotenusa

### Ejemplo rápido

Si los catetos miden 3 y 4:

$$
c = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

---

## 🔑 Resumen

| Concepto | Punto clave |
|----------|-------------|
| **Trigonometría** | Estudia relaciones entre lados y ángulos |
| **Triángulo rectángulo** | Tiene un ángulo de 90° |
| **Hipotenusa** | Lado más largo, opuesto al ángulo recto |
| **Cateto opuesto** | Está "enfrente" del ángulo de referencia |
| **Cateto adyacente** | "Toca" el ángulo de referencia |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1: Identificar elementos

En un triángulo rectángulo con catetos 5 y 12:

1. ¿Cuánto mide la hipotenusa?
2. Si el ángulo θ está opuesto al cateto de 5, ¿cuál es el lado opuesto a θ?
3. ¿Cuál es el lado adyacente a θ?

<details>
<summary>Ver solución</summary>

1. $c = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13$
2. El lado **opuesto** es **5** (el cateto que está "enfrente" del ángulo)
3. El lado **adyacente** es **12** (el cateto que "toca" el ángulo)

</details>

---

### Ejercicio 2: Verdadero o Falso

1. La trigonometría solo se usa en matemáticas.
2. En un triángulo rectángulo, la hipotenusa es el lado más largo.
3. Los dos ángulos agudos de un triángulo rectángulo suman 90°.
4. El cateto adyacente es el que está "enfrente" del ángulo.
5. La hipotenusa cambia de nombre según el ángulo de referencia.

<details>
<summary>Ver solución</summary>

1. **Falso** - Se usa en física, ingeniería, navegación, videojuegos, medicina...
2. **Verdadero** - Siempre es el más largo
3. **Verdadero** - Porque el ángulo recto es 90° y el total es 180°
4. **Falso** - El adyacente es el que "toca" el ángulo
5. **Falso** - La hipotenusa siempre tiene el mismo nombre

</details>

---

### Ejercicio 3: Cambio de perspectiva

En un triángulo rectángulo con catetos 8 y 15, e hipotenusa 17:
- Si θ está opuesto al cateto de 8, identifica opuesto, adyacente e hipotenusa respecto a θ.
- Si α está opuesto al cateto de 15, identifica opuesto, adyacente e hipotenusa respecto a α.

<details>
<summary>Ver solución</summary>

**Respecto a θ:**
- Opuesto = 8
- Adyacente = 15
- Hipotenusa = 17

**Respecto a α:**
- Opuesto = 15
- Adyacente = 8
- Hipotenusa = 17

¡Observa cómo los catetos intercambian nombres!

</details>
