# Identidades Pitagóricas

Las **identidades pitagóricas** son las más importantes en trigonometría. Se derivan del teorema de Pitágoras aplicado al círculo unitario.

---

## 📖 La identidad fundamental

$$
\sin^2\theta + \cos^2\theta = 1
$$

### Origen

En el círculo unitario, el punto $(\cos\theta, \sin\theta)$ está sobre la circunferencia $x^2 + y^2 = 1$.

Sustituyendo:

$$
\cos^2\theta + \sin^2\theta = 1
$$

---

## 📖 Segunda identidad pitagórica

$$
1 + \tan^2\theta = \sec^2\theta
$$

### Derivación

Partiendo de $\sin^2\theta + \cos^2\theta = 1$, dividimos entre $\cos^2\theta$:

$$
\frac{\sin^2\theta}{\cos^2\theta} + \frac{\cos^2\theta}{\cos^2\theta} = \frac{1}{\cos^2\theta}
$$

$$
\tan^2\theta + 1 = \sec^2\theta
$$

---

## 📖 Tercera identidad pitagórica

$$
1 + \cot^2\theta = \csc^2\theta
$$

### Derivación

Partiendo de $\sin^2\theta + \cos^2\theta = 1$, dividimos entre $\sin^2\theta$:

$$
\frac{\sin^2\theta}{\sin^2\theta} + \frac{\cos^2\theta}{\sin^2\theta} = \frac{1}{\sin^2\theta}
$$

$$
1 + \cot^2\theta = \csc^2\theta
$$

---

## 📖 Resumen de las tres identidades

| Identidad | Forma alternativa |
|-----------|-------------------|
| $\sin^2\theta + \cos^2\theta = 1$ | $\sin^2 = 1 - \cos^2$, $\cos^2 = 1 - \sin^2$ |
| $\tan^2\theta + 1 = \sec^2\theta$ | $\tan^2 = \sec^2 - 1$, $\sec^2 - \tan^2 = 1$ |
| $1 + \cot^2\theta = \csc^2\theta$ | $\cot^2 = \csc^2 - 1$, $\csc^2 - \cot^2 = 1$ |

---

## 📖 Formas factorizadas

### Diferencia de cuadrados

$$
1 - \sin^2\theta = \cos^2\theta = (1 + \sin\theta)(1 - \sin\theta)
$$

$$
1 - \cos^2\theta = \sin^2\theta = (1 + \cos\theta)(1 - \cos\theta)
$$

---

## 📖 Aplicaciones

### Encontrar una función conociendo otra

Si $\sin\theta = \frac{3}{5}$ y $\theta$ está en el primer cuadrante:

$$
\cos^2\theta = 1 - \sin^2\theta = 1 - \frac{9}{25} = \frac{16}{25}
$$

$$
\cos\theta = \frac{4}{5}
$$

(Positivo porque está en el primer cuadrante)

### Simplificar expresiones

$$
\frac{1 - \sin^2\theta}{\cos\theta} = \frac{\cos^2\theta}{\cos\theta} = \cos\theta
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Encontrar valores

Si $\cos\theta = \frac{5}{13}$ y $\theta$ está en el primer cuadrante, encuentra:

1. $\sin\theta$
2. $\tan\theta$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\sin^2\theta = 1 - \frac{25}{169} = \frac{144}{169}$, $\sin\theta = \frac{12}{13}$

2. $\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{12/13}{5/13} = \frac{12}{5}$

</details>

---

### Ejercicio 2: Simplificar

Simplifica:

1. $\sec^2\theta - 1$
2. $\csc^2\theta - \cot^2\theta$
3. $\frac{1 - \cos^2\theta}{\sin\theta}$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\sec^2\theta - 1 = \tan^2\theta$
2. $\csc^2\theta - \cot^2\theta = 1$
3. $\frac{\sin^2\theta}{\sin\theta} = \sin\theta$

</details>

---

### Ejercicio 3: Tercer cuadrante

Si $\tan\theta = \frac{4}{3}$ y $\theta$ está en el tercer cuadrante, encuentra $\sin\theta$ y $\cos\theta$.

<details>
<summary><strong>Ver respuesta</strong></summary>

Usando $1 + \tan^2\theta = \sec^2\theta$:

$$
\sec^2\theta = 1 + \frac{16}{9} = \frac{25}{9}
$$

$$
\sec\theta = -\frac{5}{3}
$$

(Negativo porque $\cos$ es negativo en QIII)

$$
\cos\theta = -\frac{3}{5}
$$

$$
\sin\theta = \tan\theta \cdot \cos\theta = \frac{4}{3} \cdot \left(-\frac{3}{5}\right) = -\frac{4}{5}
$$

</details>

---

### Ejercicio 4: Demostrar

Demuestra que $(1 + \tan^2\theta)(1 - \sin^2\theta) = 1$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
(1 + \tan^2\theta)(1 - \sin^2\theta) = \sec^2\theta \cdot \cos^2\theta
$$

$$
= \frac{1}{\cos^2\theta} \cdot \cos^2\theta = 1
$$

</details>

---
