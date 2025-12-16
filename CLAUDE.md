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
│       ├── geometria/              # SVGs de GeometrySpec
│       └── funciones/              # SVGs de GraphSpec
├── scripts/
│   ├── geometry/                   # Renderer de geometría exacta
│   └── functions/                  # Renderer de GraphSpec (unificado)
├── specs/
│   ├── geometria/                  # Specs de geometría
│   └── funciones/                  # Specs de GraphSpec (gráficas)
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
| **Ilustraciones Dicentes** | ¿Cada gráfico tiene leyenda y anotaciones explicativas? |
| Motivación | ¿El estudiante sabe POR QUÉ? |

> 🚨 **CRÍTICO: Ilustraciones Auto-Explicativas**
>
> Todo gráfico DEBE ser **auto-explicativo** sin necesidad de leer el texto alrededor:
> - **Leyendas:** Cuando hay múltiples curvas/elementos, cada uno debe estar etiquetado con su fórmula/nombre y color
> - **Anotaciones:** Flechas indicando dirección de transformaciones, líneas de referencia con etiquetas
> - **Colores consistentes:** La función base en gris (`#94a3b8`), transformaciones en colores vivos
> - **Texto contextual:** Notas breves dentro del gráfico explicando el "¿por qué?"

> 🚨 **CRÍTICO: Verificación Matemática de Puntos Críticos**
>
> Cuando se marcan puntos en gráficos de funciones transformadas, **VERIFICAR matemáticamente** las coordenadas:
>
> Para `y = A·sin(Bx - C) + D`, el **máximo** (donde sin = 1) ocurre cuando:
> - `Bx - C = π/2` → `x = (π/2 + C) / B`
>
> **Ejemplo:** `y = 3sin(2x - π) + 1`
> - Máximo: `2x - π = π/2` → `x = 3π/4` (NO π/2)
>
> **NUNCA asumir** que el máximo está en π/2 sin calcular.

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

## 🌳 Árbol de Decisión SIMPLIFICADO

```
¿QUÉ TIPO DE ILUSTRACIÓN NECESITO?
│
├─── 📈 ¿Es una GRÁFICA (funciones, datos, estadísticas)?
│    └─── SÍ → GRAPHSPEC (JSON → Python → SVG animado) ⭐ RECOMENDADO
│         • Funciones: sin(x), cos(x), lineales, cuadráticas
│         • Datos: histogramas, barras, scatter plots
│         • Fracciones: pie charts
│         • Animaciones CSS automáticas
│         📁 Ver: .agent/workflows/graphspec.md
│
├─── 📐 ¿Es GEOMETRÍA con propiedades exactas?
│    └─── SÍ → GEOMETRYSPEC (JSON → Python → SVG)
│         • Triángulos con puntos notables
│         • Mediatrices, bisectrices, alturas, medianas
│         • Circunferencias inscritas/circunscritas
│         📁 Ver: .agent/workflows/geometry-exact.md
│
├─── ✏️ ¿Es un DIAGRAMA ilustrativo/conceptual?
│    └─── SÍ → ROUGH.JS (inline en .md)
│         • Situaciones físicas (bloques, poleas)
│         • Modelos atómicos, equipos de laboratorio
│         • Mapas conceptuales
│         📁 Ver: .agent/workflows/roughjs.md
│
├─── 🎲 ¿Es GEOMETRÍA 3D?
│    └─── SÍ → THREE.JS (inline en .md)
│         📁 Ver: .agent/workflows/threejs.md
│
└─── 📝 ¿Es solo una FÓRMULA?
     └─── SÍ → LATEX (inline en .md)
          • $inline$ o $$bloque$$
```

> **NOTA:** GraphSpec unifica lo que antes eran FunctionSpec, ECharts y Chart.js en un solo sistema optimizado.

---

## Matriz de Decisión Rápida

