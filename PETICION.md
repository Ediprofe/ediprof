# 📋 PETICIÓN AL AGENTE

> **Este documento es tu punto de entrada.** Lee las instrucciones, las reglas críticas, y luego la petición del usuario al final.

---

## 🚀 INSTRUCCIONES RÁPIDAS

### Paso 1: Obtener contexto
```
LEE: CLAUDE.md (secciones relevantes según el tipo de tarea)
```

### Paso 2: Identificar tipo de tarea

| Si la petición es sobre... | Lee esta sección de CLAUDE.md |
|---------------------------|-------------------------------|
| **Crear lecciones nuevas** | "Flujo de trabajo en 5 etapas" |
| **Generar ilustraciones** | "Sistema de ilustraciones" + Árbol de decisión |
| **Modificar renderers Python** | "Módulo Core" + "Módulo Cartesian" |
| **Exportar a Word/PDF** | "Comandos útiles" |
| **Entender la estructura** | "Estructura del proyecto" |

### Paso 3: Consultar workflows específicos

| Tipo de ilustración | Workflow |
|---------------------|----------|
| Circunferencias | `.agent/workflows/circle-spec.md` |
| Triángulos | `.agent/workflows/geometry-exact.md` |
| Geometría analítica | `.agent/workflows/cartesian-spec.md` |
| Gráficas de funciones | `.agent/workflows/graphspec.md` |
| **Estadística (histogramas, barras)** | `.agent/workflows/mathplotter-spec.md` |
| **Sistemas de ecuaciones** | `.agent/workflows/mathplotter-spec.md` |
| Diagramas conceptuales | PNG de tablet (ver CLAUDE.md) |
| Química (tabla periódica) | `.agent/workflows/chemistry-spec.md` |
| Contenido educativo | `.agent/workflows/content-generation.md` |

---

## ⚠️ REGLAS CRÍTICAS (LEER SIEMPRE)

> **Estas reglas existen porque errores pasados requirieron refactorizaciones masivas. NO las ignores.**

### 🎨 1. COLORES: Nunca hardcodear

```python
# ❌ PROHIBIDO
color='#3b82f6'

# ✅ OBLIGATORIO
from core.colors import COLORS
color=COLORS['primary']
```

**Fuente de verdad:** `scripts/geometry/core/colors.py`

### 🏷️ 2. CONFIGURACIÓN: Usar centralizadas

```typescript
// ❌ PROHIBIDO
const materiaColor = '#ef4444';

// ✅ OBLIGATORIO
import { getMateriaConfig } from '../config/materias';
const config = getMateriaConfig('matematicas');
```

**Fuentes de verdad:**
- Materias: `src/config/materias.ts`
- Tipos: `src/types/content.ts`
- URLs: `src/utils/navigation-generator.js`

### 📐 3. LaTeX: Formato correcto

```markdown
<!-- ❌ PROHIBIDO -->
La fórmula es: $$A = \pi r^2$$ donde...

<!-- ✅ OBLIGATORIO -->
La fórmula es:

$$
A = \pi r^2
$$

Donde...
```

### 🖼️ 4. Contenedores SVG: Responsivos

```html
<!-- ❌ PROHIBIDO -->
<div style="max-width: 500px;">

<!-- ✅ OBLIGATORIO -->
<div style="width: 100%; box-sizing: border-box;">
```

### 📁 5. Metadatos: _meta.json obligatorio

Cada carpeta de tema DEBE tener:
```json
{
  "name": "Nombre con Tildes",
  "description": "Descripción breve"
}
```

### ✅ 6. Verificación: Ejecutar siempre

Después de modificar renderers:
```bash
bash scripts/verify-svg-rendering.sh
```

---

## 📊 TABLA RESUMEN DE FUENTES DE VERDAD

