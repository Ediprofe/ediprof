---
title: "Sustitución Trigonométrica"
---

# Sustitución Trigonométrica

La sustitución trigonométrica transforma integrales con raíces cuadráticas en integrales trigonométricas más manejables.

---

## 🎯 ¿Qué vas a aprender?

- Cuándo usar sustitución trigonométrica
- Las tres sustituciones principales
- Cómo manejar los triángulos de referencia
- Volver a la variable original

---

## 📖 Las tres sustituciones

| Forma en la integral | Sustitución | Identidad usada |
|---------------------|-------------|-----------------|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $1 - \sin^2\theta = \cos^2\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $1 + \tan^2\theta = \sec^2\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $\sec^2\theta - 1 = \tan^2\theta$ |

---

## 📖 Método general

1. **Identificar** la forma de la raíz
2. **Sustituir** $x$ según la tabla
3. **Calcular** $dx$ y simplificar la raíz
4. **Integrar** en $\theta$
5. **Dibujar** el triángulo de referencia
6. **Convertir** el resultado a $x$

---

## ⚙️ Ejemplo 1: Forma a² - x²

Calcula:

$$
\int \frac{1}{\sqrt{4 - x^2}}\,dx
$$

**Sustitución:** $x = 2\sin\theta$, $dx = 2\cos\theta\,d\theta$

$$
\sqrt{4 - x^2} = \sqrt{4 - 4\sin^2\theta} = 2\cos\theta
$$

$$
= \int \frac{2\cos\theta}{2\cos\theta}\,d\theta = \int d\theta = \theta + C
$$

**Volver a $x$:** $\sin\theta = \frac{x}{2}$ → $\theta = \arcsin\frac{x}{2}$

$$
= \arcsin\frac{x}{2} + C
$$

---

## ⚙️ Ejemplo 2: Área de semicírculo

Calcula:

$$
\int \sqrt{9 - x^2}\,dx
$$

**Solución:** $x = 3\sin\theta$, $dx = 3\cos\theta\,d\theta$

$\sqrt{9 - x^2} = 3\cos\theta$

$$
= \int 3\cos\theta \cdot 3\cos\theta\,d\theta = 9\int \cos^2\theta\,d\theta
$$

$$
= 9 \cdot \frac{\theta + \sin\theta\cos\theta}{2} + C
$$

$$
= \frac{9}{2}\theta + \frac{9}{2}\sin\theta\cos\theta + C
$$

Triángulo: $\sin\theta = \frac{x}{3}$, $\cos\theta = \frac{\sqrt{9-x^2}}{3}$

$$
= \frac{9}{2}\arcsin\frac{x}{3} + \frac{x\sqrt{9-x^2}}{2} + C
$$

---

## ⚙️ Ejemplo 3: Forma a² + x²

Calcula:

$$
\int \frac{1}{\sqrt{x^2 + 4}}\,dx
$$

**Solución:** $x = 2\tan\theta$, $dx = 2\sec^2\theta\,d\theta$

$\sqrt{x^2 + 4} = \sqrt{4\tan^2\theta + 4} = 2\sec\theta$

$$
= \int \frac{2\sec^2\theta}{2\sec\theta}\,d\theta = \int \sec\theta\,d\theta
$$

$$
= \ln|\sec\theta + \tan\theta| + C
$$

Triángulo: $\tan\theta = \frac{x}{2}$, $\sec\theta = \frac{\sqrt{x^2+4}}{2}$

$$
= \ln\left|\frac{\sqrt{x^2+4}}{2} + \frac{x}{2}\right| + C = \ln\left|x + \sqrt{x^2+4}\right| + C'
$$

---

## ⚙️ Ejemplo 4: Forma x² - a²

Calcula:

$$
\int \frac{\sqrt{x^2 - 9}}{x}\,dx
$$

**Solución:** $x = 3\sec\theta$, $dx = 3\sec\theta\tan\theta\,d\theta$

$\sqrt{x^2 - 9} = 3\tan\theta$

$$
= \int \frac{3\tan\theta}{3\sec\theta} \cdot 3\sec\theta\tan\theta\,d\theta = 3\int \tan^2\theta\,d\theta
$$

$$
= 3(\tan\theta - \theta) + C
$$

Triángulo: $\sec\theta = \frac{x}{3}$, $\tan\theta = \frac{\sqrt{x^2-9}}{3}$, $\theta = \text{arcsec}\frac{x}{3}$

$$
= \sqrt{x^2-9} - 3\text{arcsec}\frac{x}{3} + C
$$

---

## 📖 Triángulos de referencia

Para $x = a\sin\theta$ (cateto opuesto = $x$, hipotenusa = $a$):
- $\cos\theta = \frac{\sqrt{a^2-x^2}}{a}$

Para $x = a\tan\theta$ (cateto opuesto = $x$, cateto adyacente = $a$):
- $\sec\theta = \frac{\sqrt{a^2+x^2}}{a}$

Para $x = a\sec\theta$ (hipotenusa = $x$, cateto adyacente = $a$):
- $\tan\theta = \frac{\sqrt{x^2-a^2}}{a}$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

$$
\int \frac{x^2}{\sqrt{1-x^2}}\,dx
$$

<details>
<summary>Ver solución</summary>

$x = \sin\theta$, $dx = \cos\theta\,d\theta$

$$
= \int \frac{\sin^2\theta}{\cos\theta}\cos\theta\,d\theta = \int \sin^2\theta\,d\theta
$$

$$
= \frac{\theta - \sin\theta\cos\theta}{2} + C
$$

$$
= \frac{\arcsin x - x\sqrt{1-x^2}}{2} + C
$$

</details>

---

**Ejercicio 2:** Calcula:

$$
\int \frac{1}{x^2\sqrt{x^2+1}}\,dx
$$

<details>
<summary>Ver solución</summary>

$x = \tan\theta$, $dx = \sec^2\theta\,d\theta$

$$
= \int \frac{\sec^2\theta}{\tan^2\theta \cdot \sec\theta}\,d\theta = \int \frac{\sec\theta}{\tan^2\theta}\,d\theta
$$

$$
= \int \frac{\cos\theta}{\sin^2\theta}\,d\theta = -\csc\theta + C
$$

$$
= -\frac{\sqrt{x^2+1}}{x} + C
$$

</details>
