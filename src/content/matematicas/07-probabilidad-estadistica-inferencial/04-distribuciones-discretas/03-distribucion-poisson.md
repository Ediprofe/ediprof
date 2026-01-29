# Distribución Poisson

La **distribución de Poisson** modela el número de eventos que ocurren en un intervalo fijo de tiempo o espacio, cuando estos eventos ocurren de manera aleatoria e independiente.

---

## 🎯 ¿Qué vas a aprender?

- Cuándo usar la distribución Poisson
- La fórmula de probabilidad
- Ejemplos de aplicación
- Media, varianza y relación con la binomial

---

## 📖 ¿Cuándo Aplica Poisson?

| Condición | Descripción |
|-----------|-------------|
| Eventos en intervalo | Contamos eventos en tiempo, espacio o tamaño fijo |
| Independencia | Un evento no afecta la probabilidad de otro |
| Tasa constante | La tasa promedio de eventos es constante |
| Eventos raros | Cada momento individual tiene baja probabilidad |

### ⚙️ Ejemplos típicos:

- Llamadas al call center por hora
- Clientes que llegan a un banco por minuto
- Errores tipográficos por página
- Accidentes en una autopista por día
- Correos spam recibidos por hora

---

## 📖 Notación

$$
X \sim Poisson(\lambda)
$$

Donde:
- $\lambda$ = tasa promedio de eventos (también es la media)
- X = número de eventos observados

---

## 📖 Fórmula de Probabilidad

$$
P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}
$$

Donde:
- k = 0, 1, 2, 3, ... (puede ser cualquier entero no negativo)
- e ≈ 2.71828 (número de Euler)

---

## 📖 Ejemplo: Call Center

Un call center recibe en promedio 4 llamadas por minuto.

$X \sim Poisson(4)$

### ⚙️ P(exactamente 3 llamadas en un minuto):

$$
P(X = 3) = \frac{e^{-4} \cdot 4^3}{3!} = \frac{0.0183 \cdot 64}{6} = 0.195
$$

### ⚙️ P(ninguna llamada):

$$
P(X = 0) = \frac{e^{-4} \cdot 4^0}{0!} = e^{-4} = 0.0183
$$

### ⚙️ P(al menos 1 llamada):

$$
P(X \geq 1) = 1 - P(X = 0) = 1 - 0.0183 = 0.9817
$$

---

## 📖 Media y Varianza

Para $X \sim Poisson(\lambda)$:

### 💡 Media (valor esperado):

$$
E(X) = \lambda
$$

### 💡 Varianza:

$$
Var(X) = \lambda
$$

### 💡 Propiedad especial:

¡En Poisson, **media = varianza = λ**!

Esto es útil: si en datos reales la media ≈ varianza, podría ser Poisson.

---

## 📖 Escalando Intervalos

### 💡 Regla:

Si λ es la tasa para un intervalo, para un intervalo k veces más grande, la tasa es kλ.

### ⚙️ Ejemplo:

Si hay 4 llamadas/minuto (λ = 4):
- En 2 minutos: λ = 8
- En 30 segundos: λ = 2
- En 1 hora: λ = 240

### ⚙️ Aplicación:

¿Cuál es P(exactamente 6 llamadas en 2 minutos)?

$\lambda_{2min} = 4 \times 2 = 8$

$$
P(X = 6) = \frac{e^{-8} \cdot 8^6}{6!} = \frac{0.000335 \cdot 262144}{720} = 0.1221
$$

---

## 📖 Poisson como Aproximación de Binomial

### 💡 Regla:

Si $X \sim Bin(n, p)$ con:
- n grande (≥ 20)
- p pequeño (≤ 0.05)
- np moderado

Entonces $X \approx Poisson(\lambda)$ donde $\lambda = np$

### ⚙️ Ejemplo:

Un website tiene 10,000 visitantes/día. Cada uno tiene 0.05% de probabilidad de comprar.

$X \sim Bin(10000, 0.0005)$

Usando aproximación Poisson con $\lambda = 10000 \times 0.0005 = 5$:

$$
P(X = 3) \approx \frac{e^{-5} \cdot 5^3}{3!} = \frac{0.00674 \cdot 125}{6} = 0.140
$$

---

## 📖 Tabla de Probabilidades Poisson

Para λ = 3:

| k | P(X = k) |
|---|----------|
| 0 | 0.0498 |
| 1 | 0.1494 |
| 2 | 0.2240 |
| 3 | 0.2240 |
| 4 | 0.1680 |
| 5 | 0.1008 |
| 6 | 0.0504 |
| ≥7 | 0.0336 |

---

## 🔑 Resumen

| Concepto | Fórmula/Valor |
|----------|---------------|
| **Probabilidad** | $P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}$ |
| **Media** | $E(X) = \lambda$ |
| **Varianza** | $Var(X) = \lambda$ |
| **Uso** | Eventos aleatorios en intervalo fijo |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Un restaurante recibe en promedio 12 clientes por hora. ¿Cuál es la probabilidad de que en los próximos 15 minutos lleguen exactamente 4?

<details>
<summary>Ver solución</summary>

λ para 15 min = 12 × (15/60) = 12 × 0.25 = 3

$P(X = 4) = \frac{e^{-3} \cdot 3^4}{4!} = \frac{0.0498 \cdot 81}{24} = 0.168$

</details>

### Ejercicio 2
En promedio hay 2 accidentes por semana en una autopista. ¿Cuál es la probabilidad de ningún accidente en una semana?

<details>
<summary>Ver solución</summary>

$X \sim Poisson(2)$

$P(X = 0) = \frac{e^{-2} \cdot 2^0}{0!} = e^{-2} = 0.1353$

Aproximadamente 13.5% de probabilidad.

</details>

### Ejercicio 3
Si X ~ Poisson(5), calcula P(X ≤ 2).

<details>
<summary>Ver solución</summary>

$P(X \leq 2) = P(0) + P(1) + P(2)$

$P(0) = e^{-5} = 0.0067$
$P(1) = e^{-5} \cdot 5 = 0.0337$
$P(2) = e^{-5} \cdot 25/2 = 0.0842$

$P(X \leq 2) = 0.0067 + 0.0337 + 0.0842 = 0.1246$

</details>

### Ejercicio 4
¿Por qué es especial que en Poisson la media sea igual a la varianza?

<details>
<summary>Ver solución</summary>

Es especial porque:

1. **Diagnóstico:** Si en datos reales calculamos media ≈ varianza, sugiere que Poisson podría ser un buen modelo.

2. **Un solo parámetro:** Solo necesitamos λ para describir toda la distribución.

3. **Contraste con binomial:** En binomial, media = np y varianza = np(1-p), están relacionadas pero no son iguales.

4. **Verificación:** Es una forma de verificar si el modelo Poisson es apropiado para ciertos datos.

</details>
