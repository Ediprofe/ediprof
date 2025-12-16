---
description: Árbol de decisión expandido con ejemplos para elegir la tecnología correcta de ilustración globs: ["src/content/**/*.md"]
---

# 🌳 Workflow: Decisión de Ilustraciones

Este documento ayuda a elegir la **tecnología correcta** para cada tipo de ilustración.

---

## 🔑 Pregunta Clave

> **¿La ilustración requiere precisión matemática exacta o es conceptual/ilustrativa?**

| Respuesta | Acción |
|-----------|--------|
| **Precisión exacta** (propiedades geométricas, teoremas) | → GeometrySpec |
| **Conceptual/ilustrativa** (situaciones, procesos, modelos) | → Rough.js |
| **Datos/funciones** (gráficas, estadísticas) | → ECharts |
| **Fracciones visuales** (pie charts) | → Chart.js |
| **3D** (volúmenes, geometría espacial) | → Three.js |
| **Solo fórmula** | → LaTeX |

---

## 📋 Ejemplos por Materia

### 🧮 MATEMÁTICAS

| Necesidad | Tecnología | Razón |
|-----------|------------|-------|
| Gráfica de $f(x) = 2x + 3$ | **ECharts** | Es función, no geometría |
| Baricentro de un triángulo | **GeometrySpec** | Propiedad exacta |
| Comparar $y = x^2$ vs $y = x^3$ | **ECharts** | Son funciones |
| Circuncentro y circunferencia circunscrita | **GeometrySpec** | Propiedades exactas |
| Fracción 3/4 como pastel | **Chart.js** | Visualización de fracción |
| Recta de Euler | **GeometrySpec** | Alineación exacta de 3 puntos |
| Histograma de frecuencias | **ECharts** | Datos estadísticos |
| Sistema de ecuaciones (intersección) | **ECharts** | Son funciones |
| Ángulos complementarios | **GeometrySpec** | Medida exacta |
| Mapa conceptual de tipos de números | **Rough.js** | Conceptual |

### 🚀 FÍSICA

| Necesidad | Tecnología | Razón |
|-----------|------------|-------|
| Bloque en plano inclinado | **Rough.js** | Situación ilustrativa |
| Gráfica posición vs tiempo | **ECharts** | Datos/función |
| Diagrama de fuerzas | **Rough.js** | Ilustrativo |
| Gráfica velocidad vs tiempo | **ECharts** | Datos/función |
| Circuito eléctrico simple | **Rough.js** | Esquemático |
| Gráfica de MRU | **ECharts** | Función lineal |
| Ciclo del método científico | **Rough.js** | Proceso/ciclo |
| Ramas de la física (organigrama) | **Rough.js** | Jerarquía |
| Resorte con masa | **Rough.js** | Situación física |
| Gráfica de Hooke (F vs x) | **ECharts** | Función lineal |

### ⚛️ QUÍMICA

| Necesidad | Tecnología | Razón |
|-----------|------------|-------|
| Modelo atómico de Bohr | **Rough.js** | Modelo ilustrativo |
| Estados de la materia (partículas) | **Rough.js** | Conceptual |
| Equipo de destilación | **Rough.js** | Esquema de equipo |
| Tabla periódica (sección) | **Rough.js** | Diagrama |
| Gráfica de solubilidad vs temperatura | **ECharts** | Datos |
| Enlace covalente (electrones compartidos) | **Rough.js** | Modelo |
| Diagrama de fases del agua | **ECharts** | Gráfica con regiones |
| Proceso de cromatografía | **Rough.js** | Proceso |
| Estructura de Lewis | **Rough.js** | Modelo molecular |
| Titulación (equipo) | **Rough.js** | Esquema |

### 🌍 CIENCIAS

| Necesidad | Tecnología | Razón |
|-----------|------------|-------|
| Ciclo del agua | **Rough.js** | Proceso/ciclo |
| Cadena alimenticia | **Rough.js** | Jerarquía |
| Célula (organelos) | **Rough.js** | Diagrama ilustrativo |
| Gráfica de población vs tiempo | **ECharts** | Datos |
| Capas de la Tierra | **Rough.js** | Diagrama |
| Pirámide ecológica | **Rough.js** | Jerarquía |
| Fotosíntesis (proceso) | **Rough.js** | Proceso |

---

## 🎯 Casos Especiales

### Caso 1: "Triángulo con alturas"

❓ ¿Las alturas deben ser matemáticamente perpendiculares?

- **SÍ** → GeometrySpec (la perpendicularidad es una propiedad exacta)
- **NO, solo ilustrativo** → Rough.js (si solo quieres mostrar "la idea" de altura)

