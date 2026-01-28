---
title: "Inecuaciones Lineales"
---

# Inecuaciones Lineales

¿Cómo encontrar todos los valores de $x$ que hacen verdadera una desigualdad? Eso es exactamente lo que haremos con las inecuaciones lineales: encontrar el **conjunto solución** de una desigualdad.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una inecuación lineal
- Cómo resolver inecuaciones de primer grado
- Representación gráfica en la recta numérica
- Expresar soluciones en notación de intervalo

---

## 📖 ¿Qué es una inecuación lineal?

Una **inecuación lineal** es una desigualdad que contiene una variable de primer grado (exponente 1). Su forma general es:

$$
ax + b < c \quad \text{(o con } >, \leq, \geq \text{)}
$$

**Diferencia clave con ecuaciones:**
- Una **ecuación** lineal tiene una solución única: $2x = 6 \Rightarrow x = 3$
- Una **inecuación** lineal tiene infinitas soluciones: $2x < 6 \Rightarrow x < 3$ (todos los números menores que 3)

---

## 📖 Método de resolución

Resolver una inecuación es similar a resolver una ecuación, pero con una regla crucial:

> ⚠️ **Si multiplicas o divides por un número negativo, debes INVERTIR el sentido de la desigualdad.**

### Pasos para resolver

1. Simplificar ambos lados (si es necesario)
2. Agrupar términos con $x$ a un lado y constantes al otro
3. Despejar $x$
4. Expresar la solución en notación de intervalo

---

## ⚙️ Ejemplo 1: Inecuación simple

Resolver: $3x - 5 > 7$

**Paso 1:** Sumamos 5 a ambos lados
$$
3x - 5 + 5 > 7 + 5
$$
$$
3x > 12
$$

**Paso 2:** Dividimos entre 3 (positivo, no cambia sentido)
$$
\frac{3x}{3} > \frac{12}{3}
$$
$$
x > 4
$$

**Solución:** $x \in (4, +\infty)$

**Representación gráfica:**

```
        ○━━━━━━━━━━━━━→
───────┼───────────────
       4
```

El círculo vacío ○ indica que 4 **no está incluido**.

---

## ⚙️ Ejemplo 2: Con coeficiente negativo

Resolver: $-2x + 6 \leq 10$

**Paso 1:** Restamos 6 a ambos lados
$$
-2x + 6 - 6 \leq 10 - 6
$$
$$
-2x \leq 4
$$

**Paso 2:** Dividimos entre $-2$ (**¡INVERTIMOS!**)
$$
\frac{-2x}{-2} \geq \frac{4}{-2}
$$
$$
x \geq -2
$$

**Solución:** $x \in [-2, +\infty)$

**Representación gráfica:**

```
        ●━━━━━━━━━━━━━→
───────┼───────────────
      -2
```

El círculo lleno ● indica que $-2$ **sí está incluido**.

---

## ⚙️ Ejemplo 3: Variable en ambos lados

Resolver: $5x - 3 < 2x + 9$

**Paso 1:** Restamos $2x$ a ambos lados
$$
5x - 2x - 3 < 2x - 2x + 9
$$
$$
3x - 3 < 9
$$

**Paso 2:** Sumamos 3 a ambos lados
$$
3x - 3 + 3 < 9 + 3
$$
$$
3x < 12
$$

**Paso 3:** Dividimos entre 3
$$
x < 4
$$

**Solución:** $x \in (-\infty, 4)$

---

## ⚙️ Ejemplo 4: Con paréntesis

Resolver: $2(x - 3) - 4 \geq 3(x + 1)$

**Paso 1:** Distribuimos los paréntesis
$$
2x - 6 - 4 \geq 3x + 3
$$
$$
2x - 10 \geq 3x + 3
$$

**Paso 2:** Restamos $3x$ a ambos lados
$$
2x - 3x - 10 \geq 3x - 3x + 3
$$
$$
-x - 10 \geq 3
$$

**Paso 3:** Sumamos 10 a ambos lados
$$
-x \geq 13
$$

**Paso 4:** Multiplicamos por $-1$ (**¡INVERTIMOS!**)
$$
x \leq -13
$$

**Solución:** $x \in (-\infty, -13]$

---

## ⚙️ Ejemplo 5: Con fracciones

Resolver: $\frac{x + 2}{3} - \frac{x - 1}{2} > 1$

**Paso 1:** Multiplicamos todo por el MCM (6)
$$
6 \cdot \frac{x + 2}{3} - 6 \cdot \frac{x - 1}{2} > 6 \cdot 1
$$
$$
2(x + 2) - 3(x - 1) > 6
$$

**Paso 2:** Distribuimos
$$
2x + 4 - 3x + 3 > 6
$$
$$
-x + 7 > 6
$$

**Paso 3:** Restamos 7
$$
-x > -1
$$

**Paso 4:** Multiplicamos por $-1$ (**¡INVERTIMOS!**)
$$
x < 1
$$

**Solución:** $x \in (-\infty, 1)$

---

## 📊 Resumen del método

| Situación | Acción |
|-----------|--------|
| Sumar/restar | No cambia el sentido |
| Multiplicar/dividir por $c > 0$ | No cambia el sentido |
| Multiplicar/dividir por $c < 0$ | **Cambia el sentido** |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve y expresa en notación de intervalo:

a) $4x - 7 > 5$
b) $-3x + 2 \leq 11$
c) $6 - 2x < 4x + 18$

<details>
<summary>Ver soluciones</summary>

a) $4x > 12 \Rightarrow x > 3$
   
   **Solución:** $(3, +\infty)$

b) $-3x \leq 9 \Rightarrow x \geq -3$ (invertimos al dividir por $-3$)
   
   **Solución:** $[-3, +\infty)$

c) $6 - 18 < 4x + 2x \Rightarrow -12 < 6x \Rightarrow -2 < x$
   
   **Solución:** $(-2, +\infty)$
</details>

---

**Ejercicio 2:** Resuelve las siguientes inecuaciones:

a) $3(x - 2) > 2(x + 1) - 5$
b) $\frac{2x - 1}{4} \geq \frac{x + 3}{2}$

<details>
<summary>Ver soluciones</summary>

a) $3x - 6 > 2x + 2 - 5 \Rightarrow 3x - 6 > 2x - 3 \Rightarrow x > 3$
   
   **Solución:** $(3, +\infty)$

b) Multiplicamos por 4: $2x - 1 \geq 2(x + 3) \Rightarrow 2x - 1 \geq 2x + 6$
   
   $-1 \geq 6$ es **FALSO**
   
   **Solución:** $\emptyset$ (conjunto vacío, no hay solución)
</details>
