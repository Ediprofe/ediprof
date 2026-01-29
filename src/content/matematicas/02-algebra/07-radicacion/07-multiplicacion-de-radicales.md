# **Multiplicación de Radicales**

Imagina que tienes dos cajas de regalo. Si las dos cajas son del mismo tamaño, puedes meter el contenido de una dentro de la otra y hacer un solo regalo gigante. Pero si una caja es cuadrada y la otra triangular, primero tienes que hacer un truco para que encajen.

En matemáticas, multiplicar radicales es fusionarlos. Si tienen el mismo índice, es directo. Si no, hay que igualarlos primero.

---

## 🎯 ¿Qué vas a aprender?

- Cómo multiplicar raíces con el mismo índice (fácil).
- Cómo multiplicar raíces con diferente índice (nivel pro).
- La regla de "afuera con afuera, adentro con adentro".

---

## 🤝 Caso 1: Mismo Índice

Si los radicales tienen el mismo índice, la regla es simple: **multiplica lo de adentro con lo de adentro**.

**Fórmula:**
$$
\sqrt[n]{a} \cdot \sqrt[n]{b} = \sqrt[n]{a \cdot b}
$$

**Ejemplo:**
$$
\sqrt{2} \cdot \sqrt{3} = \sqrt{2 \cdot 3} = \sqrt{6}
$$

---

## 🔄 Caso 2: Diferente Índice

Si los índices son distintos (ej. $\sqrt{2} \cdot \sqrt[3]{2}$), no se pueden fusionar directamente.
**Truco:** Convertir ambos al **Mínimo Común Múltiplo (MCM)** de los índices.

**Ejemplo:** $\sqrt{2} \cdot \sqrt[3]{2}$.
1. Índices: 2 y 3. MCM = 6.
2. Convertir $\sqrt{2}$ a índice 6: Multiplicamos índice por 3, elevamos radicando a la 3. $\to \sqrt[6]{2^3}$.
3. Convertir $\sqrt[3]{2}$ a índice 6: Multiplicamos índice por 2, elevamos radicando a la 2. $\to \sqrt[6]{2^2}$.
4. Ahora multiplicamos: $\sqrt[6]{2^3 \cdot 2^2} = \sqrt[6]{2^5}$.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Mismo índice con coeficientes

Multiplica: $3\sqrt{2} \cdot 4\sqrt{5}$.

**Regla:** "Afuera con afuera, adentro con adentro".
- Afuera: $3 \cdot 4 = 12$.
- Adentro: $2 \cdot 5 = 10$.

**Resultado:**

$$
\boxed{12\sqrt{10}}
$$

### Ejemplo 2: Diferente índice

Multiplica: $\sqrt{x} \cdot \sqrt[3]{x}$.

**Paso 1: MCM de índices**
Índices 2 y 3. MCM = 6.

**Paso 2: Homogeneizar**
- $\sqrt{x} = \sqrt[6]{x^3}$.
- $\sqrt[3]{x} = \sqrt[6]{x^2}$.

**Paso 3: Multiplicar**
$$
\sqrt[6]{x^3 \cdot x^2} = \sqrt[6]{x^5}
$$

**Resultado:**

$$
\boxed{\sqrt[6]{x^5}}
$$

### Ejemplo 3: Binomio por radical

Multiplica: $\sqrt{2}(3 + \sqrt{2})$.

**Propiedad Distributiva:**
1. $\sqrt{2} \cdot 3 = 3\sqrt{2}$.
2. $\sqrt{2} \cdot \sqrt{2} = \sqrt{4} = 2$.

**Resultado:**

$$
\boxed{3\sqrt{2} + 2}
$$

### Ejemplo 4: Tres radicales con mismo índice

Multiplica: $\sqrt{2} \cdot \sqrt{8} \cdot \sqrt{3}$.

**Razonamiento:**
Podemos multiplicar de a dos o todos juntos.
$\sqrt{2 \cdot 8 \cdot 3} = \sqrt{48}$.

Simplificamos: $48 = 16 \cdot 3 = 4^2 \cdot 3$.
$\sqrt{48} = \sqrt{16 \cdot 3} = 4\sqrt{3}$.

**Resultado:**

$$
\boxed{4\sqrt{3}}
$$

### Ejemplo 5: Diferente índice con coeficientes

Multiplica: $2\sqrt{3} \cdot 3\sqrt[3]{3}$.

**Paso 1: MCM de índices**
Índices 2 y 3. MCM = 6.

**Paso 2: Convertir**
- $2\sqrt{3} = 2\sqrt[6]{3^3} = 2\sqrt[6]{27}$
- $3\sqrt[3]{3} = 3\sqrt[6]{3^2} = 3\sqrt[6]{9}$

**Paso 3: Multiplicar**
$2 \cdot 3 \cdot \sqrt[6]{27 \cdot 9} = 6\sqrt[6]{243}$.

**Resultado:**

$$
\boxed{6\sqrt[6]{243}}
$$

### Ejemplo 6: Radical con expresión algebraica

Multiplica: $\sqrt{x+1} \cdot \sqrt{x-1}$.

**Razonamiento:**
$\sqrt{(x+1)(x-1)} = \sqrt{x^2 - 1}$.

**Resultado:**

$$
\boxed{\sqrt{x^2 - 1}}
$$

### Ejemplo 7: Raíces cuarta y sexta

Multiplica: $\sqrt[4]{5} \cdot \sqrt[6]{5}$.

**Paso 1: MCM de índices**
Índices 4 y 6. MCM = 12.

