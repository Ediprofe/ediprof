---
title: "Ley de Cosenos"
---

# **Ley de Cosenos**

Si la Ley de Senos es la reina de las parejas, la **Ley de Cosenos** es el "todoterreno" de la trigonometría. Funciona cuando la Ley de Senos falla: cuando tienes los tres lados (LLL) o cuando tienes un ángulo atrapado entre dos lados (LAL). Es básicamente el Teorema de Pitágoras con esteroides.

---

## 🎯 ¿Qué vas a aprender?

- Cómo generalizar Pitágoras para triángulos que no son rectángulos.
- La fórmula para encontrar un lado si conoces los otros dos y el ángulo medio.
- La fórmula para encontrar cualquier ángulo si conoces los tres lados.
- Cuándo usar Ley de Cosenos vs. Ley de Senos.

---

## 📐 El "Pitágoras Mejorado"

El Teorema de Pitágoras ($c^2 = a^2 + b^2$) solo funciona si el ángulo $C$ es de 90°.
¿Qué pasa si el ángulo cambia? Necesitamos un **factor de corrección**.

$$
c^2 = a^2 + b^2 - 2ab\cos C
$$

Ese término extra ($-2ab\cos C$) ajusta la longitud dependiendo de si el ángulo se cierra (menos de 90°) o se abre (más de 90°).

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Ley de Cosenos: a² = b² + c² - 2bc·cos A</strong>
  </div>

![Ley de Cosenos](/images/trigonometria/triangulos-oblicuangulos/ley-cosenos.svg)

</div>

### Las Tres Versiones
En realidad es la misma fórmula, solo rotando las letras:

$$
a^2 = b^2 + c^2 - 2bc \cos A
$$

$$
b^2 = a^2 + c^2 - 2ac \cos B
$$

$$
c^2 = a^2 + b^2 - 2ab \cos C
$$

---

## 🔍 ¿Cuándo usarla?

Usa la Ley de Cosenos en los casos "difíciles" donde la Ley de Senos no sirve:

1.  **Caso LAL:** Conoces dos lados y el ángulo **atrapado** (entre ellos).
2.  **Caso LLL:** Conoces los **tres lados** y quieres hallar un ángulo.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Encontrar un lado (Caso LAL)
Tienes un triángulo con lados $b=8$, $c=10$ y el ángulo entre ellos $A=60°$. Halla $a$.

**Paso 1: Escribir la fórmula**
$$
a^2 = b^2 + c^2 - 2bc \cos A
$$

**Paso 2: Sustituir**
$$
a^2 = 8^2 + 10^2 - 2(8)(10) \cos 60°
$$

$$
a^2 = 64 + 100 - 160(0.5)
$$

$$
a^2 = 164 - 80 = 84
$$

**Paso 3: Raíz cuadrada**
$$
a = \sqrt{84} \approx 9.17
$$

**Resultado:** $\boxed{9.17}$

---

### Ejemplo 2: Encontrar un ángulo (Caso LLL)
Tienes un triángulo con lados 7, 9, 12. Halla el ángulo opuesto al lado 12 (llamémoslo $C$).

**Paso 1: Escribir la fórmula despejada para el coseno**
$$
\cos C = \frac{a^2 + b^2 - c^2}{2ab}
$$

**Paso 2: Sustituir**
$$
\cos C = \frac{7^2 + 9^2 - 12^2}{2(7)(9)}
$$

$$
\cos C = \frac{49 + 81 - 144}{126} = \frac{-14}{126} \approx -0.111
$$

**Paso 3: Arcocoseno**
$$
C = \cos^{-1}(-0.111) \approx 96.4°
$$

> **Nota:** Como el coseno dio negativo, el ángulo es obtuso ($>90°$).

**Resultado:** $\boxed{96.4°}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Halla $c$ si $a=5$, $b=9$, $C=40°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$c^2 = 5^2 + 9^2 - 2(5)(9)\cos 40°$.
$c^2 = 25 + 81 - 90(0.766) = 106 - 68.94 = 37.06$.
$c = \sqrt{37.06}$.

