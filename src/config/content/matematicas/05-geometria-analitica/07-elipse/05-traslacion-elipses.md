---
title: "Traslación de Elipses (Vértice fuera del Origen)"
---

# **Traslación de Elipses (Vértice fuera del Origen)**

Las elipses no siempre viven en el centro del universo $(0,0)$. Pueden estar en cualquier parte del plano. Cuando su centro se mueve a unas coordenadas $(h, k)$, su ecuación se "viste" con paréntesis para reflejar este cambio.

---

## 🎯 ¿Qué vas a aprender?

- Escribir la ecuación $(h, k)$: $(x-h)^2$ y $(y-k)^2$.
- Determinar el centro y la orientación a simple vista.
- Calcular los "4 Puntos Cardinales" (Vértices) reales.

---

## 🚀 La Ecuación Trasladada

Es la misma ecuación canónica, pero $x$ se convierte en $(x-h)$ y $y$ en $(y-k)$.

**1. Horizontal:** (El denominador mayor $a^2$ bajo X)
$$ \frac{(x-h)^2}{a^2} + \frac{(y-k)^2}{b^2} = 1 $$

**2. Vertical:** (El denominador mayor $a^2$ bajo Y)
$$ \frac{(x-h)^2}{b^2} + \frac{(y-k)^2}{a^2} = 1 $$

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Elipse Trasladada</strong>
  </div>
  <img src="/images/geometria/analitica/elipse-trasladada.svg" alt="Elipse con centro fuera del origen" style="width: 100%; height: auto;" />
</div>

---

## 🔍 Coordenadas Globales

Para hallar los puntos reales, sumamos el vector centro $(h, k)$ a los valores relativos:

*   **Centro:** $(h, k)$.
*   **Vértices/Focos:** Tomas $(h, k)$ y le sumas/restas $a$ o $c$ a la coordenada correspondiente (X si es horizontal, Y si es vertical).

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Lectura de Ecuación
$$ \frac{(x-2)^2}{9} + \frac{(y+1)^2}{25} = 1 $$
1.  **Centro:** $(2, -1)$. (Signos contrarios).
2.  **Orientación:** 25 > 9 y está bajo Y $\to$ **Vertical**.
3.  **Parámetros:**
    *   $a = 5$.
    *   $b = 3$.
    *   $c = \sqrt{25-9} = 4$.
4.  **Focos:**
    Como es vertical, modificamos la Y del centro.
    $F = (2, -1 \pm 4) \Rightarrow (2, 3) \text{ y } (2, -5)$.

### Ejemplo 2: Escritura de Ecuación
Centro $(-3, 5)$, Eje mayor horizontal de 10, Eje menor de 6.
1.  **Centro:** $h=-3, k=5$.
2.  **Parámetros:**
    *   $2a = 10 \Rightarrow a = 5 \Rightarrow a^2 = 25$.
    *   $2b = 6 \Rightarrow b = 3 \Rightarrow b^2 = 9$.
3.  **Orientación:** Horizontal (el grande va bajo X).
4.  **Ecuación:**
    $$ \frac{(x+3)^2}{25} + \frac{(y-5)^2}{9} = 1 $$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Halla el centro de $\frac{(x-5)^2}{16} + \frac{(y-2)^2}{4} = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cambiar signos.

**Respuesta:** $\boxed{(5, 2)}$
</details>

---

### Ejercicio 2
Orientación de la elipse anterior.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
16 > 4 y está bajo X.

**Respuesta:** **Horizontal**
</details>

---

### Ejercicio 3
Escribe ecuación: Centro $(0, 2)$, $a=4, b=1$, Vertical.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a^2$ bajo Y. $x^2/1 + (y-2)^2/16 = 1$.

**Respuesta:** $\boxed{\frac{x^2}{1} + \frac{(y-2)^2}{16} = 1}$
</details>

---

### Ejercicio 4
Calcula los focos si $C(1,1)$ y $c=2$ (Horizontal).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sumar a la X. $(1+2, 1)$ y $(1-2, 1)$.

**Respuesta:** $\boxed{(3, 1) \text{ y } (-1, 1)}$
</details>

---

### Ejercicio 5
Vértices mayores de $\frac{(x+1)^2}{9} + \frac{(y-2)^2}{25} = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Vertical $a=5$. Centro $(-1, 2)$. $(-1, 2\pm 5)$.

**Respuesta:** $\boxed{(-1, 7) \text{ y } (-1, -3)}$
</details>

---

### Ejercicio 6
Longitud del eje menor en $\frac{(x-10)^2}{100} + \frac{(y+8)^2}{64} = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$b^2=64 \Rightarrow b=8$. $2b=16$.

**Respuesta:** $\boxed{16}$
</details>

---

### Ejercicio 7
Si el centro es el origen, ¿en qué se convierte esta ecuación?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
En la forma canónica ordinaria.

**Respuesta:** **Elipse Canónica**
</details>

---

### Ejercicio 8
Excentricidad de elipse trasladada vs centrada. (Si $a,b$ son iguales).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La traslación no cambia la forma, solo la posición. La excentricidad es igual.

**Respuesta:** **Es la misma**
</details>

---

### Ejercicio 9
Dibuja los ejes de simetría de $\frac{(x-3)^2}{4} + \frac{(y-2)^2}{9} = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x=3$ (Eje Menor) y $y=2$ (Eje Mayor Vertical).

**Respuesta:** **Rectas x=3 y y=2**
</details>

---

### Ejercicio 10
Distancia del Foco 1 al Foco 2.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Siempre es $2c$, no importa dónde esté el centro.

**Respuesta:** $\boxed{2c}$
</details>

---

## 🔑 Resumen

| Paso | Acción |
| :--- | :--- |
| **1. Ubicar Centro** | Extraer $(h, k)$ de los paréntesis con signo cambiado. |
| **2. Definir Rumbo** | Mirar cuál denominador es mayor ($a^2$). |
| **3. Moverse** | Sumar $a, b, c$ a la coordenada ($x$ o $y$) según corresponda. |

> **Conclusión:** Es como mover un mueble. El mueble (la elipse $a, b$) sigue siendo el mismo, solo cambia su dirección postal $(h, k)$.
