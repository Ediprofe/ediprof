---
title: "Integración por Partes"
---

# Integración por Partes

La integración por partes es la "inversa" de la regla del producto para derivadas. Es esencial para integrar productos de funciones.

---

## 🎯 ¿Qué vas a aprender?

- La fórmula de integración por partes
- Cómo elegir $u$ y $dv$
- La regla ILATE
- Aplicaciones típicas

---

## 📖 La fórmula

$$
\boxed{\int u\,dv = uv - \int v\,du}
$$

Se deriva de la regla del producto: $(uv)' = u'v + uv'$

Integrando: $uv = \int u'v\,dx + \int uv'\,dx$

---

## 📖 Cómo aplicarla

1. **Identificar** $u$ y $dv$ en el integrando
2. **Calcular** $du$ (derivando $u$) y $v$ (integrando $dv$)
3. **Aplicar** la fórmula
4. **Resolver** la nueva integral $\int v\,du$

---

## 📖 Regla ILATE para elegir u

Elige como $u$ la función que aparezca primero en:

| Letra | Tipo de función |
|-------|-----------------|
| **I** | Inversas trigonométricas ($\arcsin$, $\arctan$, ...) |
| **L** | Logarítmicas ($\ln x$, $\log x$) |
| **A** | Algebraicas ($x$, $x^2$, polinomios) |
| **T** | Trigonométricas ($\sin$, $\cos$, ...) |
| **E** | Exponenciales ($e^x$, $a^x$) |

---

## ⚙️ Ejemplo 1: x por exponencial

Calcula:

$$
\int xe^x\,dx
$$

**Solución:** Por ILATE: $u = x$ (algebraica), $dv = e^x\,dx$

$du = dx$, $v = e^x$

$$
= xe^x - \int e^x\,dx = xe^x - e^x + C = e^x(x-1) + C
$$

---

## ⚙️ Ejemplo 2: Logaritmo

Calcula:

$$
\int \ln x\,dx
$$

**Solución:** $u = \ln x$, $dv = dx$

$du = \frac{1}{x}\,dx$, $v = x$

$$
= x\ln x - \int x \cdot \frac{1}{x}\,dx = x\ln x - \int 1\,dx
$$

$$
= x\ln x - x + C = x(\ln x - 1) + C
$$

---

## ⚙️ Ejemplo 3: x por seno

Calcula:

$$
\int x\sin x\,dx
$$

**Solución:** $u = x$, $dv = \sin x\,dx$

$du = dx$, $v = -\cos x$

$$
= -x\cos x - \int (-\cos x)\,dx = -x\cos x + \sin x + C
$$

---

## ⚙️ Ejemplo 4: Doble aplicación

Calcula:

$$
\int x^2 e^x\,dx
$$

**Primera vez:** $u = x^2$, $dv = e^x\,dx$

$$
= x^2 e^x - \int 2xe^x\,dx
$$

**Segunda vez:** Ya resolvimos $\int xe^x\,dx = e^x(x-1)$

$$
= x^2 e^x - 2e^x(x-1) + C = e^x(x^2 - 2x + 2) + C
$$

---

## ⚙️ Ejemplo 5: Truco cíclico

Calcula:

$$
\int e^x \sin x\,dx
$$

**Solución:** $u = e^x$, $dv = \sin x\,dx$ → $du = e^x\,dx$, $v = -\cos x$

$$
= -e^x\cos x + \int e^x\cos x\,dx
$$

Ahora para $\int e^x\cos x\,dx$: $u = e^x$, $dv = \cos x\,dx$

$$
= e^x\sin x - \int e^x\sin x\,dx
$$

Sustituyendo:

$$
I = -e^x\cos x + e^x\sin x - I
$$

$$
2I = e^x(\sin x - \cos x)
$$

$$
I = \frac{e^x(\sin x - \cos x)}{2} + C
$$

---

## ⚙️ Ejemplo 6: Arco tangente

Calcula:

$$
\int \arctan x\,dx
$$

**Solución:** $u = \arctan x$, $dv = dx$

$du = \frac{1}{1+x^2}\,dx$, $v = x$

$$
= x\arctan x - \int \frac{x}{1+x^2}\,dx
$$

Para la segunda integral: $w = 1 + x^2$, $dw = 2x\,dx$

$$
= x\arctan x - \frac{1}{2}\ln(1+x^2) + C
$$

---

## 📖 Fórmula tabular (para múltiples partes)

Para $\int x^n e^{ax}\,dx$ o similares, se puede usar una tabla:

| $u$ y derivadas | $dv$ e integrales | Signos |
|-----------------|-------------------|--------|
| $x^2$ | $e^x$ | $+$ |
| $2x$ | $e^x$ | $-$ |
| $2$ | $e^x$ | $+$ |
| $0$ | $e^x$ | |

Resultado: $x^2e^x - 2xe^x + 2e^x + C$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

a) $\int x\cos x\,dx$
b) $\int x^2 \ln x\,dx$

<details>
<summary>Ver soluciones</summary>

a) $u = x$, $dv = \cos x\,dx$
   
$$
= x\sin x - \int \sin x\,dx = x\sin x + \cos x + C
$$

b) $u = \ln x$, $dv = x^2\,dx$
   
$$
= \frac{x^3}{3}\ln x - \int \frac{x^3}{3} \cdot \frac{1}{x}\,dx
$$
   
$$
= \frac{x^3}{3}\ln x - \frac{x^3}{9} + C
$$

</details>

---

**Ejercicio 2:** Calcula:

$$
\int e^x \cos x\,dx
$$

<details>
<summary>Ver solución</summary>

Similar al ejemplo 5:

$$
I = e^x\cos x + e^x\sin x - I
$$

$$
I = \frac{e^x(\sin x + \cos x)}{2} + C
$$

</details>
