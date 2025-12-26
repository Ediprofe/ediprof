# **Fracciones Complejas**

Una fracción compleja no es más que una fracción que tiene... ¡más fracciones dentro! Puede parecer un edificio de varios pisos inestable, pero con la técnica adecuada, podemos colapsar todos esos pisos en una simple fracción de "un solo piso" (numerador y denominador simples).

---

## 🎯 ¿Qué vas a aprender?

- Cómo identificar una fracción compleja.
- El método de "División de Fracciones" (El Sándwich).
- El método del MCM para simplificar todo de un solo golpe.
- Estrategias para resolver fracciones "escalonadas" (torres de fracciones).

---

## 🔍 Dos Métodos para Resolver

1.  **Método del Sándwich (Oreja):** Tratas al numerador y denominador como fracciones separadas, las unificas y luego multiplicas extremos por medios.
    $$ \frac{\frac{A}{B}}{\frac{C}{D}} = \frac{A \cdot D}{B \cdot C} $$
2.  **Método del MCM (Recomendado):** Multiplicas TODO (arriba y abajo) por el MCM de las fracciones pequeñas para eliminarlas al instante.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Fracción sobre Fracción (Sándwich)

Simplifica: $\dfrac{\frac{3}{4}}{\frac{5}{7}}$

**Datos:**
- Extremos: 3 y 7.
- Medios: 4 y 5.

**Razonamiento:**
1.  Multiplicamos extremos (van arriba): $3 \cdot 7 = 21$.
2.  Multiplicamos medios (van abajo): $4 \cdot 5 = 20$.
3.  ¿Se puede simplificar? No.

**Resultado:** $\boxed{\frac{21}{20}}$

---

### Ejemplo 2: Método del Sándwich con Variables

Simplifica: $\dfrac{\frac{2x}{y^2}}{\frac{6x^2}{y}}$

**Datos:**
- Extremos: $2x$ y $y$.
- Medios: $y^2$ y $6x^2$.

**Razonamiento:**
1.  Aplicamos la regla:
    $$\frac{2x \cdot y}{y^2 \cdot 6x^2}$$
2.  Simplificamos:
    *   Números: $2/6 = 1/3$.
    *   $x$: $x/x^2 = 1/x$.
    *   $y$: $y/y^2 = 1/y$.
3.  Juntamos: $\frac{1}{3xy}$.

**Resultado:** $\boxed{\frac{1}{3xy}}$

---

### Ejemplo 3: Sumas en el numerador (Método MCM)

Simplifica: $\dfrac{1 + \frac{1}{x}}{1 - \frac{1}{x}}$

**Datos:**
- Denominador pequeño: $x$. MCM = $x$.

**Razonamiento:**
1.  Multiplicamos TODO (arriba y abajo) por $x$:
    $$\frac{x(1) + x(\frac{1}{x})}{x(1) - x(\frac{1}{x})}$$
2.  Operamos:
    *   $x \cdot 1 = x$.
    *   $x \cdot \frac{1}{x} = 1$.
3.  Queda:
    $$\frac{x+1}{x-1}$$

**Resultado:** $\boxed{\frac{x+1}{x-1}}$

---

### Ejemplo 4: Fracciones Algebraicas Mixtas

Simplifica: $\dfrac{\frac{1}{a} + \frac{1}{b}}{\frac{a}{b} - \frac{b}{a}}$

**Datos:**
- Denominadores pequeños: $a, b$.
- MCM de todos: $ab$.

**Razonamiento:**
1.  Multiplicamos todo por $ab$:
    $$\frac{ab(\frac{1}{a}) + ab(\frac{1}{b})}{ab(\frac{a}{b}) - ab(\frac{b}{a})}$$
2.  Simplificamos cada término:
    *   Numerador: $b + a$.
    *   Denominador: $a^2 - b^2$.
3.  Queda:
    $$\frac{a+b}{a^2-b^2}$$
4.  Factorizamos el denominador (Diferencia de cuadrados):
    $$\frac{a+b}{(a+b)(a-b)}$$
5.  Cancelamos $(a+b)$.

**Resultado:** $\boxed{\frac{1}{a-b}}$

---

### Ejemplo 5: Fracciones Escalonadas (Torres)

Simplifica: $1 + \dfrac{1}{1 + \dfrac{1}{x}}$

**Datos:**
- Resolvemos de abajo hacia arriba.

**Razonamiento:**
1.  **Paso 1 (Abajo):** $1 + \frac{1}{x} = \frac{x+1}{x}$.
2.  **Sustituimos:**
    $$1 + \frac{1}{\frac{x+1}{x}}$$
3.  **Paso 2 (Invertir):** Uno sobre una fracción es la fracción invertida.
    $$1 + \frac{x}{x+1}$$
