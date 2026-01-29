# **Recta que Pasa por Dos Puntos**

A veces no tienes la pendiente. A veces solo tienes dos puntos en un mapa, como "Ciudad A" y "Ciudad B", y quieres dibujar la carretera recta que las une. ¿Cómo encontramos la ecuación de esa carretera? Aprendiendo a calcular nosotros mismos la pendiente.

---

## 🎯 ¿Qué vas a aprender?

- Cómo obtener la ecuación de una recta dados dos puntos cualquiera $(x_1, y_1)$ y $(x_2, y_2)$.
- El método de dos pasos: calcular $m$ y luego usar Punto-Pendiente.
- La fórmula directa (para los que les gusta memorizar).
- Qué hacer si los puntos están alineados vertical u horizontalmente.

---

## 🏗️ El Método de Construcción

No necesitas una fórmula nueva y complicada. Solo necesitas combinar dos cosas que ya sabes:
1.  **Fórmula de la Pendiente:** $m = \frac{y_2 - y_1}{x_2 - x_1}$.
2.  **Forma Punto-Pendiente:** $y - y_1 = m(x - x_1)$.

### Pasos:
1.  Usa los dos puntos para calcular $m$.
2.  Elige **cualquiera** de los dos puntos (el que te parezca más fácil).
3.  Sustituye en la ecuación Punto-Pendiente.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">De Dos Puntos a una Recta</strong>
  </div>
  <img src="/images/geometria/analitica/recta-dos-puntos.svg" alt="Recta por dos puntos" style="width: 100%; height: auto;" />
</div>

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El Caso Estándar
Encuentra la recta que pasa por $A(1, 2)$ y $B(3, 8)$.

1.  **Calculamos $m$:**
    $$ m = \frac{8 - 2}{3 - 1} = \frac{6}{2} = 3 $$
2.  **Usamos Punto-Pendiente:** Escojo $A(1, 2)$.
    $$ y - 2 = 3(x - 1) $$
3.  **Simplificamos:**
    $y - 2 = 3x - 3$
    **Resultado:** $\boxed{y = 3x - 1}$.

### Ejemplo 2: Puntos con Negativos
Puntos $P(-2, 5)$ y $Q(4, -1)$.

1.  **Calculamos $m$:**
    $$ m = \frac{-1 - 5}{4 - (-2)} = \frac{-6}{6} = -1 $$
2.  **Usamos Punto-Pendiente:** Escojo $Q(4, -1)$ (puedes usar $P$ si quieres).
    $$ y - (-1) = -1(x - 4) $$
    $$ y + 1 = -x + 4 $$
3.  **Simplificamos:**
    $y = -x + 3$
    **Resultado:** $\boxed{y = -x + 3}$.

### Ejemplo 3: Recta Horizontal (Trampa)
Puntos $A(2, 5)$ y $B(7, 5)$.
1.  **Calculamos $m$:**
    $$ m = \frac{5 - 5}{7 - 2} = \frac{0}{5} = 0 $$
2.  **Ecuación:**
    $y - 5 = 0(x - 2)$
    $y - 5 = 0$
    **Resultado:** $\boxed{y = 5}$. (Lógico, la altura $y$ siempre es 5).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Halla la ecuación para $(0,0)$ y $(4,4)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = 4/4 = 1$. Pasa por origen.

**Respuesta:** $\boxed{y = x}$
</details>

---

### Ejercicio 2
Halla la ecuación para $(1,3)$ y $(2,5)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = (5-3)/(2-1) = 2$.
$y - 3 = 2(x - 1) \Rightarrow y = 2x + 1$.

**Respuesta:** $\boxed{y = 2x + 1}$
</details>

---

### Ejercicio 3
Halla la ecuación para $(2,0)$ y $(0,3)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = (3-0)/(0-2) = -1.5$.
$b=3$ (corte Y).

**Respuesta:** $\boxed{y = -1.5x + 3}$
</details>

---

### Ejercicio 4
Halla la ecuación para $(-1, -2)$ y $(-3, -4)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = (-4 - (-2)) / (-3 - (-1)) = -2/-2 = 1$.
$y - (-2) = 1(x - (-1)) \Rightarrow y + 2 = x + 1$.

**Respuesta:** $\boxed{y = x - 1}$
</details>

---

### Ejercicio 5
Halla la ecuación para $(5,1)$ y $(5,10)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = 9/0$ (Indefinido). Recta vertical en $x=5$.

**Respuesta:** $\boxed{x = 5}$
</details>

---

### Ejercicio 6
Una recta pasa por $(10, 10)$ y $(20, 20)$. ¿Cuál es?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m=1$. Pasa por origen (extrapolando).

**Respuesta:** $\boxed{y = x}$
</details>

---

### Ejercicio 7
Halla la pendiente de la recta que pasa por $(a, 0)$ y $(0, b)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = (b-0)/(0-a)$.

**Respuesta:** $\boxed{-\frac{b}{a}}$
</details>

---

### Ejercicio 8
Si la recta pasa por $(1,2)$ y $(3,2)$, ¿es horizontal o vertical?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Las $y$ son iguales.

**Respuesta:** **Horizontal**
</details>

---

### Ejercicio 9
Halla la ecuación general para $(1,1)$ y $(2,3)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m=2$. $y-1 = 2(x-1) \Rightarrow y-1 = 2x-2$.
$2x - y - 1 = 0$.

**Respuesta:** $\boxed{2x - y - 1 = 0}$
</details>

---

### Ejercicio 10
¿Importa qué punto elijas (punto 1 o punto 2) para la ecuación final?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La recta es la misma, los puntos solo son "estaciones" en ella.

**Respuesta:** **No, da lo mismo**
</details>

---

## 🔑 Resumen

| Paso | Acción |
| :--- | :--- |
| **1** | Calcular pendiente $m$. |
| **2** | Elegir tu punto favorito. |
| **3** | Usar la ecuación Punto-Pendiente. |
| **Ojo** | Si $x_1 = x_2$, es vertical ($x = x_1$). Si $y_1 = y_2$, es horizontal ($y = y_1$). |

> **Conclusión:** Con dos puntos tienes el poder de crear un mundo. O al menos, de crear una recta. Recuerda siempre el orden al restar para no cambiar el signo de la pendiente.
