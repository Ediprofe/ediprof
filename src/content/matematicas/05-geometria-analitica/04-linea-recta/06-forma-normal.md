# **Forma Normal de la Recta**

Imagina que estás en un barco (el origen) y ves una costa lejana (la recta). La forma más natural de describir dónde está la costa no es con pendientes, sino diciendo: "Está a 5 km en dirección Noreste". Esa es la **Forma Normal**: usa una distancia y un ángulo.

---

## 🎯 ¿Qué vas a aprender?

- Qué significan la $p$ (distancia) y la $\omega$ (ángulo normal).
- La ecuación $x \cos \omega + y \sin \omega - p = 0$.
- Cómo transformar la ecuación general a normal.
- Por qué es vital para calcular distancias.

---

## 🧭 Navegando con $p$ y $\omega$

Definimos una recta usando dos parámetros nuevos:
1.  **$p$ (Rho o p):** La distancia perpendicular desde el origen hasta la recta. **(Siempre positiva)**.
2.  **$\omega$ (Omega):** El ángulo que forma esa línea perpendicular con el eje X.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">La Normal (Perpendicular)</strong>
  </div>
  <img src="/images/geometria/analitica/forma-normal.svg" alt="Forma normal de la recta" style="width: 100%; height: auto;" />
</div>

La ecuación mágica es:
$$ x \cos \omega + y \sin \omega - p = 0 $$

---

## 🔄 Conversión: De General a Normal

Si tienes $Ax + By + C = 0$ y quieres convertirla, debes dividir toda la ecuación por un número especial llamado "el radical":

$$ r = \pm \sqrt{A^2 + B^2} $$

**¿Qué signo elijo?**
El objetivo es que $p$ (el término independiente final) sea **positivo**.
*   Si $C$ es negativo, usa el radical positivo (para que al pasar $C$ al otro lado quede positivo).
*   Si $C$ es positivo, usa el radical negativo.
*   En resumen: El radical debe tener **signo contrario a C**.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Ecuación Directa
Recta a distancia 5 del origen con ángulo normal de 60°.
*   $p = 5$.
*   $\omega = 60°$.
*   $\cos 60° = 1/2$, $\sin 60° = \sqrt{3}/2$.
*   Ecuación: $\frac{1}{2}x + \frac{\sqrt{3}}{2}y - 5 = 0$.

### Ejemplo 2: Convertir General a Normal
Ecuación: $3x - 4y - 10 = 0$.
1.  **Calcular Radical:** $\sqrt{3^2 + (-4)^2} = \sqrt{9+16} = 5$.
2.  **Elegir Signo:** $C = -10$ (Negativo). El radical debe ser **Positivo** ($+5$).
3.  **Dividir:**
    $$ \frac{3x}{5} - \frac{4y}{5} - \frac{10}{5} = 0 $$
    $$ \frac{3}{5}x - \frac{4}{5}y - 2 = 0 $$
    *   Distancia al origen ($p$) = 2.
    *   $\cos \omega = 3/5$, $\sin \omega = -4/5$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la ecuación si $p=3$ y $\omega=0°$ (Normal horizontal).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos 0 = 1, \sin 0 = 0$.
$x(1) + y(0) - 3 = 0 \Rightarrow x - 3 = 0$. (Recta vertical $x=3$).

**Respuesta:** $\boxed{x - 3 = 0}$
</details>

---

### Ejercicio 2
Escribe la ecuación si $p=2$ y $\omega=90°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos 90 = 0, \sin 90 = 1$.
$y - 2 = 0$. (Recta horizontal $y=2$).

**Respuesta:** $\boxed{y - 2 = 0}$
</details>

---

### Ejercicio 3
Convierte $4x + 3y - 12 = 0$ a normal.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Radical: $\sqrt{16+9}=5$. Signo opuesto a $C(-12)$: Positivo.
Dividir por 5.

**Respuesta:** $\boxed{\frac{4}{5}x + \frac{3}{5}y - \frac{12}{5} = 0}$
</details>

---

### Ejercicio 4
Convierte $5x + 12y + 26 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Radical: $\sqrt{25+144}=13$. Signo opuesto a $C(+26)$: **Negativo** (-13).
Dividir por -13.

**Respuesta:** $\boxed{-\frac{5}{13}x - \frac{12}{13}y - 2 = 0}$
</details>

---

### Ejercicio 5
¿Cuál es la distancia de la recta $3x + 4y - 20 = 0$ al origen?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Radical 5.
$p = |-20|/5 = 4$.

**Respuesta:** $\boxed{4}$
</details>

---

### Ejercicio 6
Si $\omega = 45°$ y $p=\sqrt{2}$, halla la ecuación.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{\sqrt{2}}{2}x + \frac{\sqrt{2}}{2}y - \sqrt{2} = 0$.
Multiplicando todo por $\sqrt{2}$: $x+y-2=0$.

**Respuesta:** $\boxed{x + y - 2 = 0}$
</details>

---

### Ejercicio 7
Halla $p$ si la ecuación normalizada es $0.6x + 0.8y - 6 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El término independiente negativo es $-p$. Así que $p=6$.

**Respuesta:** $\boxed{6}$
</details>

---

### Ejercicio 8
¿En qué cuadrante apunta el vector normal si $\cos \omega > 0$ y $\sin \omega < 0$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
X positiva, Y negativa. Cuarto Cuadrante.

**Respuesta:** **IV Cuadrante**
</details>

---

### Ejercicio 9
Convierte $x - y - 2 = 0$ a normal.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Radical $\sqrt{1+1}=\sqrt{2}$. Signo positivo.
$\frac{x}{\sqrt{2}} - \frac{y}{\sqrt{2}} - \frac{2}{\sqrt{2}} = 0$.
$\frac{\sqrt{2}}{2}x - \frac{\sqrt{2}}{2}y - \sqrt{2} = 0$.

**Respuesta:** $\boxed{\frac{\sqrt{2}}{2}x - \frac{\sqrt{2}}{2}y - \sqrt{2} = 0}$
</details>

---

### Ejercicio 10
Si la distancia al origen es 0, ¿cuánto vale $C$ en la general?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si pasa por el origen, $C=0$.

**Respuesta:** $\boxed{C = 0}$
</details>

---

## 🔑 Resumen

| Paso de Conversión | Acción |
| :--- | :--- |
| **1. Radical** | Calcular $\sqrt{A^2+B^2}$. |
| **2. Signo** | Mirar $C$. Elegir signo del radical **opuesto** a $C$. |
| **3. Dividir** | Dividir toda la ecuación general por el radical con signo. |

> **Conclusión:** La Forma Normal es la "forma de navegación". Nos dice qué tan lejos está la recta del centro del mundo (el origen) y en qué dirección mirar para encontrarla.
