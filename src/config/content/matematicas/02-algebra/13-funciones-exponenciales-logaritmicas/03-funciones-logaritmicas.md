---
title: "Funciones Logarítmicas"
---

# **Funciones Logarítmicas**

Si la función exponencial es un cohete que sube al espacio, la función logarítmica es la gravedad que lo trae de vuelta a la Tierra. Son las dos caras de la misma moneda: operaciones inversas que se deshacen mutuamente. Entenderlas es clave para medir fenómenos que varían enormemente, como la acidez (pH) o la intensidad de un terremoto.

---

## 🎯 ¿Qué vas a aprender?

- Comprender la función logarítmica como la inversa de la exponencial.
- Identificar su dominio (¡solo positivos!) y su asíntota vertical.
- Graficar funciones básicas como $y = \log_2(x)$.
- Analizar cómo se comportan el dominio y el rango.

---

## 🔄 El Espejo Matemático

La función logarítmica es simplemente la función exponencial reflejada en un espejo. Si en la exponencial cambiamos $x$ por $y$, obtenemos la logarítmica.

- **Exponencial ($y = 2^x$):** Entras un tiempo, sale un crecimiento gigante.
- **Logarítmica ($y = \log_2 x$):** Entras un número gigante, sale el tiempo que tomó llegar ahí.

![Inversa: Exponencial vs Logarítmica](/images/matematicas/algebra/funciones-exponenciales-logaritmicas/log_vs_exp.svg)

Observa en la gráfica cómo la línea punteada $y=x$ actúa como un espejo. El punto $(2, 4)$ de la exponencial se convierte en $(4, 2)$ en la logarítmica.

---

## 🏗️ La Fórmula General

Una función logarítmica estándar tiene esta forma:

$$
f(x) = \log_b(x)
$$

Sus reglas de juego son muy estrictas:

1.  **Entrada ($$x > 0$$):** Solo acepta números **mayores que cero**. No existen logaritmos de ceros ni de negativos.
2.  **Salida:** Puede dar cualquier número, positivo o negativo.
3.  **La pared ($$x=0$$):** La gráfica se acerca infinitamente al eje Y pero nunca lo toca. Es como una barrera invisible.

![Función Logarítmica Básica](/images/matematicas/algebra/funciones-exponenciales-logaritmicas/log_basic_graph_v3.svg)

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Evaluando la función
Dada la función $f(x) = \log_2(x)$, encuentra $f(8)$.

**Razonamiento:**
Sustituimos $x$ por 8 en la función:

$$
f(8) = \log_2(8)
$$

Nos preguntamos: ¿2 elevado a qué potencia da 8?
$2^3 = 8$.

**Resultado:**
$$
\boxed{3}
$$

![Evaluando el Logaritmo](/images/matematicas/algebra/funciones-exponenciales-logaritmicas/example1_eval.svg)

---

### Ejemplo 2: ¿Qué números funcionan?
Encuentra qué valores de $$x$$ sirven para $$g(x) = \log_5(x - 3)$$.

**Razonamiento:**
Lo que está dentro del logaritmo debe ser **mayor que cero**.

$$
x - 3 > 0
$$

Despejamos $$x$$:

$$
x > 3
$$

**Resultado:**
$$
\boxed{\text{Cualquier número mayor que 3}}
$$

![Dominio Desplazado](/images/matematicas/algebra/funciones-exponenciales-logaritmicas/example2_domain.svg)

---

### Ejemplo 3: Graficando Puntos
Encuentra el punto en la gráfica de $y = \log_3(x)$ cuando $x = 9$.

**Razonamiento:**
Sustituimos $x=9$:

$$
y = \log_3(9)
$$

Calculamos el logaritmo ($3^2 = 9$):

$$
y = 2
$$

El punto es $(x, y)$.

**Resultado:**
$$
\boxed{(9, 2)}
$$

![Punto en la Gráfica](/images/matematicas/algebra/funciones-exponenciales-logaritmicas/example3_point.svg)

---

### Ejemplo 4: Transformación Inversa
Si $f(x) = 10^x$, encuentra su función inversa $f^{-1}(x)$.

**Razonamiento:**
La inversa de una exponencial de base $b$ es siempre el logaritmo de base $b$.
Como la base es 10, la inversa es el logaritmo común.

