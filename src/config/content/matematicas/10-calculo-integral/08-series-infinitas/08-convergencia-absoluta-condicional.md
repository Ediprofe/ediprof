---
title: "Convergencia Absoluta y Condicional"
---

# Convergencia Absoluta y Condicional

La distinción entre convergencia absoluta y condicional tiene implicaciones profundas sobre el comportamiento de las series.

---

## 🎯 ¿Qué vas a aprender?

- Definiciones precisas
- Propiedades de cada tipo
- Ejemplos característicos
- Teorema de reordenamiento

---

## 📖 Definiciones

**Convergencia absoluta:** $\sum a_n$ converge absolutamente si $\sum |a_n|$ converge.

**Convergencia condicional:** $\sum a_n$ converge pero $\sum |a_n|$ diverge.

---

## 📖 Teorema fundamental

> Si $\sum |a_n|$ converge, entonces $\sum a_n$ también converge.

Convergencia absoluta → Convergencia

(Pero no al revés)

---

## ⚙️ Ejemplo 1: Convergencia absoluta

$$
\sum \frac{(-1)^n}{n^2}
$$

$\sum \left|\frac{(-1)^n}{n^2}\right| = \sum \frac{1}{n^2}$ converge.

**Converge absolutamente.**

---

## ⚙️ Ejemplo 2: Convergencia condicional

$$
\sum \frac{(-1)^{n+1}}{n} = 1 - \frac{1}{2} + \frac{1}{3} - ...
$$

- Por Leibniz: converge ✓
- Pero $\sum \frac{1}{n}$ diverge ✗

**Converge condicionalmente.**

---

## 📖 Estrategia de análisis

1. Verificar si $\sum |a_n|$ converge
   - Si sí: convergencia absoluta
   - Si no: verificar si $\sum a_n$ converge (quizás condicionalmente)
2. Si $\sum |a_n|$ diverge pero $\sum a_n$ converge: condicional
3. Si ambas divergen: divergencia

---

## ⚙️ Ejemplo 3: Usando razón

$$
\sum \frac{(-1)^n 2^n}{n!}
$$

Con el criterio de razón para $|a_n|$:

$$
\frac{|a_{n+1}|}{|a_n|} = \frac{2}{n+1} \to 0 < 1
$$

**Converge absolutamente.**

---

## 📖 Teorema de Riemann

Una serie que converge condicionalmente puede ser reordenada para:
- Converger a cualquier número $L$
- Diverger a $+\infty$ o $-\infty$
- Oscilar sin converger

Las series absolutamente convergentes mantienen su suma bajo cualquier reordenamiento.

---

## ⚙️ Ejemplo 4: Análisis completo

$$
\sum_{n=1}^{\infty} \frac{(-1)^n}{\sqrt{n}}
$$

**Convergencia de la serie:**
Por Leibniz: $\frac{1}{\sqrt{n}} \to 0$ y decrece → converge

**Convergencia absoluta:**
$\sum \frac{1}{\sqrt{n}}$ es serie p con p = 1/2 < 1 → diverge

**Conclusión:** Converge **condicionalmente**.

---

## 📊 Resumen

| Tipo | $\sum |a_n|$ | $\sum a_n$ | Propiedades |
|------|--------------|----------|-------------|
| Absoluta | Converge | Converge | Reordenable |
| Condicional | Diverge | Converge | No reordenable |
| Divergente | - | Diverge | - |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Clasifica la convergencia:

$$
\sum_{n=1}^{\infty} \frac{(-1)^n n}{2^n}
$$

<details>
<summary>Ver solución</summary>

$$
\frac{|a_{n+1}|}{|a_n|} = \frac{n+1}{2n} \to \frac{1}{2} < 1
$$

**Converge absolutamente.**
</details>

---

**Ejercicio 2:** Clasifica:

$$
\sum_{n=2}^{\infty} \frac{(-1)^n}{n\ln n}
$$

<details>
<summary>Ver solución</summary>

- Por Leibniz: $\frac{1}{n\ln n} \to 0$ y decrece → converge
- $\sum \frac{1}{n\ln n}$ diverge (criterio integral)

**Converge condicionalmente.**
</details>
