---
title: "Identidades Pitagóricas"
---

# **Identidades Pitagóricas**

Si Pitágoras estuviera vivo hoy, estaría orgulloso de ver que su famoso teorema ($a^2 + b^2 = c^2$) no solo sirve para triángulos, sino que es el corazón de toda la trigonometría. Las **Identidades Pitagóricas** son herramientas mágicas que nos permiten transformar senos en cosenos y tangentes en secantes con un chasquido de dedos.

---

## 🎯 ¿Qué vas a aprender?

- El origen de la identidad reina: $\sin^2(x) + \cos^2(x) = 1$.
- Cómo deducir las otras dos identidades pitagóricas sin memorizarlas.
- Cómo usar estas identidades para simplificar ecuaciones complejas.
- Cómo encontrar el valor de cualquier función trigonométrica si solo conoces una.

---

## 👑 La Identidad Fundamental

Imagina un triángulo rectángulo dentro del Círculo Unitario (radio = 1).
*   El cateto horizontal es $x = \cos(\theta)$.
*   El cateto vertical es $y = \sin(\theta)$.
*   La hipotenusa es el radio $r = 1$.

Aplicando Pitágoras ($cateto^2 + cateto^2 = hipotenusa^2$):

$$
(\cos\theta)^2 + (\sin\theta)^2 = 1^2
$$

O escrito en notación trigonométrica estándar:

$$
\sin^2\theta + \cos^2\theta = 1
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Identidad Pitagórica en el Círculo Unitario</strong>
  </div>

![Identidad pitagórica](/images/trigonometria/identidades/identidad-pitagorica.svg)

</div>

### Despejes Útiles
De esta fórmula madre nacen dos hijos muy útiles:

**1. Para hallar el Seno:**
$$
\sin^2\theta = 1 - \cos^2\theta
$$

**2. Para hallar el Coseno:**
$$
\cos^2\theta = 1 - \sin^2\theta
$$

---

## 🎩 Magia Algebraica: Las Otras Dos Identidades

No necesitas memorizar más fórmulas. Solo necesitas saber dividir.

### 1. La Identidad de Tangente y Secante
Divide toda la ecuación principal por $\cos^2\theta$:

$$
\frac{\sin^2\theta}{\cos^2\theta} + \frac{\cos^2\theta}{\cos^2\theta} = \frac{1}{\cos^2\theta}
$$

Como $\sin/\cos = \tan$ y $1/\cos = \sec$, obtenemos:

$$
\tan^2\theta + 1 = \sec^2\theta
$$

### 2. La Identidad de Cotangente y Cosecante
Divide toda la ecuación principal por $\sin^2\theta$:

$$
\frac{\sin^2\theta}{\sin^2\theta} + \frac{\cos^2\theta}{\sin^2\theta} = \frac{1}{\sin^2\theta}
$$

Como $\cos/\sin = \cot$ y $1/\sin = \csc$, obtenemos:

$$
1 + \cot^2\theta = \csc^2\theta
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Hallar Coseno dado el Seno
Si $\sin(\theta) = 0.6$ y $\theta$ está en el primer cuadrante, halla $\cos(\theta)$.

**Paso 1: Usar la identidad**
$$
\cos^2\theta = 1 - \sin^2\theta
$$

**Paso 2: Sustituir**
$$
\cos^2\theta = 1 - (0.6)^2 = 1 - 0.36 = 0.64
$$

**Paso 3: Raíz cuadrada**
$$
\cos\theta = \sqrt{0.64} = 0.8
$$

**Resultado:** $\boxed{0.8}$

---

### Ejemplo 2: Simplificar una expresión
Simplifica la expresión: $(1 - \sin^2 x) \sec^2 x$.

**Paso 1: Identificar Pitágoras**
Sabemos que $1 - \sin^2 x = \cos^2 x$.

**Paso 2: Sustituir**
$$
(\cos^2 x) \cdot \sec^2 x
$$

**Paso 3: Usar recíprocos**
Como $\sec x = 1/\cos x$, entonces $\sec^2 x = 1/\cos^2 x$.

$$
\cos^2 x \cdot \frac{1}{\cos^2 x} = 1
$$

