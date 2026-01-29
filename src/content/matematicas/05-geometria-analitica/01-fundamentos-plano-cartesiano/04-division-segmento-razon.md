# **División de un Segmento en una Razón Dada**

Ya sabemos partir un segmento a la mitad (punto medio). Pero, ¿qué pasa si queremos partirlo en tres pedazos? ¿O si queremos un punto que esté mucho más cerca del principio que del final? Aquí es donde entra el concepto de **razón**.

---

## 🎯 ¿Qué vas a aprender?

- Qué significa "dividir en una razón $r$".
- La fórmula para encontrar ese punto exacto.
- La diferencia entre división interna y externa (cuando el punto se sale del segmento).
- Cómo encontrar los puntos que parten un segmento en 3 partes iguales (trisección).

---

## ⚖️ ¿Qué es la Razón?

Imagina una cuerda de 5 metros.
Si pones una marca a 1 metro del inicio, te quedan 4 metros hasta el final.
La relación entre "lo que caminaste" (1m) y "lo que falta" (4m) es $1$ a $4$.
Matemáticamente, la razón es $r = \frac{1}{4} = 0.25$.

> **Definición:** La razón $r$ es la comparación entre la distancia del inicio al punto ($P$) y la distancia del punto al final ($B$).
> $$ r = \frac{AP}{PB} $$

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">La Razón r = m/n</strong>
  </div>
  <img src="/images/geometria/analitica/division-segmento.svg" alt="División de un segmento en razón dada" style="width: 100%; height: auto;" />
</div>

---

## 🧬 La Fórmula General

Para encontrar las coordenadas $(x, y)$ del punto $P$ que divide al segmento $A(x_1, y_1)$ y $B(x_2, y_2)$ en una razón $r$, usamos:

$$
x = \frac{x_1 + r \cdot x_2}{1 + r} \quad , \quad y = \frac{y_1 + r \cdot y_2}{1 + r}
$$

> **Nota:** A veces verás la razón escrita como $m:n$ (ej. 2:3). En ese caso $r = m/n$. La fórmula es la misma.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Razón Simple
Encuentra el punto $P$ que divide al segmento $A(1, 2)$ y $B(7, 8)$ en razón $r = \frac{1}{2}$ (o 1:2).

**Paso 1: Identificar datos**
$x_1=1, x_2=7, r=0.5$
$y_1=2, y_2=8, r=0.5$

**Paso 2: Calcular X**
$$ x = \frac{1 + 0.5(7)}{1 + 0.5} = \frac{1 + 3.5}{1.5} = \frac{4.5}{1.5} = 3 $$

**Paso 3: Calcular Y**
$$ y = \frac{2 + 0.5(8)}{1 + 0.5} = \frac{2 + 4}{1.5} = \frac{6}{1.5} = 4 $$

**Resultado:** $\boxed{P(3, 4)}$.

### Ejemplo 2: División Externa (Razón Negativa)
Si el punto está **fuera** del segmento (en la prolongación), la razón es negativa.
Halla el punto que divide a $A(2, 2)$ y $B(5, 5)$ en razón $r = -2$.

**Paso 1: Calcular X**
$$ x = \frac{2 + (-2)(5)}{1 + (-2)} = \frac{2 - 10}{-1} = \frac{-8}{-1} = 8 $$

**Paso 2: Calcular Y**
$$ y = \frac{2 + (-2)(5)}{1 + (-2)} = \frac{-8}{-1} = 8 $$

**Resultado:** $\boxed{P(8, 8)}$.
(El punto se "salió" del segmento hacia el lado de B).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el punto que divide a $A(2, 1)$ y $B(8, 7)$ en razón $r=1$. (Pista: es el punto medio).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x = (2 + 1\cdot 8)/(1+1) = 5$.
$y = (1 + 1\cdot 7)/(1+1) = 4$.

**Respuesta:** $\boxed{(5, 4)}$
</details>

---

### Ejercicio 2
Divide el segmento $A(-4, 0)$ y $B(6, 0)$ en razón $r = 3/2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x = \frac{-4 + 1.5(6)}{1+1.5} = \frac{-4 + 9}{2.5} = \frac{5}{2.5} = 2$.
$y = 0$.

**Respuesta:** $\boxed{(2, 0)}$
</details>

---

### Ejercicio 3
Encuentra el punto que divide a $A(0, 0)$ y $B(10, 0)$ en razón $r = 1/4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x = \frac{0 + 0.25(10)}{1.25} = \frac{2.5}{1.25} = 2$.
$y = 0$.

**Respuesta:** $\boxed{(2, 0)}$
</details>

---

### Ejercicio 4
Encuentra el primer punto de trisección de $A(1, 1)$ a $B(7, 7)$. (Razón $r=1/2$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x = (1 + 0.5(7))/1.5 = 4.5/1.5 = 3$.
$y = 3$.

**Respuesta:** $\boxed{(3, 3)}$
</details>

---

### Ejercicio 5
Encuentra el segundo punto de trisección del ejercicio anterior. (Razón $r=2/1=2$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x = (1 + 2(7))/3 = 15/3 = 5$.
$y = 5$.

**Respuesta:** $\boxed{(5, 5)}$
</details>

---

### Ejercicio 6
Si la razón es $r=0$, ¿dónde está el punto $P$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x = (x_1 + 0)/1 = x_1$.
El punto $P$ coincide con el punto inicial $A$.

**Respuesta:** **En el punto inicial A**
</details>

---

### Ejercicio 7
Si $AP$ es el doble que $PB$, ¿cuál es la razón $r$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$r = AP/PB = 2/1 = 2$.

**Respuesta:** $\boxed{2}$
</details>

---

### Ejercicio 8
Calcula el punto con razón $r=-1/2$ para $A(0,0)$ y $B(6,6)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x = (0 - 0.5(6))/(1-0.5) = -3/0.5 = -6$.
$y = -6$.
División externa (lado de A).

**Respuesta:** $\boxed{(-6, -6)}$
</details>

---

### Ejercicio 9
¿Por qué la razón no puede ser $r = -1$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El denominador de la fórmula es $1+r$. Si $r=-1$, dividimos por cero.
Geométricamente, implicaría un punto al infinito (líneas paralelas).

**Respuesta:** **División por cero (Infinito)**
</details>

---

### Ejercicio 10
Si $P$ está a 3/4 del camino, ¿cuál es la razón? (Cuidado).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si caminas 3 partes, te queda 1 parte.
La razón es "caminado / falta".
$r = 3/1 = 3$.

**Respuesta:** $\boxed{3}$
</details>

---

## 🔑 Resumen

| Tipo de Razón ($r$) | Ubicación de P |
| :--- | :--- |
| **$r > 0$** | Dentro del segmento (Interna). |
| **$r = 1$** | Justo en el medio. |
| **$r < 0$** | Fuera del segmento (Externa). |
| **$r = 0$** | Coincide con $A$. |

> **Conclusión:** La razón es el "GPS" del segmento. Te dice exactamente qué tan lejos estás de $A$ comparado con $B$.
