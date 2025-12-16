# Integrales de Potencias Trigonométricas

Las integrales de potencias de seno, coseno, tangente y otras funciones trigonométricas requieren técnicas específicas basadas en identidades.

---

## 🎯 ¿Qué vas a aprender?

- Integrales de $\sin^n x$ y $\cos^n x$
- Integrales de $\sin^m x \cos^n x$
- Integrales de $\tan^n x$ y $\sec^n x$
- Identidades útiles

---

## 📖 Identidades fundamentales

$$\sin^2 x + \cos^2 x = 1$$

$$\sin^2 x = \frac{1 - \cos 2x}{2}$$

$$\cos^2 x = \frac{1 + \cos 2x}{2}$$

$$\sin x \cos x = \frac{\sin 2x}{2}$$

---

## 📖 Caso 1: $\int \sin^m x \cos^n x\,dx$ (uno impar)

Si $m$ o $n$ es impar, separa un factor y usa $\sin^2 x + \cos^2 x = 1$.

---

## ⚙️ Ejemplo 1: Coseno impar

$$\int \sin^2 x \cos^3 x\,dx$$

Separamos $\cos x$ (para usar como $du$):

$$= \int \sin^2 x \cos^2 x \cdot \cos x\,dx$$

Usamos $\cos^2 x = 1 - \sin^2 x$:

$$= \int \sin^2 x (1 - \sin^2 x) \cos x\,dx$$

$u = \sin x$, $du = \cos x\,dx$:

$$= \int u^2(1 - u^2)\,du = \int (u^2 - u^4)\,du$$

$$= \frac{u^3}{3} - \frac{u^5}{5} + C = \frac{\sin^3 x}{3} - \frac{\sin^5 x}{5} + C$$

---

## 📖 Caso 2: $\int \sin^m x \cos^n x\,dx$ (ambos pares)

Usa las identidades de ángulo mitad para reducir potencias.

---

## ⚙️ Ejemplo 2: Ambos pares

$$\int \sin^2 x \cos^2 x\,dx$$

$$= \int \left(\frac{1-\cos 2x}{2}\right)\left(\frac{1+\cos 2x}{2}\right)\,dx$$

$$= \frac{1}{4}\int (1 - \cos^2 2x)\,dx = \frac{1}{4}\int \sin^2 2x\,dx$$

$$= \frac{1}{4}\int \frac{1 - \cos 4x}{2}\,dx = \frac{1}{8}\left(x - \frac{\sin 4x}{4}\right) + C$$

---

## ⚙️ Ejemplo 3: Solo seno al cuadrado

$$\int \sin^2 x\,dx = \int \frac{1 - \cos 2x}{2}\,dx = \frac{x}{2} - \frac{\sin 2x}{4} + C$$

---

## ⚙️ Ejemplo 4: Coseno cuarta

$$\int \cos^4 x\,dx = \int \left(\frac{1+\cos 2x}{2}\right)^2\,dx$$

$$= \frac{1}{4}\int (1 + 2\cos 2x + \cos^2 2x)\,dx$$

$$= \frac{1}{4}\left(x + \sin 2x + \frac{x}{2} + \frac{\sin 4x}{8}\right) + C$$

$$= \frac{3x}{8} + \frac{\sin 2x}{4} + \frac{\sin 4x}{32} + C$$

---

## 📖 Caso 3: $\int \tan^n x\,dx$

Usa $\tan^2 x = \sec^2 x - 1$ repetidamente.

---

## ⚙️ Ejemplo 5: Tangente al cuadrado

$$\int \tan^2 x\,dx = \int (\sec^2 x - 1)\,dx = \tan x - x + C$$

---

## ⚙️ Ejemplo 6: Tangente al cubo

$$\int \tan^3 x\,dx = \int \tan x (\sec^2 x - 1)\,dx$$

$$= \int \tan x \sec^2 x\,dx - \int \tan x\,dx$$

Para la primera: $u = \tan x$, $du = \sec^2 x\,dx$

$$= \frac{\tan^2 x}{2} - (-\ln|\cos x|) + C = \frac{\tan^2 x}{2} + \ln|\cos x| + C$$

---

## 📖 Caso 4: $\int \sec^n x\,dx$

Para $n$ par, usa $\sec^2 x = 1 + \tan^2 x$.

$$\int \sec^2 x\,dx = \tan x + C$$

$$\int \sec^4 x\,dx = \int \sec^2 x (1 + \tan^2 x)\,dx$$

---

## ⚙️ Ejemplo 7: Secante cuarta

$$\int \sec^4 x\,dx = \int (1 + \tan^2 x)\sec^2 x\,dx$$

$u = \tan x$, $du = \sec^2 x\,dx$:

$$= \int (1 + u^2)\,du = u + \frac{u^3}{3} + C = \tan x + \frac{\tan^3 x}{3} + C$$

---

## 📊 Resumen de estrategias

| Integral | Estrategia |
|----------|-----------|
| $\sin^m x \cos^n x$ (uno impar) | Separar y sustituir |
| $\sin^m x \cos^n x$ (ambos pares) | Identidades mitad |
| $\tan^n x$ | Usar $\tan^2 = \sec^2 - 1$ |
| $\sec^n x$ (par) | Usar $\sec^2 = 1 + \tan^2$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula $\int \sin^3 x\,dx$

<details>
<summary>Ver solución</summary>

$= \int \sin x (1 - \cos^2 x)\,dx$

$u = \cos x$, $du = -\sin x\,dx$

$= -\int (1 - u^2)\,du = -u + \frac{u^3}{3} + C$

$= -\cos x + \frac{\cos^3 x}{3} + C$
</details>

---

**Ejercicio 2:** Calcula $\int \tan^4 x\,dx$

<details>
<summary>Ver solución</summary>

$= \int \tan^2 x (\sec^2 x - 1)\,dx$

$= \int \tan^2 x \sec^2 x\,dx - \int \tan^2 x\,dx$

$= \frac{\tan^3 x}{3} - \tan x + x + C$
</details>
