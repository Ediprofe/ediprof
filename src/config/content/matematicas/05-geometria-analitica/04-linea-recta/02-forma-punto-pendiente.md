---
title: "Forma Punto-Pendiente"
---

# **Forma Punto-Pendiente**

Imagina que eres un detective. Encuentras una huella en el lugar del crimen (un punto) y sabes en qué dirección huyó el sospechoso (la pendiente). Con solo esos dos datos, puedes trazar exactamente su camino. En matemáticas, esa "huella + dirección" es la **Forma Punto-Pendiente**.

---

## 🎯 ¿Qué vas a aprender?

- La ecuación fundamental: $y - y_1 = m(x - x_1)$.
- Cómo construir una recta conociendo solo un punto y su inclinación.
- Cómo traducir esta forma misteriosa a la forma general o clásica.
- Por qué esta es la herramienta favorita de los físicos e ingenieros.

---

## 🕵️‍♂️ La Ecuación del Detective

Si conocemos **un punto** $P_1(x_1, y_1)$ y la **pendiente** $m$, la ecuación de la recta es:

$$
y - y_1 = m(x - x_1)
$$

### ¿De dónde sale?
Recuerda la fórmula de la pendiente $m = \frac{y - y_1}{x - x_1}$.
Si pasas el denominador multiplicando al otro lado, ¡obtienes esta ecuación!

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Punto + Pendiente = Recta Única</strong>
  </div>
  <img src="/images/geometria/analitica/punto-pendiente.svg" alt="Forma punto-pendiente" style="width: 100%; height: auto;" />
</div>

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El Caso Básico
Tenemos el punto $A(2, 3)$ y pendiente $m=4$.
1.  Identificamos: $x_1=2, y_1=3, m=4$.
2.  Sustituimos:
    $$ y - 3 = 4(x - 2) $$
3.  Despejamos (para ponerla bonita):
    $y - 3 = 4x - 8$
    $y = 4x - 5$

### Ejemplo 2: Pendiente Negativa
Punto $B(-1, 5)$ y pendiente $m=-2$.
1.  Identificamos: $x_1=-1, y_1=5$. (Cuidado con el menos).
2.  Sustituimos:
    $$ y - 5 = -2(x - (-1)) $$
    $$ y - 5 = -2(x + 1) $$
3.  Despejamos:
    $y - 5 = -2x - 2$
    $y = -2x + 3$

### Ejemplo 3: Pendiente Fraccionaria
Punto $C(4, 1)$ y pendiente $m=1/2$.
$$ y - 1 = \frac{1}{2}(x - 4) $$
Para evitar fracciones feas, pasamos el 2 a multiplicar al otro lado:
$$ 2(y - 1) = 1(x - 4) $$
$$ 2y - 2 = x - 4 $$
$$ x - 2y - 2 = 0 $$ (Forma general)

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la ecuación para $P(1, 1)$ y $m = 3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$y - 1 = 3(x - 1) \Rightarrow y = 3x - 3 + 1$.

**Respuesta:** $\boxed{y = 3x - 2}$
</details>

---

### Ejercicio 2
Escribe la ecuación para $P(-2, -5)$ y $m = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$y - (-5) = 1(x - (-2)) \Rightarrow y + 5 = x + 2$.

**Respuesta:** $\boxed{y = x - 3}$
</details>

---

### Ejercicio 3
Escribe la ecuación para el origen $(0, 0)$ y $m = -5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$y - 0 = -5(x - 0)$.

**Respuesta:** $\boxed{y = -5x}$
</details>

---

### Ejercicio 4
Escribe la ecuación para $P(3, 0)$ y $m = 0.5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$y - 0 = 0.5(x - 3) \Rightarrow y = 0.5x - 1.5$.

**Respuesta:** $\boxed{y = 0.5x - 1.5}$
</details>

---

### Ejercicio 5
Halla la ecuación para $P(4, 2)$ con pendiente indefinida.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Pendiente indefinida = Recta Vertical. $x$ es constante.

**Respuesta:** $\boxed{x = 4}$
</details>

---

### Ejercicio 6
Convierte $y-2 = 3(x-1)$ a forma general ($Ax+By+C=0$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$y - 2 = 3x - 3 \Rightarrow 0 = 3x - y - 1$.

**Respuesta:** $\boxed{3x - y - 1 = 0}$
</details>

---

### Ejercicio 7
Halla la recta que pasa por $(1, 2)$ y es paralela a $y=2x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Misma pendiente $m=2$.
$y - 2 = 2(x - 1) \Rightarrow y = 2x$.

**Respuesta:** $\boxed{y = 2x}$
</details>

---

### Ejercicio 8
Halla la recta que pasa por $(1, 2)$ y es perpendicular a $y=3x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Pendiente perp. $m = -1/3$.
$y - 2 = -1/3 (x - 1)$.

**Respuesta:** $\boxed{y = -\frac{1}{3}x + \frac{7}{3}}$
</details>

---

### Ejercicio 9
Si en la ecuación $y-3 = k(x-2)$, la recta es horizontal, ¿cuánto vale $k$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Recta horizontal tiene pendiente 0.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 10
Escribe la ecuación para $P(-3, 0)$ y $m = -1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$y - 0 = -1(x + 3) \Rightarrow y = -x - 3$.

**Respuesta:** $\boxed{y = -x - 3}$
</details>

---

## 🔑 Resumen

| Paso | Acción |
| :--- | :--- |
| **1** | Escribe $y - (\quad) = (\quad)(x - (\quad))$. |
| **2** | Rellena los huecos: $y_1$, $m$, $x_1$. |
| **3** | Simplifica signos (menos por menos da más). |
| **4** | Despeja $y$ o iguala a 0 según te pidan. |

> **Conclusión:** No necesitas memorizar tres fórmulas de rectas. Si te aprendes esta ("Punto-Pendiente"), puedes deducir todas las demás. Es la navaja suiza de las rectas.
