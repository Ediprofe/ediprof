---
description: Sistema para generar mapas conceptuales SVG jerárquicos (ConceptMapSpec → Python → SVG)
globs: ["specs/mapas/**/*.json", "scripts/diagrams/**/*.py"]
---

# 🗺️ Workflow: ConceptMapSpec (Mapas Conceptuales)

Sistema para generar **mapas conceptuales educativos** como SVG estructurados.

---

## 🎯 Principio Fundamental

> **ConceptMapSpec** genera diagramas jerárquicos tipo árbol:
> - ✅ Mapas de unidades/temas
> - ✅ Resúmenes visuales de lecciones
> - ✅ Clasificaciones (taxonomías)
> - ✅ Organigramas de conceptos

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  IA genera   │────▶│ Python calcula│───▶│    SVG       │
│ ConceptMap   │     │  posiciones  │     │  jerárquico  │
│   (JSON)     │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
```

---

## 🔧 Comando

```bash
python3 scripts/diagrams/conceptmap_renderer.py \
  --spec specs/mapas/[materia]/[nombre].json \
  --output public/images/[materia]/mapas/[nombre].svg
```

### Opciones

| Flag | Descripción |
|------|-------------|
| `--spec` | Archivo JSON de especificación |
| `--output` | Archivo SVG de salida |
| `--preview` | Abre en navegador al terminar |

---

## 📋 Formato JSON

```json
{
  "version": "1.0",
  "type": "conceptmap",
  "metadata": {
    "id": "mi-mapa",
    "title": "Título del Mapa"
  },
  "canvas": {
    "width": 1400,
    "height": 900,
    "background": "#fafafa"
  },
  "layout": {
    "type": "horizontal",
    "spacing_x": 220,
    "spacing_y": 60
  },
  "nodes": [
    {
      "id": "central",
      "text": "NODO CENTRAL",
      "level": 0,
      "color": "#66BB6A"
    },
    {
      "id": "rama1",
      "text": "Rama 1",
      "parent": "central",
      "level": 1,
      "color": "#9575CD"
    },
    {
      "id": "hoja1",
      "text": "Hoja 1",
      "parent": "rama1",
      "level": 2,
      "color": "#B39DDB"
    }
  ]
}
```

---

## 📊 Tipos de Layout

| Layout | Descripción | Uso |
|--------|-------------|-----|
| `horizontal` | Árbol de izquierda a derecha | Mapas con muchas ramas |
| `radial` | Nodo central con ramas en círculo | Mapas compactos |

---

## 🎨 Paleta de Colores Sugerida

| Tema | Color | Hex |
|------|-------|-----|
| Central (verde) | 🟢 | `#66BB6A` |
| Propiedades (morado) | 🟣 | `#9575CD` |
| Estados (azul) | 🔵 | `#64B5F6` |
| Cambios (naranja) | 🟠 | `#FFB74D` |
| Clasificación (lila) | 🟣 | `#BA68C8` |
| Separación (coral) | 🔴 | `#FF8A65` |

---

## 📁 Estructura de Archivos

```
proyecto/
├── specs/
│   └── mapas/
│       └── quimica/
│           └── la-materia.json
├── scripts/
│   └── diagrams/
│       └── conceptmap_renderer.py
└── public/
    └── images/
        └── quimica/
            └── mapas/
                └── la-materia.svg
```

---

## ✅ Checklist

- [ ] `"type": "conceptmap"` en el spec
- [ ] `metadata.id` único
- [ ] Cada nodo tiene `id`, `text`, `level`
- [ ] Nodos hijos tienen `parent` apuntando al padre
- [ ] Colores en formato hex
- [ ] Ejecutar con `--preview` para verificar
- [ ] Insertar en markdown: `![Alt](/images/materia/mapas/nombre.svg)`

---

## ⚠️ Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| Nodos superpuestos | `spacing_y` muy pequeño | Aumentar `spacing_y` |
| Conexiones cruzadas | Layout inadecuado | Reorganizar `parent` o cambiar a `radial` |
| Texto cortado | Nodo muy pequeño | El renderer ajusta automáticamente |

---

## 📝 Ejemplo de Uso en Markdown

```markdown
## Resumen de la Unidad

![Mapa conceptual de La Materia](/images/quimica/mapas/la-materia.svg)
```

---

## 🔗 Relacionados

- [GraphSpec](./graphspec.md) - Para gráficas matemáticas
- [ChemistrySpec](./chemistry-spec.md) - Para tabla periódica
- [Árbol de decisión](./illustration-decision.md) - Qué tecnología usar
