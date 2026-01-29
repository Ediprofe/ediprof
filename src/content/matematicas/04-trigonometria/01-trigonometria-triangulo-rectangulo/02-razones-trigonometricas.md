# **Razones Trigonométricas**

Imagina que puedes describir la forma de cualquier rampa, montaña o techo con solo un número. Ese número (una división de dos lados) es una **Razón Trigonométrica**. Son la huella digital del triángulo.

---

## 🎯 ¿Qué vas a aprender?

- Qué significa realmente una "razón" en trigonometría.
- Las 3 razones principales: **Seno**, **Coseno**, y **Tangente**.
- La legendaria regla mnemotécnica: **SOH-CAH-TOA**.
- Cómo estas razones no cambian aunque el triángulo se haga gigante.

---

## ➗ ¿Qué es una Razón?

En matemáticas, una "razón" no es tener la verdad de un argumento, sino una comparación entre dos números mediante una división (como una receta de cocina: "2 de harina por 1 de agua").

En un triángulo rectángulo, comparamos sus lados:
*   ¿Qué tan grande es el opuesto comparado con la hipotenusa?
*   ¿Qué tan grande es el opuesto comparado con el adyacente?

![Concepto de Razón](/images/geometria/trigonometria/ratio-concept.svg)

---

## 🏹 Las 3 Grandes: SOH - CAH - TOA

Existen nombres específicos para estas divisiones. Apréndetelos, porque los usarás por el resto de tu vida académica (y profesional si eliges ciencias).

### 1. Seno (sin)
Mide la proporción del lado que está **enfrente** de ti respecto al lado más largo. En nuestro triángulo 3-4-5:

$$
\sin(\theta) = \frac{\text{Opuesto}}{\text{Hipotenusa}}
$$

![Razón Seno](/images/geometria/trigonometria/ratio-sine.svg)

### 2. Coseno (cos)
Mide la proporción del lado que **toca tu ángulo** respecto al lado más largo. En nuestro triángulo 3-4-5:

$$
\cos(\theta) = \frac{\text{Adyacente}}{\text{Hipotenusa}}
$$

![Razón Coseno](/images/geometria/trigonometria/ratio-cosine.svg)

### 3. Tangente (tan)
Compara directamente tus dos catetos. En nuestro triángulo 3-4-5:

$$
\tan(\theta) = \frac{\text{Opuesto}}{\text{Adyacente}}
$$

![Razón Tangente](/images/geometria/trigonometria/ratio-tangent.svg)

### SOH-CAH-TOA
> **Para recordar:** **SOH** (Seno=Op/Hip) - **CAH** (Cos=Ad/Hip) - **TOA** (Tan=Op/Ad). Repítelo 5 veces.

![SOH-CAH-TOA](/images/geometria/trigonometria/07-soh-cah-toa.svg)

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Calcular Razones Básicas

Dado un triángulo con Opuesto=3, Adyacente=4, Hipotenusa=5. Calcular $\sin$, $\cos$ y $\tan$.

Identificaremos los valores de los lados y aplicaremos las fórmulas de SOH-CAH-TOA.

![Ejemplo 1: Razones Básicas](/images/geometria/trigonometria/example-ratios-basic.svg)

**Razonamiento:**

*   **Seno (SOH):** Opuesto / Hipotenusa.
    $$
    \sin(\theta) = \frac{3}{5} = 0.6
    $$
*   **Coseno (CAH):** Adyacente / Hipotenusa.
    $$
    \cos(\theta) = \frac{4}{5} = 0.8
    $$
*   **Tangente (TOA):** Opuesto / Adyacente.
    $$
    \tan(\theta) = \frac{3}{4} = 0.75
    $$

**Resultado:**
$$
\boxed{\sin=0.6, \cos=0.8, \tan=0.75}
$$

### Ejemplo 2: Triángulo Gigante

Imagina que duplicamos el triángulo anterior. Ahora Opuesto=6, Adyacente=8, Hipotenusa=10.

Demostraremos que la escala del triángulo no altera el valor de sus razones trigonométricas.

