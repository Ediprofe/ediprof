# **Ecuación General de la Hipérbola**

Cuando desarrollamos los binomios al cuadrado, los bonitos paréntesis desaparecen y nos queda una larga cadena de términos. Esa es la Ecuación General. Aprenderemos a reconocerla y a devolverla a su forma útil.

---

## 🎯 ¿Qué vas a aprender?

- Reconocer $Ax^2 - Cy^2...$ (Signos opuestos).
- Completar cuadrados con cuidado con los signos negativos.
- Convertir de General a Ordinaria.

---

## 🔍 Identikit de la Hipérbola

$$ Ax^2 + Cy^2 + Dx + Ey + F = 0 $$

**Condición Única:**
$A$ y $C$ tienen **SIGNOS OPUESTOS**. (Uno es positivo y el otro negativo).
*   Si $A > 0, C < 0$: Probablemente Horizontal.
*   Si $C > 0, A < 0$: Probablemente Vertical.

---

## 🔄 El Arte de Completar Cuadrados (Nivel Difícil)

El proceso es igual al de la elipse, pero con una trampa mortal: **El signo menos**.

**Algoritmo:**
1.  **Agrupar:** X con X, Y con Y.
2.  **Factorizar:** Sacar el coeficiente principal ($A$ y $C$) ¡CON SU SIGNO!
    *   *Peligro:* Si factorizas un negativo (ej. $-4$), los signos de adentro cambian.
3.  **Completar:** Sumar $(\text{mitad})^2$ adentro. Ajustar afuera.
4.  **Dividir:** Igualar a 1.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Conversión Cuidadosa
$$ 9x^2 - 4y^2 - 18x - 16y - 43 = 0 $$

1.  **Agrupar:**
    $$ (9x^2 - 18x) + (-4y^2 - 16y) = 43 $$
2.  **Factorizar:** (¡Ojo con el -4!)
    $$ 9(x^2 - 2x) - 4(y^2 + 4y) = 43 $$
    *(Nota cómo $-16y$ se volvió $+4y$ al sacar el $-4$)*.
3.  **Completar:**
    *   $(x)$: Mitad de -2 es -1, cuad 1. Agrego $9 \times 1 = 9$.
    *   $(y)$: Mitad de 4 es 2, cuad 4. Agrego $-4 \times 4 = -16$.
    $$ 9(x-1)^2 - 4(y+2)^2 = 43 + 9 - 16 $$
    $$ 9(x-1)^2 - 4(y+2)^2 = 36 $$
4.  **Dividir por 36:**
    $$ \frac{(x-1)^2}{4} - \frac{(y+2)^2}{9} = 1 $$
    *   **Resultado:** Horizontal, Centro $(1, -2)$, $a=2, b=3$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica: $4x^2 - 9y^2 - 36 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Signos opuestos en cuadrados.

**Respuesta:** **Hipérbola**
</details>

---

### Ejercicio 2
Identifica: $-x^2 + 4y^2 = 4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Signos opuestos. (Vertical).

**Respuesta:** **Hipérbola**
</details>

---

### Ejercicio 3
Factoriza $-9y^2 + 18y$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$-9(y^2 - 2y)$.

**Respuesta:** $\boxed{-9(y^2 - 2y)}$
</details>

---

### Ejercicio 4
Completa el cuadrado para $x^2 - 6x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(x-3)^2 - 9$.

**Respuesta:** $\boxed{(x-3)^2}$
</details>

---

### Ejercicio 5
Calcula el ajuste derecho de $-4(y^2 + 4y + 4)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$-4 \times 4 = -16$.

**Respuesta:** $\boxed{-16}$
</details>

---

### Ejercicio 6
Convierte $x^2 - y^2 = 9$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2/9 - y^2/9 = 1$.

**Respuesta:** $\boxed{\frac{x^2}{9} - \frac{y^2}{9} = 1}$
</details>

---

### Ejercicio 7
Si al completar da 0 al lado derecho ($=0$), ¿qué es?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Son dos rectas que se cruzan (Asíntotas).

**Respuesta:** **Dos rectas (Hipérbola degenerada)**
</details>

---

### Ejercicio 8
Centro de $4(x-2)^2 - 9(y+5)^2 = 36$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(2, -5)$.

**Respuesta:** $\boxed{(2, -5)}$
</details>

---

### Ejercicio 9
Identifica: $x^2 + y^2 - 4 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Signos iguales y coeficientes iguales.

**Respuesta:** **Circunferencia**
</details>

---

### Ejercicio 10
Si $A=0$ en la general, ¿es hipérbola?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No, sería una parábola (una sola cuadrática).

**Respuesta:** **Parábola**
</details>

---

## 🔑 Resumen

| Paso Crítico | Error Frecuente |
| :--- | :--- |
| **Factorizar Negativo** | Olvidar cambiar el signo del término lineal. |
| **Sumar Ajuste** | Olvidar que el número sumado es negativo porque se multiplica por el factor de afuera. |

> **Conclusión:** El signo negativo es traicionero. Cuando factorices un menos, enciende todas tus alarmas y revisa los signos dos veces.
