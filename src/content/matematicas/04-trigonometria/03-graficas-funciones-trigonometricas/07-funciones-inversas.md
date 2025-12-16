# Funciones Trigonométricas Inversas

Las funciones trigonométricas convierten ángulos en números. ¿Y si quieres hacer lo contrario? Aquí entran las **funciones inversas**: te dan el ángulo cuando conoces el valor.

---

## 🎯 En esta lección aprenderás

- Qué son y para qué sirven las funciones inversas
- Las gráficas de arcsin, arccos y arctan
- Por qué tienen dominios y rangos restringidos
- Cómo calcular valores exactos

---

## 📋 Cheat Sheet

| Función | Símbolo | Dominio | Rango |
|---------|---------|---------|-------|
| Arcseno | $\arcsin x$ o $\sin^{-1} x$ | $[-1, 1]$ | $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ |
| Arccoseno | $\arccos x$ o $\cos^{-1} x$ | $[-1, 1]$ | $[0, \pi]$ |
| Arctangente | $\arctan x$ o $\tan^{-1} x$ | $\mathbb{R}$ | $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ |

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Las tres funciones inversas principales</strong>
  </div>

![Las tres funciones inversas](/images/funciones/trigonometria/inversas-todas.svg)

</div>

---

## 📖 ¿Por qué "inversas"?

### El problema

Las funciones trigonométricas van de **ángulos → números**:

$$
\sin 30° = 0.5
$$

Pero a veces necesitas ir al revés: **números → ángulos**:

> "Si el seno de un ángulo es 0.5, ¿cuánto es el ángulo?"

### La solución

$$
\arcsin(0.5) = 30° = \frac{\pi}{6}
$$

> 💡 **Traducción:** La función inversa "deshace" lo que hizo la función original.

---

## 📖 El arcseno (sin⁻¹)

### Definición

$$
y = \arcsin x \quad \Leftrightarrow \quad x = \sin y
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = arcsin(x)</strong>
  </div>

![Gráfica del arcoseno](/images/funciones/trigonometria/arcsin.svg)

</div>

### Características

| Propiedad | Valor |
|-----------|-------|
| Dominio | $[-1, 1]$ |
| Rango | $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ (cuadrantes I y IV) |
| Pasa por | $(0, 0)$ |
| Función creciente | Sí |

### Valores especiales

| $x$ | $\arcsin x$ (rad) | $\arcsin x$ (grados) |
|-----|-------------------|----------------------|
| 0 | 0 | 0° |
| $\frac{1}{2}$ | $\frac{\pi}{6}$ | 30° |
| $\frac{\sqrt{2}}{2}$ | $\frac{\pi}{4}$ | 45° |
| $\frac{\sqrt{3}}{2}$ | $\frac{\pi}{3}$ | 60° |
| 1 | $\frac{\pi}{2}$ | 90° |

---

## 📖 El arccoseno (cos⁻¹)

### Definición

$$
y = \arccos x \quad \Leftrightarrow \quad x = \cos y
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = arccos(x)</strong>
  </div>

![Gráfica del arcocoseno](/images/funciones/trigonometria/arccos.svg)

</div>

### Características

| Propiedad | Valor |
|-----------|-------|
| Dominio | $[-1, 1]$ |
| Rango | $[0, \pi]$ (cuadrantes I y II) |
| Pasa por | $(1, 0)$ y $(0, \frac{\pi}{2})$ |
| Función decreciente | Sí |

### Valores especiales

| $x$ | $\arccos x$ (rad) | $\arccos x$ (grados) |
|-----|-------------------|----------------------|
| 1 | 0 | 0° |
| $\frac{\sqrt{3}}{2}$ | $\frac{\pi}{6}$ | 30° |
| $\frac{\sqrt{2}}{2}$ | $\frac{\pi}{4}$ | 45° |
| $\frac{1}{2}$ | $\frac{\pi}{3}$ | 60° |
| 0 | $\frac{\pi}{2}$ | 90° |

---

## 📖 La arctangente (tan⁻¹)

### Definición

$$
y = \arctan x \quad \Leftrightarrow \quad x = \tan y
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = arctan(x)</strong>
  </div>

