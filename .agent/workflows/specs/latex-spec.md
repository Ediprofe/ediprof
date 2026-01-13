---
description: Reglas de formato LaTeX para ecuaciones matemáticas en lecciones
globs: ["src/content/**/*.md"]
---

# 📐 LaTeX Spec: Formato de Ecuaciones

> **Todas las ecuaciones matemáticas deben seguir estas reglas sin excepción.**

---

## 🚨 Regla Principal: Bloques Separados

**NUNCA uses LaTeX inline** (`$...$`) para ecuaciones. Cada ecuación va en su propio bloque:

```markdown
$$
\text{ecuación aquí}
$$
```

---

## 📦 Resultados Importantes: Usar `\boxed{}`

**Toda respuesta final o fórmula clave debe ir enmarcada** con `\boxed{}`:

```markdown
**Resultado:**

$$
\boxed{x = 5}
$$
```

Esto aplica para:
- ✅ Respuestas finales de ejemplos y ejercicios
- ✅ Fórmulas importantes que el estudiante debe memorizar
- ✅ Conclusiones de demostraciones

**Ejemplo visual:**

$$
\boxed{\frac{\text{Área}_2}{\text{Área}_1} = k^2}
$$

---

## ✅ Formato Correcto

### Cada ecuación en su propio bloque

```markdown
Para los perímetros:

$$
\frac{\text{Perímetro}_2}{\text{Perímetro}_1} = k
$$

Para las alturas:

$$
\frac{\text{Altura}_2}{\text{Altura}_1} = k
$$
```

### Pasos de razonamiento separados

```markdown
**Razonamiento:**

1. Sustituimos valores:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

2. Calculamos el discriminante:

$$
\Delta = b^2 - 4ac = 25 - 16 = 9
$$

3. Obtenemos las raíces:

$$
x_1 = 4 \quad ; \quad x_2 = 1
$$
```

---

## ❌ Formato Incorrecto

### Múltiples ecuaciones en una línea

```markdown
❌ INCORRECTO:
$$ \frac{P_2}{P_1} = k \quad ; \quad \frac{A_2}{A_1} = k $$
```

### LaTeX inline mezclado con texto

```markdown
❌ INCORRECTO:
Sustituimos $x = 5$ en la ecuación $y = 2x + 3$ y obtenemos $y = 13$.
```

### Bloques pegados al texto

```markdown
❌ INCORRECTO:
**Razonamiento:**
$$x = 5$$
Entonces...
```

---

## 📋 Checklist de Verificación

Antes de guardar una lección, verifica:

| ✅ Verificar | Descripción |
|-------------|-------------|
| Línea vacía ANTES del `$$` | El bloque no está pegado al texto |
| Línea vacía DESPUÉS del `$$` | El bloque no está pegado al siguiente texto |
| Una ecuación por bloque | No hay `;` separando múltiples ecuaciones |
| Sin inline en pasos | Los pasos de razonamiento usan bloques |
| Resultados con `\boxed{}` | Las respuestas finales están enmarcadas |

---

## 🔍 Ejemplo Completo

```markdown
### Ejemplo 1: Calcular el área del triángulo grande

Si $k = 2$ y el área del triángulo pequeño es $A_1 = 10$ cm².

**Datos:**
- $k = 2$
- $A_1 = 10$ cm²

**Razonamiento:**

La razón de las áreas es $k^2$:

$$
\frac{A_2}{A_1} = k^2
$$

Sustituimos:

$$
A_2 = A_1 \cdot k^2
$$

$$
A_2 = 10 \cdot 2^2
$$

$$
A_2 = 10 \cdot 4
$$

**Resultado:**

$$
\boxed{A_2 = 40 \text{ cm}^2}
$$
```

---

## ⚠️ Excepciones Permitidas

El formato inline `$...$` **solo** se permite para:

1. **Variables simples en texto**: "donde $k$ es la razón de semejanza"
2. **Unidades**: "el resultado es 5 $\text{m/s}$"
3. **Referencias cortas**: "según la fórmula $A = \pi r^2$..."

**NUNCA** para ecuaciones que el estudiante debe resolver o analizar.

---

## 📚 Referencia

- Documento completo: `.agent/prompts/estilo-ediprofe.md`
- Workflow de corrección: `.agent/workflows/comandos/corregir.md`
