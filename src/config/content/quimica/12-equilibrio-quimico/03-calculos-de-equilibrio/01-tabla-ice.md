---
title: "Tabla ICE"
---

# Tabla ICE

La **tabla ICE** (Initial, Change, Equilibrium) es un método sistemático para resolver problemas de equilibrio químico. Permite organizar la información y calcular concentraciones en el equilibrio.

---

## 🎯 ¿Qué vas a aprender?

- Qué significa ICE y cómo usarlo
- Cómo construir una tabla ICE
- Resolver problemas paso a paso
- Cuándo usar aproximaciones

---

## 📊 Significado de ICE

| Letra | Significado | Descripción |
|-------|-------------|-------------|
| **I** | Initial | Concentraciones iniciales |
| **C** | Change | Cambio durante la reacción |
| **E** | Equilibrium | Concentraciones en equilibrio |

---

## 📖 Estructura de la Tabla

Para la reacción: aA + bB ⇌ cC + dD

|  | A | B | C | D |
|--|---|---|---|---|
| **I** | [A]₀ | [B]₀ | [C]₀ | [D]₀ |
| **C** | -ax | -bx | +cx | +dx |
| **E** | [A]₀-ax | [B]₀-bx | [C]₀+cx | [D]₀+dx |

### 💡 Notas:

- **x** = variable desconocida (extensión de reacción)
- Los coeficientes de C son los coeficientes estequiométricos
- Reactivos: **-** (disminuyen)
- Productos: **+** (aumentan)

---

## 📖 Ejemplo 1: Problema Básico

### Problema:

Para N₂ + 3H₂ ⇌ 2NH₃, se inicia con [N₂] = 1.0 M y [H₂] = 3.0 M. Si Kc = 0.5, ¿cuáles son las concentraciones en equilibrio?

### Paso 1: Construir tabla ICE

|  | N₂ | H₂ | NH₃ |
|--|----|----|-----|
| **I** | 1.0 | 3.0 | 0 |
| **C** | -x | -3x | +2x |
| **E** | 1.0-x | 3.0-3x | 2x |

### Paso 2: Escribir expresión de K

$$
K_c = \frac{[\text{NH}_3]^2}{[\text{N}_2][\text{H}_2]^3} = \frac{(2x)^2}{(1.0-x)(3.0-3x)^3}
$$

### Paso 3: Sustituir y resolver

$$
0.5 = \frac{4x^2}{(1.0-x)(3.0-3x)^3}
$$

Esta ecuación se resuelve numéricamente o con aproximaciones.

---

## 📖 Ejemplo 2: Con Aproximación

### Problema:

Para 2NO₂ ⇌ N₂O₄ con [NO₂]₀ = 0.1 M y Kc = 170, encuentre el equilibrio.

### Tabla ICE:

|  | NO₂ | N₂O₄ |
|--|----|------|
| **I** | 0.1 | 0 |
| **C** | -2x | +x |
| **E** | 0.1-2x | x |

### Expresión:

$$
170 = \frac{x}{(0.1-2x)^2}
$$

Como K es grande, asumimos que la reacción avanza bastante (2x ≈ 0.1).

---

## 📖 Ejemplo 3: Partiendo de Productos

### Problema:

Si partimos con [NH₃]₀ = 2.0 M (sin N₂ ni H₂), la reacción va "hacia atrás".

### Tabla ICE:

|  | N₂ | H₂ | NH₃ |
|--|----|----|-----|
| **I** | 0 | 0 | 2.0 |
| **C** | +x | +3x | -2x |
| **E** | x | 3x | 2.0-2x |

### 💡 Nota:

Cuando la reacción va hacia reactivos, los signos se invierten.

---

## 📖 Reglas para Cambios (C)

### 💡 Los cambios son proporcionales a los coeficientes:

Para aA + bB ⇌ cC:
- Si A cambia en -x, entonces:
  - B cambia en -(b/a)x
  - C cambia en +(c/a)x

### ⚙️ Ejemplo:

N₂ + **3**H₂ ⇌ **2**NH₃

Si N₂ cambia en -x:
- H₂ cambia en -3x (coef. 3)
- NH₃ cambia en +2x (coef. 2)

---

## 📖 Cuándo Usar Aproximaciones

### 💡 Aproximación √(Ka·C):

Si K es pequeño y C₀ es grande, se puede asumir que x << C₀.

### ⚙️ Verificación:

Si x < 5% de C₀, la aproximación es válida.

---

## 🔑 Resumen

| Fila | Representa |
|------|------------|
| **I** | Concentraciones iniciales |
| **C** | Cambios (con signos y coeficientes) |
| **E** | I + C = Equilibrio |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Completa la tabla ICE para: H₂ + I₂ ⇌ 2HI, con [H₂]₀ = [I₂]₀ = 0.5 M

<details>
<summary>Ver solución</summary>

|  | H₂ | I₂ | HI |
|--|----|----|-----|
| **I** | 0.5 | 0.5 | 0 |
| **C** | -x | -x | +2x |
| **E** | 0.5-x | 0.5-x | 2x |

</details>

### Ejercicio 2
Para PCl₅ ⇌ PCl₃ + Cl₂, [PCl₅]₀ = 1 M. Si en equilibrio [Cl₂] = 0.4 M, ¿cuál es [PCl₅]eq?

<details>
<summary>Ver solución</summary>

De la tabla ICE:
- [Cl₂] = x = 0.4 M
- [PCl₃] = x = 0.4 M
- [PCl₅] = 1 - x = 1 - 0.4 = **0.6 M**

</details>

### Ejercicio 3
¿Por qué los cambios (C) deben mantener las proporciones estequiométricas?

<details>
<summary>Ver solución</summary>

Porque la **estequiometría** de la reacción dicta las proporciones exactas en que se consumen y producen las sustancias.

Si 1 mol de N₂ reacciona, necesariamente:
- Se consumen 3 mol de H₂ (proporción 1:3)
- Se producen 2 mol de NH₃ (proporción 1:2)

Esto es consecuencia de la **ley de conservación de la masa** y los coeficientes de la ecuación balanceada.

</details>
