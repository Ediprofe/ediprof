# Otras Distribuciones Continuas

Además de la normal, existen otras distribuciones continuas importantes. Aquí presentamos brevemente las más usadas en estadística aplicada.

---

## 🎯 ¿Qué vas a aprender?

- La distribución uniforme continua
- La distribución exponencial
- Breve introducción a t-Student, Chi-cuadrado y F

---

## 📖 Distribución Uniforme Continua

> En la distribución **uniforme**, todos los valores en un intervalo [a, b] tienen la misma probabilidad.

### 💡 Notación:

$$
X \sim U(a, b)
$$

### 💡 Función de densidad:

$$
f(x) = \frac{1}{b-a} \text{ para } a \leq x \leq b
$$

### 💡 Media y varianza:

$$
E(X) = \frac{a + b}{2}
$$

$$
Var(X) = \frac{(b-a)^2}{12}
$$

### ⚙️ Ejemplo:

El tiempo de llegada de un bus está uniformemente distribuido entre 0 y 20 minutos.

$X \sim U(0, 20)$

**P(esperar menos de 5 minutos):**
$$
P(X < 5) = \frac{5 - 0}{20 - 0} = \frac{5}{20} = 0.25
$$

**Tiempo promedio de espera:**
$$
E(X) = \frac{0 + 20}{2} = 10 \text{ minutos}
$$

---

## 📖 Distribución Exponencial

> La distribución **exponencial** modela el tiempo entre eventos en un proceso de Poisson.

### 💡 Notación:

$$
X \sim Exp(\lambda)
$$

Donde λ es la tasa de eventos (la misma λ de Poisson).

### 💡 Función de densidad:

$$
f(x) = \lambda e^{-\lambda x} \text{ para } x \geq 0
$$

### 💡 Función de distribución:

$$
P(X \leq x) = 1 - e^{-\lambda x}
$$

### 💡 Media y varianza:

$$
E(X) = \frac{1}{\lambda}
$$

$$
Var(X) = \frac{1}{\lambda^2}
$$

### ⚙️ Ejemplo:

Clientes llegan a una tienda a razón de 4 por hora (λ = 4).

¿Cuál es la probabilidad de esperar más de 30 minutos (0.5 horas) para el próximo cliente?

$$
P(X > 0.5) = e^{-4 \times 0.5} = e^{-2} \approx 0.135
$$

**Tiempo promedio entre clientes:**
$$
E(X) = \frac{1}{4} = 0.25 \text{ horas} = 15 \text{ minutos}
$$

---

## 📖 Propiedad de Pérdida de Memoria

La exponencial es la **única** distribución continua con la propiedad de "pérdida de memoria":

$$
P(X > s + t | X > s) = P(X > t)
$$

### 💡 Interpretación:

Si ya esperaste s minutos, la probabilidad de esperar t minutos más es la misma que si acabaras de empezar.

---

## 📖 Distribución t de Student

> Se usa cuando estimamos la media poblacional con muestras pequeñas y σ desconocida.

### 💡 Características:

- Similar a la normal pero con colas más pesadas
- Depende de los **grados de libertad** (df = n - 1)
- Cuando df → ∞, se aproxima a la normal

### 💡 Uso:

$$
t = \frac{\bar{X} - \mu}{s/\sqrt{n}}
$$

donde s es la desviación estándar muestral.

---

## 📖 Distribución Chi-Cuadrado (χ²)

> Se usa para pruebas de varianza y pruebas de independencia.

### 💡 Características:

- Solo valores positivos
- Sesgada a la derecha
- Depende de grados de libertad

### 💡 Uso típico:

$$
\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}
$$

donde O = observado, E = esperado.

---

## 📖 Distribución F

> Se usa para comparar varianzas de dos poblaciones (ANOVA).

### 💡 Características:

- Razón de dos Chi-cuadrados
- Solo valores positivos
- Depende de dos parámetros de grados de libertad

---

## 📊 Resumen de Distribuciones Continuas

| Distribución | Uso típico | Parámetros |
|--------------|------------|------------|
| **Normal** | Fenómenos naturales | μ, σ |
| **Uniforme** | Igual probabilidad en intervalo | a, b |
| **Exponencial** | Tiempo entre eventos | λ |
| **t-Student** | Media con muestra pequeña | df |
| **Chi-cuadrado** | Varianza, independencia | df |
| **F** | Comparar varianzas | df₁, df₂ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
X ~ U(10, 30). Calcula:
a) E(X)
b) P(15 < X < 25)

<details>
<summary>Ver solución</summary>

a) $E(X) = \frac{10 + 30}{2} = 20$

b) $P(15 < X < 25) = \frac{25 - 15}{30 - 10} = \frac{10}{20} = 0.5$

</details>

### Ejercicio 2
El tiempo entre fallas de una máquina sigue Exp(0.1) en horas. ¿Cuál es la probabilidad de que funcione al menos 20 horas sin fallar?

<details>
<summary>Ver solución</summary>

$P(X > 20) = e^{-0.1 \times 20} = e^{-2} = 0.135$

13.5% de probabilidad.

</details>

### Ejercicio 3
¿Por qué usamos t-Student en lugar de la normal cuando la muestra es pequeña?

<details>
<summary>Ver solución</summary>

Usamos t-Student porque:

1. **No conocemos σ poblacional:** Debemos estimarla con s (desviación muestral).

2. **Más incertidumbre:** La estimación de σ con muestras pequeñas es menos precisa, lo que añade variabilidad.

3. **Colas más pesadas:** La t-Student tiene colas más gruesas que la normal, lo que refleja esta mayor incertidumbre y da intervalos de confianza más amplios (más conservadores).

4. **Convergencia:** Cuando n crece (≥30), t-Student se aproxima a la normal y la diferencia es mínima.

</details>
