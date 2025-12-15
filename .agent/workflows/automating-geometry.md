---
description: Pipeline de automatización para generar ilustraciones geométricas perfectas y didácticas usando Python.
---

# 📐 Workflow: Generación de Geometría Estática

Este workflow define cómo generar ilustraciones geométricas que sean:
1. **Matemáticamente Perfectas**: Coordenadas exactas calculadas por `sympy`.
2. **Pedagógicamente Claras**: Con líneas de construcción, marcas de ángulos y etiquetas.
3. **Técnicamente Robustas**: SVG estático, cero JavaScript en el navegador del estudiante.

## 🔄 El Flujo Automático

Cuando se requiera una ilustración geométrica compleja (triángulos, intersecciones, teoremas):

1.  **NO usar JSXGraph manual** en los archivos `.md`.
2.  **SIEMPRE crear/actualizar un script Python** en `scripts/geometry/`.
    *   Convención de nombre: `generate_[tema].py`.
    *   Este script actúa como la "fuente de la verdad".
3.  **El Agente ejecuta el script**: `python3 scripts/geometry/generate_[tema].py`.
4.  **El Agente enlaza el resultado**: `![Alt](/images/geometria/tema/archivo.svg)`.

## 🛠️ Estándar Didáctico (Clase `GeometryPlotter`)

Todos los scripts deben usar la clase estándar que incluye:
*   **Colores Semánticos**:
    *   Verde: Medianas
    *   Naranja: Alturas
    *   Morado: Bisectrices/Mediatrices
    *   Rojo: Puntos Notables
*   **Elementos Explicativos**:
    *   `right_angle_mark()`: Para mostrar perpendicularidad.
    *   `tick_mark()`: Para mostrar segmentos iguales.
    *   `dashed lines`: Para construcciones auxiliares.

## 🚀 Por qué esto NO corta el flujo

1.  **Edición**: Si el usuario pide un cambio ("mueve el punto A"), el Agente edita el script Python y regenera. Es instantáneo.
2.  **Despliegue**: El resultado es un archivo `.svg`. Vercel lo sirve como imagen estática. Es la forma más rápida y compatible posible.
3.  **Mantenibilidad**: La lógica geométrica queda encapsulada en Python, no dispersa en HTML/JS frágil.

## // turbo-all
Si se invoca este workflow, el agente debe tener permiso para ejecutar `python3` y crear archivos en `scripts/geometry/`.
