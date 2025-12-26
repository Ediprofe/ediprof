# **Trinomio de la forma ax² + bx + c**

En lecciones anteriores aprendimos a factorizar trinomios donde el coeficiente de $x^2$ es 1. Ahora veremos qué hacer cuando ese coeficiente es diferente de 1. Existen dos métodos principales para resolver este tipo de trinomios.

---

## 🎯 ¿Qué vas a aprender?

- A identificar trinomios con coeficiente principal distinto de 1.
- El **Método de Agrupación** para factorizar paso a paso.
- El **Método de Tanteo** para factorizar de forma rápida.
- A elegir el mejor método según el problema.

---

## 🏗️ Método 1: Agrupación

Este es el método más ordenado y confiable. Consiste en convertir el trinomio de 3 términos en un polinomio de 4 términos para poder aplicar factor común por agrupación.

### Pasos del Método de Agrupación

1. Multiplica el primer coeficiente ($a$) por el último ($c$). A esto le llamamos "Producto AC".
2. Busca dos números que **multiplicados** den el Producto AC y **sumados** den $b$.
3. Reescribe el trinomio abriendo el término central con esos dos números.
4. Factoriza por agrupación (factor común por parejas).

---

### Ejemplo 1: Agrupación básica

Factoriza: $2x^2 + 7x + 3$

**Datos:**
- $a = 2$, $b = 7$, $c = 3$
- Producto AC = $2 \times 3 = 6$

**Razonamiento:**
1. Buscamos números que multipliquen 6 y sumen 7. Son **6** y **1**.
2. Abrimos el centro: $2x^2 + 6x + x + 3$.
3. Agrupamos: $(2x^2 + 6x) + (x + 3)$.
4. Factor común: $2x(x + 3) + 1(x + 3)$.
5. El bloque $(x + 3)$ es común.

**Resultado:** $\boxed{(x + 3)(2x + 1)}$

---

### Ejemplo 2: Agrupación con signos negativos

Factoriza: $3x^2 - 10x + 8$

**Datos:**
- Producto AC = $3 \times 8 = 24$
- Necesitamos que sumen $-10$ y multipliquen $+24$

**Razonamiento:**
1. Ambos números deben ser negativos: **-6** y **-4**.
2. Abrimos: $3x^2 - 6x - 4x + 8$.
3. Agrupamos: $3x(x - 2) - 4(x - 2)$.
4. Al sacar el -4, el signo interno cambia.

**Resultado:** $\boxed{(x - 2)(3x - 4)}$

---

### Ejemplo 3: Agrupación con término negativo al final

Factoriza: $2x^2 + 3x - 2$

**Datos:**
- Producto AC = $2 \times (-2) = -4$
- Necesitamos que sumen $+3$ y multipliquen $-4$

**Razonamiento:**
1. Números con signos diferentes: **+4** y **-1**.
2. Abrimos: $2x^2 + 4x - x - 2$.
3. Agrupamos: $2x(x + 2) - 1(x + 2)$.

**Resultado:** $\boxed{(x + 2)(2x - 1)}$

---

## 🏗️ Método 2: Tanteo

Este método consiste en probar combinaciones de factores hasta encontrar la correcta. Es más rápido cuando los coeficientes son pequeños.

### Pasos del Método de Tanteo

1. Descompón el primer término ($ax^2$) en dos factores.
2. Descompón el último término ($c$) en dos factores.
3. Prueba combinaciones multiplicando en cruz.
4. Si la suma de los productos cruzados da el término central, encontraste los factores.

---

### Ejemplo 4: Tanteo básico

Factoriza: $2x^2 + 5x + 2$

**Datos:**
- Factores de $2x^2$: $(2x)$ y $(x)$
- Factores de $2$: $(1)$ y $(2)$

**Razonamiento:**
1. Probamos: $(2x + 1)(x + 2)$.
2. Verificamos en cruz: $2x \cdot 2 = 4x$ y $x \cdot 1 = x$.
3. Suma: $4x + x = 5x$. ¡Coincide con el centro!

**Resultado:** $\boxed{(2x + 1)(x + 2)}$

---

### Ejemplo 5: Tanteo con signos diferentes

Factoriza: $3x^2 - 5x - 2$

**Datos:**
- Factores de $3x^2$: $(3x)$ y $(x)$
- Factores de $-2$: $(1)$ y $(-2)$ o $(-1)$ y $(2)$

**Razonamiento:**
1. Probamos: $(3x + 1)(x - 2)$.
2. Verificamos: $3x \cdot (-2) = -6x$ y $x \cdot 1 = x$.
3. Suma: $-6x + x = -5x$. ¡Correcto!

