---
title: "Ángulos Negativos"
---

# **Ángulos Negativos**

Hasta ahora hemos girado siempre en sentido antihorario, como se hace usualmente en matemáticas. Pero, ¿qué pasa si giramos al revés? Los **ángulos negativos** aparecen cuando medimos en sentido horario, y aprender a calcularlos es crucial para no confundirte con signos.

---

## 🎯 ¿Qué vas a aprender?

- Qué significa geométricamente un ángulo negativo.
- La equivalencia entre ángulos negativos y positivos (coterminales).
- Las propiedades de paridad: por qué el coseno "se come" el signo menos y el seno no.
- Cómo calcular rápidamente funciones trigonométricas de valores negativos.

---

## 🔄 El Sentido del Giro

En trigonometría estándar:
*   **Giro Antihorario (contra reloj):** Ángulos Positivos ($+30°$).
*   **Giro Horario (a favor del reloj):** Ángulos Negativos ($-30°$).

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Ángulos positivos vs negativos</strong>
  </div>

![Ángulos negativos](/images/trigonometria/circulo-unitario/angulos-negativos.svg)

</div>

GEOMÉTRICAMENTE, un ángulo negativo llega al mismo lugar que uno positivo grande.
> **Regla de oro:** Si sumas $360°$ a cualquier ángulo negativo, obtienes su equivalente positivo.
> $$-30° + 360° = 330°$$

---

## 🪞 Identidades de Paridad (Simetría)

Si observas el círculo unitario, verás una simetría interesante respecto al eje X. Si giras $\theta$ hacia arriba o $-\theta$ hacia abajo:
1.  La coordenada $x$ (Coseno) es **la misma**.
2.  La coordenada $y$ (Seno) es **la opuesta** (cambia de signo).

De ahí nacen las reglas de paridad:

### 1. Función Par (Coseno y Secante)
El signo negativo **desaparece**.

$$
\cos(-\theta) = \cos(\theta)
$$

$$
\sec(-\theta) = \sec(\theta)
$$

### 2. Función Impar (Las demás)
El signo negativo **sale fuera** de la función.

$$
\sin(-\theta) = -\sin(\theta)
$$

$$
\tan(-\theta) = -\tan(\theta)
$$

$$
\csc(-\theta) = -\csc(\theta)
$$

$$
\cot(-\theta) = -\cot(\theta)
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Calcular $\cos(-60°)$

**Método 1: Paridad**
Como el coseno es par:

$$
\cos(-60°) = \cos(60°) = 0.5
$$

**Método 2: Coterminal**
Sumamos 360°:

$$
-60° + 360° = 300°
$$

$$
\cos(300°) = 0.5 \quad \text{(QIV)}
$$

**Resultado:** $\boxed{0.5}$

---

### Ejemplo 2: Calcular $\sin(-45°)$

**Método 1: Paridad**
Como el seno es impar:

$$
\sin(-45°) = -\sin(45°) = -\frac{\sqrt{2}}{2}
$$

**Resultado:** $\boxed{-\frac{\sqrt{2}}{2}}$

---

### Ejemplo 3: Calcular $\tan(-150°)$

**Método 1: Paridad**
La tangente es impar:

$$
\tan(-150°) = -\tan(150°)
$$

Sabemos que $\tan(150°) = -\frac{\sqrt{3}}{3}$ (QII, Ref 30°).
Entonces:

$$
-(-\frac{\sqrt{3}}{3}) = +\frac{\sqrt{3}}{3}
$$

**Resultado:** $\boxed{\frac{\sqrt{3}}{3}}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el valor de $\sin(-30°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sin(-30°) = -\sin(30°)$.
Sabemos que $\sin(30°) = 0.5$.

**Respuesta:** $\boxed{-0.5}$
</details>

---

### Ejercicio 2
Calcula el valor de $\cos(-30°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos(-30°) = \cos(30°)$.
Sabemos que $\cos(30°) = \frac{\sqrt{3}}{2}$.

**Respuesta:** $\boxed{\frac{\sqrt{3}}{2}}$
</details>

---

### Ejercicio 3
Calcula el valor de $\tan(-45°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan(-45°) = -\tan(45°)$.
Sabemos que $\tan(45°) = 1$.

**Respuesta:** $\boxed{-1}$
</details>

---

### Ejercicio 4
Encuentra el ángulo positivo equivalente a $-90°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$-90° + 360° = 270°$.

**Respuesta:** $\boxed{270°}$
</details>

---

### Ejercicio 5
Calcula $\sec(-60°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La secante es par, igual que el coseno.
$\sec(-60°) = \sec(60°)$.
$\sec(60°) = 1/\cos(60°) = 1/0.5 = 2$.

**Respuesta:** $\boxed{2}$
</details>

---

### Ejercicio 6
Calcula $\csc(-30°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La cosecante es impar.
$\csc(-30°) = -\csc(30°)$.
$\csc(30°) = 1/\sin(30°) = 1/0.5 = 2$.

**Respuesta:** $\boxed{-2}$
</details>

---

### Ejercicio 7
Determina el signo de $\cos(-100°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos(-100°) = \cos(100°)$.
100° está en el Cuadrante II.
El coseno en QII es negativo.

**Respuesta:** **Negativo (-)**
</details>

---

### Ejercicio 8
Determina el signo de $\sin(-200°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sin(-200°) = -\sin(200°)$.
200° está en QIII, donde el seno es negativo (-).
Entonces: $-(\text{Negativo}) = \text{Positivo}$.

**Alternativa:** $-200° + 360° = 160°$ (QII), donde el seno es positivo.

**Respuesta:** **Positivo (+)**
</details>

---

### Ejercicio 9
Calcula $\tan(-180°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan(-180°) = -\tan(180°)$.
$\tan(180°) = 0$.
$-0 = 0$.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 10
Si $\sin(-\theta) = 0.8$, ¿cuánto vale $\sin(\theta)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sabemos que $\sin(-\theta) = -\sin(\theta)$.
Entonces: $-\sin(\theta) = 0.8$.
Multiplicamos por -1.

**Respuesta:** $\boxed{-0.8}$
</details>

---

## 🔑 Resumen

| Función | Tipo de Simetría | Regla Matemática |
| :--- | :--- | :--- |
| **Coseno / Secante** | **Par** | El signo se ignora: $f(-x) = f(x)$ |
| **Seno / Tangente** | **Impar** | El signo sale fuera: $f(-x) = -f(x)$ |

> **Conclusión:** Cuando veas un ángulo negativo dentro de un coseno, ignóralo. Si está dentro de un seno o tangente, saca el signo afuera. ¡Así de simple!