4.  **Paso 3 (Suma final):**
    $$\frac{x+1 + x}{x+1} = \frac{2x+1}{x+1}$$

**Resultado:** $\boxed{\frac{2x+1}{x+1}}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Simplifica $\dfrac{\frac{a}{b}}{\frac{c}{d}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Extremos $ad$, medios $bc$.
**Resultado:** $\boxed{\frac{ad}{bc}}$

</details>

### Ejercicio 2
Simplifica $\dfrac{\frac{x}{2}}{\frac{x}{3}}$.

<details>
<summary>Ver solución</summary>
**Razonamiento:** $\frac{3x}{2x} = \frac{3}{2}$.
**Resultado:** $\boxed{\frac{3}{2}}$
</details>

### Ejercicio 3
Simplifica $\dfrac{1 - \frac{1}{2}}{3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** $1 - 1/2 = 1/2$. $\frac{1/2}{3} = \frac{1}{6}$.
**Resultado:** $\boxed{\frac{1}{6}}$

</details>

### Ejercicio 4
Simplifica $\dfrac{\frac{1}{x} + 1}{\frac{1}{x}}$.

<details>
<summary>Ver solución</summary>
**Razonamiento:** Mult todo por $x$.
$(1 + x) / 1$.
**Resultado:** $\boxed{x+1}$
</details>

### Ejercicio 5
Simplifica $\dfrac{\frac{1}{x} - \frac{1}{y}}{x-y}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Num: $\frac{y-x}{xy}$.
Div: $\frac{y-x}{xy(x-y)} = \frac{-(x-y)}{xy(x-y)}$.
**Resultado:** $\boxed{-\frac{1}{xy}}$

</details>

### Ejercicio 6
Simplifica $\dfrac{x + \frac{x}{y}}{y + \frac{y}{x}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Mult todo por $xy$.
Num: $xy^2 + x^2y = xy(y+x)$.
Den: $xy^2 + y^2$ (espera, al multiplicar por $xy$: $xy(y) + xy(y/x) = xy^2 + y^2$. Error en cálculo rápido, hagámoslo lento.
MCM $xy$.
Num: $x(xy) + x(x) = x^2y + x^2$? No, $x(xy)$ sumado.
Mejor por partes:
Num $\frac{xy+x}{y}$. Den $\frac{xy+y}{x}$.
Prod: $\frac{x(xy+x)}{y(xy+y)} = \frac{x^2(y+1)}{y^2(x+1)}$. No se ve simple.
Probemos MCM $xy$:
Num: $x(xy) + x(x) = x^2y + x^2 = x^2(y+1)$.
Den: $y(xy) + y(y) = xy^2 + y^2 = y^2(x+1)$.
**Resultado:** $\boxed{\frac{x^2(y+1)}{y^2(x+1)}}$

</details>

### Ejercicio 7
Simplifica $2 - \dfrac{3}{1 - \frac{1}{x}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** $1 - 1/x = \frac{x-1}{x}$.
Invierte: $\frac{3x}{x-1}$.
Resta: $2 - \frac{3x}{x-1} = \frac{2x-2-3x}{x-1} = \frac{-x-2}{x-1}$.
**Resultado:** $\boxed{\frac{-(x+2)}{x-1}}$

</details>

### Ejercicio 8
Simplifica $\dfrac{\frac{x^2}{y^2} - 1}{\frac{x}{y} + 1}$.

<details>
<summary>Ver solución</summary>
**Razonamiento:** Mult por $y^2$.
Num: $x^2 - y^2$. Den: $xy + y^2 = y(x+y)$.
$\frac{(x+y)(x-y)}{y(x+y)}$.
**Resultado:** $\boxed{\frac{x-y}{y}}$
</details>

### Ejercicio 9
Simplifica $\dfrac{\frac{1}{x+h} - \frac{1}{x}}{h}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Num: $\frac{x - (x+h)}{x(x+h)} = \frac{-h}{x(x+h)}$.
Div por $h$: Se va la $h$.
**Resultado:** $\boxed{\frac{-1}{x(x+h)}}$

</details>

### Ejercicio 10
Simplifica $\dfrac{x^{-1} + y^{-1}}{x^{-1}y^{-1}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{1/x + 1/y}{1/xy}$.
Mult por $xy$.
Num: $y + x$. Den: $1$.
**Resultado:** $\boxed{x+y}$

</details>

---

## 🔑 Resumen

| Método | Cuándo usarlo |
| :--- | :--- |
| **Sándwich** | Cuando es una sola fracción dividida entre otra sola fracción. |
| **MCM** | Cuando hay sumas o restas de fracciones dentro. |

> ¡No te asustes por la altura de la torre! Rompe el problema piso por piso, simplificando siempre que puedas.
