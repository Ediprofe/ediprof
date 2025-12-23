# 📐 Especificaciones de Geometría Exacta

Esta carpeta contiene las especificaciones JSON para el sistema GeometrySpec.

## Estructura

```
specs/geometria/
├── triangulos/         # Puntos notables, medianas, alturas, etc.
├── cuadrilateros/      # Paralelogramos, rombos, etc.
├── circulos/           # Circunferencias, tangentes, secantes
└── README.md           # Este archivo
```

## Uso

Cada archivo `.json` se procesa con el renderer:

```bash
python scripts/geometry/renderer.py \
  --spec specs/geometria/triangulos/baricentro.json \
  --output public/images/geometria/triangulos/baricentro.svg \
  --verify
```

## Referencia

Ver `.agent/workflows/geometry-exact.md` para documentación completa del formato.