![Ejemplo 2: Razones en Semejanza](/images/geometria/trigonometria/example-ratios-similarity.svg)

**Razonamiento:**

Probamos con el Seno:
$$
\sin(\theta) = \frac{6}{10} = 0.6
$$

Como puedes ver, al simplificar la fracción $\frac{6}{10}$, volvemos al valor original de $\frac{3}{5}$.

**Resultado:**
$$
\boxed{0.6}
$$

> **¡Magia!** El resultado es idéntico. Las razones trigonométricas **solo dependen del ángulo**, no del tamaño del triángulo.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
En un triángulo, el lado opuesto mide 5 y la hipotenusa 13. ¿Cuánto vale el Seno?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Aplicamos la definición de Seno:

$$
\text{Seno} = \frac{\text{Opuesto}}{\text{Hipotenusa}}
$$

**Resultado:**
$$
\boxed{\frac{5}{13} \approx 0.38}
$$

</details>

### Ejercicio 2
En el mismo triángulo ($Op=5, Hip=13$), usa Pitágoras para hallar el Adyacente, y luego calcula el Coseno.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
1.  Hallamos el cateto adyacente usando el Teorema de Pitágoras:

$$
Ady = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12
$$

2.  Calculamos el Coseno:

$$
\cos = \frac{12}{13}
$$

**Resultado:**
$$
\boxed{\frac{12}{13} \approx 0.92}
$$

</details>

### Ejercicio 3
¿Cuál es la fórmula para la Tangente?

<details>
<summary>Ver solución</summary>

**Resultado:**
$$
\boxed{\frac{\text{Opuesto}}{\text{Adyacente}}}
$$

</details>

### Ejercicio 4
Si $\tan(\theta) = 1$, ¿qué relación existe entre el lado Opuesto y el Adyacente?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si $O/A = 1$, entonces $O = A$.

**Resultado:**
$$
\boxed{\text{Son iguales}}
$$

</details>

### Ejercicio 5
Calcula el Seno de un ángulo si Opuesto=8 e Hipotenusa=10. Simplifica la fracción.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Simplificamos la fracción dividiendo ambos números por 2:

$$
\frac{8}{10} = \frac{4}{5}
$$

**Resultado:**
$$
\boxed{\frac{4}{5}}
$$

</details>

### Ejercicio 6
Verdadero o Falso: El Seno nunca puede ser mayor que 1.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Verdadero. Como la hipotenusa es el lado más largo, la división $Op/Hip$ siempre es menor (o igual) a 1.

**Resultado:**
$$
\boxed{\text{Verdadero}}
$$

</details>

### Ejercicio 7
Si $\sin(\theta) = 0.5$, ¿cuál es la relación entre el Opuesto y la Hipotenusa?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Una razón de $0.5$ equivale a $\frac{1}{2}$. Esto significa que el numerador es la mitad del denominador.

**Resultado:**
$$
\boxed{\text{El opuesto mide la mitad que la hipotenusa}}
$$

</details>

### Ejercicio 8
Completa la frase: "SOH - CAH - ..."

<details>
<summary>Ver solución</summary>

**Resultado:**

$$
\boxed{\text{TOA}}
$$

</details>

### Ejercicio 9
Calcula la Tangente si Opuesto=10 y Adyacente=2.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Dividimos los valores dados:

$$
\frac{10}{2} = 5
$$

**Resultado:**
$$
\boxed{5}
$$

</details>

### Ejercicio 10
Un triángulo rectángulo isósceles tiene catetos iguales (digamos que miden 1). Calcula su tangente.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Al ser isósceles, el opuesto y el adyacente valen 1:

$$
\tan = \frac{1}{1} = 1
$$

**Resultado:**
$$
\boxed{1}
$$

</details>

---

## 🔑 Resumen

| Razón | Fórmula | Mnemotecnia |
| :--- | :--- | :--- |
| **Seno** | Opuesto / Hipotenusa | **S**OH |
| **Coseno** | Adyacente / Hipotenusa | **C**AH |
| **Tangente** | Opuesto / Adyacente | **T**OA |

> **SOH-CAH-TOA**. Si recuerdas esto, aprobaste trigonometría.
