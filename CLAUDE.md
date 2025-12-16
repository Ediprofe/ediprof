# 🎓 Ediprofe - Plataforma Educativa

> **Plataforma de contenido educativo para matemáticas y ciencias, generada con IA y validada pedagógicamente.**

## 📋 Resumen del Proyecto

| Aspecto | Detalle |
|---------|---------|
| **Framework** | Astro (Static Site Generation) |
| **Hosting** | Vercel |
| **Contenido** | Markdown con LaTeX, gráficos interactivos |
| **Materias** | Matemáticas, Física, Química, Ciencias |
| **URL** | https://ediprofe.com |

---

## 🏗️ Estructura del Proyecto

```
ediprofe/
├── src/
│   ├── content/                    # 📚 CONTENIDO EDUCATIVO
│   │   ├── matematicas/
│   │   ├── fisica/
│   │   ├── quimica/
│   │   └── ciencias/
│   ├── components/
│   ├── layouts/
│   ├── pages/
│   ├── styles/
│   └── utils/
├── public/
│   └── images/
│       └── geometria/
├── scripts/
│   └── geometry/
├── specs/
│   └── geometria/
├── .agent/
│   └── workflows/
└── CLAUDE.md
```

### Jerarquía del Contenido

```
MATERIA (matematicas, fisica, quimica, ciencias)
└── CAPÍTULO (01-aritmetica, 02-algebra, ...)
    └── TEMA (01-numeros-naturales, ...)
        └── LECCIÓN (01-introduccion.md, 02-operaciones.md, ...)
```

### Convención de Nombres
- Carpetas: `XX-nombre-del-tema` (XX = número de orden)
- Archivos: `XX-titulo-leccion.md`
- Todo en **minúsculas**, sin tildes, guiones en lugar de espacios

---

# 🔄 FLUJO DE TRABAJO EN 3 ETAPAS

## ETAPA 1: PLANEADOR DOCENTE 📋

**Objetivo:** Estructurar el árbol de carpetas y archivos para un CAPÍTULO completo.

**Qué hacer:**
1. Recibir el nombre del capítulo y contexto
2. Proponer el árbol de carpetas con temas y lecciones (.md)
3. Para cada lección, indicar brevemente qué conceptos cubrirá
4. Presentar el árbol para **APROBACIÓN** del usuario

**Formato de entrega:**
```
CAPÍTULO: [Nombre]
├── 01-tema-nombre/
│   ├── _meta.json
│   ├── 01-leccion-nombre.md → [conceptos que cubre]
│   └── 02-leccion-nombre.md → [conceptos que cubre]
```

> ⚠️ **NO generar contenido hasta que el árbol sea APROBADO.**

---

## ETAPA 2: GENERADOR DE LECCIONES 📝

**Objetivo:** Generar MASIVAMENTE todas las lecciones del árbol aprobado.

**Qué hacer:**
1. Tomar el árbol aprobado de la Etapa 1
2. Generar TODAS las lecciones siguiendo la filosofía pedagógica
3. Crear los archivos `_meta.json` para cada tema
4. Cada lección = **LIBRETO completo** que el mejor profesor seguiría

**Reglas:**
- Una lección por archivo .md
- Estructura: Intro motivadora → Conceptos + ejemplos + ilustraciones → Práctica
- **SIN gráficos complejos** (se agregan en Etapa 3)
- Tablas y LaTeX SÍ permitidos
- Usar marcadores: `<!-- ILUSTRACIÓN: descripción -->`

---

## ETAPA 3: DISEÑADOR Y EVALUADOR PEDAGÓGICO 🎨

**Objetivo:** Enriquecer con gráficos y evaluar mejoras pedagógicas.

**Qué hacer:**

### 3.1 Agregar Gráficos

