---
title: "Gráficas de Cotangente, Secante y Cosecante"
---

# **Gráficas de Cotangente, Secante y Cosecante**

Si ya conoces a los "Tres Grandes" (Seno, Coseno y Tangente), ahora te presentamos a sus contrapartes: las **funciones recíprocas**. Son como los "reversos" de las funciones originales, llenas de curvas en forma de U y asíntotas invisibles.

---

## 🎯 ¿Qué vas a aprender?

- Cómo se ven las gráficas de $\cot(x)$, $\sec(x)$ y $\csc(x)$.
- Por qué tienen "zonas prohibidas" entre -1 y 1.
- Cómo usar las gráficas de seno y coseno como "esqueleto" para dibujar estas.
- Dónde aparecen sus asíntotas verticales.

---

## 📉 Gráfica de la Cotangente

La cotangente es la inversa multiplicativa de la tangente:
$$
\cot(x) = \frac{1}{\tan(x)} = \frac{\cos(x)}{\sin(x)}
$$

*   **Asíntotas:** Donde $\sin(x) = 0$ (en $0, \pi, 2\pi...$).
*   **Ceros:** Donde $\cos(x) = 0$ (en $90°, 270°...$).
*   **Comportamiento:** Al revés de la tangente. Siempre va **bajando** (decreciente).

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = cot(x)</strong>
  </div>

![Gráfica de la cotangente](/images/funciones/trigonometria/cotangente.svg)

</div>

---

## ∪ Gráfica de la Secante

La secante es la recíproca del coseno:
$$
\sec(x) = \frac{1}{\cos(x)}
$$

*   **Truco:** Dibuja el coseno suavemente. Donde el coseno es 1, la secante toca la cima y sube. Donde el coseno es -1, la secante toca el fondo y baja.
*   **Zona Prohibida:** Nunca está entre -1 y 1.
*   **Asíntotas:** Donde $\cos(x) = 0$ ($90°, 270°...$).

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = sec(x) vs y = cos(x)</strong>
  </div>

![Gráfica de la secante](/images/funciones/trigonometria/secante.svg)

</div>

---

## ∩ Gráfica de la Cosecante

La cosecante es la recíproca del seno:
$$
\csc(x) = \frac{1}{\sin(x)}
$$

El patrón es idéntico al de la secante, pero desplazado (igual que el seno está desplazado del coseno).
*   **Puntos de contacto:** Las "U" tocan las cimas y valles de la onda senoidal.
*   **Asíntotas:** Donde $\sin(x) = 0$ ($0, \pi, 2\pi...$).

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = csc(x) vs y = sin(x)</strong>
  </div>

![Gráfica de la cosecante](/images/funciones/trigonometria/cosecante.svg)

</div>

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
¿Cuál es el valor mínimo positivo que puede tomar la función $\sec(x)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El rango de la secante positiva es $[1, \infty)$.
El valor más bajo es 1.

**Respuesta:** $\boxed{1}$
</details>

---

### Ejercicio 2
Determina dónde tiene asíntotas verticales la función $\csc(x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\csc(x) = 1/\sin(x)$.
Indefinida cuando $\sin(x) = 0$.
Esto ocurre en $k\pi$ ($0, \pi, 2\pi...$).

**Respuesta:** En los múltiplos enteros de $\pi$.
</details>

---

### Ejercicio 3
Calcula $\cot(45°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cot(45°) = 1/\tan(45°)$.
$\tan(45°) = 1$.
$1/1 = 1$.

**Respuesta:** $\boxed{1}$
</details>

---

### Ejercicio 4
¿Es verdad que $\sec(x)$ nunca puede ser cero?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sí. $\sec(x) = 1/\cos(x)$.
Para que una fracción sea cero, el numerador debe ser cero.
Aquí el numerador es siempre 1.

**Respuesta:** **Verdadero**
</details>

---

### Ejercicio 5
En el intervalo $(0, \pi)$, ¿dónde es la cotangente igual a cero?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cot(x) = \cos(x)/\sin(x)$.
Es cero cuando $\cos(x) = 0$.
En ese intervalo, ocurre a 90°.

**Respuesta:** $\boxed{\frac{\pi}{2}}$
</details>

---

### Ejercicio 6
Si $\sin(x) = 0.5$, ¿cuánto vale $\csc(x)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Son recíprocos.
$\csc(x) = 1/0.5 = 2$.

**Respuesta:** $\boxed{2}$
</details>

---

### Ejercicio 7
¿Cuál es el periodo de $\sec(x)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Depende del coseno.
El periodo del coseno es $2\pi$.
Por tanto, la secante también repite su patrón cada $2\pi$.

**Respuesta:** $\boxed{2\pi}$
</details>

---

### Ejercicio 8
¿En qué cuadrantes es la cotangente positiva?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Igual que la tangente.
Positiva donde Seno y Coseno tienen el mismo signo.
Cuadrantes I y III.

**Respuesta:** **I y III**
</details>

---

### Ejercicio 9
Describe el comportamiento de $\csc(x)$ cuando $x$ se acerca a 0 por la derecha.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x \to 0^+$, seno es positivo muy pequeño.
$1 / (\text{positivo pequeño}) = \text{infinito positivo}$.

**Respuesta:** **Tiende a $+\infty$**
</details>

---

### Ejercicio 10
¿Es $\sec(x)$ una función par o impar?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Hereda la simetría de su recíprococo, el coseno.
El coseno es par.

**Respuesta:** **Par**
</details>

---

## 🔑 Resumen

| Función | Recíproca de... | Dominio prohibido | Rango |
| :--- | :--- | :--- | :--- |
| **Cotangente** | Tangente | $k\pi$ | $\mathbb{R}$ |
| **Secante** | Coseno | $\frac{\pi}{2} + k\pi$ | Fuera de $(-1, 1)$ |
| **Cosecante** | Seno | $k\pi$ | Fuera de $(-1, 1)$ |

> **Conclusión:** Las gráficas recíprocas viven donde sus madres no pueden. Si el seno es pequeño, la cosecante es gigante. Si el seno es cero, la cosecante explota. Son el Yin y el Yang de la magnitud.
