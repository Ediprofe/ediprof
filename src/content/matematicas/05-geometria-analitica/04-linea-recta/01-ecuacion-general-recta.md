# **Ecuación General de la Recta**

Hasta ahora hemos visto rectas como $y = 3x+2$ (Forma Pendiente-Intersección). Pero, ¿qué pasa con las rectas verticales como $x=5$? No encajan ahí. Para tener una fórmula universal que cubra **todas** las rectas posibles, los matemáticos inventaron la **Ecuación General**.

---

## 🎯 ¿Qué vas a aprender?

- La forma estándar $Ax + By + C = 0$.
- Cómo extraer la pendiente y los cortes si te dan la ecuación desordenada.
- Cómo transformar cualquier ecuación a esta forma "elegante".
- El truco para identificar rectas horizontales y verticales al ojo.

---

## 🎩 La Fórmula Universal

$$
Ax + By + C = 0
$$

Donde $A, B, C$ son números enteros (preferiblemente).
*   **A y B** no pueden ser ambos cero (si no, no hay recta).
*   **A** debe ser positivo (por convención de elegancia).

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">La Recta General</strong>
  </div>
  <img src="/images/geometria/analitica/ecuacion-general.svg" alt="Ecuación general de la recta" style="width: 100%; height: auto;" />
</div>

---

## 🔍 Extrayendo Información (Hacking)

Si te dan $2x + 3y - 6 = 0$, ¿cómo sabes su pendiente o dónde corta?
Solo despeja la $y$:
$$ 3y = -2x + 6 $$
$$ y = -\frac{2}{3}x + 2 $$

¡Ajá!
*   **Pendiente ($m$):** $-2/3$ (Lo que acompaña a $x$).
*   **Corte Y ($b$):** $2$ (El número solo).

**Fórmulas Directas:**
*   $m = -A/B$
*   $b = -C/B$
*   $a = -C/A$ (Corte con X)

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Convertir a General
Convierte $y = \frac{1}{2}x - 3$ a la forma general.
1.  Eliminar fracciones: Multiplica todo por 2.
    $2y = x - 6$.
2.  Mover todo a un lado (preferible $x$ positiva).
    $0 = x - 2y - 6$.
    **Resultado:** $\boxed{x - 2y - 6 = 0}$.

### Ejemplo 2: Hacking de la Ecuación
Dada $4x - 2y + 8 = 0$, halla $m$ y los cortes.
*   **Pendiente:** $m = -A/B = -4 / (-2) = 2$.
*   **Corte Y:** Si $x=0$, $-2y+8=0 \Rightarrow 2y=8 \Rightarrow y=4$.
*   **Corte X:** Si $y=0$, $4x+8=0 \Rightarrow 4x=-8 \Rightarrow x=-2$.

### Ejemplo 3: Rectas Especiales
*   $3x - 12 = 0 \Rightarrow 3x = 12 \Rightarrow x = 4$. (**Vertical**).
*   $2y + 10 = 0 \Rightarrow 2y = -10 \Rightarrow y = -5$. (**Horizontal**).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la ecuación general si $A=2, B=3, C=-6$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sustituir en $Ax+By+C=0$.

**Respuesta:** $\boxed{2x + 3y - 6 = 0}$
</details>

---

### Ejercicio 2
Convierte $y = 3x + 1$ a general.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$0 = 3x - y + 1$.

**Respuesta:** $\boxed{3x - y + 1 = 0}$
</details>

---

### Ejercicio 3
Halla la pendiente de $5x + 10y - 20 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = -A/B = -5/10 = -1/2$.

**Respuesta:** $\boxed{-0.5}$
</details>

---

### Ejercicio 4
Halla el corte con el eje X de $x - y + 5 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Haz $y=0$. $x+5=0 \Rightarrow x=-5$.

**Respuesta:** $\boxed{(-5, 0)}$
</details>

---

### Ejercicio 5
¿La recta $0x + 2y - 8 = 0$ es horizontal o vertical?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$A=0$. Queda $2y=8 \Rightarrow y=4$.

**Respuesta:** **Horizontal**
</details>

---

### Ejercicio 6
Convierte $y = -\frac{2}{5}x$ a general.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Multiplica por 5: $5y = -2x$.
Pasa $2x$ a sumar: $2x + 5y = 0$.

**Respuesta:** $\boxed{2x + 5y = 0}$
</details>

---

### Ejercicio 7
Si $C=0$, ¿por dónde pasa obligatoriamente la recta?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si $x=0$ y $y=0$, $A(0)+B(0)=0$. Cumple la ecuación.

**Respuesta:** **Por el Origen (0,0)**
</details>

---

### Ejercicio 8
Halla $k$ para que $kx + 3y - 9 = 0$ tenga pendiente $-2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = -A/B = -k/3$.
$-k/3 = -2 \Rightarrow -k = -6 \Rightarrow k=6$.

**Respuesta:** $\boxed{6}$
</details>

---

### Ejercicio 9
Escribe la ecuación general de la recta vertical que pasa por $(3, 5)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Vertical en $x=3$.
$x - 3 = 0$.

**Respuesta:** $\boxed{x - 3 = 0}$
</details>

---

### Ejercicio 10
Convierte $x/2 + y/3 = 1$ a general.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Multiplica por 6 (MCM).
$3x + 2y = 6 \Rightarrow 3x + 2y - 6 = 0$.

**Respuesta:** $\boxed{3x + 2y - 6 = 0}$
</details>

---

## 🔑 Resumen

| Si falta... | La Ecuación es... | La Recta es... |
| :--- | :--- | :--- |
| **A ($Ax$)** | $By + C = 0$ | Horizontal ($y=k$). |
| **B ($By$)** | $Ax + C = 0$ | Vertical ($x=k$). |
| **C ($C$)** | $Ax + By = 0$ | Pasa por el Origen. |
| **Nada** | $Ax + By + C = 0$ | Oblicua (Normal). |

> **Conclusión:** La ecuación general es como el "traje de etiqueta" de la recta. Siempre igualamos a cero y dejamos todo limpio, sin fracciones. Es la forma más profesional de presentar tu respuesta.
