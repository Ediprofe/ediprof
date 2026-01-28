---
title: "Fracciones Complejas"
---

# **Fracciones Complejas**

Una fracción compleja no es más que una fracción que tiene... ¡más fracciones dentro! Puede parecer un edificio de varios pisos inestable, pero con la técnica adecuada, podemos colapsar todos esos pisos en una simple fracción de "un solo piso" (numerador y denominador simples).

---

## 🎯 ¿Qué vas a aprender?

- El método de la "Oreja" (Sándwich) para casos simples.
- El método del MCM para simplificar expresiones con sumas y restas.
- Cómo resolver "torres" de fracciones (fracciones escalonadas).
- A simplificar el resultado final usando factorización.

---

## 👂 Método 1: Del Sándwich (La Oreja)

Este método es ideal cuando tienes **una sola fracción arriba y una sola fracción abajo**. Se basa en multiplicar los extremos por los medios.

**Gráficamente se ve así:**

$$
\left. \frac{ \overbrace{ \frac{\color{blue}{A}}{\color{red}{B}} }^{ \text{Extremo} } }{ \underbrace{ \frac{\color{red}{C}}{\color{blue}{D}} }_{ \text{Medio} } } \right\}
\quad \longrightarrow \quad
\boxed{\frac{\color{blue}{A} \cdot \color{blue}{D}}{\color{red}{B} \cdot \color{red}{C}}}
$$

1.  **Oreja Grande (Extremos):** Une el de hasta arriba ($\color{blue}A$) con el de hasta abajo ($\color{blue}D$). Su producto va **ARRIBA**.
2.  **Oreja Chica (Medios):** Une los dos del centro ($\color{red}B$ y $\color{red}C$). Su producto va **ABAJO**.

---

### ⚙️ Ejemplos: El Método de la Oreja

#### Ejemplo 1: Con números simples
Simplifica: $\dfrac{\frac{3}{4}}{\frac{5}{7}}$

**Razonamiento:**
1. Extremos (Oreja grande): $3 \cdot 7 = 21$.
2. Medios (Oreja chica): $4 \cdot 5 = 20$.

**Resultado:** $\boxed{\frac{21}{20}}$

#### Ejemplo 2: Con variables y monomios
Simplifica: $\dfrac{\frac{2x}{y^2}}{\frac{6x^2}{y}}$

**Razonamiento:**
1. Aplicamos la regla:
   
$$
\frac{2x \cdot y}{y^2 \cdot 6x^2}
$$

2. Simplificamos términos:
   - $2/6 = 1/3$.
   - $x/x^2 = 1/x$.
   - $y/y^2 = 1/y$.

**Resultado:** $\boxed{\frac{1}{3xy}}$

#### Ejemplo 3: Oreja con binomios (Simplificación)
Simplifica: $\dfrac{\frac{x+1}{3}}{\frac{x^2-1}{6}}$

**Razonamiento:**
1. Multiplicamos extremos y medios:
   
$$
\frac{6(x+1)}{3(x^2-1)}
$$

2. Factorizamos el denominador ($x^2-1$ es diferencia de cuadrados):
   
$$
\frac{6(x+1)}{3(x+1)(x-1)}
$$

3. Simplificamos: $6/3=2$ y cancelamos $(x+1)$.

**Resultado:** $\boxed{\frac{2}{x-1}}$

#### Ejemplo 4: Entero dividido por Fracción
Simplifica: $\dfrac{2a}{\frac{a}{b}}$

**Razonamiento:**
1. Imagina que el $2a$ tiene un 1 debajo: $\frac{2a}{1} / \frac{a}{b}$.
2. Oreja Grande: $2a \cdot b = 2ab$.
3. Oreja Chica: $1 \cdot a = a$.
4. Queda: $\frac{2ab}{a}$. Se cancela la "a".

**Resultado:** $\boxed{2b}$

---

## 🚀 Método 2: Del MCM (El Profesional)

Este método es mucho más potente y rápido cuando tienes **sumas o restas dentro** de la fracción compleja. En lugar de resolver arriba y abajo por separado, eliminamos todos los denominadores pequeños de un solo golpe.

**El Proceso:**
1. Encuentra el **MCM** de todos los denominadores "pequeños" (los que están dentro de las fracciones internas).
2. Multiplica cada término (individualmente) del numerador y denominador por ese MCM.
3. ¡Simplifica lo que queda!

