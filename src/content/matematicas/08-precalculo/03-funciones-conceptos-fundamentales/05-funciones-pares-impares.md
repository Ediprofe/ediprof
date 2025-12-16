# Funciones Pares e Impares

¿Por qué algunas gráficas son simétricas respecto al eje Y mientras que otras lo son respecto al origen? La respuesta está en la paridad de las funciones.

---

## 🎯 ¿Qué vas a aprender?

- Definición de función par
- Definición de función impar
- Simetría gráfica asociada
- Cómo verificar la paridad algebraicamente

---

## 📖 Función par

> Una función es **par** si $f(-x) = f(x)$ para todo $x$ en su dominio.

### Simetría asociada

Las funciones pares tienen **simetría respecto al eje Y**.

Esto significa que si el punto $(a, b)$ está en la gráfica, el punto $(-a, b)$ también está.

### Ejemplos clásicos de funciones pares

- $f(x) = x^2$
- $f(x) = x^4$
- $f(x) = |x|$
- $f(x) = \cos(x)$

---

## 📖 Función impar

> Una función es **impar** si $f(-x) = -f(x)$ para todo $x$ en su dominio.

### Simetría asociada

Las funciones impares tienen **simetría respecto al origen**.

Esto significa que si el punto $(a, b)$ está en la gráfica, el punto $(-a, -b)$ también está.

### Ejemplos clásicos de funciones impares

- $f(x) = x$
- $f(x) = x^3$
- $f(x) = \frac{1}{x}$
- $f(x) = \sin(x)$

---

## 📖 Funciones que no son ni pares ni impares

La mayoría de las funciones **no son ni pares ni impares**.

**Ejemplo:** $f(x) = x^2 + x$

Verificamos:
$$f(-x) = (-x)^2 + (-x) = x^2 - x$$

- ¿Es par? $f(-x) = x^2 - x \neq x^2 + x = f(x)$ ❌
- ¿Es impar? $f(-x) = x^2 - x \neq -(x^2 + x) = -x^2 - x$ ❌

**No es ni par ni impar.**

---

## ⚙️ Ejemplo 1: Verificar paridad de $f(x) = x^4 - 2x^2 + 1$

**Paso 1:** Calculamos $f(-x)$
$$f(-x) = (-x)^4 - 2(-x)^2 + 1 = x^4 - 2x^2 + 1$$

**Paso 2:** Comparamos con $f(x)$
$$f(-x) = x^4 - 2x^2 + 1 = f(x)$$

**Conclusión:** Es **función par** ✓

---

## ⚙️ Ejemplo 2: Verificar paridad de $f(x) = x^3 - x$

**Paso 1:** Calculamos $f(-x)$
$$f(-x) = (-x)^3 - (-x) = -x^3 + x$$

**Paso 2:** Comparamos con $-f(x)$
$$-f(x) = -(x^3 - x) = -x^3 + x$$

Vemos que $f(-x) = -f(x)$.

**Conclusión:** Es **función impar** ✓

---

## ⚙️ Ejemplo 3: Verificar paridad de $f(x) = \frac{x^2}{x + 1}$

**Paso 1:** Calculamos $f(-x)$
$$f(-x) = \frac{(-x)^2}{-x + 1} = \frac{x^2}{1 - x}$$

**Paso 2:** Comparamos
- $f(x) = \frac{x^2}{x + 1}$
- $f(-x) = \frac{x^2}{1 - x}$
- $-f(x) = \frac{-x^2}{x + 1}$

$f(-x) \neq f(x)$ y $f(-x) \neq -f(x)$

**Conclusión:** No es par ni impar.

---

## 📖 Propiedades algebraicas

| Operación | Resultado |
|-----------|-----------|
| Par $+$ Par | Par |
| Impar $+$ Impar | Impar |
| Par $+$ Impar | Ni par ni impar |
| Par $\times$ Par | Par |
| Impar $\times$ Impar | Par |
| Par $\times$ Impar | Impar |

---

## ⚙️ Ejemplo 4: Usando propiedades

Sea $f(x) = x^4$ (par) y $g(x) = x^3$ (impar).

