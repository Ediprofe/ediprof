---
title: "Concepto de Antiderivada"
---

# Concepto de Antiderivada

Si la derivación responde "¿cuánto cambia?", la antiderivación responde "¿qué función tiene esta derivada?". Es el proceso inverso de derivar.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una antiderivada
- Por qué hay infinitas antiderivadas
- La constante de integración
- Conexión con la derivación

---

## 📖 Definición

Una **antiderivada** (o primitiva) de $f(x)$ es una función $F(x)$ tal que:

$$
F'(x) = f(x)
$$

En palabras: $F$ es antiderivada de $f$ si al derivar $F$ obtenemos $f$.

---

## ⚙️ Ejemplo 1: Verificación

¿Es $F(x) = x^3$ una antiderivada de $f(x) = 3x^2$?

**Verificamos:**

$$
F'(x) = 3x^2 = f(x) \quad \checkmark
$$

Sí, $x^3$ es una antiderivada de $3x^2$.

---

## ⚙️ Ejemplo 2: Otra verificación

¿Es $F(x) = x^3 + 5$ también antiderivada de $f(x) = 3x^2$?

**Verificamos:**

$$
F'(x) = 3x^2 + 0 = 3x^2 \quad \checkmark
$$

¡También lo es!

---

## 📖 Infinitas antiderivadas

Si $F(x)$ es antiderivada de $f(x)$, entonces $F(x) + C$ también lo es para cualquier constante $C$.

**Razón:**

$$
(F(x) + C)' = F'(x) + 0 = f(x)
$$

Las antiderivadas difieren solo en una constante.

---

## 📖 La familia de antiderivadas

La **familia de antiderivadas** de $f(x)$ se escribe:

$$
F(x) + C
$$

donde $C$ es la **constante de integración**.

---

## ⚙️ Ejemplo 3: Familia completa

Encuentra todas las antiderivadas de $f(x) = 2x$.

**Pensamos:** ¿Qué función al derivarla da $2x$?

$$
\frac{d}{dx}[x^2] = 2x \quad \checkmark
$$

**Familia de antiderivadas:**

$$
x^2 + C
$$

---

## ⚙️ Ejemplo 4: De constante

Encuentra las antiderivadas de $f(x) = 5$.

**Pensamos:** ¿Qué función da $5$ al derivarla?

$$
\frac{d}{dx}[5x] = 5 \quad \checkmark
$$

**Antiderivadas:**

$$
5x + C
$$

---

## ⚙️ Ejemplo 5: Función seno

Encuentra las antiderivadas de $f(x) = \cos x$.

**Pensamos:**

$$
\frac{d}{dx}[\sin x] = \cos x \quad \checkmark
$$

**Antiderivadas:**

$$
\sin x + C
$$

---

## 📖 Notación

La antiderivación también se llama **integración**, y usamos el símbolo integral:

$$
\int f(x)\,dx = F(x) + C
$$

donde:
- $\int$ = símbolo de integral
- $f(x)$ = integrando
- $dx$ = variable de integración
- $F(x) + C$ = antiderivada general

---

## 📖 Derivación vs. Antiderivación

| Derivación | Antiderivación |
|------------|----------------|
| $f(x) \to f'(x)$ | $f(x) \to \int f(x)\,dx$ |
| Respuesta única | Familia de respuestas ($+C$) |
| "Pendiente de tangente" | "Área bajo la curva" |
| Proceso directo | Proceso inverso |

---

## 📖 Verificación

Para verificar una antiderivada, derivamos el resultado:

$$
\frac{d}{dx}\left[\int f(x)\,dx\right] = f(x)
$$

---

## ⚙️ Ejemplo 6: Verificar integral

Si $\int (3x^2 + 2)\,dx = x^3 + 2x + C$, verificar.

$$
\frac{d}{dx}[x^3 + 2x + C] = 3x^2 + 2 \quad \checkmark
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra todas las antiderivadas:

a) $f(x) = x^4$
b) $f(x) = \sin x$
c) $f(x) = e^x$

<details>
<summary>Ver soluciones</summary>

a) 

$$
\frac{x^5}{5} + C
$$

Verificar: $\frac{d}{dx}\left[\frac{x^5}{5}\right] = x^4$ ✓

b) 

$$
-\cos x + C
$$

Verificar: $\frac{d}{dx}[-\cos x] = \sin x$ ✓

c) 

$$
e^x + C
$$

Verificar: $\frac{d}{dx}[e^x] = e^x$ ✓

</details>

---

**Ejercicio 2:** Verifica que $F(x) = x^2 - 3x + 7$ es antiderivada de $f(x) = 2x - 3$.

<details>
<summary>Ver solución</summary>

$$
F'(x) = 2x - 3 = f(x) \quad \checkmark
$$

</details>
