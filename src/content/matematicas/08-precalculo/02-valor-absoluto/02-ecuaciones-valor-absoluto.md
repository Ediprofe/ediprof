# Ecuaciones con Valor Absoluto

Resolver ecuaciones que contienen valor absoluto requiere considerar los casos donde la expresión interior es positiva o negativa. Es como abrir una "caja de posibilidades".

---

## 🎯 ¿Qué vas a aprender?

- Resolver ecuaciones del tipo $|f(x)| = a$
- Resolver ecuaciones del tipo $|f(x)| = |g(x)|$
- Identificar cuándo una ecuación no tiene solución
- Verificar las soluciones obtenidas

---

## 📖 Caso fundamental: $|f(x)| = a$

Si $a > 0$, la ecuación $|f(x)| = a$ tiene **dos casos**:

$$
|f(x)| = a \quad \Leftrightarrow \quad f(x) = a \quad \text{o} \quad f(x) = -a
$$

### 💡 Interpretación geométrica

$|x - c| = d$ significa: "la distancia de $x$ al punto $c$ es igual a $d$".

Hay exactamente dos puntos a distancia $d$ de $c$: uno a la izquierda y otro a la derecha.

---

## ⚙️ Ejemplo 1: Ecuación simple

Resolver: $|x| = 5$

**Caso 1:** $x = 5$

**Caso 2:** $x = -5$

**Solución:** $x \in \{-5, 5\}$

---

## ⚙️ Ejemplo 2: Expresión lineal dentro

Resolver: $|x - 3| = 7$

**Caso 1:** $x - 3 = 7$
$$x = 10$$

**Caso 2:** $x - 3 = -7$
$$x = -4$$

**Solución:** $x \in \{-4, 10\}$

**Verificación:**
- $|10 - 3| = |7| = 7$ ✓
- $|-4 - 3| = |-7| = 7$ ✓

---

## ⚙️ Ejemplo 3: Con coeficientes

Resolver: $|2x + 5| = 9$

**Caso 1:** $2x + 5 = 9$
$$2x = 4 \quad \Rightarrow \quad x = 2$$

**Caso 2:** $2x + 5 = -9$
$$2x = -14 \quad \Rightarrow \quad x = -7$$

**Solución:** $x \in \{-7, 2\}$

---

## ⚙️ Ejemplo 4: Valor absoluto igualado a expresión

Resolver: $|x - 4| = 2x - 1$

**Condición:** El lado derecho debe ser $\geq 0$, es decir, $2x - 1 \geq 0 \Rightarrow x \geq \frac{1}{2}$

**Caso 1:** $x - 4 = 2x - 1$
$$-4 + 1 = 2x - x$$
$$x = -3$$

¿Es válido? Verificamos $x \geq \frac{1}{2}$: $-3 \not\geq \frac{1}{2}$ ❌ (se descarta)

**Caso 2:** $x - 4 = -(2x - 1)$
$$x - 4 = -2x + 1$$
$$3x = 5$$
$$x = \frac{5}{3}$$

¿Es válido? $\frac{5}{3} \geq \frac{1}{2}$ ✓

**Verificación:** $\left|\frac{5}{3} - 4\right| = \left|-\frac{7}{3}\right| = \frac{7}{3}$ y $2 \cdot \frac{5}{3} - 1 = \frac{10}{3} - 1 = \frac{7}{3}$ ✓

**Solución:** $x = \frac{5}{3}$

---

## 📖 Caso especial: $|f(x)| = 0$

Si $|f(x)| = 0$, entonces $f(x) = 0$.

El valor absoluto solo es cero cuando lo que hay adentro es cero.

**Ejemplo:** $|3x - 12| = 0$

$$3x - 12 = 0 \quad \Rightarrow \quad x = 4$$

---

## 📖 Caso imposible: $|f(x)| = a$ con $a < 0$

Si $a < 0$, la ecuación **no tiene solución**.

El valor absoluto nunca es negativo.

**Ejemplo:** $|2x + 1| = -5$

**Solución:** $\emptyset$ (conjunto vacío)

