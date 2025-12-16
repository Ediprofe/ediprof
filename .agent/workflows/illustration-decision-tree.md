# 🌳 Árbol de Decisión para Ilustraciones

## Pregunta Principal: ¿Qué tipo de ilustración necesitas?

```
¿Qué tipo de ilustración?
│
├─ 📐 GEOMETRÍA EXACTA (medidas precisas, propiedades matemáticas)
│   └─ → GeometrySpec → SVG
│   │
│   ├─ Triángulos con razones trigonométricas
│   ├─ Puntos notables (baricentro, ortocentro, etc.)
│   ├─ Círculos con radios y ángulos exactos
│   ├─ Polígonos con medidas específicas
│   └─ Cualquier figura donde la PRECISIÓN MATEMÁTICA sea crítica
│
├─ 📈 FUNCIONES Y DATOS (gráficas, estadísticas, tendencias)
│   └─ → ECharts
│   │
│   ├─ Gráficas de sin(x), cos(x), tan(x)
│   ├─ Funciones cuadráticas, lineales, exponenciales
│   ├─ Tablas de valores como gráficos de barras
│   ├─ Tendencias y comparaciones numéricas
│   └─ Cualquier visualización de DATOS o FUNCIONES
│
├─ 🎨 CONCEPTOS / SITUACIONES DEL MUNDO REAL
│   └─ → Rough.js (estilo "dibujado a mano")
│   │
│   ├─ Edificios, torres, faros
│   ├─ Personas observando objetos
│   ├─ Escaleras, rampas, puentes
│   ├─ Escenarios de física (proyectiles, fuerzas)
│   ├─ Diagramas conceptuales no exactos
│   └─ Cualquier SITUACIÓN REAL donde el estilo amigable ayude
│
├─ 🥧 FRACCIONES COMO PASTEL
│   └─ → Chart.js (pie charts)
│
└─ 🧊 GEOMETRÍA 3D
    └─ → Three.js
```

## Ejemplos por Tecnología

### GeometrySpec → SVG
```
specs/geometria/trigonometria/03-triangulo-345.json
↓
python3 scripts/geometry/trigonometry_renderer.py --spec ... --output ...
↓
public/images/geometria/trigonometria/03-triangulo-345.svg
```

**Cuándo usar:**
- ✅ "Dibuja un triángulo 3-4-5 con las razones etiquetadas"
- ✅ "Muestra el baricentro de un triángulo"
- ✅ "Círculo con radio 5 y ángulo de 60°"

**Cuándo NO usar:**
- ❌ "Un edificio con una persona mirando hacia arriba"
- ❌ "La gráfica de y = sin(x)"

### ECharts
```javascript
var option = {
  xAxis: { type: 'value', min: 0, max: 90 },
  yAxis: { type: 'value', min: 0, max: 1 },
  series: [{ type: 'line', data: sinData }]
};
```

**Cuándo usar:**
- ✅ "Gráfica de seno de 0° a 90°"
- ✅ "Comparación de valores de sin, cos, tan"
- ✅ "Visualización de datos estadísticos"

**Cuándo NO usar:**
- ❌ "Un triángulo con medidas exactas"
- ❌ "Una escalera apoyada en una pared"

### Rough.js
```javascript
import rough from 'https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.esm.js';
const rc = rough.svg(svg);
svg.appendChild(rc.rectangle(280, 50, 50, 150, { fill: '#94a3b8', fillStyle: 'hachure' }));
```

**Cuándo usar:**
- ✅ "Persona observando un edificio con ángulo de elevación"
- ✅ "Faro y barco para ángulo de depresión"
- ✅ "Escalera apoyada en una pared"
- ✅ "Cualquier escenario de 'mundo real'"

**Cuándo NO usar:**
- ❌ "Triángulo con razones trigonométricas exactas"
- ❌ "Puntos notables de un triángulo"

## Resumen Rápido

| Pregunta | Tecnología |
|----------|------------|
| ¿Necesito precisión matemática? | **GeometrySpec → SVG** |
| ¿Es una función o datos? | **ECharts** |
| ¿Es una situación del mundo real? | **Rough.js** |
| ¿Es una fracción como pastel? | **Chart.js** |
| ¿Es 3D? | **Three.js** |

## Estructura de Archivos

```
specs/geometria/
├── trigonometria/        # Triángulos para trigonometría
├── triangulos/           # Triángulos generales
├── circulos/             # Círculos y arcos
└── conica/               # Parábolas, elipses, hipérbolas

scripts/geometry/
├── trigonometry_renderer.py   # Triángulos rectángulos
├── renderer.py                # Geometría general
└── (futuro) conic_renderer.py # Cónicas

public/images/geometria/
└── trigonometria/        # SVGs generados
```

## Flujo de Trabajo

1. **Identificar tipo de ilustración** → Usar este árbol
2. **Si es GeometrySpec** → Crear JSON en `specs/`, ejecutar renderer
3. **Si es ECharts** → Código JavaScript directo en el markdown
4. **Si es Rough.js** → Código JavaScript con import de CDN

## Notas Importantes

- **Rough.js** se importa desde CDN: `https://cdn.jsdelivr.net/npm/roughjs@4.6.6/bundled/rough.esm.js`
- **ECharts** ya está disponible globalmente en el sitio
- **GeometrySpec SVGs** se referencian como `/images/geometria/...`

