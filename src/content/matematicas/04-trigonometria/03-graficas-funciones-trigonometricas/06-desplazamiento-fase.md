# Desplazamiento de Fase

El **desplazamiento de fase** (o desfase) mueve la gráfica horizontalmente. También estudiaremos el desplazamiento vertical.

---

## 📖 La función general

$$
y = A \sin(Bx - C) + D
$$

o

$$
y = A \sin\left(B\left(x - \frac{C}{B}\right)\right) + D
$$

Donde:
- $A$ = amplitud
- $B$ = afecta el período
- $C$ (o $\frac{C}{B}$) = desplazamiento de fase
- $D$ = desplazamiento vertical

---

## 📖 Desplazamiento de fase (horizontal)

> **Definición:** El desplazamiento de fase es cuánto se mueve la gráfica horizontalmente.

$$
\text{Fase} = \frac{C}{B}
$$

### Efecto

| Signo | Dirección |
|-------|-----------|
| $\frac{C}{B} > 0$ | Desplaza a la **derecha** |
| $\frac{C}{B} < 0$ | Desplaza a la **izquierda** |

### Ejemplo

$$
y = \sin\left(x - \frac{\pi}{4}\right)
$$

Desplazamiento de fase = $\frac{\pi}{4}$ a la derecha

---

## 📖 Desplazamiento vertical

> **Definición:** El desplazamiento vertical sube o baja toda la gráfica.

$$
\text{Desplazamiento vertical} = D
$$

### Efecto

| Valor | Dirección |
|-------|-----------|
| $D > 0$ | Sube la gráfica |
| $D < 0$ | Baja la gráfica |

### Nuevo rango

$$
\text{Rango} = [D - |A|, D + |A|]
$$

---

## 📖 Ejemplo completo

$$
y = 3\sin(2x - \pi) + 1
$$

### Análisis

| Parámetro | Valor | Significado |
|-----------|-------|-------------|
| $A$ | 3 | Amplitud = 3 |
| $B$ | 2 | Período = $\frac{2\pi}{2} = \pi$ |
| $C$ | $\pi$ | Fase = $\frac{\pi}{2}$ a la derecha |
| $D$ | 1 | Sube 1 unidad |

### Rango

$$
[1 - 3, 1 + 3] = [-2, 4]
$$

---

## 📖 Forma alternativa

A veces se escribe:

$$
y = A\sin(B(x - h)) + k
$$

Donde:
- $h$ = desplazamiento horizontal directo
- $k$ = desplazamiento vertical

Esta forma es más intuitiva.

---

## 📖 Puntos clave nuevo

Para $y = A\sin(B(x - h)) + k$, los puntos clave se desplazan:

| Punto original | Punto desplazado |
|----------------|------------------|
| $(0, 0)$ | $(h, k)$ |
| $(\frac{\pi}{2B}, A)$ | $(\frac{\pi}{2B} + h, A + k)$ |
| $(\frac{\pi}{B}, 0)$ | $(\frac{\pi}{B} + h, k)$ |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar desplazamiento de fase

¿Cuál es el desplazamiento de fase?

1. $y = \sin(x - \pi)$
2. $y = \cos(x + \frac{\pi}{2})$
3. $y = \sin(2x - \pi)$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Fase = $\pi$ a la derecha
2. Fase = $-\frac{\pi}{2}$ = $\frac{\pi}{2}$ a la izquierda
3. Fase = $\frac{\pi}{2}$ a la derecha (porque $\frac{\pi}{2} = \frac{C}{B} = \frac{\pi}{2}$)

</details>

---

### Ejercicio 2: Desplazamiento vertical

Para $y = 2\cos x + 3$, encuentra:

1. Amplitud
2. Desplazamiento vertical
3. Rango

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Amplitud = 2
2. Desplazamiento vertical = 3 hacia arriba
3. Rango = $[3-2, 3+2] = [1, 5]$

</details>

---

### Ejercicio 3: Análisis completo

Para $y = 4\sin\left(3x + \frac{\pi}{2}\right) - 2$, determina:

1. Amplitud
2. Período
3. Desplazamiento de fase
4. Desplazamiento vertical
5. Rango

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Amplitud = 4
2. Período = $\frac{2\pi}{3}$
3. Fase = $-\frac{\pi}{6}$ (a la izquierda)
4. Desplazamiento vertical = -2 (abajo)
5. Rango = $[-2-4, -2+4] = [-6, 2]$

</details>

---

### Ejercicio 4: Escribir función

Escribe una función coseno con:
- Amplitud 2
- Período $4\pi$
- Desplazamiento $\frac{\pi}{3}$ a la derecha
- Desplazamiento 5 arriba

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
y = 2\cos\left(\frac{1}{2}\left(x - \frac{\pi}{3}\right)\right) + 5
$$

o

$$
y = 2\cos\left(\frac{x}{2} - \frac{\pi}{6}\right) + 5
$$

</details>

---
