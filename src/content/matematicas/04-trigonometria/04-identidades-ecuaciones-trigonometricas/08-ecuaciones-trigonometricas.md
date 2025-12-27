# **Ecuaciones Trigonométricas**

Resolver una ecuación normal es como encontrar el valor de $x$ en una línea recta. Resolver una **ecuación trigonométrica** es un poco más interesante: buscas ángulos en un círculo, lo que significa que a veces hay muchas (o infinitas) respuestas que funcionan.

---

## 🎯 ¿Qué vas a aprender?

- La diferencia entre resolver una ecuación lineal y una trigonométrica.
- Por qué una sola ecuación puede tener dos soluciones en cada vuelta.
- El método infalible en 3 pasos: Aislar, Referencia, Cuadrantes.
- Cómo escribir la solución general ($+ 360k$) para cubrir infinitas vueltas.

---

## 🔄 El Concepto Clave: La Periodicidad

Si te pregunto: "¿Qué ángulo tiene un seno de 0.5?", podrías decir $30°$. ¡Correcto!
Pero $150°$ también tiene seno de 0.5. Y $390°$ (una vuelta y pico) también.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Soluciones en el Círculo Unitario</strong>
  </div>

![Soluciones de ecuaciones](/images/trigonometria/identidades/soluciones-ecuaciones.svg)

</div>

Por lo general, pedimos soluciones en una sola vuelta: $[0°, 360°)$.

---

## 🛠️ El Método Infalible

### Paso 1: Aislar la Función
Trata a $\sin x$ o $\cos x$ como si fuera una $x$ grande. Despeja hasta tener:
$$ \sin(x) = \text{Número} $$

### Paso 2: Ángulo de Referencia
Ignora el signo (si es negativo) por un momento. ¿Qué ángulo agudo del primer cuadrante da ese valor?
$$ \text{Ref} = \sin^{-1}(|\text{Número}|) $$

### Paso 3: Ubicar los Cuadrantes
Ahora mira el signo original.
*   Si es **positivo** (+): ¿En qué cuadrantes es positiva la función?
*   Si es **negativo** (-): ¿En qué cuadrantes es negativa?

### Paso 4: Calcular los Ángulos Reales
Usa el ángulo de referencia para encontrar los ángulos en esos cuadrantes.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Ecuación Simple
Resuelve $2\cos(x) - 1 = 0$ para $0° \le x < 360°$.

**Paso 1: Aislar**
$$
2\cos x = 1 \implies \cos x = 0.5
$$

**Paso 2: Referencia**
¿Qué ángulo tiene coseno 0.5?
$$
Ref = 60°
$$

**Paso 3: Cuadrantes**
El coseno es positivo (+) en **QI** y **QIV**.

**Paso 4: Soluciones**
*   **QI:** $60°$
*   **QIV:** $360° - 60° = 300°$

**Resultado:** $\boxed{60°, 300°}$

### Ejemplo 2: Ecuación Cuadrática
Resuelve $2\sin^2(x) - \sin(x) - 1 = 0$.

**Paso 1: Factorizar**
Imagina que $u = \sin x$. La ecuación es $2u^2 - u - 1 = 0$.
Factorizamos: $(2u + 1)(u - 1) = 0$.

**Paso 2: Dos caminos**
*   Camino A: $2\sin x + 1 = 0 \implies \sin x = -0.5$
*   Camino B: $\sin x - 1 = 0 \implies \sin x = 1$

**Paso 3: Resolver Camino A ($\sin x = -0.5$)**
*   Ref: $30°$.
*   Signo Negativo $\rightarrow$ QIII ($180+30=210°$) y QIV ($360-30=330°$).

**Paso 4: Resolver Camino B ($\sin x = 1$)**
*   El seno es 1 solo en $90°$.

