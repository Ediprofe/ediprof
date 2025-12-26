# **División de Fracciones Algebraicas**

¿Sabías que la división no existe realmente en el mundo de las fracciones? Todo es un truco de magia: convertimos la división en una multiplicación dándole la vuelta a la segunda fracción. Es como hacer judo con los números: usas la fuerza del oponente (la fracción divisora) invirtiéndola a tu favor.

---

## 🎯 ¿Qué vas a aprender?

- La regla del "inverso multiplicativo" (dar vuelta a la tortilla).
- Cómo transformar cualquier división en una multiplicación sencilla.
- A simplificar divisiones complejas con polinomios.
- El orden correcto para no equivocarse nunca.

---

## 🔍 La Técnica del "Giro"

Para dividir dos fracciones, simplemente **invertimos** la segunda fracción (el divisor) y cambiamos el signo $\div$ por $\times$.

$$
\frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \cdot \frac{D}{C}
$$

> **Regla vital:** Solo se invierte la fracción que está **después** del signo de división.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: División de Monomios

Divide: $\dfrac{4x^2}{3y} \div \dfrac{2x}{9y^2}$

**Datos:**
- Operación: División.
- Segunda fracción: $2x / 9y^2$.

**Razonamiento:**

1. **Invertimos** la segunda fracción: 

$$
\frac{9y^2}{2x}
$$

2. **Multiplicamos** normalmente:

$$
\frac{4x^2}{3y} \cdot \frac{9y^2}{2x}
$$

3. **Simplificamos** (Números con números, letras con letras):
   - $4/2 = 2$ y $9/3 = 3$. $\to 2 \cdot 3 = 6$.
   - $x^2/x = x$.
   - $y^2/y = y$.

**Resultado:** $\boxed{6xy}$

---

### Ejemplo 2: Polinomios Simples

Divide: $\dfrac{2x+6}{5} \div \dfrac{x+3}{10}$

**Datos:**
- Numerador factorizable: $2x+6$.

**Razonamiento:**

1. **Invertimos** la segunda: $\frac{10}{x+3}$.

2. Factorizamos la primera:

$$
\frac{2(x+3)}{5} \cdot \frac{10}{x+3}
$$

3. **Cancelamos** cruzado:
   - $(x+3)$ se va con $(x+3)$.
   - $10/5 = 2$.
   - Queda $2 \cdot 2 = 4$.

**Resultado:** $\boxed{4}$

---

### Ejemplo 3: Diferencia de Cuadrados

Divide: $\dfrac{x^2-16}{x+2} \div \dfrac{x-4}{x+2}$

**Datos:**
- $x^2-16 = (x+4)(x-4)$.

**Razonamiento:**

1. Convertimos a multiplicación:

$$
\frac{x^2-16}{x+2} \cdot \frac{x+2}{x-4}
$$

2. Factorizamos:

$$
\frac{(x+4)(x-4)}{x+2} \cdot \frac{x+2}{x-4}
$$

3. Cancelamos todo lo repetido (arriba-abajo):
   - $(x-4)$ con $(x-4)$.
   - $(x+2)$ con $(x+2)$.

4. Solo sobrevive $(x+4)$.

**Resultado:** $\boxed{x+4}$

---

### Ejemplo 4: Trinomios (¡El clásico de examen!)

Divide: $\dfrac{x^2+5x+6}{x-3} \div \dfrac{x+2}{x-3}$

**Datos:**
- $x^2+5x+6 = (x+3)(x+2)$.

**Razonamiento:**

1. Invertimos y escribimos como producto:

$$
\frac{x^2+5x+6}{x-3} \cdot \frac{x-3}{x+2}
$$

2. Factorizamos el trinomio:

$$
\frac{(x+3)(x+2)}{x-3} \cdot \frac{x-3}{x+2}
$$

3. Cancelación masiva:
   - $(x+2)$ con $(x+2)$.
   - $(x-3)$ con $(x-3)$.

**Resultado:** $\boxed{x+3}$

---

### Ejemplo 5: División de entero por fracción

Divide: $(x^2 - 9) \div \dfrac{x+3}{2}$

