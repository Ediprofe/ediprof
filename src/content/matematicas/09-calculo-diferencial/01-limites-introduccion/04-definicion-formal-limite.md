# Definición Formal de Límite (Épsilon-Delta)

La definición épsilon-delta transforma la idea intuitiva de "acercarse" en un enunciado matemático riguroso. Es la base lógica de todo el cálculo.

---

## 🎯 ¿Qué vas a aprender?

- La definición formal $\varepsilon$-$\delta$
- Cómo interpretar cada parte de la definición
- Demostrar límites simples formalmente
- Por qué es importante el rigor matemático

---

## 📖 La definición formal

$$\lim_{x \to a} f(x) = L$$

significa que:

> **Para todo** $\varepsilon > 0$, **existe** un $\delta > 0$ tal que si $0 < |x - a| < \delta$, entonces $|f(x) - L| < \varepsilon$.

En símbolos:

$$\forall \varepsilon > 0, \exists \delta > 0 : 0 < |x - a| < \delta \Rightarrow |f(x) - L| < \varepsilon$$

---

## 📖 Interpretación de cada parte

### $\varepsilon$ (épsilon)

- Representa qué tan cerca queremos que $f(x)$ esté de $L$
- Es la "tolerancia" en el eje Y
- $|f(x) - L| < \varepsilon$ significa que $f(x)$ está en $(L - \varepsilon, L + \varepsilon)$

### $\delta$ (delta)

- Representa qué tan cerca debe estar $x$ de $a$ para lograr esa tolerancia
- Es la "precisión" requerida en el eje X
- $|x - a| < \delta$ significa que $x$ está en $(a - \delta, a + \delta)$

### $0 < |x - a|$

- $x$ está cerca de $a$ pero **no es igual** a $a$
- El límite no depende del valor en el punto, solo cerca de él

---

## 📖 Visualización geométrica

Imagina un rectángulo centrado en $(a, L)$:

- **Ancho:** $2\delta$ (de $a - \delta$ a $a + \delta$)
- **Alto:** $2\varepsilon$ (de $L - \varepsilon$ a $L + \varepsilon$)

El límite existe si para cualquier altura que elijas ($\varepsilon$), puedes encontrar un ancho ($\delta$) tal que la gráfica de $f$ dentro del ancho esté completamente dentro del alto.

---

## ⚙️ Ejemplo 1: Demostración formal

Demuestra que $\lim_{x \to 3} (2x + 1) = 7$

**Queremos probar:** Para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:

$$0 < |x - 3| < \delta \Rightarrow |(2x + 1) - 7| < \varepsilon$$

**Desarrollo:**

Simplifiquemos $|(2x + 1) - 7|$:
$$|(2x + 1) - 7| = |2x - 6| = 2|x - 3|$$

Queremos: $2|x - 3| < \varepsilon$

Entonces: $|x - 3| < \frac{\varepsilon}{2}$

**Elección:** $\delta = \frac{\varepsilon}{2}$

**Demostración:**

Si $0 < |x - 3| < \delta = \frac{\varepsilon}{2}$, entonces:

$$|(2x + 1) - 7| = 2|x - 3| < 2 \cdot \frac{\varepsilon}{2} = \varepsilon$$

$$\boxed{\lim_{x \to 3} (2x + 1) = 7 \quad \blacksquare}$$

---

## ⚙️ Ejemplo 2: Función cuadrática

Demuestra que $\lim_{x \to 2} x^2 = 4$

**Queremos:** $|x^2 - 4| < \varepsilon$ cuando $|x - 2| < \delta$

**Desarrollo:**

$$|x^2 - 4| = |x - 2||x + 2|$$

Necesitamos acotar $|x + 2|$. Si restringimos $|x - 2| < 1$:

$$1 < x < 3 \Rightarrow 3 < x + 2 < 5 \Rightarrow |x + 2| < 5$$

Entonces: $|x^2 - 4| = |x - 2||x + 2| < 5|x - 2|$

Queremos: $5|x - 2| < \varepsilon \Rightarrow |x - 2| < \frac{\varepsilon}{5}$

**Elección:** $\delta = \min\left(1, \frac{\varepsilon}{5}\right)$

Tomamos el mínimo para garantizar ambas condiciones.

---

## 📖 Estrategia general

1. **Escribir** lo que queremos: $|f(x) - L| < \varepsilon$
2. **Simplificar** hasta obtener una expresión con $|x - a|$
3. **Acotar** cualquier factor problemático (restringiendo $\delta$)
4. **Despejar** $\delta$ en términos de $\varepsilon$
5. **Verificar** que funciona

---

## 📖 Límites que no existen (formalmente)

Para demostrar que un límite **no existe**, debemos encontrar un $\varepsilon > 0$ específico para el cual **ningún** $\delta$ funciona.

### ⚙️ Ejemplo 3

La función de Heaviside:
$$H(x) = \begin{cases} 0 & x < 0 \\ 1 & x \geq 0 \end{cases}$$

$\lim_{x \to 0} H(x)$ no existe.

**Demostración:** Tomemos $\varepsilon = \frac{1}{2}$.

Para cualquier $\delta > 0$:
- Si $x = -\frac{\delta}{2}$ (a la izquierda): $H(x) = 0$
- Si $x = \frac{\delta}{2}$ (a la derecha): $H(x) = 1$

No pueden ambos estar a distancia menor que $\frac{1}{2}$ del mismo $L$.

---

## 📊 Resumen de símbolos

| Símbolo | Significado |
|---------|-------------|
| $\varepsilon$ | Tolerancia en el eje Y |
| $\delta$ | Precisión en el eje X |
| $\forall$ | "Para todo" |
| $\exists$ | "Existe" |
| $\Rightarrow$ | "Implica que" |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Usa la definición para demostrar:

$$\lim_{x \to 4} (3x - 5) = 7$$

<details>
<summary>Ver solución</summary>

Queremos: $|(3x - 5) - 7| < \varepsilon$

$|3x - 12| = 3|x - 4| < \varepsilon$

$|x - 4| < \frac{\varepsilon}{3}$

**Elegimos:** $\delta = \frac{\varepsilon}{3}$

Si $|x - 4| < \delta$, entonces $|3x - 12| = 3|x - 4| < 3 \cdot \frac{\varepsilon}{3} = \varepsilon$ ✓
</details>

---

**Ejercicio 2:** Encuentra $\delta$ para demostrar $\lim_{x \to 1} 5x = 5$ con $\varepsilon = 0.1$

<details>
<summary>Ver solución</summary>

$|5x - 5| = 5|x - 1| < 0.1$

$|x - 1| < 0.02$

**$\delta = 0.02$** funciona.
</details>