![Gráfica de la arcotangente](/images/funciones/trigonometria/arctan.svg)

</div>

### Características

| Propiedad | Valor |
|-----------|-------|
| Dominio | $\mathbb{R}$ (todos los reales) |
| Rango | $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ (sin incluir extremos) |
| Pasa por | $(0, 0)$ |
| Función creciente | Sí |
| Asíntotas horizontales | $y = \pm\frac{\pi}{2}$ |

### Valores especiales

| $x$ | $\arctan x$ (rad) | $\arctan x$ (grados) |
|-----|-------------------|----------------------|
| 0 | 0 | 0° |
| $\frac{\sqrt{3}}{3}$ | $\frac{\pi}{6}$ | 30° |
| 1 | $\frac{\pi}{4}$ | 45° |
| $\sqrt{3}$ | $\frac{\pi}{3}$ | 60° |

---

## 📖 Notación

Hay dos formas de escribir las funciones inversas:

| Notación "arc" | Notación exponente |
|----------------|-------------------|
| $\arcsin x$ | $\sin^{-1} x$ |
| $\arccos x$ | $\cos^{-1} x$ |
| $\arctan x$ | $\tan^{-1} x$ |

> ⚠️ **¡Cuidado!** $\sin^{-1} x \neq \frac{1}{\sin x}$. El -1 indica función **inversa**, no recíproco.

---

## 📖 Propiedades de composición

### Cuando se "cancelan"

$$
\sin(\arcsin x) = x \quad \text{para } x \in [-1, 1]
$$

$$
\arcsin(\sin x) = x \quad \text{para } x \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]
$$

> 💡 La segunda ecuación solo funciona si $x$ está en el rango del arcseno.

---

## 🧠 ¿Por qué restricciones de rango?

Las funciones trigonométricas **no son biyectivas** (muchos ángulos dan el mismo valor).

Por ejemplo: $\sin 30° = \sin 150° = 0.5$

Para que exista una inversa, debemos **restringir** el dominio original:

| Función | Restricción para inversa |
|---------|-------------------------|
| $\sin x$ | Solo usamos $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ |
| $\cos x$ | Solo usamos $[0, \pi]$ |
| $\tan x$ | Solo usamos $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Calcular valores

Calcula sin calculadora:

1. $\arcsin(1)$
2. $\arccos(0)$
3. $\arctan(1)$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\arcsin(1) = \frac{\pi}{2} = 90°$ (el seno vale 1 en 90°)
2. $\arccos(0) = \frac{\pi}{2} = 90°$ (el coseno vale 0 en 90°)
3. $\arctan(1) = \frac{\pi}{4} = 45°$ (la tangente vale 1 en 45°)

</details>

---

### Ejercicio 2: Evaluar expresiones

Calcula:

1. $\sin(\arcsin(0.5))$
2. $\arccos(\cos(\frac{\pi}{4}))$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\sin(\arcsin(0.5)) = 0.5$ (se "cancelan")
2. $\arccos(\cos(\frac{\pi}{4})) = \frac{\pi}{4}$ (porque $\frac{\pi}{4}$ está en el rango $[0, \pi]$)

</details>

---

### Ejercicio 3: Dominio

¿Cuál de estos valores está definido?

1. $\arcsin(2)$
2. $\arccos(-0.5)$
3. $\arctan(100)$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **No definido** — 2 está fuera del dominio $[-1, 1]$
2. **Definido** — $-0.5 \in [-1, 1]$, resultado: $\frac{2\pi}{3} = 120°$
3. **Definido** — $\arctan$ acepta cualquier número real, resultado: muy cerca de $\frac{\pi}{2}$

</details>

---

### Ejercicio 4: Encontrar ángulo

Si $\sin\theta = \frac{3}{5}$ y $\theta$ es un ángulo agudo, encuentra $\theta$ usando arcseno.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\theta = \arcsin\left(\frac{3}{5}\right) = \arcsin(0.6) \approx 36.87° \approx 0.6435 \text{ rad}
$$

Como el ángulo es agudo (está en el primer cuadrante), el arcseno nos da directamente la respuesta.

</details>

---
