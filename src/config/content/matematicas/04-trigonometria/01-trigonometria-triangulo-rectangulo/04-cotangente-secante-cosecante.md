---
title: "Cotangente, Secante y Cosecante"
---

# **Cotangente, Secante y Cosecante**

Así como cada superhéroe tiene un alter ego, las razones trigonométricas tienen sus **razones recíprocas**. Son simplemente las mismas fracciones, pero "patas arriba" (invertidas).

---

## 🎯 ¿Qué vas a aprender?

- Calcular las 3 razones recíprocas: **Cotangente**, **Secante** y **Cosecante**.
- Entender que "inverso" o "recíproco" significa dar la vuelta a la fracción ($\frac{a}{b} \rightarrow \frac{b}{a}$).
- Nuevas identidades pitagóricas como $1 + \tan^2 = \sec^2$.

---

## 🔄 El Mundo al Revés

Si el Seno es $Opuesto / Hipotenusa$, ¿qué pasa si dividimos $Hipotenusa / Opuesto$? Obtenemos una nueva razón.

### 1. Cosecante ($\csc$)
Es la inversa del **Seno**.

$$
\csc(\theta) = \frac{1}{\sin(\theta)} = \frac{\text{Hipotenusa}}{\text{Opuesto}}
$$

> **Truco:** La **C**osecante va con el **S**eno (**C** con **S**).

### 2. Secante ($\sec$)
Es la inversa del **Coseno**.

$$
\sec(\theta) = \frac{1}{\cos(\theta)} = \frac{\text{Hipotenusa}}{\text{Adyacente}}
$$

> **Truco:** La **S**ecante va con el **C**oseno (**S** con **C**).

### 3. Cotangente ($\cot$)
Es la inversa de la **Tangente**.

$$
\cot(\theta) = \frac{1}{\tan(\theta)} = \frac{\text{Adyacente}}{\text{Opuesto}}
$$

![Triángulo 3-4-5 con las 6 razones](/images/geometria/trigonometria/03-triangulo-345.svg)

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Calcular Recíprocas

Si $\sin(\theta) = \frac{3}{5}$, calcula $\csc(\theta)$.

**Razonamiento:**
Simplemente invertimos la fracción del seno.
$\frac{3}{5} \rightarrow \frac{5}{3}$.

**Resultado:**
$$
\boxed{\frac{5}{3} \approx 1.66}
$$

### Ejemplo 2: De Decimal a Recíproca

Si $\cos(\theta) = 0.5$, calcula $\sec(\theta)$.

**Razonamiento:**
$0.5 = \frac{1}{2}$.
La inversa de $\frac{1}{2}$ es $\frac{2}{1} = 2$.

**Resultado:**
$$
\boxed{2}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si $\tan(\theta) = 4$, ¿cuánto vale $\cot(\theta)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$4 = 4/1$. La inversa es $1/4$.

**Resultado:**
$$
\boxed{0.25}
$$

</details>

### Ejercicio 2
Si el Seno es muy pequeño (p.ej. 0.001), ¿cómo es la Cosecante?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$1 / 0.001 = 1000$. Es muy grande.

**Resultado:**
$$
\boxed{\text{Muy grande}}
$$

</details>

### Ejercicio 3
Calcula $\sec(60^{\circ})$ sabiendo que $\cos(60^{\circ}) = 0.5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{1}{0.5} = 2$.

**Resultado:**
$$
\boxed{2}
$$

</details>

### Ejercicio 4
En un triángulo con lados 5, 12, 13 ($Op=5$), calcula la Cosecante.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\text{Seno} = 5/13$. $\text{Cosecante} = 13/5$.

**Resultado:**
$$
\boxed{2.6}
$$

</details>

### Ejercicio 5
Verdadero o Falso: La Secante siempre es mayor o igual a 1.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Verdadero. Como la Hipotenusa es mayor que el cateto, la fracción $Hip/Ady$ siempre es $>1$.

**Resultado:**
$$
\boxed{\text{Verdadero}}
$$

</details>

### Ejercicio 6
Calcula $\cot(45^{\circ})$. (Pista: $\tan(45^{\circ}) = 1$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$1/1 = 1$.

**Resultado:**
$$
\boxed{1}
$$

</details>

### Ejercicio 7
Si $\sin(\theta) = \frac{\sqrt{3}}{2}$, calcula $\csc(\theta)$ y racionaliza.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{2}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}} = \frac{2\sqrt{3}}{3}$.

**Resultado:**
$$
\boxed{\frac{2\sqrt{3}}{3}}
$$

</details>

### Ejercicio 8
Usa la identidad $1 + \tan^2 = \sec^2$. Si $\tan=3$, halla $\sec$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$1 + 3^2 = 1+9=10$.
$\sec^2 = 10 \Rightarrow \sec = \sqrt{10}$.

**Resultado:**
$$
\boxed{\sqrt{10}}
$$

</details>

### Ejercicio 9
¿Qué razón recíproca no está definida para $0^{\circ}$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\csc(0) = 1/\sin(0) = 1/0$. No existe.
$\cot(0) = 1/\tan(0) = 1/0$. No existe.

**Resultado:**
$$
\boxed{\text{Cosecante y Cotangente}}
$$

</details>

### Ejercicio 10
Si $\sec(\theta) = 1$, ¿cuánto vale el coseno?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$1/1 = 1$.

**Resultado:**
$$
\boxed{1}
$$

</details>

---

## 🔑 Resumen

| Razón | Inversa de... | Fórmula |
| :--- | :--- | :--- |
| **Cosecante ($\csc$)** | Seno | $H/O$ |
| **Secante ($\sec$)** | Coseno | $H/A$ |
| **Cotangente ($\cot$)** | Tangente | $A/O$ |

> Recuerda: Solo dales la vuelta "patas arriba".
