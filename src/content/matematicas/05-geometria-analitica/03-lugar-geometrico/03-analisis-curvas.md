# **Análisis de Curvas**

Cuando un médico ve una radiografía, busca patrones específicos para hacer un diagnóstico. En matemáticas, nosotros "diagnosticamos" ecuaciones. No necesitamos graficar punto por punto para saber si una ecuación es una circunferencia, una parábola o una hipérbola. Solo necesitamos analizar sus "síntomas" (coeficientes).

---

## 🎯 ¿Qué vas a aprender?

- Cómo identificar una curva solo mirando su ecuación general.
- El sistema de los 6 pasos para analizar cualquier gráfica.
- Qué son las asíntotas y por qué son importantes.
- Cómo saber, de un vistazo, si una ecuación es un círculo o una elipse.

---

## 🕵️‍♂️ El Método de Diagnóstico Rápido

Dada una ecuación general de segundo grado:
$$Ax^2 + Cy^2 + Dx + Ey + F = 0$$

Podemos saber qué es mirando solo $A$ y $C$ (los números que acompañan a los cuadrados).

| Pista (Coeficientes) | Diagnóstico (Curva) |
| :--- | :--- |
| **Solo uno está al cuadrado** | **Parábola** ($y=x^2$ o $x=y^2$). |
| **Mismo signo, Mismo número** | **Circunferencia** ($x^2 + y^2 = r^2$). |
| **Mismo signo, Distinto número** | **Elipse** ($2x^2 + 5y^2 = 10$). |
| **Signos Opuestos** | **Hipérbola** ($x^2 - y^2 = 1$). |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Análisis de Curvas</strong>
  </div>
  <img src="/images/geometria/analitica/analisis-curva.svg" alt="Análisis de curva con interceptos y simetría" style="width: 100%; height: auto;" />
</div>

---

## 🔬 El Análisis Profundo (6 Pasos)

Si necesitas dibujar la curva con precisión, sigue este checklist:

1.  **Interceptos:** ¿Dónde corta a los ejes X e Y?
2.  **Simetría:** ¿Es un espejo en algún eje?
3.  **Extensión (Dominio/Rango):** ¿La curva existe en todo el plano o está confinada en una caja? (Ej: Una circunferencia no existe fuera de su radio).
4.  **Asíntotas:** ¿Hay líneas prohibidas que la curva nunca toca? (Típico de hipérbolas).
5.  **Factorización:** ¿Se puede romper la ecuación en dos más simples?
6.  **Cálculo de Puntos:** Un par de puntos extra para confirmar.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Diagnóstico Rápido
Ecuación: $4x^2 + 4y^2 - 16 = 0$.
*   Miro los cuadrados: $4x^2$ y $4y^2$.
*   Mismo signo (+) y mismo número (4).
*   **Diagnóstico:** Es una **Circunferencia**.

### Ejemplo 2: Análisis de Extensión
Ecuación: $x^2 + y^2 = 9$.
Despejando $y$:
$$ y = \pm \sqrt{9 - x^2} $$
Para que la raíz exista (números reales), lo de adentro debe ser positivo:
$$ 9 - x^2 \geq 0 \Rightarrow x^2 \leq 9 $$
$$ -3 \leq x \leq 3 $$
**Conclusión:** La curva solo existe entre $x=-3$ y $x=3$. No pierdas el tiempo buscando puntos en $x=10$.

### Ejemplo 3: Asíntotas
Ecuación: $xy = 1$ o $y = 1/x$.
*   Si $x=0$, dividimos por cero (¡Error!). La curva nunca toca el eje Y.
*   Si $x$ es gigante ($1,000,000$), $y$ es pequeñito ($0.000001$), pero nunca llega a cero. La curva nunca toca el eje X.
*   **Conclusión:** Los ejes son asíntotas.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica la curva: $x^2 + 2y^2 = 10$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cuadrados positivos pero coeficientes distintos (1 y 2).

**Respuesta:** **Elipse**
</details>

---

### Ejercicio 2
Identifica la curva: $y = x^2 - 5x + 6$.

<details>
<summary>Ver solución</summary>
<br>
**Razonamiento:**
Solo la $x$ está al cuadrado. La $y$ es lineal.

**Respuesta:** **Parábola**
</details>

---

### Ejercicio 3
Identifica la curva: $x^2 - y^2 = 4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Signos opuestos (uno positivo, uno negativo).

**Respuesta:** **Hipérbola**
</details>

---

### Ejercicio 4
Determina la extensión en Y de $y^2 = x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$y = \pm \sqrt{x}$. $y$ puede ser cualquier número real (si $x$ es suficientemente grande).
Rango: Todo $\mathbb{R}$.

**Respuesta:** **De $-\infty$ a $+\infty$**
</details>

---

### Ejercicio 5
¿Qué curva es $3x + 2y - 5 = 0$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ninguna variable está al cuadrado. Son lineales (grado 1).

**Respuesta:** **Recta**
</details>

---

### Ejercicio 6
Encuentra la asíntota vertical de $y = \frac{1}{x-2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El denominador se hace cero cuando $x-2=0 \Rightarrow x=2$.

**Respuesta:** $\boxed{x = 2}$
</details>

---

### Ejercicio 7
Factoriza $x^2 - y^2 = 0$ e interpreta la gráfica.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(x-y)(x+y)=0$.
Esto significa que o $y=x$ o $y=-x$.
Son dos rectas cruzadas (una hipérbola degenerada).

**Respuesta:** **Dos rectas (X)**
</details>

---

### Ejercicio 8
Identifica la curva: $2x^2 + 2y^2 - 4x = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Mismo coeficiente (2) en ambos cuadrados.

**Respuesta:** **Circunferencia**
</details>

---

### Ejercicio 9
¿Cuál es el dominio máximo de $y = \sqrt{x}$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No existen raíces de negativos. $x \geq 0$.

**Respuesta:** $\boxed{x \geq 0}$
</details>

---

### Ejercicio 10
Si $A=0$ y $C=0$ en la ecuación general, ¿qué es?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No hay cuadrados. Queda $Dx + Ey + F = 0$.

**Respuesta:** **Una Recta**
</details>

---

## 🔑 Resumen

| Señal | Tu Diagnóstico |
| :--- | :--- |
| **Grado 1 (sin cuadrados)** | Recta. |
| **Solo 1 cuadrado** | Parábola. |
| **2 cuadrados, signos opuestos** | Hipérbola. |
| **2 cuadrados iguales** | Circunferencia. |
| **2 cuadrados distintos (+)** | Elipse. |

> **Conclusión:** No te dejes intimidar por ecuaciones largas. Mira los cuadrados ($x^2, y^2$). Ellos son el ADN de la curva y te dicen todo lo que necesitas saber.