**Resultado:** $\boxed{90°, 210°, 330°}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Resuelve $\sin x = \frac{\sqrt{3}}{2}$ en $[0°, 360°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ref = 60°.
Seno positivo en QI y QII.
$60°$ y $180-60=120°$.

**Respuesta:** $\boxed{60°, 120°}$
</details>

---

### Ejercicio 2
Resuelve $\tan x = -1$ en $[0°, 360°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ref = 45° (tangente 1).
Tangente negativa en QII y QIV.
QII: $180-45=135°$.
QIV: $360-45=315°$.

**Respuesta:** $\boxed{135°, 315°}$
</details>

---

### Ejercicio 3
Resuelve $4\cos^2 x = 3$ en $[0°, 360°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos^2 x = 3/4 \implies \cos x = \pm\frac{\sqrt{3}}{2}$.
Ref = 30°.
Como es $\pm$, valen los 4 cuadrantes.
$30°, 150°, 210°, 330°$.

**Respuesta:** $\boxed{30°, 150°, 210°, 330°}$
</details>

---

### Ejercicio 4
Resuelve $\csc x = 2$ en $[0°, 360°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si $\csc x = 2$, entonces $\sin x = 1/2$.
Ref = 30°. Positivo en QI, QII.

**Respuesta:** $\boxed{30°, 150°}$
</details>

---

### Ejercicio 5
Resuelve $2\cos(3x) = 1$ en $[0°, 360°)$ (Ojo con el 3x).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos(3x) = 0.5$.
Ángulo $3x$ puede ser $60°, 300°, 420°, 660°...$ (damos más vueltas).
Dividimos todo entre 3.
$x = 20°, 100°, 140°, 220°, 260°, 340°$.

**Respuesta:** $\boxed{20°, 100°, 140°, 220°, 260°, 340°}$
</details>

---

### Ejercicio 6
Resuelve $\sin x \cos x = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
O bien $\sin x = 0$ o bien $\cos x = 0$.
$\sin x = 0 \rightarrow 0°, 180°$.
$\cos x = 0 \rightarrow 90°, 270°$.

**Respuesta:** $\boxed{0°, 90°, 180°, 270°}$
</details>

---

### Ejercicio 7
Resuelve $\sqrt{3}\tan x - 1 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan x = 1/\sqrt{3} = \sqrt{3}/3$.
Ref = 30°. Tangente positiva (QI, QIII).

**Respuesta:** $\boxed{30°, 210°}$
</details>

---

### Ejercicio 8
Resuelve $2\sin^2 x + \sin x = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Factor común: $\sin x(2\sin x + 1) = 0$.
1. $\sin x = 0 \rightarrow 0°, 180°$.
2. $\sin x = -0.5 \rightarrow 210°, 330°$.

**Respuesta:** $\boxed{0°, 180°, 210°, 330°}$
</details>

---

### Ejercicio 9
Resuelve $\sec^2 x - 1 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sec^2 x = 1 \rightarrow \cos^2 x = 1 \rightarrow \cos x = \pm 1$.
$0°, 180°$.

**Respuesta:** $\boxed{0°, 180°}$
</details>

---

### Ejercicio 10
Resuelve $\sin(2x) = \cos x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Usa identidad: $2\sin x \cos x = \cos x$.
$2\sin x \cos x - \cos x = 0$.
$\cos x(2\sin x - 1) = 0$.
$\cos x = 0$ ($90, 270$) ó $\sin x = 0.5$ ($30, 150$).

**Respuesta:** $\boxed{30°, 90°, 150°, 270°}$
</details>

---

## 🔑 Resumen

| Paso | Pregunta Clave |
| :--- | :--- |
| **Referencia** | ¿Qué ángulo agudo me da este valor numérico? |
| **Signo** | ¿En qué cuadrantes vive este signo? (+ ó -) |
| **Respuestas** | ¿Calculé todas las opciones posibles (generalmente 2)? |

> **Conclusión:** La mayoría de los errores ocurren al olvidar el segundo cuadrante o al confundir senos con cosenos. Dibuja siempre un pequeño círculo unitario para guiarte.
