# **Curvas Paramétricas Especiales**

Más allá de los círculos y elipses, existe un zoológico de curvas fascinantes que solo pueden describirse fácilmente mediante ecuaciones paramétricas. Muchas nacen de la mecánica de ruedas girando sobre otras ruedas.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una **Cicloide** (la curva de la llanta).
- Espirografía matemática: **Epi e Hipocicloides**.
- Otras curvas famosas como la **Astroide**.

---

## 🚲 Concepto 1: La Familia Cicloide

Imagina una luz pegada en el borde de una llanta de bicicleta. Mientras la bicicleta avanza, la luz dibuja una curva en el aire. Eso es una cicloide.

**5 Ejemplos de Esta Familia:**

### Ejemplo 1.1: La Cicloide Clásica
Una rueda de radio $r$ gira sobre el piso plano.
*   Ecuaciones:
    $$ x = r(t - \sin t) $$
    $$ y = r(1 - \cos t) $$
*   Esta curva es famosa por ser la **Braquistócrona**: la rampa de bajada más rápida posible entre dos puntos.

### Ejemplo 1.2: La Cicloide Cortada (Curtate)
La luz no está en el borde, sino más cerca del eje (radio del punto $b < r$ de la llanta).
*   Dibuja una onda suave, sin tocar el suelo.
*   Ec: $x = rt - b \sin t, \ y = r - b \cos t$.

### Ejemplo 1.3: La Cicloide Alargada (Prolate)
La luz está en una varilla que sobresale de la llanta ($b > r$).
*   La curva hace bucles ("lazos") hacia atrás cada vez que toca el suelo. Es como la antigua caligrafía escolar.

### Ejemplo 1.4: Trocoide
Es el nombre general para los casos 1.2 y 1.3. Cualquier punto de un disco rodante genera una trocoide.

### Ejemplo 1.5: Propiedad del Arco
Un arco completo de cicloide (de un rebote al siguiente) tiene una longitud exacta de **$8r$**. ¡Es un número entero, sin $\pi$, aunque provenga de un círculo!

---

## ⚙️ Concepto 2: Rodando sobre Círculos (Espirografía)

Ahora la rueda no gira en el piso, sino sobre otra rueda (como un engranaje planetario).

**5 Curvas Espirográficas:**

### Ejemplo 2.1: Epicicloide
Una rueda pequeña (radio $r$) rueda por **fuera** de una grande (radio $R$).
*   Parece una flor con pétalos redondos hacia afuera.
*   Ec: $x = (R+r)\cos t - r \cos(\frac{R+r}{r}t)$.

### Ejemplo 2.2: Hipocicloide
La rueda pequeña rueda por **dentro** de la grande.
*   Parece una estrella o flor con pétalos hacia adentro.

### Ejemplo 2.3: La Astroide (Estrella)
Es un caso especial de Hipocicloide donde la rueda pequeña es exactamente 1/4 de la grande ($R=4r$).
*   Dibuja una estrella de 4 puntas cóncavas perfectas.
*   Ec: $x = a \cos^3 t, \ y = a \sin^3 t$.

### Ejemplo 2.4: Recta de Tusi (Caso Mágico)
Si la rueda pequeña es exactamente **la mitad** de la grande ($R=2r$) en una Hipocicloide.
*   ¡La curva resultante es una línea recta perfecta!
*   El punto se mueve de un lado a otro del diámetro.

### Ejemplo 2.5: Cardioide (Corazón)
Es una Epicicloide donde ambas ruedas son **iguales** ($R=r$).
*   Dibuja la forma de corazón clásica (con una cúspide).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la altura máxima de una cicloide con $r=2$.

<details>
<summary>Ver solución</summary>
$y_{max} = 2r = 4$. (Cuando la rueda da media vuelta, el punto está arriba).
</details>

---

### Ejercicio 2
¿Cuántas puntas tiene una astroide?

<details>
<summary>Ver solución</summary>
4 puntas.
</details>

---

### Ejercicio 3
Identifica la curva $x = 5 \cos^3 t, y = 5 \sin^3 t$.

<details>
<summary>Ver solución</summary>
Astroide de radio 5.
</details>

---

### Ejercicio 4
En una cicloide, ¿qué pasa cuando $t=2\pi$?

<details>
<summary>Ver solución</summary>
Se completa una vuelta. El punto vuelve a tocar el suelo ($y=0$).
</details>

---

### Ejercicio 5
Diferencia entre Epi e Hipo cicloide.

<details>
<summary>Ver solución</summary>
Epi = Rueda por fuera (Externa). Hipo = Rueda por dentro (Interna).
</details>

---

### Ejercicio 6
Valor de $x$ en la Astroide ($a=1$) cuando $t=\pi/4$.

<details>
<summary>Ver solución</summary>
$x = \cos^3(45^\circ) = (\frac{\sqrt{2}}{2})^3 = \frac{2\sqrt{2}}{8} = \frac{\sqrt{2}}{4}$.
</details>

---

### Ejercicio 7
¿Qué curva genera un punto en el eje de la rueda ($b=0$)?

<details>
<summary>Ver solución</summary>
Una línea recta horizontal (el eje no sube ni baja).
</details>

---

### Ejercicio 8
Si $R=3r$ en una Epicicloide, ¿cuántos pétalos tiene?

<details>
<summary>Ver solución</summary>
3 pétalos.
</details>

---

### Ejercicio 9
Ecuación general de la Cicloide.

<details>
<summary>Ver solución</summary>
$x = r(t-\sin t), y = r(1-\cos t)$.
</details>

---

### Ejercicio 10
¿Qué figura tiene la propiedad de que una pelota rueda hasta el fondo en el mismo tiempo sin importar de qué altura la sueltes?

<details>
<summary>Ver solución</summary>
La Cicloide (Isocrona). Un péndulo cicloidal tiene periodo perfecto.
</details>

---

## 🔑 Resumen

| Curva | Mecanismo | Forma |
| :--- | :--- | :--- |
| **Cicloide** | Rueda en piso recto. | Arcos de puente. |
| **Epicicloide** | Rueda externa sobre círculo. | Flor inflada. |
| **Hipocicloide**| Rueda interna. | Estrella (puntas agudas). |
| **Astroide** | Hipocicloide 1:4. | Estrella de 4 puntas. |

> **Conclusión:** Estas curvas no son solo bonitas. La cicloide resolvió retos legendarios de la física y ayudó a Newton y Bernoulli a crear el cálculo de variaciones.
