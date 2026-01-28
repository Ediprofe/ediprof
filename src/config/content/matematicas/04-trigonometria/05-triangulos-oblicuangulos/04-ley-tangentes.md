---
title: "Ley de Tangentes"
---

# **Ley de Tangentes**

Probablemente hayas oído hablar de la Ley de Senos y de Cosenos, pero ¿sabías que existe una tercera ley secreta? La **Ley de Tangentes** es la herramienta olvidada de la trigonometría. Aunque la Ley de Cosenos le robó el protagonismo, esta ley era la favorita de los astrónomos antiguos porque es más fácil de calcular a mano (sin raíces cuadradas).

---

## 🎯 ¿Qué vas a aprender?

- La fórmula "rara" pero elegante de la Ley de Tangentes.
- Cómo usarla para resolver el caso LAL sin encontrar el tercer lado primero.
- Por qué es una alternativa poderosa a la Ley de Cosenos.
- Cómo usar sistemas de ecuaciones ($A+B$ y $A-B$) para hallar ángulos.

---

## 🧬 La Fórmula Olvidada

Esta ley relaciona la suma y resta de dos lados con la suma y resta de sus ángulos opuestos.

$$
\frac{a - b}{a + b} = \frac{\tan\left(\frac{A - B}{2}\right)}{\tan\left(\frac{A + B}{2}\right)}
$$

> **Nota:** Puedes cambiar las letras como quieras ($b$ con $c$, $a$ con $c$), siempre que mantengas la correspondencia lado-ángulo.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Fórmula de la Ley de Tangentes</strong>
  </div>

![Ley de Tangentes](/images/trigonometria/triangulos-oblicuangulos/ley-tangentes.svg)

</div>

---

## 🔍 ¿Para qué sirve hoy en día?

Es especialmente útil en el **Caso LAL** (Lado-Ángulo-Lado).
Si usaras la Ley de Cosenos, primero encontrarías el tercer lado ($c$) y luego usarías ese lado para hallar los ángulos.
Con la Ley de Tangentes, puedes encontrar los ángulos $A$ y $B$ **directamente**, sin pasar por el lado $c$.

---

## ⚙️ Ejemplo Resuelto (Caso LAL)

Tienes un triángulo con lados $a=8$, $b=5$ y el ángulo comprendido $C=60°$. Halla $A$ y $B$.

**Paso 1: Hallar la suma de ángulos (A + B)**
Sabemos que $A+B+C = 180°$.
$$ A + B = 180° - 60° = 120° $$
Por tanto:
$$ \frac{A + B}{2} = 60° $$

**Paso 2: Usar la Ley para hallar la diferencia (A - B)**
$$
\frac{8 - 5}{8 + 5} = \frac{\tan(\frac{A - B}{2})}{\tan(60°)}
$$
$$
\frac{3}{13} = \frac{\tan(\frac{A - B}{2})}{1.732}
$$
$$
\tan\left(\frac{A - B}{2}\right) = \frac{3 \cdot 1.732}{13} \approx 0.4
$$
$$
\frac{A - B}{2} = \tan^{-1}(0.4) \approx 21.8°
$$
$$
A - B = 43.6°
$$

**Paso 3: Resolver el sistema**
Tenemos:
1.  $A + B = 120°$
2.  $A - B = 43.6°$

Sumamos ambas ecuaciones:
$$ 2A = 163.6° \Rightarrow A = 81.8° $$
Restamos:
$$ 2B = 76.4° \Rightarrow B = 38.2° $$

**Resultado:** $\boxed{A=81.8°, B=38.2°}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $\frac{a-b}{a+b}$ si $a=15$ y $b=5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{15-5}{15+5} = \frac{10}{20} = 0.5$.

**Respuesta:** $\boxed{0.5}$
</details>

---

### Ejercicio 2
Si $A=80°$ y $B=20°$, calcula $\frac{A+B}{2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{80+20}{2} = \frac{100}{2} = 50°$.

**Respuesta:** $\boxed{50°}$
</details>

---

### Ejercicio 3
Encuentra $\tan(\frac{A-B}{2})$ si $\frac{a-b}{a+b} = 0.2$ y $\tan(\frac{A+B}{2}) = 2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$0.2 = \frac{x}{2} \Rightarrow x = 0.4$.

**Respuesta:** $\boxed{0.4}$
</details>

---

### Ejercicio 4
Si conoces $a, b$ y $C$, ¿cuánto vale $A+B$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$180° - C$.

**Respuesta:** $\boxed{180° - C}$
</details>

---

### Ejercicio 5
¿Qué pasa si $a=b$ en la Ley de Tangentes?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El lado izquierdo $\frac{a-b}{a+b}$ se vuelve 0.
$\tan(\frac{A-B}{2}) = 0 \Rightarrow A=B$.
Es un triángulo isósceles.

**Respuesta:** **El numerador es cero**
</details>

---

### Ejercicio 6
Resuelve para $\frac{A-B}{2}$ si $\tan(\frac{A-B}{2}) = 0.577$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan^{-1}(0.577) = 30°$.

**Respuesta:** $\boxed{30°}$
</details>

---

### Ejercicio 7
Si $A=90°$ y $B=30°$, calcula el lado derecho de la fórmula.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{A-B}{2} = 30°$, $\frac{A+B}{2} = 60°$.
$\frac{\tan 30°}{\tan 60°} = \frac{1/\sqrt{3}}{\sqrt{3}} = \frac{1}{3}$.

**Respuesta:** $\boxed{\frac{1}{3}}$
</details>

---

### Ejercicio 8
¿Por qué preferían esta ley antes de las calculadoras?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Porque usa tangentes y divisiones, lo cual era fácil de manejar con **logaritmos**, a diferencia de la Ley de Cosenos que tiene sumas y raíces.

**Respuesta:** **Facilidad con logaritmos**
</details>

---

### Ejercicio 9
Despeja $a$ de la ecuación $\frac{a-b}{a+b} = K$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a-b = K(a+b) \Rightarrow a-b = Ka + Kb$.
$a - Ka = b + Kb \Rightarrow a(1-K) = b(1+K)$.
$a = b\frac{1+K}{1-K}$.

**Respuesta:** $\boxed{a = b\frac{1+K}{1-K}}$
</details>

---

### Ejercicio 10
Si resuelves el sistema $A+B=100$ y $A-B=20$, ¿cuánto valen $A$ y $B$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2A = 120 \Rightarrow A=60$.
$2B = 80 \Rightarrow B=40$.

**Respuesta:** $\boxed{A=60, B=40}$
</details>

---

## 🔑 Resumen

| Ley | Uso Principal | Característica |
| :---: | :---: | :--- |
| **Tangentes** | Caso LAL (hallar ángulos) | Sin raíces, usa sistema de ecuaciones. |
| **Cosenos** | Caso LAL (hallar lado) | Usa cuadrados y raíces. |

> **Conclusión:** Aunque la Ley de Cosenos es la más famosa, la Ley de Tangentes es una joya de elegancia algebraica. Te permite "desenredar" los ángulos sin necesidad de saber cuánto mide el lado opuesto.
