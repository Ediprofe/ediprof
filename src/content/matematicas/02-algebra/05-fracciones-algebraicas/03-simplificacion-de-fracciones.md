# **Simplificación de Fracciones Algebraicas**

Simplificar una fracción algebraica es como reducir una fracción numérica: el objetivo es hacerla más sencilla dividiendo arriba y abajo por lo mismo. Si sabes que $\frac{4}{8}$ es lo mismo que $\frac{1}{2}$, ¡ya entiendes el concepto básico!

---

## 🎯 ¿Qué vas a aprender?

- El principio fundamental: solo se simplifican factores (multiplicaciones), no términos (sumas).
- A simplificar coeficientes y variables usando leyes de exponentes.
- A usar la factorización para reducir polinomios complejos.
- A evitar el error número 1 de los estudiantes: cancelar sumas.

---

## 🔍 La regla de oro

> **"Solo puedes cancelar lo que está multiplicando a todo el bloque."**

Si tienes una suma o resta, **¡PROHIBIDO CANCELAR!** Primero debes factorizar para convertir esas sumas en multiplicaciones.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Simplificación de monomios

Simplifica: $\dfrac{15x^3y^2}{25x^2y^4}$

**Datos:**
- Coeficientes: 15 y 25.
- Variables: $x$ y $y$.

**Razonamiento:**
1.  **Números:** Simplificamos $\frac{15}{25}$ dividiendo por 5 $\to \frac{3}{5}$.
2.  **Letras:** Restamos exponentes (el mayor "gana" y se queda en su lugar).
    *   $x$: Arriba 3, abajo 2. Gana arriba por 1. $\to x^1$ arriba.
    *   $y$: Arriba 2, abajo 4. Gana abajo por 2. $\to y^2$ abajo.

**Resultado:** $\boxed{\frac{3x}{5y^2}}$

---

### Ejemplo 2: Polinomio entre Monomio

Simplifica: $\dfrac{4x^2 + 8x}{2x}$

**Datos:**
- Arriba hay una suma. **¡No cancelar el $2x$ de arriba con el de abajo directamente!**

**Razonamiento:**
1.  Factorizamos el numerador (Factor común $4x$):
    $$4x^2 + 8x = 4x(x+2)$$
2.  Reescribimos la fracción:
    $$\frac{4x(x+2)}{2x}$$
3.  Ahora sí, $4x$ y $2x$ están multiplicando.
    *   $\frac{4}{2} = 2$.
    *   $\frac{x}{x} = 1$ (se van).

**Resultado:** $\boxed{2(x+2)}$

---

### Ejemplo 3: Diferencia de Cuadrados

Simplifica: $\dfrac{x^2 - 9}{x + 3}$

**Datos:**
- Numerador: $x^2 - 9$ (Diferencia de cuadrados).
- Denominador: $x + 3$.

**Razonamiento:**
1.  Factorizamos arriba:
    $$x^2 - 9 = (x - 3)(x + 3)$$
2.  Sustituimos:
    $$\frac{(x-3)(x+3)}{x+3}$$
3.  Cancelamos el bloque completo $(x+3)$.

**Resultado:** $\boxed{x - 3}$

---

### Ejemplo 4: Trinomios

Simplifica: $\dfrac{x^2 + 2x - 15}{x^2 - 9}$

**Datos:**
- Numerador: Trinomio de la forma $x^2+bx+c$.
- Denominador: Diferencia de cuadrados.

**Razonamiento:**
1.  Factorizamos numerador:
    *   Multiplican -15, suman 2: $(5, -3)$.
    *   $(x+5)(x-3)$.
2.  Factorizamos denominador:
    *   $(x+3)(x-3)$.
3.  Reescribimos:
    $$\frac{(x+5)(x-3)}{(x+3)(x-3)}$$
4.  Cancelamos $(x-3)$.

**Resultado:** $\boxed{\frac{x+5}{x+3}}$

---

### Ejemplo 5: Factorización de signo negativo (Truco avanzado)

Simplifica: $\dfrac{a - b}{b - a}$

