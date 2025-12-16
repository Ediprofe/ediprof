# Recta Normal

La recta normal es perpendicular a la tangente en el punto de tangencia. Tiene aplicaciones en óptica, reflexión y problemas de distancia mínima.

---

## 🎯 ¿Qué vas a aprender?

- Definición de recta normal
- Ecuación de la normal usando la derivada
- Relación entre tangente y normal
- Aplicaciones

---

## 📖 Definición

La **recta normal** a una curva en un punto es la recta perpendicular a la tangente en ese punto.

---

## 📖 Pendiente de la normal

Si la tangente tiene pendiente $m_t = f'(a)$:

$$m_n = -\frac{1}{f'(a)}$$

(Las pendientes de rectas perpendiculares son opuestas recíprocas)

---

## 📖 Ecuación de la normal

$$\boxed{y - f(a) = -\frac{1}{f'(a)}(x - a)}$$

siempre que $f'(a) \neq 0$.

---

## ⚠️ Casos especiales

- Si $f'(a) = 0$ (tangente horizontal): la normal es **vertical** → $x = a$
- Si $f'(a)$ no existe (tangente vertical): la normal es **horizontal** → $y = f(a)$

---

## ⚙️ Ejemplo 1: Normal básica

Encuentra la normal a $f(x) = x^2$ en $x = 2$.

**Punto:** $(2, 4)$

**Pendiente tangente:** $f'(2) = 4$

**Pendiente normal:** $m_n = -\frac{1}{4}$

**Normal:**
$$y - 4 = -\frac{1}{4}(x - 2)$$
$$y = -\frac{1}{4}x + \frac{9}{2}$$

---

## ⚙️ Ejemplo 2: Con función raíz

Normal a $f(x) = \sqrt{x}$ en $x = 9$.

**Punto:** $(9, 3)$

**Pendiente tangente:** $f'(9) = \frac{1}{6}$

**Pendiente normal:** $m_n = -6$

**Normal:**
$$y - 3 = -6(x - 9)$$
$$y = -6x + 57$$

---

## ⚙️ Ejemplo 3: Normal a un círculo

Normal a $x^2 + y^2 = 25$ en $(3, 4)$.

**Pendiente tangente:** $-\frac{x}{y} = -\frac{3}{4}$

**Pendiente normal:** $\frac{4}{3}$

**Normal:**
$$y - 4 = \frac{4}{3}(x - 3)$$

Simplificando: $y = \frac{4}{3}x$

**Observación:** La normal a un círculo siempre pasa por el centro.

---

## ⚙️ Ejemplo 4: Tangente horizontal

Normal a $f(x) = x^3 - 3x$ en $x = 1$ (donde $f'(1) = 0$).

**Punto:** $(1, -2)$

**Pendiente tangente:** $f'(1) = 0$ (horizontal)

**Normal:** vertical → $x = 1$

---

## 📖 Aplicaciones de la normal

| Campo | Aplicación |
|-------|------------|
| Óptica | Ley de reflexión (ángulo respecto a la normal) |
| Física | Fuerza normal en superficies |
| Geometría | Distancia punto-curva |
| Ingeniería | Diseño de curvas de carretera |

---

## ⚙️ Ejemplo 5: Dónde pasa la normal por el origen

¿Desde qué punto(s) de $y = x^2$ la normal pasa por el origen?

Sea $(a, a^2)$ el punto de tangencia.

**Pendiente normal:** $-\frac{1}{2a}$

**Normal pasa por $(a, a^2)$ y $(0, 0)$:**

$$\frac{a^2 - 0}{a - 0} = -\frac{1}{2a}$$

$$\frac{a^2}{a} = -\frac{1}{2a}$$

$$a = -\frac{1}{2a}$$

$$2a^2 = -1$$

No tiene solución real. Ninguna normal pasa por el origen.

---

## ⚙️ Ejemplo 6: Tangente y normal juntas

Para $f(x) = e^x$ en $x = 0$:

**Punto:** $(0, 1)$

**$f'(0) = 1$**

**Tangente:** $y - 1 = 1(x - 0)$ → $y = x + 1$

**Normal:** $y - 1 = -1(x - 0)$ → $y = -x + 1$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra las ecuaciones de la tangente y la normal a $f(x) = \ln x$ en $x = e$.

<details>
<summary>Ver solución</summary>

$f(e) = 1$, $f'(x) = \frac{1}{x}$, $f'(e) = \frac{1}{e}$

**Tangente:** $y - 1 = \frac{1}{e}(x - e)$ → $y = \frac{x}{e}$

**Normal:** $y - 1 = -e(x - e)$ → $y = -ex + e^2 + 1$
</details>

---

**Ejercicio 2:** Encuentra la normal a $xy = 4$ en el punto $(2, 2)$.

<details>
<summary>Ver solución</summary>

Derivando implícitamente: $y + xy' = 0 \Rightarrow y' = -\frac{y}{x}$

En $(2, 2)$: $y' = -1$

Normal: $m_n = 1$

$y - 2 = 1(x - 2)$ → $y = x$
</details>
