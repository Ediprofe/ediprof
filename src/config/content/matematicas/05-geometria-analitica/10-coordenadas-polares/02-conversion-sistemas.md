---
title: "Conversión entre Sistemas"
---

# **Conversión entre Sistemas**

Como ser bilingüe, un matemático debe saber traducir fluidamente entre el idioma del radar (Polares) y el idioma del mapa (Cartesianas). Las herramientas de traducción son el **Teorema de Pitágoras** y la **Trigonometría**.

---

## 🎯 ¿Qué vas a aprender?

- Fórmulas de Polar a Rectangular ($x, y$).
- Fórmulas de Rectangular a Polar ($r, \theta$).
- Cómo ajustar el cuadrante del ángulo con la arco-tangente.

---

## ➡️ Concepto 1: De Polares a Rectangulares

Si conoces $(r, \theta)$, es fácil hallar $(x, y)$. Solo proyecta la sombra del radio sobre los ejes.

$$ x = r \cos \theta $$
$$ y = r \sin \theta $$

**5 Ejemplos de Conversión:**

### Ejemplo 1.1
Convertir $(4, 60^\circ)$.
*   $x = 4 \cos(60^\circ) = 4(0.5) = 2$.
*   $y = 4 \sin(60^\circ) = 4(\sqrt{3}/2) = 2\sqrt{3}$.
*   **Resultado:** $(2, 2\sqrt{3})$.

### Ejemplo 1.2
Convertir $(10, \pi/2)$.
*   $x = 10 \cos(90^\circ) = 0$.
*   $y = 10 \sin(90^\circ) = 10$.
*   **Resultado:** $(0, 10)$.

### Ejemplo 1.3
Convertir $(-2, 0)$. (Radio negativo).
*   $x = -2 \cos(0) = -2(1) = -2$.
*   $y = -2 \sin(0) = -2(0) = 0$.
*   **Resultado:** $(-2, 0)$.

### Ejemplo 1.4
Convertir $(6, 225^\circ)$ (III Cuadrante).
*   $x = 6 (-\sqrt{2}/2) = -3\sqrt{2}$.
*   $y = 6 (-\sqrt{2}/2) = -3\sqrt{2}$.
*   **Resultado:** $(-3\sqrt{2}, -3\sqrt{2})$.

### Ejemplo 1.5
Convertir $(2, \pi)$.
*   $x = 2(-1) = -2$.
*   $y = 2(0) = 0$.
*   **Resultado:** $(-2, 0)$.

---

## ⬅️ Concepto 2: De Rectangulares a Polares

Si conoces $(x, y)$, quieres saber qué tan lejos está ($r$) y hacia dónde apunta ($\theta$).

1.  **Radio:** Pitágoras.
    $$ r = \sqrt{x^2 + y^2} $$
2.  **Ángulo:** Arco Tangente (¡Con cuidado!).
    $$ \theta = \arctan(y/x) $$

**🚨 ¡Alerta de Cuadrante!**
La calculadora te dará un ángulo entre $-90^\circ$ y $90^\circ$. Si tu punto está en el II o III cuadrante (X negativo), debes **SUMAR $180^\circ$ ($\pi$)** al resultado.

**5 Ejemplos de Conversión Inversa:**

### Ejemplo 2.1: I Cuadrante
Punto $(3, 3)$.
*   $r = \sqrt{9+9} = \sqrt{18} = 3\sqrt{2}$.
*   $\theta = \arctan(3/3) = \arctan(1) = 45^\circ$.
*   **Resultado:** $(3\sqrt{2}, 45^\circ)$.

### Ejemplo 2.2: II Cuadrante (Cuidado)
Punto $(-1, \sqrt{3})$.
*   $r = \sqrt{1+3} = 2$.
*   Calc: $\theta = \arctan(-\sqrt{3}) = -60^\circ$ (Incorrecto geométricamente, esto es IV cuadrante).
*   Ajuste: $-60^\circ + 180^\circ = 120^\circ$.
*   **Resultado:** $(2, 120^\circ)$.

### Ejemplo 2.3: III Cuadrante
Punto $(-2, -2)$.
*   $r = \sqrt{4+4} = \sqrt{8} = 2\sqrt{2}$.
*   Calc: $\arctan(1) = 45^\circ$.
*   Ajuste: $45^\circ + 180^\circ = 225^\circ$.
*   **Resultado:** $(2\sqrt{2}, 225^\circ)$.

### Ejemplo 2.4: IV Cuadrante
Punto $(1, -1)$.
*   $r = \sqrt{2}$.
*   $\theta = \arctan(-1) = -45^\circ$ ($315^\circ$).
*   **Resultado:** $(\sqrt{2}, 315^\circ)$.

### Ejemplo 2.5: Sobre un Eje
Punto $(0, -5)$.
*   $r = 5$.
*   $\arctan$ indefinido (división por cero).
*   Por inspección: Eje Y negativo $\to 270^\circ$.
*   **Resultado:** $(5, 270^\circ)$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Cartesiana de $(5, \pi)$.

<details>
<summary>Ver solución</summary>
$x=-5, y=0 \Rightarrow (-5, 0)$.
</details>

---

### Ejercicio 2
Cartesiana de $(2, 30^\circ)$.

<details>
<summary>Ver solución</summary>
$(\sqrt{3}, 1)$.
</details>

---

### Ejercicio 3
Polar de $(1, 0)$.

<details>
<summary>Ver solución</summary>
$(1, 0^\circ)$.
</details>

---

### Ejercicio 4
Polar de $(0, 2)$.

<details>
<summary>Ver solución</summary>
$(2, 90^\circ)$.
</details>

---

### Ejercicio 5
Calcula $r$ para $(-3, -4)$.

<details>
<summary>Ver solución</summary>
$\sqrt{9+16} = 5$.
</details>

---

### Ejercicio 6
Ángulo polar de $(-1, -1)$.

<details>
<summary>Ver solución</summary>
$225^\circ$ ($5\pi/4$).
</details>

---

### Ejercicio 7
Convierte $(0, 0)$ a polar.

<details>
<summary>Ver solución</summary>
$(0, \theta)$ (Ángulo indefinido).
</details>

---

### Ejercicio 8
Signo de $x$ si $\theta = 100^\circ$.

<details>
<summary>Ver solución</summary>
Negativo (II cuadrante).
</details>

---

### Ejercicio 9
Traducción polar de $x^2 + y^2 = 25$.

<details>
<summary>Ver solución</summary>
$r^2 = 25 \Rightarrow r = 5$.
</details>

---

### Ejercicio 10
Traducción polar de $y/x = 1$.

<details>
<summary>Ver solución</summary>
$\tan \theta = 1 \Rightarrow \theta = 45^\circ$.
</details>

---

## 🔑 Resumen

| Dirección | Fórmulas Clave | Tip |
| :--- | :--- | :--- |
| **P $\to$ R** | $x=r\cos\theta, y=r\sin\theta$ | Directo. La calculadora hace todo. |
| **R $\to$ P** | $r=\sqrt{x^2+y^2}, \tan\theta=y/x$ | **¡Ojo al Cuadrante!** Si $x<0$, suma $180^\circ$. |

> **Conclusión:** Las fórmulas son simples trigonometría. El único peligro es confiar ciegamente en la tecla `tan⁻¹` de la calculadora. Dibuja siempre el punto para saber dónde estás.
