---
title: "Identidades de Suma y Diferencia"
---

# **Identidades de Suma y Diferencia**

¿Cuánto vale $\sin(75°)$? No está en tu tabla de ángulos notables (30°, 45°, 60°), pero 75° es la suma de 30° y 45°. Las **identidades de suma y diferencia** son como llaves que te permiten romper ángulos difíciles en piezas fáciles que ya conoces.

---

## 🎯 ¿Qué vas a aprender?

- Las fórmulas para calcular senos y cosenos de sumas ($\alpha + \beta$).
- Las fórmulas para restas ($\alpha - \beta$) y tangentes.
- Cómo calcular valores exactos como $\cos(15°)$ sin calculadora.
- Cómo usar estas identidades para demostrar otras propiedades trigonométricas.

---

## ➕ Identidades del Seno

El seno es "amigable": mezcla senos con cosenos y **respeta** el signo.

### Suma
$$
\sin(\alpha + \beta) = \sin\alpha \cos\beta + \cos\alpha \sin\beta
$$

### Resta
$$
\sin(\alpha - \beta) = \sin\alpha \cos\beta - \cos\alpha \sin\beta
$$

> **Patrón:** "Seno-Coseno, Coseno-Seno". El signo se mantiene (+ con +, - con -).

---

## ➖ Identidades del Coseno

El coseno es "egoísta" y "contreras": se junta con su propia clase (coseno con coseno) y **cambia** el signo.

### Suma
$$
\cos(\alpha + \beta) = \cos\alpha \cos\beta - \sin\alpha \sin\beta
$$

### Resta
$$
\cos(\alpha - \beta) = \cos\alpha \cos\beta + \sin\alpha \sin\beta
$$

> **Patrón:** "Coseno-Coseno, Seno-Seno". El signo se invierte (+ se vuelve -, - se vuelve +).

---

## 📈 Identidades de la Tangente

### Suma
$$
\tan(\alpha + \beta) = \frac{\tan\alpha + \tan\beta}{1 - \tan\alpha \tan\beta}
$$

### Resta
$$
\tan(\alpha - \beta) = \frac{\tan\alpha - \tan\beta}{1 + \tan\alpha \tan\beta}
$$

> **Pista:** El signo de arriba es el mismo que el de la operación. El de abajo es el opuesto.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Calcular $\sin(75°)$
Rompemos 75° en $45° + 30°$.

$$
\sin(45° + 30°) = \sin(45°)\cos(30°) + \cos(45°)\sin(30°)
$$

