---
title: "Transformación de Productos a Sumas"
---

# **Transformación de Productos a Sumas**

A veces en matemáticas queremos sumar cosas (como ondas de sonido) y otras veces queremos multiplicarlas (como en procesadores de señales). Estas fórmulas son el puente entre ambos mundos. Son vitales en música, ingeniería y para resolver integrales "imposibles".

---

## 🎯 ¿Qué vas a aprender?

- Cómo convertir una multiplicación de senos/cosenos en una suma o resta simple.
- Cómo convertir una suma de senos/cosenos en una multiplicación compacta.
- Por qué esto es útil para simplificar fracciones trigonométricas.
- Aplicaciones en física (como el fenómeno de batimiento en el sonido).

---

## 🏗️ De Producto a Suma

Estas identidades son la salvación en Cálculo Integral. Transforman productos difíciles en sumas fáciles.

### Fórmulas
$$
\sin A \cos B = \frac{1}{2}[\sin(A + B) + \sin(A - B)]
$$

$$
\cos A \sin B = \frac{1}{2}[\sin(A + B) - \sin(A - B)]
$$

$$
\cos A \cos B = \frac{1}{2}[\cos(A + B) + \cos(A - B)]
$$

$$
\sin A \sin B = \frac{1}{2}[\cos(A - B) - \cos(A + B)]
$$

> **¡Ojo!** En la última fórmula (Seno por Seno), el orden de la resta al final está invertido: es Resta menos Suma.

---

## 🏗️ De Suma a Producto

Estas son útiles para simplificar fracciones o resolver ecuaciones donde hay sumas igualadas a cero.

### Fórmulas
$$
\sin A + \sin B = 2\sin\left(\frac{A + B}{2}\right)\cos\left(\frac{A - B}{2}\right)
$$

$$
\sin A - \sin B = 2\cos\left(\frac{A + B}{2}\right)\sin\left(\frac{A - B}{2}\right)
$$

$$
\cos A + \cos B = 2\cos\left(\frac{A + B}{2}\right)\cos\left(\frac{A - B}{2}\right)
$$

$$
\cos A - \cos B = -2\sin\left(\frac{A + B}{2}\right)\sin\left(\frac{A - B}{2}\right)
$$

> **¡Ojo!** La resta de cosenos da como resultado un signo negativo al principio.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Producto a Suma
Transforma $2\cos(3x)\cos(4x)$ en una suma.

Usamos la identidad de Coseno-Coseno:
$$
\cos A \cos B = \frac{1}{2}[\cos(A+B) + \cos(A-B)]
$$

$$
2\cos(3x)\cos(4x) = 2 \cdot \frac{1}{2}[\cos(7x) + \cos(-x)]
$$

Como el coseno es par, $\cos(-x) = \cos(x)$.

**Resultado:** $\boxed{\cos(7x) + \cos(x)}$

### Ejemplo 2: Suma a Producto
Transforma $\sin(40°) + \sin(20°)$.

Usamos la identidad Seno + Seno:
$$
\sin A + \sin B = 2\sin\left(\frac{A+B}{2}\right)\cos\left(\frac{A-B}{2}\right)
$$