**Datos:**
- El primero parece un entero, pero es una fracción sobre 1: $\frac{x^2-9}{1}$.

**Razonamiento:**

1. Reescribimos e invertimos:

$$
\frac{x^2-9}{1} \cdot \frac{2}{x+3}
$$

2. Factorizamos:

$$
\frac{(x+3)(x-3)}{1} \cdot \frac{2}{x+3}
$$

3. Cancelamos $(x+3)$.

4. Queda: $2(x-3)$.

**Resultado:** $\boxed{2(x-3)}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Divide $\dfrac{10a^2}{3b} \div \dfrac{5a}{6b}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

Invierte $\to \frac{6b}{5a}$.

Simplifica: $10/5=2$, $6/3=2 \to 4$. 

$$
a^2/a=a \quad , \quad b/b=1
$$

**Resultado:** $\boxed{4a}$

</details>

### Ejercicio 2
Divide $\dfrac{3x}{y} \div 6x$.

<details>
<summary>Ver solución</summary>

**Datos:** $6x$ se invierte a $\frac{1}{6x}$.
**Razonamiento:** 

$$
\frac{3x}{y} \cdot \frac{1}{6x} = \frac{3x}{6xy} = \frac{1}{2y}
$$

**Resultado:** $\boxed{\frac{1}{2y}}$

</details>

### Ejercicio 3
Divide $\dfrac{x+5}{x-1} \div \dfrac{x+5}{2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\frac{x+5}{x-1} \cdot \frac{2}{x+5}
$$

Se van los $(x+5)$.

**Resultado:** $\boxed{\frac{2}{x-1}}$

</details>

### Ejercicio 4
Divide $\dfrac{x^2-1}{x} \div \dfrac{x+1}{x}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\frac{(x+1)(x-1)}{x} \cdot \frac{x}{x+1}
$$

Queda $x-1$.

**Resultado:** $\boxed{x-1}$

</details>

### Ejercicio 5
Divide $\dfrac{4x-8}{3} \div \dfrac{x-2}{6}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\frac{4(x-2)}{3} \cdot \frac{6}{x-2}
$$

Cancelamos $(x-2)$. 

$$
4 \cdot 2 = 8
$$

**Resultado:** $\boxed{8}$

</details>

### Ejercicio 6
Divide $\dfrac{x^2-2x+1}{x^2+x} \div \dfrac{x-1}{x}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\frac{(x-1)^2}{x(x+1)} \cdot \frac{x}{x-1}
$$

Se va un $(x-1)$ y la $x$.

**Resultado:** $\boxed{\frac{x-1}{x+1}}$

</details>

### Ejercicio 7
Divide $\dfrac{a^2-b^2}{2} \div (a+b)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\frac{(a+b)(a-b)}{2} \cdot \frac{1}{a+b}
$$

**Resultado:** $\boxed{\frac{a-b}{2}}$

</details>

### Ejercicio 8
Divide $\dfrac{1}{x^2-9} \div \dfrac{1}{x-3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\frac{1}{(x+3)(x-3)} \cdot \frac{x-3}{1}
$$

**Resultado:** $\boxed{\frac{1}{x+3}}$

</details>

### Ejercicio 9
Divide $\dfrac{x^2+7x+12}{x} \div \dfrac{x+4}{2x}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\frac{(x+4)(x+3)}{x} \cdot \frac{2x}{x+4}
$$

Cancelamos $(x+4)$ y $x$. Queda $2(x+3)$.

**Resultado:** $\boxed{2x+6}$

</details>

### Ejercicio 10
Divide $\dfrac{x^3}{y^2} \div \dfrac{x^2}{y^3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\frac{x^3}{y^2} \cdot \frac{y^3}{x^2} = x \cdot y
$$

**Resultado:** $\boxed{xy}$

</details>

---

## 🔑 Resumen

| Operación | Acción Clave |
| :--- | :--- |
| **Multiplicación** | Directo ($\to$) |
| **División** | Invertir el segundo y multiplicar ($\times \leftrightarrow$) |

> Recuerda: Divide y vencerás... ¡pero invirtiendo primero!
