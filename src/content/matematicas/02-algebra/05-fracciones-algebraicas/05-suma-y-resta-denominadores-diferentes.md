# ➕ Suma y Resta con Denominadores Diferentes

En esta lección aprenderemos a sumar y restar fracciones algebraicas cuando tienen denominadores distintos, aplicando el concepto de mínimo común múltiplo (MCM) que estudiamos anteriormente.

---

## 📖 Método general

Para sumar o restar fracciones con denominadores diferentes:

1. **Encontrar** el MCM de los denominadores (denominador común)
2. **Convertir** cada fracción al denominador común
3. **Sumar o restar** los numeradores
4. **Simplificar** si es posible

---

## 📖 Denominadores monomios

### Ejemplo 1

Resolver $\dfrac{3}{x} + \dfrac{5}{x^2}$.

**Paso 1:** El MCM de $x$ y $x^2$ es $x^2$.

**Paso 2:** Convertimos cada fracción:

$$
\frac{3}{x} = \frac{3 \cdot x}{x \cdot x} = \frac{3x}{x^2}
$$

$$
\frac{5}{x^2} = \frac{5}{x^2}
$$

**Paso 3:** Sumamos:

$$
\frac{3x}{x^2} + \frac{5}{x^2} = \frac{3x + 5}{x^2}
$$

$$
\boxed{\frac{3}{x} + \frac{5}{x^2} = \frac{3x + 5}{x^2}}
$$

---

### Ejemplo 2

Resolver $\dfrac{2}{3x} - \dfrac{5}{6x^2}$.

**Paso 1:** El MCM de $3x$ y $6x^2$ es $6x^2$.

**Paso 2:** Convertimos:

$$
\frac{2}{3x} = \frac{2 \cdot 2x}{3x \cdot 2x} = \frac{4x}{6x^2}
$$

$$
\frac{5}{6x^2} = \frac{5}{6x^2}
$$

**Paso 3:** Restamos:

$$
\frac{4x}{6x^2} - \frac{5}{6x^2} = \frac{4x - 5}{6x^2}
$$

$$
\boxed{\frac{2}{3x} - \frac{5}{6x^2} = \frac{4x - 5}{6x^2}}
$$

---

### Ejemplo 3

Resolver $\dfrac{1}{xy} + \dfrac{2}{xz} + \dfrac{3}{yz}$.

**Paso 1:** El MCM de $xy$, $xz$ y $yz$ es $xyz$.

**Paso 2:** Convertimos cada fracción:

$$
\frac{1}{xy} = \frac{z}{xyz}, \quad \frac{2}{xz} = \frac{2y}{xyz}, \quad \frac{3}{yz} = \frac{3x}{xyz}
$$

**Paso 3:** Sumamos:

$$
\frac{z + 2y + 3x}{xyz}
$$

$$
\boxed{\frac{1}{xy} + \frac{2}{xz} + \frac{3}{yz} = \frac{3x + 2y + z}{xyz}}
$$

---

## 📖 Denominadores binomios sin factores comunes

### Ejemplo 4

Resolver $\dfrac{2}{x+1} + \dfrac{3}{x-1}$.

**Paso 1:** El MCM de $(x+1)$ y $(x-1)$ es $(x+1)(x-1)$.

**Paso 2:** Convertimos:

$$
\frac{2}{x+1} = \frac{2(x-1)}{(x+1)(x-1)}, \quad \frac{3}{x-1} = \frac{3(x+1)}{(x+1)(x-1)}
$$

**Paso 3:** Sumamos:

$$
\frac{2(x-1) + 3(x+1)}{(x+1)(x-1)} = \frac{2x - 2 + 3x + 3}{(x+1)(x-1)} = \frac{5x + 1}{(x+1)(x-1)}
$$

$$
\boxed{\frac{2}{x+1} + \frac{3}{x-1} = \frac{5x + 1}{x^2-1}}
$$

---

### Ejemplo 5

Resolver $\dfrac{x}{x+2} - \dfrac{x}{x-2}$.

**Paso 1:** El MCM es $(x+2)(x-2)$.

**Paso 2:** Convertimos:

$$
\frac{x(x-2)}{(x+2)(x-2)} - \frac{x(x+2)}{(x+2)(x-2)}
$$

**Paso 3:** Restamos:

$$
\frac{x(x-2) - x(x+2)}{(x+2)(x-2)} = \frac{x^2 - 2x - x^2 - 2x}{(x+2)(x-2)} = \frac{-4x}{(x+2)(x-2)}
$$

$$
\boxed{\frac{x}{x+2} - \dfrac{x}{x-2} = \frac{-4x}{x^2-4}}
$$

---

### Ejemplo 6

Resolver $\dfrac{3}{x+3} + \dfrac{2}{x-4}$.

**Solución:**

$$
\frac{3(x-4) + 2(x+3)}{(x+3)(x-4)} = \frac{3x - 12 + 2x + 6}{(x+3)(x-4)} = \frac{5x - 6}{(x+3)(x-4)}
$$

$$
\boxed{\frac{3}{x+3} + \frac{2}{x-4} = \frac{5x - 6}{(x+3)(x-4)}}
$$

---

## 📖 Denominadores con factores comunes

### Ejemplo 7

Resolver $\dfrac{3}{x+2} + \dfrac{5}{(x+2)^2}$.

**Paso 1:** El MCM es $(x+2)^2$.

**Paso 2:** Convertimos:

$$
\frac{3(x+2)}{(x+2)^2} + \frac{5}{(x+2)^2}
$$

**Paso 3:** Sumamos:

