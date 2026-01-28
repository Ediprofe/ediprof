---
title: "Ecuación General de la Elipse"
---

# **Ecuación General de la Elipse**

Esta es la forma "sin paréntesis" de la elipse. Es útil para las computadoras pero terrible para los humanos porque esconde el centro y el tamaño. Aquí aprenderemos a "domarla" para que nos revele sus secretos.

---

## 🎯 ¿Qué vas a aprender?

- Reconocer $Ax^2 + Cy^2...$ (Signos iguales, números distintos).
- Completar cuadrados dobles (en X y en Y).
- Convertirla a la forma ordinaria.

---

## 🔍 Identikit de la Elipse

En la ecuación general $Ax^2 + Cy^2 + Dx + Ey + F = 0$:

1.  **Ambos al cuadrado:** Existen $x^2$ y $y^2$. (No es parábola).
2.  **Mismo signo:** $A$ y $C$ son ambos positivos (o ambos negativos). (Si fueran opuestos, sería hipérbola).
3.  **Coeficientes distintos:** $A \neq C$. (Si fueran iguales, sería circunferencia).

> **Ejemplo:** $4x^2 + 9y^2...$ es Elipse. $5x^2 + 5y^2...$ es Círculo.

---

## 🔄 El Proceso de Conversión

Debemos pasar de:
$$ Ax^2 + Cy^2 + Dx + Ey + F = 0 $$
A:
$$ \frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1 $$

**Algoritmo:**
1.  **Agrupar:** Las X con las X, las Y con las Y. El número suelto al otro lado.
2.  **Factorizar:** Saca el coeficiente principal ($A$ y $C$) como factor común.
3.  **Completar Cuadrados:** Suma $(\text{mitad})^2$ dentro del paréntesis. ¡OJO! Al sumar adentro, estás sumando (coeficiente $\times$ valor) al total. Equilibra la ecuación.
4.  **Dividir:** Divide todo por el número de la derecha para obtener un "1".

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Conversión Completa
$$ 4x^2 + 9y^2 - 16x + 18y - 11 = 0 $$

1.  **Agrupar:**
    $$ (4x^2 - 16x) + (9y^2 + 18y) = 11 $$
2.  **Factorizar:**
    $$ 4(x^2 - 4x) + 9(y^2 + 2y) = 11 $$
3.  **Completar:**
    *   Mitad de -4 es -2, cuadrado 4. (Sumo $4 \times 4 = 16$ a la derecha).
    *   Mitad de 2 es 1, cuadrado 1. (Sumo $9 \times 1 = 9$ a la derecha).
    $$ 4(x^2 - 4x + 4) + 9(y^2 + 2y + 1) = 11 + 16 + 9 $$
    $$ 4(x-2)^2 + 9(y+1)^2 = 36 $$
4.  **Dividir por 36:**
    $$ \frac{4(x-2)^2}{36} + \frac{9(y+1)^2}{36} = 1 $$
    $$ \frac{(x-2)^2}{9} + \frac{(y+1)^2}{4} = 1 $$
    *   **Resultado:** Elipse Horizontal, Centro $(2, -1)$, $a=3, b=2$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica la cónica: $2x^2 + 2y^2 - 4x = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Coeficientes iguales ($A=C=2$).

**Respuesta:** **Circunferencia**
</details>

---

### Ejercicio 2
Identifica: $4x^2 - 9y^2 = 36$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Signos opuestos ($+4, -9$).

**Respuesta:** **Hipérbola**
</details>

---

### Ejercicio 3
Factoriza coeficientes en: $25x^2 - 100x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$25(x^2 - 4x)$.

**Respuesta:** $\boxed{25(x^2 - 4x)}$
</details>

---

### Ejercicio 4
Completa el cuadrado: $x^2 + 6x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Mitad 3, cuadrado 9. $(x+3)^2 - 9$.

**Respuesta:** $\boxed{(x+3)^2}$
</details>

---

### Ejercicio 5
Calcula el lado derecho si sumas dentro: $4(x^2 + ... + 4)$

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Estás sumando $4 \times 4 = 16$.

**Respuesta:** $\boxed{16}$
</details>

---

### Ejercicio 6
Convierte $x^2 + 4y^2 = 4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Divide por 4.

**Respuesta:** $\boxed{\frac{x^2}{4} + \frac{y^2}{1} = 1}$
</details>

---

### Ejercicio 7
Centro de $2(x-1)^2 + 3(y+2)^2 = 10$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Paréntesis $(x-1)$ y $(y+2)$.

**Respuesta:** $\boxed{(1, -2)}$
</details>

---

### Ejercicio 8
Si al final el lado derecho es negativo, ¿qué pasa?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Suma de cuadrados no puede dar negativo.

**Respuesta:** **Elipse Imaginaria (No existe)**
</details>

---

### Ejercicio 9
Si al final el lado derecho es 0, ¿qué pasa?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Solo existe un punto (el centro).

**Respuesta:** **Punto**
</details>

---

### Ejercicio 10
¿Qué pasa si $F=0$ en la general?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El origen $(0,0)$ satisface la ecuación. La elipse pasa por el origen.

**Respuesta:** **Pasa por el Origen**
</details>

---

## 🔑 Resumen

| Paso Crítico | Error Común |
| :--- | :--- |
| **Factorizar** | Olvidar dividir el término lineal ($x$ o $y$) por el factor común. |
| **Sumar derecha** | Olvidar multiplicar lo que agregaste por el número de afuera del paréntesis. |

> **Conclusión:** La conversión es mecánica. Si sigues el algoritmo (Agrupar-Factorizar-Completar-Dividir) disciplinadamente, la ecuación general se rendirá ante ti.
