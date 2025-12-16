# Posiciones entre Circunferencias

Dos circunferencias pueden estar en diferentes posiciones relativas según la distancia entre sus centros y la relación con sus radios.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Posiciones relativas entre circunferencias</strong>
  </div>

![Posiciones entre circunferencias](/images/geometria/circulos/posiciones-circunferencias.svg)

</div>

---

## 📖 Elementos a considerar

Sean dos circunferencias con:
- Centros $O_1$ y $O_2$
- Radios $r_1$ y $r_2$ (asumimos $r_1 \geq r_2$)
- Distancia entre centros $d = \overline{O_1O_2}$

---

## 📖 Circunferencias exteriores

> **Definición:** Dos circunferencias son **exteriores** cuando **no tienen puntos en común** y una está completamente fuera de la otra.

### Condición

$$
d > r_1 + r_2
$$

La distancia entre centros es **mayor** que la suma de los radios.

### Puntos comunes: 0

---

## 📖 Circunferencias tangentes exteriores

> **Definición:** Dos circunferencias son **tangentes exteriores** cuando se tocan en **un solo punto** y cada una está fuera de la otra.

### Condición

$$
d = r_1 + r_2
$$

La distancia entre centros es **igual** a la suma de los radios.

### Puntos comunes: 1

---

## 📖 Circunferencias secantes

> **Definición:** Dos circunferencias son **secantes** cuando se cortan en **dos puntos**.

### Condición

$$
|r_1 - r_2| < d < r_1 + r_2
$$

La distancia está entre la diferencia y la suma de los radios.

### Puntos comunes: 2

---

## 📖 Circunferencias tangentes interiores

> **Definición:** Dos circunferencias son **tangentes interiores** cuando se tocan en **un solo punto** y una está dentro de la otra.

### Condición

$$
d = |r_1 - r_2|
$$

La distancia entre centros es **igual** a la diferencia de los radios.

### Puntos comunes: 1

---

## 📖 Circunferencias interiores

> **Definición:** Dos circunferencias son **interiores** cuando una está completamente **dentro** de la otra, sin tocarse.

### Condición

$$
d < |r_1 - r_2|
$$

La distancia entre centros es **menor** que la diferencia de los radios.

### Puntos comunes: 0

---

## 📖 Circunferencias concéntricas

> **Definición:** Dos circunferencias son **concéntricas** cuando tienen el **mismo centro**.

### Condición

$$
d = 0
$$

### Puntos comunes: 0 (si $r_1 \neq r_2$) o infinitos (si $r_1 = r_2$)

---

## 📖 Tabla resumen

| Posición | Condición | Puntos comunes |
|----------|-----------|----------------|
| Exteriores | $d > r_1 + r_2$ | 0 |
| Tangentes exteriores | $d = r_1 + r_2$ | 1 |
| Secantes | $\|r_1 - r_2\| < d < r_1 + r_2$ | 2 |
| Tangentes interiores | $d = \|r_1 - r_2\|$ | 1 |
| Interiores | $d < \|r_1 - r_2\|$ | 0 |
| Concéntricas | $d = 0$ | 0 (o infinitos) |

---

## 📖 Ejemplos

### Ejemplo 1

$r_1 = 5$ cm, $r_2 = 3$ cm, $d = 10$ cm

$$
r_1 + r_2 = 8, \quad |r_1 - r_2| = 2
$$

Como $d = 10 > 8 = r_1 + r_2$: **Exteriores**

### Ejemplo 2

$r_1 = 6$ cm, $r_2 = 4$ cm, $d = 10$ cm

$$
d = 6 + 4 = r_1 + r_2
$$

**Tangentes exteriores**

### Ejemplo 3

$r_1 = 8$ cm, $r_2 = 5$ cm, $d = 6$ cm

$$
|r_1 - r_2| = 3, \quad r_1 + r_2 = 13
$$

Como $3 < 6 < 13$: **Secantes**

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificar posiciones

Determina la posición relativa de las circunferencias:

1. $r_1 = 7$ cm, $r_2 = 4$ cm, $d = 15$ cm
2. $r_1 = 6$ cm, $r_2 = 3$ cm, $d = 9$ cm
3. $r_1 = 10$ cm, $r_2 = 4$ cm, $d = 8$ cm
4. $r_1 = 8$ cm, $r_2 = 3$ cm, $d = 5$ cm

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $r_1 + r_2 = 11$, $d = 15 > 11$ → **Exteriores**
2. $r_1 + r_2 = 9$, $d = 9 = 9$ → **Tangentes exteriores**
3. $|r_1 - r_2| = 6$, $r_1 + r_2 = 14$, $6 < 8 < 14$ → **Secantes**
4. $|r_1 - r_2| = 5$, $d = 5 = 5$ → **Tangentes interiores**

</details>

---

### Ejercicio 2: Encontrar distancia

¿A qué distancia deben estar los centros para que las circunferencias sean tangentes exteriores si $r_1 = 5$ cm y $r_2 = 3$ cm?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
d = r_1 + r_2 = 5 + 3 = 8 \text{ cm}
$$

</details>

---

### Ejercicio 3: Problema inverso

Dos circunferencias secantes tienen radios 10 cm y 6 cm. ¿Entre qué valores puede estar la distancia entre centros?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
|10 - 6| < d < 10 + 6
$$

$$
4 < d < 16
$$

La distancia debe estar entre 4 cm y 16 cm (sin incluir los extremos).

</details>

---

### Ejercicio 4: Verdadero o Falso

1. Dos circunferencias concéntricas tienen el mismo centro.
2. Si $d = r_1 + r_2$, las circunferencias son tangentes interiores.
3. Dos circunferencias secantes tienen exactamente 2 puntos en común.
4. Si una circunferencia está dentro de otra sin tocarla, son interiores.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero**
2. **Falso** - Son tangentes exteriores
3. **Verdadero**
4. **Verdadero**

</details>

---