**Regla:** Si el estudiante podría "verificar" la propiedad con una regla/compás, usa GeometrySpec.

### Caso 2: "Función lineal con intersección"

Es una **función** → ECharts

Aunque tenga un punto de intersección (que podrías llamar "geometría"), el contexto es álgebra de funciones, no geometría euclidiana.

### Caso 3: "Comparar áreas de figuras"

❓ ¿Las figuras tienen medidas exactas que demostrar?

- **SÍ** (ej: "el cuadrado de lado 4 tiene área 16") → GeometrySpec
- **NO** (ej: "visualmente comparar que un rectángulo parece más grande") → Rough.js

### Caso 4: "Diagrama de vectores"

❓ ¿Los vectores deben tener magnitudes/direcciones exactas?

- **SÍ** (ej: "vector de 5N a 30°") → GeometrySpec o ECharts con cálculos
- **NO** (ej: "mostrar que hay fuerzas actuando") → Rough.js

### Caso 5: "Plano cartesiano"

❓ ¿Qué se grafica?

- **Puntos sueltos o funciones** → ECharts
- **Figuras geométricas con propiedades** → GeometrySpec
- **Solo mostrar el concepto de coordenadas** → Rough.js

---

## 📊 Matriz de Decisión Completa

```
                        ┌─────────────────────────────────────────────┐
                        │        TIPO DE CONTENIDO                    │
                        ├─────────────────────────────────────────────┤
                        │                                             │
 PRECISIÓN   Alta       │  GeometrySpec    │    ECharts               │
 REQUERIDA              │  (geometría)     │    (funciones)           │
             ──────────────────────────────────────────────────────────
             Baja       │  Rough.js        │    Rough.js              │
                        │  (diagramas)     │    (conceptos)           │
                        │                                             │
                        └────────┬─────────────────┬──────────────────┘
                                 │                 │
                           Geométrico        Numérico/Datos
                        
                                NATURALEZA
```

---

## ⚠️ Señales de Alerta

### 🚨 Probablemente estás eligiendo MAL si...

| Señal | Problema | Solución |
|-------|----------|----------|
| Usas JSXGraph con `circumcenter`, `incircle` | Estas funciones fallan | Cambiar a GeometrySpec |
| Hardcodeas coordenadas de puntos notables | No son exactas | Cambiar a GeometrySpec |
| Usas ECharts para dibujar un triángulo | No es una función | Cambiar a GeometrySpec o Rough.js |
| Usas Rough.js para "bisectriz exacta" | No garantiza ángulos iguales | Cambiar a GeometrySpec |
| Usas GeometrySpec para "bloque en rampa" | Overkill, es ilustrativo | Cambiar a Rough.js |

---

## 🔄 Flujo de Decisión Paso a Paso

```
1. ¿Necesito mostrar una FÓRMULA MATEMÁTICA?
   └── SÍ → LaTeX ($...$ o $$...$$)
   └── NO → Continuar

2. ¿Es una GRÁFICA de función o datos?
   └── SÍ → ECharts
   └── NO → Continuar

3. ¿Es GEOMETRÍA con propiedades que DEBEN cumplirse exactamente?
   (perpendiculares, bisectrices, puntos notables, tangencias, etc.)
   └── SÍ → GeometrySpec
   └── NO → Continuar

4. ¿Es GEOMETRÍA 3D?
   └── SÍ → Three.js
   └── NO → Continuar

5. ¿Es una FRACCIÓN visual (pie chart)?
   └── SÍ → Chart.js
   └── NO → Continuar

6. Es un DIAGRAMA ilustrativo/conceptual
   └── → Rough.js
```

---

## ✅ Resumen Ejecutivo

| Pregúntate | Si SÍ → Usa |
|------------|-------------|
| ¿Es una función $f(x)$? | ECharts |
| ¿Son datos/estadísticas? | ECharts |
| ¿Las propiedades geométricas DEBEN ser exactas? | GeometrySpec |
| ¿Es solo ilustrativo/conceptual? | Rough.js |
| ¿Es 3D? | Three.js |
| ¿Es fracción como pastel? | Chart.js |
| ¿Es solo texto matemático? | LaTeX |

---

## 🔗 Workflows Detallados

- [ECharts](./echarts.md) - Funciones y datos
- [GeometrySpec](./geometry-exact.md) - Geometría exacta
- [Rough.js](./roughjs.md) - Diagramas ilustrativos
- [Chart.js](./chartjs.md) - Fracciones
- [Three.js](./threejs.md) - Geometría 3D