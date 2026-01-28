---
title: "Identidades del Ángulo Doble"
---

# **Identidades del Ángulo Doble**

¿Sabías que el seno del doble de un ángulo no es simplemente el doble del seno? ¡Si fuera tan fácil, los matemáticos estarían aburridos! Las **identidades del ángulo doble** son atajos poderosos que te permiten calcular el seno, coseno y tangente de $2x$ usando solo las medidas de $x$.

---

## 🎯 ¿Qué vas a aprender?

- Cómo calcular $\sin(2x)$, $\cos(2x)$ y $\tan(2x)$.
- Las tres versiones diferentes del coseno del ángulo doble.
- Cómo usar estas fórmulas para simplificar ecuaciones largas.
- Cómo hallar el valor exacto de funciones trigonométricas sin calculadora.

---

## 🧬 El Origen

Estas identidades son hijas directas de las **fórmulas de suma**.
Simplemente hacemos que $\alpha = x$ y $\beta = x$.
Entonces $\alpha + \beta = 2x$.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Resumen: Fórmulas del Ángulo Doble</strong>
  </div>

![Fórmulas ángulo doble](/images/trigonometria/identidades/angulo-doble.svg)

</div>

---

## 🔵 Seno del Ángulo Doble

$$
\sin(2x) = 2\sin(x)\cos(x)
$$

> **Nota:** ¡No distribuyas el 2! $\sin(2x) \neq 2\sin(x)$.

---

## 🔴 Coseno del Ángulo Doble

El coseno es especial; tiene tres identidades equivalentes. Puedes usar cualquiera, dependiendo de lo que tengas a mano.

### 1. La Clásica (Seno y Coseno)
$$
\cos(2x) = \cos^2(x) - \sin^2(x)
$$

### 2. Solo Coseno
$$
\cos(2x) = 2\cos^2(x) - 1
$$

### 3. Solo Seno
$$
\cos(2x) = 1 - 2\sin^2(x)
$$

---

## 📐 Tangente del Ángulo Doble

$$
\tan(2x) = \frac{2\tan(x)}{1 - \tan^2(x)}
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Calcular $\sin(120°)$
Usamos $x = 60°$.
$$
\sin(120°) = \sin(2 \cdot 60°) = 2\sin(60°)\cos(60°)
$$
$$
= 2\left(\frac{\sqrt{3}}{2}\right)\left(\frac{1}{2}\right) = \frac{\sqrt{3}}{2}
$$
**Resultado:** $\boxed{\frac{\sqrt{3}}{2}}$

### Ejemplo 2: Calcular $\cos(2x)$ si $\sin(x) = 3/5$
Usamos la fórmula que solo tiene seno:
$$
\cos(2x) = 1 - 2\sin^2(x)
$$
$$
= 1 - 2\left(\frac{3}{5}\right)^2 = 1 - 2\left(\frac{9}{25}\right)
$$
$$
= 1 - \frac{18}{25} = \frac{25-18}{25}
$$
**Resultado:** $\boxed{\frac{7}{25}}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si $\sin x = 4/5$ (x en Q1), halla $\sin 2x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si $\sin x = 4/5$, entonces $\cos x = 3/5$ (triángulo 3-4-5).
$\sin 2x = 2(4/5)(3/5)$.

**Respuesta:** $\boxed{\frac{24}{25}}$
</details>

---

### Ejercicio 2
Si $\cos x = 5/13$ (x en Q1), halla $\cos 2x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Usamos la fórmula de solo coseno: $2\cos^2 x - 1$.
$2(5/13)^2 - 1 = 2(25/169) - 1 = 50/169 - 169/169$.

**Respuesta:** $\boxed{-\frac{119}{169}}$
</details>

---

### Ejercicio 3
Simplifica $2\sin(15°)\cos(15°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es la fórmula de seno doble: $\sin(2 \cdot 15°) = \sin(30°)$.

**Respuesta:** $\boxed{0.5}$
</details>

---

### Ejercicio 4
Simplifica $\cos^2(22.5°) - \sin^2(22.5°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es la fórmula de coseno doble: $\cos(2 \cdot 22.5°) = \cos(45°)$.

**Respuesta:** $\boxed{\frac{\sqrt{2}}{2}}$
</details>

---

### Ejercicio 5
Calcula $\tan 2x$ si $\tan x = 3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{2(3)}{1 - 3^2} = \frac{6}{1 - 9} = \frac{6}{-8}$.

**Respuesta:** $\boxed{-\frac{3}{4}}$
</details>

---

### Ejercicio 6
Demuestra que $\frac{\sin 2x}{2\sin x} = \cos x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{2\sin x \cos x}{2\sin x} = \cos x$.
Se cancelan términos.

**Respuesta:** $\boxed{\cos x}$
</details>

---

### Ejercicio 7
Si $\cos 2x = 1/2$, halla $x$ (0 a 90°).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2x = 60°$ (porque $\cos 60° = 0.5$).
$x = 30°$.

**Respuesta:** $\boxed{30°}$
</details>

---

### Ejercicio 8
Simplifica $1 - 2\sin^2(3x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es la fórmula de coseno doble con argumento $3x$.
$\cos(2 \cdot 3x) = \cos(6x)$.

**Respuesta:** $\boxed{\cos(6x)}$
</details>

---

### Ejercicio 9
Usa indentidades para hallar $\cos 2x$ si $\sin x = 1/\sqrt{2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$1 - 2(1/\sqrt{2})^2 = 1 - 2(1/2) = 1 - 1 = 0$.
Nota: $x$ era 45°, así que $2x$ es 90°.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 10
Demuestra $(\sin x + \cos x)^2 = 1 + \sin 2x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sin^2 x + 2\sin x \cos x + \cos^2 x$.
$(\sin^2 x + \cos^2 x) + (2\sin x \cos x)$.
$1 + \sin 2x$.

**Respuesta:** **Q.E.D.**
</details>

---

## 🔑 Resumen

| Función Doble | Fórmula Principal | Se usa para... |
| :---: | :---: | :--- |
| **Seno** | $2\sin x \cos x$ | Simplificar productos sin-cos. |
| **Coseno** | $\cos^2 x - \sin^2 x$ | Pasar de cuadrados a ángulo simple. |
| **Tangente** | $\frac{2\tan x}{1-\tan^2 x}$ | Ángulos en términos de pendientes. |

> **Conclusión:** Las identidades de ángulo doble son herramientas de reducción. Te permiten transformar potencias ($\sin^2$) en múltiplos de ángulo ($\cos 2x$), lo cual es vital en Cálculo Integral.