**Resultado:** $\boxed{1}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $\sin^2(45°) + \cos^2(45°)$ sin usar calculadora.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Según la identidad fundamental, $\sin^2\theta + \cos^2\theta$ siempre es 1, sin importar el ángulo.

**Respuesta:** $\boxed{1}$
</details>

---

### Ejercicio 2
Simplifica la expresión $\frac{1 - \cos^2\theta}{\sin\theta}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El numerador $1 - \cos^2\theta$ es igual a $\sin^2\theta$.
$$
\frac{\sin^2\theta}{\sin\theta} = \sin\theta
$$

**Respuesta:** $\boxed{\sin\theta}$
</details>

---

### Ejercicio 3
Si $\tan\theta = 3$ y el ángulo es agudo, ¿cuánto vale $\sec^2\theta$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Usamos $\sec^2\theta = \tan^2\theta + 1$.
$$
\sec^2\theta = 3^2 + 1 = 9 + 1 = 10
$$

**Respuesta:** $\boxed{10}$
</details>

---

### Ejercicio 4
Simplifica $\csc^2\theta - \cot^2\theta$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Despejamos de la identidad $1 + \cot^2\theta = \csc^2\theta$.
Si pasamos restando la cotangente: $1 = \csc^2\theta - \cot^2\theta$.

**Respuesta:** $\boxed{1}$
</details>

---

### Ejercicio 5
Calcula $\cos(\theta)$ si $\sin(\theta) = \frac{3}{5}$ (Primer cuadrante).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos^2\theta = 1 - (3/5)^2 = 1 - 9/25 = 16/25$.
$\cos\theta = \sqrt{16/25} = 4/5$.

**Respuesta:** $\boxed{\frac{4}{5}}$
</details>

---

### Ejercicio 6
Demuestra que $(\sec\theta + 1)(\sec\theta - 1) = \tan^2\theta$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es una diferencia de cuadrados: $a^2 - b^2$.
$$
\sec^2\theta - 1
$$
Por identidad, sabemos que $\sec^2\theta - 1 = \tan^2\theta$.

**Respuesta:** **Q.E.D.**
</details>

---

### Ejercicio 7
Simplifica $\cos\theta \cdot \tan\theta$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Convertimos tangente a seno/coseno.
$$
\cos\theta \cdot \frac{\sin\theta}{\cos\theta}
$$
Se cancelan los cosenos.

**Respuesta:** $\boxed{\sin\theta}$
</details>

---

### Ejercicio 8
Expresa $\sin^4\theta - \cos^4\theta$ en términos de seno y coseno más simples.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es diferencia de cuadrados: $(\sin^2\theta - \cos^2\theta)(\sin^2\theta + \cos^2\theta)$.
El segundo paréntesis es 1.
Queda: $\sin^2\theta - \cos^2\theta$.

**Respuesta:** $\boxed{\sin^2\theta - \cos^2\theta}$
</details>

---

### Ejercicio 9
Si $\csc\theta = 2$, halla $\cot\theta$ (Q1).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$1 + \cot^2\theta = \csc^2\theta$.
$1 + \cot^2\theta = 2^2 = 4$.
$\cot^2\theta = 3$.

**Respuesta:** $\boxed{\sqrt{3}}$
</details>

---

### Ejercicio 10
Simplifica $\frac{1}{\sec^2\theta} + \frac{1}{\csc^2\theta}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Recíprocos: $\frac{1}{\sec^2\theta} = \cos^2\theta$ y $\frac{1}{\csc^2\theta} = \sin^2\theta$.
$$
\cos^2\theta + \sin^2\theta = 1
$$

**Respuesta:** $\boxed{1}$
</details>

---

## 🔑 Resumen

| Identidad Base | ¿Para qué sirve? | Relaciona |
| :--- | :--- | :--- |
| $\sin^2 + \cos^2 = 1$ | La más usada. Fundamental. | Seno y Coseno |
| $\tan^2 + 1 = \sec^2$ | Útil en cálculo e integración. | Tangente y Secante |
| $1 + \cot^2 = \csc^2$ | La hermana gemela de la anterior. | Cotangente y Cosecante |

> **Conclusión:** Si ves un "cuadrado" en una función trigonométrica, piensa inmediatamente en Pitágoras. ¡Casi siempre es la llave para simplificar el problema!
