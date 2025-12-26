# **Propiedades de los Radicales (II)**

¿Alguna vez has visto la película *Inception* (El Origen)? Es un sueño dentro de un sueño. En matemáticas, también tenemos "raíces dentro de raíces".

En esta lección completaremos tu caja de herramientas con las propiedades avanzadas para manejar estas situaciones y simplificar expresiones que parecen imposibles.

---

## 🎯 ¿Qué vas a aprender?

- Qué hacer cuando tienes una raíz elevada a una potencia.
- Cómo resolver una "raíz dentro de otra raíz" (Raíz de una raíz).
- El truco para simplificar índices y exponentes como si fueran fracciones.

---

## ⚡ Propiedad 3: Potencia de un Radical

**"El exponente entra a la casa".**

Si elevas toda una raíz a una potencia, ese exponente puede entrar y elevar directamente al número de adentro.

$$
(\sqrt[n]{a})^m = \sqrt[n]{a^m}
$$

### ¿Por qué funciona?
Recuerda que la raíz es un exponente fraccionario.
$$
(a^{\frac{1}{n}})^m = a^{\frac{m}{n}} = \sqrt[n]{a^m}
$$

---

## ⚡ Propiedad 4: Raíz de una Raíz

**"Los índices se multiplican".**

Si tienes una raíz dentro de otra, puedes fusionarlas en una sola multiplicando sus índices.

$$
\sqrt[m]{\sqrt[n]{a}} = \sqrt[m \cdot n]{a}
$$

> 💡 **Analogía:** Es como mirar a través de dos lentes. El aumento total es la multiplicación de los aumentos individuales.

---

## ⚡ Propiedad 5: Simplificación de Índice y Exponente

**"Como simplificar una fracción".**

Si el índice de la raíz y el exponente de adentro tienen un divisor común, ¡puedes dividirlos!

$$
\sqrt[n \cdot k]{a^{m \cdot k}} = \sqrt[n]{a^m}
$$

**Ejemplo:**
$\sqrt[6]{x^4}$ es lo mismo que $x^{\frac{4}{6}}$.
Simplificando la fracción: $\frac{4}{6} = \frac{2}{3}$.
Entonces queda $\sqrt[3]{x^2}$.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Potencia entrando

Simplifica $(\sqrt[3]{2})^6$.

**Razonamiento:**
Metemos el 6 dentro de la raíz.

$$
\sqrt[3]{2^6}
$$

Dividimos exponente entre índice: $6 \div 3 = 2$.

$$
2^2 = 4
$$

**Resultado:**

$$
\boxed{4}
$$

### Ejemplo 2: Raíz de raíz

Simplifica $\sqrt{\sqrt[3]{64}}$.

**Razonamiento:**
Multiplicamos los índices. Recuerda que la raíz sola tiene un 2 invisible.
$2 \times 3 = 6$.

$$
\sqrt[6]{64}
$$

Buscamos un número que multiplicado 6 veces dé 64. Es el 2.

**Resultado:**

$$
\boxed{2}
$$

### Ejemplo 3: Simplificación extrema

Simplifica $\sqrt[12]{x^8}$.

**Razonamiento:**
Índice 12 y exponente 8. Ambos son divisibles por 4.
$12 \div 4 = 3$
$8 \div 4 = 2$

$$
\sqrt[3]{x^2}
$$

**Resultado:**

$$
\boxed{\sqrt[3]{x^2}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Simplifica $(\sqrt{5})^4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{5^4} = 5^{\frac{4}{2}} = 5^2$.

**Resultado:**
$$
\boxed{25}
$$

</details>

### Ejercicio 2
Simplifica $\sqrt[3]{\sqrt{x}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Índices $3 \times 2 = 6$.

**Resultado:**
$$
\boxed{\sqrt[6]{x}}
$$

</details>

### Ejercicio 3
Simplifica $\sqrt[10]{a^5}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Dividimos entre 5. Índice $10 \to 2$, Exponente $5 \to 1$.

**Resultado:**
$$
\boxed{\sqrt{a}}
$$

</details>

### Ejercicio 4
Calcula $\sqrt{\sqrt{16}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt[4]{16} = 2$.

**Resultado:**
$$
\boxed{2}
$$

</details>

### Ejercicio 5
Simplifica $(\sqrt[4]{3})^8$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt[4]{3^8} = 3^{\frac{8}{4}} = 3^2$.

**Resultado:**
$$
\boxed{9}
$$

</details>

### Ejercicio 6
Simplifica $\sqrt[6]{8}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$8 = 2^3$. Entonces $\sqrt[6]{2^3}$. Simplificamos por 3.

**Resultado:**
$$
\boxed{\sqrt{2}}
$$

</details>

### Ejercicio 7
Simplifica $\sqrt[4]{x^2 y^2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Todos divisibles por 2.

**Resultado:**
$$
\boxed{\sqrt{xy}}
$$

</details>

### Ejercicio 8
Calcula $\sqrt[3]{\sqrt[2]{64}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt[6]{64} = 2$.

**Resultado:**
$$
\boxed{2}
$$

</details>

### Ejercicio 9
Simplifica $(\sqrt[5]{x})^{10}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^{\frac{10}{5}} = x^2$.

**Resultado:**
$$
\boxed{x^2}
$$

</details>

### Ejercicio 10
Simplifica $\sqrt[9]{27}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$27 = 3^3$. $\sqrt[9]{3^3}$. Simplificamos por 3.

**Resultado:**
$$
\boxed{\sqrt[3]{3}}
$$

</details>

---

## 🔑 Resumen

| Propiedad | Fórmula |
|----------|---------|
| **Potencia** | $(\sqrt[n]{a})^m = \sqrt[n]{a^m}$ |
| **Raíz de Raíz** | $\sqrt[m]{\sqrt[n]{a}} = \sqrt[m \cdot n]{a}$ |
| **Simplificación** | Dividir índice y exponente por el mismo número. |

> Estas propiedades son esenciales para "limpiar" expresiones algebraicas antes de resolverlas.
