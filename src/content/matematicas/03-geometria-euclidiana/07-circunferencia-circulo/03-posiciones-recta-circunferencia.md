# Posiciones de una Recta respecto a la Circunferencia

Una recta puede estar en diferentes posiciones respecto a una circunferencia: exterior, tangente o secante. La posición depende de la distancia de la recta al centro.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Tangente vs Secante</strong>
  </div>

![Tangente y secante](/images/geometria/circulos/tangente-secante.svg)

</div>

---

## 📖 Distancia de una recta al centro

Para determinar la posición de una recta respecto a la circunferencia, comparamos:
- $d$ = distancia perpendicular de la recta al centro
- $r$ = radio de la circunferencia

---

## 📖 Posición exterior

> **Definición:** Una recta es **exterior** a la circunferencia cuando **no la toca** en ningún punto.

### Condición

$$
d > r
$$

La distancia de la recta al centro es **mayor** que el radio.

### Ejemplo

Si $r = 5$ cm y la distancia de la recta al centro es 7 cm:
$$
7 > 5 \Rightarrow \text{Recta exterior}
$$

---

## 📖 Posición tangente

> **Definición:** Una recta es **tangente** a la circunferencia cuando la toca en **exactamente un punto**.

### Condición

$$
d = r
$$

La distancia de la recta al centro es **igual** al radio.

### Propiedades de la tangente

1. El punto de contacto se llama **punto de tangencia**
2. La tangente es **perpendicular** al radio en el punto de tangencia
3. El radio que pasa por el punto de tangencia forma ángulo de 90° con la tangente

### Ejemplo

Si $r = 5$ cm y la distancia de la recta al centro es 5 cm:
$$
5 = 5 \Rightarrow \text{Recta tangente}
$$

---

## 📖 Posición secante

> **Definición:** Una recta es **secante** a la circunferencia cuando la corta en **dos puntos**.

### Condición

$$
d < r
$$

La distancia de la recta al centro es **menor** que el radio.

### Propiedades de la secante

1. Define una **cuerda** (segmento entre los dos puntos de intersección)
2. Divide a la circunferencia en dos **arcos**
3. Divide al círculo en dos regiones

### Ejemplo

Si $r = 5$ cm y la distancia de la recta al centro es 3 cm:
$$
3 < 5 \Rightarrow \text{Recta secante}
$$

---

## 📖 Tabla resumen

| Posición | Condición | Puntos comunes |
|----------|-----------|----------------|
| Exterior | $d > r$ | 0 |
| Tangente | $d = r$ | 1 |
| Secante | $d < r$ | 2 |

---

## 📖 Caso especial: Recta que pasa por el centro

Si una recta pasa por el centro de la circunferencia:
- $d = 0$
- Es una **secante** (corta en 2 puntos)
- La cuerda que define es el **diámetro**

---

## 📖 Tangentes desde un punto exterior

Desde un punto $P$ exterior a la circunferencia:
- Se pueden trazar **exactamente dos tangentes**
- Los segmentos desde $P$ hasta los puntos de tangencia son **iguales**

### Fórmula

Si $P$ está a distancia $d$ del centro y el radio es $r$, la longitud de cada segmento tangente es:

$$
t = \sqrt{d^2 - r^2}
$$

### Ejemplo

Si $P$ está a 13 cm del centro y $r = 5$ cm:

$$
t = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12 \text{ cm}
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificar posiciones

Una circunferencia tiene radio 6 cm. ¿Cuál es la posición de cada recta?

1. Recta a 8 cm del centro
2. Recta a 6 cm del centro
3. Recta a 4 cm del centro
4. Recta que pasa por el centro

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $8 > 6$ → **Exterior**
2. $6 = 6$ → **Tangente**
3. $4 < 6$ → **Secante**
4. $0 < 6$ → **Secante** (pasa por el centro, es diámetro)

</details>

---

### Ejercicio 2: Encontrar la distancia

¿A qué distancia del centro debe estar una recta para ser tangente a una circunferencia de radio 10 cm?

<details>
<summary><strong>Ver respuesta</strong></summary>

Para ser tangente: $d = r = 10$ cm

</details>

---

### Ejercicio 3: Longitud de tangente

Desde un punto $P$ a 15 cm del centro de una circunferencia de radio 9 cm, ¿cuánto mide el segmento tangente?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
t = \sqrt{15^2 - 9^2} = \sqrt{225 - 81} = \sqrt{144} = 12 \text{ cm}
$$

</details>

---

### Ejercicio 4: Problema inverso

El segmento tangente desde un punto $P$ mide 8 cm y la circunferencia tiene radio 6 cm. ¿A qué distancia está $P$ del centro?

<details>
<summary><strong>Ver respuesta</strong></summary>

Usando Pitágoras:
$$
d^2 = t^2 + r^2 = 8^2 + 6^2 = 64 + 36 = 100
$$

$$
d = 10 \text{ cm}
$$

</details>

---

### Ejercicio 5: Verdadero o Falso

1. Una recta tangente toca la circunferencia en dos puntos.
2. La tangente es perpendicular al radio en el punto de tangencia.
3. Si $d < r$, la recta es exterior.
4. Desde un punto exterior se pueden trazar exactamente dos tangentes.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** - Toca en exactamente un punto
2. **Verdadero**
3. **Falso** - Si $d < r$, la recta es secante
4. **Verdadero**

</details>

---
