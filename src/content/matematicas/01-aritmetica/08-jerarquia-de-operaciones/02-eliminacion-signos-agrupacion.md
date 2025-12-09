# 🔗 Eliminación de Signos de Agrupación

En este tema aprenderemos a resolver operaciones que incluyen paréntesis, corchetes y llaves.

---

## 📖 Signos de agrupación

Los **signos de agrupación** indican qué operaciones deben realizarse primero.

| Símbolo | Nombre | Ejemplo |
|---------|--------|---------|
| $( \; )$ | Paréntesis | $(3 + 2)$ |
| $[ \; ]$ | Corchetes | $[4 - 1]$ |
| $\{ \; \}$ | Llaves | $\{5 + 3\}$ |

---

## 📖 Orden de resolución

Cuando hay varios niveles de agrupación, resolvemos de **adentro hacia afuera**:

$$
\text{Paréntesis} \rightarrow \text{Corchetes} \rightarrow \text{Llaves}
$$

---

## 📖 Reglas para eliminar signos de agrupación

### Signo positivo delante

Si hay un $+$ antes del paréntesis, los signos interiores **no cambian**.

$$
+(a - b + c) = a - b + c
$$

### Signo negativo delante

Si hay un $-$ antes del paréntesis, los signos interiores **cambian**.

$$
-(a - b + c) = -a + b - c
$$

---

## 📖 Ejemplo paso a paso

Calcular: $15 - (8 - 3) + 2$

**Paso 1:** Resolver el paréntesis

$$
15 - \underbrace{(8 - 3)}_{5} + 2
$$

**Paso 2:** Operar

$$
15 - 5 + 2 = 12
$$

$$
\boxed{15 - (8 - 3) + 2 = 12}
$$

---

## 📖 Ejemplo con signos anidados

Calcular: $20 - [5 + (3 - 1)]$

**Paso 1:** Paréntesis interno

$$
20 - [5 + \underbrace{(3 - 1)}_{2}]
$$

**Paso 2:** Corchetes

$$
20 - \underbrace{[5 + 2]}_{7}
$$

**Paso 3:** Resta final

$$
20 - 7 = 13
$$

$$
\boxed{20 - [5 + (3 - 1)] = 13}
$$

---

## 📖 Ejemplo con cambio de signos

Calcular: $10 - (4 - 7 + 2)$

**Paso 1:** Eliminar paréntesis (signo negativo delante, cambiamos signos)

$$
10 - 4 + 7 - 2
$$

**Paso 2:** Operar

$$
= 6 + 7 - 2 = 11
$$

$$
\boxed{10 - (4 - 7 + 2) = 11}
$$

---

## ⚙️ Ejercicio 1 — Paréntesis simples

1. $(5 + 3) \times 2$
2. $15 - (4 + 6)$
3. $3 \times (8 - 2)$

### ✅ Solución

**1.** $(5 + 3) \times 2 = 8 \times 2 = \boxed{16}$

**2.** $15 - (4 + 6) = 15 - 10 = \boxed{5}$

**3.** $3 \times (8 - 2) = 3 \times 6 = \boxed{18}$

---

## ⚙️ Ejercicio 2 — Signos anidados

1. $25 - [10 - (3 + 2)]$
2. $\{20 - [8 + (5 - 3)]\} + 4$

### ✅ Solución

**1.** 
$$
25 - [10 - 5] = 25 - 5 = \boxed{20}
$$

**2.** 
$$
\{20 - [8 + 2]\} + 4 = \{20 - 10\} + 4 = 10 + 4 = \boxed{14}
$$

---

## ⚙️ Ejercicio 3 — Cambio de signos

1. $12 - (5 - 8)$
2. $-(3 - 7 + 2) + 10$
3. $8 + [-(4 - 1)]$

### ✅ Solución

**1.** $12 - 5 + 8 = \boxed{15}$

**2.** $-3 + 7 - 2 + 10 = \boxed{12}$

**3.** $8 + (-4 + 1) = 8 - 3 = \boxed{5}$

---

## ⚙️ Ejercicio 4 — Expresión compleja

Calcular: $\{18 - [10 - (4 + 3 \times 2)]\} \div 2$

### ✅ Solución

**Paso 1:** Multiplicación dentro del paréntesis

$$
4 + 3 \times 2 = 4 + 6 = 10
$$

**Paso 2:** Paréntesis

$$
10 - 10 = 0
$$

**Paso 3:** Corchetes

$$
18 - 0 = 18
$$

**Paso 4:** División

$$
18 \div 2 = 9
$$

$$
\boxed{\{18 - [10 - (4 + 3 \times 2)]\} \div 2 = 9}
$$

---
