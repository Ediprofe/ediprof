---
title: "Familias de Circunferencias"
---

# **Familias de Circunferencias**

Una familia es un grupo con rasgos compartidos. En el mundo de los círculos, una familia puede compartir el centro (como las ondas en un estanque), o compartir dos puntos por donde pasan. Estos grupos nos permiten modelar fenómenos como ondas, campos magnéticos y mapas topográficos.

---

## 🎯 ¿Qué vas a aprender?

- La Familia Concéntrica: Mismo centro, distinto radio.
- El Haz de Circunferencias: Todas pasan por la intersección de dos círculos base.
- El Eje Radical: La línea recta mágica donde los "poderes" se equilibran.

---

## 🎯 Tipos de Familias

### 1. Concéntricas (El Blanco de Tiro)
Comparten el centro $(h, k)$. Solo cambia $r$.
$$ (x-h)^2 + (y-k)^2 = k^2 $$
(Aquí $k$ es el parámetro variable, no la coordenada Y).

### 2. Haz de Circunferencias (Intersección)
Si tienes dos círculos $C_1 = 0$ y $C_2 = 0$ que se cruzan, puedes generar infinitos círculos que pasen por esos mismos dos puntos usando esta fórmula:
$$ C_1 + \lambda C_2 = 0 $$
Donde $\lambda$ (lambda) es un número que tú eliges.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Haz de Circunferencias</strong>
  </div>
  <img src="/images/geometria/analitica/haz-circunferencias.svg" alt="Haz de circunferencias" style="width: 100%; height: auto;" />
</div>

---

## ⚡ El Eje Radical

Es un caso especial del Haz. Si restas las ecuaciones de dos circunferencias ($C_1 - C_2 = 0$), los términos cuadráticos ($x^2, y^2$) se cancelan. ¡Lo que queda es una **Recta**!
Esta recta (Eje Radical) pasa por los puntos de intersección de los dos círculos.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Familia Concéntrica
Halla la familia con centro $(2, 3)$.
$$ (x-2)^2 + (y-3)^2 = R^2 $$
Si quiero el miembro que pasa por $(5, 7)$, sustituyo:
$(5-2)^2 + (7-3)^2 = R^2 \Rightarrow 3^2 + 4^2 = R^2 \Rightarrow 25 = R^2$.
Ecuación: $(x-2)^2 + (y-3)^2 = 25$.

### Ejemplo 2: El Eje Radical
$C_1: x^2 + y^2 = 4$
$C_2: x^2 + y^2 - 4x = 0$
Resta ($C_1 - C_2$):
$(x^2+y^2-4) - (x^2+y^2-4x) = 0$
$4x - 4 = 0 \Rightarrow x = 1$.
El eje radical es la recta vertical $x=1$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la familia de círculos con centro en el origen.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2 + y^2 = R^2$.

**Respuesta:** $\boxed{x^2 + y^2 = R^2}$
</details>

---

### Ejercicio 2
Halla el eje radical de $x^2+y^2=1$ y $x^2+y^2 - 2y = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Resta: $-1 - (-2y) = 0 \Rightarrow 2y - 1 = 0$.

**Respuesta:** $\boxed{y = 0.5}$
</details>

---

### Ejercicio 3
¿Qué forma tienen los círculos $x^2+y^2+Dx=0$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sus centros están en el eje X ($E=0$) y pasan por el origen ($F=0$).

**Respuesta:** **Centros en Eje X, pasan por (0,0)**
</details>

---

### Ejercicio 4
Si $\lambda = -1$ en el haz, ¿qué obtienes?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$C_1 - C_2 = 0$. Se van los cuadrados.

**Respuesta:** **El Eje Radical (Recta)**
</details>

---

### Ejercicio 5
Familia de círculos de radio 5 con centro en $y=x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Centro $(h, h)$. Radio 5.

**Respuesta:** $\boxed{(x-h)^2 + (y-h)^2 = 25}$
</details>

---

### Ejercicio 6
Dos círculos concéntricos se pueden tocar?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Solo si tienen el mismo radio (son el mismo). Si no, jamás.

**Respuesta:** **No (salvo si son idénticos)**
</details>

---

### Ejercicio 7
Ecuación del círculo más pequeño de una familia concéntrica.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Radio 0 (El punto centro).

**Respuesta:** **El punto centro**
</details>

---

### Ejercicio 8
¿El eje radical es perpendicular a la línea de los centros?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Propiedad fundamental. Siempre lo es.

**Respuesta:** **Sí, siempre**
</details>

---

### Ejercicio 9
Escribe la familia tangente al eje X en el origen.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Centro en el eje Y $(0, k)$. Radio $k$.
$x^2 + (y-k)^2 = k^2 \Rightarrow x^2 + y^2 - 2ky = 0$.

**Respuesta:** $\boxed{x^2 + y^2 + Ey = 0}$
</details>

---

### Ejercicio 10
¿Cuántos círculos pasan por 3 puntos no alineados?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Solo uno. (El circuncentro del triángulo).

**Respuesta:** **Exactamente uno**
</details>

---

## 🔑 Resumen

| Concepto | Fórmula |
| :--- | :--- |
| **Concéntricas** | $(x-h)^2 + (y-k)^2 = \text{Variable}$. |
| **Haz** | $C_1 + \lambda C_2 = 0$. |
| **Eje Radical** | $C_1 - C_2 = 0$ (Recta). |

> **Conclusión:** Las familias nos permiten generalizar. En lugar de resolver un problema para un solo círculo, lo resolvemos para infinitos círculos a la vez.
