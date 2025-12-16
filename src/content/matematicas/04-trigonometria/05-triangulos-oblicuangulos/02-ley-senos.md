# Ley de Senos

La **Ley de Senos** relaciona los lados de un triángulo con los senos de sus ángulos opuestos.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Ley de Senos: a/sin A = b/sin B = c/sin C</strong>
  </div>

![Ley de Senos](/images/trigonometria/triangulos-oblicuangulos/ley-senos.svg)

</div>

---

## 📖 Enunciado

En cualquier triángulo $ABC$:

$$
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}
$$

También se puede escribir como:

$$
\frac{\sin A}{a} = \frac{\sin B}{b} = \frac{\sin C}{c}
$$

---

## 📖 Interpretación

> El cociente entre un lado y el seno del ángulo opuesto es **constante** para todos los lados del triángulo.

Esta constante es igual al diámetro del círculo circunscrito:

$$
\frac{a}{\sin A} = 2R
$$

donde $R$ es el radio del circuncírculo.

---

## 📖 Cuándo usar la Ley de Senos

| Caso | Datos | Uso |
|------|-------|-----|
| ALA | Dos ángulos y un lado | Encontrar los otros lados |
| LAA | Un lado y dos ángulos | Encontrar los otros lados |
| LLA | Dos lados y ángulo opuesto | Encontrar otro ángulo (caso ambiguo) |

---

## 📖 Ejemplo 1: Caso ALA

En un triángulo, $A = 40°$, $B = 60°$ y $c = 15$ cm. Encuentra los lados $a$ y $b$.

### Paso 1: Encontrar el ángulo C

$$
C = 180° - 40° - 60° = 80°
$$

### Paso 2: Aplicar Ley de Senos

$$
\frac{a}{\sin 40°} = \frac{15}{\sin 80°}
$$

$$
a = \frac{15 \times \sin 40°}{\sin 80°} = \frac{15 \times 0.6428}{0.9848} \approx 9.79 \text{ cm}
$$

$$
\frac{b}{\sin 60°} = \frac{15}{\sin 80°}
$$

$$
b = \frac{15 \times \sin 60°}{\sin 80°} = \frac{15 \times 0.8660}{0.9848} \approx 13.19 \text{ cm}
$$

---

## 📖 Ejemplo 2: Encontrar un ángulo

En un triángulo, $a = 10$, $b = 8$ y $A = 50°$. Encuentra $B$.

$$
\frac{\sin B}{8} = \frac{\sin 50°}{10}
$$

$$
\sin B = \frac{8 \times \sin 50°}{10} = \frac{8 \times 0.766}{10} = 0.613
$$

$$
B = \arcsin(0.613) \approx 37.8°
$$

---

## 📖 El caso ambiguo (LLA)

Cuando conocemos dos lados y el ángulo **opuesto** a uno de ellos, puede haber:

| Situación | Soluciones |
|-----------|------------|
| $\sin B > 1$ | Ninguna |
| $\sin B = 1$ | Una (ángulo recto) |
| $\sin B < 1$ | Una o dos |

### ¿Por qué dos soluciones?

Si $\sin B = 0.6$, entonces $B$ podría ser:
- $B = \arcsin(0.6) \approx 37°$, o
- $B = 180° - 37° = 143°$

Debemos verificar si ambas son válidas.

---

## 📝 Ejercicios de práctica

### Ejercicio 1

En un triángulo, $A = 35°$, $C = 75°$ y $a = 12$ cm. Encuentra $c$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$B = 180° - 35° - 75° = 70°$

$$
\frac{c}{\sin 75°} = \frac{12}{\sin 35°}
$$

$$
c = \frac{12 \times \sin 75°}{\sin 35°} = \frac{12 \times 0.966}{0.574} \approx 20.2 \text{ cm}
$$

</details>

---

### Ejercicio 2

En un triángulo, $a = 15$, $b = 12$ y $A = 65°$. Encuentra $B$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\sin B = \frac{12 \times \sin 65°}{15} = \frac{12 \times 0.906}{15} = 0.725
$$

$$
B = \arcsin(0.725) \approx 46.5°
$$

(Verificar: $180° - 46.5° = 133.5°$, que daría $A + B = 65° + 133.5° = 198.5° > 180°$, imposible. Solo una solución.)

</details>

---

### Ejercicio 3

Resuelve el triángulo: $A = 48°$, $B = 72°$, $c = 20$ m.

<details>
<summary><strong>Ver respuesta</strong></summary>

$C = 180° - 48° - 72° = 60°$

$$
a = \frac{20 \times \sin 48°}{\sin 60°} = \frac{20 \times 0.743}{0.866} \approx 17.2 \text{ m}
$$

$$
b = \frac{20 \times \sin 72°}{\sin 60°} = \frac{20 \times 0.951}{0.866} \approx 22.0 \text{ m}
$$

</details>

---