$$
= 2\sin\left(\frac{60°}{2}\right)\cos\left(\frac{20°}{2}\right)
$$
$$
= 2\sin(30°)\cos(10°)
$$
$$
= 2(0.5)\cos(10°) = \cos(10°)
$$
**Resultado:** $\boxed{\cos(10°)}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Transforma a suma: $\sin(3x)\cos(x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{1}{2}[\sin(4x) + \sin(2x)]$.

**Respuesta:** $\boxed{\frac{1}{2}\sin(4x) + \frac{1}{2}\sin(2x)}$
</details>

---

### Ejercicio 2
Transforma a producto: $\cos(5x) + \cos(3x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2\cos(\frac{8x}{2})\cos(\frac{2x}{2})$.

**Respuesta:** $\boxed{2\cos(4x)\cos(x)}$
</details>

---

### Ejercicio 3
Simplifica $\frac{\sin 3x + \sin x}{\cos 3x + \cos x}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{2\sin(2x)\cos(x)}{2\cos(2x)\cos(x)}$.
Se cancela $2\cos(x)$. Queda $\tan(2x)$.

**Respuesta:** $\boxed{\tan(2x)}$
</details>

---

### Ejercicio 4
Calcula el valor exacto de $\cos(75°)\sin(15°)$ usando producto a suma.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{1}{2}[\sin(90°) - \sin(60°)]$.
$\frac{1}{2}[1 - \sqrt{3}/2] = 1/2 - \sqrt{3}/4$.

**Respuesta:** $\boxed{\frac{2-\sqrt{3}}{4}}$
</details>

---

### Ejercicio 5
Transforma a suma: $\sin(2\theta)\sin(4\theta)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{1}{2}[\cos(-2\theta) - \cos(6\theta)]$.
$\cos(-2\theta) = \cos(2\theta)$.

**Respuesta:** $\boxed{\frac{1}{2}\cos(2\theta) - \frac{1}{2}\cos(6\theta)}$
</details>

---

### Ejercicio 6
Calcula $\cos(15°) - \cos(75°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$-2\sin(45°)\sin(-30°)$.
$-2(\frac{\sqrt{2}}{2})(-\frac{1}{2}) = \frac{\sqrt{2}}{2}$.

**Respuesta:** $\boxed{\frac{\sqrt{2}}{2}}$
</details>

---

### Ejercicio 7
Demuestra que $\sin(A+B) + \sin(A-B) = 2\sin A \cos B$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Usa la fórmula de producto a suma para $2\sin A \cos B$.
$2 \cdot \frac{1}{2}[\sin(A+B) + \sin(A-B)]$.
Da exactamente la expresión original.

**Respuesta:** **Q.E.D.**
</details>

---

### Ejercicio 8
Expresa $\cos x \cos 2x \cos 4x$ como suma (Este es un reto).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Primero $\cos x \cos 2x = \frac{1}{2}(\cos 3x + \cos x)$.
Multiplicamos por $\cos 4x$.
$\frac{1}{2}(\cos 3x \cos 4x + \cos x \cos 4x)$.
Expandimos cada par.

**Respuesta:** $\boxed{\frac{1}{4}(\cos 7x + \cos x + \cos 5x + \cos 3x)}$
</details>

---

### Ejercicio 9
Simplifica $\frac{\sin A - \sin B}{\cos A + \cos B}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{2\cos(\frac{A+B}{2})\sin(\frac{A-B}{2})}{2\cos(\frac{A+B}{2})\cos(\frac{A-B}{2})}$.
Se cancelan términos. Queda tangente.

**Respuesta:** $\boxed{\tan\left(\frac{A-B}{2}\right)}$
</details>

---

### Ejercicio 10
Si $\sin x + \sin y = 1$ y $\cos x + \cos y = 0$, halla $x+y$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Dividimos (Suma senos / Suma cosenos) = $\tan(\frac{x+y}{2}) = 1/0$ (Indefinido).
$\frac{x+y}{2} = 90° \rightarrow x+y = 180°$.

**Respuesta:** $\boxed{180°}$
</details>

---

## 🔑 Resumen

| Identidad | Se usa para... | Clave |
| :--- | :--- | :--- |
| **Producto $\to$ Suma** | Integrales ($\int \sin x \cos x \, dx$) | Factor $1/2$ al frente. |
| **Suma $\to$ Producto** | Simplificar fracciones. | Factor $2$ al frente. Argumentos promedio. |

> **Conclusión:** Estas fórmulas son el "traductor universal" entre multiplicación y suma. Son un poco largas de memorizar, así que ten esta hoja a mano.
