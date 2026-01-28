---
title: "Área del Círculo"
---

# Área del Círculo

El área del círculo representa la superficie encerrada por la circunferencia. También estudiaremos las áreas de sectores y segmentos circulares.

---

## 📖 Área del círculo

> **Fórmula:** El área de un círculo con radio $r$ es:

$$
A = \pi r^2
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Área: A = πr²</strong>
  </div>

![Área del círculo](/images/geometria/circulos/formula-area.svg)

</div>

### ¿Por qué $\pi r^2$?

El círculo puede dividirse en muchos sectores pequeños que, al reorganizarse, forman aproximadamente un rectángulo de:
- Largo = $\pi r$ (mitad de la circunferencia)
- Ancho = $r$
- Área = $\pi r \times r = \pi r^2$

---

## 📖 Fórmulas equivalentes

$$
A = \pi r^2 = \frac{\pi d^2}{4}
$$

### Con el diámetro

Si conocemos el diámetro:

$$
A = \pi \left(\frac{d}{2}\right)^2 = \frac{\pi d^2}{4}
$$

---

## 📖 Ejemplos

### Ejemplo 1

Círculo de radio 5 cm:

$$
A = \pi(5)^2 = 25\pi \approx 78.54 \text{ cm}^2
$$

### Ejemplo 2

Círculo de diámetro 10 cm:

$$
r = 5 \text{ cm}
$$

$$
A = \pi(5)^2 = 25\pi \approx 78.54 \text{ cm}^2
$$

---

## 📖 Área del sector circular

Un **sector circular** es la región comprendida entre dos radios y un arco (como una rebanada de pizza).

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Área del Sector</strong>
  </div>

![Área del sector circular](/images/geometria/circulos/formula-area-sector.svg)

</div>

### Fórmula (ángulo en grados)

$$
A_{sector} = \frac{\theta}{360°} \times \pi r^2
$$

### Fórmula (ángulo en radianes)

$$
A_{sector} = \frac{1}{2} r^2 \theta
$$

### Ejemplo

Sector con radio 6 cm y ángulo de 60°:

$$
A = \frac{60°}{360°} \times \pi(6)^2 = \frac{1}{6} \times 36\pi = 6\pi \approx 18.85 \text{ cm}^2
$$

---

## 📖 Área del segmento circular

Un **segmento circular** es la región entre una cuerda y su arco.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Área del Segmento</strong>
  </div>

![Área del segmento circular](/images/geometria/circulos/formula-area-segmento.svg)

</div>

$$
A_{segmento} = A_{sector} - A_{triángulo}
$$

### Fórmula para el triángulo

El triángulo formado por los dos radios tiene:

$$
A_{triángulo} = \frac{1}{2} r^2 \sin(\theta)
$$

### Fórmula completa del segmento

$$
A_{segmento} = \frac{r^2}{2}(\theta - \sin\theta)
$$

(con $\theta$ en radianes)

---

## 📖 Área de la corona circular

Una **corona circular** es la región entre dos círculos concéntricos.

$$
A_{corona} = \pi R^2 - \pi r^2 = \pi(R^2 - r^2)
$$

Donde:
- $R$ = radio exterior
- $r$ = radio interior

### Ejemplo

Corona con $R = 10$ cm y $r = 6$ cm:

$$
A = \pi(10^2 - 6^2) = \pi(100 - 36) = 64\pi \approx 201.1 \text{ cm}^2
$$

---

## 📖 Encontrar el radio conociendo el área

$$
r = \sqrt{\frac{A}{\pi}}
$$

### Ejemplo

Si $A = 314$ cm² (usando $\pi \approx 3.14$):

$$
r = \sqrt{\frac{314}{3.14}} = \sqrt{100} = 10 \text{ cm}
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Área del círculo

Calcula el área de círculos con:

1. Radio = 4 cm
2. Radio = 7 cm
3. Diámetro = 12 cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \pi(4)^2 = 16\pi \approx 50.27$ cm²
2. $A = \pi(7)^2 = 49\pi \approx 153.94$ cm²
3. $r = 6$, $A = \pi(6)^2 = 36\pi \approx 113.1$ cm²

</details>

---

### Ejercicio 2: Área del sector

Calcula el área del sector:

1. Radio = 10 cm, ángulo = 90°
2. Radio = 6 cm, ángulo = 120°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = \frac{90°}{360°} \times \pi(10)^2 = \frac{1}{4} \times 100\pi = 25\pi \approx 78.54$ cm²
2. $A = \frac{120°}{360°} \times \pi(6)^2 = \frac{1}{3} \times 36\pi = 12\pi \approx 37.7$ cm²

</details>

---

### Ejercicio 3: Corona circular

Calcula el área de una corona con radio exterior 8 cm y radio interior 5 cm.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A = \pi(8^2 - 5^2) = \pi(64 - 25) = 39\pi \approx 122.5 \text{ cm}^2
$$

</details>

---

### Ejercicio 4: Encontrar el radio

El área de un círculo es 154 cm². ¿Cuál es el radio? (Usa $\pi = \frac{22}{7}$)

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
r^2 = \frac{A}{\pi} = \frac{154}{\frac{22}{7}} = 154 \times \frac{7}{22} = 49
$$

$$
r = 7 \text{ cm}
$$

</details>

---

### Ejercicio 5: Problema combinado

Un círculo tiene área 100π cm². Calcula:

1. El radio
2. El diámetro
3. La longitud de la circunferencia

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $r^2 = 100 \Rightarrow r = 10$ cm
2. $d = 2(10) = 20$ cm
3. $C = 2\pi(10) = 20\pi \approx 62.83$ cm

</details>

---
