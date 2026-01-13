---
description: Workflow para generar ilustraciones SVG de química
globs: ["src/content/quimica/**/*.md"]
---

# 🧪 Workflow: Química (ChemistrySpec)

Este documento define el proceso para generar ilustraciones de química usando el sistema Spec-First.

---

## Cuándo Usar Este Workflow

| Tipo de ilustración | Usar este workflow |
|---------------------|-------------------|
| Tabla periódica | ✅ Sí |
| Tendencias periódicas | ✅ Sí |
| Niveles de energía | ✅ Sí |
| Orbitales atómicos | ✅ Sí |
| Estructuras de Lewis | ⚠️ Preferir Rough.js |
| Diagramas de procesos | ⚠️ Preferir Rough.js |

---

## Renderers Disponibles

### 1. Tabla Periódica

```bash
python3 scripts/chemistry/periodic_table_renderer.py \
    --spec specs/quimica/elementos/[SPEC].json \
    --output public/images/quimica/[NOMBRE].svg
```

**Specs disponibles:**
- `tabla-periodica-simple.json` - Períodos 1-4 (36 elementos)
- `tabla-periodica-completa.json` - 118 elementos con lantánidos/actínidos

### 2. Tendencias Periódicas

```bash
python3 scripts/chemistry/trend_renderer.py \
    --type [TIPO] \
    --output public/images/quimica/tendencias/[NOMBRE].svg
```

**Tipos disponibles:**
| Tipo | Descripción |
|------|-------------|
| `radio_atomico` | Radio atómico (↓ horizontal, ↑ vertical) |
| `energia_ionizacion` | EI (↑ horizontal, ↓ vertical) |
| `afinidad_electronica` | AE (↑ horizontal, ↓ vertical) |
| `electronegatividad` | EN (↑ horizontal, ↓ vertical) |

---

## Proceso Paso a Paso

### Paso 1: Identificar el tipo de ilustración

Revisar el ASCII art en la lección y determinar qué tipo de ilustración es:

```
¿Es una tabla periódica?
  → Usar periodic_table_renderer.py

¿Es una tendencia periódica?
  → Usar trend_renderer.py

¿Es un diagrama de niveles de energía?
  → Crear spec JSON + nuevo renderer (o Rough.js)

¿Es una estructura de Lewis o proceso?
  → Usar Rough.js (ver roughjs.md)
```

### Paso 2: Crear o usar spec existente

**Si el spec ya existe:**
```bash
ls specs/quimica/
```

**Si necesitas crear un spec nuevo:**

```json
{
    "version": "1.0",
    "title": "Título de la ilustración",
    "description": "Descripción breve",
    "layout": {
        "width": 600,
        "height": 400
    },
    // ... datos específicos del tipo
}
```

Guardar en: `specs/quimica/[categoria]/[nombre].json`

### Paso 3: Ejecutar el renderer

```bash
python3 scripts/chemistry/[renderer].py \
    --spec specs/quimica/[categoria]/[nombre].json \
    --output public/images/quimica/[nombre].svg
```

### Paso 4: Verificar el SVG

1. Abrir en navegador: `http://localhost:4321/images/quimica/[nombre].svg`
2. Verificar que se ve correctamente
3. Verificar modo claro y oscuro

### Paso 5: Insertar en el markdown

Reemplazar el ASCII art con:

```markdown
![Descripción](/images/quimica/nombre.svg)
```

O con wrapper para contexto:

```html
<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <img src="/images/quimica/nombre.svg" alt="Descripción" style="width: 100%; height: auto;" />
</div>
```

---

## Estructura de Carpetas

```
specs/quimica/
├── elementos/           # Tabla periódica y elementos
│   ├── tabla-periodica-simple.json
│   └── tabla-periodica-completa.json
├── tendencias/          # Propiedades periódicas
│   └── radio-atomico-tendencia.json
├── configuracion/       # Configuración electrónica (por crear)
│   ├── niveles-energia.json
│   └── orbitales-spdf.json
└── enlaces/             # Enlace químico (por crear)
    └── tipos-enlace.json

scripts/chemistry/
├── periodic_table_renderer.py   # Tabla periódica
├── trend_renderer.py            # Tendencias periódicas
└── [futuros renderers]

public/images/quimica/
├── tabla-periodica-simple.svg
├── tabla-periodica-completa.svg
├── tendencias/
│   ├── radio-atomico.svg
│   ├── energia-ionizacion.svg
│   ├── afinidad-electronica.svg
│   └── electronegatividad.svg
└── [futuras imágenes]
```

---

## Crear Nuevo Renderer

Si necesitas un tipo de ilustración que no existe:

### 1. Crear el renderer

```python
#!/usr/bin/env python3
"""
📊 Mi Nuevo Renderer - Descripción

Uso:
    python3 scripts/chemistry/mi_renderer.py \
        --spec specs/quimica/mi-spec.json \
        --output public/images/quimica/mi-svg.svg
"""

import sys
from pathlib import Path

# OBLIGATORIO: Importar de core
sys.path.insert(0, str(Path(__file__).parent.parent / 'geometry'))
from core import COLORS
from core.primitives import escape_xml

def render(spec: dict) -> str:
    # ... lógica de renderizado
    pass

def main():
    # ... CLI con argparse
    pass

if __name__ == '__main__':
    main()
```

### 2. Definir el spec JSON

```json
{
    "version": "1.0",
    "title": "Título",
    "description": "Descripción",
    // campos específicos
}
```

### 3. Documentar en este workflow

Agregar sección con:
- Comando de uso
- Formato del spec
- Ejemplos

---

## Cuándo Usar Rough.js en Lugar de SVG

Para química, usar Rough.js cuando:

1. **Estructuras de Lewis** - Aspecto de "dibujado a mano"
2. **Procesos químicos** - Flechas de reacción
3. **Diagramas conceptuales** - Sin precisión matemática
4. **Comparaciones visuales** - Antes/después

Ver: `.agent/workflows/roughjs.md`

---

## Checklist de Calidad

- [ ] El SVG se renderiza correctamente
- [ ] Los colores usan `COLORS` de core
- [ ] El texto usa `escape_xml()` para caracteres especiales
- [ ] El viewBox es apropiado para el contenido
- [ ] Funciona en modo claro y oscuro
- [ ] El spec está guardado en `specs/quimica/`
- [ ] El SVG está en `public/images/quimica/`
