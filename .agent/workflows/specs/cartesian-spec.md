# 📐 Cartesian Spec - Geometría Analítica

## Resumen

Sistema de renderizado para ilustraciones de geometría analítica (plano cartesiano).

## Arquitectura

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  IA genera   │────▶│   Python     │────▶│    SVG       │
│ CartesianSpec│     │  renderer    │     │   exacto     │
│   (JSON)     │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
```

## Uso Rápido

### Tipos predefinidos

```bash
# Plano cartesiano básico con cuadrantes
python3 scripts/geometry/cartesian_renderer.py \
  --type plano-basico \
  --output public/images/geometria/analitica/plano.svg

# Distancia entre dos puntos
python3 scripts/geometry/cartesian_renderer.py \
  --type distancia \
  --output public/images/geometria/analitica/distancia.svg

# Punto medio
python3 scripts/geometry/cartesian_renderer.py \
  --type punto-medio \
  --output public/images/geometria/analitica/punto-medio.svg

# División de segmento
python3 scripts/geometry/cartesian_renderer.py \
  --type division-segmento \
  --output public/images/geometria/analitica/division.svg

# Área de triángulo
python3 scripts/geometry/cartesian_renderer.py \
  --type area-triangulo \
  --output public/images/geometria/analitica/area.svg
```

### Desde spec JSON

```bash
python3 scripts/geometry/cartesian_renderer.py \
  --spec specs/geometria/analitica/mi-ilustracion.json \
  --output public/images/geometria/analitica/mi-ilustracion.svg
```

## Especificaciones JSON

### Plano básico

```json
{
  "tipo": "plano-basico",
  "titulo": "El Plano Cartesiano"
}
```

### Distancia entre puntos

```json
{
  "tipo": "distancia",
  "titulo": "Distancia entre A y B",
  "p1": [1, 2],
  "p2": [4, 6]
}
```

### Punto medio

```json
{
  "tipo": "punto-medio",
  "titulo": "Punto medio del segmento AB",
  "p1": [2, 1],
  "p2": [6, 5]
}
```

### División de segmento

```json
{
  "tipo": "division-segmento",
  "titulo": "División en razón 2:3",
  "p1": [1, 2],
  "p2": [7, 8],
  "m": 2,
  "n": 3
}
```

### Área de triángulo

```json
{
  "tipo": "area-triangulo",
  "titulo": "Área del triángulo ABC",
  "vertices": [[1, 1], [5, 1], [3, 5]]
}
```

## Estructura de Archivos

```
scripts/geometry/
├── core/                      # Módulo base compartido
│   ├── __init__.py
│   ├── base.py                # Point, COLORS, ValidationResult
│   ├── svg_builder.py         # Primitivas SVG
│   └── coordinate_system.py   # Sistema de coordenadas
├── cartesian_renderer.py      # Renderer de geometría analítica
├── circle_spec_renderer.py    # Renderer de circunferencias
└── renderer.py                # Renderer de triángulos

specs/geometria/
├── analitica/                 # Specs de geometría analítica
├── circulos/                  # Specs de circunferencias
└── triangulos/                # Specs de triángulos

public/images/geometria/
├── analitica/                 # SVGs de geometría analítica
├── circulos/                  # SVGs de circunferencias
└── triangulos/                # SVGs de triángulos
```

## Insertar en Markdown

```markdown
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/plano-cartesiano.svg" alt="Plano Cartesiano" style="width: 100%; height: auto;" />
</div>
```

## Paleta de Colores

| Elemento | Color | Hex |
|----------|-------|-----|
| Ejes | Gris | `#64748b` |
| Cuadrícula | Gris claro | `#e2e8f0` |
| Puntos | Rojo | `#ef4444` |
| Segmentos | Azul | `#3b82f6` |
| Auxiliares | Gris | `#94a3b8` |
| Fórmulas (fondo) | Amarillo | `#fef3c7` |

## Módulo Core

El módulo `core/` contiene código reutilizable:

- **Point**: Clase para puntos 2D con operaciones vectoriales
- **SVGBuilder**: API fluida para construir SVGs
- **CoordinateSystem**: Transformación matemáticas ↔ SVG

Esto permite que otros renderers (circunferencias, triángulos) compartan código.
