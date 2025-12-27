# **Eliminación del Parámetro**

Si las ecuaciones paramétricas son la película, la ecuación rectangular es la fotografía final del recorrido. A veces queremos eliminar el tiempo ($t$) para ver simplemente la forma del camino ($y$ vs $x$).

---

## 🎯 ¿Qué vas a aprender?

- Método de Sustitución Directa.
- Identidades Trigonométricas (Pitágoras).
- Ajuste de Dominio (La trampa del rango).

---

## 🔄 Concepto 1: Despeje Algebraico

Si las ecuaciones son algebraicas ($t, t^2, \dots$), despeja $t$ de la más fácil y métela en la otra.

**5 Ejemplos de Sustitución:**

### Ejemplo 1.1: La Recta
$$ x = t + 2, \quad y = 3t $$
1.  Despeja $t$ de $x$: $t = x - 2$.
2.  Sustituye en $y$: $y = 3(x - 2)$.
3.  Resultado: $y = 3x - 6$.

### Ejemplo 1.2: La Parábola
$$ x = t - 1, \quad y = t^2 $$
1.  Despeja $t$: $t = x + 1$.
2.  Sustituye: $y = (x + 1)^2$.
3.  Resultado: $y = x^2 + 2x + 1$.

### Ejemplo 1.3: La Raíz
$$ x = t^2, \quad y = t $$
1.  Es más fácil despejar de $y$: $t = y$.
2.  Sustituye en $x$: $x = y^2$.
3.  Resultado: Parábola horizontal $x = y^2$. (Ojo: como $x=t^2$, $x \ge 0$).

### Ejemplo 1.4: Inversas
$$ x = e^t, \quad y = t $$
1.  Despeja $t$ de la segunda: $t=y$.
2.  Sustituye: $x = e^y \Rightarrow y = \ln x$.
3.  Dominio: $x > 0$.

### Ejemplo 1.5: Racional
$$ x = \frac{1}{t}, \quad y = t + 1 $$
1.  Despeja $t$: $t = 1/x$.
2.  Sustituye: $y = \frac{1}{x} + 1$.
3.  Resultado: $y = \frac{1+x}{x}$.

---

## 🔺 Concepto 2: Identidades Trigonométricas

Si ves senos y cosenos, **NO DESPEJES $t$** (a menos que quieras sufrir con arcosenos). Mejor usa:
$$ \sin^2 t + \cos^2 t = 1 $$

**5 Ejemplos Circulares y Elípticos:**

### Ejemplo 2.1: Círculo Unitario
$$ x = \cos t, \quad y = \sin t $$
1.  Eleva al cuadrado: $x^2 = \cos^2 t$, $y^2 = \sin^2 t$.
2.  Suma: $x^2 + y^2 = 1$.

### Ejemplo 2.2: Elipse
$$ x = 3 \cos t, \quad y = 2 \sin t $$
1.  Aísla trigonométricas: $\frac{x}{3} = \cos t$, $\frac{y}{2} = \sin t$.
2.  Pitágoras: $(\frac{x}{3})^2 + (\frac{y}{2})^2 = 1$.
3.  Resultado: $\frac{x^2}{9} + \frac{y^2}{4} = 1$.

### Ejemplo 2.3: Círculo Desplazado
$$ x = h + r \cos t, \quad y = k + r \sin t $$
1.  Aísla: $\frac{x-h}{r} = \cos t$.
2.  Aísla: $\frac{y-k}{r} = \sin t$.
3.  Suma cuadrados: $\frac{(x-h)^2}{r^2} + \frac{(y-k)^2}{r^2} = 1$.
4.  Resultado: $(x-h)^2 + (y-k)^2 = r^2$.

### Ejemplo 2.4: Hipérbola (Secante/Tangente)
$$ x = \sec t, \quad y = \tan t $$
1.  Identidad: $\sec^2 t - \tan^2 t = 1$.
2.  Resultado: $x^2 - y^2 = 1$.

### Ejemplo 2.5: Cicloide (Avanzado)
$$ x = t - \sin t, \quad y = 1 - \cos t $$
Aquí es difícil eliminar $t$ algebraicamente de forma limpia. Se suele dejar en paramétrica.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Elimina $t$ de $x=2t, y=4t$.

<details>
<summary>Ver solución</summary>
$t=x/2 \Rightarrow y=4(x/2)=2x$.
</details>

---

### Ejercicio 2
Elimina $t$ de $x=\sqrt{t}, y=t$.

<details>
<summary>Ver solución</summary>
$y = (\sqrt{t})^2 = x^2$ (con $x \ge 0$).
</details>

---

### Ejercicio 3
Elimina $t$ de $x=5\sin t, y=5\cos t$.

<details>
<summary>Ver solución</summary>
$x^2+y^2=25$. Círculo.
</details>

---

### Ejercicio 4
Si $x=e^t, y=e^{-t}$, halla la cartesiana.

<details>
<summary>Ver solución</summary>
$y = 1/e^t = 1/x \Rightarrow y = 1/x$ (Hipérbola rectangular para $x>0$).
</details>

---

### Ejercicio 5
¿Qué pierdes al eliminar el parámetro?

<details>
<summary>Ver solución</summary>
La información de dirección, velocidad y a veces los límites del dominio.
</details>

---

### Ejercicio 6
Elimina $t$ de $x = t^3, y = t^2$.

<details>
<summary>Ver solución</summary>
$t = x^{1/3}$. $y = x^{2/3}$. O $y^3 = x^2$.
</details>

---

### Ejercicio 7
Convierte $x = 2 + \cos \theta, y = \sin \theta$.

<details>
<summary>Ver solución</summary>
$(x-2)^2 + y^2 = 1$.
</details>

---

### Ejercicio 8
Elimina $t$ de $x = \ln t, y = t$.

<details>
<summary>Ver solución</summary>
$t = e^x \Rightarrow y = e^x$.
</details>

---

### Ejercicio 9
Diferencia entre $y=x$ y las paramétricas $x=\sin t, y=\sin t$.

<details>
<summary>Ver solución</summary>
La paramétrica solo existe entre -1 y 1. La cartesiana es infinita.
</details>

---

### Ejercicio 10
Identifica $x = 3 \tan \theta, y = 2 \sec \theta$.

<details>
<summary>Ver solución</summary>
Identidad $\sec^2 - \tan^2 = 1$. $(y/2)^2 - (x/3)^2 = 1 \Rightarrow y^2/4 - x^2/9 = 1$. (Hipérbola vertical).
</details>

---

## 🔑 Resumen

| Tipo Paramétrico | Estrategia |
| :--- | :--- |
| **Algebraico ($t$)** | Despeja $t$ en una y sustituye en la otra. |
| **Trigonométrico** | Aísla $\sin/\cos$ y usa **Pitágoras** ($\sin^2 + \cos^2 = 1$). |

> **Conclusión:** La ecuación cartesiana te muestra el "mapa" completo de la carretera, pero la paramétrica te dice cómo conducías (rápido, lento, hacia adelante o hacia atrás).
