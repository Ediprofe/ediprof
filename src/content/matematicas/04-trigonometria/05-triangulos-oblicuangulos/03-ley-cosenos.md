# Ley de Cosenos

La **Ley de Cosenos** generaliza el teorema de Pitágoras a cualquier triángulo.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Ley de Cosenos: a² = b² + c² - 2bc·cos A</strong>
  </div>

![Ley de Cosenos](/images/trigonometria/triangulos-oblicuangulos/ley-cosenos.svg)

</div>

---

## 📖 Enunciado

En cualquier triángulo $ABC$:

$$
a^2 = b^2 + c^2 - 2bc\cos A
$$

$$
b^2 = a^2 + c^2 - 2ac\cos B
$$

$$
c^2 = a^2 + b^2 - 2ab\cos C
$$

---

## 📖 Relación con Pitágoras

Si $C = 90°$, entonces $\cos C = 0$:

$$
c^2 = a^2 + b^2 - 2ab(0) = a^2 + b^2
$$

¡Es el teorema de Pitágoras!

---

## 📖 Cuándo usar la Ley de Cosenos

| Caso | Datos | Uso |
|------|-------|-----|
| LAL | Dos lados y el ángulo incluido | Encontrar el tercer lado |
| LLL | Los tres lados | Encontrar los ángulos |

---

## 📖 Ejemplo 1: Caso LAL

En un triángulo, $b = 8$, $c = 10$ y $A = 60°$. Encuentra $a$.

$$
a^2 = 8^2 + 10^2 - 2(8)(10)\cos 60°
$$

$$
a^2 = 64 + 100 - 160(0.5)
$$

$$
a^2 = 164 - 80 = 84
$$

$$
a = \sqrt{84} \approx 9.17
$$

---

## 📖 Ejemplo 2: Caso LLL (encontrar ángulo)

En un triángulo, $a = 7$, $b = 9$, $c = 12$. Encuentra el ángulo $C$.

Despejando $\cos C$:

$$
c^2 = a^2 + b^2 - 2ab\cos C
$$

$$
\cos C = \frac{a^2 + b^2 - c^2}{2ab}
$$

$$
\cos C = \frac{49 + 81 - 144}{2(7)(9)} = \frac{-14}{126} = -0.111
$$

$$
C = \arccos(-0.111) \approx 96.4°
$$

El triángulo es obtusángulo.

---

## 📖 Forma despejada para ángulos

$$
\cos A = \frac{b^2 + c^2 - a^2}{2bc}
$$

$$
\cos B = \frac{a^2 + c^2 - b^2}{2ac}
$$

$$
\cos C = \frac{a^2 + b^2 - c^2}{2ab}
$$

---

## 📖 Notas importantes

### Signo del coseno

- Si $\cos > 0$: ángulo agudo (< 90°)
- Si $\cos = 0$: ángulo recto (= 90°)
- Si $\cos < 0$: ángulo obtuso (> 90°)

### Estrategia para LLL

Encontrar primero el ángulo **mayor** (opuesto al lado mayor), así si hay un ángulo obtuso, lo encontramos primero.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Caso LAL

En un triángulo, $a = 5$, $c = 7$ y $B = 45°$. Encuentra $b$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
b^2 = 5^2 + 7^2 - 2(5)(7)\cos 45°
$$

$$
b^2 = 25 + 49 - 70(0.707) = 74 - 49.5 = 24.5
$$

$$
b = \sqrt{24.5} \approx 4.95
$$

</details>

---

### Ejercicio 2: Caso LLL

En un triángulo con lados $a = 5$, $b = 6$, $c = 8$, encuentra el ángulo $A$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\cos A = \frac{36 + 64 - 25}{2(6)(8)} = \frac{75}{96} = 0.781
$$

$$
A = \arccos(0.781) \approx 38.6°
$$

</details>

---

### Ejercicio 3: Triángulo completo

Un triángulo tiene $a = 10$, $b = 12$, $c = 15$. Encuentra todos los ángulos.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\cos C = \frac{100 + 144 - 225}{2(10)(12)} = \frac{19}{240} = 0.079
$$

$C = \arccos(0.079) \approx 85.5°$

$$
\cos A = \frac{144 + 225 - 100}{2(12)(15)} = \frac{269}{360} = 0.747
$$

$A = \arccos(0.747) \approx 41.7°$

$B = 180° - 85.5° - 41.7° = 52.8°$

</details>

---

### Ejercicio 4: Aplicación

Dos barcos parten del mismo puerto. Uno navega 30 km al norte y otro 40 km con rumbo N60°E. ¿A qué distancia están?

<details>
<summary><strong>Ver respuesta</strong></summary>

El ángulo entre las trayectorias es 60°.

$$
d^2 = 30^2 + 40^2 - 2(30)(40)\cos 60°
$$

$$
d^2 = 900 + 1600 - 2400(0.5) = 2500 - 1200 = 1300
$$

$$
d = \sqrt{1300} \approx 36.1 \text{ km}
$$

</details>

---
