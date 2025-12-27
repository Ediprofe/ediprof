# **Ángulo Entre Dos Rectas**

Cuando dos calles se cruzan, no siempre lo hacer formando una cruz perfecta (90°). A veces se cruzan de forma oblicua. ¿Cómo calculamos exactamente qué tan abierto o cerrado es ese cruce? Con la **fórmula del ángulo entre rectas**.

---

## 🎯 ¿Qué vas a aprender?

- Cómo calcular el ángulo ($\theta$) donde se cortan dos rectas.
- La fórmula que usa solo las pendientes ($m_1$ y $m_2$).
- Por qué importa el orden (y cómo el valor absoluto nos salva).
- Cómo saber si el ángulo es agudo u obtuso.

---

## ⚔️ El Cruce de Espadas

Imagina dos rectas como dos espadas chocando. Se forman 4 ángulos, pero opuestos por el vértice son iguales.
Generalmente buscamos el **ángulo agudo** (el pequeño, $<90°$).

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Intersección de Rectas</strong>
  </div>
  <img src="/images/geometria/analitica/angulo-entre-rectas.svg" alt="Ángulo φ entre dos rectas" style="width: 100%; height: auto;" />
</div>

La fórmula mágica usa la función tangente:

$$
\tan(\theta) = \left| \frac{m_2 - m_1}{1 + m_1 \cdot m_2} \right|
$$

Y para obtener el ángulo:
$$
\theta = \tan^{-1} \left( \left| \frac{m_2 - m_1}{1 + m_1 \cdot m_2} \right| \right)
$$

> **¿Por qué valor absoluto?** Para que el resultado sea siempre positivo, dándonos el ángulo agudo.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Cálculo Simple
Recta 1: $m_1 = 3$
Recta 2: $m_2 = -2$

**Paso 1: Numerador (resta de pendientes)**
$-2 - 3 = -5$.

**Paso 2: Denominador (1 + producto)**
$1 + (3)(-2) = 1 - 6 = -5$.

**Paso 3: División y Valor Absoluto**
$\frac{-5}{-5} = 1$. Valor absoluto $|1| = 1$.

**Paso 4: Ángulo**
$\tan^{-1}(1) = 45°$.

**Resultado:** Se cruzan formando un ángulo de $\boxed{45°}$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el ángulo entre $m_1 = 0$ y $m_2 = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{1-0}{1+0} = 1$. $\tan^{-1}(1) = 45°$.

**Respuesta:** $\boxed{45°}$
</details>

---

### Ejercicio 2
Ángulo entre $m_1 = 2$ y $m_2 = 2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Numerador $2-2=0$. Ángulo 0°.
(Son paralelas).

**Respuesta:** $\boxed{0°}$
</details>

---

### Ejercicio 3
Ángulo entre $m_1 = 2$ y $m_2 = -0.5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Denominador $1 + 2(-0.5) = 1 - 1 = 0$.
División por cero $\to$ 90°.
(Son perpendiculares).

**Respuesta:** $\boxed{90°}$
</details>

---

### Ejercicio 4
Calcula el ángulo entre $y=x$ y el eje X ($m=0$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m_1=1, m_2=0$. $\tan^{-1}(1) = 45°$.

**Respuesta:** $\boxed{45°}$
</details>

---

### Ejercicio 5
Calcula el ángulo entre $m_1 = 3$ y $m_2 = -3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Num: $-6$. Den: $1-9=-8$.
$\tan^{-1}(6/8) \approx 36.8°$.

**Respuesta:** $\boxed{36.87°}$
</details>

---

### Ejercicio 6
Dos rectas con pendientes 1 y -1.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$1(-1) = -1$.
Perpendiculares.

**Respuesta:** $\boxed{90°}$
</details>

---

### Ejercicio 7
Si $\tan(\theta) = \sqrt{3}$, ¿cuál es el ángulo?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan^{-1}(\sqrt{3}) = 60°$.

**Respuesta:** $\boxed{60°}$
</details>

---

### Ejercicio 8
¿Cuál es el ángulo máximo agudo posible entre dos rectas?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
90° (bueno, eso ya es recto). Agudo sería justo antes, 89.99...

**Respuesta:** $\boxed{90°}$
</details>

---

### Ejercicio 9
Calcula el ángulo entre $y=4$ y $x=4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Horizontal y Vertical.

**Respuesta:** $\boxed{90°}$
</details>

---

### Ejercicio 10
Si las pendientes son recíprocas positivas ($2$ y $1/2$), ¿el ángulo es 90?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No. El producto es 1, no -1.
$\tan^{-1}(| (0.5-2)/(1+1) |) = \tan^{-1}(0.75) \approx 36.8°$.

**Respuesta:** **No**
</details>

---

## 🔑 Resumen

| Denominador ($1+m_1m_2$) | Significado Geométrico |
| :--- | :--- |
| **Cero** | Perpendiculares ($90°$). |
| **Positivo/Negativo** | Se cruzan oblicuamente. |
| **Numerador es Cero** | Paralelas ($0°$). |

> **Conclusión:** Esta fórmula es tu transportador digital. Te dice la precisión exacta del cruce sin necesidad de dibujar nada.
