# Distribución Binomial

La **distribución binomial** es una de las más importantes en estadística. Modela situaciones donde hay un número fijo de ensayos independientes, cada uno con dos posibles resultados: éxito o fracaso.

---

## 🎯 ¿Qué vas a aprender?

- Cuándo aplica la distribución binomial
- La fórmula de la probabilidad binomial
- Cómo calcular probabilidades específicas
- El valor esperado y la varianza

---

## 📖 Condiciones para Distribución Binomial

Un experimento sigue distribución binomial si:

| Condición | Descripción |
|-----------|-------------|
| **n fijo** | Número de ensayos es fijo |
| **Dos resultados** | Cada ensayo: éxito o fracaso |
| **Independencia** | Los ensayos son independientes |
| **p constante** | Probabilidad de éxito es igual en cada ensayo |

### ⚙️ Ejemplos que SÍ son binomiales:

- Lanzar moneda 10 veces, contar caras
- 20 pacientes, contar cuántos se curan
- 50 productos, contar cuántos son defectuosos

### ⚙️ Ejemplos que NO son binomiales:

- Sacar cartas sin reemplazo (probabilidad cambia)
- Contar clientes hasta el primero que compra (n no es fijo)

---

## 📖 Notación

$$
X \sim Bin(n, p)
$$

- X = número de éxitos
- n = número de ensayos
- p = probabilidad de éxito en cada ensayo
- q = 1 - p = probabilidad de fracaso

---

## 📖 Fórmula de Probabilidad

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

Donde:
- $\binom{n}{k} = C(n,k) = \frac{n!}{k!(n-k)!}$ es el coeficiente binomial
- k = número de éxitos deseados (0 ≤ k ≤ n)

### 💡 Interpretación de cada parte:

- $\binom{n}{k}$: Formas de elegir cuáles k ensayos son éxitos
- $p^k$: Probabilidad de k éxitos
- $(1-p)^{n-k}$: Probabilidad de (n-k) fracasos

---

## 📖 Ejemplo: Lanzar Moneda 5 Veces

X = número de caras en 5 lanzamientos

$X \sim Bin(5, 0.5)$

### ⚙️ P(exactamente 3 caras):

$$
P(X = 3) = \binom{5}{3} (0.5)^3 (0.5)^2 = 10 \cdot 0.125 \cdot 0.25 = 0.3125
$$

### ⚙️ Toda la distribución:

| k | $\binom{5}{k}$ | P(X = k) |
|---|----------------|----------|
| 0 | 1 | 0.03125 |
| 1 | 5 | 0.15625 |
| 2 | 10 | 0.3125 |
| 3 | 10 | 0.3125 |
| 4 | 5 | 0.15625 |
| 5 | 1 | 0.03125 |
| **Total** | | **1.00** |

---

## 📖 Ejemplo: Control de Calidad

Una máquina produce 10% de piezas defectuosas. De un lote de 20 piezas, ¿cuál es la probabilidad de encontrar exactamente 3 defectuosas?

$X \sim Bin(20, 0.1)$

$$
P(X = 3) = \binom{20}{3} (0.1)^3 (0.9)^{17}
$$
$$
= 1140 \cdot 0.001 \cdot 0.1668 = 0.1901
$$

---

## 📖 Probabilidades Acumuladas

### 💡 "Al menos", "A lo más", "Más de":

| Expresión | Cálculo |
|-----------|---------|
| P(X ≤ k) | $\sum_{i=0}^{k} P(X = i)$ |
| P(X < k) | P(X ≤ k-1) |
| P(X ≥ k) | 1 - P(X ≤ k-1) |
| P(X > k) | 1 - P(X ≤ k) |

### ⚙️ Ejemplo: Al menos 2 caras en 5 lanzamientos

$P(X \geq 2) = 1 - P(X \leq 1) = 1 - [P(X=0) + P(X=1)]$
$= 1 - [0.03125 + 0.15625] = 1 - 0.1875 = 0.8125$

---

## 📖 Valor Esperado y Varianza

