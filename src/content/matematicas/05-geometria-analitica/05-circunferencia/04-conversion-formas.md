# Conversión Entre Formas de la Circunferencia

Dominar la conversión entre la forma ordinaria y la forma general de la circunferencia es una habilidad fundamental. En esta lección practicaremos sistemáticamente estas conversiones.

---

## 🎯 ¿Qué vas a aprender?

- Técnicas para convertir entre formas
- Cómo verificar resultados
- Casos especiales y errores comunes

---

## 📖 Lo Esencial de Conversiones

| De → A | Técnica |
|--------|---------|
| Ordinaria → General | Expandir binomios y simplificar |
| General → Ordinaria | Completar el cuadrado |

---

## 📖 De Ordinaria a General

### Procedimiento

1. Expande $(x - h)^2 = x^2 - 2hx + h^2$
2. Expande $(y - k)^2 = y^2 - 2ky + k^2$
3. Pasa $r^2$ al lado izquierdo
4. Identifica $D$, $E$, $F$

### ⚙️ Ejemplo 1: Conversión básica

Convierte $(x - 2)^2 + (y - 5)^2 = 9$ a forma general.

$$
x^2 - 4x + 4 + y^2 - 10y + 25 = 9
$$

$$
x^2 + y^2 - 4x - 10y + 29 - 9 = 0
$$

$$
x^2 + y^2 - 4x - 10y + 20 = 0
$$

### ⚙️ Ejemplo 2: Con signos negativos

Convierte $(x + 3)^2 + (y - 1)^2 = 16$ a forma general.

Recordamos: $(x + 3)^2 = x^2 + 6x + 9$

$$
x^2 + 6x + 9 + y^2 - 2y + 1 = 16
$$

$$
x^2 + y^2 + 6x - 2y + 10 - 16 = 0
$$

$$
x^2 + y^2 + 6x - 2y - 6 = 0
$$

---

## 📖 De General a Ordinaria

### Procedimiento: Completar el Cuadrado

Para $x^2 + bx$: suma y resta $\left(\frac{b}{2}\right)^2$

**Fórmula:**
$$
x^2 + bx = \left(x + \frac{b}{2}\right)^2 - \frac{b^2}{4}
$$

### ⚙️ Ejemplo 3: Paso a paso

Convierte $x^2 + y^2 - 8x + 6y - 11 = 0$ a forma ordinaria.

**Paso 1:** Reorganiza:
$$
(x^2 - 8x) + (y^2 + 6y) = 11
$$

**Paso 2:** Completa el cuadrado para $x$:
- Coeficiente de $x$: $-8$
- Mitad: $-4$
- Cuadrado: $16$
- $x^2 - 8x + 16 = (x - 4)^2$

**Paso 3:** Completa el cuadrado para $y$:
- Coeficiente de $y$: $6$
- Mitad: $3$
- Cuadrado: $9$
- $y^2 + 6y + 9 = (y + 3)^2$

**Paso 4:** Añade los mismos valores al lado derecho:
$$
(x - 4)^2 + (y + 3)^2 = 11 + 16 + 9 = 36
$$

**Resultado:** Centro $(4, -3)$, radio $6$

### ⚙️ Ejemplo 4: Otro ejemplo completo

Convierte $x^2 + y^2 + 2x - 10y + 17 = 0$.

$$
(x^2 + 2x) + (y^2 - 10y) = -17
$$

Para $x$: $x^2 + 2x + 1 = (x + 1)^2$

Para $y$: $y^2 - 10y + 25 = (y - 5)^2$

$$
(x + 1)^2 + (y - 5)^2 = -17 + 1 + 25 = 9
$$

**Resultado:** Centro $(-1, 5)$, radio $3$

---

## 📖 Verificación de Resultados

Siempre verifica tu conversión:

1. **De ordinaria a general:** Expande nuevamente y compara
2. **De general a ordinaria:** Sustituye centro y radio en fórmulas

### ⚙️ Ejemplo 5: Verificación

Verificar que $(x-3)^2 + (y+2)^2 = 25$ da $x^2 + y^2 - 6x + 4y - 12 = 0$.

