---
title: "Desplazamiento de Fase"
---

# **Desplazamiento de Fase**

Hasta ahora hemos estirado y aplastado las ondas. Ahora vamos a **moverlas** de lugar. Si empujas la gráfica a la derecha, a la izquierda, arriba o abajo, estás aplicando desplazamientos. Es como mover una diapositiva en una presentación.

---

## 🎯 ¿Qué vas a aprender?

- Cómo mover la gráfica horizontalmente (**Desplazamiento de Fase**).
- Cómo mover la gráfica verticalmente (**Desplazamiento Vertical**).
- La fórmula maestra que combina los 4 parámetros ($A, B, C, D$).
- Cómo calcular el rango final de una función desplazada.

---

## ↔️ Desplazamiento de Fase (Horizontal)

Este es el movimiento lateral. Ocurre cuando sumas o restas algo **dentro** del paréntesis, junto a la $x$.

Para $y = \sin(Bx - C)$:

$$
\text{Desplazamiento de Fase} = \frac{C}{B}
$$

> **¡Cuidado con el signo!** Funciona al revés de lo que piensas.
> *   $(x - C)$: Mueve a la **DERECHA**.
> *   $(x + C)$: Mueve a la **IZQUIERDA**.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Desplazamiento de fase (horizontal)</strong>
  </div>

![Desplazamiento de fase horizontal](/images/funciones/trigonometria/fase-horizontal.svg)

</div>

---

## ↕️ Desplazamiento Vertical

Este es el movimiento hacia arriba o abajo. Ocurre cuando sumas o restas algo **fuera** de la función.

Para $y = \sin(x) + D$:
*   $D > 0$: Sube.
*   $D < 0$: Baja.

El nuevo eje central de la onda será $y = D$.
El nuevo rango será $[D-A, D+A]$.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Desplazamiento vertical (D)</strong>
  </div>

![Desplazamiento vertical](/images/funciones/trigonometria/desplazamiento-vertical.svg)

</div>

---

## ⚛️ La Fórmula General

Combinando todo, tenemos la ecuación maestra de la trigonometría:

$$
y = A \sin(Bx - C) + D
$$

| Parámetro | Nombre | Efecto |
| :---: | :---: | :--- |
| **A** | Amplitud | Estira verticalmente. |
| **B** | Frecuencia | Estira horizontalmente (fórmula del periodo). |
| **C/B** | Fase | Mueve horizontalmente (cuidado, divide por B). |
| **D** | Vertical | Mueve verticalmente. |

---

## ⚙️ Análisis de Ejemplo

Analicemos la función:
$$
y = 3\sin(2x - \pi) + 1
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">y = 3sin(2x - π) + 1: Análisis completo</strong>
  </div>

![Ejemplo completo: y = 3sin(2x - π) + 1](/images/funciones/trigonometria/ejemplo-4-parametros.svg)

</div>

1.  **Amplitud:** $3$.
2.  **Periodo:** $2\pi/2 = \pi$.
3.  **Desplazamiento de Fase:** $C/B = \pi/2$. Como es resta, va a la **derecha**.
4.  **Desplazamiento Vertical:** $+1$. Sube 1 unidad.
5.  **Rango:** $[1-3, 1+3] = [-2, 4]$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el desplazamiento de fase de $y = \sin(x - \pi/2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$C = \pi/2$, $B = 1$.
Fase $= C/B = \pi/2$. Signo menos significa derecha.

**Respuesta:** $\boxed{\frac{\pi}{2} \text{ a la derecha}}$
</details>

---

### Ejercicio 2
¿Cuánto sube o baja la función $y = \cos(x) - 5$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$D = -5$.

**Respuesta:** **Baja 5 unidades**.
</details>

---

### Ejercicio 3
Calcula el rango de $y = 2\sin(x) + 3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Centro en 3. Sube 2 y baja 2.
Máximo: $3+2=5$. Mínimo: $3-2=1$.

**Respuesta:** $\boxed{[1, 5]}$
</details>

---

### Ejercicio 4
Determina el desplazamiento de fase de $y = \sin(2x - \pi)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$B=2, C=\pi$.
Fase $= \pi/2$.
Signo resta $\rightarrow$ Derecha.

**Respuesta:** $\boxed{\frac{\pi}{2} \text{ a la derecha}}$
</details>

---

### Ejercicio 5
Describe la transformación completa de $y = \sin(x+\pi)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Suma $\pi$ dentro del paréntesis.

**Respuesta:** **Desplazamiento $\pi$ a la izquierda**.
</details>

---

### Ejercicio 6
Si la función $y = \cos(x)$ se mueve $\pi/2$ a la derecha, ¿con qué otra función coincide?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos(x - \pi/2)$.
El coseno retrasado 90° es igual al seno.

**Respuesta:** $\boxed{\sin(x)}$
</details>

---

### Ejercicio 7
Encuentra el nuevo eje central de $y = 5\sin(3x) - 2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El eje central lo determina $D$.
$D = -2$.

**Respuesta:** $\boxed{y = -2}$
</details>

---

### Ejercicio 8
Determina el punto de inicio de un ciclo para $y = \sin(3x + \pi)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Igualamos el interior a 0 para ver dónde "resetea".
$3x + \pi = 0 \rightarrow 3x = -\pi \rightarrow x = -\pi/3$.

**Respuesta:** $\boxed{x = -\frac{\pi}{3}}$
</details>

---

### Ejercicio 9
Escribe la ecuación de un seno desplazado 2 unidades arriba.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$D = +2$.

**Respuesta:** $\boxed{y = \sin(x) + 2}$
</details>

---

### Ejercicio 10
Calcula el valor máximo de $y = -\cos(x) + 10$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Amplitud 1, desplazado 10 arriba.
La onda oscila alrededor de 10.
Máximo = $10 + 1$.

**Respuesta:** $\boxed{11}$
</details>

---

## 🔑 Resumen

| Parámetro | Posición en fórmula | Acción |
| :---: | :---: | :--- |
| **C** (Fase) | Dentro $(Bx - C)$ | Movimiento lateral (Signo opuesto). |
| **D** (Vertical) | Fuera $+ D$ | Movimiento vertical (Signo directo). |

> **Conclusión:** Recuerda siempre dividir $C$ entre $B$ para hallar el desplazamiento de fase real. Es la trampa más común ("la trampa de la frecuencia").