| Necesito... | Uso... | Tipo GraphSpec |
|-------------|--------|----------------|
| Gráfica de $\sin x$, $\cos x$, $\tan x$ | **GraphSpec** | `function` |
| Onda con amplitud/período/fase | **GraphSpec** | `function` |
| Gráfica lineal $f(x) = 2x + 3$ | **GraphSpec** | `function` |
| Histograma de frecuencias | **GraphSpec** | `histogram` |
| Gráfico de barras | **GraphSpec** | `bar` |
| Scatter plot (dispersión) | **GraphSpec** | `scatter` |
| Fracción 3/4 como pastel | **GraphSpec** | `pie` |
| Baricentro de triángulo | GeometrySpec | - |
| Circuncentro exacto | GeometrySpec | - |
| Bloque en plano inclinado | Rough.js | - |
| Modelo atómico de Bohr | Rough.js | - |
| Cubo con diagonales 3D | Three.js | - |

---

## 🚨 Reglas Críticas para Ilustraciones

### Para Gráficas de Funciones y Datos (GraphSpec)

```
✅ OBLIGATORIO:
   • Crear GraphSpec JSON en specs/funciones/
   • Especificar "type": "function" | "bar" | "histogram" | "pie" | "scatter"
   • Ejecutar: python scripts/functions/renderer.py --spec [archivo]
   • Enlazar SVG resultante: ![Alt](/images/funciones/...)

TIPOS DISPONIBLES:
   • "function" → Funciones matemáticas (sin, cos, lineales, etc.)
   • "bar" → Gráficos de barras
   • "histogram" → Histogramas de frecuencias
   • "pie" → Gráficos de pastel (fracciones)
   • "scatter" → Gráficos de dispersión
```

### Para Geometría Exacta (GeometrySpec)

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

### Reutilización Inteligente de Specs

```
ANTES de crear un nuevo spec:

1. BUSCAR si ya existe uno similar:
   • Funciones trig → specs/funciones/trigonometria/
   • Geometría → specs/geometria/triangulos/

2. SI EXISTE similar:
   • Duplicar y modificar parámetros
   • Mantener nomenclatura consistente

3. SI NO EXISTE:
   • Crear nuevo con nombre descriptivo

CONVENCIÓN DE NOMBRES:
   • descripcion-concisa.json
   • Ejemplos: seno-principal.json, histograma-edades.json
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

> 🚨 **CRÍTICO: NUNCA usar LaTeX en títulos Markdown**
> 
> Los títulos `## Sección` aparecen en la tabla de contenidos. Si tienen `$x^2$`, se verá como código crudo: `$x^2$`
> 
> | ❌ MAL | ✅ BIEN |
> |--------|---------|
> | `## Función $f(x) = x^2$` | `## Función cuadrática f(x) = x²` |
> | `## El seno $\sin\theta$` | `## El seno (sin θ)` |
> | `## Derivada $\frac{dy}{dx}$` | `## La derivada dy/dx` |

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
| `.agent/workflows/graphspec.md` | **GraphSpec: sistema unificado de gráficas** ⭐ PRINCIPAL |
| `.agent/workflows/geometry-exact.md` | GeometrySpec: geometría exacta |
| `.agent/workflows/roughjs.md` | Diagramas ilustrativos |
| `.agent/workflows/threejs.md` | Geometría 3D |
| `.agent/workflows/illustration-decision.md` | Árbol de decisión simplificado |

> **NOTA:** GraphSpec reemplaza a ECharts, Chart.js y FunctionSpec para todas las gráficas.

---

# 🔧 SISTEMA DE RENDERERS ESPECIALIZADOS

Además de los renderers principales (GraphSpec, GeometrySpec), existen renderers especializados por tema:

## Renderers Disponibles

| Renderer | Ubicación | Propósito |
|----------|-----------|-----------|
| `renderer.py` | `scripts/functions/` | GraphSpec: funciones, barras, pie, scatter |
| `renderer.py` | `scripts/geometry/` | GeometrySpec: geometría exacta |
| `trigonometry_renderer.py` | `scripts/geometry/` | Triángulos trigonométricos con etiquetas |
| `unit_circle_renderer.py` | `scripts/geometry/` | Círculo unitario, cuadrantes, signos |
| `identity_renderer.py` | `scripts/geometry/` | Identidades trig, fórmulas, estrategias |
| `oblique_triangle_renderer.py` | `scripts/geometry/` | Triángulos oblicuángulos, leyes de senos/cosenos |
| `circle_renderer.py` | `scripts/geometry/` | Circunferencia, círculo, elementos, ángulos, teoremas |