**a) $h(x) = f(x) + g(x) = x^4 + x^3$**

Par + Impar = Ni par ni impar.

**b) $h(x) = f(x) \cdot g(x) = x^4 \cdot x^3 = x^7$**

Par × Impar = Impar.

Verificación: $(-x)^7 = -x^7 = -f(x)$ ✓

---

## 📖 Descomposición en parte par e impar

Cualquier función puede escribirse como:

$$f(x) = f_{\text{par}}(x) + f_{\text{impar}}(x)$$

donde:

$$f_{\text{par}}(x) = \frac{f(x) + f(-x)}{2}$$

$$f_{\text{impar}}(x) = \frac{f(x) - f(-x)}{2}$$

---

## ⚙️ Ejemplo 5: Descomponer $f(x) = e^x$

**Parte par:**
$$f_{\text{par}}(x) = \frac{e^x + e^{-x}}{2} = \cosh(x)$$

**Parte impar:**
$$f_{\text{impar}}(x) = \frac{e^x - e^{-x}}{2} = \sinh(x)$$

Verificamos: $\cosh(x) + \sinh(x) = \frac{e^x + e^{-x}}{2} + \frac{e^x - e^{-x}}{2} = e^x$ ✓

---

## 📊 Resumen visual

| Tipo | Condición algebraica | Simetría gráfica |
|------|---------------------|------------------|
| **Par** | $f(-x) = f(x)$ | Eje Y |
| **Impar** | $f(-x) = -f(x)$ | Origen |

### 💡 Tip para recordar

- **Par:** Los exponentes de $x$ son pares (como $x^2, x^4$)
- **Impar:** Los exponentes de $x$ son impares (como $x, x^3$)

Pero cuidado: esto solo funciona para polinomios con un solo término o términos del mismo tipo.

---

## ⚠️ Nota sobre el dominio

Para que una función sea par o impar, su dominio debe ser **simétrico respecto al origen**.

Es decir, si $x$ está en el dominio, entonces $-x$ también debe estar.

**Ejemplo:** $f(x) = \sqrt{x}$ no puede ser par ni impar porque su dominio $[0, +\infty)$ no es simétrico.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Determina si cada función es par, impar, o ninguna:

a) $f(x) = x^6 - 3x^2$
b) $g(x) = x^5 - 4x^3 + x$
c) $h(x) = x^3 + 2$

<details>
<summary>Ver soluciones</summary>

a) $f(-x) = (-x)^6 - 3(-x)^2 = x^6 - 3x^2 = f(x)$
   
   **Par** ✓

b) $g(-x) = (-x)^5 - 4(-x)^3 + (-x) = -x^5 + 4x^3 - x = -(x^5 - 4x^3 + x) = -g(x)$
   
   **Impar** ✓

c) $h(-x) = (-x)^3 + 2 = -x^3 + 2$
   
   $h(-x) \neq h(x)$ y $h(-x) \neq -h(x) = -x^3 - 2$
   
   **Ni par ni impar**
</details>

---

**Ejercicio 2:** Verifica la paridad:

a) $f(x) = \frac{x}{x^2 + 1}$
b) $g(x) = \frac{1}{x^2 - 4}$

<details>
<summary>Ver soluciones</summary>

a) $f(-x) = \frac{-x}{(-x)^2 + 1} = \frac{-x}{x^2 + 1} = -f(x)$
   
   **Impar** ✓

b) $g(-x) = \frac{1}{(-x)^2 - 4} = \frac{1}{x^2 - 4} = g(x)$
   
   **Par** ✓
</details>

---

**Ejercicio 3:** Si $f$ es par y $g$ es impar, determina la paridad de:

a) $f(x) \cdot g(x)$
b) $f(g(x))$
c) $g(f(x))$

<details>
<summary>Ver soluciones</summary>

a) Par × Impar = **Impar**

b) $f(g(-x)) = f(-g(x)) = f(g(x))$ (porque $f$ es par)
   
   **Par**

c) $g(f(-x)) = g(f(x))$ (porque $f$ es par)
   
   La composición no tiene paridad definida sin más información sobre $g$.
</details>