$$
\frac{3(x+2) + 5}{(x+2)^2} = \frac{3x + 6 + 5}{(x+2)^2} = \frac{3x + 11}{(x+2)^2}
$$

$$
\boxed{\frac{3}{x+2} + \frac{5}{(x+2)^2} = \frac{3x + 11}{(x+2)^2}}
$$

---

### Ejemplo 8

Resolver $\dfrac{2}{x-3} - \dfrac{1}{x^2-9}$.

**Paso 1:** Factorizamos $x^2-9 = (x+3)(x-3)$.

**Paso 2:** El MCM es $(x+3)(x-3)$.

**Paso 3:** Convertimos y restamos:

$$
\frac{2(x+3)}{(x+3)(x-3)} - \frac{1}{(x+3)(x-3)} = \frac{2(x+3) - 1}{(x+3)(x-3)}
$$

$$
= \frac{2x + 6 - 1}{(x+3)(x-3)} = \frac{2x + 5}{(x+3)(x-3)}
$$

$$
\boxed{\frac{2}{x-3} - \frac{1}{x^2-9} = \frac{2x + 5}{x^2 - 9}}
$$

---

### Ejemplo 9

Resolver $\dfrac{x}{x^2-4} + \dfrac{1}{x+2}$.

**Paso 1:** Factorizamos $x^2-4 = (x+2)(x-2)$.

**Paso 2:** El MCM es $(x+2)(x-2)$.

**Paso 3:** Operamos:

$$
\frac{x}{(x+2)(x-2)} + \frac{(x-2)}{(x+2)(x-2)} = \frac{x + x - 2}{(x+2)(x-2)}
$$

$$
= \frac{2x - 2}{(x+2)(x-2)} = \frac{2(x-1)}{(x+2)(x-2)}
$$

$$
\boxed{\frac{x}{x^2-4} + \frac{1}{x+2} = \frac{2(x-1)}{x^2-4}}
$$

---

### Ejemplo 10

Resolver $\dfrac{3}{x^2+5x+6} + \dfrac{2}{x+2}$.

**Paso 1:** Factorizamos $x^2+5x+6 = (x+2)(x+3)$.

**Paso 2:** El MCM es $(x+2)(x+3)$.

**Paso 3:** Operamos:

$$
\frac{3}{(x+2)(x+3)} + \frac{2(x+3)}{(x+2)(x+3)}
$$

$$
= \frac{3 + 2(x+3)}{(x+2)(x+3)} = \frac{3 + 2x + 6}{(x+2)(x+3)} = \frac{2x + 9}{(x+2)(x+3)}
$$

$$
\boxed{\frac{3}{x^2+5x+6} + \frac{2}{x+2} = \frac{2x + 9}{(x+2)(x+3)}}
$$

---

## 📋 Resumen del proceso

| Paso | Descripción |
|:----:|:------------|
| 1 | Factorizar los denominadores |
| 2 | Encontrar el MCM (denominador común) |
| 3 | Multiplicar cada fracción para obtener el denominador común |
| 4 | Sumar o restar los numeradores |
| 5 | Simplificar si es posible |

---

## 📝 Ejercicios de práctica

### Denominadores monomios

**Ejercicio 1:** Resuelve $\dfrac{4}{x} + \dfrac{3}{x^2}$.

<details>
<summary>Ver solución</summary>

El MCM es $x^2$:

$$
\frac{4x}{x^2} + \frac{3}{x^2} = \frac{4x + 3}{x^2}
$$

</details>

---

**Ejercicio 2:** Resuelve $\dfrac{5}{2x} - \dfrac{3}{4x^2}$.

<details>
<summary>Ver solución</summary>

El MCM es $4x^2$:

$$
\frac{10x}{4x^2} - \frac{3}{4x^2} = \frac{10x - 3}{4x^2}
$$

</details>

---

### Denominadores binomios

**Ejercicio 3:** Resuelve $\dfrac{4}{x-2} + \dfrac{3}{x+5}$.

<details>
<summary>Ver solución</summary>

$$
\frac{4(x+5) + 3(x-2)}{(x-2)(x+5)} = \frac{4x + 20 + 3x - 6}{(x-2)(x+5)} = \frac{7x + 14}{(x-2)(x+5)}
$$

$$
= \frac{7(x+2)}{(x-2)(x+5)}
$$

</details>

---

**Ejercicio 4:** Resuelve $\dfrac{x}{x+1} - \dfrac{x}{x-1}$.

<details>
<summary>Ver solución</summary>

$$
\frac{x(x-1) - x(x+1)}{(x+1)(x-1)} = \frac{x^2 - x - x^2 - x}{x^2-1} = \frac{-2x}{x^2-1}
$$

</details>

---

### Denominadores factorizables

**Ejercicio 5:** Resuelve $\dfrac{1}{x-4} + \dfrac{3}{x^2-16}$.

<details>
<summary>Ver solución</summary>

$x^2 - 16 = (x+4)(x-4)$, MCM = $(x+4)(x-4)$:

$$
\frac{(x+4) + 3}{(x+4)(x-4)} = \frac{x + 7}{x^2 - 16}
$$

</details>

---

**Ejercicio 6:** Resuelve $\dfrac{2}{x^2-9} + \dfrac{5}{x-3}$.

<details>
<summary>Ver solución</summary>

$x^2 - 9 = (x+3)(x-3)$, MCM = $(x+3)(x-3)$:

$$
\frac{2 + 5(x+3)}{(x+3)(x-3)} = \frac{2 + 5x + 15}{x^2-9} = \frac{5x + 17}{x^2-9}
$$

</details>

---
