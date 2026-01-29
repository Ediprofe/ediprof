# **Racionalización**

En matemáticas, existe una "regla de etiqueta" importante: nunca dejamos raíces en la parte de abajo de una fracción (el denominador). Racionalizar es el proceso de mover esa raíz al numerador sin cambiar el valor del número. Es fundamental para poder sumar fracciones con raíces y para simplificar resultados finales.

---

## 🎯 ¿Qué vas a aprender?

- Por qué es necesario eliminar las raíces del denominador.
- Cómo racionalizar fracciones simples con raíces cuadradas.
- Cómo racionalizar raíces de cualquier índice ($\sqrt[3]{}, \sqrt[4]{}$, etc.).
- El uso del **conjugado** para racionalizar sumas y restas.

---

## 🧹 Caso 1: Un solo término en el denominador

Si tienes una raíz sola abajo, el objetivo es completar el cuadrado (o el cubo) para que la raíz se cancele.

### **Raíces Cuadradas**
Simplemente multiplicamos arriba y abajo por la **misma raíz**.

$$
\frac{a}{\sqrt{b}} \cdot \frac{\sqrt{b}}{\sqrt{b}} = \frac{a\sqrt{b}}{b}
$$

### **Ejemplo 1: Racionalización básica**

Racionaliza:

$$
\frac{5}{\sqrt{2}}
$$

**Razonamiento:**
Multiplicamos numerador y denominador por $\sqrt{2}$.

$$
\frac{5}{\sqrt{2}} \cdot \frac{\sqrt{2}}{\sqrt{2}}
$$

**Paso a paso:**

$$
\frac{5\sqrt{2}}{\sqrt{4}}
$$

$$
\frac{5\sqrt{2}}{2}
$$

**Resultado:**

$$
\boxed{\frac{5\sqrt{2}}{2}}
$$

---

### **Raíces de Índice Mayor**
Si es una raíz cúbica ($\sqrt[3]{}$), necesitamos que el exponente de adentro sea 3 para que se cancele. Si tenemos $\sqrt[3]{x^1}$, nos faltan 2. Multiplicamos por $\sqrt[3]{x^2}$.

### **Ejemplo 2: Raíz Cúbica**

Racionaliza:

$$
\frac{6}{\sqrt[3]{2}}
$$

**Razonamiento:**
El 2 tiene exponente 1 ($2^1$). Para llegar a 3, nos faltan 2.
Multiplicamos por $\sqrt[3]{2^2} = \sqrt[3]{4}$.

$$
\frac{6}{\sqrt[3]{2}} \cdot \frac{\sqrt[3]{4}}{\sqrt[3]{4}}
$$

**Paso a paso:**

$$
\frac{6\sqrt[3]{4}}{\sqrt[3]{2 \cdot 4}}
$$

$$
\frac{6\sqrt[3]{4}}{\sqrt[3]{8}}
$$

$$
\frac{6\sqrt[3]{4}}{2}
$$

Simplificamos $6/2 = 3$.

**Resultado:**

$$
\boxed{3\sqrt[3]{4}}
$$

---

## 🤝 Caso 2: Sumas o Restas (El Conjugado)

Si el denominador es un binomio como $\sqrt{a} + b$ o $\sqrt{a} - \sqrt{b}$, usar una sola raíz no funciona. Usamos el **conjugado**.

> **El Conjugado:** Es la misma expresión pero con el signo del medio cambiado.
> - De $(A + B)$ el conjugado es $(A - B)$.
> - De $(A - B)$ el conjugado es $(A + B)$.

Al multiplicar conjugados, siempre obtenemos una **Diferencia de Cuadrados**, lo que elimina las raíces:

$$
(\sqrt{a} + \sqrt{b})(\sqrt{a} - \sqrt{b}) = (\sqrt{a})^2 - (\sqrt{b})^2 = a - b
$$

---

### **Ejemplo 3: Racionalizar con Conjugado**

Racionaliza:

$$
\frac{4}{3 - \sqrt{5}}
$$

**Razonamiento:**
El denominador es $3 - \sqrt{5}$. Su conjugado es $3 + \sqrt{5}$.

**Paso 1: Multiplicar**

$$
\frac{4}{3 - \sqrt{5}} \cdot \frac{3 + \sqrt{5}}{3 + \sqrt{5}}
$$

**Paso 2: Operar abajo (Diferencia de Cuadrados)**

$$
(3)^2 - (\sqrt{5})^2 = 9 - 5 = 4
$$

**Paso 3: Operar arriba y simplificar**

$$
\frac{4(3 + \sqrt{5})}{4}
$$

Cancelamos los 4.

**Resultado:**

$$
\boxed{3 + \sqrt{5}}
$$

---

### **Ejemplo 4: Dos Raíces en el Denominador**

Racionaliza:

$$
\frac{10}{\sqrt{7} + \sqrt{2}}
$$

**Razonamiento:**
Conjugado de $\sqrt{7} + \sqrt{2}$ es $\sqrt{7} - \sqrt{2}$.

**Paso 1: Denominador**
$(\sqrt{7})^2 - (\sqrt{2})^2 = 7 - 2 = 5$.

