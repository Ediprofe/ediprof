# **Amplitud y Período**

¿Cómo hacemos que una onda sea más alta o más baja (como subir el volumen)? ¿Cómo hacemos que sea más rápida o más lenta (como acelerar una canción)? Los parámetros **Amplitud** ($A$) y **Período** ($T$) son los controles que nos permiten modificar la forma de las ondas.

---

## 🎯 ¿Qué vas a aprender?

- Cómo cambiar la altura de la onda (**Amplitud**).
- Cómo cambiar la velocidad de la onda (**Período**).
- Cómo leer estos valores directamente de la ecuación.
- Cómo escribir la ecuación de una onda si te dan sus características.

---

## 🔊 Amplitud (A): El Volumen

La amplitud es la distancia desde la línea central hasta la cima (o hasta el valle). Controla el **estiramiento vertical**.

Para $y = A \sin(x)$:
$$
\text{Amplitud} = |A|
$$

*   Si $A > 1$: La onda se hace más alta.
*   Si $A < 1$: La onda se aplana.
*   Si $A < 0$: La onda se invierte (efecto espejo), pero la amplitud sigue siendo positiva.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Efecto de la amplitud: A = 1, 2, 0.5</strong>
  </div>

![Efecto de la amplitud](/images/funciones/trigonometria/amplitud-comparacion.svg)

</div>

---

## ⏱️ Período (T): La Velocidad

El período es la longitud de un ciclo completo. Controla el **estiramiento horizontal**.
En la ecuación $y = \sin(Bx)$, el número $B$ es la **frecuencia angular** (qué tan rápido gira).

$$
\text{Período no es B, sino:} \quad T = \frac{2\pi}{|B|}
$$

*   Si $B > 1$: La onda va más rápido y el período se acorta (comprimida).
*   Si $B < 1$: La onda va más lento y el período se alarga (estirada).

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Efecto del período: B = 1, 2, 0.5</strong>
  </div>

![Efecto del período](/images/funciones/trigonometria/periodo-comparacion.svg)

</div>

**Nota Importante:** Para tangente y cotangente, la fórmula cambia porque su periodo natural es $\pi$.
$$
T_{\tan} = \frac{\pi}{|B|}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la amplitud de la función $y = -5\sin(x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Amplitud = $|A| = |-5| = 5$.
El signo negativo solo invierte la gráfica, no cambia la altura total.

**Respuesta:** $\boxed{5}$
</details>

---

### Ejercicio 2
Calcula el período de la función $y = \cos(4x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Aquí $B = 4$.
$T = \frac{2\pi}{B} = \frac{2\pi}{4} = \frac{\pi}{2}$.

**Respuesta:** $\boxed{\frac{\pi}{2}}$
</details>

---

### Ejercicio 3
Determina la amplitud y el período de $y = 3\sin(2x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$A = 3$, así que Amplitud = 3.
$B = 2$, así que Periodo = $\frac{2\pi}{2} = \pi$.

**Respuesta:** Amplitud **3**, Período **$\pi$**.
</details>

---

### Ejercicio 4
¿Cuál es el período de la función $y = \tan(3x)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ojo: la tangente tiene periodo base $\pi$.
$T = \frac{\pi}{3}$.

**Respuesta:** $\boxed{\frac{\pi}{3}}$
</details>

---

### Ejercicio 5
Escribe la ecuación de una función seno con amplitud 4 y período $\pi$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$A = 4$.
Si $T = \pi$, necesitamos encontrar $B$.
$\pi = \frac{2\pi}{B} \rightarrow B = 2$.

**Respuesta:** $\boxed{y = 4\sin(2x)}$
</details>

---

### Ejercicio 6
Calcula la frecuencia (número de ciclos en $2\pi$) de $y = \cos(\frac{x}{2})$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$B = 1/2$. Esto significa que completa medio ciclo en $2\pi$.
También: $T = \frac{2\pi}{0.5} = 4\pi$.

**Respuesta:** **0.5 ciclos** (o media onda).
</details>

---

### Ejercicio 7
¿Cuál es el rango de la función $y = -2\cos(3x)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La amplitud es 2.
La onda oscila entre -2 y 2.

**Respuesta:** $\boxed{[-2, 2]}$
</details>

---

### Ejercicio 8
Si duplicas el valor de $B$, ¿qué le pasa al período?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$T$ es inversamente proporcional a $B$.
Si $B$ se duplica, $T$ se reduce a la mitad.

**Respuesta:** **Se reduce a la mitad**.
</details>

---

### Ejercicio 9
Encuentra el período de $y = \sin(\pi x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$B = \pi$.
$T = \frac{2\pi}{\pi} = 2$.

**Respuesta:** $\boxed{2}$ (es un número entero, no radianes).
</details>

---

### Ejercicio 10
Compara $y = \sin(x)$ con $y = 2\sin(x)$. ¿Qué cambia?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La amplitud se duplica. La onda es dos veces más alta.
El período (velocidad) no cambia.

**Respuesta:** **Se estira verticalmente**.
</details>

---

## 🔑 Resumen

| Parámetro | Nombre | Fórmula | Efecto Visual |
| :---: | :---: | :---: | :--- |
| **A** | Amplitud | $\|A\|$ | Estiramiento Vertical (Altura) |
| **B** | Frecuencia Angular | $T = 2\pi/B$ | Estiramiento Horizontal (Acordeón) |

> **Conclusión:** $A$ controla la altura (Y), $B$ controla la anchura (X). ¡No los mezcles!