> ⚠️ **REGLA OBLIGATORIA: MÍNIMO UNA ILUSTRACIÓN POR CONCEPTO**
> 
> Un "concepto" = cada sección que inicia con título Markdown (##, ###)
> 
> **EXCEPCIÓN:** La sección de "Ejercicios de Práctica" NO requiere ilustraciones

- Usar el **Árbol de Decisión** para elegir tecnología
- Seguir `.agent/workflows/` para cada librería
- Gráficos claros como dibujos de pizarra

### 3.2 Evaluar Pedagógicamente

| Aspecto | Pregunta clave |
|---------|----------------|
| Claridad | ¿Se entiende a la primera? |
| Progresión | ¿Simple → complejo? |
| Ejemplos | ¿Suficientes y paso a paso? |
| Visuales | ¿Hay mínimo 1 ilustración por concepto? |
| Motivación | ¿El estudiante sabe POR QUÉ? |

### 3.3 Proponer Mejoras

Si detecta oportunidades de mejora pedagógica, proponerlas.

---

# 📚 FILOSOFÍA PEDAGÓGICA

## El Profesor Modelo

Cada lección debe ser un **LIBRETO LITERAL** que el mejor profesor del colegio pueda seguir AL PIE DE LA LETRA.

| Característica | Descripción |
|----------------|-------------|
| **SIMPLICIDAD** | Explica conceptos complejos de forma brutalmente simple |
| **CLARIDAD** | Cada oración tiene un solo propósito, sin ambigüedades |
| **ORDEN** | Secuencia lógica y natural de ideas |
| **MOTIVADOR** | Engancha al estudiante con preguntas y contexto real |
| **INDUCTIVO** | Va de lo particular a lo general, de ejemplos a teoría |
| **PROGRESIVO** | Una idea a la vez, sin saltos |

---

## Filosofía Anti-Abrumamiento

> **PRINCIPIO:** El estudiante no debe ver mucho texto antes de entender visualmente qué va a aprender.

### Reglas:
1. **Cheat Sheet (Llamarle "Lo escencial" o de una manera que no sea confusa en américa latina) + Ilustración JUNTOS al inicio:** Tabla resumen + gráfico visual = combo ganador
2. **Motivación rápida en 10 segundos:** El estudiante debe ver inmediatamente QUÉ va a obtener
3. **Síntesis antes de detalle:** Primero el resumen visual, luego la explicación
4. **NUNCA cheat sheet solo sin ilustración:** La tabla sin el gráfico NO tiene sentido

### Patrón Correcto:
```
1️⃣ Título + 1 línea intro  
2️⃣ Tabla resumen (Cheat Sheet)  
3️⃣ Ilustración visual JUSTO DESPUÉS  
4️⃣ Tip/regla para recordar  
5️⃣ --- (separador)
6️⃣ Detalles de cada concepto
```

**Ejemplo:**
- ❌ MALO: Tabla resumen → 200 líneas de texto → ilustración al final
- ✅ BUENO: Tabla resumen → ILUSTRACIÓN inmediata → Tip → detalles

---

## Estructura de Cada Lección

```
1. INTRODUCCIÓN MOTIVADORA
   - Pregunta enganchadora ("¿Alguna vez te has preguntado...?")
   - Conexión con la vida real
   - ¿Qué vas a aprender? (lista clara)
   - El resumen de resultados (Cheat Sheet)
   - [Ilustración visual inmediata]

2. CONCEPTO 1
   - Definición simple
   - Ejemplo 1 (resuelto paso a paso)
   - Ejemplo 2 (resuelto paso a paso)
   - [Ilustración]

3. CONCEPTO 2
   - Definición simple
   - Ejemplo 1
   - Ejemplo 2
   - [Ilustración]

4. [REPETIR para cada concepto]

5. RESUMEN (opcional pero recomendado)
   - Tabla o lista con los puntos clave

6. EJERCICIOS DE PRÁCTICA
   - 2 ejercicios por concepto
   - Con soluciones en <details>
```

---

## Reglas de Redacción

| ✅ HACER | ❌ EVITAR |
|----------|-----------|
| Oraciones cortas y directas | Párrafos densos sin pausas |
| Una idea por párrafo | Múltiples conceptos mezclados |
| Verbos en segunda persona ("vas a aprender") | Lenguaje impersonal |
| Ejemplos antes que teoría abstracta | Definiciones sin contexto |
| Preguntas retóricas para enganchar | Entrar directo en fórmulas |
| Transiciones claras ("Ahora que sabes X, veamos Y") | Saltar entre temas |

---

# 🎨 SISTEMA DE ILUSTRACIONES

## Principio Fundamental

> **La IA describe QUÉ construir, no CÓMO dibujarlo.**
> 
> Para ilustraciones que requieren precisión matemática, la IA genera especificaciones que un motor exacto renderiza.

---

## 🌳 Árbol de Decisión

```
¿QUÉ TIPO DE ILUSTRACIÓN NECESITO?
│
├─── 📊 ¿Es una GRÁFICA de funciones o datos?
│    └─── SÍ → ECHARTS (inline en .md)
│         • Funciones: f(x), parábolas, exponenciales
│         • Series de datos, estadísticas
│         • Histogramas, barras, líneas
│         • Plano cartesiano con puntos
│         📁 Ver: .agent/workflows/echarts.md
│
├─── 📐 ¿Es GEOMETRÍA con propiedades exactas?
│    └─── SÍ → GEOMETRYSPEC (JSON → Python → SVG)
│         • Triángulos con puntos notables
│         • Mediatrices, bisectrices, alturas, medianas
│         • Circunferencias inscritas/circunscritas
│         • Paralelismo, perpendicularidad exacta
│         📁 Ver: .agent/workflows/geometry-exact.md
│
├─── ✏️ ¿Es un DIAGRAMA ilustrativo/conceptual?
│    └─── SÍ → ROUGH.JS (inline en .md)
│         • Situaciones físicas (bloques, poleas)
│         • Modelos atómicos, partículas
│         • Equipos de laboratorio
│         • Mapas conceptuales, organigramas
│         📁 Ver: .agent/workflows/roughjs.md
│
├─── 🥧 ¿Es una representación de FRACCIONES?
│    └─── SÍ → CHART.JS (pie charts, inline)
│         📁 Ver: .agent/workflows/chartjs.md
│
├─── 🎲 ¿Es GEOMETRÍA 3D?
│    └─── SÍ → THREE.JS (inline en .md)
│         📁 Ver: .agent/workflows/threejs.md
│
└─── 📝 ¿Es solo una FÓRMULA?
     └─── SÍ → LATEX (inline en .md)
          • $inline$ o $$bloque$$
```

---

## Matriz de Decisión Rápida

| Necesito... | Uso... | Confianza |
|-------------|--------|-----------|
| Gráfica de $f(x) = 2x + 3$ | ECharts | ⭐⭐⭐⭐⭐ 95% |
| Baricentro de triángulo | GeometrySpec | ⭐⭐⭐⭐⭐ 99% |
| Histograma de datos | ECharts | ⭐⭐⭐⭐⭐ 95% |
| Circuncentro exacto | GeometrySpec | ⭐⭐⭐⭐⭐ 99% |
| Bloque en plano inclinado | Rough.js | ⭐⭐⭐⭐ 85% |
| Modelo atómico de Bohr | Rough.js | ⭐⭐⭐⭐ 85% |
| Fracción 3/4 visual | Chart.js | ⭐⭐⭐⭐ 90% |
| Cubo con diagonales | Three.js | ⭐⭐⭐ 70% |

---

## 🚨 Reglas Críticas para Ilustraciones

### Para Geometría Exacta

```
❌ PROHIBIDO:
   • Escribir JSXGraph con coordenadas "a ojo"
   • Usar funciones JSXGraph: circumcenter, incircle, incenter, perpendicularbisector
   • Hardcodear coordenadas sin cálculo matemático

✅ OBLIGATORIO:
   • Crear GeometrySpec JSON en specs/geometria/
   • Ejecutar: python scripts/geometry/renderer.py --spec [archivo] --verify
   • Enlazar SVG resultante: ![Alt](/images/geometria/...)
```

### Para Todos los Gráficos

```
✅ SIEMPRE:
   • Envolver en DOMContentLoaded
   • Verificar disponibilidad: if (typeof echarts !== 'undefined')
   • Usar wrapper con fondo y bordes redondeados
   • ID únicos: tipo-leccion-numero

❌ NUNCA:
   • Interactividad por defecto (fixed: true en todos los puntos)
   • Zoom, pan, o elementos arrastrables sin solicitud explícita
```

---

# 📝 FORMATO TÉCNICO

## LaTeX

```markdown
# Bloque (centrado):
$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

# Inline:
La fórmula es $a^2 + b^2 = c^2$

# En tablas:
| Operación | Fórmula |
|-----------|---------|
| Área del círculo | $A = \pi r^2$ |
```

### ⚠️ Restricciones de LaTeX

| ❌ NO hacer | ✅ Alternativa |
|-------------|----------------|
| LaTeX en títulos de secciones | Usar texto plano o Unicode |
| `\[...\]` o `\(...\)` | Usar `$$...$$` o `$...$` |
| Símbolos de moneda `$` solos | Usar `USD`, `COP`, o escapar |

---

## Emojis en Secciones

Usar emojis consistentes:
- 📖 Definiciones
- 📊 Ejemplos/Gráficos
- 💡 Tips/Notas importantes
- ⚙️ Ejemplos detallados
- 📝 Ejercicios
- 🎯 Objetivos
- 📋 Resúmenes/Tablas

> ⚠️ **NO usar emojis en el título H1 principal** (causa problemas de renderizado)

---

# 🎨 ESTILO VISUAL (MODO CLARO/OSCURO)

> **REGLA GENERAL:** Todo elemento visual debe verse bien en AMBOS modos.

## ✅ USAR (funcionan en ambos modos)

### 1. Markdown Nativo
Blockquotes (`>`), tablas, listas, LaTeX, enlaces

### 2. Canvas (Rough.js/JSXGraph/ECharts)
Controlan sus propios colores

### 3. Tarjetas con Fondos OSCUROS
```html
<div style="background: #1e293b; border-radius: 12px; padding: 1rem;">
  <div style="color: #f8fafc; font-weight: bold;">Título</div>
  <div style="color: #94a3b8;">Contenido</div>
</div>
```

### 4. Tarjetas con Colores SATURADOS de Alto Contraste
| Color | Background | Text |
|-------|------------|------|
| Amarillo | `#fef3c7` | `#1e293b` |
| Azul | `#dbeafe` | `#1e3a8a` |
| Verde oscuro | `#064e3b` | `#ffffff` |

## ❌ EVITAR

- Fondos claros (`#f0fdf4`) + texto gris (`#166534`) → invisible en modo oscuro
- Colores de texto sin especificar → dependen del tema
- `border-left` con fondo claro sin color de texto explícito

## Wrapper Estándar para Gráficos

```html
<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <span style="font-size: 1.1rem;">📊</span>
  <div id="grafico-id" style="width: 100%; height: 400px;"></div>
</div>
```

---

# 🎨 PALETA DE COLORES

## Por Elemento Geométrico

| Elemento | Color | Hex |
|----------|-------|-----|
| Medianas | Verde | `#22c55e` |
| Alturas | Naranja | `#f97316` |
| Bisectrices | Violeta | `#8b5cf6` |
| Mediatrices | Rosa | `#ec4899` |
| Puntos notables | Rojo | `#ef4444` |
| Vértices | Gris oscuro | `#1e293b` |
| Auxiliares | Gris | `#94a3b8` |
| Circunferencias | Azul | `#3b82f6` |

## Por Materia

| Materia | Color | Hex |
|---------|-------|-----|
| Matemáticas | Azul | `#3b82f6` |
| Física | Naranja | `#f97316` |
| Química | Verde | `#22c55e` |
| Ciencias | Morado | `#a855f7` |

---

# 📁 DOCUMENTACIÓN DE WORKFLOWS

| Archivo | Contenido |
|---------|-----------|
| `.agent/workflows/content-generation.md` | Flujo de generación de lecciones |
| `.agent/workflows/echarts.md` | Funciones, datos, estadísticas |
| `.agent/workflows/geometry-exact.md` | GeometrySpec: geometría exacta |
| `.agent/workflows/roughjs.md` | Diagramas ilustrativos |
| `.agent/workflows/chartjs.md` | Fracciones |
| `.agent/workflows/threejs.md` | Geometría 3D |
| `.agent/workflows/illustration-decision.md` | Árbol de decisión expandido |

---

# ✅ CHECKLIST ANTES DE ENTREGAR

## Contenido (Etapa 2)
- [ ] ¿Tiene introducción motivadora con pregunta enganchadora?
- [ ] ¿Cheat Sheet + Ilustración juntos al inicio?
- [ ] ¿Cada concepto tiene al menos 2 ejemplos resueltos?
- [ ] ¿Las ideas van de lo simple a lo complejo?
- [ ] ¿Hay transiciones claras entre conceptos?
- [ ] ¿Los títulos NO tienen LaTeX?
- [ ] ¿Hay ejercicios de práctica al final con `<details>`?

## Ilustraciones (Etapa 3)
- [ ] ¿Mínimo 1 ilustración por concepto (excepto ejercicios)?
- [ ] ¿Tecnología correcta según árbol de decisión?
- [ ] ¿Las tarjetas HTML funcionan en modo oscuro?
- [ ] ¿Las ilustraciones son claras como un dibujo de pizarra?
- [ ] ¿IDs únicos en todos los gráficos?
- [ ] ¿Wrapper estándar con fondo y bordes?

---

# 🔧 COMANDOS ÚTILES

```bash
# Desarrollo local
npm run dev

# Build de producción
npm run build

# Generar SVG de geometría
python scripts/geometry/renderer.py --spec specs/geometria/triangulos/baricentro.json --output public/images/geometria/ --verify

# Crear nueva lección
node scripts/new-lesson.js
```

---

# 📌 NOTAS PARA EL AGENTE

1. **Respetar las 3 etapas:** Planeación → Lecciones → Ilustraciones
2. **No generar contenido sin aprobación** del árbol de carpetas
3. **Siempre consultar** `.agent/workflows/` antes de generar ilustraciones
4. **Usar el árbol de decisión** para elegir la tecnología correcta
5. **Mínimo 1 ilustración por concepto** (excepto ejercicios de práctica)
6. **Validar geometría exacta** con `--verify` antes de enlazar SVG
7. **IDs únicos** para evitar colisiones en gráficos inline
8. **Anti-abrumamiento:** Cheat Sheet + Ilustración JUNTOS al inicio

---

# 📚 EJEMPLOS DE REFERENCIA

Para ver el estilo correcto de lecciones, revisar:
- `src/content/matematicas/01-aritmetica/05-proporcionalidad/03-regla-de-tres-simple.md`
- `/fisica/cinematica/mrua/lanzamiento-vertical`
- `/fisica/introduccion-a-la-fisica/introduccion/la-fisica-y-sus-ramas`

# SOLICITUD CONCRETA

La solicitud concreta que te voy a pedir con base en este contexto, está en la raíz de este proyecto, en PETICION.md