**Respuesta:** $\boxed{6.09}$
</details>

---

### Ejercicio 2
Encuentra el ángulo $A$ si lados son 3, 4, 5.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es un triángulo notable, pero usemos la fórmula.
$\cos A = \frac{4^2+5^2-3^2}{2(4)(5)} = \frac{16+25-9}{40} = \frac{32}{40} = 0.8$.
$A = \cos^{-1}(0.8) \approx 36.87°$.

**Respuesta:** $\boxed{36.9°}$
</details>

---

### Ejercicio 3
¿Qué pasa con la Ley de Cosenos si el ángulo es $90°$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos 90° = 0$. El término $-2ab \cos C$ desaparece.
Queda $c^2 = a^2 + b^2$.

**Respuesta:** **Se convierte en Pitágoras**
</details>

---

### Ejercicio 4
Encuentra la distancia entre dos barcos que salieron del mismo punto: uno viajó 10 km, el otro 20 km, y el ángulo entre sus rumbos es $120°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$d^2 = 10^2 + 20^2 - 2(10)(20)\cos 120°$.
$\cos 120° = -0.5$.
$d^2 = 100 + 400 - 400(-0.5) = 500 + 200 = 700$.

**Respuesta:** $\boxed{\sqrt{700} \approx 26.46 \text{ km}}$
</details>

---

### Ejercicio 5
Calcula el ángulo mayor de un triángulo con lados 5, 6, 7.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El ángulo mayor está opuesto al lado mayor (7).
$\cos C = \frac{5^2+6^2-7^2}{2(5)(6)} = \frac{25+36-49}{60} = \frac{12}{60} = 0.2$.
$C = \cos^{-1}(0.2)$.

**Respuesta:** $\boxed{78.5°}$
</details>

---

### Ejercicio 6
Si $a=b=10$ y $C=60°$, ¿qué tipo de triángulo es?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Lados iguales + ángulo $60°$ $\Rightarrow$ Equilátero.
$c^2 = 100+100 - 200(0.5) = 100 \Rightarrow c=10$.

**Respuesta:** **Equilátero**
</details>

---

### Ejercicio 7
Halla $b$ si $a=2$, $c=3$, $B=180°$. (Caso extremo).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No es un triángulo, es una línea recta.
$b^2 = 4 + 9 - 2(2)(3)(-1) = 13 + 12 = 25$.
$b=5$ ($a+c$).

**Respuesta:** $\boxed{5}$
</details>

---

### Ejercicio 8
Encuentra el coseno del ángulo $B$ si $a=2, b=3, c=4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos B = \frac{2^2+4^2-3^2}{2(2)(4)} = \frac{4+16-9}{16} = \frac{11}{16}$.

**Respuesta:** $\boxed{0.6875}$
</details>

---

### Ejercicio 9
Si $c^2 > a^2 + b^2$, ¿cómo es el ángulo $C$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si $c^2$ es "demasiado grande" para Pitágoras, significa que el ángulo se abrió más de $90°$.

**Respuesta:** **Obtuso ($>90°$)**
</details>

---

### Ejercicio 10
Simplifica $x^2 + x^2 - 2(x)(x)\cos(60°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2x^2 - 2x^2(0.5) = 2x^2 - x^2 = x^2$.
Es el tercer lado de un triángulo equilátero de lado $x$.

**Respuesta:** $\boxed{x^2}$
</details>

---

## 🔑 Resumen

| Herramienta | Cuándo usarla | Pista visual |
| :--- | :--- | :--- |
| **Ley de Cosenos** | 3 Lados (LLL) | El triángulo rígido (no se deforma). |
| **Ley de Cosenos** | Lado-Ángulo-Lado (LAL) | El abrazo (dos lados abrazan un ángulo). |
| **Ley de Senos** | Parejas (Lado/Opuesto) | La "X" o proporción. |

> **Conclusión:** Si tienes los tres lados, usa Cosenos. Si tienes un "sándwich" de ángulo entre lados, usa Cosenos. Para todo lo demás, prueba Senos primero (es más fácil).
