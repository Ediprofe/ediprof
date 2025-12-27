# **Identidades del Ángulo Mitad**

¿Alguna vez te has preguntado cómo calcular el seno de $15°$? No está en la tabla de ángulos notables. Pero espera... $15°$ es la mitad de $30°$. Las **identidades del ángulo mitad** son como una lupa que nos permite ver qué pasa dentro de un ángulo al dividirlo en dos.

---

## 🎯 ¿Qué vas a aprender?

- Cómo calcular $\sin(x/2)$, $\cos(x/2)$ y $\tan(x/2)$.
- Por qué estas fórmulas tienen una raíz cuadrada y un signo $\pm$.
- Cómo determinar qué signo elegir según el cuadrante.
- Cómo usar estas identidades para calcular valores exactos de ángulos "raros".

---

## 🔍 Raíces y Signos

Las fórmulas de ángulo mitad son famosas por tener raíces cuadradas. Esto introduce un pequeño dilema: ¿elegimos el signo más ($+$) o el menos ($-$)?

> **Regla de Oro:** El signo $\pm$ NO significa que haya dos respuestas. Significa que **tú** tienes que elegir el signo correcto dependiendo del cuadrante donde caiga el ángulo mitad $x/2$.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Resumen: Fórmulas del Ángulo Mitad</strong>
  </div>

![Fórmulas ángulo mitad](/images/trigonometria/identidades/angulo-mitad.svg)

</div>

---

## 🔵 Seno del Ángulo Mitad

$$
\sin\left(\frac{x}{2}\right) = \pm\sqrt{\frac{1 - \cos x}{2}}
$$

> **Nota:** El seno usa "1 **menos** coseno".

---

## 🔴 Coseno del Ángulo Mitad

$$
\cos\left(\frac{x}{2}\right) = \pm\sqrt{\frac{1 + \cos x}{2}}
$$

> **Nota:** El coseno usa "1 **más** coseno".

---

## 📐 Tangente del Ángulo Mitad

La tangente tiene tres fórmulas. La primera tiene raíz, las otras dos son más amigables (sin raíces).

### 1. Con Raíz
$$
\tan\left(\frac{x}{2}\right) = \pm\sqrt{\frac{1 - \cos x}{1 + \cos x}}
$$

### 2. Sin Raíz (Seno arriba)
$$
\tan\left(\frac{x}{2}\right) = \frac{\sin x}{1 + \cos x}
$$

### 3. Sin Raíz (Seno abajo)
$$
\tan\left(\frac{x}{2}\right) = \frac{1 - \cos x}{\sin x}
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Calcular $\sin(15°)$
Usamos $x = 30°$, así que $x/2 = 15°$.
15° está en el Cuadrante I, así que el seno es **Positivo (+)**.

$$
\sin(15°) = +\sqrt{\frac{1 - \cos(30°)}{2}}
$$

$$
= \sqrt{\frac{1 - \frac{\sqrt{3}}{2}}{2}} = \sqrt{\frac{\frac{2-\sqrt{3}}{2}}{2}} = \sqrt{\frac{2-\sqrt{3}}{4}}
$$

$$
= \frac{\sqrt{2-\sqrt{3}}}{2}
$$

**Resultado:** $\boxed{\frac{\sqrt{2-\sqrt{3}}}{2}}$

### Ejemplo 2: Calcular $\cos(105°)$
Usamos $x = 210°$. Como 105° está en Cuadrante II, el coseno es **Negativo (-)**.

$$
\cos(105°) = -\sqrt{\frac{1 + \cos(210°)}{2}}
$$

Sabemos que $\cos(210°) = -\frac{\sqrt{3}}{2}$.

$$
= -\sqrt{\frac{1 - \frac{\sqrt{3}}{2}}{2}} = -\frac{\sqrt{2-\sqrt{3}}}{2}
$$

