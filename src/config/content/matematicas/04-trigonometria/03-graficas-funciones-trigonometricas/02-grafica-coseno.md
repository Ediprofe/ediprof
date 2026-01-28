---
title: "Gráfica de la Función Coseno"
---

# **Gráfica de la Función Coseno**

El **coseno** es el "hermano gemelo" del seno. Son tan parecidos que sus gráficas son idénticas, solo que una está desplazada respecto a la otra. ¿La diferencia visual más rápida? El coseno empieza en la cima de la montaña (1), no en el suelo (0).

---

## 🎯 ¿Qué vas a aprender?

- Cómo dibujar la gráfica de $y = \cos(x)$ sin usar tablas.
- La diferencia visual clave entre seno y coseno.
- Por qué decimos que el coseno es una función "par" (espejo).
- Cómo identificar dónde la función se hace cero, máxima o mínima.

---

## 🏔️ La Onda que Empieza Arriba

Mientras que el seno es la altura ($y$) en el círculo unitario, el coseno es la distancia horizontal ($x$).
Al ángulo 0° (inicio), la distancia horizontal es máxima (el radio completo). Por eso la gráfica empieza en 1.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Gráfica de y = cos(x)</strong>
  </div>

![Gráfica de la función coseno](/images/funciones/trigonometria/coseno-principal.svg)

</div>

**Propiedades Clave:**
1.  **Dominio:** $\mathbb{R}$.
2.  **Rango:** $[-1, 1]$.
3.  **Periodo:** $2\pi$.
4.  **Paridad:** Par (Simétrica eje Y).

---

## 📍 Anatomía de un Ciclo ($0$ a $2\pi$)

Observa lo que pasa en una vuelta completa:

| Punto | Ángulo $x$ | Valor $y$ | Descripción |
| :--- | :--- | :--- | :--- |
| **Inicio** | $0$ | $1$ | Empieza en el Máximo. |
| **Cruce** | $\pi/2$ ($90°$) | $0$ | Baja y cruza el eje. |
| **Mínimo** | $\pi$ ($180°$) | $-1$ | Llega al fondo. |
| **Cruce** | $3\pi/2$ ($270°$) | $0$ | Sube y cruza el eje. |
| **Fin** | $2\pi$ ($360°$) | $1$ | Vuelve a la cima. |

> **Patrón:** MÁX $\rightarrow$ CERO $\rightarrow$ MÍN $\rightarrow$ CERO $\rightarrow$ MÁX.

---

## 👯 Gemelos Desplazados

Si tomas la gráfica del seno y la empujas hacia la izquierda 90° ($\pi/2$), obtienes exactamente la gráfica del coseno.

$$
\cos(x) = \sin\left(x + \frac{\pi}{2}\right)
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Comparación: Seno vs Coseno</strong>
  </div>

![Comparación sin(x) vs cos(x)](/images/funciones/trigonometria/seno-vs-coseno.svg)

</div>

---

## 🪞 Simetría Par

El coseno funciona como un espejo. Lo que pasa a la izquierda del eje Y es idéntico a lo que pasa a la derecha.
Matemáticamente:
$$
\cos(-x) = \cos(x)
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
¿Cuál es el valor mínimo de la función $y = \cos(x)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El rango es $[-1, 1]$.
El mínimo absoluto es -1.

**Respuesta:** $\boxed{-1}$
</details>

---

### Ejercicio 2
¿En qué valores de $x$ (entre 0 y $2\pi$) la gráfica cruza el eje X?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Mirando la tabla de los 5 puntos clave: cruza en $90°$ y $270°$.

**Respuesta:** $\boxed{\frac{\pi}{2}, \frac{3\pi}{2}}$
</details>

---

### Ejercicio 3
Calcula $\cos(\pi)$ usando la gráfica.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
En $x = \pi$ (mitad del ciclo), la gráfica está en su punto más bajo.

**Respuesta:** $\boxed{-1}$
</details>

---

### Ejercicio 4
Determina el signo del coseno en el intervalo $(\frac{\pi}{2}, \frac{3\pi}{2})$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Entre 90° y 270°, la gráfica está por debajo del eje X ("bajo el agua").

**Respuesta:** **Negativo (-)**
</details>

---

### Ejercicio 5
¿Es la función coseno creciente o decreciente en el intervalo $[0, \pi]$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Empieza en 1 (0°) y baja hasta -1 (180°).
Va bajando todo el camino.

**Respuesta:** **Decreciente**
</details>

---

### Ejercicio 6
Calcula $\cos(-\frac{\pi}{3})$ sabiendo que $\cos(\frac{\pi}{3}) = 0.5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Simetría par: $\cos(-x) = \cos(x)$.
Los valores son idénticos.

**Respuesta:** $\boxed{0.5}$
</details>

---

### Ejercicio 7
¿Cuántas veces alcanza el coseno su valor máximo en el intervalo $[0, 4\pi]$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Alcanza el máximo al inicio de cada ciclo.
En $0$, $2\pi$ y $4\pi$.

**Respuesta:** **3 veces**
</details>

---

### Ejercicio 8
¿Cuál es la amplitud de la función $y = -3\cos(x)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La amplitud es el valor absoluto del coeficiente.
$|-3| = 3$.

**Respuesta:** $\boxed{3}$
</details>

---

### Ejercicio 9
Si desplazas la gráfica del coseno $\frac{\pi}{2}$ a la derecha, ¿qué función obtienes?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El coseno está "adelantado". Si lo atrasas (mueves a la erecha), coincide con el seno.
$\cos(x - \pi/2) = \sin(x)$.

**Respuesta:** $\boxed{\sin(x)}$
</details>

---

### Ejercicio 10
¿Para qué valores de $x$ en un ciclo se cumple $\cos(x) = 1$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Solo ocurre al principio y al final del intervalo cerrado.
$0$ y $2\pi$.

**Respuesta:** $\boxed{0, 2\pi}$
</details>

---

## 🔑 Resumen

| Característica | Seno | Coseno |
| :--- | :--- | :--- |
| **Inicio ($x=0$)** | **0** (Centro) | **1** (Cima) |
| **Primer cruce** | $\pi$ | $\pi/2$ |
| **Simetría** | Impar (Origen) | Par (Eje Y) |

> **Conclusión:** Si empieza en 0, es Seno. Si empieza en 1, es Coseno. Aparte de eso, ¡son la misma onda viajando por el espacio!