**Resultado:**
$$
\boxed{f^{-1}(x) = \log(x)}
$$

![Función Inversa](/images/matematicas/algebra/funciones-exponenciales-logaritmicas/example4_inverse.svg)

---

### Ejemplo 5: Comparación de Crecimiento
¿Cuál valor es mayor: $f(100)$ para $f(x)=\sqrt{x}$ o para $g(x)=\log(x)$?

**Razonamiento:**
Evaluamos ambas funciones en $x=100$.

1. Para la raíz cuadrada:
$$
\sqrt{100} = 10
$$

2. Para el logaritmo (base 10):
$$
\log(100) = 2
$$

La raíz cuadrada crece más rápido que el logaritmo.

**Resultado:**
$$
\boxed{\sqrt{100} > \log(100)}
$$

![Comparación de Crecimiento](/images/matematicas/algebra/funciones-exponenciales-logaritmicas/example5_growth.svg)

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Evalúa $f(x) = \log_4(x)$ cuando $x=64$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
¿4 elevado a qué da 64? $4^3 = 64$.

**Resultado:**
$$
\boxed{3}
$$

</details>

---

### Ejercicio 2
¿Para qué valores de $$x$$ funciona $$h(x) = \log(x + 5)$$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$x + 5 > 0 \implies x > -5$$.

**Resultado:**
$$
\boxed{x > -5}
$$

</details>

---

### Ejercicio 3
Si $f(x) = \ln(x)$, ¿cuánto vale $f(e)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\ln$ es base $e$. $\log_e(e) = 1$.

**Resultado:**
$$
\boxed{1}
$$

</details>

---

### Ejercicio 4
¿Cuál es la "pared" o límite vertical de $$y = \log_2(x)$$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El logaritmo no puede tocar el 0.

**Resultado:**
$$
\boxed{x = 0}
$$

</details>

---

### Ejercicio 5
Convierte $y = \log_3(x)$ a su forma exponencial.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Base 3, exponente $y$, resultado $x$.

**Resultado:**
$$
\boxed{x = 3^y}
$$

</details>

---

### Ejercicio 6
Encuentra el intercepto en X de $y = \log_5(x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El intercepto es cuando $y=0$.
$0 = \log_5(x) \implies 5^0 = x \implies x = 1$.

**Resultado:**
$$
\boxed{(1, 0)}
$$

</details>

---

### Ejercicio 7
Evalúa $f(x) = \log_{0.5}(4)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(1/2)^? = 4$. Si invertimos es 2, y al cuadrado es 4. Entonces $-2$.

**Resultado:**
$$
\boxed{-2}
$$

</details>

---

### Ejercicio 8
¿Qué valores de $$x$$ acepta $$y = \log(2x)$$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$2x > 0 \implies x > 0$$.

**Resultado:**
$$
\boxed{x > 0}
$$

</details>

---

### Ejercicio 9
¿Cuál función crece más lento: $x$ o $\ln(x)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El logaritmo aplana curvas gigantes. Crece mucho más lento que la lineal.

**Resultado:**
$$
\boxed{\ln(x)}
$$

</details>

---

### Ejercicio 10
Si la gráfica pasa por $(b, 1)$, ¿cuál es la base?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$1 = \log_{\text{base}}(b)$. Base a la 1 es $b$.
La base es el mismo valor $x$ donde $y=1$.

**Resultado:**
$$
\boxed{\text{La base es } b}
$$

</details>

---

## 🔑 Resumen

| Concepto | Característica | Importancia |
| :--- | :--- | :--- |
| **Entrada ($$x$$)** | $$x > 0$$ | No existen logaritmos de negativos. |
| **Salida ($$y$$)** | Cualquier número | Puede dar positivo o negativo. |
| **Límite** | $$x = 0$$ | La gráfica choca contra una pared invisible en el eje Y. |
| **Punto Clave** | $$(1, 0)$$ | $$\log(1)$$ siempre es 0, sin importar la base. |

> **Conclusión:** Las funciones logarítmicas son las "frenos" del crecimiento matemático. Nos permiten manejar números astronómicos convirtiéndolos en valores pequeños y manejables.
