# **Funciones Exponenciales**

¿Alguna vez has escuchado que algo "creció exponencialmente"? Usamos esa frase para decir "muy rápido", pero matemáticamente significa algo más preciso: crecimiento por *multiplicación* constante. Desde los virus hasta los intereses de tu tarjeta de crédito, el mundo funciona con exponentes.

---

## 🎯 ¿Qué vas a aprender?

- Diferenciar crecimiento lineal (suma) de exponencial (multiplicación).
- La anatomía de la fórmula $y = a \cdot b^x$.
- Cómo modelar poblaciones, bacterias y dinero.
- Distinguir crecimientos explosivos de decaimientos rápidos.

---

## 🦠 El Experimento Mental

Imagina dos ofertas de trabajo:

1.  **Oferta A:** Te pagan 1 millón de pesos al día durante 30 días. Total: $30.000.000$.
2.  **Oferta B:** Te pagan 1 peso el primer día, 2 el segundo, 4 el tercero... duplicando cada día durante 30 días.

¿Cuál eliges?
La **Oferta B** te daría más de **500 millones de pesos**. Eso es el poder exponencial.

---

## 🏗️ La Fórmula General

Una función exponencial se ve así:

$$
f(x) = a \cdot b^x
$$

Donde:
- **$a$ (Inicio):** Es la cantidad inicial (cuando $x=0$).
- **$b$ (Base):** Es el factor de crecimiento.
    - Si $b > 1$: **Crece** explosivamente.
    - Si $0 < b < 1$: **Decrece** (se achica) rápidamente.
- **$x$ (Tiempo):** El número de periodos que pasan.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Bacterias en el Laboratorio
Empiezas con 100 bacterias que se **triplican** cada hora.

**1. Identificar partes:**
- Inicio ($a$): 100
- Base ($b$): 3 (se triplican)

**2. Fórmula:**
$$
B(t) = 100 \cdot 3^t
$$

**3. Predicción:**
¿Cuántas habrá en 4 horas?
$$
B(4) = 100 \cdot 3^4
$$
$$
B(4) = 100 \cdot 81 = 8100 \text{ bacterias}
$$

**Resultado:**
$$
\boxed{8100 \text{ bacterias}}
$$

---

### Ejemplo 2: El Auto Nuevo (Depreciación)
Compras un auto por 20.000.000 de pesos. Cada año pierde el 10% de su valor (o sea, conserva el 90%).

**1. Identificar partes:**
- Inicio ($a$): 20.000.000
- Base ($b$): 0.90 (el 90% que queda)

**2. Fórmula:**
$$
V(t) = 20.000.000 \cdot (0.9)^t
$$

**3. Predicción:**
¿Valor en 5 años?
$$
V(5) = 20.000.000 \cdot (0.9)^5
$$
$$
V(5) = 20.000.000 \cdot 0.59049 \approx 11.809.800
$$

**Resultado:**
$$
\boxed{11.809.800 \text{ pesos}}
$$

---

### Ejemplo 3: ¿Crece o Decrece?
Analiza $f(x) = 500 \cdot (1.05)^x$.

**Razonamiento:**
Miramos la base $b = 1.05$.
Como $1.05 > 1$, la función **crece**.
De hecho, crece un 5% en cada paso (el 0.05 extra).

**Resultado:**
$$
\boxed{\text{Crece}}
$$

---

### Ejemplo 4: El Papel Doblado
Si doblas una hoja de papel (grosor 0.1 mm) por la mitad 42 veces, ¿qué tan gruesa sería?

**Fórmula:**
$$
G(n) = 0.1 \cdot 2^n
$$
$$
G(42) = 0.1 \cdot 2^{42} \approx 439.804.651.110 \text{ mm}
$$
¡Eso es 439.804 km! (Más que la distancia a la Luna).

**Resultado:**
$$
\boxed{\approx 440.000 \text{ km}}
$$

---

### Ejemplo 5: Gráfica Básica
Graficar $y = 2^x$.

Calculamos puntos:
- $x=0 \implies y = 2^0 = 1$ (Punto $0,1$)
- $x=1 \implies y = 2^1 = 2$ (Punto $1,2$)
- $x=2 \implies y = 2^2 = 4$ (Punto $2,4$)
- $x=-1 \implies y = 2^{-1} = 0.5$ (Punto $-1, 0.5$)

La curva nunca toca el eje X (asíntota horizontal), pero sube rapidísimo a la derecha.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si tienes 5 conejos y se duplican cada mes, escribe la función.

<details>
<summary>Ver solución</summary>

$a=5, b=2$.
**Resultado:** $\boxed{f(x) = 5 \cdot 2^x}$

</details>

---

### Ejercicio 2
Calcula $3 \cdot 2^4$.

<details>
<summary>Ver solución</summary>

$3 \cdot 16 = 48$.
**Resultado:** $\boxed{48}$

</details>

---

### Ejercicio 3
¿La función $y = 100 \cdot (0.8)^x$ representa crecimiento o decrecimiento?

<details>
<summary>Ver solución</summary>

Decrecimiento ($0.8 < 1$).

</details>

---

### Ejercicio 4
Si una población crece al 15% anual, ¿cuál es su base $b$?

<details>
<summary>Ver solución</summary>

$100\% + 15\% = 115\% = 1.15$.
**Resultado:** $\boxed{1.15}$

</details>

---

### Ejercicio 5
Evalúa $f(x) = 10 \cdot 3^{x}$ para $x=2$.

<details>
<summary>Ver solución</summary>

$10 \cdot 9 = 90$.
**Resultado:** $\boxed{90}$

</details>

---

### Ejercicio 6
Una sustancia radiactiva se reduce a la mitad cada día. Inicio: 80g.

<details>
<summary>Ver solución</summary>

$f(x) = 80 \cdot (0.5)^x$.

</details>

---

### Ejercicio 7
¿Cuánto es $5^0$?

<details>
<summary>Ver solución</summary>

Todo número elevado a 0 es 1.
**Resultado:** $\boxed{1}$

</details>

---

### Ejercicio 8
En la función $y = 50 \cdot 2^x$, ¿qué representa el 50?

<details>
<summary>Ver solución</summary>

El valor inicial.

</details>

---

### Ejercicio 9
Si inviertes 100 pesos al 100% de interés anual compuesto, ¿base?

<details>
<summary>Ver solución</summary>

$1 + 1 = 2$. Se duplica.
**Resultado:** $\boxed{b=2}$

</details>

---

### Ejercicio 10
Predice el valor siguiente en la secuencia: $3, 6, 12, 24, \dots$

<details>
<summary>Ver solución</summary>

Se multiplica por 2.
**Resultado:** $\boxed{48}$

</details>

---

## 🔑 Resumen

| Parte | Nombre | Significado |
|:--- |:--- |:--- |
| **$a$** | Valor Inicial | Cantidad cuando $t=0$. El corte con el eje Y. |
| **$b$** | Base | $b>1$: Crecimiento. $0<b<1$: Decaimiento. |
| **$x$** | Exponente | Indica cuántas veces multiplicamos la base. |

> **Conclusión:** La función exponencial es el motor detrás de las pandemias, las inversiones y las explosiones demográficas. Es la forma en que la naturaleza se multiplica.
