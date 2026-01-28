---
title: "Ecuación General de la Circunferencia"
---

# **Ecuación General de la Circunferencia**

Si desarrollas los cuadrados de la ecuación ordinaria y mueves todo a la izquierda, obtienes la **Ecuación General**. Es menos intuitiva (no ves el centro a simple vista), pero es la forma estándar en que las computadoras y los libros avanzados presentan las cónicas.

---

## 🎯 ¿Qué vas a aprender?

- La forma $x^2 + y^2 + Dx + Ey + F = 0$.
- Cómo recuperar el centro y el radio desde esta "sopa de letras".
- Cómo saber si la ecuación es una circunferencia real, un punto o nada (imaginaria).

---

## 🧩 La Fórmula Expandida

Partiendo de $(x - h)^2 + (y - k)^2 = r^2$, si expandimos:
$x^2 - 2hx + h^2 + y^2 - 2ky + k^2 - r^2 = 0$.

Reorganizando y renombrando constantes:
$$ x^2 + y^2 + Dx + Ey + F = 0 $$

Donde:
*   $D = -2h$
*   $E = -2k$
*   $F = h^2 + k^2 - r^2$

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">De General a Gráfica</strong>
  </div>
  <img src="/images/geometria/analitica/ecuacion-general-conicas.svg" alt="Ecuación general de la circunferencia" style="width: 100%; height: auto;" />
</div>

> **Truco Detective:** Para que sea circunferencia, $x^2$ y $y^2$ deben tener el **mismo coeficiente** (usualmente 1). Si son distintos, es una elipse o hipérbola.

---

## 🔍 Recuperando el Centro y Radio

Si te dan $x^2 + y^2 + Dx + Ey + F = 0$:

1.  **Centro $(h, k)$:**
    $$ h = -D/2 $$
    $$ k = -E/2 $$
    *(Solo divide D y E por -2)*.

2.  **Radio $r$:**
    $$ r = \sqrt{h^2 + k^2 - F} $$
    *(Usa el centro que acabas de hallar)*.

---

## ⚖️ El Discriminante (¿Existe?)

Lo que está dentro de la raíz ($h^2 + k^2 - F$) decide el destino:
*   **Positivo (>0):** Circunferencia Real.
*   **Cero (=0):** Es un Punto (Radio 0).
*   **Negativo (<0):** Circunferencia Imaginaria (No existe en el plano real).

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Análisis Completo
Dada $x^2 + y^2 - 6x + 4y - 12 = 0$.
1.  **Identificar:** $D=-6, E=4, F=-12$.
2.  **Centro:**
    $h = -(-6)/2 = 3$.
    $k = -4/2 = -2$.
    **C(3, -2)**.
3.  **Radio:**
    $r = \sqrt{3^2 + (-2)^2 - (-12)}$.
    $r = \sqrt{9 + 4 + 12} = \sqrt{25} = 5$.

### Ejemplo 2: ¿Es Real?
Dada $x^2 + y^2 + 2x + 2y + 10 = 0$.
1.  Centro: $(-1, -1)$.
2.  Radio: $\sqrt{(-1)^2 + (-1)^2 - 10} = \sqrt{1 + 1 - 10} = \sqrt{-8}$.
    **¡Error!** Raíz negativa. Es una circunferencia **Imaginaria**.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Halla el centro de $x^2 + y^2 - 10x + 6y - 2 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$h = -(-10)/2 = 5$.
$k = -6/2 = -3$.

**Respuesta:** $\boxed{(5, -3)}$
</details>

---

### Ejercicio 2
Halla el radio de la anterior ($C(5, -3), F=-2$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$r = \sqrt{25 + 9 - (-2)} = \sqrt{36} = 6$.

**Respuesta:** $\boxed{6}$
</details>

---

### Ejercicio 3
Convierte $(x-1)^2 + y^2 = 4$ a General.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2 - 2x + 1 + y^2 - 4 = 0$.

**Respuesta:** $\boxed{x^2 + y^2 - 2x - 3 = 0}$
</details>

---

### Ejercicio 4
Si $D=0$ y $E=0$, ¿dónde está el centro?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$h=0, k=0$.

**Respuesta:** **En el Origen**
</details>

---

### Ejercicio 5
Analiza $x^2 + y^2 + 4 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2+y^2 = -4$. Suma de cuadrados no puede ser negativa.

**Respuesta:** **Imaginaria**
</details>

---

### Ejercicio 6
Centro de $2x^2 + 2y^2 - 8x = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Primero divide todo por 2: $x^2 + y^2 - 4x = 0$.
$D=-4 \implies h=2, k=0$.

**Respuesta:** $\boxed{(2, 0)}$
</details>

---

### Ejercicio 7
¿Qué representa $x^2 + y^2 - 2x - 2y + 2 = 0$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$C(1, 1)$. $r = \sqrt{1+1-2} = \sqrt{0}$.

**Respuesta:** **Un Punto (1, 1)**
</details>

---

### Ejercicio 8
Expande $(x+3)^2 + (y-2)^2 = 9$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2 + 6x + 9 + y^2 - 4y + 4 - 9 = 0$.

**Respuesta:** $\boxed{x^2 + y^2 + 6x - 4y + 4 = 0}$
</details>

---

### Ejercicio 9
Si $F=0$, ¿por dónde pasa la circunferencia?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si $(0,0)$ cumple la ecuación ($0+0+0+0+0=0$).

**Respuesta:** **Por el Origen**
</details>

---

### Ejercicio 10
Halla $k$ para que $x^2 + y^2 + 4x - 6y + k = 0$ sea un punto.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Radio debe ser 0. $C(-2, 3)$.
$(-2)^2 + 3^2 - k = 0 \implies 4+9=k$.

**Respuesta:** $\boxed{13}$
</details>

---

## 🔑 Resumen

| Dato | Fórmula rápida |
| :--- | :--- |
| **Centro X** | Cambio signo de D y mitad. |
| **Centro Y** | Cambio signo de E y mitad. |
| **Radio** | Pitágoras con centro ($h, k$) menos F. |

> **Conclusión:** La ecuación general es "fea" pero útil. Solo recuerda limpiar los coeficientes de $x^2$ (dividiendo si es necesario) antes de aplicar las fórmulas de $D$ y $E$.
