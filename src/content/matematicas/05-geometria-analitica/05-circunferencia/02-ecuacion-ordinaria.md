# Ecuación Ordinaria de la Circunferencia

La **ecuación ordinaria** (o canónica) de la circunferencia es la forma más directa de escribir su ecuación, ya que muestra explícitamente el centro y el radio.

---

## 🎯 ¿Qué vas a aprender?

- La forma ordinaria de la ecuación
- Cómo extraer información del centro y radio
- Cómo construir la ecuación en diferentes situaciones

---

## 📖 Lo Esencial de Ecuación Ordinaria

| Situación | Ecuación |
|-----------|----------|
| Centro $(h, k)$, radio $r$ | $(x - h)^2 + (y - k)^2 = r^2$ |
| Centro en el origen | $x^2 + y^2 = r^2$ |

---

## 📖 La Forma Ordinaria

La **ecuación ordinaria** de una circunferencia con centro $C(h, k)$ y radio $r$ es:

$$
(x - h)^2 + (y - k)^2 = r^2
$$

**Características:**
- Los términos $(x - h)$ y $(y - k)$ son binomios al cuadrado
- El lado derecho es $r^2$, no $r$
- El centro se lee directamente: $(h, k)$
- El radio se obtiene: $r = \sqrt{\text{lado derecho}}$

---

## 📖 Lectura de Centro y Radio

Para leer el centro y radio de una ecuación ordinaria:

| De la ecuación | Se obtiene |
|----------------|-----------|
| $(x - h)$ | $h$ (coordenada x del centro) |
| $(y - k)$ | $k$ (coordenada y del centro) |
| Número del lado derecho | $r^2$ (radio al cuadrado) |

### ⚙️ Ejemplo 1: Lectura directa

De $(x - 3)^2 + (y - 5)^2 = 16$:

- $h = 3$, $k = 5$ → Centro: $(3, 5)$
- $r^2 = 16$ → $r = 4$

### ⚙️ Ejemplo 2: Con signos negativos

De $(x + 2)^2 + (y - 4)^2 = 25$:

- $(x + 2) = (x - (-2))$ → $h = -2$
- $(y - 4)$ → $k = 4$
- Centro: $(-2, 4)$
- $r = 5$

### ⚙️ Ejemplo 3: Centro en origen

De $x^2 + y^2 = 9$:

Esto es $(x - 0)^2 + (y - 0)^2 = 9$

- Centro: $(0, 0)$
- $r = 3$

---

## 📖 Construcción de la Ecuación

### Dado centro y radio

### ⚙️ Ejemplo 4: Centro y radio dados

Centro $(4, -1)$, radio $7$.

$$
(x - 4)^2 + (y - (-1))^2 = 49
$$

$$
(x - 4)^2 + (y + 1)^2 = 49
$$

### Dado centro y un punto de la circunferencia

Primero calculamos el radio como la distancia del centro al punto.

### ⚙️ Ejemplo 5: Centro y punto

Centro $(1, 2)$ y pasa por $(4, 6)$.

**Paso 1:** Calcular radio:
$$
r = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = 5
$$

**Paso 2:** Ecuación:
$$
(x - 1)^2 + (y - 2)^2 = 25
$$

### Dados los extremos del diámetro

El centro es el punto medio del diámetro, y el radio es la mitad de la longitud del diámetro.

### ⚙️ Ejemplo 6: Extremos del diámetro

Extremos del diámetro en $A(2, 3)$ y $B(8, 11)$.

**Paso 1:** Centro (punto medio):
$$
C = \left(\frac{2+8}{2}, \frac{3+11}{2}\right) = (5, 7)
$$

**Paso 2:** Diámetro:
$$
d = \sqrt{(8-2)^2 + (11-3)^2} = \sqrt{36 + 64} = 10
$$

**Paso 3:** Radio: $r = \frac{d}{2} = 5$

**Paso 4:** Ecuación:
$$
(x - 5)^2 + (y - 7)^2 = 25
$$

---

## 📖 Dado el Centro y Tangente a un Eje

Si la circunferencia es **tangente** a un eje, el radio es la distancia del centro al eje.

### ⚙️ Ejemplo 7: Tangente al eje X

Centro $(3, 4)$, tangente al eje X.

La distancia del centro $(3, 4)$ al eje X es $|4| = 4$.

Por lo tanto, $r = 4$.

$$
(x - 3)^2 + (y - 4)^2 = 16
$$

### ⚙️ Ejemplo 8: Tangente al eje Y

Centro $(-5, 2)$, tangente al eje Y.

La distancia del centro al eje Y es $|-5| = 5$.

Por lo tanto, $r = 5$.

$$
(x + 5)^2 + (y - 2)^2 = 25
$$

---

## 📖 Dado el Centro y Tangente a una Recta

El radio es la distancia del centro a la recta tangente.

### ⚙️ Ejemplo 9: Tangente a una recta

Centro $(4, 1)$, tangente a la recta $3x + 4y - 20 = 0$.

**Radio = distancia punto-recta:**
$$
r = \frac{|3(4) + 4(1) - 20|}{\sqrt{9 + 16}} = \frac{|12 + 4 - 20|}{5} = \frac{4}{5}
$$

**Ecuación:**
$$
(x - 4)^2 + (y - 1)^2 = \frac{16}{25}
$$

---

## 🔑 Resumen

| Datos conocidos | Procedimiento |
|-----------------|---------------|
| Centro y radio | Sustituir directamente |
| Centro y punto | Calcular radio con distancia |
| Extremos del diámetro | Centro = punto medio, radio = d/2 |
| Centro y tangente a eje | Radio = distancia al eje |
| Centro y tangente a recta | Radio = distancia punto-recta |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la ecuación de la circunferencia con centro $(-3, 5)$ y radio 4.

<details>
<summary>Ver solución</summary>

$$
(x + 3)^2 + (y - 5)^2 = 16
$$

</details>

### Ejercicio 2
Identifica centro y radio de $(x + 4)^2 + (y + 1)^2 = 81$.

<details>
<summary>Ver solución</summary>

Centro: $(-4, -1)$
Radio: $r = 9$

</details>

### Ejercicio 3
Encuentra la ecuación de la circunferencia con centro en $(2, -3)$ que pasa por $(5, 1)$.

<details>
<summary>Ver solución</summary>

$$
r = \sqrt{(5-2)^2 + (1-(-3))^2} = \sqrt{9 + 16} = 5
$$

Ecuación: $(x - 2)^2 + (y + 3)^2 = 25$

</details>

### Ejercicio 4
Una circunferencia tiene centro en $(0, 5)$ y es tangente al eje X. Encuentra su ecuación.

<details>
<summary>Ver solución</summary>

Radio = distancia al eje X = $|5| = 5$

Ecuación: $x^2 + (y - 5)^2 = 25$

</details>

### Ejercicio 5
Encuentra la ecuación de la circunferencia cuyo diámetro tiene extremos en $(1, 1)$ y $(7, 9)$.

<details>
<summary>Ver solución</summary>

Centro: $(4, 5)$

Diámetro: $\sqrt{36 + 64} = 10$

Radio: $r = 5$

Ecuación: $(x - 4)^2 + (y - 5)^2 = 25$

</details>
