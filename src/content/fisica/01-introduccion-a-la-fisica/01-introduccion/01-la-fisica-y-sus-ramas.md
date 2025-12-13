
# **La física y sus ramas**

## ⚙️ **¿Qué es la física?**

La **física** es la ciencia que estudia

> **la materia, la energía y las interacciones que ocurren entre ellas.**

Busca describir y predecir los fenómenos naturales mediante leyes universales.

---

## 🌍 **¿Por qué es importante la física?**

La física explica el funcionamiento del mundo natural, desde lo microscópico hasta lo cósmico.

**Ejemplos cotidianos:**

* La caída de los objetos → *gravedad*
* El sonido → *ondas*
* La formación de imágenes → *óptica*
* El funcionamiento de motores y aparatos → *energía y trabajo*

> **En pocas palabras:**
> La física nos permite **comprender**, **modelar** y **aprovechar** los fenómenos del universo.

---

## 🧩 **Ramas de la física**

Las ramas de la física pueden organizarse en dos grandes bloques:

### 🎯 **Visualización: El árbol de la Física**

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <canvas id="roughjs-ramas" width="600" height="320" style="width: 100%; height: auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-ramas')) {
    var canvas = document.getElementById('roughjs-ramas');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Nodo Central: FÍSICA
    var cx = 300;
    rc.rectangle(cx - 55, 15, 110, 40, { fill: '#1e293b', fillStyle: 'solid', stroke: '#0f172a', strokeWidth: 2, roughness: 0.5 });
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#ffffff';
    ctx.textAlign = 'center';
    ctx.fillText('🔬 FÍSICA', cx, 42);
    
    // Líneas de conexión
    rc.line(cx, 55, 150, 90, { stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5 });
    rc.line(cx, 55, 450, 90, { stroke: '#db2777', strokeWidth: 2, roughness: 0.5 });
    
    // --- Rama Izquierda: CLÁSICA ---
    rc.rectangle(75, 90, 150, 35, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5 });
    ctx.fillStyle = '#1e3a8a';
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('🏛️ CLÁSICA', 150, 113);
    
    // Sub-ramas Clásica
    var branchesC = ['Mecánica', 'Termodinámica', 'Óptica', 'Acústica', 'Electromagnetismo'];
    for(var i=0; i<branchesC.length; i++) {
       var y = 145 + i*35;
       rc.line(150, 125, 150, y, { stroke: '#94a3b8', roughness: 0.5 });
       rc.line(150, y, 165, y, { stroke: '#94a3b8', roughness: 0.5 });
       rc.rectangle(35, y-12, 115, 24, { stroke: '#3b82f6', roughness: 0.5, fill: 'rgba(59, 130, 246, 0.15)', fillStyle: 'solid' });
       ctx.fillStyle = '#1e40af';
       ctx.font = '11px Inter, sans-serif';
       ctx.fillText(branchesC[i], 92, y+4);
    }
    
    // --- Rama Derecha: MODERNA ---
    rc.rectangle(375, 90, 150, 35, { fill: '#fce7f3', fillStyle: 'solid', stroke: '#db2777', strokeWidth: 2, roughness: 0.5 });
    ctx.fillStyle = '#831843';
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('🚀 MODERNA', 450, 113);
    
    // Sub-ramas Moderna
    var branchesM = ['Relatividad', 'Mecánica Cuántica', 'Atómica / Nuclear', 'Partículas', 'Cosmología'];
    for(var i=0; i<branchesM.length; i++) {
       var y = 145 + i*35;
       rc.line(450, 125, 450, y, { stroke: '#94a3b8', roughness: 0.5 });
       rc.line(450, y, 435, y, { stroke: '#94a3b8', roughness: 0.5 });
       rc.rectangle(450, y-12, 120, 24, { stroke: '#db2777', roughness: 0.5, fill: 'rgba(219, 39, 119, 0.15)', fillStyle: 'solid' });
       ctx.fillStyle = '#9d174d';
       ctx.font = '11px Inter, sans-serif';
       ctx.fillText(branchesM[i], 510, y+4);
    }
  }
});
</script>

---

### 🏛️ **1. Física clásica**

Estudia los fenómenos que ocurren a **escala humana**, con **bajas velocidades** y en **condiciones ordinarias**.

#### Principales ramas de la física clásica

| **Rama**              | **Qué estudia**                              | **Ejemplos**                     |
| --------------------- | -------------------------------------------- | -------------------------------- |
| **Mecánica clásica**  | Movimiento, fuerzas y equilibrio             | Tiro parabólico, palancas        |
| **Termodinámica**     | Calor, temperatura y energía térmica         | Motores térmicos, refrigeradores |
| **Óptica clásica**    | Comportamiento de la luz                     | Espejos, lentes, arcoíris        |
| **Acústica**          | Producción y propagación del sonido          | Instrumentos musicales, ecos     |
| **Electromagnetismo** | Electricidad, magnetismo y cargas eléctricas | Circuitos, imanes, antenas       |

---

### 🚀 **2. Física moderna**

Surge a comienzos del siglo XX para explicar fenómenos que la física clásica no podía describir: **velocidades cercanas a la luz**, **dimensiones atómicas** y **escala cósmica**.

#### Principales ramas de la física moderna

| **Rama**                     | **Qué estudia**                                                               | **Ejemplos**                       |
| ---------------------------- | ----------------------------------------------------------------------------- | ---------------------------------- |
| **Relatividad**              | Estructura del espacio-tiempo y efectos a grandes velocidades o grandes masas | GPS, agujeros negros               |
| **Mecánica cuántica**        | Comportamiento de partículas subatómicas                                      | Átomos, láseres, semiconductores   |
| **Física atómica y nuclear** | Estructura del átomo y del núcleo                                             | Radiactividad, fisión/fusión       |
| **Física de partículas**     | Componentes fundamentales de la materia                                       | Quarks, aceleradores de partículas |
| **Cosmología**               | Origen y evolución del universo                                               | Big Bang, expansión del cosmos     |

---

## 🔗 **Relación con otras ciencias**

| **Ciencia**                 | **Relación con la física**                                                                |
| --------------------------- | ----------------------------------------------------------------------------------------- |
| **Química**                 | Explica las interacciones y la energía entre átomos y moléculas.                          |
| **Biología**                | Describe procesos vitales mediante principios físicos (movimiento, respiración, energía). |
| **Matemáticas**             | Proporcionan el lenguaje para expresar leyes y modelos físicos.                           |
| **Tecnología e ingeniería** | Aplican principios físicos para crear herramientas, máquinas y sistemas.                  |

---

## 💡 **Conclusión**

> La física es una **ciencia fundamental** que nos permite comprender las reglas del universo,
> desde el movimiento de una pelota hasta el comportamiento de las estrellas y partículas subatómicas.
> Es la base del desarrollo científico, tecnológico e industrial del mundo moderno.

---
