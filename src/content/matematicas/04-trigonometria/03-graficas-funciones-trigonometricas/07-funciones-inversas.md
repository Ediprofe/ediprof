# Funciones Trigonométricas Inversas

Las **funciones inversas** permiten encontrar el ángulo cuando conocemos el valor de una razón trigonométrica.

---

## 📖 ¿Por qué "inversas"?

Las funciones trigonométricas convierten **ángulos en números**:

$$
\sin 30° = 0.5
$$

Las funciones inversas convierten **números en ángulos**:

$$
\arcsin(0.5) = 30°
$$

---

## 📖 Las tres funciones inversas principales

### Arcseno (sin⁻¹)

$$
y = \arcsin x \quad \Leftrightarrow \quad x = \sin y
$$

| Propiedad | Valor |
|-----------|-------|
| Dominio | $[-1, 1]$ |
| Rango | $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ |

### Arccoseno (cos⁻¹)

$$
y = \arccos x \quad \Leftrightarrow \quad x = \cos y
$$

| Propiedad | Valor |
|-----------|-------|
| Dominio | $[-1, 1]$ |
| Rango | $[0, \pi]$ |

### Arctangente (tan⁻¹)

$$
y = \arctan x \quad \Leftrightarrow \quad x = \tan y
$$

| Propiedad | Valor |
|-----------|-------|
| Dominio | Todos los reales |
| Rango | $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ |

---

## 📖 Notación

Hay dos formas de escribir las funciones inversas:

| Notación 1 | Notación 2 |
|------------|------------|
| $\arcsin x$ | $\sin^{-1} x$ |
| $\arccos x$ | $\cos^{-1} x$ |
| $\arctan x$ | $\tan^{-1} x$ |

> **Nota:** $\sin^{-1} x \neq \frac{1}{\sin x}$. El superíndice -1 indica función inversa, no recíproco.

---

## 📖 Valores especiales

### Arcseno

| $x$ | $\arcsin x$ (rad) | $\arcsin x$ (grados) |
|-----|-------------------|----------------------|
| 0 | 0 | 0° |
| 0.5 | $\frac{\pi}{6}$ | 30° |
| $\frac{\sqrt{2}}{2}$ | $\frac{\pi}{4}$ | 45° |
| $\frac{\sqrt{3}}{2}$ | $\frac{\pi}{3}$ | 60° |
| 1 | $\frac{\pi}{2}$ | 90° |

### Arccoseno

| $x$ | $\arccos x$ (rad) | $\arccos x$ (grados) |
|-----|-------------------|----------------------|
| 1 | 0 | 0° |
| $\frac{\sqrt{3}}{2}$ | $\frac{\pi}{6}$ | 30° |
| $\frac{\sqrt{2}}{2}$ | $\frac{\pi}{4}$ | 45° |
| 0.5 | $\frac{\pi}{3}$ | 60° |
| 0 | $\frac{\pi}{2}$ | 90° |

### Arctangente

| $x$ | $\arctan x$ (rad) | $\arctan x$ (grados) |
|-----|-------------------|----------------------|
| 0 | 0 | 0° |
| $\frac{\sqrt{3}}{3}$ | $\frac{\pi}{6}$ | 30° |
| 1 | $\frac{\pi}{4}$ | 45° |
| $\sqrt{3}$ | $\frac{\pi}{3}$ | 60° |

---

## 📖 Propiedades importantes

### Composición

$$
\sin(\arcsin x) = x \quad \text{para } x \in [-1, 1]
$$

$$
\arcsin(\sin x) = x \quad \text{para } x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]
$$

(Similar para coseno y tangente en sus rangos respectivos)

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular valores

Calcula sin calculadora:

1. $\arcsin(1)$
2. $\arccos(0)$
3. $\arctan(1)$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\arcsin(1) = \frac{\pi}{2} = 90°$
2. $\arccos(0) = \frac{\pi}{2} = 90°$
3. $\arctan(1) = \frac{\pi}{4} = 45°$

</details>

---

### Ejercicio 2: Evaluar expresiones

Calcula:

1. $\sin(\arcsin(0.5))$
2. $\arccos(\cos(\frac{\pi}{4}))$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\sin(\arcsin(0.5)) = 0.5$
2. $\arccos(\cos(\frac{\pi}{4})) = \frac{\pi}{4}$

</details>

---

### Ejercicio 3: Dominio

¿Cuál de estos valores está definido?

1. $\arcsin(2)$
2. $\arccos(-0.5)$
3. $\arctan(100)$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **No definido** - 2 está fuera del dominio $[-1, 1]$
2. **Definido** - $-0.5 \in [-1, 1]$
3. **Definido** - $\arctan$ acepta cualquier número real

</details>

---

### Ejercicio 4: Encontrar ángulo

Si $\sin\theta = \frac{3}{5}$ y $\theta$ es agudo, encuentra $\theta$ usando arcseno.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\theta = \arcsin\left(\frac{3}{5}\right) = \arcsin(0.6) \approx 36.87°
$$

</details>

---
