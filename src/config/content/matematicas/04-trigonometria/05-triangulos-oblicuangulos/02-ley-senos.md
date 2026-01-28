---
title: "Ley de Senos"
---

# **Ley de Senos**

Imagina que solo conoces un lado de un triángulo y un par de ángulos. ¿Cómo encuentras el resto? La **Ley de Senos** es la herramienta perfecta para resolver triángulos cuando tienes "parejas" completas de datos (un ángulo y su lado opuesto).

---

## 🎯 ¿Qué vas a aprender?

- La fórmula simple de la Ley de Senos.
- Cómo usarla para encontrar un lado perdido.
- Cómo usarla para encontrar un ángulo desconocido.
- Qué es el "Caso Ambiguo" y por qué a veces hay dos soluciones.

---

## 📏 La Fórmula Mágica

En cualquier triángulo (sea oblicuángulo o no), la proporción entre un lado y el seno de su ángulo opuesto es **siempre la misma**.

$$
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}
$$

También puedes escribirla al revés (útil cuando buscas ángulos):

$$
\frac{\sin A}{a} = \frac{\sin B}{b} = \frac{\sin C}{c}
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Ley de Senos: a/sin A = b/sin B = c/sin C</strong>
  </div>

![Ley de Senos](/images/trigonometria/triangulos-oblicuangulos/ley-senos.svg)

</div>

Esta constante misteriosa es igual al diámetro ($2R$) del círculo que rodea al triángulo. ¡Todo está conectado!

---

## 🔍 ¿Cuándo usarla?

Usa la Ley de Senos cuando conozcas **una pareja completa** (lado y ángulo opuesto) y **un dato más**.

1.  **Caso ALA o AAL:** Conoces dos ángulos y un lado. (¡Es el más fácil!).
2.  **Caso LLA:** Conoces dos lados y un ángulo opuesto. (¡Cuidado! Este es el caso ambiguo).

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Encontrar un lado (Caso ALA)
En un triángulo, $A = 40°$, $B = 60°$ y el lado $a = 10$. Halla el lado $b$.

**Paso 1: Identificar la pareja completa**
Tenemos la pareja $A$ y $a$ ($40°$ y $10$).
Buscamos $b$ y tenemos su ángulo opuesto $B$ ($60°$).

**Paso 2: Escribir la proporción**
$$
\frac{a}{\sin A} = \frac{b}{\sin B}
$$

**Paso 3: Sustituir y despejar**
$$
\frac{10}{\sin 40°} = \frac{b}{\sin 60°}
$$

$$
b = \frac{10 \cdot \sin 60°}{\sin 40°}
$$

$$
b \approx \frac{10 \cdot 0.866}{0.643} \approx 13.47
$$

**Resultado:** $\boxed{13.47}$

---

### Ejemplo 2: Encontrar un ángulo (Caso LLA)
En un triángulo, $a = 20$, $c = 15$ y $A = 40°$. Halla el ángulo $C$.

**Paso 1: Usar la forma inversa**
$$
\frac{\sin C}{c} = \frac{\sin A}{a}
$$

**Paso 2: Sustituir**
$$
\frac{\sin C}{15} = \frac{\sin 40°}{20}
$$

$$
\sin C = \frac{15 \cdot \sin 40°}{20} \approx \frac{15 \cdot 0.643}{20} \approx 0.482
$$

**Paso 3: Arcoseno**
$$
C = \sin^{-1}(0.482) \approx 28.8°
$$

**Resultado:** $\boxed{28.8°}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra $b$ si $a = 10$, $A = 30°$, $B = 45°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{b}{\sin 45°} = \frac{10}{\sin 30°}$.
$b = \frac{10 \cdot 0.707}{0.5} = 14.14$.

**Respuesta:** $\boxed{14.14}$
</details>

---

### Ejercicio 2
Encuentra $\sin B$ si $a = 8$, $b = 10$, $A = 30°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{\sin B}{10} = \frac{\sin 30°}{8}$.
$\sin B = \frac{10 \cdot 0.5}{8} = \frac{5}{8} = 0.625$.

**Respuesta:** $\boxed{0.625}$
</details>

---

### Ejercicio 3
Resuelve para $c$: $C = 60°$, $A = 45°$, $a = 5\sqrt{2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{c}{\sin 60°} = \frac{5\sqrt{2}}{\sin 45°}$.
$c = \frac{5\sqrt{2} \cdot (\sqrt{3}/2)}{\sqrt{2}/2} = 5\sqrt{3}$.

**Respuesta:** $\boxed{5\sqrt{3}}$
</details>

---

### Ejercicio 4
Si $\frac{a}{\sin A} = 10$, ¿cuánto vale el lado $b$ si $B = 30°$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La razón es constante. $\frac{b}{\sin 30°} = 10$.
$b = 10 \cdot 0.5$.

**Respuesta:** $\boxed{5}$
</details>

---

### Ejercicio 5
¿Por qué la Ley de Senos es peligrosa para encontrar el ángulo mayor?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Porque el seno es positivo en Q1 y Q2. $\sin(80°)$ y $\sin(100°)$ valen lo mismo. La calculadora solo te dará $80°$, escondiendo la posible solución obtusa.

**Respuesta:** **Ambigüedad del seno**
</details>

---

### Ejercicio 6
Encuentra $a$ dado $A=60°$, $B=90°$ (rectángulo), $b=10$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Apliquemos la ley aunque sea rectángulo.
$a = \frac{10 \cdot \sin 60°}{\sin 90°} = 10 \cdot \frac{\sqrt{3}}{2} = 5\sqrt{3}$.
Coincide con la definición de seno ($a = b \sin A$).

**Respuesta:** $\boxed{5\sqrt{3}}$
</details>

---

### Ejercicio 7
Si $\sin A = 2 \sin B$, ¿qué relación existe entre los lados $a$ y $b$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{a}{\sin A} = \frac{b}{\sin B} \rightarrow a = b \frac{\sin A}{\sin B}$.
$a = b \frac{2\sin B}{\sin B} = 2b$.

**Respuesta:** $\boxed{a = 2b}$
</details>

---

### Ejercicio 8
Encuentra $C$ si $A=100°$ y $B=30°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$180 - (100+30) = 50°$.

**Respuesta:** $\boxed{50°}$
</details>

---

### Ejercicio 9
Calcula el diámetro del círculo circunscrito si $a=10$ y $A=30°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2R = \frac{a}{\sin A} = \frac{10}{0.5} = 20$.

**Respuesta:** $\boxed{20}$
</details>

---

### Ejercicio 10
Si $\frac{a}{\sin 30°} = \frac{12}{\sin 90°}$, halla $a$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a = \frac{12 \cdot 0.5}{1} = 6$.

**Respuesta:** $\boxed{6}$
</details>

---

## 🔑 Resumen

| Concepto | Fórmula | Cuándo usar |
| :---: | :---: | :--- |
| **Ley de Senos** | $\frac{a}{\sin A} = \frac{b}{\sin B}$ | Pareja completa + 1 dato. |
| **Caso Inverso** | $\frac{\sin A}{a} = \frac{\sin B}{b}$ | Para hallar ángulos. |

> **Conclusión:** La Ley de Senos es la reina de las proporciones. Úsala siempre que tengas una "pareja" conocida. Si no tienes parejas... tendrás que esperar a la Ley de Cosenos.