**Paso 2: Fracción Completa**

$$
\frac{10(\sqrt{7} - \sqrt{2})}{5}
$$

**Paso 3: Simplificar**
$10 / 5 = 2$.

**Resultado:**

$$
\boxed{2(\sqrt{7} - \sqrt{2})}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Racionaliza: $\dfrac{1}{\sqrt{3}}$

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Multiplicamos por $\sqrt{3}/\sqrt{3}$.

$$
\frac{1\sqrt{3}}{\sqrt{9}} = \frac{\sqrt{3}}{3}
$$

**Resultado:**

$$
\boxed{\frac{\sqrt{3}}{3}}
$$

</details>

---

### Ejercicio 2
Racionaliza: $\dfrac{8}{\sqrt{2}}$

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
\frac{8\sqrt{2}}{2} = 4\sqrt{2}
$$

**Resultado:**

$$
\boxed{4\sqrt{2}}
$$

</details>

---

### Ejercicio 3
Racionaliza: $\dfrac{2}{\sqrt{5}}$

<details>
<summary>Ver solución</summary>

$$
\frac{2\sqrt{5}}{5}
$$

**Resultado:**

$$
\boxed{\frac{2\sqrt{5}}{5}}
$$

</details>

---

### Ejercicio 4
Racionaliza: $\dfrac{5}{\sqrt[3]{5}}$

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Falta exponente 2 para completar $5^3$. Multiplicamos por $\sqrt[3]{5^2} = \sqrt[3]{25}$.

$$
\frac{5\sqrt[3]{25}}{5} = \sqrt[3]{25}
$$

**Resultado:**

$$
\boxed{\sqrt[3]{25}}
$$

</details>

---

### Ejercicio 5
Racionaliza: $\dfrac{9}{\sqrt{3}}$

<details>
<summary>Ver solución</summary>

$$
\frac{9\sqrt{3}}{3} = 3\sqrt{3}
$$

**Resultado:**

$$
\boxed{3\sqrt{3}}
$$

</details>

---

### Ejercicio 6
Racionaliza: $\dfrac{6}{\sqrt{5} - 1}$

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Conjugado: $\sqrt{5} + 1$.
Denominador: $5 - 1 = 4$.

$$
\frac{6(\sqrt{5} + 1)}{4} = \frac{3(\sqrt{5} + 1)}{2}
$$

**Resultado:**

$$
\boxed{\frac{3(\sqrt{5} + 1)}{2}}
$$

</details>

---

### Ejercicio 7
Racionaliza: $\dfrac{2}{\sqrt{3} + 1}$

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Conjugado: $\sqrt{3} - 1$.
Denominador: $3 - 1 = 2$.

$$
\frac{2(\sqrt{3} - 1)}{2}
$$

**Resultado:**

$$
\boxed{\sqrt{3} - 1}
$$

</details>

---

### Ejercicio 8
Racionaliza: $\dfrac{10}{\sqrt{6} - \sqrt{2}}$

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Conjugado: $\sqrt{6} + \sqrt{2}$.
Denominador: $6 - 2 = 4$.

$$
\frac{10(\sqrt{6} + \sqrt{2})}{4} = \frac{5(\sqrt{6} + \sqrt{2})}{2}
$$

**Resultado:**

$$
\boxed{\frac{5(\sqrt{6} + \sqrt{2})}{2}}
$$

</details>

---

### Ejercicio 9
Racionaliza: $\dfrac{\sqrt{2}}{\sqrt{2} + \sqrt{3}}$

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Conjugado: $\sqrt{2} - \sqrt{3}$.
Denominador: $2 - 3 = -1$.

$$
\frac{\sqrt{2}(\sqrt{2} - \sqrt{3})}{-1} = \frac{2 - \sqrt{6}}{-1} = \sqrt{6} - 2
$$

**Resultado:**

$$
\boxed{\sqrt{6} - 2}
$$

</details>

---

### Ejercicio 10
Racionaliza: $\dfrac{1}{\sqrt[4]{x}}$

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Tenemos $x^1$, necesitamos $x^4$. Faltan 3. Multiplicamos por $\sqrt[4]{x^3}$.

$$
\frac{1 \cdot \sqrt[4]{x^3}}{\sqrt[4]{x^4}}
$$

**Resultado:**

$$
\boxed{\frac{\sqrt[4]{x^3}}{x}}
$$

</details>

---

## 🔑 Resumen

| Forma del Denominador | Multiplicar por | Resultado en Denominador |
|:--- |:--- |:--- |
| $\sqrt{A}$ | $\sqrt{A}$ | $A$ |
| $\sqrt[3]{A}$ | $\sqrt[3]{A^2}$ | $A$ |
| $\sqrt{A} + \sqrt{B}$ | $\sqrt{A} - \sqrt{B}$ (Conjugado) | $A - B$ |
| $\sqrt{A} - \sqrt{B}$ | $\sqrt{A} + \sqrt{B}$ (Conjugado) | $A - B$ |

> **Conclusión:** La racionalización es como "limpiar" la fracción. No cambiamos su valor, solo su presentación para que sea más fácil de manejar en cálculos futuros.
