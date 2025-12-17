# Circunferencia y Círculo

Aunque a veces se usan como sinónimos, la **circunferencia** y el **círculo** son conceptos diferentes. En esta lección aprendemos la diferencia y los elementos básicos.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Circunferencia: puntos equidistantes del centro</strong>
  </div>

![Circunferencia básica](/images/geometria/circulos/circunferencia-basica.svg)

</div>

---

## 📖 Diferencia entre circunferencia y círculo

### Circunferencia

> **Definición:** La circunferencia es el conjunto de **todos los puntos** del plano que están a la **misma distancia** de un punto llamado centro.

La circunferencia es una **línea curva cerrada** (tiene longitud pero no área).

### Círculo

> **Definición:** El círculo es la **región del plano** limitada por una circunferencia.

El círculo es una **superficie** (tiene área).

### Analogía

- **Circunferencia** = el borde de una pizza
- **Círculo** = la pizza completa (incluyendo el interior)

---

## 📖 Elementos básicos

### Centro

El **centro** ($O$) es el punto del cual todos los puntos de la circunferencia están a igual distancia.

### Radio

El **radio** ($r$) es la distancia desde el centro hasta cualquier punto de la circunferencia. También es el segmento que une el centro con un punto de la circunferencia.

$$
r = \overline{OP}
$$

donde $P$ es cualquier punto de la circunferencia.

### Diámetro

El **diámetro** ($d$) es un segmento que pasa por el centro y tiene sus extremos en la circunferencia.

$$
d = 2r
$$

El diámetro es el **mayor segmento** que se puede trazar dentro de un círculo.

---

## 📖 Posición de un punto respecto a la circunferencia

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 700px;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Posiciones de un punto</strong>
  </div>

![Posiciones de un punto](/images/geometria/circulos/posiciones-punto.svg)

</div>

| Posición | Condición | Descripción |
|----------|-----------|-------------|
| Interior | distancia < $r$ | El punto está dentro |
| En la circunferencia | distancia = $r$ | El punto está en la curva |
| Exterior | distancia > $r$ | El punto está fuera |

### Ejemplo

Si el radio es $r = 5$ cm y la distancia de un punto $P$ al centro es 3 cm:

$$
3 < 5 \Rightarrow P \text{ está en el interior}
$$

---

## 📖 Longitud de la circunferencia

La longitud (o perímetro) de la circunferencia es:

$$
C = 2\pi r = \pi d
$$

Donde $\pi \approx 3.14159...$

### Ejemplo

Si $r = 7$ cm:

$$
C = 2\pi(7) = 14\pi \approx 43.98 \text{ cm}
$$

---

## 📖 Área del círculo

El área del círculo es:

$$
A = \pi r^2
$$

### Ejemplo

Si $r = 5$ cm:

$$
A = \pi(5)^2 = 25\pi \approx 78.54 \text{ cm}^2
$$

---

## 📖 Relación entre fórmulas

| Elemento | Fórmula |
|----------|---------|
| Radio | $r$ |
| Diámetro | $d = 2r$ |
| Longitud de circunferencia | $C = 2\pi r$ |
| Área del círculo | $A = \pi r^2$ |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar

Indica si cada afirmación se refiere a la circunferencia o al círculo:

1. Tiene área
2. Es una línea curva cerrada
3. Tiene longitud pero no área
4. Incluye todos los puntos interiores

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Círculo**
2. **Circunferencia**
3. **Circunferencia**
4. **Círculo**

</details>

---

### Ejercicio 2: Calcular diámetro

El radio de una circunferencia es 8 cm. ¿Cuánto mide el diámetro?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
d = 2r = 2(8) = 16 \text{ cm}
$$

</details>

---

### Ejercicio 3: Longitud de circunferencia

Calcula la longitud de circunferencias con estos radios (usa $\pi \approx 3.14$):

1. $r = 5$ cm
2. $r = 10$ cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $C = 2\pi(5) = 10\pi \approx 31.4$ cm
2. $C = 2\pi(10) = 20\pi \approx 62.8$ cm

</details>

---

### Ejercicio 4: Área del círculo

Calcula el área de círculos con estos radios:

1. $r = 3$ cm
2. $r = 6$ cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \pi(3)^2 = 9\pi \approx 28.27$ cm²
2. $A = \pi(6)^2 = 36\pi \approx 113.1$ cm²

</details>

---

### Ejercicio 5: Posición de puntos

El centro de una circunferencia está en $O$ y el radio es 4 cm. ¿Dónde está cada punto?

1. $P$ a 3 cm del centro
2. $Q$ a 4 cm del centro
3. $R$ a 5 cm del centro

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $P$ está en el **interior** (3 < 4)
2. $Q$ está en la **circunferencia** (4 = 4)
3. $R$ está en el **exterior** (5 > 4)

</details>

---
