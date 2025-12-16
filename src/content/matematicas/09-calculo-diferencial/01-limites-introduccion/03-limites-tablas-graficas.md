# Límites con Tablas y Gráficas

Antes de calcular límites algebraicamente, es fundamental saber estimarlos usando tablas de valores y gráficas. Estas herramientas desarrollan tu intuición sobre el comportamiento de funciones.

---

## 🎯 ¿Qué vas a aprender?

- Estimar límites usando tablas de valores
- Interpretar límites desde gráficas
- Identificar cuándo un límite no existe
- Reconocer límites infinitos visualmente

---

## 📖 Método de la tabla de valores

### Pasos

1. Identificar el valor $a$ al que tiende $x$
2. Crear valores que se acerquen a $a$ por ambos lados
3. Calcular $f(x)$ para cada valor
4. Observar hacia qué valor convergen los resultados

### Ejemplo de aproximación

| Acercándose por izquierda | $f(x)$ | Acercándose por derecha | $f(x)$ |
|---------------------------|--------|-------------------------|--------|
| $a - 0.1$ | ? | $a + 0.1$ | ? |
| $a - 0.01$ | ? | $a + 0.01$ | ? |
| $a - 0.001$ | ? | $a + 0.001$ | ? |

---

## ⚙️ Ejemplo 1: Límite que existe

Estima $\lim_{x \to 2} \frac{x^3 - 8}{x - 2}$

### Por la izquierda ($x < 2$)

| $x$ | $\frac{x^3 - 8}{x - 2}$ |
|-----|-------------------------|
| $1.9$ | $11.41$ |
| $1.99$ | $11.9401$ |
| $1.999$ | $11.994001$ |

### Por la derecha ($x > 2$)

| $x$ | $\frac{x^3 - 8}{x - 2}$ |
|-----|-------------------------|
| $2.1$ | $12.61$ |
| $2.01$ | $12.0601$ |
| $2.001$ | $12.006001$ |

**Conclusión:** Ambos lados convergen a **12**.

$$\lim_{x \to 2} \frac{x^3 - 8}{x - 2} = 12$$

---

## ⚙️ Ejemplo 2: Límite infinito

Estima $\lim_{x \to 0} \frac{1}{x^2}$

### Por la izquierda

| $x$ | $\frac{1}{x^2}$ |
|-----|-----------------|
| $-0.1$ | $100$ |
| $-0.01$ | $10{,}000$ |
| $-0.001$ | $1{,}000{,}000$ |

### Por la derecha

| $x$ | $\frac{1}{x^2}$ |
|-----|-----------------|
| $0.1$ | $100$ |
| $0.01$ | $10{,}000$ |
| $0.001$ | $1{,}000{,}000$ |

**Conclusión:** La función crece sin límite desde ambos lados.

$$\lim_{x \to 0} \frac{1}{x^2} = +\infty$$

---

## ⚙️ Ejemplo 3: Límite que no existe

Estima $\lim_{x \to 0} \frac{1}{x}$

### Por la izquierda

| $x$ | $\frac{1}{x}$ |
|-----|---------------|
| $-0.1$ | $-10$ |
| $-0.01$ | $-100$ |
| $-0.001$ | $-1000$ |

### Por la derecha

| $x$ | $\frac{1}{x}$ |
|-----|---------------|
| $0.1$ | $10$ |
| $0.01$ | $100$ |
| $0.001$ | $1000$ |

**Conclusión:** Los límites laterales son diferentes ($-\infty$ vs $+\infty$).

$$\lim_{x \to 0} \frac{1}{x} \text{ no existe}$$

Pero podemos escribir:
- $\lim_{x \to 0^-} \frac{1}{x} = -\infty$
- $\lim_{x \to 0^+} \frac{1}{x} = +\infty$

---

## 📖 Interpretación desde gráficas

### Pasos para leer un límite de una gráfica

1. Localizar el punto $x = a$ en el eje horizontal
2. Seguir la curva desde la izquierda hacia $a$
3. Seguir la curva desde la derecha hacia $a$
4. Observar hacia qué valor de $y$ convergen

### Lo que buscamos

| Comportamiento visual | Interpretación |
|----------------------|----------------|
| Ambos lados convergen al mismo punto | $\lim_{x \to a} f(x) = L$ |
| Lados convergen a diferentes valores | Límite no existe |
| La curva "explota" hacia arriba | $\lim = +\infty$ |
| La curva "explota" hacia abajo | $\lim = -\infty$ |
| Hay un punto aislado en $(a, f(a))$ | El límite puede ser diferente de $f(a)$ |

---

## ⚙️ Ejemplo 4: Función con hueco

Considera la gráfica de $f(x) = \frac{x^2 - 1}{x - 1}$ (simplificada a $x + 1$ para $x \neq 1$).

La gráfica es una línea recta $y = x + 1$ con un **hueco** en $(1, 2)$.

**Desde la gráfica:**
- Por la izquierda: la curva se acerca a $y = 2$
- Por la derecha: la curva se acerca a $y = 2$

$$\lim_{x \to 1} f(x) = 2$$

Aunque $f(1)$ no existe, el límite sí existe.

---

## ⚙️ Ejemplo 5: Función definida por partes

$$g(x) = \begin{cases} x^2 & \text{si } x < 1 \\ 3 & \text{si } x = 1 \\ 2x - 1 & \text{si } x > 1 \end{cases}$$

**Analizando:**
- Por la izquierda: $\lim_{x \to 1^-} x^2 = 1$
- Por la derecha: $\lim_{x \to 1^+} (2x - 1) = 1$

$$\lim_{x \to 1} g(x) = 1$$

Nota: $g(1) = 3 \neq 1$, pero el límite es 1.

---

## 📊 Casos especiales en gráficas

| Situación | Límite |
|-----------|--------|
| Asíntota vertical | $\pm\infty$ |
| Asíntota horizontal | Valor de la asíntota |
| Hueco en la curva | El límite puede existir |
| Salto en la función | Límite no existe |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Usa una tabla para estimar:

$$\lim_{x \to 4} \frac{x - 4}{\sqrt{x} - 2}$$

<details>
<summary>Ver solución</summary>

| $x$ cercano a 4 | $\frac{x - 4}{\sqrt{x} - 2}$ |
|-----------------|------------------------------|
| $3.9$ | $3.9749...$ |
| $3.99$ | $3.9975...$ |
| $4.01$ | $4.0025...$ |
| $4.1$ | $4.0249...$ |

$$\lim_{x \to 4} \frac{x - 4}{\sqrt{x} - 2} = 4$$
</details>

---

**Ejercicio 2:** A partir de la tabla, determina si el límite existe:

| $x$ | $-0.1$ | $-0.01$ | $-0.001$ | $0.001$ | $0.01$ | $0.1$ |
|-----|--------|---------|----------|---------|--------|-------|
| $f(x)$ | $2.9$ | $2.99$ | $2.999$ | $3.001$ | $3.01$ | $3.1$ |

<details>
<summary>Ver solución</summary>

El límite existe y es igual a **3**.

Por ambos lados, $f(x)$ converge a 3.
</details>