| Qué | Dónde | Importar |
|-----|-------|----------|
| Colores SVG | `scripts/geometry/core/colors.py` | `from core.colors import COLORS` |
| MathPlotter | `scripts/geometry/core/plotter.py` | `from scripts.geometry.core.plotter import MathPlotter` |
| Config materias | `src/config/materias.ts` | `getMateriaConfig()` |
| Tipos TypeScript | `src/types/content.ts` | `MateriaSlug`, `isMateriaSlug` |
| Helpers de URL | `src/utils/navigation-generator.js` | `cleanSlug()`, `cleanSegment()` |
| Tamaños canvas | `scripts/geometry/core/canvas.py` | `SIZE_SIMPLE`, `SIZE_COMPOUND` |

---

## 🚫 ANTI-PATRONES (NO REPETIR)

| ❌ Error | ✅ Solución |
|---------|------------|
| Hardcodear colores hex | Usar `COLORS` de core |
| `max-width` fijo en SVG | Usar `width: 100%` |
| LaTeX en títulos | Usar texto plano |
| Usar tags HTML/JSX para imágenes | Usar Markdown `![alt](path)` |
| Crear `_meta.json` sin `name` | Siempre incluir `name` |
| Definir tipos localmente | Importar de `types/content` |

---

## 📋 CHECKLIST ANTES DE ENTREGAR

- [ ] ¿Usé las fuentes de verdad para colores/config?
- [ ] ¿Los contenedores SVG son responsivos?
- [ ] ¿El LaTeX está en bloques con líneas vacías?
- [ ] ¿Ejecuté la verificación de renderers?
- [ ] ¿Los `_meta.json` tienen `name`?

---

## 🔄 PROTOCOLO DE CLARIFICACIÓN

**Si NO tienes certeza de algo → PREGUNTA ANTES de ejecutar.**

Situaciones que requieren confirmación:
- Diagramas técnicos/visuales
- Primera vez haciendo algo de ese tipo
- Solicitud ambigua o con múltiples interpretaciones

---

# 📝 PETICIÓN DEL USUARIO

http://localhost:4321/fisica/cinematica/mrua/introduccion

quiero que para esta lección tengas en cuenta un análisis por ejemplo en el caso de a = 2m/s2, que se encuentre la posición, durante los primeros tres egundos por ejemplo, y que muestre un análsisi muy pedagógico efectivo, que considere esto:
Entendido, vamos a calcular la posición paso a paso para un móvil que parte del reposo () con una aceleración constante de  durante los primeros 2 segundos.

### 1. Razonamiento por intervalos (Método Inductivo)

En el **MRUA**, la velocidad cambia uniformemente, lo que hace que la distancia recorrida en cada segundo sea distinta.

* **Segundo 1 (de  a ):**
* La velocidad inicial es  y la final es  (aumentó  unidades por la aceleración).
* La velocidad promedio en este intervalo es .
* En 1 segundo a  promedio, recorre ****.
* **Posición a :** .


* **Segundo 2 (de  a ):**
* Empieza el segundo a  y termina a  (sumamos otros  de aceleración).
* La velocidad promedio en este intervalo es .
* En este segundo recorre ****.
* **Posición a :** Posición anterior () + tramo nuevo () = ****.



---

### 2. Comprobación con la Fórmula

La fórmula de posición para objetos que parten del origen y del reposo () es:

Sustituimos :

* **Para :**


* **Para :**



---

### 🔑 Resumen de Resultados (Cheat Sheet)

| Tiempo () | Velocidad () | Razonamiento (Tramo) | Posición Final () |
| --- | --- | --- | --- |
| **** |  | Inicio | **** |
| **** |  |  | **** |
| **** |  |  | **** |

```markdown
      t = 0s       t = 1s             t = 2s
        ●────────────●──────────────────●
       0m           1m                 4m
        [  1 metro  ] [   3 metros     ]

```

> 💡 **Tip del Profe:** Nota que las distancias recorridas en cada segundo consecutivo () siempre siguen la secuencia de los **números impares** cuando la aceleración es constante y se parte del reposo.

¿Te gustaría que grafiquemos esto para ver cómo se forma la curva (parábola) en el plano cartesiano?

y puedes hacerlo al ginal, o de la manera que más progresiva lo consideres tú. ADELANTE. LUEGO CUANDO TENGAMOS LA LECCIÓN COMPLETA, NOS ENCARGAMOS DE LAS IMÁGENES.