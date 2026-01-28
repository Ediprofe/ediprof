---
title: "Recta Tangente a la Circunferencia"
---

# **Recta Tangente a la Circunferencia**

Una tangente es una recta que "besa" a la circunferencia en un solo punto, rozándola suavemente sin atravesarla. Este concepto es crucial en física (la velocidad es tangente a la trayectoria) y en diseño de carreteras.

---

## 🎯 ¿Qué vas a aprender?

- La propiedad fundamental: Radio $\perp$ Tangente.
- Cómo hallar la ecuación de la tangente si conoces el punto de contacto.
- Cómo hallarla si solo conoces la pendiente (habrá dos soluciones).

---

## 📐 La Propiedad de Oro

> **Regla:** La recta tangente a una circunferencia es siempre **perpendicular al radio** en el punto de contacto.

Esto simplifica todo:
1.  Calcula la pendiente del radio ($m_{rad}$).
2.  La pendiente de la tangente es la inversa negativa: $m_{tan} = -1 / m_{rad}$.
3.  Usa la ecuación Punto-Pendiente.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Geometría de la Tangente</strong>
  </div>
  <img src="/images/geometria/analitica/tangente-circunferencia.svg" alt="Recta tangente a la circunferencia" style="width: 100%; height: auto;" />
</div>

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Tangente en un Punto
Circunferencia $x^2 + y^2 = 25$ en el punto $(3, 4)$.
1.  **Centro:** $(0, 0)$. **Punto:** $(3, 4)$.
2.  **Pendiente Radio:** $m_{rad} = \frac{4-0}{3-0} = \frac{4}{3}$.
3.  **Pendiente Tangente:** $m_{tan} = -\frac{3}{4}$.
4.  **Ecuación:** Pasando por $(3, 4)$.
    $y - 4 = -\frac{3}{4}(x - 3) \Rightarrow 4y - 16 = -3x + 9$.
    $3x + 4y - 25 = 0$.

### Ejemplo 2: Tangentes con Pendiente Conocida
Halla las tangentes a $x^2 + y^2 = 9$ con pendiente $m=1$ (Paralelas a $y=x$).
La fórmula para el desplazamiento $c$ es $c = \pm r\sqrt{1+m^2}$.
*   $r=3, m=1$.
*   $c = \pm 3\sqrt{1+1} = \pm 3\sqrt{2}$.
*   Ecuaciones: $y = x + 3\sqrt{2}$ y $y = x - 3\sqrt{2}$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Tangente a $x^2+y^2=10$ en $(1, 3)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m_{rad} = 3/1 = 3 \to m_{tan} = -1/3$.
$y-3 = -1/3(x-1) \to 3y-9 = -x+1$.

**Respuesta:** $\boxed{x + 3y - 10 = 0}$
</details>

---

### Ejercicio 2
Tangente a $x^2+y^2=1$ en $(0, 1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Punto más alto. Tangente horizontal.

**Respuesta:** $\boxed{y = 1}$
</details>

---

### Ejercicio 3
Pendiente de la tangente a $(x-2)^2 + y^2 = 5$ en $(4, 1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$C(2,0)$. $m_{rad} = (1-0)/(4-2) = 0.5$. $m_{tan} = -2$.

**Respuesta:** $\boxed{-2}$
</details>

---

### Ejercicio 4
¿Cuántas tangentes puedes trazar desde un punto EXTERIOR?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Imagina un cono de helado. Dos lados.

**Respuesta:** **Dos**
</details>

---

### Ejercicio 5
Desde el centro, ¿cuántas tangentes puedes trazar?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ninguna que toque el borde desde adentro.

**Respuesta:** **Cero**
</details>

---

### Ejercicio 6
Halla las tangentes horizontales de $x^2+y^2=16$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$r=4$. Arriba y abajo.

**Respuesta:** $\boxed{y = 4, y = -4}$
</details>

---

### Ejercicio 7
Si la tangente es vertical $x=5$, ¿dónde está el centro si $r=5$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El centro debe estar a 5 unidades de la tangente. $x_c = 0$ o $x_c = 10$.

**Respuesta:** **En x=0 o x=10**
</details>

---

### Ejercicio 8
Usa la fórmula $x_0 x + y_0 y = r^2$ para el ejemplo 1.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$3x + 4y = 25$.

**Respuesta:** $\boxed{3x + 4y = 25}$
</details>

---

### Ejercicio 9
Tangente a $x^2+y^2=5$ en $(-1, -2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$-x - 2y = 5 \Rightarrow x + 2y + 5 = 0$.

**Respuesta:** $\boxed{x + 2y + 5 = 0}$
</details>

---

### Ejercicio 10
Distancia del centro a cualquier tangente.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Definición de tangencia.

**Respuesta:** **El Radio**
</details>

---

## 🔑 Resumen

| Método | Cuándo usarlo |
| :--- | :--- |
| **Perpendicularidad** | Cuando tienes el punto de contacto. ($m_{tan} = -1/m_{rad}$). |
| **Fórmula Desdoble** | Para círculos en el origen ($x_0x + y_0y = r^2$). ¡La más rápida! |
| **Discriminante** | Cuando buscas la pendiente ($m$) y no tienes el punto. |

> **Conclusión:** La recta tangente es la "frontera segura". Te permite acercarte al máximo a la curva sin chocar contra ella.
