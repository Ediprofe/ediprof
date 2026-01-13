## Plan de Ilustraciones

### Lección: Paralelogramos
**URL:** `matematicas/geometria-euclidiana/cuadrilateros/paralelogramos`
**Archivo:** `02-paralelogramos.md`

| # | Ubicación | Descripción | Renderer |
|---|-----------|-------------|----------|
| 1 | Definición | Paralelogramo genérico resaltando las líneas paralelas ($>>$ y $>$). | `parallelogram_renderer.py` (Nuevo) |
| 2 | Propiedades Fundamentales | Mostrar ángulos opuestos iguales ($\alpha = \gamma$) y lados opuestos iguales ($a=c$). | `parallelogram_renderer.py` |
| 3 | Diagonales | Ilustrar que las diagonales se bisecan (marcas de igualdad en segmentos de cada diagonal). | `parallelogram_renderer.py` |
| 4 | Área y Perímetro | Distinción clara entre lado inclinado y altura perpendicular ($h$). | `parallelogram_renderer.py` |
| 5 | Ejemplo 1 | Cálculo de ángulos dado $60^\circ$ (mostrar $60, 120, 60, 120$). | `parallelogram_renderer.py` |
| 6 | Ejemplo 2 | Ejemplo de área con datos numéricos ($b=10, h=4$, lado=$5$). | `parallelogram_renderer.py` |
| 7 | Resumen | Panel visual con las 4 propiedades clave (Lados, Ángulos, Diagonales, Área). | `parallelogram_renderer.py` |

---

### Detalles Técnicos
- **Nuevo Script:** `scripts/geometry/parallelogram_renderer.py`
- **Base:** Copiar estructura de `quadrilateral_renderer.py`
- **Modos:**
    - `concept_definition`
    - `concept_properties`
    - `concept_diagonals`
    - `concept_area`
    - `example_angles`
    - `example_area`
    - `summary_all`
- **Colores:**
    - Lados paralelos: `primary`
    - Altura: `danger` (para resaltar y diferenciar)
    - Diagonales: `medianas`
