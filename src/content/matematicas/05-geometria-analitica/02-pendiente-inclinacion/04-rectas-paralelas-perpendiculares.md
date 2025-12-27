# **Rectas Paralelas y Perpendiculares**

En las calles de una ciudad moderna, casi todas las avenidas son paralelas (nunca se cruzan) o perpendiculares (se cruzan formando una "L" perfecta). En geometría analítica, no necesitamos un mapa para saber esto; solo necesitamos comparar sus **pendientes**.

---

## 🎯 ¿Qué vas a aprender?

- Cómo identificar si dos rectas son paralelas mirando sus pendientes.
- La regla mágica de las perpendiculares (inverso negativo).
- Cómo crear la ecuación de una recta paralela o perpendicular a otra.
- Por qué las rectas verticales y horizontales son los mejores amigos.

---

## 🛤️ Rectas Paralelas

Dos rectas son paralelas si tienen la **misma inclinación**. Si suben al mismo ritmo, nunca se chocarán.

$$
m_1 = m_2
$$

> **Ejemplo:** Una rampa con pendiente 2 y otra rampa con pendiente 2 son paralelas.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Relación entre Pendientes</strong>
  </div>
  <img src="/images/geometria/analitica/paralelas-perpendiculares.svg" alt="Rectas paralelas y perpendiculares" style="width: 100%; height: auto;" />
</div>

---

## ⚔️ Rectas Perpendiculares

Dos rectas son perpendiculares si forman un ángulo de 90° al cruzarse.
La relación entre sus pendientes es más curiosa: Son **recíprocas negativas**.

$$
m_1 \cdot m_2 = -1
$$
O despejando:
$$
m_2 = -\frac{1}{m_1}
$$

> **Traducción:** Voltea la fracción y cámbiale el signo.
> Si $m_1 = \frac{2}{3}$, entonces $m_2 = -\frac{3}{2}$.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: ¿Son Paralelas?
Recta A: $y = 3x + 2$ ($m=3$)
Recta B: $y = 3x - 5$ ($m=3$)
Como $3 = 3$, **SÍ son paralelas**.

### Ejemplo 2: ¿Son Perpendiculares?
Recta A: $m = 4$
Recta B: $m = -0.25$
Multiplicamos: $4 \cdot (-0.25) = -1$.
**SÍ son perpendiculares**.

### Ejemplo 3: Hallar la Perpendicular
Encuentra la pendiente perpendicular a $m = -5$.
1.  Invertimos 5 (es como $5/1$) $\to$ $1/5$.
2.  Cambiamos signo (de negativo a positivo) $\to$ $1/5$.
**Resultado:** $m_{\perp} = 0.2$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si $m_1 = 2/3$, halla la pendiente paralela.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Deben ser iguales.

**Respuesta:** $\boxed{2/3}$
</details>

---

### Ejercicio 2
Si $m_1 = 2/3$, halla la pendiente perpendicular.

<details>
<summary>Ver solución</summary>
<br>
**Razonamiento:**
Inverso negativo.
Voltear 2/3 -> 3/2. Cambiar signo -> -3/2.

**Respuesta:** $\boxed{-3/2}$
</details>

---

### Ejercicio 3
La recta $y = 5x$ es paralela a $y = 5x + 10$. ¿Verdadero o Falso?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ambas tienen $m=5$.

**Respuesta:** **Verdadero**
</details>

---

### Ejercicio 4
Halla la perpendicular a $m = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Inverso de 1 es 1. Signo opuesto es -1.

**Respuesta:** $\boxed{-1}$
</details>

---

### Ejercicio 5
¿Son perpendiculares $y=x$ y $y=-x$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$1 \cdot (-1) = -1$. Sí.

**Respuesta:** **Sí**
</details>

---

### Ejercicio 6
Una calle va de Norte a Sur (vertical). Otra va de Este a Oeste (horizontal). ¿Cómo son sus pendientes?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Una es indefinida, la otra es 0. Son perpendiculares geométricamente.

**Respuesta:** **Perpendiculares**
</details>

---

### Ejercicio 7
Halla $k$ para que $y=kx$ sea perpendicular a $y=2x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$k \cdot 2 = -1 \Rightarrow k = -1/2$.

**Respuesta:** $\boxed{-0.5}$
</details>

---

### Ejercicio 8
Halla la pendiente paralela a la recta que pasa por $(0,0)$ y $(1,4)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = 4/1 = 4$. Paralela es la misma.

**Respuesta:** $\boxed{4}$
</details>

---

### Ejercicio 9
Si dos rectas tienen pendientes negativas, ¿pueden ser perpendiculares?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No. Negativo $\cdot$ Negativo = Positivo. El producto debe ser $-1$. Una debe subir y la otra bajar.

**Respuesta:** **No**
</details>

---

### Ejercicio 10
Recta A: $2x + y = 0$. Recta B: $x - 2y = 0$. ¿Relación?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Despejar y.
A: $y = -2x$ ($m=-2$).
B: $-2y = -x \Rightarrow y = 0.5x$ ($m=0.5$).
$-2 \cdot 0.5 = -1$.

**Respuesta:** **Perpendiculares**
</details>

---

## 🔑 Resumen

| Relación | Regla de Pendientes | Truco Visual |
| :--- | :--- | :--- |
| **Paralelas** | $m_1 = m_2$ | Vías del tren. |
| **Perpendiculares** | $m_1 = -\frac{1}{m_2}$ | Cruz "+" o Esquina "L". |

> **Conclusión:** Si quieres construir algo recto y cuadrado (como una casa), necesitas dominar las perpendiculares. Si quieres que algo no choque nunca (como carriles de autopista), necesitas las paralelas.
