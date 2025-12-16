# Ángulo entre Curvas

Cuando dos curvas se intersectan, forman un ángulo. Podemos calcularlo usando las pendientes de sus tangentes en el punto de intersección.

---

## 🎯 ¿Qué vas a aprender?

- Cómo definir el ángulo entre dos curvas
- Fórmula para calcular el ángulo
- Curvas ortogonales
- Familias de curvas ortogonales

---

## 📖 Definición

El **ángulo entre dos curvas** en su punto de intersección es el ángulo entre sus rectas tangentes en ese punto.

---

## 📖 Fórmula del ángulo

Si $m_1$ y $m_2$ son las pendientes de las tangentes:

$$\tan\theta = \left|\frac{m_1 - m_2}{1 + m_1 m_2}\right|$$

donde $\theta$ está entre 0 y $\frac{\pi}{2}$.

---

## 📖 Casos especiales

- Si $m_1 = m_2$: las curvas son **tangentes** ($\theta = 0$)
- Si $m_1 m_2 = -1$: las curvas son **ortogonales** ($\theta = 90°$)
- Si $1 + m_1 m_2 = 0$: ángulo recto

---

## ⚙️ Ejemplo 1: Parábola y recta

Encuentra el ángulo entre $y = x^2$ y $y = x$ en sus intersecciones.

**Intersecciones:** $x^2 = x \Rightarrow x(x-1) = 0 \Rightarrow x = 0, 1$

**En $x = 0$:**
- $m_1 = 2(0) = 0$ (parábola)
- $m_2 = 1$ (recta)
- $\tan\theta = \left|\frac{0 - 1}{1 + 0}\right| = 1 \Rightarrow \theta = 45°$

**En $x = 1$:**
- $m_1 = 2(1) = 2$
- $m_2 = 1$
- $\tan\theta = \left|\frac{2 - 1}{1 + 2}\right| = \frac{1}{3} \Rightarrow \theta \approx 18.43°$

---

## ⚙️ Ejemplo 2: Dos parábolas

Encuentra el ángulo entre $y = x^2$ y $y = -x^2 + 2$.

**Intersección:** $x^2 = -x^2 + 2 \Rightarrow 2x^2 = 2 \Rightarrow x = \pm 1$

**En $x = 1$ (punto $(1, 1)$):**
- $m_1 = 2(1) = 2$
- $m_2 = -2(1) = -2$
- $\tan\theta = \left|\frac{2 - (-2)}{1 + (2)(-2)}\right| = \left|\frac{4}{-3}\right| = \frac{4}{3}$
- $\theta \approx 53.13°$

---

## 📖 Curvas ortogonales

Dos curvas son **ortogonales** si se cortan en ángulo recto:

$$m_1 \cdot m_2 = -1$$

---

## ⚙️ Ejemplo 3: Verificar ortogonalidad

¿Son ortogonales $xy = 4$ y $x^2 - y^2 = 0$ en sus intersecciones?

**Intersecciones:** De $x^2 - y^2 = 0$: $y = \pm x$

Con $xy = 4$ y $y = x$: $x^2 = 4 \Rightarrow x = 2$ (tomando positivo)

**Punto $(2, 2)$:**

Para $xy = 4$: $y + xy' = 0 \Rightarrow y' = -\frac{y}{x} = -1$

Para $x^2 - y^2 = 0$: $2x - 2yy' = 0 \Rightarrow y' = \frac{x}{y} = 1$

$m_1 \cdot m_2 = (-1)(1) = -1$ ✓

**Son ortogonales.**

---

## 📖 Familias ortogonales

Dos familias de curvas son **ortogonales** si cada curva de una familia es ortogonal a cada curva de la otra familia.

**Ejemplo clásico:**
- Círculos concéntricos: $x^2 + y^2 = c$
- Rectas radiales: $y = kx$

---

## ⚙️ Ejemplo 4: Encontrar familia ortogonal

Encuentra la familia ortogonal a $y = cx^2$.

**Paso 1:** Derivar para obtener $y'$:
$$y' = 2cx$$

**Paso 2:** Eliminar $c$:
$$c = \frac{y}{x^2}$$
$$y' = 2 \cdot \frac{y}{x^2} \cdot x = \frac{2y}{x}$$

**Paso 3:** Para la familia ortogonal, $y'_{ort} = -\frac{1}{y'}$:
$$\frac{dy}{dx} = -\frac{x}{2y}$$

**Paso 4:** Resolver:
$$2y\,dy = -x\,dx$$
$$y^2 = -\frac{x^2}{2} + C$$
$$x^2 + 2y^2 = k$$ (elipses)

Las parábolas $y = cx^2$ y las elipses $x^2 + 2y^2 = k$ son familias ortogonales.

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra el ángulo entre $y = x^3$ y $y = x$ en $x = 1$.

<details>
<summary>Ver solución</summary>

En $(1, 1)$:
- $m_1 = 3x^2 = 3$
- $m_2 = 1$

$\tan\theta = \left|\frac{3 - 1}{1 + 3}\right| = \frac{2}{4} = \frac{1}{2}$

$\theta = \arctan(0.5) \approx 26.57°$
</details>

---

**Ejercicio 2:** Demuestra que las curvas $y = e^x$ y $y = e^{-x}$ son ortogonales en su intersección.

<details>
<summary>Ver solución</summary>

Intersección: $e^x = e^{-x} \Rightarrow x = 0$

En $x = 0$:
- $(e^x)' = e^0 = 1$
- $(e^{-x})' = -e^0 = -1$

$m_1 \cdot m_2 = (1)(-1) = -1$ ✓ Ortogonales
</details>