---

### ⚙️ Ejemplos: El Método del MCM

#### Ejemplo 5: Variable simple
Simplifica: $\dfrac{1 + \frac{1}{x}}{1 - \frac{1}{x}}$

**Razonamiento:**
1. Los denominadores pequeños son $x$. El MCM es $x$.
2. Multiplicamos cada término de arriba y de abajo por $x$:
   
$$
\frac{x(1) + x(\frac{1}{x})}{x(1) - x(\frac{1}{x})}
$$

3. Al multiplicar $x \cdot \frac{1}{x}$, la $x$ desaparece y queda 1:
   
$$
\frac{x + 1}{x - 1}
$$

**Resultado:** $\boxed{\frac{x+1}{x-1}}$

#### Ejemplo 6: Fracciones Algebraicas Mixtas
Simplifica: $\dfrac{\frac{1}{a} + \frac{1}{b}}{\frac{a}{b} - \frac{b}{a}}$

**Razonamiento:**
1. Denominadores pequeños: $a$ y $b$. El MCM es $ab$.
2. Multiplicamos todo por $ab$:
   
$$
\frac{ab(\frac{1}{a}) + ab(\frac{1}{b})}{ab(\frac{a}{b}) - ab(\frac{b}{a})} = \frac{b + a}{a^2 - b^2}
$$

3. Factorizamos el denominador (Diferencia de cuadrados):
   
$$
\frac{a+b}{(a+b)(a-b)}
$$

4. Cancelamos el factor común $(a+b)$.

**Resultado:** $\boxed{\frac{1}{a-b}}$

#### Ejemplo 7: Diferencia de Cuadrados (MCM $x^2$)
Simplifica: $\dfrac{1 - \frac{9}{x^2}}{1 + \frac{3}{x}}$

**Razonamiento:**
1. El MCM de $x^2$ y $x$ es $x^2$.
2. Multiplicamos todo por $x^2$:
   
$$
\frac{x^2(1) - x^2(\frac{9}{x^2})}{x^2(1) + x^2(\frac{3}{x})} = \frac{x^2 - 9}{x^2 + 3x}
$$

3. Factorizamos:
   - Numerador: $(x+3)(x-3)$.
   - Denominador: $x(x+3)$.
4. Cancelamos $(x+3)$.

**Resultado:** $\boxed{\frac{x-3}{x}}$

#### Ejemplo 8: Binomios Complejos
Simplifica: $\dfrac{\frac{1}{x-1} + 1}{\frac{1}{x+1} - 1}$

**Razonamiento:**
1. El MCM es $(x-1)(x+1)$.
2. Multiplicamos arriba y abajo:
   
$$
\frac{(x-1)(x+1)[\frac{1}{x-1} + 1]}{(x-1)(x+1)[\frac{1}{x+1} - 1]}
$$

3. Distribuimos el MCM:
   - Arriba: $(x+1) + (x-1)(x+1) = (x+1) + (x^2-1) = x^2+x$.
   - Abajo: $(x-1) - (x-1)(x+1) = (x-1) - (x^2-1) = x-x^2$.
4. Factorizamos final:
   
$$
\frac{x(x+1)}{x(1-x)} = \frac{x+1}{1-x}
$$

**Resultado:** $\boxed{\frac{x+1}{1-x}}$

---


---

## 🏗️ Fracciones Escalonadas (Torres)

Cuando veas una fracción que parece una escalera hacia abajo, la clave es resolver **de abajo hacia arriba**, un escalón a la vez.

#### Ejemplo 5: La Gran Escalera
Simplifica: $1 + \dfrac{1}{1 + \dfrac{1}{x}}$

**Razonamiento:**
1. **Paso 1 (Último escalón):** Resolvemos $1 + \frac{1}{x} = \frac{x+1}{x}$.
2. **Paso 2 (Invertir):** Ahora tenemos $1 / (\frac{x+1}{x})$. Dividir 1 entre una fracción es simplemente voltearla: $\to \frac{x}{x+1}$.
3. **Paso 3 (Suma final):** 
   
$$
1 + \frac{x}{x+1} = \frac{(x+1) + x}{x+1} = \frac{2x+1}{x+1}
$$

