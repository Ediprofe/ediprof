# **Número atómico**

Para comprender cómo está formada la materia, es necesario conocer la **estructura interna del átomo**, sus partes y las partículas que lo componen.
A continuación se presentan sus zonas, características y la forma en que se identifican los elementos en la tabla periódica.

---

## **División general del átomo**

El átomo se organiza en **dos regiones fundamentales**:

* **Núcleo** → zona interna
* **Periferia** → zona externa

### 🎯 **Representación del átomo**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-atomo" width="600" height="280" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-atomo')) {
    var canvas = document.getElementById('roughjs-atomo');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    var cx = 200; // Centro X del átomo
    var cy = 140; // Centro Y del átomo
    
    // Órbitas de electrones (periferia)
    rc.circle(cx, cy, 200, { stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.8 });
    rc.circle(cx, cy, 140, { stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.8 });
    rc.circle(cx, cy, 80, { stroke: '#94a3b8', strokeWidth: 1.5, roughness: 0.8 });
    
    // Núcleo (centro con protones y neutrones)
    rc.circle(cx, cy, 35, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', strokeWidth: 2, roughness: 0.6 });
    
    // Protones en el núcleo (rojo con +)
    rc.circle(cx - 8, cy - 5, 12, { fill: '#ef4444', fillStyle: 'solid', stroke: '#b91c1c', roughness: 0.5 });
    rc.circle(cx + 8, cy + 5, 12, { fill: '#ef4444', fillStyle: 'solid', stroke: '#b91c1c', roughness: 0.5 });
    
    // Neutrones en el núcleo (gris)
    rc.circle(cx + 8, cy - 8, 10, { fill: '#6b7280', fillStyle: 'solid', stroke: '#374151', roughness: 0.5 });
    rc.circle(cx - 6, cy + 8, 10, { fill: '#6b7280', fillStyle: 'solid', stroke: '#374151', roughness: 0.5 });
    
    // Electrones en las órbitas (azul con -)
    rc.circle(cx + 98, cy, 10, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 0.5 });
    rc.circle(cx - 98, cy, 10, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 0.5 });
    rc.circle(cx, cy - 68, 10, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 0.5 });
    rc.circle(cx + 50, cy + 55, 10, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 0.5 });
    
    // Etiquetas de las partículas
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#fff';
    ctx.textAlign = 'center';
    ctx.fillText('+', cx - 8, cy - 1);
    ctx.fillText('+', cx + 8, cy + 9);
    ctx.fillText('−', cx + 98, cy + 4);
    ctx.fillText('−', cx - 98, cy + 4);
    ctx.fillText('−', cx, cy - 64);
    ctx.fillText('−', cx + 50, cy + 59);
    
    // Leyenda a la derecha
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.textAlign = 'left';
    
    // Título
    ctx.fillStyle = '#1e293b';
    ctx.fillText('LEYENDA', 380, 40);
    
    // Protón
    rc.circle(395, 65, 14, { fill: '#ef4444', fillStyle: 'solid', stroke: '#b91c1c', roughness: 0.5 });
    ctx.fillStyle = '#fff';
    ctx.fillText('+', 392, 69);
    ctx.fillStyle = '#ef4444';
    ctx.font = '12px Inter, sans-serif';
    ctx.fillText('Protón (+)', 415, 70);
    
    // Neutrón
    rc.circle(395, 100, 14, { fill: '#6b7280', fillStyle: 'solid', stroke: '#374151', roughness: 0.5 });
    ctx.fillStyle = '#6b7280';
    ctx.fillText('Neutrón (0)', 415, 105);
    
    // Electrón
    rc.circle(395, 135, 14, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1d4ed8', roughness: 0.5 });
    ctx.fillStyle = '#fff';
    ctx.fillText('−', 392, 139);
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Electrón (−)', 415, 140);
    
    // Etiquetas de zonas
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('NÚCLEO', 380, 180);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Protones + Neutrones', 380, 195);
    
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('PERIFERIA', 380, 225);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Electrones en órbitas', 380, 240);
  }
});
</script>

## **Núcleo**

El núcleo es la **parte central del átomo** y contiene dos tipos de partículas subatómicas:

* **Protones** → carga **positiva (+)**
* **Neutrones** → carga **neutra (0)**

Estas partículas se encuentran **muy juntas**, lo que hace que el núcleo tenga **gran densidad**.

---

## **Periferia**

La periferia (o corteza) es la **región que rodea al núcleo**.
Allí se encuentran los:

* **Electrones** → carga **negativa (−)**

Los electrones se mueven alrededor del núcleo formando **niveles o capas de energía**.

---

## **Número atómico (Z)**

El **número atómico**, representado con la letra **Z**, indica:

* La **cantidad de protones** en el núcleo
* La identidad del **elemento químico**
* Cada elemento tiene **un número atómico único**

**En resumen:**
**Z = número de protones**

---

## **Ejemplos de número atómico**

* **Hidrógeno (Z = 1)** → 1 protón
* **Helio (Z = 2)** → 2 protones
* **Litio (Z = 3)** → 3 protones
* **Berilio (Z = 4)** → 4 protones
* **Boro (Z = 5)** → 5 protones

---

## **Tabla periódica**

La tabla periódica **ordena los elementos** según su número atómico.
Se **lee de izquierda a derecha** y de **arriba hacia abajo**, aumentando siempre la cantidad de protones.
Gracias a ella es posible **identificar el elemento** únicamente conociendo su número atómico.

---

https://youtu.be/efOK-ZVm0NI

[Ver en Tiktok](https://vt.tiktok.com/ZSBJPBDcg/)

--- 

## **Completa la tabla**

Para reforzar el concepto de **número atómico (Z)**, observa los átomos de la tabla y **rellena la columna que falta**.
Recuerda: **Z es igual al número de protones** del átomo.

| Átomo   | Número de protones | Número atómico (Z) | Elemento al que pertenece |
| ------- | ------------------ | ------------------ | ------------------------- |
| Átomo 1 | 7                  |                    | Nitrógeno                 |
| Átomo 2 | 22                 |                    | Titanio                   |
| Átomo 3 | 88                 |                    | Radio                     |
| Átomo 4 | 82                 |                    | Plomo                     |

---
https://youtu.be/JN-802f841Y

[Ver en Tiktok](https://vt.tiktok.com/ZSBJPDnqf/)