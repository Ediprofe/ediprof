# Poliedros Regulares

Los **poliedros regulares** (también llamados **sólidos platónicos**) son poliedros donde todas las caras son polígonos regulares iguales y en cada vértice se unen el mismo número de caras.

---

## 📖 Definición

> **Definición:** Un poliedro regular es aquel en el que:
> 1. Todas las **caras** son polígonos regulares idénticos
> 2. En cada **vértice** se unen el mismo número de caras

---

## 📖 Solo existen 5 poliedros regulares

Por razones geométricas, solo pueden existir **exactamente 5** poliedros regulares:

| Nombre | Caras | Tipo de cara | Vértices | Aristas |
|--------|-------|--------------|----------|---------|
| Tetraedro | 4 | Triángulo | 4 | 6 |
| Hexaedro (Cubo) | 6 | Cuadrado | 8 | 12 |
| Octaedro | 8 | Triángulo | 6 | 12 |
| Dodecaedro | 12 | Pentágono | 20 | 30 |
| Icosaedro | 20 | Triángulo | 12 | 30 |

---

## 📖 El Tetraedro

- **Caras:** 4 triángulos equiláteros
- **Vértices:** 4
- **Aristas:** 6
- **Caras por vértice:** 3

### Fórmulas (arista $a$)

$$
A = a^2\sqrt{3}
$$

$$
V = \frac{a^3\sqrt{2}}{12}
$$

---

## 📖 El Cubo (Hexaedro)

- **Caras:** 6 cuadrados
- **Vértices:** 8
- **Aristas:** 12
- **Caras por vértice:** 3

### Fórmulas (arista $a$)

$$
A = 6a^2
$$

$$
V = a^3
$$

---

## 📖 El Octaedro

- **Caras:** 8 triángulos equiláteros
- **Vértices:** 6
- **Aristas:** 12
- **Caras por vértice:** 4

### Fórmulas (arista $a$)

$$
A = 2a^2\sqrt{3}
$$

$$
V = \frac{a^3\sqrt{2}}{3}
$$

---

## 📖 El Dodecaedro

- **Caras:** 12 pentágonos regulares
- **Vértices:** 20
- **Aristas:** 30
- **Caras por vértice:** 3

Es el poliedro regular más cercano a una esfera.

---

## 📖 El Icosaedro

- **Caras:** 20 triángulos equiláteros
- **Vértices:** 12
- **Aristas:** 30
- **Caras por vértice:** 5

Es el poliedro regular con más caras.

---

## 📖 Verificación con fórmula de Euler

Para todos los poliedros regulares:

$$
V - A + C = 2
$$

| Poliedro | V | A | C | V - A + C |
|----------|---|---|---|-----------|
| Tetraedro | 4 | 6 | 4 | 2 ✓ |
| Cubo | 8 | 12 | 6 | 2 ✓ |
| Octaedro | 6 | 12 | 8 | 2 ✓ |
| Dodecaedro | 20 | 30 | 12 | 2 ✓ |
| Icosaedro | 12 | 30 | 20 | 2 ✓ |

---

## 📖 Poliedros duales

Cada poliedro regular tiene un **dual**:

| Poliedro | Dual |
|----------|------|
| Tetraedro | Tetraedro (auto-dual) |
| Cubo | Octaedro |
| Octaedro | Cubo |
| Dodecaedro | Icosaedro |
| Icosaedro | Dodecaedro |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar

¿Qué poliedro regular tiene...?

1. 4 caras triangulares
2. 6 caras cuadradas
3. 20 caras triangulares
4. 12 caras pentagonales

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Tetraedro**
2. **Cubo**
3. **Icosaedro**
4. **Dodecaedro**

</details>

---

### Ejercicio 2: Fórmula de Euler

Verifica la fórmula de Euler para el dodecaedro (20 vértices, 30 aristas, 12 caras).

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
V - A + C = 20 - 30 + 12 = 2 \quad ✓
$$

</details>

---

### Ejercicio 3: Cubo

Un cubo tiene arista de 4 cm. Calcula:

1. Área total
2. Volumen

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $A = 6(16) = 96$ cm²
2. $V = 64$ cm³

</details>

---

### Ejercicio 4: Contar elementos

El octaedro tiene 8 caras y 6 vértices. ¿Cuántas aristas tiene?

<details>
<summary><strong>Ver respuesta</strong></summary>

Usando $V - A + C = 2$:

$$
6 - A + 8 = 2
$$

$$
A = 12 \text{ aristas}
$$

</details>

---

### Ejercicio 5: Verdadero o Falso

1. Existen infinitos poliedros regulares.
2. El tetraedro es su propio dual.
3. El cubo y el octaedro tienen el mismo número de aristas.
4. El icosaedro tiene todas sus caras triangulares.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** - Solo existen 5
2. **Verdadero**
3. **Verdadero** - Ambos tienen 12 aristas
4. **Verdadero**

</details>

---