**Resultado:** $\boxed{\frac{2x+1}{x+1}}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1 (Oreja)
Simplifica $\dfrac{\frac{a}{b}}{\frac{c}{d}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Extremos $ad$, medios $bc$.

**Resultado:** $\boxed{\frac{ad}{bc}}$

</details>

### Ejercicio 2 (Oreja)
Simplifica $\dfrac{\frac{x}{2}}{\frac{x}{3}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\frac{3x}{2x} = \frac{3}{2}
$$

**Resultado:** $\boxed{\frac{3}{2}}$

</details>

### Ejercicio 3 (Aritmético)
Simplifica $\dfrac{1 - \frac{1}{2}}{3}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Primero arriba $1 - 1/2 = 1/2$. Luego oreja (3 tiene un 1 abajo):

$$
\frac{1/2}{3/1} = \frac{1}{6}
$$

**Resultado:** $\boxed{\frac{1}{6}}$

</details>

### Ejercicio 4 (MCM)
Simplifica $\dfrac{\frac{1}{x} + 1}{\frac{1}{x}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
Multiplica todo por $x$:

$$
\frac{1 + x}{1}
$$

**Resultado:** $\boxed{x+1}$

</details>

### Ejercicio 5 (Signos)
Simplifica $\dfrac{\frac{1}{x} - \frac{1}{y}}{x-y}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
MCM arriba es $xy \to \frac{y-x}{xy}$.
Dividimos por $(x-y)$ (oreja):

$$
\frac{y-x}{xy(x-y)} = \frac{-(x-y)}{xy(x-y)} = -\frac{1}{xy}
$$

**Resultado:** $\boxed{-\frac{1}{xy}}$

</details>

### Ejercicio 6 (MCM Polinómico)
Simplifica $\dfrac{x + \frac{x}{y}}{y + \frac{y}{x}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
MCM = $xy$.

$$
\frac{xy(x) + xy(\frac{x}{y})}{xy(y) + xy(\frac{y}{x})} = \frac{x^2y + x^2}{xy^2 + y^2} = \frac{x^2(y+1)}{y^2(x+1)}
$$

**Resultado:** $\boxed{\frac{x^2(y+1)}{y^2(x+1)}}$

</details>

### Ejercicio 7 (Escalonada)
Simplifica $2 - \dfrac{3}{1 - \frac{1}{x}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
1. Abajo: $1 - 1/x = \frac{x-1}{x}$.
2. División: $3 / (\frac{x-1}{x}) = \frac{3x}{x-1}$.
3. Resta: $2 - \frac{3x}{x-1} = \frac{2x-2-3x}{x-1} = \frac{-x-2}{x-1}$.

**Resultado:** $\boxed{\frac{-(x+2)}{x-1}}$

</details>

### Ejercicio 8 (Diferencia de cuadrados)
Simplifica $\dfrac{\frac{x^2}{y^2} - 1}{\frac{x}{y} + 1}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
MCM = $y^2$.

$$
\frac{x^2 - y^2}{xy + y^2} = \frac{(x+y)(x-y)}{y(x+y)} = \frac{x-y}{y}
$$

**Resultado:** $\boxed{\frac{x-y}{y}}$

</details>

### Ejercicio 9 (Cálculo)
Simplifica $\dfrac{\frac{1}{x+h} - \frac{1}{x}}{h}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
MCM arriba = $x(x+h)$.
Numerador: $\frac{x - (x+h)}{x(x+h)} = \frac{-h}{x(x+h)}$.
Dividir por $h$: se cancela la $h$.

**Resultado:** $\boxed{\frac{-1}{x(x+h)}}$

</details>

### Ejercicio 10 (Exponentes)
Simplifica $\dfrac{x^{-1} + y^{-1}}{x^{-1}y^{-1}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
\frac{1/x + 1/y}{1/xy}
$$

MCM = $xy$:

$$
\frac{y + x}{1}
$$

**Resultado:** $\boxed{x+y}$

</details>

---

## 🔑 Resumen

| Método | Cuándo usarlo |
| :--- | :--- |
| **Sándwich (Oreja)** | Una sola fracción arriba y una sola abajo. |
| **MCM** | Hay sumas o restas de fracciones en cualquiera de los términos. |
| **Escalonada** | Resolver siempre del "piso" más bajo hacia arriba. |

> **Consejo:** Si ves muchas fracciones dentro de otra, el método del **MCM** es siempre tu mejor amigo. ¡Te ahorra mucho tiempo y papel!
