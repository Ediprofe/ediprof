# 🎓 Estilo Ediprofe - Referencia Rápida

> **Toda lección sigue el mismo estilo, sin importar si es introducción o desarrollo.**

---

## 📋 Estructura Obligatoria

```markdown
# **Título de la Lección**

[1-2 oraciones que conectan con la vida real o con la lección anterior]

---

## 🎯 ¿Qué vas a aprender?

- Punto 1
- Punto 2
- Punto 3
- Punto 4

---

## [Secciones de contenido]

[Contenido con ejemplos paso a paso]

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Enunciado**

<details>
<summary>Ver solución</summary>

**Datos:** ...
**Razonamiento:** ...
**Resultado:** $\boxed{...}$

</details>

[10 ejercicios total]

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **X** | ... |

> Conclusión breve.
```

---

## 🧠 Principios Pedagógicos

| Principio | Qué hacer |
|-----------|-----------|
| **Inductivo** | Ejemplo concreto → Regla general (NUNCA al revés) |
| **Cotidiano** | Conectar con vida real desde la primera oración |
| **Paso a paso** | No dar saltos lógicos, explicar cada paso |
| **Simple** | Una idea por párrafo, oraciones cortas |

---

## ✍️ Formato Técnico

| Elemento | Formato |
|----------|---------|
| **Título** | `# **Título**` (SIN emoji) |
| **Fórmula importante** | Bloque `$$...$$` con líneas vacías antes/después |
| **TODAS las ecuaciones** | Formato de bloque para legibilidad (ver abajo) |
| **Resultado final** | `$$\boxed{...}$$` — Siempre en bloque, nunca inline |
| **Soluciones** | Dentro de `<details><summary>Ver solución</summary>...</details>` |

### ⚠️ Regla Crítica: Ecuaciones en Bloque

> **🚨 MUY IMPORTANTE:** Esta regla se aplica a TODAS las ecuaciones, incluyendo las que están dentro de razonamientos y soluciones de ejercicios.

**TODAS** las ecuaciones en ejemplos y razonamientos deben estar en formato de bloque, **NUNCA inline**. Esto mejora la legibilidad y evita errores de renderizado.

**✅ Correcto (cada ecuación en su propio renglón):**
```markdown
**Razonamiento:**

1. Abrimos el centro:

$$
2x^2 + 6x + x + 3
$$

2. Agrupamos:

$$
(2x^2 + 6x) + (x + 3)
$$

3. Factor común:

$$
2x(x + 3) + 1(x + 3)
$$
```

**❌ Incorrecto (todo en una línea o mezclado con texto):**
```markdown
**Razonamiento:**
Abrimos: $2x^2 + 6x + x + 3$, agrupamos $(2x^2+6x)+(x+3)$ y sacamos...
```

**❌ También incorrecto (bloque sin líneas vacías):**
```markdown
**Razonamiento:**
$$2x^2 + 6x + x + 3$$
Agrupamos:
$$...
```

---

## ❌ Errores a Evitar

| Error | Corrección |
|-------|------------|
| Fórmula → ejemplo | Ejemplo → fórmula |
| "Es evidente que..." | Nunca asumir que algo es evidente |
| Párrafos largos (5+ líneas) | Máximo 3 líneas por párrafo |
| Ejercicios sin razonamiento | Siempre incluir el "por qué" |
| LaTeX inline en títulos | Solo texto plano en títulos |

---

### Ejemplos de las lecciones modelo

```
MRUA: mrua.png, mapa-movimiento-mrua.png, mrua-analisis-edificio.png
MCU: mcu-intro.png, carrusel-mcu.png, rueda-2hz.png, mcu-resumen.png
```

---

## 📚 Lecciones Modelo

Estas lecciones ya están aprobadas y representan el estilo objetivo:

- `src/content/fisica/02-cinematica/04-MRUA/01-introduccion.md`
- `src/content/fisica/02-cinematica/05-MCU/01-introduccion.md`
