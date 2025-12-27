# **Funciones Trigonométricas Inversas**

Hasta ahora has aprendido a tomar un ángulo y encontrar su seno, coseno o tangente. Es como ir de tu casa a la escuela. ¿Pero qué pasa si quieres volver? Las **funciones inversas** te permiten tomar un valor y encontrar el ángulo que lo generó.

---

## 🎯 ¿Qué vas a aprender?

- Qué son Arcoseno, Arcocoseno y Arcotangente.
- Por qué $\sin^{-1}(x)$ NO es lo mismo que $1/\sin(x)$.
- Las gráficas de las funciones inversas y sus rangos "cortados".
- Cómo usarlas para encontrar ángulos desconocidos en triángulos.

---

## 🔄 El Concepto de "Arco"

Las funciones inversas preguntan: **"¿El arco de qué ángulo me da este valor?"**

*   Si $\sin(30°) = 0.5$
*   Entonces $\arcsin(0.5) = 30°$

La notación puede ser confusa:
1.  **Arcseno:** $\arcsin(x)$ o $\sin^{-1}(x)$
2.  **Arcocoseno:** $\arccos(x)$ o $\cos^{-1}(x)$
3.  **Arcotangente:** $\arctan(x)$ o $\tan^{-1}(x)$

> ⚠️ **¡Pillada común!** El exponente $-1$ aquí significa **Función Inversa**, NO recíproco.
> $$ \sin^{-1}(x) \neq \frac{1}{\sin(x)} $$
> (El recíproco es la **cosecante**).

---

## 📉 Arcoseno ($\arcsin$)

Como el seno se repite infinitamente, no podemos simplemente "inventar" una inversa (daría infinitas respuestas). Tenemos que **restringirla**.
Solo tomamos el pedazo de la gráfica que va de $-90°$ a $+90°$.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = arcsin(x)</strong>
  </div>

![Gráfica del arcoseno](/images/funciones/trigonometria/arcsin.svg)

</div>

*   **Dominio:** $[-1, 1]$ (Solo puedes pedir arcoseno de números entre -1 y 1).
*   **Rango:** $[-\frac{\pi}{2}, \frac{\pi}{2}]$ (Cuadrantes I y IV).

---

## 📈 Arcocoseno ($\arccos$)

Para el coseno, restringimos la gráfica entre $0$ y $\pi$. Así cubrimos todos los valores posibles de 1 a -1 una sola vez.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = arccos(x)</strong>
  </div>

![Gráfica del arcocoseno](/images/funciones/trigonometria/arccos.svg)

</div>

*   **Dominio:** $[-1, 1]$.
*   **Rango:** $[0, \pi]$ (Cuadrantes I y II).

---

## 🚀 Arcotangente ($\arctan$)

Esta es genial porque acepta **cualquier número** como entrada.
Te devuelve un ángulo entre $-90°$ y $90°$.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = arctan(x)</strong>
  </div>

![Gráfica de la arcotangente](/images/funciones/trigonometria/arctan.svg)

</div>

*   **Dominio:** $(-\infty, \infty)$.
*   **Rango:** $(-\frac{\pi}{2}, \frac{\pi}{2})$ (Abierto, porque nunca toca 90°).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $\arcsin(1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
¿Qué ángulo (entre -90° y 90°) tiene seno igual a 1?
El ángulo de 90°.

**Respuesta:** $\boxed{\frac{\pi}{2}}$
</details>

---

### Ejercicio 2
Calcula $\arccos(0.5)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
¿Qué ángulo (entre 0° y 180°) tiene coseno 0.5?
El ángulo de 60°.

**Respuesta:** $\boxed{\frac{\pi}{3}}$
</details>

---

### Ejercicio 3
Calcula $\arctan(1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
¿Qué ángulo tiene tangente 1?
Es 45°.

**Respuesta:** $\boxed{\frac{\pi}{4}}$
</details>

---

### Ejercicio 4
Calcula $\arcsin(2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El dominio del arcoseno es $[-1, 1]$.
El número 2 está fuera del dominio (no existe ángulo con seno 2).

**Respuesta:** **Indefinido**
</details>

---

### Ejercicio 5
Calcula $\arctan(-1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Tangente es impar. El ángulo será negativo.
Si $\tan(45°) = 1$, entonces $\tan(-45°) = -1$.

**Respuesta:** $\boxed{-\frac{\pi}{4}}$
</details>

---

### Ejercicio 6
Calcula $\sin(\arcsin(0.3))$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Son funciones inversas, se "cancelan" mutuamente si el valor está en el dominio.
$0.3$ está en $[-1, 1]$.

**Respuesta:** $\boxed{0.3}$
</details>

---

### Ejercicio 7
Calcula $\arcsin(\sin(2\pi))$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ojo: $2\pi$ está fuera del rango del arcoseno.
1. $\sin(2\pi) = 0$.
2. $\arcsin(0) = 0$.

**Respuesta:** $\boxed{0}$ (No $2\pi$)
</details>

---

### Ejercicio 8
¿En qué cuadrante cae el resultado de $\arccos(-0.8)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El rango del arcocoseno es $[0, \pi]$.
Como el valor es negativo, debe estar en el **segundo cuadrante** (donde el coseno es negativo).

**Respuesta:** **Cuadrante II**
</details>

---

### Ejercicio 9
Calcula $\tan(\arcsin(\frac{3}{5}))$ sin calculadora.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Imagina un triángulo donde $\sin = \text{Opuesto}/\text{Hipotenusa} = 3/5$.
Por Pitágoras, el adyacente es $\sqrt{5^2 - 3^2} = 4$.
$\tan = \text{Opuesto}/\text{Adyacente} = 3/4$.

**Respuesta:** $\boxed{0.75}$
</details>

---

### Ejercicio 10
¿Cuál es el dominio de $\arccos(2x)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El argumento $2x$ debe estar entre -1 y 1.
$-1 \le 2x \le 1$.
Dividimos por 2: $-0.5 \le x \le 0.5$.

**Respuesta:** $\boxed{[-0.5, 0.5]}$
</details>

---

## 🔑 Resumen

| Función | Dominio (Entrada) | Rango (Salida) | Cuadrantes |
| :---: | :---: | :---: | :---: |
| $\arcsin(x)$ | $[-1, 1]$ | $[-\pi/2, \pi/2]$ | **IV y I** |
| $\arccos(x)$ | $[-1, 1]$ | $[0, \pi]$ | **I y II** |
| $\arctan(x)$ | $(-\infty, \infty)$ | $(-\pi/2, \pi/2)$ | **IV y I** |

> **Conclusión:** Las funciones inversas son "tímidas": solo viven en dos cuadrantes. Si buscas un ángulo en otro lugar, tendrás que usar tu ingenio (y ángulos de referencia) para encontrarlo.