**Usando fórmulas directas:**

De la forma general $D = -6$, $E = 4$, $F = -12$:

- Centro: $\left(\frac{6}{2}, \frac{-4}{2}\right) = (3, -2)$ ✓
- Radio: $\frac{1}{2}\sqrt{36 + 16 + 48} = \frac{1}{2}\sqrt{100} = 5$ ✓

---

## 📖 Casos Especiales

### Circunferencia centrada en el origen

$$
x^2 + y^2 = r^2 \iff x^2 + y^2 - r^2 = 0
$$

En este caso: $D = 0$, $E = 0$, $F = -r^2$

### ⚙️ Ejemplo 6: Centro en origen

$x^2 + y^2 = 49$

Forma general: $x^2 + y^2 - 49 = 0$

### Circunferencia con centro en un eje

Si el centro está sobre el eje X: $C(h, 0)$

$$
(x - h)^2 + y^2 = r^2
$$

### ⚙️ Ejemplo 7: Centro sobre eje X

$(x - 4)^2 + y^2 = 9$

Forma general: $x^2 - 8x + 16 + y^2 - 9 = 0$

$$
x^2 + y^2 - 8x + 7 = 0
$$

---

## 📖 Errores Comunes

| Error | Corrección |
|-------|-----------|
| Olvidar sumar al lado derecho | Al completar el cuadrado, lo que sumas a la izquierda también va a la derecha |
| Confundir signos del centro | $(x + 3) = (x - (-3))$ significa $h = -3$ |
| Olvidar que $r^2$ está en la ecuación | El número es $r^2$, no $r$ |

---

## 🔑 Resumen

| Proceso | Pasos clave |
|---------|-------------|
| Ordinaria → General | Expandir, reorganizar, simplificar |
| General → Ordinaria | Agrupar, completar cuadrado, sumar a ambos lados |
| Centro de forma general | $\left(-\frac{D}{2}, -\frac{E}{2}\right)$ |
| Radio de forma general | $\frac{1}{2}\sqrt{D^2 + E^2 - 4F}$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Convierte $(x + 5)^2 + (y - 2)^2 = 36$ a forma general.

<details>
<summary>Ver solución</summary>

$x^2 + 10x + 25 + y^2 - 4y + 4 = 36$

$x^2 + y^2 + 10x - 4y - 7 = 0$

</details>

### Ejercicio 2
Convierte $x^2 + y^2 - 12x + 4y + 15 = 0$ a forma ordinaria.

<details>
<summary>Ver solución</summary>

$(x^2 - 12x + 36) + (y^2 + 4y + 4) = -15 + 36 + 4$

$(x - 6)^2 + (y + 2)^2 = 25$

Centro: $(6, -2)$, Radio: $5$

</details>

### Ejercicio 3
Encuentra centro y radio de $x^2 + y^2 + 6x = 0$.

<details>
<summary>Ver solución</summary>

$D = 6$, $E = 0$, $F = 0$

Centro: $(-3, 0)$

Radio: $\frac{1}{2}\sqrt{36 + 0 - 0} = 3$

O completando cuadrado:
$(x + 3)^2 - 9 + y^2 = 0$
$(x + 3)^2 + y^2 = 9$

</details>

### Ejercicio 4
Convierte $(x - 1)^2 + (y + 4)^2 = 1$ a forma general.

<details>
<summary>Ver solución</summary>

$x^2 - 2x + 1 + y^2 + 8y + 16 = 1$

$x^2 + y^2 - 2x + 8y + 16 = 0$

</details>

### Ejercicio 5
Verifica convirtiendo en ambas direcciones: ¿$(x-2)^2+(y-3)^2=4$ es equivalente a $x^2+y^2-4x-6y+9=0$?

<details>
<summary>Ver solución</summary>

**Expandiendo la forma ordinaria:**

$x^2 - 4x + 4 + y^2 - 6y + 9 = 4$

$x^2 + y^2 - 4x - 6y + 13 - 4 = 0$

$x^2 + y^2 - 4x - 6y + 9 = 0$ ✓

**Sí son equivalentes.**

</details>