**Paso 2: Convertir**
- $\sqrt[4]{5} = \sqrt[12]{5^3}$
- $\sqrt[6]{5} = \sqrt[12]{5^2}$

**Paso 3: Multiplicar**
$$
\sqrt[12]{5^3 \cdot 5^2} = \sqrt[12]{5^5}
$$

**Resultado:**

$$
\boxed{\sqrt[12]{3125}}
$$

### Ejemplo 8: Binomio por binomio con radicales

Multiplica: $(\sqrt{2} + \sqrt{3})(\sqrt{2} - \sqrt{3})$.

**Razonamiento:**
Es una diferencia de cuadrados: $(a+b)(a-b) = a^2 - b^2$.
$(\sqrt{2})^2 - (\sqrt{3})^2 = 2 - 3 = -1$.

**Resultado:**

$$
\boxed{-1}
$$

### Ejemplo 9: Coeficiente grande

Multiplica: $5\sqrt{12} \cdot 2\sqrt{3}$.

**Paso 1: Simplificar primero**
- $\sqrt{12} = 2\sqrt{3}$

**Paso 2: Multiplicar**
$5 \cdot 2\sqrt{3} \cdot \sqrt{3} = 10\sqrt{9} = 10 \cdot 3 = 30$.

**Resultado:**

$$
\boxed{30}
$$

### Ejemplo 10: Tres radicales con diferente índice

Multiplica: $\sqrt{2} \cdot \sqrt[3]{3} \cdot \sqrt[6]{5}$.

**Paso 1: MCM de índices**
Índices 2, 3 y 6. MCM = 6.

**Paso 2: Convertir todos a índice 6**
- $\sqrt{2} = \sqrt[6]{2^3} = \sqrt[6]{8}$
- $\sqrt[3]{3} = \sqrt[6]{3^2} = \sqrt[6]{9}$
- $\sqrt[6]{5} = \sqrt[6]{5}$

**Paso 3: Multiplicar**
$$
\sqrt[6]{8 \cdot 9 \cdot 5} = \sqrt[6]{360}
$$

**Resultado:**

$$
\boxed{\sqrt[6]{360}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Multiplica: $\sqrt{3} \cdot \sqrt{12}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{3 \cdot 12} = \sqrt{36} = 6$.

**Resultado:**
$$
\boxed{6}
$$

</details>

### Ejercicio 2
Multiplica: $2\sqrt{5} \cdot 3\sqrt{2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2 \cdot 3 = 6$.
$5 \cdot 2 = 10$.

**Resultado:**
$$
\boxed{6\sqrt{10}}
$$

</details>

### Ejercicio 3
Multiplica: $\sqrt[3]{4} \cdot \sqrt[3]{2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt[3]{4 \cdot 2} = \sqrt[3]{8} = 2$.

**Resultado:**
$$
\boxed{2}
$$

</details>

### Ejercicio 4
Multiplica: $\sqrt{x} \cdot \sqrt{x^3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{x \cdot x^3} = \sqrt{x^4} = x^2$.

**Resultado:**
$$
\boxed{x^2}
$$

</details>

### Ejercicio 5
Multiplica: $\sqrt{2} \cdot \sqrt[4]{2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
MCM(2,4) = 4.
$\sqrt{2} = \sqrt[4]{2^2}$.
$\sqrt[4]{2^2} \cdot \sqrt[4]{2^1} = \sqrt[4]{2^3}$.

**Resultado:**
$$
\boxed{\sqrt[4]{8}}
$$

</details>

### Ejercicio 6
Multiplica: $(1 + \sqrt{2})(1 - \sqrt{2})$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es una diferencia de cuadrados: $1^2 - (\sqrt{2})^2$.
$1 - 2 = -1$.

**Resultado:**
$$
\boxed{-1}
$$

</details>

### Ejercicio 7
Multiplica: $5\sqrt{3} \cdot \sqrt{3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$5 \cdot \sqrt{9} = 5 \cdot 3 = 15$.

**Resultado:**
$$
\boxed{15}
$$

</details>

### Ejercicio 8
Multiplica: $\sqrt[3]{x^2} \cdot \sqrt[3]{x}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt[3]{x^2 \cdot x} = \sqrt[3]{x^3} = x$.

**Resultado:**
$$
\boxed{x}
$$

</details>

### Ejercicio 9
Multiplica: $\sqrt{2} \cdot \sqrt{3} \cdot \sqrt{6}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{2 \cdot 3 \cdot 6} = \sqrt{36} = 6$.

**Resultado:**
$$
\boxed{6}
$$

</details>

### Ejercicio 10
Multiplica: $\sqrt{a} \cdot \sqrt[3]{b}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
MCM(2,3) = 6.
$\sqrt{a} = \sqrt[6]{a^3}$.
$\sqrt[3]{b} = \sqrt[6]{b^2}$.

**Resultado:**
$$
\boxed{\sqrt[6]{a^3 b^2}}
$$

</details>

---

## 🔑 Resumen

| Caso | Acción |
|------|--------|
| **Mismo Índice** | Multiplica directo ($\sqrt{a} \cdot \sqrt{b} = \sqrt{ab}$). |
| **Coeficientes** | Multiplica los números de afuera entre sí. |
| **Diferente Índice** | Busca el MCM de los índices y convierte los radicales. |
| **Polinomios** | Usa la propiedad distributiva. |

> **Tip:** Siempre intenta simplificar el resultado final. Si te queda $\sqrt{12}$, escribe $2\sqrt{3}$.
