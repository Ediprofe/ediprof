# 📐 **Fórmulas del MRUA: De dónde salen y cómo usarlas**

En física, las fórmulas no son "magia"; son consecuencias lógicas de las definiciones básicas. A continuación, vamos a deducir las tres ecuaciones fundamentales del **Movimiento Rectilíneo Uniformemente Acelerado (MRUA)** paso a paso.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <canvas id="rough-mrua-intro" width="550" height="180" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  var canvas = document.getElementById('rough-mrua-intro');
  if (!canvas || typeof rough === 'undefined') return;
  
  var rc = rough.canvas(canvas);
  var ctx = canvas.getContext('2d');
  
  // Piso
  rc.line(20, 130, 530, 130, { stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
  
  // Auto inicial (pequeño)
  rc.rectangle(40, 100, 50, 25, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 0.8 });
  rc.circle(55, 128, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
  rc.circle(80, 128, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
  
  // Flechas de velocidad creciente
  rc.line(100, 105, 130, 105, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
  rc.line(125, 100, 130, 105, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
  rc.line(125, 110, 130, 105, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
  
  ctx.font = '10px Inter, sans-serif';
  ctx.fillStyle = '#16a34a';
  ctx.textAlign = 'left';
  ctx.fillText('v₁', 105, 98);
  
  // Auto medio
  rc.rectangle(180, 100, 50, 25, { fill: '#60a5fa', fillStyle: 'solid', stroke: '#2563eb', roughness: 0.8 });
  rc.circle(195, 128, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
  rc.circle(220, 128, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
  
  // Flecha más larga
  rc.line(240, 105, 290, 105, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
  rc.line(285, 100, 290, 105, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
  rc.line(285, 110, 290, 105, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.5 });
  
  ctx.fillText('v₂ > v₁', 250, 98);
  
  // Auto final
  rc.rectangle(340, 100, 50, 25, { fill: '#93c5fd', fillStyle: 'solid', stroke: '#3b82f6', roughness: 0.8 });
  rc.circle(355, 128, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
  rc.circle(380, 128, 12, { fill: '#1e293b', fillStyle: 'solid', roughness: 0.5 });
  
  // Flecha aún más larga
  rc.line(400, 105, 480, 105, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
  rc.line(475, 98, 480, 105, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
  rc.line(475, 112, 480, 105, { stroke: '#22c55e', strokeWidth: 3, roughness: 0.5 });
  
  ctx.fillText('v₃ > v₂', 430, 98);
  
  // Aceleración
  rc.rectangle(180, 20, 180, 50, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', strokeWidth: 2, roughness: 1 });
  
  ctx.font = 'bold 14px Inter, sans-serif';
  ctx.fillStyle = '#b45309';
  ctx.textAlign = 'center';
  ctx.fillText('MRUA: a = constante', 270, 42);
  ctx.font = '11px Inter, sans-serif';
  ctx.fillText('La velocidad cambia uniformemente', 270, 58);
  
  // Título
  ctx.font = 'bold 13px Inter, sans-serif';
  ctx.fillStyle = '#1e293b';
  ctx.fillText('Velocidad AUMENTA con el tiempo', 270, 160);
});
</script>

---

## 1️⃣ **Primera Ecuación: Calculando la Velocidad Final**

Esta fórmula nace directamente de la definición de **Aceleración**. Sabemos que la aceleración es el cambio de velocidad en el tiempo.

**Paso 1: Escribimos la definición**

$$
a = \frac{\text{Cambio de velocidad}}{\text{Tiempo}} = \frac{v_f - v_i}{t}
$$

**Paso 2: Despejamos la Velocidad Final ($v_f$)**

Pasamos el tiempo ($t$) a multiplicar al otro lado:

$$
a \cdot t = v_f - v_i
$$

Ahora pasamos la velocidad inicial ($v_i$) a sumar:

$$
v_i + a \cdot t = v_f
$$

**✅ FÓRMULA DE VELOCIDAD:**

$$
v_f = v_i + a \cdot t
$$

> **Uso:** Ideal cuando conoces el tiempo y la aceleración, y quieres saber qué tan rápido vas al final.

---

## 2️⃣ **Segunda Ecuación: Calculando la Posición**

Esta fórmula permite hallar dónde está el objeto en cualquier instante. Nace del concepto de **Velocidad Promedio**.

**Paso 1: Definimos el Desplazamiento usando el promedio**

Si la aceleración es constante, la velocidad promedio es justo la mitad entre la inicial y la final. El desplazamiento es esa velocidad promedio por el tiempo.

$$
\Delta x = \left( \frac{v_i + v_f}{2} \right) \cdot t
$$

**Paso 2: Sustitución**

En lugar de escribir $v_f$, insertamos la **Primera Ecuación** que acabamos de hallar ($v_i + a \cdot t$):

$$
\Delta x = \left( \frac{v_i + (v_i + a \cdot t)}{2} \right) \cdot t
$$

**Paso 3: Simplificación Algebraica**

Sumamos las velocidades iniciales ($2v_i$) y distribuimos el divisor 2:

$$
\Delta x = \left( v_i + \frac{1}{2}a \cdot t \right) \cdot t
$$

Multiplicamos todo por el tiempo ($t$) de afuera:

$$
\Delta x = v_i \cdot t + \frac{1}{2}a \cdot t^2
$$

**Paso 4: Posición Final**

Como $\Delta x = x_f - x_i$, despejamos $x_f$:

**✅ FÓRMULA DE POSICIÓN:**

$$
x_f = x_i + v_i \cdot t + \frac{1}{2}a \cdot t^2
$$

> **Uso:** La ecuación reina. Te dice dónde estás ($x_f$) en cualquier instante $t$.

---

## 3️⃣ **Tercera Ecuación: Eliminando el Tiempo**

A veces tenemos problemas donde conocemos las velocidades y distancias, pero **no sabemos el tiempo**. Para estos casos, fusionamos las ecuaciones anteriores para eliminar la variable $t$.

### **Paso 1: Recordamos las dos bases**

1.  **Desplazamiento por promedio:** $\Delta x = \left( \frac{v_f + v_i}{2} \right) \cdot t$
2.  **Definición de Aceleración:** $a = \frac{v_f - v_i}{t}$

### **Paso 2: Despejamos el Tiempo (t)**

De la ecuación de aceleración, despejamos $t$:

$$
t = \frac{v_f - v_i}{a}
$$

### **Paso 3: Sustitución**

Reemplazamos esta $t$ en la ecuación de desplazamiento:

$$
\Delta x = \left( \frac{v_f + v_i}{2} \right) \cdot \left( \frac{v_f - v_i}{a} \right)
$$

### **Paso 4: Diferencia de Cuadrados**

Multiplicamos las fracciones. En el numerador tenemos $(v_f + v_i)(v_f - v_i)$, lo cual es un producto notable (diferencia de cuadrados):

$$
\Delta x = \frac{v_f^2 - v_i^2}{2a}
$$

### **Paso 5: Despeje Final**

Pasamos $2a$ a multiplicar con el desplazamiento y despejamos $v_f^2$:

$$
2 \cdot a \cdot \Delta x = v_f^2 - v_i^2
$$

**✅ FÓRMULA SIN TIEMPO:**

$$
v_f^2 = v_i^2 + 2 \cdot a \cdot \Delta x
$$

> **Uso:** Fundamental cuando el problema **no menciona el tiempo**.

---

## 📝 **Resumen: Caja de Herramientas MRUA**

Usa esta tabla para saber qué fórmula elegir según los datos que tengas:

| **¿Qué quieres hallar?** | **¿Qué datos tienes?** | **Fórmula a usar** |
| :--- | :--- | :--- |
| **Velocidad Final ($v_f$)** | Tiempo y Aceleración | $$v_f = v_i + a \cdot t$$ |
| **Posición Final ($x_f$)** | Tiempo y Aceleración | $$x_f = x_i + v_i \cdot t + \frac{1}{2}a \cdot t^2$$ |
| **Velocidad o Posición** | **NO** tienes el tiempo | $$v_f^2 = v_i^2 + 2 \cdot a \cdot \Delta x$$ |