**Resultado:** $\boxed{-\frac{\sqrt{2-\sqrt{3}}}{2}}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $\cos(15°)$ usando la fórmula.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x=30°$. Coseno. Q1 (+).
$\sqrt{\frac{1+\sqrt{3}/2}{2}} = \frac{\sqrt{2+\sqrt{3}}}{2}$.

**Respuesta:** $\boxed{\frac{\sqrt{2+\sqrt{3}}}{2}}$
</details>

---

### Ejercicio 2
Si $\cos x = 1/2$ (Q1), halla $\sin(x/2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{\frac{1-0.5}{2}} = \sqrt{\frac{0.5}{2}} = \sqrt{0.25} = 0.5$.

**Respuesta:** $\boxed{0.5}$
</details>

---

### Ejercicio 3
Si $\cos x = -7/25$ y $180° < x < 270°$, halla $\cos(x/2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si $x$ está en Q3 ($180-270$), entonces $x/2$ está en Q2 ($90-135$).
Cos en Q2 es negativo.
$-\sqrt{\frac{1+(-7/25)}{2}} = -\sqrt{\frac{18/25}{2}} = -\sqrt{9/25} = -3/5$.

**Respuesta:** $\boxed{-\frac{3}{5}}$
</details>

---

### Ejercicio 4
Usa la fórmula de tangente sin raíz para hallar $\tan(15°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{1-\cos 30}{\sin 30} = \frac{1-\sqrt{3}/2}{1/2} = 2 - \sqrt{3}$.

**Respuesta:** $\boxed{2 - \sqrt{3}}$
</details>

---

### Ejercicio 5
Simplifica $\sqrt{\frac{1-\cos 40°}{2}}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Reconocemos la fórmula de seno de mitad.
$\sin(20°)$.

**Respuesta:** $\boxed{\sin(20°)}$
</details>

---

### Ejercicio 6
Calcula $\sin(22.5°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x=45°$. Q1.
$\sqrt{\frac{1-\sqrt{2}/2}{2}} = \frac{\sqrt{2-\sqrt{2}}}{2}$.

**Respuesta:** $\boxed{\frac{\sqrt{2-\sqrt{2}}}{2}}$
</details>

---

### Ejercicio 7
Verifica la identidad $\tan(x/2) + \cot(x/2) = 2\csc x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{\sin}{\cos} + \frac{\cos}{\sin} = \frac{\sin^2+\cos^2}{\sin\cos} = \frac{1}{\sin\cos}$.
Multiplicamos por 2 arriba y abajo: $\frac{2}{2\sin\cos} = \frac{2}{\sin 2(x/2)} = \frac{2}{\sin x} = 2\csc x$.

**Respuesta:** **Q.E.D.**
</details>

---

### Ejercicio 8
Determina el cuadrante de $x/2$ si $x = 300°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$300/2 = 150°$. Cuadrante II.

**Respuesta:** **II**
</details>

---

### Ejercicio 9
Simplifica $\frac{1-\cos x}{\sin x}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es directamente la fórmula de tangente de ángulo mitad.

**Respuesta:** $\boxed{\tan(x/2)}$
</details>

---

### Ejercicio 10
Si $\cos x = -1$, ¿cuánto vale $\cos(x/2)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\pm\sqrt{\frac{1+(-1)}{2}} = \sqrt{0} = 0$.

**Respuesta:** $\boxed{0}$
</details>

---

## 🔑 Resumen

| Función Mitad | Signo | Fórmula Clave |
| :---: | :---: | :---: |
| $\sin(x/2)$ | $\pm$ (Cuadrante) | $\sqrt{\frac{1-\cos x}{2}}$ |
| $\cos(x/2)$ | $\pm$ (Cuadrante) | $\sqrt{\frac{1+\cos x}{2}}$ |
| $\tan(x/2)$ | $\pm$ o directo | $\frac{1-\cos x}{\sin x}$ |

> **Conclusión:** La clave de estas fórmulas es el coseno. Todo se basa en saber el coseno del ángulo original. Y no olvides: ¡el signo $\pm$ lo decides tú mirando el cuadrante!
