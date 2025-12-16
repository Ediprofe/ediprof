# Sumas de Riemann

Las sumas de Riemann aproximan el área bajo una curva mediante rectángulos. Son la base conceptual de la integral definida.

---

## 🎯 ¿Qué vas a aprender?

- El problema del área
- Particiones y puntos de muestra
- Sumas de Riemann izquierda, derecha y del punto medio
- Paso al límite

---

## 📖 El problema del área

¿Cómo encontrar el área de una región curvilínea?

**Idea:** Aproximar con rectángulos y refinar la aproximación.

---

## 📖 Partición del intervalo

Dividimos $[a, b]$ en $n$ subintervalos:

$$
a = x_0 < x_1 < x_2 < ... < x_n = b
$$

**Ancho de cada subintervalo (uniforme):**

$$
\Delta x = \frac{b - a}{n}
$$

---

## 📖 Sumas de Riemann

La **suma de Riemann** es:

$$
S_n = \sum_{i=1}^{n} f(x_i^*) \cdot \Delta x
$$

donde $x_i^*$ es un punto de muestra en el $i$-ésimo subintervalo.

---

## 📖 Tipos de sumas

| Tipo | Punto de muestra $x_i^*$ |
|------|-------------------------|
| Izquierda | $x_{i-1}$ (extremo izquierdo) |
| Derecha | $x_i$ (extremo derecho) |
| Punto medio | $\frac{x_{i-1} + x_i}{2}$ |

---

## ⚙️ Ejemplo 1: Área bajo $f(x) = x^2$ en $[0, 2]$

Con $n = 4$ subintervalos: $\Delta x = \frac{2-0}{4} = 0.5$

**Puntos:** $x_0=0$, $x_1=0.5$, $x_2=1$, $x_3=1.5$, $x_4=2$

**Suma izquierda:**

$$
L_4 = \Delta x[f(0) + f(0.5) + f(1) + f(1.5)] = 0.5[0 + 0.25 + 1 + 2.25] = 0.5(3.5) = 1.75
$$

**Suma derecha:**

$$
R_4 = \Delta x[f(0.5) + f(1) + f(1.5) + f(2)] = 0.5[0.25 + 1 + 2.25 + 4] = 0.5(7.5) = 3.75
$$

**Valor real:** $\int_0^2 x^2\,dx = \frac{8}{3} \approx 2.67$

---

## ⚙️ Ejemplo 2: Más rectángulos

Para $f(x) = x^2$ en $[0, 2]$ con $n = 8$: $\Delta x = 0.25$

**Suma derecha:**

$$
R_8 = 0.25[f(0.25) + f(0.5) + ... + f(2)] = 0.25[0.0625 + 0.25 + 0.5625 + 1 + 1.5625 + 2.25 + 3.0625 + 4] = 0.25(12.75) = 3.1875
$$

¡Más cerca de 2.67!

---

## 📖 Notación sigma

$$
S_n = \sum_{i=1}^{n} f(x_i^*) \Delta x
$$

Para suma derecha con partición uniforme:

$$
R_n = \sum_{i=1}^{n} f\left(a + i \cdot \frac{b-a}{n}\right) \cdot \frac{b-a}{n}
$$

---

## 📖 El límite

Cuando $n \to \infty$:

$$
\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x = \int_a^b f(x)\,dx
$$

Todas las sumas de Riemann convergen al mismo valor.

---

## ⚙️ Ejemplo 3: Cálculo exacto por límite

Para $f(x) = x$ en $[0, 1]$:

**Suma derecha:**
$$R_n = \sum_{i=1}^{n} f\left(\frac{i}{n}\right) \cdot \frac{1}{n} = \sum_{i=1}^{n} \frac{i}{n^2}$$

$$= \frac{1}{n^2} \sum_{i=1}^{n} i = \frac{1}{n^2} \cdot \frac{n(n+1)}{2} = \frac{n+1}{2n}$$

$$\lim_{n \to \infty} R_n = \lim_{n \to \infty} \frac{n+1}{2n} = \frac{1}{2}$$

Verificación: $\int_0^1 x\,dx = \frac{x^2}{2}\Big|_0^1 = \frac{1}{2}$ ✓

---

## 📊 Resumen gráfico

```
       f(x)
        │    ┌──────┐
        │    │      │
        │  ┌─┤      │
        │  │ │      │
        │──┼─┼──────┴────
        a  x₁ x₂     b
```

A más rectángulos, mejor aproximación.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula $L_4$ y $R_4$ para $f(x) = x + 1$ en $[0, 4]$.

<details>
<summary>Ver solución</summary>

$\Delta x = 1$

$L_4 = 1[f(0) + f(1) + f(2) + f(3)] = 1 + 2 + 3 + 4 = 10$

$R_4 = 1[f(1) + f(2) + f(3) + f(4)] = 2 + 3 + 4 + 5 = 14$

Valor real: $\int_0^4 (x+1)\,dx = 12$
</details>

---

**Ejercicio 2:** Expresa $\int_1^3 x^2\,dx$ como límite de suma de Riemann.

<details>
<summary>Ver solución</summary>

$\Delta x = \frac{2}{n}$, $x_i = 1 + \frac{2i}{n}$

$\lim_{n \to \infty} \sum_{i=1}^{n} \left(1 + \frac{2i}{n}\right)^2 \cdot \frac{2}{n}$
</details>
