# **Logaritmos**

"Logaritmo" es una palabra que asusta, pero en el fondo es algo muy simple: es un buscador de exponentes. Si la exponenciación es multiplicar, el logaritmo es preguntar "¿cuántas veces multipliqué?". Es el detective que averigua el tiempo en las fórmulas de crecimiento.

---

## 🎯 ¿Qué vas a aprender?

- Que un logaritmo es solo un exponente disfrazado.
- Cómo pasar de forma exponencial ($2^3=8$) a logarítmica ($\log_2 8 = 3$).
- Calcular logaritmos mentalmente.
- Entender los logaritmos especiales: $\log$ (base 10) y $\ln$ (base $e$).

---

## 🔍 La Pregunta Clave

Cuando veas esto:
$$
\log_b(x)
$$
Debes leerlo como una pregunta:
**"¿A qué potencia debo elevar la base $b$ para obtener el número $x$?"**

### Ejemplo Conceptual
$$
\log_2(8) = ?
$$
*Traducción:* ¿Cuántas veces multiplico el 2 para llegar a 8?
$2 \cdot 2 \cdot 2 = 8$ (3 veces).
$$
\log_2(8) = 3
$$

---

## 🔄 El Diccionario Bilingüe

La logaritmación y la exponenciación son dos formas de decir lo mismo.

$$
\text{Logarítmica: } \log_{\text{base}}(\text{resultado}) = \text{exponente}
$$
$$
\text{Exponencial: } \text{base}^{\text{exponente}} = \text{resultado}
$$

| Exponencial | Logarítmica |
|:--- |:--- |
| $5^2 = 25$ | $\log_5(25) = 2$ |
| $2^4 = 16$ | $\log_2(16) = 4$ |
| $10^3 = 1000$ | $\log_{10}(1000) = 3$ |
| $3^{-1} = \frac{1}{3}$ | $\log_3(\frac{1}{3}) = -1$ |

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Cálculo Mental
Calcular $\log_3(81)$.

**Pregunta:** ¿$3$ elevado a qué me da $81$?
- $3^1 = 3$
- $3^2 = 9$
- $3^3 = 27$
- $3^4 = 81$

**Resultado:**
$$
\boxed{4}
$$

### Ejemplo 2: El Logaritmo de 1
Calcular $\log_7(1)$.

**Pregunta:** ¿$7$ elevado a qué me da $1$?
Sabemos que cualquier número elevado a 0 es 1.

**Resultado:**
$$
\boxed{0}
$$

### Ejemplo 3: Base 10
Calcular $\log(100)$.
(Cuando no se escribe la base, asumimos base 10).

**Pregunta:** ¿$10$ elevado a qué me da $100$?
$10^2 = 100$.

**Resultado:**
$$
\boxed{2}
$$

### Ejemplo 4: Fracciones
Calcular $\log_2(\frac{1}{8})$.

**Pregunta:** ¿$2$ elevado a qué da $\frac{1}{8}$?
Sabemos que $2^3 = 8$. Para que se invierta ($1/8$), el exponente debe ser negativo.

**Resultado:**
$$
\boxed{-3}
$$

### Ejemplo 5: Incógnita en la Base
Si $\log_x(36) = 2$, ¿cuánto vale $x$?

**Traducción:** $x^2 = 36$.
¿Qué número al cuadrado es 36? (Base debe ser positiva).

**Resultado:**
$$
\boxed{x = 6}
$$

---

## 🌟 Logaritmos Famosos

### Logaritmo Común ($\log$)
Usa base 10. Es el de la escala Richter (terremotos) y el pH (química).
$$
\log(1000) = 3 \quad (\text{que significa } 10^3)
$$

### Logaritmo Natural ($\ln$)
Usa base $e \approx 2.718$. Es el lenguaje de la naturaleza y el cálculo.
$$
\ln(e) = 1 \quad (\text{que significa } e^1)
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe $4^3 = 64$ en forma logarítmica.

<details>
<summary>Ver solución</summary>

$\log_4(64) = 3$.

</details>

---

### Ejercicio 2
Calcula $\log_5(125)$.

<details>
<summary>Ver solución</summary>

$5^3 = 125$.
**Resultado:** $\boxed{3}$

</details>

---

### Ejercicio 3
Calcula $\log_{10}(0.1)$.

<details>
<summary>Ver solución</summary>

$0.1 = 1/10 = 10^{-1}$.
**Resultado:** $\boxed{-1}$

</details>

---

### Ejercicio 4
Si $\log_2(x) = 5$, encuentra $x$.

<details>
<summary>Ver solución</summary>

$2^5 = x \implies x = 32$.
**Resultado:** $\boxed{32}$

</details>

---

### Ejercicio 5
Calcula $\log_9(3)$.

<details>
<summary>Ver solución</summary>

Razonamiento: $\sqrt{9} = 3 \implies 9^{1/2} = 3$.
**Resultado:** $\boxed{0.5 \text{ o } 1/2}$

</details>

---

### Ejercicio 6
Calcula $\ln(1)$.

<details>
<summary>Ver solución</summary>

¿$e$ elevado a qué da 1? Siempre es 0.
**Resultado:** $\boxed{0}$

</details>

---

### Ejercicio 7
Calcula $\log_4(2)$.

<details>
<summary>Ver solución</summary>

$\sqrt{4}=2$, o sea exponente $1/2$.
**Resultado:** $\boxed{0.5}$

</details>

---

### Ejercicio 8
¿Cuánto es $\log_b(b)$?

<details>
<summary>Ver solución</summary>

Siempre es 1.

</details>

---

### Ejercicio 9
Resuelve para $x$: $\log_x(16) = 4$.

<details>
<summary>Ver solución</summary>

$x^4 = 16$. ¿Qué número multiplicado 4 veces da 16? El 2.
**Resultado:** $\boxed{2}$

</details>

---

### Ejercicio 10
Calcula $\log(10,000,000)$.

<details>
<summary>Ver solución</summary>

Cuenta los ceros.
**Resultado:** $\boxed{7}$

</details>

---

## 🔑 Resumen

| Símbolo | Significado | Traducción Mental |
|:--- |:--- |:--- |
| $\log_b x$ | Logaritmo en base $b$ | ¿$b$ a la qué potencia da $x$? |
| $\log x$ | Logaritmo común | Base 10 implícita. |
| $\ln x$ | Logaritmo natural | Base $e$ implícita. |

> **Conclusión:** El logaritmo no es mágico, es simplemente preguntar "¿cuál es el exponente?". Es la operación inversa a potenciar, igual que restar es lo inverso a sumar.
