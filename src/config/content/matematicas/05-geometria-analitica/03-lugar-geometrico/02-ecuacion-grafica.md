---
title: "Ecuación y Gráfica"
---

# **Ecuación y Gráfica**

Una ecuación algebraica ($y = x^2$) y una curva dibujada en un papel son la misma cosa vista desde dos ángulos distintos. Si tienes la ecuación, puedes dibujar la gráfica. Si tienes la gráfica, puedes deducir la ecuación. Hoy aprenderemos a viajar entre estos dos mundos.

---

## 🎯 ¿Qué vas a aprender?

- Cómo graficar cualquier ecuación usando **tabulación**.
- Cómo encontrar los **interceptos** (cortes con los ejes).
- Cómo detectar **simetrías** para ahorrar trabajo.
- Cómo deducir la ecuación viendo el dibujo.

---

## 📉 De la Ecuación a la Gráfica

El método infalible (aunque lento) es la **Tabulación**. Haces una tabla "x vs y", calculas puntos y los unes.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Tabulación de una Parábola</strong>
  </div>
  <img src="/images/geometria/analitica/parabola-tabulacion.svg" alt="Gráfica de parábola por tabulación" style="width: 100%; height: auto;" />
</div>

### Los Atajos: Interceptos
En lugar de calcular mil puntos, busca los más importantes:
1.  **Corte con X:** Haz $y=0$ y despeja $x$.
2.  **Corte con Y:** Haz $x=0$ y despeja $y$.

---

## 🪞 El Poder de la Simetría

Si sabes que una mariposa es simétrica, solo necesitas dibujar el lado izquierdo y copiarlo al derecho. En matemáticas es igual.

| Tipo | Prueba Matemática | Ejemplo Visual |
| :--- | :--- | :--- |
| **Simetría Eje Y** | Si cambias $x \to -x$, la ecuación NO cambia. | Una parábola $y=x^2$. |
| **Simetría Eje X** | Si cambias $y \to -y$, la ecuación NO cambia. | Una parábola acostada $x=y^2$. |
| **Simetría Origen** | Si cambias ambos signos, NO cambia. | Una cúbica $y=x^3$. |

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Graficar una Recta
Ecuación: $y = 2x - 4$.
1.  **Intercepto Y ($x=0$):** $y = 2(0) - 4 = -4$. Punto $(0, -4)$.
2.  **Intercepto X ($y=0$):** $0 = 2x - 4 \Rightarrow 2x = 4 \Rightarrow x=2$. Punto $(2, 0)$.
Unes los dos puntos y extiendes la línea. ¡Listo!

### Ejemplo 2: Simetría de una Circunferencia
Ecuación: $x^2 + y^2 = 25$.
*   Cambio $x \to -x$: $(-x)^2 + y^2 = 25 \Rightarrow x^2 + y^2 = 25$. (¡Igual!) -> Simetría Eje Y.
*   Cambio $y \to -y$: $x^2 + (-y)^2 = 25 \Rightarrow x^2 + y^2 = 25$. (¡Igual!) -> Simetría Eje X.
*   Tiene simetría total (como un círculo debe tener).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el intercepto Y de $y = x^2 + 5x + 6$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Haz $x=0$.
$y = 0 + 0 + 6 = 6$.

**Respuesta:** $\boxed{(0, 6)}$
</details>

---

### Ejercicio 2
Encuentra los interceptos X de $y = x^2 - 9$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Haz $y=0$.
$x^2 - 9 = 0 \Rightarrow x^2 = 9 \Rightarrow x = \pm 3$.

**Respuesta:** $\boxed{(3,0) \text{ y } (-3,0)}$
</details>

---

### Ejercicio 3
¿La función $y = x^4$ es simétrica respecto al eje Y?

<details>
<summary>Ver solución</summary>
<br>
**Razonamiento:**
$(-x)^4 = x^4$. La ecuación no cambia.

**Respuesta:** **Sí**
</details>

---

### Ejercicio 4
Si una gráfica pasa por $(2, 3)$ y es simétrica al eje X, ¿por qué otro punto pasa obligatoriamente?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Reflejo vertical. Mantén $x$, invierte $y$.

**Respuesta:** $\boxed{(2, -3)}$
</details>

---

### Ejercicio 5
Halla el intercepto Y de $3x + 4y = 12$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x=0 \Rightarrow 4y = 12 \Rightarrow y = 3$.

**Respuesta:** $\boxed{(0, 3)}$
</details>

---

### Ejercicio 6
Grafica mentalmente $y = |x|$. ¿Tiene simetría?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es una V. Es idéntica a izquierda y derecha del eje Y.

**Respuesta:** **Simetría respecto al Eje Y**
</details>

---

### Ejercicio 7
¿Cuántos interceptos tiene $x^2 + y^2 = 1$ con los ejes?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Corte X: $x^2=1 \Rightarrow \pm 1$. Corte Y: $y^2=1 \Rightarrow \pm 1$.
Total 4 puntos: $(1,0), (-1,0), (0,1), (0,-1)$.

**Respuesta:** $\boxed{4}$
</details>

---

### Ejercicio 8
Deduce la ecuación si la gráfica es una recta horizontal que pasa por $y=5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$y$ siempre es 5, sin importar $x$.

**Respuesta:** $\boxed{y = 5}$
</details>

---

### Ejercicio 9
Determina si $y = x^3$ pasa por el origen.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si $x=0$, $y=0^3=0$. Sí pasa.

**Respuesta:** **Sí**
</details>

---

### Ejercicio 10
Si una ecuación no cambia al reemplazar $x \leftrightarrow y$ (como $x+y=1$), ¿qué simetría tiene?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Simetría respecto a la recta $y=x$ (diagonal a 45°).

**Respuesta:** **Simetría diagonal**
</details>

---

## 🔑 Resumen

| ¿Qué buscas? | ¿Qué haces? |
| :--- | :--- |
| **Corte con el Eje de pie (Y)** | Matas a la $x$ ($x=0$). |
| **Corte con el Eje acostado (X)** | Matas a la $y$ ($y=0$). |
| **Simetría de Espejo** | Pruebas cambiando signos. |

> **Conclusión:** No grafiques a ciegas. Busca los puntos clave (interceptos) y usa la simetría para trabajar la mitad. "Trabaja inteligentemente, no duramente".
