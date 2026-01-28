---
title: "Función Constante e Identidad"
---

# Función Constante e Identidad

Las funciones más simples son los bloques de construcción para entender todas las demás. Empezamos con las dos funciones más básicas: la constante y la identidad.

---

## 🎯 ¿Qué vas a aprender?

- La función constante y sus propiedades
- La función identidad y sus propiedades
- Gráficas de ambas funciones
- Por qué son fundamentales en matemáticas

---

## 📖 Función constante

La **función constante** asigna el mismo valor de salida sin importar la entrada.

$$
f(x) = c \quad \text{donde } c \text{ es una constante}
$$

### Ejemplos

- $f(x) = 5$ (siempre devuelve 5)
- $g(x) = -2$ (siempre devuelve -2)
- $h(x) = 0$ (la función cero)

### Propiedades

| Propiedad | Valor |
|-----------|-------|
| **Dominio** | $\mathbb{R}$ |
| **Rango** | $\{c\}$ (un solo elemento) |
| **Gráfica** | Línea horizontal en $y = c$ |
| **Paridad** | Par (si $c \neq 0$); si $c = 0$, también es impar |
| **Pendiente** | $0$ |

### Gráfica

```
     y
     ↑
─────●━━━━━━━━━━━━━━━→ y = c
     |
─────┼─────────────→ x
     |
```

---

## 📖 Función identidad

La **función identidad** devuelve exactamente el valor de entrada.

$$
f(x) = x
$$

También se denota como $I(x) = x$ o $\text{id}(x) = x$.

### Propiedades

| Propiedad | Valor |
|-----------|-------|
| **Dominio** | $\mathbb{R}$ |
| **Rango** | $\mathbb{R}$ |
| **Gráfica** | Línea recta que pasa por el origen con pendiente 1 |
| **Paridad** | Impar ($f(-x) = -x = -f(x)$) |
| **Pendiente** | $1$ |
| **Biyectiva** | Sí |
| **Inversa** | Ella misma: $f^{-1}(x) = x$ |

### Gráfica

```
     y
     ↑        /
     |       /
     |      /
     |     /
─────┼────/────────→ x
     |   / 45°
     |  /
```

La gráfica es la bisectriz del primer y tercer cuadrante.

---

## 📖 ¿Por qué son importantes?

### La función identidad como "neutro"

En composición de funciones, la identidad es el elemento neutro:

$$
f(I(x)) = f(x) \quad \text{y} \quad I(f(x)) = f(x)
$$

Cualquier función compuesta con la identidad da la misma función.

### La función constante en límites

En cálculo, aparece en reglas como:

$$
\frac{d}{dx}[c] = 0 \quad \text{(derivada de constante)}
$$

$$
\int c \, dx = cx + K \quad \text{(integral de constante)}
$$

---

## ⚙️ Ejemplo 1: Evaluación

Sea $f(x) = 7$ y $g(x) = x$.

a) $f(100) = 7$
b) $f(-50) = 7$
c) $g(100) = 100$
d) $g(-50) = -50$

---

## ⚙️ Ejemplo 2: Composición con identidad

Sea $h(x) = x^2 + 3x$ e $I(x) = x$.

$h(I(x)) = h(x) = x^2 + 3x$

$I(h(x)) = h(x) = x^2 + 3x$

La identidad no cambia nada.

---

## ⚙️ Ejemplo 3: Intersección de gráficas

¿Dónde se intersectan $f(x) = x$ y $g(x) = 3$?

Igualamos: $x = 3$

**Punto de intersección:** $(3, 3)$

---

## 📊 Comparación resumida

| Característica | Constante $f(x) = c$ | Identidad $f(x) = x$ |
|----------------|---------------------|---------------------|
| Depende de $x$ | No | Sí |
| Gráfica | Horizontal | Diagonal 45° |
| Inyectiva | No (si el dominio tiene más de un punto) | Sí |
| Suprayectiva | No | Sí |
| Derivada | $0$ | $1$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Identifica qué tipo de función es:

a) $f(x) = \pi$
b) $g(x) = x$
c) $h(x) = 0$
d) $k(x) = 2x$

<details>
<summary>Ver soluciones</summary>

a) **Constante** (siempre vale $\pi$)

b) **Identidad**

c) **Constante** (la función cero, también es la identidad multiplicativa en suma)

d) **Ni constante ni identidad** (es una función lineal con pendiente 2)
</details>

---

**Ejercicio 2:** Si $f(x) = 4$ y $g(x) = x$, calcula:

a) $f(g(2))$
b) $g(f(2))$
c) $f(f(f(100)))$

<details>
<summary>Ver soluciones</summary>

a) $f(g(2)) = f(2) = 4$

b) $g(f(2)) = g(4) = 4$

c) $f(f(f(100))) = f(f(4)) = f(4) = 4$ (siempre da 4)
</details>