## Uso de Renderers Especializados

```bash
# Círculo unitario
python3 scripts/geometry/unit_circle_renderer.py --type basic --output archivo.svg
# Tipos: basic, point, quadrants, reference, negative, quadrantal, cofunctions

# Identidades trigonométricas  
python3 scripts/geometry/identity_renderer.py --type map --output archivo.svg
# Tipos: map, pythagorean, double, half, proof, equations

# Triángulos trigonométricos
python3 scripts/geometry/trigonometry_renderer.py --spec archivo.json --output archivo.svg

# Triángulos oblicuángulos
python3 scripts/geometry/oblique_triangle_renderer.py --type types --output archivo.svg
# Tipos: types, sines, cosines, cases, navigation

# Circunferencia y círculo (v2.0 - una ilustración por concepto)
python3 scripts/geometry/circle_renderer.py --type TYPE --output archivo.svg

# === BÁSICOS ===
#   basic              → Circunferencia con centro y radio

# === ELEMENTOS (uno por concepto) ===
#   element_radius     → Solo el radio
#   element_diameter   → Solo el diámetro
#   element_chord      → Solo la cuerda
#   element_arc        → Solo el arco
#   element_sector     → Sector circular (2 radios + arco, "rebanada de pizza")
#   element_segment    → Segmento circular (cuerda + arco, "media luna")
#   element_crown      → Corona circular (2 circunferencias concéntricas)

# === POSICIONES ===
#   point_positions    → Punto interior/sobre/exterior
#   tangent_secant     → Recta tangente vs secante
#   circle_positions   → Exteriores, tangentes, secantes, concéntricas

# === ÁNGULOS (uno por tipo) ===
#   angle_central      → Ángulo central (vértice en centro)
#   angle_inscribed    → Ángulo inscrito (vértice en circunferencia)
#   angle_semi_inscribed → Ángulo semi-inscrito (un lado tangente)
#   angle_interior     → Ángulo interior (vértice dentro)
#   angle_exterior     → Ángulo exterior (vértice fuera)

# === TEOREMAS ===
#   theorem_inscribed  → Teorema: inscrito = ½ central
#   theorem_tales      → Teorema de Tales (semicircunferencia = 90°)

# === FÓRMULAS ===
#   formula_length     → Longitud L = 2πr
#   formula_area       → Área A = πr²
#   formula_sector_area → Área del sector
#   formula_segment_area → Área del segmento
```

## Organización de Salidas SVG

```
public/images/
├── funciones/           # GraphSpec (gráficas de funciones)
│   └── trigonometria/   # sin, cos, tan, inversas, etc.
├── geometria/           # GeometrySpec (construcciones geométricas)
│   └── triangulos/      # Puntos notables, etc.
├── trigonometria/       # Renderers especializados
│   ├── circulo-unitario/  # unit_circle_renderer.py
│   ├── identidades/       # identity_renderer.py
│   └── triangulos-oblicuangulos/  # oblique_triangle_renderer.py
└── geometria/
    └── circulos/          # circle_renderer.py
```

---

# 📊 MANTENIBILIDAD DEL SISTEMA DE SPECS

## Principio de Organización

> **REGLA:** Cada tipo de ilustración tiene su lugar predefinido.
> El agente NO debe crear nuevas carpetas sin justificación.

## Estructura de Specs

```
specs/
├── geometria/
│   ├── triangulos/      # GeometrySpec de triángulos
│   ├── cuadrilateros/   # GeometrySpec de cuadriláteros
│   ├── circulos/        # GeometrySpec de círculos
│   └── trigonometria/   # Specs de triángulos trig (OAH)
└── funciones/
    ├── trigonometria/   # GraphSpec de sin, cos, tan
    ├── estadistica/     # GraphSpec de histogramas, barras
    └── fracciones/      # GraphSpec de pie charts
```