**Datos:**
- Los términos son iguales pero con signos opuestos.

**Razonamiento:**
1.  Factorizamos un signo negativo en el denominador para invertirlo:
    $$b - a = -(-b + a) = -(a - b)$$
2.  Sustituimos:
    $$\frac{a - b}{-(a - b)}$$
3.  Cancelamos el bloque $(a-b)$.
4.  Queda: $\frac{1}{-1} = -1$.

**Resultado:** $\boxed{-1}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Simplifica $\dfrac{14a^2}{21a}$.

<details>
<summary>Ver solución</summary>

**Datos:** Simplificar 14/21 y $a^2/a$.
**Razonamiento:** 14/21 = 2/3. $a^2/a = a$.
**Resultado:** $\boxed{\frac{2a}{3}}$

</details>

### Ejercicio 2
Simplifica $\dfrac{3x + 12}{3}$.

<details>
<summary>Ver solución</summary>

**Datos:** Factor común 3 arriba.
**Razonamiento:** $\frac{3(x+4)}{3}$. Se van los 3.
**Resultado:** $\boxed{x+4}$

</details>

### Ejercicio 3
Simplifica $\dfrac{x^2 - x}{xy}$.

<details>
<summary>Ver solución</summary>

**Datos:** Factor común x arriba.
**Razonamiento:** $\frac{x(x-1)}{xy}$. Cancelamos x.
**Resultado:** $\boxed{\frac{x-1}{y}}$

</details>

### Ejercicio 4
Simplifica $\dfrac{5x - 5y}{x - y}$.

<details>
<summary>Ver solución</summary>

**Datos:** Factor común 5.
**Razonamiento:** $\frac{5(x-y)}{x-y} = 5$.
**Resultado:** $\boxed{5}$

</details>

### Ejercicio 5
Simplifica $\dfrac{x^2 - 16}{x - 4}$.

<details>
<summary>Ver solución</summary>

**Datos:** Dif. cuadrados.
**Razonamiento:** $\frac{(x+4)(x-4)}{x-4}$.
**Resultado:** $\boxed{x+4}$

</details>

### Ejercicio 6
Simplifica $\dfrac{x^2 + 5x + 6}{x + 2}$.

<details>
<summary>Ver solución</summary>

**Datos:** Trinomio.
**Razonamiento:** Num: $(x+3)(x+2)$. Den: $(x+2)$.
**Resultado:** $\boxed{x+3}$

</details>

### Ejercicio 7
Simplifica $\dfrac{2x - 4}{x^2 - 4}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Num: $2(x-2)$.
Den: $(x+2)(x-2)$.
Cancelamos $(x-2)$.
**Resultado:** $\boxed{\frac{2}{x+2}}$

</details>

### Ejercicio 8
Simplifica $\dfrac{a^2 - 2ab + b^2}{a^2 - b^2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Num: $(a-b)^2$.
Den: $(a+b)(a-b)$.
Cancelamos un $(a-b)$.
**Resultado:** $\boxed{\frac{a-b}{a+b}}$

</details>

### Ejercicio 9
Simplifica $\dfrac{3x - 6}{5x - 10}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Num: $3(x-2)$.
Den: $5(x-2)$.
**Resultado:** $\boxed{\frac{3}{5}}$

</details>

### Ejercicio 10
Simplifica $\dfrac{x^2 - 5x + 6}{x^2 - 4x + 4}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Num: $(x-3)(x-2)$.
Den: $(x-2)^2$.
Cancelamos un $(x-2)$.
**Resultado:** $\boxed{\frac{x-3}{x-2}}$

</details>

---

## 🔑 Resumen

| Paso | Acción |
| :--- | :--- |
| **1. Factorizar** | Convierte TODAS las sumas en multiplicaciones. |
| **2. Cancelar** | Elimina los bloques idénticos arriba y abajo. |
| **3. Resultado** | Escribe lo que quedó. |

> **Recuerda:** $\frac{x+5}{5}$ **NO** es $x+1$. El 5 divide a *todo*, no solo al 5.
