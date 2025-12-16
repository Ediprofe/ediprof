# Notación de Límites

La notación matemática para límites es precisa y expresiva. Dominarla te permitirá comunicar ideas complejas de manera clara y concisa.

---

## 🎯 ¿Qué vas a aprender?

- Notación estándar para límites
- Cómo leer y escribir límites
- Límites laterales y su notación
- Límites infinitos y en el infinito

---

## 📖 Notación básica

$$\lim_{x \to a} f(x) = L$$

| Símbolo | Significado |
|---------|-------------|
| $\lim$ | "Límite de" |
| $x \to a$ | "$x$ tiende a $a$" o "$x$ se acerca a $a$" |
| $f(x)$ | La función que estamos evaluando |
| $= L$ | "Es igual a $L$" |

### Lectura completa

"El límite de $f(x)$ cuando $x$ tiende a $a$ es igual a $L$."

---

## 📖 Límites laterales

### Por la izquierda

$$\lim_{x \to a^-} f(x) = L$$

El superíndice $-$ indica que $x$ se acerca desde valores **menores** que $a$.

También se escribe: $\lim_{x \to a^{-}}$ o $\lim_{x \nearrow a}$

### Por la derecha

$$\lim_{x \to a^+} f(x) = L$$

El superíndice $+$ indica que $x$ se acerca desde valores **mayores** que $a$.

También se escribe: $\lim_{x \to a^{+}}$ o $\lim_{x \searrow a}$

---

## 📖 Límites infinitos

Cuando la función crece sin cota:

$$\lim_{x \to a} f(x) = +\infty$$

"$f(x)$ tiende a infinito positivo cuando $x$ tiende a $a$."

$$\lim_{x \to a} f(x) = -\infty$$

"$f(x)$ tiende a infinito negativo cuando $x$ tiende a $a$."

### ⚠️ Nota importante

Cuando escribimos $= \infty$, **no** significa que el límite existe en el sentido tradicional. Es una forma de describir el comportamiento.

---

## 📖 Límites en el infinito

Cuando $x$ crece sin cota:

$$\lim_{x \to +\infty} f(x) = L$$

"Cuando $x$ tiende a infinito (positivo), $f(x)$ se acerca a $L$."

$$\lim_{x \to -\infty} f(x) = L$$

"Cuando $x$ tiende a menos infinito, $f(x)$ se acerca a $L$."

---

## ⚙️ Ejemplo 1: Escribir en notación de límites

"Cuando $x$ se acerca a 5, $f(x) = x^2$ se acerca a 25."

$$\lim_{x \to 5} x^2 = 25$$

---

## ⚙️ Ejemplo 2: Límites laterales

Para $f(x) = \frac{1}{x}$:

**Por la derecha de 0:**
$$\lim_{x \to 0^+} \frac{1}{x} = +\infty$$

**Por la izquierda de 0:**
$$\lim_{x \to 0^-} \frac{1}{x} = -\infty$$

---

## ⚙️ Ejemplo 3: Límites en el infinito

Para $f(x) = \frac{1}{x}$:

$$\lim_{x \to +\infty} \frac{1}{x} = 0$$

$$\lim_{x \to -\infty} \frac{1}{x} = 0$$

La función se aproxima a 0 cuando $x$ es muy grande (en valor absoluto).

---

## 📖 Notación para "no existe"

Cuando un límite no existe, escribimos:

$$\lim_{x \to a} f(x) \text{ no existe}$$

O abreviado: $\nexists \lim_{x \to a} f(x)$

**Razones por las que puede no existir:**
1. Límites laterales diferentes
2. Oscilación infinita
3. Comportamiento errático

---

## ⚙️ Ejemplo 4: Límite que no existe

Para $f(x) = \sin\left(\frac{1}{x}\right)$ cuando $x \to 0$:

$$\lim_{x \to 0} \sin\left(\frac{1}{x}\right) \text{ no existe}$$

La función oscila infinitamente entre $-1$ y $1$ sin acercarse a ningún valor.

---

## 📖 Tabla de notaciones

| Expresión | Significado |
|-----------|-------------|
| $\lim_{x \to a} f(x) = L$ | Límite bilateral igual a $L$ |
| $\lim_{x \to a^+} f(x)$ | Límite por la derecha |
| $\lim_{x \to a^-} f(x)$ | Límite por la izquierda |
| $\lim_{x \to +\infty} f(x)$ | Límite cuando $x$ crece sin cota |
| $\lim_{x \to -\infty} f(x)$ | Límite cuando $x$ decrece sin cota |
| $\lim_{x \to a} f(x) = +\infty$ | La función crece sin cota |
| $\lim_{x \to a} f(x) = -\infty$ | La función decrece sin cota |

---

## 📖 Equivalencias importantes

El límite bilateral existe si y solo si:

$$\lim_{x \to a} f(x) = L \quad \Leftrightarrow \quad \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Escribe en notación de límites:

a) "Cuando $x$ se acerca a 2, $3x + 1$ se acerca a 7"
b) "Cuando $x$ crece sin límite, $\frac{1}{x^2}$ se acerca a 0"
c) "Cuando $x$ se acerca a 0 por la derecha, $\ln x$ decrece sin límite"

<details>
<summary>Ver soluciones</summary>

a) $\lim_{x \to 2} (3x + 1) = 7$

b) $\lim_{x \to +\infty} \frac{1}{x^2} = 0$

c) $\lim_{x \to 0^+} \ln x = -\infty$
</details>

---

**Ejercicio 2:** ¿Qué significa cada expresión?

a) $\lim_{x \to 3^-} f(x) = 5$
b) $\lim_{x \to -\infty} g(x) = 2$
c) $\lim_{x \to 0} h(x) = +\infty$

<details>
<summary>Ver soluciones</summary>

a) Cuando $x$ se acerca a 3 desde la izquierda (valores menores que 3), $f(x)$ se acerca a 5.

b) Cuando $x$ decrece sin cota (hacia menos infinito), $g(x)$ se acerca a 2.

c) Cuando $x$ se acerca a 0, $h(x)$ crece sin cota.
</details>