## ¿Qué Renderer Usar por Tema?

| Tema de la Lección | Renderer | Carpeta Output |
|--------------------|----------|----------------|
| Gráficas de funciones trig | `scripts/functions/renderer.py` | `public/images/funciones/trigonometria/` |
| Círculo unitario | `scripts/geometry/unit_circle_renderer.py` | `public/images/trigonometria/circulo-unitario/` |
| Identidades trig | `scripts/geometry/identity_renderer.py` | `public/images/trigonometria/identidades/` |
| Triángulos rectángulos | `scripts/geometry/trigonometry_renderer.py` | `public/images/geometria/trigonometria/` |
| Triángulos oblicuángulos | `scripts/geometry/oblique_triangle_renderer.py` | `public/images/trigonometria/triangulos-oblicuangulos/` |
| **Circunferencia y círculo** | `scripts/geometry/circle_renderer.py` | `public/images/geometria/circulos/` |
| Puntos notables | `scripts/geometry/renderer.py` | `public/images/geometria/triangulos/` |
| Histogramas/barras | `scripts/functions/renderer.py` | `public/images/funciones/estadistica/` |

## Checklist para Nuevos Renderers

Antes de crear un nuevo renderer, verificar:

1. [ ] ¿Existe ya un renderer que cubra este caso?
2. [ ] ¿Se puede extender un renderer existente?
3. [ ] Si es nuevo: documentar en esta tabla y en `.agent/workflows/`
4. [ ] Crear carpeta de output en `public/images/` correspondiente

---

# 🔒 REGLAS DE RIGUROSIDAD PARA SVGs (TODAS LAS ILUSTRACIONES)

> **PRINCIPIO:** Todo SVG generado debe ser 100% fiel a la descripción matemática. No hay margen para "aproximaciones visuales".

## 1. Validación Matemática de Coordenadas

```
ANTES DE GENERAR:
1. ¿Se calcularon TODAS las coordenadas con fórmulas matemáticas?
2. ¿Se usaron funciones trigonométricas exactas (cos, sin, etc.)?
3. ¿Se verificó que los puntos están donde deben estar?

NUNCA:
- Hardcodear coordenadas "a ojo"
- Copiar coordenadas de un ejemplo sin recalcular
- Asumir que x=π/2 es siempre el máximo de una función transformada
```

## 2. Verificación de Visibilidad del Texto

```
REGLA: Todo texto/etiqueta debe ser 100% visible.

CHECKLIST:
- [ ] ¿El texto cabe dentro del viewBox?
- [ ] ¿No hay texto cortado en los bordes?
- [ ] ¿El texto no se superpone con otros elementos?
- [ ] ¿El tamaño de fuente es legible (mínimo 10px)?

SOLUCIÓN: Calcular posición del texto DESPUÉS de definir el viewBox.
Si el texto no cabe, ajustar viewBox o reubicar el texto.
```

## 3. Fidelidad Visual de Figuras Geométricas

```
REGLA: Cada figura debe ser EXACTAMENTE lo que representa.

SECTOR CIRCULAR ≠ SEGMENTO CIRCULAR:
- SECTOR: Región limitada por 2 radios y un arco (triángulo curvo)
- SEGMENTO: Región limitada por 1 cuerda y un arco (media luna)

VERIFICACIÓN: Antes de renderizar, preguntar:
"¿Esta figura se ve EXACTAMENTE como la definición matemática?"
```

## 4. Consistencia de Escala y Proporciones

```
REGLA: Los elementos relacionados deben mantener proporciones coherentes.

EJEMPLOS:
- Radio menor < Radio mayor (siempre)
- Ángulo de 30° debe verse como 30° (no como 60°)
- Circunferencias concéntricas deben compartir el mismo centro
```

## 5. Control de Calidad en Arcos y Curvas

