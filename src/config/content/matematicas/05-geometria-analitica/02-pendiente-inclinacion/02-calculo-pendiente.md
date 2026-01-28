---
title: "Cálculo de la Pendiente"
---

# **Cálculo de la Pendiente**

Ya sabemos que la pendiente es "subida sobre avance". Pero, ¿cómo calculamos ese número exacto si solo tenemos dos puntos en un plano? No necesitamos una cinta métrica, solo una simple resta y una división.

---

## 🎯 ¿Qué vas a aprender?

- La famosa fórmula de la pendiente ($m$).
- Cómo aplicarla dados dos puntos cualesquiera $(x_1, y_1)$ y $(x_2, y_2)$.
- Por qué el orden de los puntos no importa.
- Cómo detectar errores de signos (el error más común).

---

## 🧬 La Fórmula Maestra

Para ir del punto A al punto B, tienes que averiguar cuánto cambió la altura ($y$) y cuánto cambió la posición horizontal ($x$).

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Fórmula de la Pendiente</strong>
  </div>
  <img src="/images/geometria/analitica/calculo-pendiente.svg" alt="Cálculo de la pendiente con Δx y Δy" style="width: 100%; height: auto;" />
</div>

$$
m = \frac{\text{Cambio en } y}{\text{Cambio en } x} = \frac{y_2 - y_1}{x_2 - x_1}
$$

> **Truco Nemotécnico:** Las $y$ van arriba (porque "yes" queremos subir). Las $x$ van abajo.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Pendiente Positiva
Calcula $m$ para los puntos $A(1, 2)$ y $B(3, 6)$.

**Paso 1: Identificar**
$x_1=1, y_1=2$
$x_2=3, y_2=6$

**Paso 2: Diferencias (Restas)**
Arriba ($y$): $6 - 2 = 4$.
Abajo ($x$): $3 - 1 = 2$.

**Paso 3: División**
$$ m = \frac{4}{2} = 2 $$

**Interpretación:** La recta sube 2 unidades por cada 1 que avanza.

### Ejemplo 2: Cuidado con los Negativos
Calcula $m$ para $P(-2, 3)$ y $Q(1, -3)$.

**Paso 1: Diferencias**
Arriba ($y$): $-3 - 3 = -6$.
Abajo ($x$): $1 - (-2) = 1 + 2 = 3$.

**Paso 2: División**
$$ m = \frac{-6}{3} = -2 $$

**Interpretación:** La recta baja 2 unidades por cada 1 que avanza.

---

## 📝 Ejercicios de Práctica

### Ejemplo 1
Calcula $m$ para $(2, 5)$ y $(4, 9)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{9-5}{4-2} = \frac{4}{2} = 2$.

**Respuesta:** $\boxed{2}$
</details>

---

### Ejemplo 2
Calcula $m$ para $(0, 0)$ y $(5, 10)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{10-0}{5-0} = \frac{10}{5} = 2$.

**Respuesta:** $\boxed{2}$
</details>

---

### Ejemplo 3
Calcula $m$ para $(1, 8)$ y $(3, 2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{2-8}{3-1} = \frac{-6}{2} = -3$.

**Respuesta:** $\boxed{-3}$
</details>

---

### Ejemplo 4
Calcula $m$ para $(-2, -1)$ y $(2, 3)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{3-(-1)}{2-(-2)} = \frac{4}{4} = 1$.

**Respuesta:** $\boxed{1}$
</details>

---

### Ejemplo 5
Calcula $m$ para $(3, 4)$ y $(7, 4)$. (Misma altura).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{4-4}{7-3} = \frac{0}{4} = 0$.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejemplo 6
Calcula $m$ para $(5, 2)$ y $(5, 8)$. (Misma $x$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{8-2}{5-5} = \frac{6}{0}$. Indefinida.

**Respuesta:** **Indefinida**
</details>

---

### Ejemplo 7
Si $m=3$ y pasa por $(0,0)$ y $(2, y)$. Halla $y$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$3 = \frac{y-0}{2-0} \Rightarrow 3 = \frac{y}{2} \Rightarrow y=6$.

**Respuesta:** $\boxed{6}$
</details>

---

### Ejemplo 8
Calcula $m$ para $(100, 200)$ y $(101, 205)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{205-200}{101-100} = \frac{5}{1} = 5$.

**Respuesta:** $\boxed{5}$
</details>

---

### Ejemplo 9
Si cambias el orden de los puntos ($A \to B$ vs $B \to A$), ¿cambia $m$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No. $\frac{y_1-y_2}{x_1-x_2}$ da lo mismo que $\frac{y_2-y_1}{x_2-x_1}$ (los signos negativos se cancelan).

**Respuesta:** **No, da lo mismo**
</details>

---

### Ejemplo 10
Halla la pendiente de una recta que pasa por $(a, 0)$ y $(0, b)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\frac{b-0}{0-a} = \frac{b}{-a} = -\frac{b}{a}$.

**Respuesta:** $\boxed{-\frac{b}{a}}$
</details>

---

## 🔑 Resumen

| Paso | Acción |
| :--- | :--- |
| **1** | Resta las $y$ arriba. |
| **2** | Resta las $x$ abajo (¡en el mismo orden!). |
| **3** | Simplifica la fracción. |

> **Conclusión:** Calcular la pendiente es solo restar y dividir. El único "enemigo" son los signos negativos (menos por menos da más). ¡Vigílalos de cerca!
