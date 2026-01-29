# **Posiciones de una Recta respecto a la Circunferencia**

Imagina que lanzas una flecha (recta) hacia un escudo redondo (circunferencia). Puede pasar por un lado sin tocarlo, puede rozarlo en el borde, o puede clavarse y atravesarlo. Estas son las tres relaciones posibles entre una recta y un círculo.

---

## 🎯 ¿Qué vas a aprender?

- Determinar si una recta es exterior, tangente o secante comparando distancias.
- Comprender la propiedad fundamental de perpendicularidad en la tangente.
- Calcular la longitud de segmentos tangentes desde puntos exteriores usando Pitágoras.

---

## 📏 Clasificación por Distancia

La clave para clasificar la posición es comparar la distancia ($d$) desde el centro a la recta con el radio ($r$).

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Posiciones Relativas</strong>
  </div>
  <img src="/images/geometria/circulos/tangente-secante.svg" alt="Diagrama de recta tangente y secante" style="width: 100%; height: auto;">
</div>

### 1. Recta Exterior
Pasa "lejos" de la circunferencia. No tienen ningún punto en común.
*   **Condición:** La distancia es mayor que el radio.
$$ d > r $$

### 2. Recta Tangente
"Besa" a la circunferencia en un solo punto.
*   **Condición:** La distancia es igual al radio.
$$ d = r $$
*   **Propiedad Crítica:** El radio en el punto de contacto es perpendicular ($90^\circ$) a la recta.

### 3. Recta Secante
"Corta" a la circunferencia en dos puntos.
*   **Condición:** La distancia es menor que el radio.
$$ d < r $$
*   La parte de la recta que queda dentro se llama **cuerda**.

---

## 📐 El Teorema de la Tangente

Si trazas una recta tangente desde un punto exterior $P$ hasta el punto de contacto $T$, se forma un triángulo rectángulo con el centro $O$.

-   **Hipotenusa:** Distancia del centro a $P$ ($d$).
-   **Cateto 1:** Radio ($r$).
-   **Cateto 2:** Segmento Tangente ($t$).

Por Pitágoras:

$$
d^2 = r^2 + t^2
$$

De aquí podemos calcular la longitud del segmento tangente:

$$
t = \sqrt{d^2 - r^2}
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Identificación

Una circunferencia tiene radio $r=5$ cm. Una recta pasa a una distancia $d=3$ cm del centro. ¿Cómo es la recta?

**Razonamiento:**
Comparamos $3$ con $5$.
Como $3 < 5$, la recta se "mete" dentro del círculo.

**Resultado:**
$$
\boxed{\text{Secante}}
$$

### Ejemplo 2: Cálculo de Tangente

Desde un punto situado a 10 cm del centro de una circunferencia de radio 6 cm, se traza una tangente. ¿Cuánto mide el segmento desde el punto hasta el contacto?

**Datos:**
-   $d = 10$ (Hipotenusa)
-   $r = 6$ (Cateto)
-   $t = ?$ (Cateto)

**Razonamiento:**
$$
t = \sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64}
$$

**Resultado:**
$$
\boxed{8 \text{ cm}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
El radio mide 8 cm y la distancia de la recta al centro es 8 cm. ¿Qué posición tiene?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$d = r$.

**Resultado:**
$$
\boxed{\text{Tangente}}
$$

</details>

### Ejercicio 2
Si la recta es exterior, ¿cómo es la distancia al centro comparada con el radio?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
d > r
$$

</details>

### Ejercicio 3
Calcula la longitud de la tangente trazada desde un punto a 13 cm del centro, si el radio es 5 cm.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Triángulo (5, 12, 13).
$$
t = \sqrt{13^2 - 5^2} = \sqrt{169-25} = \sqrt{144}
$$

**Resultado:**
$$
\boxed{12 \text{ cm}}
$$

</details>

### Ejercicio 4
Una recta corta a la circunferencia en dos puntos. ¿Cómo se llama?

<details>
<summary>Ver solución</summary>

**Respuesta:**
$$
\text{Secante}
$$

</details>

### Ejercicio 5
¿Cuántos puntos en común tiene una recta exterior con la circunferencia?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
0
$$

</details>

### Ejercicio 6
Verdadero o Falso: El segmento tangente desde un punto exterior es más largo que la distancia de ese punto al centro.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La distancia al centro es la hipotenusa. La tangente es un cateto. La hipotenusa siempre es mayor.

**Resultado:**
$$
\boxed{\text{Falso}}
$$

</details>

### Ejercicio 7
Si $r = 10$, $d = 12$, la recta es...

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$12 > 10$.

**Resultado:**
$$
\boxed{\text{Exterior}}
$$

</details>

### Ejercicio 8
¿Qué ángulo forman el radio y la tangente en el punto de contacto?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
90^\circ
$$

</details>

### Ejercicio 9
Calcula la distancia al centro si el radio es 3 y la tangente mide 4.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
d = \sqrt{3^2 + 4^2} = \sqrt{9+16} = 5
$$

**Resultado:**
$$
\boxed{5}
$$

</details>

### Ejercicio 10
Desde un punto exterior se trazan dos tangentes. Si una mide 15 cm, ¿cuánto mide la otra?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Por el teorema de las dos tangentes (teorema del sombrero), ambos segmentos son congruentes.

**Resultado:**
$$
\boxed{15 \text{ cm}}
$$

</details>

---

## 🔑 Resumen

| Posición | Distancia ($d$) vs Radio ($r$) | Puntos de contacto |
| :--- | :--- | :---: |
| **Exterior** | $d > r$ | 0 |
| **Tangente** | $d = r$ | 1 |
| **Secante** | $d < r$ | 2 |

> La tangente es el límite preciso entre cortar y no tocar.