**Resultado:** $\boxed{(3x + 1)(x - 2)}$

---

### Ejemplo 6: Combinando con factor común

Factoriza completamente: $6x^2 + 15x + 9$

**Datos:**
- Todos los coeficientes (6, 15, 9) son divisibles por 3.

**Razonamiento:**
1. Sacamos factor común 3: $3(2x^2 + 5x + 3)$.
2. Factorizamos el trinomio interno por tanteo o agrupación.
3. Probamos: $(2x + 3)(x + 1)$. Verificación: $2x + 3x = 5x$. ✓

**Resultado:** $\boxed{3(2x + 3)(x + 1)}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Factoriza usando Agrupación: $2x^2 + 9x + 4$

<details>
<summary>Ver solución</summary>

**Datos:** AC = 8. Números: 8 y 1.
**Razonamiento:** $2x^2 + 8x + x + 4 = 2x(x+4) + 1(x+4)$.
**Resultado:** $\boxed{(x + 4)(2x + 1)}$

</details>

### Ejercicio 2
Factoriza usando Tanteo: $3x^2 + 7x + 2$

<details>
<summary>Ver solución</summary>

**Datos:** Factores $(3x, x)$ y $(1, 2)$.
**Razonamiento:** $3x(2) + x(1) = 7x$. Coincide.
**Resultado:** $\boxed{(3x + 1)(x + 2)}$

</details>

### Ejercicio 3
Factoriza: $2x^2 + 11x + 5$

<details>
<summary>Ver solución</summary>

**Datos:** AC = 10. Números: 10 y 1.
**Razonamiento:** $2x(x+5) + 1(x+5)$.
**Resultado:** $\boxed{(x + 5)(2x + 1)}$

</details>

### Ejercicio 4
Factoriza: $6x^2 - 7x + 2$

<details>
<summary>Ver solución</summary>

**Datos:** AC = 12. Números: -4 y -3.
**Razonamiento:** $6x^2 - 4x - 3x + 2 = 2x(3x-2) - 1(3x-2)$.
**Resultado:** $\boxed{(3x - 2)(2x - 1)}$

</details>

### Ejercicio 5
Factoriza: $5x^2 + 7x + 2$

<details>
<summary>Ver solución</summary>

**Datos:** AC = 10. Números: 5 y 2.
**Razonamiento:** $5x(x+1) + 2(x+1)$.
**Resultado:** $\boxed{(x + 1)(5x + 2)}$

</details>

### Ejercicio 6
Factoriza: $4x^2 - 15x - 4$

<details>
<summary>Ver solución</summary>

**Datos:** Tanteo: $(4x, x)$ y $(1, -4)$.
**Razonamiento:** $4x(-4) + x(1) = -15x$.
**Resultado:** $\boxed{(4x + 1)(x - 4)}$

</details>

### Ejercicio 7
Factoriza: $3x^2 - 14x - 5$

<details>
<summary>Ver solución</summary>

**Datos:** AC = -15. Números: -15 y 1.
**Razonamiento:** $3x(x-5) + 1(x-5)$.
**Resultado:** $\boxed{(x - 5)(3x + 1)}$

</details>

### Ejercicio 8
Factoriza: $2x^2 - 5x - 3$

<details>
<summary>Ver solución</summary>

**Datos:** Tanteo: $(2x, x)$ y $(1, -3)$.
**Razonamiento:** $2x(-3) + x(1) = -5x$.
**Resultado:** $\boxed{(2x + 1)(x - 3)}$

</details>

### Ejercicio 9
Factoriza: $6x^2 + x - 2$

<details>
<summary>Ver solución</summary>

**Datos:** AC = -12. Números: 4 y -3.
**Razonamiento:** $2x(3x+2) - 1(3x+2)$.
**Resultado:** $\boxed{(3x + 2)(2x - 1)}$

</details>

### Ejercicio 10
Factoriza sacando primero factor común: $4x^2 + 18x + 8$

<details>
<summary>Ver solución</summary>

**Datos:** Factor común 2.
**Razonamiento:** $2(2x^2 + 9x + 4)$. Adentro: $(2x+1)(x+4)$.
**Resultado:** $\boxed{2(2x + 1)(x + 4)}$

</details>

---

## 🔑 Resumen

| Método | Cuándo usarlo | Ventaja |
| :--- | :--- | :--- |
| **Agrupación** | Cuando los números son grandes o no ves la respuesta rápido | Siempre funciona |
| **Tanteo** | Cuando los coeficientes son pequeños | Más rápido |

> Ambos métodos dan el mismo resultado. Elige el que te resulte más cómodo según el problema. Lo importante es verificar siempre multiplicando los factores.
