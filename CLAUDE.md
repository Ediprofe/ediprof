# 🎓 Ediprofe - Plataforma Educativa

> **Plataforma de contenido educativo para matemáticas y ciencias, generada con IA y validada pedagógicamente.**

---

## 🚨 LECTURA OBLIGATORIA PARA AGENTES NUEVOS

**Si eres un agente que llega por primera vez, lee esto:**

### 1. Sistema de Ilustraciones (Spec-First)
- **La IA NO dibuja directamente** → genera specs JSON
- **Python/SymPy renderiza** → cálculos exactos, SVG perfecto
- **Ver sección:** [🏛️ ARQUITECTURA DEL SISTEMA](#-arquitectura-del-sistema-crítico-para-agentes-nuevos)

### 2. Código Compartido (DRY)
- **NUNCA duplicar** colores, helpers, o constantes
- **SIEMPRE importar** de `scripts/geometry/core/`
- **Ver sección:** [🔧 MÓDULO CORE](#-módulo-core---utilidades-compartidas-para-renderers)

### 3. Extensibilidad
- **Nuevas funciones** → agregar a módulos existentes
- **Nuevos tipos** → crear spec + renderer
- **Nuevos dominios** → crear carpeta en `scripts/`
- **Ver sección:** [🚀 GUÍA: CREAR NUEVO TIPO DE ILUSTRACIÓN](#-guía-crear-nuevo-tipo-de-ilustración)

### 4. Documentación
- **TODO va en CLAUDE.md** → no crear READMEs separados
- **Workflows en** `.agent/workflows/` → para sistemas Spec

### 5. Protocolo de Clarificación (CRÍTICO)
- **Cuando NO tengas certeza** de lo que vas a hacer → **CONFIRMAR ANTES**
- **Para diagramas técnicos/visuales** → describir el plan y esperar aprobación
- **Ver sección:** [🔄 PROTOCOLO DE CLARIFICACIÓN](#-protocolo-de-clarificación-antes-de-ejecutar)

### Índice Rápido de Secciones Técnicas

| Sección | Línea | Contenido |
|---------|-------|-----------|
| Arquitectura del Sistema | ~406 | Diagrama de flujo, principios de diseño |
| Árbol de Decisión | ~507 | Qué tecnología usar para cada tipo |
| **Protocolo de Clarificación** | ~788 | Cuándo confirmar antes de ejecutar |
| Módulo Core | ~1110 | Colores, canvas, primitivas, SVGBuilder |
| Módulo Cartesian | ~1226 | 30 funciones de geometría analítica |
| Guía Nuevo Tipo | ~1320 | Paso a paso para extender el sistema |
| Reglas Críticas | ~1564 | NUNCA/SIEMPRE para extensibilidad |

---

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

# 🔄 FLUJO DE TRABAJO EN 5 ETAPAS

> **Referencia completa:** `.agent/workflows/content-generation.md`

| Etapa | Nombre | Responsable | Entregable |
|-------|--------|-------------|------------|
| 1 | Planeador Docente | Agente IA | Árbol de carpetas aprobado |
| 2 | Generador de Lecciones | Agente IA | Lecciones con **ASCII art** para ilustraciones |
| 3 | Generador de Ilustraciones | Agente IA | SVGs/Rough.js a partir del ASCII art |
| 4 | Evaluador Pedagógico | Agente IA | Lecciones corregidas + ilustraciones ajustadas |
| 5 | Evaluación Final | Humano | Aprobación definitiva |

---

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
- Estructura: Intro motivadora → Conceptos con ejemplos → Práctica
- **SIN gráficos SVG/Rough.js** (se agregan en Etapa 3)
- **Las ilustraciones se describen en ASCII art**
- Tablas y LaTeX SÍ permitidos

> 💡 **¿Por qué ASCII art?** Separa la creación de contenido pedagógico de la generación técnica de SVGs. Permite revisión rápida y facilita el trabajo de modelos menos avanzados.

---

## ETAPA 3: GENERADOR DE ILUSTRACIONES 🎨

**Objetivo:** Convertir ASCII art en SVGs/Rough.js de alta calidad.

**Qué hacer:**
1. Identificar todo ASCII art en las lecciones
2. Consultar el Árbol de Decisión para elegir tecnología
3. Generar specs JSON y ejecutar renderers
4. Reemplazar ASCII art con enlaces a SVG

> ⚠️ **REGLA OBLIGATORIA: MÍNIMO UNA ILUSTRACIÓN POR CONCEPTO**
> 
> Concepto = cada sección con título Markdown (##, ###)
> 
> **EXCEPCIÓN:** Sección de "Ejercicios de Práctica"

---

## ETAPA 4: EVALUADOR PEDAGÓGICO 🎓

**Objetivo:** Revisar con mentalidad del **mejor profesor** y corregir.

**Criterios de evaluación:**

| Aspecto | Pregunta clave |
|---------|----------------|
| Claridad | ¿Se entiende a la primera? |
| Progresión | ¿Simple → complejo? |
| Ejemplos | ¿Suficientes y paso a paso? |
| Visuales | ¿Hay mínimo 1 ilustración por concepto? |
| Motivación | ¿El estudiante sabe POR QUÉ? |
| **Auto-explicativo** | ¿La ilustración se entiende SIN leer el texto? |

**Acciones correctivas:**
- Reorganizar lecciones si el orden no es lógico
- Reescribir secciones poco claras
- Agregar ejemplos faltantes
- Corregir errores de contenido
- Ajustar/generar ilustraciones faltantes

---

## ETAPA 5: EVALUACIÓN FINAL DEL HUMANO ✅

**Objetivo:** Aprobación definitiva antes de publicar.

**El humano revisa:**
1. Precisión del contenido
2. Calidad pedagógica
3. Claridad visual
4. Experiencia de usuario
5. **APROBACIÓN para publicar**

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

## 📝 ESTRUCTURA ESTÁNDAR DE LECCIONES

> **OBLIGATORIO:** Toda lección debe seguir esta estructura para mantener consistencia.

### Plantilla de Lección

```markdown
# **Título de la Lección**

Breve párrafo introductorio (1-2 oraciones) que contextualiza el tema.

---

## 🎯 ¿Qué vas a aprender?

- Punto 1 (concepto principal)
- Punto 2
- Punto 3
- (máximo 4-5 puntos)

---

## 📖 Contenido Principal

(Secciones de contenido con ## y ###)

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Pregunta del ejercicio**

<details>
<summary>Ver solución</summary>

Respuesta detallada con explicación.

</details>

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Concepto 1** | Descripción breve |
| **Concepto 2** | Descripción breve |

> Conclusión breve destacando lo más importante.

---
```

### Reglas

| Sección | Obligatoria | Posición |
|---------|-------------|----------|
| 🎯 ¿Qué vas a aprender? | ✅ SÍ | Después del título e intro |
| 📝 Ejercicios de Práctica | ⚠️ Recomendado | Antes del resumen |
| 🔑 Resumen | ✅ SÍ | Al final (después de ejercicios) |

### Lecciones de Referencia

- [que-es-la-materia.mdx](file:///Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/src/content/quimica/01-la-materia/01-conceptos-basicos/01-que-es-la-materia.mdx)
- [la-fisica-y-sus-ramas.md](file:///Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/src/content/fisica/01-introduccion-a-la-fisica/01-introduccion/01-la-fisica-y-sus-ramas.md)
- [metodo-cientifico.md](file:///Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/src/content/fisica/01-introduccion-a-la-fisica/01-introduccion/02-metodo-cientifico.md)

---

## 🎨 CRITERIOS PEDAGÓGICOS PARA ILUSTRACIONES

> **Principio:** Cada ilustración debe ser como la que haría el mejor profesor del colegio en el pizarrón: clara, auto-explicativa y con alto valor didáctico.

### Regla de Oro: AUTO-EXPLICATIVA

Una ilustración es correcta si un estudiante puede entenderla **SIN leer el texto alrededor**.

| ✅ CORRECTO | ❌ INCORRECTO |
|-------------|---------------|
| Etiquetas claras: "ARCO MAYOR", "ARCO MENOR" | Solo colores sin explicación |
| Leyendas completas con fórmulas | "Ver texto para más detalles" |
| El ángulo α visible con su arco | Solo el símbolo α flotando |
| Fórmula destacada dentro del SVG | Fórmula solo en el markdown |

### Reglas Específicas por Tipo

#### Para Ángulos:
```
✅ El arco del ángulo (α, θ, β) SIEMPRE visible dentro de la abertura
✅ Etiqueta del ángulo pegada al arco, dentro de la abertura
✅ Si hay varios ángulos, usar colores distintos con leyenda
```

#### Para Fórmulas de Área:
```
✅ Si la fórmula tiene componentes (ej: Segmento = Sector - Triángulo),
   mostrar VISUALMENTE cada componente
✅ El triángulo debe ser visible cuando se menciona "área del triángulo"
✅ Usar colores para diferenciar: sector (amarillo), triángulo (rojo), resultado (verde)
```

#### Para Arcos:
```
✅ Si se menciona "arco mayor" y "arco menor", AMBOS deben tener etiquetas
✅ Usar colores distintos para mayor (naranja) y menor (amarillo)
✅ Las etiquetas deben ser cajas visibles, no solo texto pequeño
```

### Ejemplo de Verificación

Antes de dar por terminada una ilustración, preguntar:

1. ¿Un estudiante de 15 años entendería esto sin explicación adicional?
2. ¿Todos los elementos mencionados en la fórmula están dibujados?
3. ¿Las etiquetas son legibles y están bien posicionadas?
4. ¿Los colores distinguen claramente cada elemento?
5. ¿El ángulo/arco/área que quiero mostrar es el protagonista visual?

---

## 📐 ESTÁNDARES TÉCNICOS PARA SVGs

> **Principio:** Todos los SVGs deben tener tamaños consistentes para una experiencia visual uniforme.

### Tamaños Estándar de viewBox

| Tipo de Ilustración | viewBox | Uso |
|---------------------|---------|-----|
| **Simple** (1 concepto) | `0 0 500 400` | Radio, diámetro, cuerda, arco, ángulo simple |
| **Compuesto** (2-3 elementos) | `0 0 600 460` | Sector+triángulo, teoremas con comparación (altura extra para leyendas) |
| **Múltiple** (4+ elementos) | `0 0 750 450` | Posiciones de circunferencias, comparaciones múltiples |
| **Horizontal** (lado a lado) | `0 0 750 420` | Operaciones A - B = C, antes/después (ancho extra para 3 elementos) |

### Regla de Consistencia

```
⚠️ CRÍTICO: Todas las ilustraciones de un mismo tema deben usar 
el MISMO tamaño de viewBox para verse consistentes en la página.
```

**Ejemplo para Elementos de la Circunferencia:**
- Radio, Diámetro, Cuerda, Arco → Todos `0 0 500 400`
- Sector, Segmento, Corona → Todos `0 0 500 400`

### Regla de Centrado

```
⚠️ CRÍTICO: El contenido debe estar CENTRADO en el viewBox.
Para un viewBox de 500px de ancho, el centro del círculo debe estar en cx=250.
```

### Constantes en el Renderer

```python
# En circle_renderer.py:
SIZE_SIMPLE = (500, 400)       # 1 concepto
SIZE_COMPOUND = (600, 460)     # 2-3 elementos (altura extra para leyendas)
SIZE_MULTIPLE = (750, 450)     # 4+ elementos
SIZE_HORIZONTAL = (750, 420)   # Operaciones lado a lado
```

### Verificación de Carga

Antes de considerar un SVG terminado:
1. ✅ El archivo existe en `public/images/...`
2. ✅ La ruta en markdown es EXACTA (case-sensitive)
3. ✅ El SVG tiene contenido válido (no vacío)
4. ✅ El viewBox está definido correctamente

---

## 🤖 CHECKLIST PARA AGENTE IA: Generación de SVGs

> **INSTRUCCIÓN:** Cuando se pida "genera las ilustraciones para esta lección", seguir este checklist:

### Método RECOMENDADO: CircleSpec (JSON → SVG)

> **Referencia completa:** `.agent/workflows/circle-spec.md`

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  IA genera   │────▶│ Python/SymPy │────▶│    SVG       │
│ CircleSpec   │     │   calcula    │     │   exacto     │
│   (JSON)     │     │ y valida     │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
```

### Paso 1: Crear spec JSON
```json
{
  "tipo": "elemento-radio",
  "titulo": "Radio",
  "canvas": "simple",
  "elemento": { "angulo": 45, "color": "#ef4444" },
  "leyenda": { "texto": "Segmento del centro a la circunferencia" }
}
```

Guardar en: `specs/geometria/circulos/NOMBRE.json`

### Paso 2: Generar SVG desde spec
```bash
python3 scripts/geometry/circle_spec_renderer.py \
  --spec specs/geometria/circulos/NOMBRE.json \
  --output public/images/geometria/circulos/NOMBRE.svg
```

### Paso 3: Verificar el SVG generado
```
□ El archivo existe en public/images/...
□ El SVG tiene contenido (no está vacío)
□ Abrir directamente en navegador: http://localhost:4321/images/geometria/circulos/NOMBRE.svg
□ No hay errores de parsing XML
```

### Paso 4: Insertar en el markdown
```markdown
![Descripción](/images/geometria/circulos/nombre.svg)
```

### Método LEGACY: circle_renderer.py (funciones hardcodeadas)

Para ilustraciones ya existentes:
```bash
python3 scripts/geometry/circle_renderer.py --type TIPO --output public/images/geometria/circulos/NOMBRE.svg
```

### Garantías Automáticas del Renderer
- ✅ Caracteres `<`, `>`, `&` se escapan automáticamente
- ✅ Centrado correcto (cx = width/2)
- ✅ viewBox consistente según tipo de ilustración
- ✅ Paleta de colores estandarizada
- ✅ Cálculos exactos con SymPy

---

## Filosofía Anti-Abrumamiento

> **PRINCIPIO:** El estudiante no debe ver mucho texto antes de entender visualmente qué va a aprender.

### Reglas:
1. **Cheat Sheet + Ilustración JUNTOS al inicio:** Tabla resumen + gráfico visual = combo ganador
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

## �️ ARQUITECTURA DEL SISTEMA (CRÍTICO PARA AGENTES NUEVOS)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        FLUJO DE GENERACIÓN DE SVG                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐           │
│   │   AGENTE IA  │────▶│    SPEC      │────▶│   RENDERER   │           │
│   │  (describe)  │     │   (JSON)     │     │   (Python)   │           │
│   └──────────────┘     └──────────────┘     └──────────────┘           │
│          │                    │                    │                    │
│          │                    │                    ▼                    │
│          │                    │            ┌──────────────┐             │
│          │                    │            │     SVG      │             │
│          │                    │            │   (output)   │             │
│          │                    │            └──────────────┘             │
│          │                    │                    │                    │
│          │                    ▼                    │                    │
│          │         specs/geometria/...             │                    │
│          │         specs/fisica/...                │                    │
│          │         specs/quimica/...               │                    │
│          │                                         ▼                    │
│          │                              public/images/...               │
│          │                                                              │
│          ▼                                                              │
│   ┌──────────────────────────────────────────────────────────────┐     │
│   │                    MÓDULOS COMPARTIDOS                        │     │
│   │  ┌─────────────────────────────────────────────────────────┐ │     │
│   │  │ scripts/geometry/core/                                   │ │     │
│   │  │   ├── colors.py      ← PALETA ÚNICA (NUNCA duplicar)    │ │     │
│   │  │   ├── canvas.py      ← TAMAÑOS ESTÁNDAR                 │ │     │
│   │  │   ├── primitives.py  ← HELPERS (escape_xml, etc.)       │ │     │
│   │  │   ├── svg_builder.py ← API FLUIDA PARA SVG              │ │     │
│   │  │   └── coordinate_system.py ← TRANSFORMACIÓN COORDS      │ │     │
│   │  └─────────────────────────────────────────────────────────┘ │     │
│   └──────────────────────────────────────────────────────────────┘     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Principios de Diseño (OBLIGATORIOS)

| Principio | Descripción | Ejemplo |
|-----------|-------------|---------|
| **Spec-First** | La IA genera JSON, el renderer dibuja | `specs/geometria/circulos/radio.json` |
| **DRY** | No duplicar código, usar `core/` | `from core import COLORS` |
| **Modular** | Archivos ≤ 300 líneas | `cartesian/points.py`, `cartesian/lines.py` |
| **Extensible** | Nuevos tipos = nuevos módulos | `scripts/chemistry/` para química |
| **Documentado** | Todo en `CLAUDE.md`, no READMEs separados | Esta sección |

### Estructura de Carpetas para Ilustraciones

```
scripts/
├── geometry/                    # ← DOMINIO: Geometría
│   ├── core/                    # Utilidades compartidas (NUNCA duplicar)
│   │   ├── colors.py
│   │   ├── canvas.py
│   │   ├── primitives.py
│   │   ├── svg_builder.py
│   │   └── coordinate_system.py
│   ├── cartesian/               # Submódulo: Geometría analítica
│   │   ├── points.py
│   │   ├── slopes.py
│   │   ├── lines.py
│   │   ├── circles.py
│   │   └── parabolas.py
│   ├── circle_renderer.py       # Renderer para circunferencias
│   ├── circle_spec_renderer.py  # Renderer basado en specs
│   └── renderer.py              # Renderer para triángulos
│
├── physics/                     # ← DOMINIO FUTURO: Física
│   ├── core/                    # (puede importar de geometry/core)
│   ├── mechanics/               # Cinemática, dinámica
│   └── waves/                   # Ondas, óptica
│
└── chemistry/                   # ← DOMINIO FUTURO: Química
    ├── core/
    ├── atoms/                   # Modelos atómicos
    └── molecules/               # Estructuras moleculares

specs/
├── geometria/
│   ├── circulos/                # Specs para circunferencias
│   ├── triangulos/              # Specs para triángulos
│   └── analitica/               # Specs para geometría analítica
├── fisica/                      # ← FUTURO
└── quimica/                     # ← FUTURO

public/images/
├── geometria/
│   ├── circulos/                # SVGs generados
│   ├── triangulos/
│   └── analitica/
├── fisica/                      # ← FUTURO
└── quimica/                     # ← FUTURO
```

### 🏷️ Convención de Prefijos para Imágenes

> **Regla:** Usar prefijos en los nombres de archivo para identificar el origen de la imagen.

| Origen | Prefijo | Formato | Ejemplo |
|--------|---------|---------|---------|
| **Tablet** (dibujos manuales) | `t-` | PNG/WebP | `t-cambios-de-fase.png` |
| **SVG generado** (renderers) | (sin prefijo) | SVG | `diagrama-moeller.svg` |
| **3D renders** | `3d-` | PNG | `3d-orbital-s.png` |

#### Reglas Específicas

```
✅ TABLET (prefijo t-):
   • Ilustraciones dibujadas manualmente en tablet
   • Formato: PNG (original) o WebP (optimizado)
   • Ruta: public/images/{materia}/t-nombre.png
   • Ejemplo: /images/quimica/t-ciclo-agua.png

✅ SVG GENERADO (sin prefijo):
   • SVGs creados por renderers Python
   • Mantiene la convención existente
   • Ejemplo: /images/geometria/circulos/radio.svg

✅ 3D RENDERS (prefijo 3d-):
   • Imágenes 3D pre-renderizadas
   • Formato: PNG con transparencia
   • Ejemplo: /images/quimica/3d-orbital-p.png
```

### 📱 Workflow: Imágenes de Tablet (MDX + Astro Image)

> **Optimización automática:** Astro convierte PNG → WebP (~75% reducción) al hacer build.

#### Flujo de Trabajo Paso a Paso

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    FLUJO: IMAGEN DE TABLET → WEB                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  1️⃣ DIBUJAR                                                            │
│     └─→ En tu tablet, creas la ilustración                             │
│                                                                         │
│  2️⃣ EXPORTAR                                                           │
│     └─→ Guardas como PNG                                               │
│                                                                         │
│  3️⃣ NOMBRAR CON PREFIJO                                                │
│     └─→ t-nombre-descriptivo.png                                       │
│         Ejemplo: t-cambios-de-fase.png                                 │
│                                                                         │
│  4️⃣ UBICAR EN CARPETA                                                  │
│     └─→ public/images/{materia}/t-nombre.png                           │
│         Ejemplo: public/images/quimica/t-cambios-de-fase.png           │
│                                                                         │
│  5️⃣ CONVERTIR ARCHIVO A MDX                                            │
│     └─→ Renombrar: leccion.md → leccion.mdx                            │
│                                                                         │
│  6️⃣ AGREGAR IMPORTS AL INICIO                                          │
│     └─→ import { Image } from 'astro:assets';                          │
│         import nombreVar from '/public/images/.../t-nombre.png';       │
│                                                                         │
│  7️⃣ USAR COMPONENTE IMAGE                                              │
│     └─→ <Image src={nombreVar} alt="..." format="webp" />              │
│                                                                         │
│  8️⃣ BUILD/DEPLOY                                                       │
│     └─→ Astro optimiza automáticamente: PNG → WebP                     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Cuándo usar `.md` vs `.mdx`

| Contenido del archivo | Formato |
|-----------------------|---------|
| Solo texto, LaTeX, tablas, SVGs | `.md` |
| Tiene al menos 1 imagen de tablet | `.mdx` |

#### Ejemplo Completo de Archivo `.mdx`

```mdx
import { Image } from 'astro:assets';
import cambiosFase from '/public/images/quimica/t-cambios-de-fase.png';
import estadosMateria from '/public/images/quimica/t-estados-materia.png';

# Título de la Lección

Contenido normal en markdown...

## Sección con imagen

<Image src={cambiosFase} alt="Diagrama de cambios de fase" format="webp" />

## Otra sección

Más contenido...

<Image src={estadosMateria} alt="Estados de la materia" format="webp" />
```

#### Reglas

| ✅ SIEMPRE | ❌ NUNCA |
|-----------|----------|
| Archivo `.mdx` si tiene imagen de tablet | Usar `![alt](url)` para imágenes de tablet |
| Import al inicio, antes del contenido | Olvidar `format="webp"` |
| Prefijo `t-` en el nombre del PNG | Mezclar rutas hardcodeadas con imports |
| Nombre de variable en camelCase | Usar mayúsculas en nombres de archivo |
| Alt text descriptivo | |

#### IDE: Extensión requerida

Para syntax highlighting de archivos `.mdx` en VS Code:
```bash
code --install-extension unifiedjs.vscode-mdx
```

---

### 🗺️ Sistema MindMap Spec (Mapas Conceptuales)

> **Mapas conceptuales como SVG estático** - 0 JS, 100% responsive.

#### Arquitectura

```
specs/mindmap/*.json  →  Python Renderer  →  public/images/mindmap/*.svg
```

#### Comando de generación

```bash
python3 scripts/mindmap/mindmap_renderer.py \
  --spec specs/mindmap/nombre.json \
  --output public/images/mindmap/nombre.svg
```

#### Formato de Spec JSON

```json
{
  "tipo": "mindmap",
  "estilo": "profesional-dark",
  "nodo_central": {
    "texto": "TEMA PRINCIPAL",
    "icono": "🔬"
  },
  "ramas": [
    {
      "texto": "Rama 1",
      "icono": "🏛️",
      "color": "#3b82f6",
      "hijos": ["Hijo 1", "Hijo 2", "Hijo 3"]
    }
  ]
}
```

#### Estilos disponibles

| Estilo | Descripción |
|--------|-------------|
| `profesional-dark` | Fondo oscuro, nodos con bordes (default) |
| `profesional-light` | Fondo blanco, sombras sutiles |
| `pizarra` | Estilo dibujado a mano |
| `minimalista` | Líneas y texto simple |

#### En el markdown

```markdown
![Mapa conceptual](/images/mindmap/nombre.svg)
```

---

## 🌳 Árbol de Decisión

> ⚠️ **TRES TECNOLOGÍAS PARA ILUSTRACIONES: SVG, Rough.js y JSXGraph**

```
¿QUÉ TIPO DE ILUSTRACIÓN NECESITO?
│
├─── 📐 ¿Es GEOMETRÍA con propiedades exactas?
│    │   (circunferencias, triángulos, geometría analítica)
│    │
│    └─── SÍ → SVG ESTÁTICO (Python/SymPy → SVG)
│         • Circunferencias: radio, cuerda, arco, sector
│         • Triángulos: puntos notables, alturas, medianas
│         • Geometría analítica: plano cartesiano, rectas
│         • Gráficas de funciones: parábolas, rectas, exponenciales
│         📁 Ver: .agent/workflows/circle-spec.md
│         📁 Ver: .agent/workflows/geometry-exact.md
│         📁 Ver: .agent/workflows/cartesian-spec.md
│
├─── 🎮 ¿Necesita INTERACTIVIDAD (arrastrar, animar)?
│    │   (simulaciones, demostraciones manipulables)
│    │
│    └─── SÍ → JSXGRAPH (inline en .md)
│         • Vectores interactivos (arrastrar para ver cambios)
│         • Simulaciones de física (MRU, MRUA, caída libre)
│         • Geometría dinámica (mover puntos, ver propiedades)
│         • Demostraciones de teoremas
│         📁 Ver: documentación JSXGraph
│
├─── ✏️ ¿Es un DIAGRAMA ilustrativo/conceptual?
│    │   (situaciones físicas estáticas, modelos, procesos)
│    │
│    └─── SÍ → ROUGH.JS (inline en .md)
│         • Situaciones físicas (bloques, poleas, planos)
│         • Modelos atómicos, partículas, estados de materia
│         • Equipos de laboratorio, procesos químicos
│         • Mapas conceptuales, organigramas, ciclos
│         • Transformaciones geométricas (traslación, rotación)
│         • Fracciones visuales (círculos divididos)
│         📁 Ver: .agent/workflows/roughjs.md
│
└─── 📝 ¿Es solo una FÓRMULA?
     └─── SÍ → LATEX (inline en .md)
          • $inline$ o $$bloque$$
```

### Resumen de Tecnologías

| Tecnología | Uso | Tamaño JS |
|------------|-----|-----------|
| **SVG estático** | Geometría exacta, gráficas | **0 KB** ⭐ |
| **Rough.js** | Diagramas conceptuales | ~50KB |
| **JSXGraph** | Simulaciones interactivas | ~600KB |
| ~~ECharts~~ | ❌ ELIMINADO | ~~1MB~~ |
| ~~Chart.js~~ | ❌ ELIMINADO | ~~200KB~~ |
| ~~Three.js~~ | ❌ ELIMINADO | ~~500KB~~ |

---

## Matriz de Decisión Rápida

| Necesito... | Uso... | Tipo |
|-------------|--------|------|
| Gráfica de función $f(x)$ | **SVG** (CartesianSpec) | Estático |
| Radio, cuerda, arco de círculo | **SVG** (CircleSpec) | Estático |
| Ángulo inscrito/central | **SVG** (CircleSpec) | Estático |
| Baricentro de triángulo | **SVG** (GeometrySpec) | Estático |
| Circuncentro exacto | **SVG** (GeometrySpec) | Estático |
| Plano cartesiano con puntos | **SVG** (CartesianSpec) | Estático |
| Distancia entre puntos | **SVG** (CartesianSpec) | Estático |
| Punto medio, división segmento | **SVG** (CartesianSpec) | Estático |
| Área de polígonos (coordenadas) | **SVG** (CartesianSpec) | Estático |
| Traslación de figura | **Rough.js** | Dinámico |
| Rotación/Reflexión | **Rough.js** | Dinámico |
| Homotecia (ampliación) | **Rough.js** | Dinámico |
| Bloque en plano inclinado | **Rough.js** | Dinámico |
| Modelo atómico de Bohr | **Rough.js** | Dinámico |
| Fracción 3/4 visual | **Rough.js** | Dinámico |
| Estados de la materia | **Rough.js** | Dinámico |
| Equipos de laboratorio | **Rough.js** | Dinámico |

### ⚠️ Cuándo usar SymPy (para SVGs)

| Situación | ¿Usar SymPy? | Razón |
|-----------|--------------|-------|
| Puntos notables de triángulo | ✅ SÍ | Cálculos de intersección exactos |
| Tangentes a circunferencia | ✅ SÍ | Cálculos trigonométricos exactos |
| Gráficas de funciones | ✅ SÍ | Curvas matemáticamente exactas |
| Traslación de figura | ❌ NO | Fórmula directa → Rough.js |
| Rotación de figura | ❌ NO | Fórmula directa → Rough.js |
| Reflexión | ❌ NO | Fórmula directa → Rough.js |
| Homotecia | ❌ NO | Fórmula directa → Rough.js |

---

## 🚨 Reglas Críticas para Ilustraciones

### Para Circunferencias (CircleSpec)

```
✅ OBLIGATORIO:
   1. Crear spec JSON en specs/geometria/circulos/
   2. Ejecutar: python3 scripts/geometry/circle_spec_renderer.py --spec [archivo] --output [svg]
   3. Enlazar SVG: ![Alt](/images/geometria/circulos/...)

📁 Referencia: .agent/workflows/circle-spec.md
```

### Para Triángulos (GeometrySpec)

```
✅ OBLIGATORIO:
   1. Crear spec JSON en specs/geometria/triangulos/
   2. Ejecutar: python3 scripts/geometry/renderer.py --spec [archivo] --verify
   3. Enlazar SVG: ![Alt](/images/geometria/triangulos/...)

📁 Referencia: .agent/workflows/geometry-exact.md
```

### Para Transformaciones Geométricas

```
✅ RECOMENDADO: Rough.js inline
   • Mostrar figura ORIGINAL (azul) e IMAGEN (verde)
   • Incluir correspondencia de puntos: A → A', B → B'
   • Mostrar elemento de transformación: vector, centro, eje
   • SymPy NO es necesario (fórmulas directas)

📁 Referencia: .agent/workflows/roughjs.md
```

### ❌ PROHIBIDO en Geometría

```
❌ NUNCA:
   • Escribir JSXGraph con coordenadas "a ojo"
   • Usar funciones JSXGraph: circumcenter, incircle, incenter
   • Hardcodear coordenadas sin cálculo matemático
   • Generar SVG sin usar los renderers oficiales
```

### Para Ángulos en SVG (CRÍTICO)

> ⚠️ **PROBLEMA COMÚN:** Los arcos de ángulos quedan mal posicionados.

**Reglas para dibujar ángulos correctamente:**

1. **El arco del ángulo debe estar ENTRE los dos lados**, no fuera de ellos
2. **Calcular matemáticamente** los puntos de inicio y fin del arco:
   - El arco inicia en la dirección del primer lado
   - El arco termina en la dirección del segundo lado
   - El radio del arco es pequeño (20-40px típicamente)

3. **La etiqueta (θ, α, β) debe estar:**
   - DENTRO de la abertura del ángulo
   - A una distancia ligeramente mayor que el arco
   - Centrada en la bisectriz del ángulo

**Ejemplo de cálculo correcto:**
```python
# Para un ángulo en el punto O con lados hacia A y B:
import math

# Ángulos de los lados respecto al eje X
angle_OA = math.atan2(A.y - O.y, A.x - O.x)
angle_OB = math.atan2(B.y - O.y, B.x - O.x)

# Puntos del arco (radio = 30)
arc_start_x = O.x + 30 * math.cos(angle_OA)
arc_start_y = O.y + 30 * math.sin(angle_OA)
arc_end_x = O.x + 30 * math.cos(angle_OB)
arc_end_y = O.y + 30 * math.sin(angle_OB)

# Etiqueta en la bisectriz (radio = 45)
bisector_angle = (angle_OA + angle_OB) / 2
label_x = O.x + 45 * math.cos(bisector_angle)
label_y = O.y + 45 * math.sin(bisector_angle)
```

4. **Verificar visualmente** que:
   - El arco está en la "abertura" del ángulo
   - La etiqueta es legible y no se superpone con otros elementos
   - El ángulo se ve como lo dibujaría un profesor en el pizarrón

### Para Rough.js (Diagramas Conceptuales)

```
✅ SIEMPRE:
   • Usar patrón ES module: import rough from 'https://...'
   • Usar wrapper con fondo y bordes redondeados
   • ID únicos: rough-leccion-numero
   • CENTRAR contenedores: margin: 0 auto
   • Canvas responsive: width="800" + style="width: 100%"

❌ NUNCA:
   • Usar Rough.js para geometría que requiere exactitud matemática
   • Contenedores con max-width sin centrar
```

📁 Referencia: .agent/workflows/roughjs.md

---

# 🔄 PROTOCOLO DE CLARIFICACIÓN (ANTES DE EJECUTAR)

> **REGLA CRÍTICA:** Cuando NO tengas certeza absoluta sobre qué vas a hacer, **CONFIRMA ANTES de ejecutar**.

## ⚠️ Situaciones que Requieren Clarificación

| Situación | Acción Requerida |
|-----------|------------------|
| El usuario da una **referencia visual** (imagen) | Describir lo que ves y confirmar interpretación |
| Solicitud de **diagrama técnico/científico** | Proponer estructura y esperar aprobación |
| Solicitud **ambigua** o con múltiples interpretaciones | Hacer preguntas específicas |
| **Primera vez** que haces algo de ese tipo | Proponer plan y esperar confirmación |
| Hay **coordenadas, medidas o geometría exacta** | Explicar cálculos antes de ejecutar |

## 📋 Protocolo de 3 Pasos para Diagramas Técnicos

### Paso 1: ANALIZAR la referencia
```
"Veo en tu imagen:
- [Descripción elemento 1]
- [Descripción elemento 2]
- [Descripción posicionamiento/relaciones]

¿Es correcta mi interpretación?"
```

### Paso 2: PROPONER estructura
```
"Mi plan es:
1. [Acción 1 con coordenadas específicas si aplica]
2. [Acción 2]
3. [Acción 3]

¿Procedo?"
```

### Paso 3: EJECUTAR solo con aprobación
- Solo ejecutar después de confirmación
- Una sola iteración = éxito

## 🚫 Errores a Evitar (Aprendidos de Experiencia)

| ❌ Error | ✅ Correcto |
|---------|-------------|
| Empezar a codificar basándose en mi interpretación | Describir interpretación y pedir confirmación |
| "Las flechas van diagonalmente" (vago) | "Flecha 1 entra en (x1,y1), sale en (x2,y2), atravesando bloques A, B, C" |
| Iterar 4+ veces hasta acertar | Confirmar 1 vez, ejecutar 1 vez |
| Usar `generate_image` para diagramas técnicos | Usar SVG manual o Python/Matplotlib |

## 💡 Frases Útiles para Clarificación

```
"Antes de proceder, quiero confirmar mi entendimiento..."
"¿Podrías verificar si mi interpretación es correcta?"
"Mi plan detallado es... ¿Procedo?"
"¿Hay algo que deba ajustar antes de ejecutar?"
```

## 📊 Caso de Estudio: Diagrama de Moeller

**Problema:** Se iteró 4 veces para un diagrama que debió hacerse bien la primera vez.

**Causa raíz:** El agente interpretó "flechas diagonales" sin confirmar:
- Las flechas atraviesan bloques específicos
- Cada flecha va de vértice superior-derecho a inferior-izquierdo
- Las coordenadas son críticas

**Solución correcta:** Antes de escribir código:
1. "Veo flechas que atraviesan los bloques 1s, 2s, 2p→3s, etc."
2. "Cada flecha entra por esquina superior-derecha y sale por inferior-izquierda"
3. "¿Es correcta mi interpretación? ¿Procedo?"

---

# 📝 FORMATO TÉCNICO

## LaTeX - Reglas de Formato Visual

### Fórmulas Importantes = Bloque con Espacio

> **REGLA:** Las expresiones matemáticas importantes deben lucir BONITAS y destacadas.

**✅ CORRECTO (vistoso, con espacio):**
```markdown
La fórmula del área es:

$$
A = \pi r^2
$$

Donde $r$ es el radio.
```

**❌ INCORRECTO (comprimido, poco vistoso):**
```markdown
La fórmula del área es: $$A = \pi r^2$$ donde $r$ es el radio.
```

### Cuándo Usar Bloque vs Inline

| Situación | Usar | Ejemplo |
|-----------|------|---------|
| Fórmula principal del concepto | Bloque `$$` con líneas vacías | Teoremas, definiciones |
| Resultado final de un ejemplo | Bloque con `\boxed{}` | `$$\boxed{x = 5}$$` |
| Variable mencionada en texto | Inline `$` | "donde $x$ es..." |
| Fórmula secundaria/auxiliar | Inline `$` | "sabemos que $a + b = c$" |

### Resultados con Recuadro

```markdown
Resultado:

$$
\boxed{x = 5}
$$
```

### Restricciones de LaTeX

| ❌ NO hacer | ✅ Alternativa |
|-------------|----------------|
| LaTeX en títulos de secciones | Usar texto plano o Unicode |
| `\[...\]` o `\(...\)` | Usar `$$...$$` o `$...$` |
| Símbolos de moneda `$` solos | Usar `USD`, `COP`, o `\$` |
| `$$formula$$` en una línea | Dejar línea vacía antes y después |

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

## Contenedores de Ilustraciones - RESPONSIVOS

> ⚠️ **REGLA CRÍTICA:** Usar `width: 100%` en lugar de `max-width` fijo para SVGs.

### Por qué NO usar max-width fijo

El problema con `max-width: 500px` es que:
1. Si el SVG tiene viewBox más ancho (ej: 750px), se comprime y deja espacio en blanco
2. No se adapta a diferentes tamaños de pantalla
3. Requiere conocer el tamaño exacto del SVG al escribir el markdown

### Wrapper Correcto (RESPONSIVO)

```html
<!-- ✅ CORRECTO: width 100% + box-sizing -->
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">

<!-- ❌ INCORRECTO: max-width fijo que no coincide con el SVG -->
<div style="background: #f1f5f9; max-width: 500px;">
```

### Cuándo usar max-width (casos especiales)

Solo usar `max-width` cuando el SVG es pequeño y no debe crecer demasiado:

| Tipo de SVG | viewBox | Contenedor |
|-------------|---------|------------|
| Simple (1 concepto) | 500x400 | `width: 100%` o `max-width: 550px` |
| Compuesto (2-3 elementos) | 600x460 | `width: 100%` |
| Horizontal (A - B = C) | 750x420 | `width: 100%` (NUNCA max-width pequeño) |
| Múltiple (4+ elementos) | 750x450 | `width: 100%` |

## ✅ USAR (funcionan en ambos modos)

### 1. Markdown Nativo
Blockquotes (`>`), tablas, listas, LaTeX, enlaces

### 2. Canvas (Rough.js)
Controla sus propios colores

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

## Wrapper Estándar para Gráficos (RESPONSIVO)

```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Título</strong>
  </div>
  <img src="/images/ruta/imagen.svg" alt="Descripción" style="width: 100%; height: auto;" />
</div>
```

> ⚠️ **CRÍTICO:** Dentro de bloques HTML (`<div>`), usar `<img>` en lugar de `![]()`
> 
> El markdown `![alt](src)` NO se procesa dentro de etiquetas HTML en Astro.
> Siempre usar: `<img src="..." alt="..." style="width: 100%; height: auto;" />`

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
| Arcos de ángulos | Naranja | `#f97316` |

## Por Materia

> **Fuente de verdad:** `src/config/materias.ts`

| Materia | Color | Hex |
|---------|-------|-----|
| Matemáticas | Rojo | `#ef4444` |
| Física | Azul | `#3b82f6` |
| Química | Naranja | `#ea580c` |
| Ciencias | Verde | `#22c55e` |

---

# 📁 DOCUMENTACIÓN DE WORKFLOWS

| Archivo | Contenido |
|---------|-----------|
| `.agent/workflows/content-generation.md` | **Flujo de 5 etapas para lecciones** |
| `.agent/workflows/circle-spec.md` | CircleSpec: circunferencias (SymPy) |
| `.agent/workflows/geometry-exact.md` | GeometrySpec: triángulos (SymPy) |
| `.agent/workflows/cartesian-spec.md` | CartesianSpec: geometría analítica |
| `.agent/workflows/chemistry-spec.md` | **ChemistrySpec: tabla periódica, tendencias** |
| `.agent/workflows/graphspec.md` | Gráficas de funciones |
| `.agent/workflows/roughjs.md` | Diagramas ilustrativos, transformaciones |
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
- [ ] ¿Las fórmulas importantes están en bloque `$$` con líneas vacías?

## Ilustraciones (Etapa 3)
- [ ] ¿Mínimo 1 ilustración por concepto (excepto ejercicios)?
- [ ] ¿Tecnología correcta según árbol de decisión?
- [ ] ¿Las tarjetas HTML funcionan en modo oscuro?
- [ ] ¿Las ilustraciones son claras como un dibujo de pizarra?
- [ ] ¿IDs únicos en todos los gráficos?
- [ ] ¿Contenedores CENTRADOS con `margin: 0 auto`?
- [ ] ¿Los ángulos tienen arcos BIEN POSICIONADOS (dentro de la abertura)?
- [ ] ¿Las etiquetas de ángulos (α, θ, β) están DENTRO del ángulo?

## 🎯 Validación de Ángulos en SVGs (CRÍTICO)

> **Regla de Oro:** El arco de un ángulo SIEMPRE debe estar ENTRE los dos lados del ángulo, en la abertura.

### Metodología Correcta: `get_angle_arc_svg()`

```python
# CORRECTO: Usar las posiciones REALES de los puntos
arc_data = get_angle_arc_svg(
    vertex=(px, py),     # El vértice del ángulo
    point1=(ax, ay),     # Punto que define un lado
    point2=(bx, by),     # Punto que define el otro lado
    radius=30            # Radio del arco
)

# La función calcula automáticamente:
# 1. Los ángulos reales respecto al vértice
# 2. El camino más corto (ángulo menor)
# 3. La posición óptima de la etiqueta
```

### Checklist de Validación

| Verificar | Descripción |
|-----------|-------------|
| ✅ Arco dentro de abertura | El arco debe curvarse HACIA ADENTRO del ángulo |
| ✅ Radio pequeño | 25-40px para que sea visible pero no intrusivo |
| ✅ Etiqueta visible | α, θ, β dentro del ángulo, sin superposiciones |
| ✅ Dirección correcta | El arco debe ir del lado 1 al lado 2 por el camino corto |

### ❌ Error Común: Usar ángulos abstractos

```python
# INCORRECTO: Ángulos hardcodeados que no corresponden a los puntos
arc = angle_arc_path(cx, cy, 35, 90, 180)  # ¿Por qué 90° y 180°?

# CORRECTO: Calcular desde las posiciones reales
arc_data = get_angle_arc_svg(vertex, point1, point2, 35)
```

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

## 📄 Exportar a Word (DOCX)

```bash
# Una lección individual
bash scripts/export-to-docx.sh \
  src/content/fisica/01-introduccion-a-la-fisica/01-introduccion/01-la-fisica-y-sus-ramas.md \
  -o ~/Desktop/leccion.docx

# Múltiples lecciones en un solo documento
bash scripts/export-to-docx.sh \
  src/content/fisica/01-introduccion-a-la-fisica/01-introduccion/01-la-fisica-y-sus-ramas.md \
  src/content/fisica/01-introduccion-a-la-fisica/01-introduccion/02-metodo-cientifico.md \
  src/content/fisica/01-introduccion-a-la-fisica/01-introduccion/03-medicion-y-cantidades-fisicas.md \
  -o ~/Desktop/guia-completa.docx

# Sin imágenes (solo texto)
bash scripts/export-to-docx.sh archivo.md -o salida.docx --no-images
```

## 📕 Exportar a PDF

> **Requisito:** El servidor de desarrollo debe estar corriendo (`npm run dev`)

```bash
# PDF de una lección individual
node scripts/export-to-pdf.mjs \
  --lesson fisica/introduccion-a-la-fisica/introduccion/la-fisica-y-sus-ramas \
  --output ~/Desktop/leccion.pdf

# PDF de un tema completo (todas las lecciones combinadas)
node scripts/export-to-pdf.mjs \
  --tema fisica/introduccion-a-la-fisica/introduccion \
  --output ~/Desktop/guia-introduccion-fisica.pdf

# Si el servidor corre en otro puerto (ej: 4322)
BASE_URL=http://localhost:4322 node scripts/export-to-pdf.mjs \
  --tema fisica/introduccion-a-la-fisica/introduccion \
  --output ~/Desktop/guia.pdf
```

### Rutas de impresión

| Tipo | Ruta | Descripción |
|------|------|-------------|
| Lección | `/print/{materia}/{slug-leccion}` | Una lección con encabezado |
| Tema | `/print-tema/{materia}/{unidad}/{tema}` | Tema completo con portada e índice |

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
9. **Fórmulas bonitas:** Bloques `$$` con líneas vacías antes y después
10. **Centrar siempre** los contenedores de ilustraciones
11. **Verificar ángulos:** Arco DENTRO de la abertura, etiqueta visible

---

# 🐛 ERRORES CONOCIDOS Y SOLUCIONES

## Error: Ángulo mal posicionado en SVG

**Síntoma:** El arco del ángulo aparece fuera de la abertura entre los lados.

**Causa:** Los puntos de inicio/fin del arco no están calculados sobre las direcciones de los lados.

**Solución:** Calcular matemáticamente usando atan2:
```python
angle_lado1 = math.atan2(P1.y - Vertice.y, P1.x - Vertice.x)
angle_lado2 = math.atan2(P2.y - Vertice.y, P2.x - Vertice.x)
```

## Error: Etiqueta de ángulo invisible

**Síntoma:** La letra α, θ, β no aparece o está fuera del área visible.

**Causa:** La posición de la etiqueta no está en la bisectriz del ángulo.

**Solución:** Posicionar en la bisectriz a una distancia mayor que el arco.

## Error: Contenedor no centrado

**Síntoma:** La ilustración está pegada a la izquierda.

**Causa:** `max-width` sin `margin: 0 auto`.

**Solución:** Agregar `margin: 1.5rem auto` al estilo.

## Error: SVG comprimido con espacio en blanco

**Síntoma:** El SVG se ve "achatado" horizontalmente con espacio vacío a los lados.

**Causa:** El contenedor tiene `max-width` menor que el viewBox del SVG.

**Solución:** Usar `width: 100%; box-sizing: border-box;` en lugar de `max-width` fijo.

```html
<!-- ✅ CORRECTO -->
<div style="... width: 100%; box-sizing: border-box;">

<!-- ❌ INCORRECTO -->
<div style="... max-width: 500px;">  <!-- Si el SVG tiene viewBox 750px -->
```

## Error: SVG con caracteres XML inválidos (RESUELTO AUTOMÁTICAMENTE)

**Síntoma:** El SVG muestra error de parsing o solo se renderiza parcialmente.

**Causa:** Caracteres `<`, `>`, `&` sin escapar en el texto del SVG.

**Solución:** ✅ **AUTOMÁTICO** - El renderer escapa automáticamente estos caracteres.

```python
# En circle_renderer.py, text_element() y label_box() escapan automáticamente:
# "d < r"      → se convierte a → "d &lt; r"
# "d > R + r"  → se convierte a → "d &gt; R + r"

# El código puede usar caracteres normales:
positions = [
    ("Interior", "d < r"),   # ✅ Funciona automáticamente
    ("Exterior", "d > r"),   # ✅ Funciona automáticamente
]
```

**Función de escape (ya integrada en el renderer):**
```python
def escape_svg_text(text):
    """Escapa caracteres XML inválidos automáticamente."""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
```

## Error: Fórmula poco vistosa

**Síntoma:** La ecuación se ve comprimida o poco destacada.

**Causa:** `$$formula$$` en una sola línea sin espacios.

**Solución:** 
```markdown

$$
formula
$$

```

---

# 📚 EJEMPLOS DE REFERENCIA

Para ver el estilo correcto de lecciones, revisar:
- `src/content/matematicas/01-aritmetica/05-proporcionalidad/03-regla-de-tres-simple.md`
- `/fisica/cinematica/mrua/lanzamiento-vertical`
- `/fisica/introduccion-a-la-fisica/introduccion/la-fisica-y-sus-ramas`

---

# 🔧 MÓDULO CORE - Utilidades Compartidas para Renderers

> **Ubicación:** `scripts/geometry/core/`
> 
> **Principio:** Un solo lugar para colores, tamaños y helpers. NUNCA duplicar en renderers.

## Estructura del Módulo

```
scripts/geometry/core/
├── __init__.py          # Exporta todo (usar: from core import ...)
├── base.py              # Point, ValidationResult
├── colors.py            # COLORS (paleta unificada) ← FUENTE ÚNICA
├── canvas.py            # SIZE_SIMPLE, SIZE_COMPOUND, etc.
├── primitives.py        # escape_xml, point_on_circle, format_number
├── svg_builder.py       # SVGBuilder (API fluida para SVG)
└── coordinate_system.py # CoordinateSystem (transformación math↔SVG)
```

## Uso Básico

```python
# Importar todo lo necesario desde core
from core import (
    COLORS,                    # Paleta de colores
    SIZE_SIMPLE,               # Tamaños de canvas
    Point, SVGBuilder,         # Clases
    escape_xml, point_on_circle_svg  # Helpers
)

# Crear un SVG
builder = SVGBuilder(500, 400)
builder.rect(0, 0, 500, 400, fill=COLORS['background'])
builder.circle(Point(250, 200), 100, stroke=COLORS['primary'])
builder.save('output.svg')
```

## Colores (core/colors.py)

**FUENTE ÚNICA DE VERDAD.** NO definir colores en otros archivos.

```python
from core import COLORS

COLORS['primary']      # #3b82f6 - Azul (figuras principales)
COLORS['secondary']    # #22c55e - Verde (elementos secundarios)
COLORS['accent']       # #ef4444 - Rojo (puntos notables)
COLORS['highlight']    # #f97316 - Naranja (destacados)
COLORS['purple']       # #8b5cf6 - Púrpura (diámetros, bisectrices)
COLORS['pink']         # #ec4899 - Rosa (tangentes, mediatrices)
```

## Tamaños de Canvas (core/canvas.py)

```python
from core import SIZE_SIMPLE, SIZE_COMPOUND, get_canvas_config

SIZE_SIMPLE    # (500, 400) - 1 concepto
SIZE_COMPOUND  # (600, 460) - 2-3 elementos
SIZE_MULTIPLE  # (750, 450) - 4+ elementos
SIZE_CARTESIAN # (600, 500) - Plano cartesiano

config = get_canvas_config('simple')
# {'width': 500, 'height': 400, 'padding': 40}
```

## Primitivas (core/primitives.py)

```python
from core import escape_xml, point_on_circle_svg, format_number

# Escapar texto para SVG (CRÍTICO para <, >, &)
escape_xml("x < 5")  # "x &lt; 5"

# Punto en circunferencia (coordenadas SVG, Y invertido)
point_on_circle_svg(cx=100, cy=100, r=50, angle_deg=45)

# Formatear números (elimina decimales innecesarios)
format_number(3.0)      # "3"
format_number(3.14159)  # "3.14"
```

## Reglas para Nuevos Renderers

| ✅ HACER | ❌ NO HACER |
|----------|-------------|
| `from core import COLORS` | Definir `COLORS = {...}` localmente |
| `from core import SIZE_SIMPLE` | Definir `SIZE_SIMPLE = (500, 400)` |
| `from core import escape_xml` | Crear `escape_svg_text()` local |
| Usar `SVGBuilder` | Generar SVG con strings manuales |

## Agregar Nuevos Colores

Si necesitas un color nuevo, agregarlo **SOLO** en `core/colors.py`:

```python
# En core/colors.py
COLORS = {
    ...
    'mi_nuevo_color': '#hexcode',  # ← Agregar aquí
}
```

Luego exportarlo en `core/__init__.py` si es necesario.

## Agregar Nuevos Helpers

Si necesitas una función compartida:

1. Agregarla a `core/primitives.py`
2. Exportarla en `core/__init__.py`
3. Documentar su uso aquí en CLAUDE.md

---

# 📐 MÓDULO CARTESIAN - Geometría Analítica Modular

> **Ubicación:** `scripts/geometry/cartesian/`
> 
> **Principio:** Funciones de renderizado organizadas por tema. Cada archivo ≤ 300 líneas.

## Estructura del Módulo

```
scripts/geometry/cartesian/
├── __init__.py    # Exporta 30 funciones
├── points.py      # Plano básico, distancia, punto medio, división, áreas (5)
├── slopes.py      # Pendientes, inclinación, paralelas/perpendiculares (5)
├── lines.py       # Ecuaciones de rectas (8)
├── circles.py     # Circunferencias en el plano cartesiano (6)
└── parabolas.py   # Parábolas (6)
```

## Uso

```python
# Importar funciones específicas
from cartesian import render_plano_basico, render_distancia

# O importar todo
from cartesian import *

# Generar SVG
render_plano_basico('output.svg', title='Mi Plano')
render_distancia('distancia.svg', p1=(1, 2), p2=(4, 6))
```

## Funciones Disponibles (30 funciones)

### points.py - Puntos y Segmentos (5)
| Función | Descripción |
|---------|-------------|
| `render_plano_basico` | Plano cartesiano con 4 cuadrantes |
| `render_distancia` | Distancia entre dos puntos con triángulo |
| `render_punto_medio` | Punto medio de un segmento |
| `render_division_segmento` | División en razón m:n |
| `render_area_triangulo` | Área con fórmula del determinante |

### slopes.py - Pendientes (5)
| Función | Descripción |
|---------|-------------|
| `render_tipos_pendiente` | Positiva, negativa, horizontal |
| `render_concepto_pendiente` | Triángulo Δx, Δy |
| `render_calculo_pendiente` | Cálculo con dos puntos |
| `render_angulo_inclinacion` | Ángulo θ respecto al eje X |
| `render_paralelas_perpendiculares` | Relación entre pendientes |

### lines.py - Ecuaciones de Rectas (8)
| Función | Descripción |
|---------|-------------|
| `render_ecuacion_general` | Forma Ax + By + C = 0 |
| `render_punto_pendiente` | Forma y - y₁ = m(x - x₁) |
| `render_pendiente_ordenada` | Forma y = mx + b |
| `render_recta_dos_puntos` | Recta por dos puntos |
| `render_forma_simetrica` | Forma x/a + y/b = 1 |
| `render_forma_normal` | Forma x·cos(ω) + y·sin(ω) = p |
| `render_distancia_punto_recta` | Distancia de punto a recta |
| `render_familias_rectas` | Haz de rectas por un punto |

### circles.py - Circunferencias (6)
| Función | Descripción |
|---------|-------------|
| `render_elementos_circunferencia` | Centro, radio, diámetro, cuerda |
| `render_ecuacion_ordinaria_circ` | Forma (x-h)² + (y-k)² = r² |
| `render_posiciones_recta_circ` | Exterior, tangente, secante |
| `render_posiciones_dos_circ` | Posiciones entre circunferencias |
| `render_circunferencias_concentricas` | Familia concéntrica |
| `render_tangente_circunferencia` | Recta tangente |

### parabolas.py - Parábolas (6)
| Función | Descripción |
|---------|-------------|
| `render_elementos_parabola` | Foco, directriz, vértice, lado recto |
| `render_parabola_vertical_arriba` | x² = 4py (p > 0) |
| `render_parabola_vertical_abajo` | x² = -4py |
| `render_parabola_horizontal_derecha` | y² = 4px (p > 0) |
| `render_parabola_horizontal_izquierda` | y² = -4px |
| `render_cuatro_orientaciones_parabola` | Las 4 orientaciones |

## Agregar Nuevas Funciones a Módulos Existentes

1. Identificar el módulo correcto (points, slopes, lines, circles, parabolas)
2. Agregar la función al módulo
3. Exportarla en `cartesian/__init__.py`
4. Documentar aquí en CLAUDE.md

---

# 🧪 MÓDULO CHEMISTRY - Química

> **Ubicación:** `scripts/chemistry/`
> 
> **Workflow:** `.agent/workflows/chemistry-spec.md`

## Estructura del Módulo

```
scripts/chemistry/
├── periodic_table_renderer.py   # Tabla periódica desde spec JSON
└── trend_renderer.py            # Tendencias periódicas (4 tipos)

specs/quimica/
├── elementos/                   # Tabla periódica
│   ├── tabla-periodica-simple.json
│   └── tabla-periodica-completa.json
├── tendencias/                  # Propiedades periódicas
│   └── radio-atomico-tendencia.json
├── configuracion/               # (Por crear) Configuración electrónica
└── enlaces/                     # (Por crear) Enlace químico

public/images/quimica/
├── tabla-periodica-simple.svg
├── tabla-periodica-completa.svg
├── tendencias/
│   ├── radio-atomico.svg
│   ├── energia-ionizacion.svg
│   ├── afinidad-electronica.svg
│   └── electronegatividad.svg
```

## Uso

### Tabla Periódica

```bash
python3 scripts/chemistry/periodic_table_renderer.py \
    --spec specs/quimica/elementos/tabla-periodica-simple.json \
    --output public/images/quimica/tabla-periodica-simple.svg
```

### Tendencias Periódicas

```bash
python3 scripts/chemistry/trend_renderer.py \
    --type radio_atomico \
    --output public/images/quimica/tendencias/radio-atomico.svg
```

**Tipos disponibles:**
- `radio_atomico` - Radio atómico (↓ horizontal, ↑ vertical)
- `energia_ionizacion` - EI (↑ horizontal, ↓ vertical)
- `afinidad_electronica` - AE (↑ horizontal, ↓ vertical)
- `electronegatividad` - EN (↑ horizontal, ↓ vertical)

## Cuándo Usar Química vs Rough.js

| Tipo de ilustración | Tecnología |
|---------------------|------------|
| Tabla periódica | **ChemistrySpec** |
| Tendencias periódicas | **ChemistrySpec** |
| Niveles de energía | **ChemistrySpec** (crear renderer) |
| Estructuras de Lewis | **Rough.js** |
| Diagramas de procesos | **Rough.js** |
| Enlace iónico/covalente | **Rough.js** |

---

# 🚀 GUÍA: CREAR NUEVO TIPO DE ILUSTRACIÓN

> **Para agentes que necesitan agregar soporte para un nuevo tipo de ilustración que NO existe.**

## Paso 1: Evaluar si ya existe soporte

```
PREGUNTA: ¿El tipo de ilustración que necesito ya tiene renderer?

├── Circunferencias → circle_spec_renderer.py ✅
├── Triángulos → renderer.py ✅
├── Geometría analítica → cartesian/ ✅
├── Tabla periódica → chemistry/periodic_table_renderer.py ✅
├── Tendencias periódicas → chemistry/trend_renderer.py ✅
├── Gráficas de funciones → GraphSpec (inline) ✅
├── Diagramas conceptuales → Rough.js (inline) ✅
│
└── ¿NO existe? → Seguir esta guía para CREAR uno nuevo
```

## Paso 2: Decidir el enfoque

| Situación | Enfoque | Ejemplo |
|-----------|---------|---------|
| Ilustración simple, pocas variantes | Función directa en módulo existente | `render_nuevo_concepto()` |
| Muchas variantes del mismo tipo | Sistema Spec (JSON → Renderer) | `specs/nuevo_tipo/` |
| Nuevo dominio completo | Nuevo módulo con estructura completa | `scripts/physics/` |

## Paso 3: Crear nuevo módulo (si es necesario)

### 3.1 Estructura mínima para nuevo submódulo

```python
# scripts/geometry/nuevo_modulo.py
"""
📐 NuevoModulo - Descripción breve

Incluye:
- Función 1
- Función 2
"""

import math
import sys
from pathlib import Path

# OBLIGATORIO: Importar desde core (NUNCA duplicar)
sys.path.insert(0, str(Path(__file__).parent))
from core import Point, COLORS, SVGBuilder, CoordinateSystem


def render_mi_ilustracion(output_path: str, title: str = "Título"):
    """
    Descripción de qué renderiza.
    Para: XX-nombre-leccion.md
    """
    # Usar tamaños estándar
    width, height = 600, 500
    
    # Crear builder
    builder = SVGBuilder(width, height)
    builder.rect(0, 0, width, height, fill='#ffffff')
    builder.text(title, Point(width/2, 25), font_size=16, font_weight='bold')
    
    # ... lógica de renderizado ...
    
    builder.save(output_path)
    return True
```

### 3.2 Estructura para nuevo dominio (ej: Física)

```
scripts/physics/
├── __init__.py              # Exporta todo
├── core/                    # Puede importar de geometry/core
│   └── __init__.py
├── mechanics/
│   ├── __init__.py
│   ├── kinematics.py        # MRU, MRUA, caída libre
│   └── dynamics.py          # Fuerzas, planos inclinados
└── waves/
    ├── __init__.py
    └── simple_harmonic.py   # MAS, ondas
```

### 3.3 Ejemplo: Crear módulo de Física - Cinemática

```python
# scripts/physics/mechanics/kinematics.py
"""
🚀 Kinematics - Ilustraciones de cinemática

Incluye:
- MRU (Movimiento Rectilíneo Uniforme)
- MRUA (Movimiento Rectilíneo Uniformemente Acelerado)
- Caída libre
"""

import sys
from pathlib import Path

# Importar core de geometry (reutilizar)
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'geometry'))
from core import Point, COLORS, SVGBuilder, CoordinateSystem


def render_mru_grafica(output_path: str, v: float = 5, t_max: float = 10):
    """
    Gráfica posición vs tiempo para MRU.
    x = v·t
    """
    coord = CoordinateSystem(
        svg_width=600, svg_height=500,
        x_range=(0, t_max), y_range=(0, v * t_max),
        padding=60
    )
    
    builder = SVGBuilder(600, 500)
    builder.rect(0, 0, 600, 500, fill='#ffffff')
    builder.text(f'MRU: x = {v}t', Point(300, 25), font_size=16, font_weight='bold')
    
    coord.draw_grid(builder, step=1)
    coord.draw_axes(builder, show_arrows=True)
    
    # Dibujar recta x = vt
    p1 = Point(0, 0)
    p2 = Point(t_max, v * t_max)
    coord.draw_segment(builder, p1, p2, color=COLORS['primary'], width=2.5)
    
    # Etiquetas de ejes
    builder.text('t (s)', Point(550, 480), font_size=12)
    builder.text('x (m)', Point(30, 30), font_size=12)
    
    builder.save(output_path)
    return True
```

## Paso 4: Sistema Spec (para tipos con muchas variantes)

### 4.1 Definir esquema del spec

```json
// specs/fisica/cinematica/mru-ejemplo.json
{
  "tipo": "mru",
  "titulo": "MRU: Velocidad 5 m/s",
  "parametros": {
    "velocidad": 5,
    "tiempo_max": 10,
    "posicion_inicial": 0
  },
  "canvas": "cartesian",
  "mostrar": {
    "grafica_x_t": true,
    "grafica_v_t": true,
    "ecuacion": true
  }
}
```

### 4.2 Crear renderer para specs

```python
# scripts/physics/mechanics/kinematics_spec_renderer.py
"""
Renderer basado en specs para cinemática.
"""

import json
import argparse
from pathlib import Path

def render_from_spec(spec_path: str, output_path: str):
    """Renderiza desde un spec JSON."""
    with open(spec_path) as f:
        spec = json.load(f)
    
    tipo = spec.get('tipo')
    
    if tipo == 'mru':
        return render_mru_from_spec(spec, output_path)
    elif tipo == 'mrua':
        return render_mrua_from_spec(spec, output_path)
    else:
        raise ValueError(f"Tipo desconocido: {tipo}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--spec', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    
    render_from_spec(args.spec, args.output)


if __name__ == '__main__':
    main()
```

## Paso 5: Documentar en CLAUDE.md

### 5.1 Agregar al Árbol de Decisión

```markdown
├─── 🚀 ¿Es CINEMÁTICA (MRU, MRUA, caída libre)?
│    └─── SÍ → KINEMATICSSPEC (JSON → Python → SVG)
│         • Gráficas x-t, v-t, a-t
│         • Vectores de velocidad y aceleración
│         📁 Ver: .agent/workflows/kinematics-spec.md
```

### 5.2 Agregar sección de módulo

```markdown
# 🚀 MÓDULO PHYSICS - Física

> **Ubicación:** `scripts/physics/`

## Estructura
...

## Funciones Disponibles
...
```

## Paso 6: Crear workflow en .agent/workflows/

```markdown
<!-- .agent/workflows/kinematics-spec.md -->
# Workflow: Cinemática (KinematicsSpec)

## Cuándo usar
- Gráficas de MRU, MRUA, caída libre
- Vectores de velocidad y aceleración

## Paso 1: Crear spec
...

## Paso 2: Generar SVG
...
```

---

# ⚠️ REGLAS CRÍTICAS PARA EXTENSIBILIDAD

## ❌ NUNCA hacer

```python
# ❌ NUNCA duplicar colores
COLORS = {'primary': '#3b82f6', ...}  # NO! Ya existe en core/colors.py

# ❌ NUNCA duplicar helpers
def escape_xml(text):  # NO! Ya existe en core/primitives.py
    return text.replace('&', '&amp;')...

# ❌ NUNCA crear archivos > 300 líneas
# Si el archivo crece, dividirlo en submódulos
```

## ✅ SIEMPRE hacer

```python
# ✅ SIEMPRE importar de core
from core import COLORS, escape_xml, SVGBuilder

# ✅ SIEMPRE usar tamaños estándar
from core import SIZE_SIMPLE, SIZE_COMPOUND

# ✅ SIEMPRE documentar en CLAUDE.md
# No crear READMEs separados

# ✅ SIEMPRE seguir el patrón Spec → Renderer → SVG
# para tipos con muchas variantes
```

## Checklist antes de crear nuevo módulo

- [ ] ¿Revisé que no existe ya soporte para este tipo?
- [ ] ¿Importo de `core/` en lugar de duplicar?
- [ ] ¿El archivo tiene ≤ 300 líneas?
- [ ] ¿Documenté en CLAUDE.md?
- [ ] ¿Creé workflow en `.agent/workflows/` si es sistema Spec?
- [ ] ¿Agregué al Árbol de Decisión?
- [ ] ¿Los colores usan `COLORS['nombre']` de core?