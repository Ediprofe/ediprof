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
- Estructura: Intro motivadora → Conceptos con ejemplos → Práctica
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
| **Auto-explicativo** | ¿La ilustración se entiende SIN leer el texto? |

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
| **Compuesto** (2-3 elementos) | `0 0 600 420` | Sector+triángulo, teoremas con comparación |
| **Múltiple** (4+ elementos) | `0 0 750 450` | Posiciones de circunferencias, comparaciones múltiples |
| **Horizontal** (lado a lado) | `0 0 700 350` | Operaciones A - B = C, antes/después |

### Regla de Consistencia

```
⚠️ CRÍTICO: Todas las ilustraciones de un mismo tema deben usar 
el MISMO tamaño de viewBox para verse consistentes en la página.
```

**Ejemplo para Elementos de la Circunferencia:**
- Radio, Diámetro, Cuerda, Arco → Todos `0 0 500 400`
- Sector, Segmento, Corona → Todos `0 0 500 400`

### Regla de Ancho Mínimo

```python
# En cada renderer, definir constantes:
STANDARD_WIDTH = 500   # Ancho mínimo para ocupar el contenedor
STANDARD_HEIGHT = 400  # Alto proporcional

# Para ilustraciones compuestas (A - B = C):
COMPOSITE_WIDTH = 700  # Más ancho para 3 elementos
COMPOSITE_HEIGHT = 420
```

### Verificación de Carga

Antes de considerar un SVG terminado:
1. ✅ El archivo existe en `public/images/...`
2. ✅ La ruta en markdown es EXACTA (case-sensitive)
3. ✅ El SVG tiene contenido válido (no vacío)
4. ✅ El viewBox está definido correctamente

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
│         • ÁNGULOS con arcos correctamente posicionados
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

### Para Todos los Gráficos

```
✅ SIEMPRE:
   • Envolver en DOMContentLoaded
   • Verificar disponibilidad: if (typeof echarts !== 'undefined')
   • Usar wrapper con fondo y bordes redondeados
   • ID únicos: tipo-leccion-numero
   • CENTRAR contenedores: margin: 0 auto

❌ NUNCA:
   • Interactividad por defecto (fixed: true en todos los puntos)
   • Zoom, pan, o elementos arrastrables sin solicitud explícita
   • Contenedores con max-width sin centrar
```

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

## Contenedores de Ilustraciones - CENTRADOS

> ⚠️ **SIEMPRE centrar** los contenedores de ilustraciones.

```html
<!-- ✅ CORRECTO: centrado con margin auto -->
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 500px;">

<!-- ❌ INCORRECTO: max-width sin centrar -->
<div style="background: #f1f5f9; max-width: 500px;">
```

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

## Wrapper Estándar para Gráficos (CENTRADO)

```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Título</strong>
  </div>
  
  ![Descripción](/images/ruta/imagen.svg)
  
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
| Arcos de ángulos | Naranja | `#f97316` |

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
- `/fisica/introduccion-a-la-fisica/introduccion/la-fisica-y-sus-ramas`|