---

## 📖 Ecuaciones de la forma $|f(x)| = |g(x)|$

Si dos valores absolutos son iguales, sus contenidos son iguales o son opuestos:

$$
|f(x)| = |g(x)| \quad \Leftrightarrow \quad f(x) = g(x) \quad \text{o} \quad f(x) = -g(x)
$$

---

## ⚙️ Ejemplo 5: Dos valores absolutos

Resolver: $|x - 2| = |3x + 4|$

**Caso 1:** $x - 2 = 3x + 4$
$$-2 - 4 = 3x - x$$
$$-6 = 2x$$
$$x = -3$$

**Caso 2:** $x - 2 = -(3x + 4)$
$$x - 2 = -3x - 4$$
$$4x = -2$$
$$x = -\frac{1}{2}$$

**Verificación:**
- Para $x = -3$: $|-3-2| = |-5| = 5$ y $|3(-3)+4| = |-5| = 5$ ✓
- Para $x = -\frac{1}{2}$: $|-\frac{1}{2}-2| = |\frac{-5}{2}| = \frac{5}{2}$ y $|3(-\frac{1}{2})+4| = |\frac{5}{2}| = \frac{5}{2}$ ✓

**Solución:** $x \in \left\{-3, -\frac{1}{2}\right\}$

---

## ⚙️ Ejemplo 6: Ecuación cuadrática resultante

Resolver: $|x^2 - 4| = 5$

**Caso 1:** $x^2 - 4 = 5$
$$x^2 = 9$$
$$x = \pm 3$$

**Caso 2:** $x^2 - 4 = -5$
$$x^2 = -1$$
No tiene solución real (un cuadrado no puede ser negativo).

**Solución:** $x \in \{-3, 3\}$

---

## 📊 Resumen de métodos

| Forma de la ecuación | Estrategia |
|---------------------|------------|
| $\|f(x)\| = a$ (con $a > 0$) | Resolver $f(x) = a$ y $f(x) = -a$ |
| $\|f(x)\| = 0$ | Resolver $f(x) = 0$ |
| $\|f(x)\| = a$ (con $a < 0$) | Sin solución |
| $\|f(x)\| = g(x)$ | Agregar condición $g(x) \geq 0$ |
| $\|f(x)\| = \|g(x)\|$ | Resolver $f(x) = g(x)$ y $f(x) = -g(x)$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Resuelve:

a) $|x + 6| = 2$
b) $|4x - 3| = 11$
c) $|5 - 2x| = 0$

<details>
<summary>Ver soluciones</summary>

a) $x + 6 = 2$ o $x + 6 = -2$
   
   $x = -4$ o $x = -8$

b) $4x - 3 = 11$ o $4x - 3 = -11$
   
   $x = \frac{14}{4} = \frac{7}{2}$ o $x = \frac{-8}{4} = -2$

c) $5 - 2x = 0 \Rightarrow x = \frac{5}{2}$
</details>

---

**Ejercicio 2:** Resuelve:

a) $|x - 5| = |2x + 1|$
b) $|x^2 - 9| = 7$
c) $|3x + 2| = x + 4$

<details>
<summary>Ver soluciones</summary>

a) $x - 5 = 2x + 1$ → $x = -6$
   
   $x - 5 = -(2x + 1)$ → $x = \frac{4}{3}$
   
   **Solución:** $\{-6, \frac{4}{3}\}$

b) $x^2 - 9 = 7$ → $x^2 = 16$ → $x = \pm 4$
   
   $x^2 - 9 = -7$ → $x^2 = 2$ → $x = \pm\sqrt{2}$
   
   **Solución:** $\{-4, -\sqrt{2}, \sqrt{2}, 4\}$

c) Condición: $x + 4 \geq 0$ → $x \geq -4$
   
   Caso 1: $3x + 2 = x + 4$ → $x = 1$ ✓
   
   Caso 2: $3x + 2 = -(x + 4)$ → $x = -\frac{3}{2}$ ✓
   
   **Solución:** $\{-\frac{3}{2}, 1\}$
</details>