Sustituimos valores conocidos:
$$
= \left(\frac{\sqrt{2}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) + \left(\frac{\sqrt{2}}{2}\right)\left(\frac{1}{2}\right)
$$

$$
= \frac{\sqrt{6}}{4} + \frac{\sqrt{2}}{4}
$$

**Resultado:** $\boxed{\frac{\sqrt{6} + \sqrt{2}}{4}}$

---

### Ejemplo 2: Calcular $\cos(15°)$
Rompemos 15° en $45° - 30°$. (O también $60° - 45°$).

$$
\cos(45° - 30°) = \cos(45°)\cos(30°) + \sin(45°)\sin(30°)
$$

$$
= \left(\frac{\sqrt{2}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) + \left(\frac{\sqrt{2}}{2}\right)\left(\frac{1}{2}\right)
$$

**Resultado:** $\boxed{\frac{\sqrt{6} + \sqrt{2}}{4}}$
*(¡Curioso! Es igual al seno de 75° porque son cofunciones).*

---

### Ejemplo 3: Simplificar $\cos(\pi - x)$
Usamos la fórmula de resta del coseno.

$$
\cos(\pi - x) = \cos(\pi)\cos(x) + \sin(\pi)\sin(x)
$$

Sabemos que $\cos(\pi) = -1$ y $\sin(\pi) = 0$.

$$
= (-1)\cos(x) + (0)\sin(x)
$$

**Resultado:** $\boxed{-\cos(x)}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Usa la fórmula de suma para encontrar $\sin(105°)$ ($60°+45°$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sin(60°+45°) = \sin 60°\cos 45° + \cos 60°\sin 45°$.
$(\frac{\sqrt{3}}{2})(\frac{\sqrt{2}}{2}) + (\frac{1}{2})(\frac{\sqrt{2}}{2})$.

**Respuesta:** $\boxed{\frac{\sqrt{6} + \sqrt{2}}{4}}$
</details>

---

### Ejercicio 2
Calcula $\cos(105°)$ usando suma.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos(60°+45°) = \cos 60°\cos 45° - \sin 60°\sin 45°$.
$(\frac{1}{2})(\frac{\sqrt{2}}{2}) - (\frac{\sqrt{3}}{2})(\frac{\sqrt{2}}{2})$.

**Respuesta:** $\boxed{\frac{\sqrt{2} - \sqrt{6}}{4}}$
</details>

---

### Ejercicio 3
Calcula $\tan(15°)$ usando resta ($45°-30°$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan(45°-30°) = \frac{\tan 45° - \tan 30°}{1 + \tan 45°\tan 30°}$.
$\frac{1 - \sqrt{3}/3}{1 + 1(\sqrt{3}/3)} = \frac{3-\sqrt{3}}{3+\sqrt{3}}$.
Racionalizando...

**Respuesta:** $\boxed{2 - \sqrt{3}}$
</details>

---

### Ejercicio 4
Verifica la identidad $\sin(x + \pi) = -\sin(x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sin(x)\cos(\pi) + \cos(x)\sin(\pi)$.
$\sin(x)(-1) + \cos(x)(0)$.

**Respuesta:** $-\sin(x)$
</details>

---

### Ejercicio 5
Simplifica $\cos(\frac{\pi}{2} + x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos(\frac{\pi}{2})\cos(x) - \sin(\frac{\pi}{2})\sin(x)$.
$0 \cdot \cos(x) - 1 \cdot \sin(x)$.

**Respuesta:** $\boxed{-\sin(x)}$
</details>

---

### Ejercicio 6
Halla el valor exacto de $\sin(15°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sin(45°-30°) = \sin 45°\cos 30° - \cos 45°\sin 30°$.
$(\frac{\sqrt{2}}{2})(\frac{\sqrt{3}}{2}) - (\frac{\sqrt{2}}{2})(\frac{1}{2})$.

**Respuesta:** $\boxed{\frac{\sqrt{6} - \sqrt{2}}{4}}$
</details>

---

### Ejercicio 7
Si $\sin A = 3/5$ y $\cos B = 12/13$ (ambos en Q1), halla $\sin(A+B)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos A = 4/5$, $\sin B = 5/13$.
$\sin(A+B) = (3/5)(12/13) + (4/5)(5/13)$.
$36/65 + 20/65$.

**Respuesta:** $\boxed{\frac{56}{65}}$
</details>

---

### Ejercicio 8
Simplifica $\cos(A+B) + \cos(A-B)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(\cos A \cos B - \sin A \sin B) + (\cos A \cos B + \sin A \sin B)$.
Se cancelan los senos.

**Respuesta:** $\boxed{2\cos A \cos B}$
</details>

---

### Ejercicio 9
Demuestra que $\tan(x + \pi) = \tan(x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{\tan x + \tan \pi}{1 - \tan x \tan \pi}$.
$\tan \pi = 0$.
$\frac{\tan x + 0}{1 - 0}$.

**Respuesta:** $\boxed{\tan x}$
</details>

---

### Ejercicio 10
Si $\alpha + \beta = 90°$, demuestra que $\sin(\alpha) = \cos(\beta)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\beta = 90° - \alpha$.
$\cos(90° - \alpha) = \cos 90° \cos \alpha + \sin 90° \sin \alpha$.
$0 + 1 \cdot \sin \alpha$.

**Respuesta:** $\boxed{\sin \alpha}$
</details>

---

## 🔑 Resumen

| Función | Operación ($\pm$) | Fórmula | Signo Resultado |
| :---: | :---: | :---: | :---: |
| **Seno** | $\alpha \pm \beta$ | $\sin \cos \pm \cos \sin$ | **Mismo** ($\pm$) |
| **Coseno** | $\alpha \pm \beta$ | $\cos \cos \mp \sin \sin$ | **Opuesto** ($\mp$) |
| **Tangente** | $\alpha \pm \beta$ | $\frac{\tan \pm \tan}{1 \mp \tan \tan}$ | Num: Mismo / Den: Opuesto |

> **Conclusión:** ¡El orden importa! Con el seno, mezcla las funciones. Con el coseno, agrupa las iguales. Y no olvides que el coseno siempre lleva la contraria con el signo.
