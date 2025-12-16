# Desplazamiento de Fase

Ya dominaste cómo estirar y comprimir las ondas. Ahora aprenderás a **moverlas**: hacia los lados y hacia arriba o abajo. Es como ajustar la posición de un slider en la pantalla.

---

## 🎯 En esta lección aprenderás

- Cómo mover la onda horizontalmente (desplazamiento de fase)
- Cómo mover la onda verticalmente (desplazamiento vertical)
- La fórmula general completa con los 4 parámetros
- A identificar todos los parámetros en cualquier función

---

## 📋 Cheat Sheet

Para la función general:

$$
y = A \sin(B(x - C)) + D \quad \text{o} \quad y = A \sin(Bx - C) + D
$$

| Parámetro | Nombre | Efecto |
|-----------|--------|--------|
| A | Amplitud | Estiramiento vertical |
| B | Frecuencia | Compresión horizontal |
| C | Fase | Desplazamiento horizontal |
| D | Desplazamiento vertical | Subir/bajar toda la onda |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Desplazamiento de fase (horizontal)</strong>
  </div>

![Desplazamiento de fase horizontal](/images/funciones/trigonometria/fase-horizontal.svg)

</div>

---

## 📖 Desplazamiento de fase (horizontal)

### La regla de oro

$$
y = \sin(x - C) \quad \Rightarrow \quad \text{desplaza } C \text{ unidades a la DERECHA}
$$

$$
y = \sin(x + C) \quad \Rightarrow \quad \text{desplaza } C \text{ unidades a la IZQUIERDA}
$$

> ⚠️ **¡Contraintuitivo!** Restar mueve a la derecha, sumar mueve a la izquierda.

### Forma general con B

Cuando hay un coeficiente $B$:

$$
y = \sin(Bx - C) = \sin\left(B\left(x - \frac{C}{B}\right)\right)
$$

El desplazamiento de fase es:

$$
\text{Fase} = \frac{C}{B}
$$

### Ejemplo

$$
y = \sin(2x - \pi)
$$

- $B = 2$
- $C = \pi$
- Fase $= \frac{\pi}{2}$ a la **derecha**

---

## 📖 Desplazamiento vertical

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Desplazamiento vertical (D)</strong>
  </div>

![Desplazamiento vertical](/images/funciones/trigonometria/desplazamiento-vertical.svg)

</div>

### La fórmula

$$
y = \sin x + D
$$

| Valor de D | Efecto |
|------------|--------|
| $D > 0$ | Sube toda la onda |
| $D < 0$ | Baja toda la onda |

### Nuevo rango

$$
\text{Rango} = [D - |A|, D + |A|]
$$

---

## 📖 Ejemplo completo: los 4 parámetros

Analicemos $y = 3\sin(2x - \pi) + 1$:

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">y = 3sin(2x - π) + 1: Análisis completo</strong>
  </div>

![Ejemplo completo: y = 3sin(2x - π) + 1](/images/funciones/trigonometria/ejemplo-4-parametros.svg)

</div>

### Análisis paso a paso

| Parámetro | Valor | Significado |
|-----------|-------|-------------|
| $A$ | 3 | Amplitud = 3 |
| $B$ | 2 | Período = $\frac{2\pi}{2} = \pi$ |
| $C$ | $\pi$ | Fase = $\frac{\pi}{2}$ a la derecha |
| $D$ | 1 | Sube 1 unidad |

### Rango

$$
\text{Rango} = [D - |A|, D + |A|] = [1 - 3, 1 + 3] = [-2, 4]
$$

---

## 📖 Forma alternativa (más intuitiva)

A veces se escribe:

$$
y = A\sin(B(x - h)) + k
$$

Donde:
- $h$ = desplazamiento horizontal **directo**
- $k$ = desplazamiento vertical

> 💡 Esta forma es más fácil de leer: $h$ te dice directamente cuánto se desplaza.

---

## 📖 Puntos clave desplazados

Para $y = A\sin(B(x - h)) + k$, los puntos clave se mueven:

| Punto original de sin(x) | Nuevo punto |
|--------------------------|-------------|
| $(0, 0)$ | $(h, k)$ |
| $(\frac{\pi}{2B}, A)$ | $(\frac{\pi}{2B} + h, A + k)$ |
| $(\frac{\pi}{B}, 0)$ | $(\frac{\pi}{B} + h, k)$ |
| $(\frac{3\pi}{2B}, -A)$ | $(\frac{3\pi}{2B} + h, -A + k)$ |
| $(\frac{2\pi}{B}, 0)$ | $(\frac{2\pi}{B} + h, k)$ |

---

## 🧠 Resumen de efectos

| Transformación | Fórmula | Efecto |
|----------------|---------|--------|
| Estiramiento vertical | $A \cdot f(x)$ | Multiplica altura por $A$ |
| Compresión horizontal | $f(Bx)$ | Divide período por $B$ |
| Desplazamiento derecha | $f(x - C)$ | Mueve $C$ a la derecha |
| Desplazamiento arriba | $f(x) + D$ | Sube $D$ unidades |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar desplazamiento de fase

¿Cuál es el desplazamiento de fase?

1. $y = \sin(x - \pi)$
2. $y = \cos(x + \frac{\pi}{2})$
3. $y = \sin(2x - \pi)$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. Fase = $\pi$ a la **derecha** (restar = derecha)
2. Fase = $\frac{\pi}{2}$ a la **izquierda** (sumar = izquierda)
3. Fase = $\frac{\pi}{2}$ a la **derecha** (porque $\frac{C}{B} = \frac{\pi}{2}$)

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
3. Fase = $\frac{\pi/2}{3} = \frac{\pi}{6}$ a la **izquierda** (signo positivo)
4. Desplazamiento vertical = 2 hacia **abajo**
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

Necesitamos:
- $A = 2$
- Período = $4\pi$ → $B = \frac{2\pi}{4\pi} = \frac{1}{2}$
- Fase = $\frac{\pi}{3}$ derecha
- $D = 5$

$$
y = 2\cos\left(\frac{1}{2}\left(x - \frac{\pi}{3}\right)\right) + 5
$$

O expandiendo:

$$
y = 2\cos\left(\frac{x}{2} - \frac{\pi}{6}\right) + 5
$$

</details>

---