```
REGLA: Arcos y curvas deben ser suaves y matemáticamente correctos.

CHECKLIST:
- [ ] ¿Los arcos usan SVG path con A (arc) correctamente?
- [ ] ¿El sweep-flag y large-arc-flag son correctos?
- [ ] ¿Los ángulos de inicio y fin son precisos?

FÓRMULA para punto en circunferencia:
x = cx + r * cos(θ)
y = cy - r * sin(θ)  ← NOTA: "-" porque Y en SVG crece hacia abajo
```

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
- [ ] **¿Gráficos auto-explicativos?** (leyendas, flechas, anotaciones cuando hay múltiples elementos)
- [ ] **¿Puntos marcados verificados matemáticamente?** (máximos, mínimos, intersecciones calculados correctamente)
- [ ] **¿Texto 100% visible?** (no cortado, no superpuesto)
- [ ] **¿Figuras geométricas fieles a su definición?** (sector ≠ segmento, etc.)
- [ ] ¿IDs únicos en todos los gráficos?
- [ ] ¿Wrapper estándar con fondo y bordes?

---

# 🔧 COMANDOS ÚTILES

```bash
# Desarrollo local
npm run dev

# Build de producción
npm run build

# === GraphSpec (gráficas de funciones y datos) ===
# Generar SVG de función
python3 scripts/functions/renderer.py \
  --spec specs/funciones/trigonometria/seno-principal.json \
  --output public/images/funciones/trigonometria/seno-principal.svg

# Generar con preview en navegador
python3 scripts/functions/renderer.py \
  --spec specs/funciones/ejemplo.json \
  --output public/images/funciones/ejemplo.svg \
  --preview

# === GeometrySpec (geometría exacta) ===
python3 scripts/geometry/renderer.py \
  --spec specs/geometria/triangulos/baricentro.json \
  --output public/images/geometria/ \
  --verify

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
9. **NUNCA usar LaTeX en títulos Markdown** (se ve mal en tabla de contenidos)
10. **Consultar tabla de renderers** para saber qué usar por tema

---

# 🎯 FLUJO DE EVALUACIÓN PEDAGÓGICA E ILUSTRACIONES

> Cuando el usuario pide "evaluación pedagógica e ilustraciones" para un tema, seguir este flujo:

## Paso 1: Leer las lecciones del tema
```bash
# Listar archivos del tema
ls src/content/matematicas/XX-capitulo/YY-tema/
# Leer cada .md para evaluar
```

## Paso 2: Evaluar pedagógicamente
| Aspecto | Verificar |
|---------|-----------|
| Ilustraciones | ¿Tiene al menos 1 por concepto? |
| Cheat Sheet | ¿Tabla resumen + ilustración juntos al inicio? |
| Títulos | ¿Sin LaTeX? |
| Progresión | ¿Simple → complejo? |
| Ejercicios | ¿Con soluciones en `<details>`? |

## Paso 3: Identificar renderer correcto
Consultar la **tabla "¿Qué Renderer Usar por Tema?"** más arriba.

## Paso 4: Generar specs e ilustraciones
```bash
# 1. Crear specs (si aplica) o usar renderer directo
# 2. Ejecutar renderer
# 3. Guardar en carpeta correcta de public/images/
```

## Paso 5: Actualizar archivos .md
```markdown
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b;">Título de la ilustración</strong>
  </div>

![Alt text](/images/carpeta/archivo.svg)

</div>
```

## Paso 6: Reportar resultados
- Número de ilustraciones creadas
- Archivos actualizados
- Mejoras pedagógicas aplicadas

---

# 📚 EJEMPLOS DE REFERENCIA

Para ver el estilo correcto de lecciones, revisar:
- `src/content/matematicas/01-aritmetica/05-proporcionalidad/03-regla-de-tres-simple.md`
- `/fisica/cinematica/mrua/lanzamiento-vertical`
- `/fisica/introduccion-a-la-fisica/introduccion/la-fisica-y-sus-ramas`

# SOLICITUD CONCRETA

La solicitud concreta que te voy a pedir con base en este contexto, está en la raíz de este proyecto, en PETICION.md