# **Distancia de un Punto a una Recta**

Imagina que estás en medio del mar (un punto) y hay una costa recta a lo lejos. Si quieres nadar hacia la orilla lo más rápido posible, no nadas en diagonal. Nadas en línea recta perpendicular a la playa. Esa distancia mínima es lo que aprenderemos a calcular hoy.

---

## 🎯 ¿Qué vas a aprender?

- La fórmula definitiva para calcular distancias exactas.
- Por qué usamos el valor absoluto.
- Cómo saber si dos puntos están del mismo lado de la recta o en lados opuestos.
- Calcular la distancia entre dos rectas paralelas.

---

## 📏 La Fórmula de la Distancia

Para hallar la distancia $d$ desde un punto $P(x_1, y_1)$ hasta una recta $Ax + By + C = 0$:

$$
d = \frac{|Ax_1 + By_1 + C|}{\sqrt{A^2 + B^2}}
$$

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">La Ruta Más Corta (Perpendicular)</strong>
  </div>
  <img src="/images/geometria/analitica/distancia-punto-recta.svg" alt="Distancia de punto a recta" style="width: 100%; height: auto;" />
</div>

> **Nota:** La recta debe estar escrita en su **Forma General** ($=0$). Si te la dan como $y=mx+b$, primero ordénala.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Cálculo Básico
Punto $P(2, 3)$ y Recta $3x + 4y - 12 = 0$.
1.  **Sustituir:** Reemplaza $x$ con 2 y $y$ con 3 en la ecuación.
    $3(2) + 4(3) - 12 = 6 + 12 - 12 = 6$.
2.  **Numerador:** $|6| = 6$.
3.  **Denominador (Radical):** $\sqrt{3^2 + 4^2} = \sqrt{9+16} = \sqrt{25} = 5$.
4.  **Dividir:** $d = 6/5 = 1.2$.

### Ejemplo 2: Distancia al Origen
Distancia de $5x - 12y + 26 = 0$ al origen $(0,0)$.
1.  **Sustituir:** $5(0) - 12(0) + 26 = 26$.
2.  **Denominador:** $\sqrt{5^2 + (-12)^2} = \sqrt{25 + 144} = \sqrt{169} = 13$.
3.  **Dividir:** $d = 26/13 = 2$.

### Ejemplo 3: Puntos en Lados Opuestos
Si evaluamos la ecuación sin valor absoluto para dos puntos distintos:
*   Si los signos son iguales ($+/+$ o $-/-$), están del **mismo lado**.
*   Si los signos son opuestos ($+/-$), están en **lados opuestos** de la recta.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Distancia de $(1, 1)$ a $3x - 4y + 1 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Num: $|3(1) - 4(1) + 1| = |0| = 0$.
(El punto está sobre la recta).

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 2
Distancia de $(0, 0)$ a $x + y - 4 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Num: $|-4| = 4$. Den: $\sqrt{1+1} = \sqrt{2}$.
$d = 4/\sqrt{2} = 2\sqrt{2}$.

**Respuesta:** $\boxed{2\sqrt{2} \approx 2.82}$
</details>

---

### Ejercicio 3
Distancia de $(2, -1)$ a $4x + 3y + 10 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Num: $4(2) + 3(-1) + 10 = 8 - 3 + 10 = 15$.
Den: $\sqrt{16+9} = 5$.
$d = 15/5 = 3$.

**Respuesta:** $\boxed{3}$
</details>

---

### Ejercicio 4
Distancia entre las rectas paralelas $x+y=2$ y $x+y=5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Toma un punto de la primera (ej: $2,0$) y halla la distancia a la segunda ($x+y-5=0$).
Num: $|2+0-5| = 3$. Den: $\sqrt{2}$.

**Respuesta:** $\boxed{3/\sqrt{2}}$
</details>

---

### Ejercicio 5
Distancia de $(5, 5)$ a la recta horizontal $y=2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Visualmente es obvio: de $y=5$ a $y=2$ hay 3 unidades.
Fórmula: $0x + 1y - 2 = 0$. Num: $|5-2|=3$. Den: 1.

**Respuesta:** $\boxed{3}$
</details>

---

### Ejercicio 6
Distancia de $(3, 3)$ a la recta vertical $x=1$.

<details>
<summary>Ver solución</summary>
<br>
**Razonamiento:**
Diferencia en X: $|3 - 1| = 2$.

**Respuesta:** $\boxed{2}$
</details>

---

### Ejercicio 7
Si la distancia es 0, ¿qué significa?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No hay separación.

**Respuesta:** **El punto pertenece a la recta**
</details>

---

### Ejercicio 8
Calcula la altura del triángulo con vértice $A(1,2)$ y base en la recta $3x-4y-5=0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La altura es la distancia del vértice a la base.
Num: $|3(1) - 4(2) - 5| = |3 - 8 - 5| = |-10| = 10$.
Den: 5.
$h = 10/5 = 2$.

**Respuesta:** $\boxed{2}$
</details>

---

### Ejercicio 9
¿El punto $(0,0)$ está arriba o abajo de $y = x + 2$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Recta: $x - y + 2 = 0$. Evaluamos $(0,0) \to +2$.
Coeficiente de Y es -1 (negativo). Signos opuestos (+/-) significa "arriba" (generalmente).
Visualmente: Recta pasa por $(0,2)$, el origen $(0,0)$ está "abajo".

**Respuesta:** **Abajo**
</details>

---

### Ejercicio 10
Distancia de $(-1, 2)$ a $12x + 5y - 3 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Num: $|12(-1) + 5(2) - 3| = |-12 + 10 - 3| = |-5| = 5$.
Den: $\sqrt{144+25} = 13$.

**Respuesta:** $\boxed{5/13 \approx 0.38}$
</details>

---

## 🔑 Resumen

| Paso | Acción |
| :--- | :--- |
| **1. Ordenar** | Escribir recta como $Ax + By + C = 0$. |
| **2. Numerador** | Sustituir el punto y tomar Valor Absoluto. |
| **3. Denominador** | Calcular $\sqrt{A^2 + B^2}$. |
| **4. Dividir** | Resultado siempre positivo. |

> **Conclusión:** Esta fórmula es tu regla de medir universal. Funciona para cualquier recta en cualquier dirección. Es fundamental para calcular áreas de triángulos y polígonos.