Para $X \sim Bin(n, p)$:

### 💡 Valor esperado:

$$
E(X) = n \cdot p
$$

### 💡 Varianza:

$$
Var(X) = n \cdot p \cdot (1-p) = n \cdot p \cdot q
$$

### 💡 Desviación estándar:

$$
\sigma = \sqrt{n \cdot p \cdot q}
$$

### ⚙️ Ejemplo:

Si $X \sim Bin(20, 0.1)$:

- $E(X) = 20 \times 0.1 = 2$
- $Var(X) = 20 \times 0.1 \times 0.9 = 1.8$
- $\sigma = \sqrt{1.8} \approx 1.34$

**Interpretación:** En promedio, esperamos 2 defectuosas en cada lote de 20, con una desviación típica de 1.34.

---

## 📖 Forma de la Distribución

| Condición | Forma |
|-----------|-------|
| p = 0.5 | Simétrica |
| p < 0.5 | Sesgada a la derecha |
| p > 0.5 | Sesgada a la izquierda |
| n grande, p no extremo | Aproximadamente normal |

---

## 🔑 Resumen

| Concepto | Fórmula |
|----------|---------|
| **Probabilidad** | $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$ |
| **Media** | $E(X) = np$ |
| **Varianza** | $Var(X) = np(1-p)$ |
| **Condiciones** | n fijo, independientes, p constante |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Un estudiante adivina las respuestas de un examen de 10 preguntas de verdadero/falso. ¿Cuál es la probabilidad de acertar exactamente 7?

<details>
<summary>Ver solución</summary>

$X \sim Bin(10, 0.5)$

$P(X = 7) = \binom{10}{7}(0.5)^7(0.5)^3$
$= 120 \cdot 0.0078 \cdot 0.125 = 0.1172$

Probabilidad ≈ 11.7%

</details>

### Ejercicio 2
El 30% de los clientes de un banco usa banca online. De 15 clientes:
a) ¿Cuál es el número esperado que usa banca online?
b) ¿Cuál es P(exactamente 5)?

<details>
<summary>Ver solución</summary>

$X \sim Bin(15, 0.3)$

a) $E(X) = 15 \times 0.3 = 4.5$ clientes

b) $P(X = 5) = \binom{15}{5}(0.3)^5(0.7)^{10}$
$= 3003 \cdot 0.00243 \cdot 0.0282 = 0.206$

</details>

### Ejercicio 3
Una vacuna tiene 95% de efectividad. Si se vacunan 100 personas, ¿cuál es la probabilidad de que al menos 90 estén protegidas?

<details>
<summary>Ver solución</summary>

$X \sim Bin(100, 0.95)$

Esto requiere calcular $P(X \geq 90) = \sum_{k=90}^{100} P(X=k)$

Usando la media: $E(X) = 100 \times 0.95 = 95$
$\sigma = \sqrt{100 \times 0.95 \times 0.05} = \sqrt{4.75} = 2.18$

Como 90 está a más de 2σ debajo de la media, P(X ≥ 90) es muy alta, aproximadamente 0.99 o más.

(El cálculo exacto requiere suma de 11 términos o aproximación normal)

</details>

### Ejercicio 4
¿Por qué la distribución binomial no aplica si sacas 5 cartas de una baraja sin reemplazo y cuentas cuántas son rojas?

<details>
<summary>Ver solución</summary>

No aplica porque **la probabilidad cambia** con cada extracción:

- Primera carta: P(roja) = 26/52 = 0.5
- Segunda carta (si la primera fue roja): P(roja) = 25/51 ≈ 0.49
- Segunda carta (si la primera fue negra): P(roja) = 26/51 ≈ 0.51

Las probabilidades **no son constantes** → No cumple la condición de p constante.

**Alternativa:** Esta situación sigue una **distribución hipergeométrica**, no binomial.

(Sin embargo, si la baraja fuera muy grande, como millones de cartas, la diferencia sería despreciable y podría aproximarse con binomial)

</details>
