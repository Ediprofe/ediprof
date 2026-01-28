---
title: "Introducción a Coordenadas Polares"
---

# **Introducción a Coordenadas Polares**

Imagina que eres un controlador de tráfico aéreo. No le dices a un piloto "muévete 5 km al este y 3 km al norte". Le dices "gira 30 grados y avanza 6 km". Eso es el sistema polar: una dirección y una distancia.

---

## 🎯 ¿Qué vas a aprender?

- El concepto de Polo (origen) y Eje Polar (eje X).
- Cómo ubicar puntos usando radio $r$ y ángulo $\theta$.
- Por qué un mismo punto tiene infinitos nombres.

---

## 🧭 El Sistema Polar

En lugar de una cuadrícula de calles ($x, y$), usamos una diana de tiro al blanco.
1.  **Polo ($O$):** El punto central fijo (equivalente al origen).
2.  **Eje Polar:** Una semirrecta horizontal que sale hacia la derecha (equivalente al eje X positivo).
3.  **Coordenadas $(r, \theta)$:**
    *   **$r$ (Radio):** Distancia desde el Polo hasta el punto.
    *   **$\theta$ (Ángulo):** Giro desde el Eje Polar (en sentido antihorario).

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Plano Polar</strong>
  </div>
  <img src="/images/geometria/analitica/plano-polar.svg" alt="Representación de un punto en coordenadas polares" style="width: 100%; height: auto;" />
</div>

---

## 📍 Concepto 1: Ubicación de Puntos

Para graficar $(r, \theta)$, primero giras el ángulo $\theta$ y luego caminas $r$ pasos.

**5 Ejemplos de Ubicación:**

### Ejemplo 1.1
Punto $A(3, 60^\circ)$.
*   Gira $60^\circ$.
*   Avanza 3 unidades desde el centro.

### Ejemplo 1.2
Punto $B(4, \pi)$.
*   Gira $\pi$ radianes ($180^\circ$).
*   Avanza 4 unidades (hacia la izquierda).

### Ejemplo 1.3
Punto $C(2, -90^\circ)$.
*   Gira $90^\circ$ en sentido **horario** (hacia abajo).
*   Avanza 2 unidades.

### Ejemplo 1.4
Punto $D(5, 0^\circ)$.
*   No gires.
*   Avanza 5 unidades sobre el eje polar.

### Ejemplo 1.5
Punto $E(1, 450^\circ)$.
*   Gira una vuelta completa ($360^\circ$) más $90^\circ$.
*   Quedas mirando hacia arriba. Avanza 1 unidad.

---

## 🔄 Concepto 2: El Radio Negativo

¿Qué significa un radio negativo, como $(-3, 45^\circ)$?
Significa que miras hacia $45^\circ$, pero caminas 3 pasos **hacia atrás** (en dirección opuesta, o sea, $225^\circ$).

**5 Ejemplos de Radios Negativos:**

### Ejemplo 2.1
$(-2, 0^\circ)$.
*   Mira a la derecha ($0^\circ$).
*   Camina 2 pasos atrás. Terminas en $(-2, 0)$ cartesiano.

### Ejemplo 2.2
$(-4, 90^\circ)$.
*   Mira arriba ($90^\circ$).
*   Camina 4 atrás. Terminas abajo ($270^\circ$).

### Ejemplo 2.3
$(-1, \pi/4)$.
*   Mira a $45^\circ$.
*   Camina 1 atrás. Es equivalente a $(1, 5\pi/4)$.

### Ejemplo 2.4
$(-5, 180^\circ)$.
*   Mira a la izquierda.
*   Camina atrás. Terminas a la derecha ($0^\circ$).

### Ejemplo 2.5
$(-3, -30^\circ)$.
*   Mira a $-30^\circ$ (cuadrante IV).
*   Camina atrás. Terminas en el cuadrante II ($150^\circ$).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Ubica $(2, 3\pi/2)$.

<details>
<summary>Ver solución</summary>
2 unidades hacia abajo (sobre el eje Y negativo).
</details>

---

### Ejercicio 2
Escribe otra coordenada polar para $(3, 90^\circ)$.

<details>
<summary>Ver solución</summary>
$(3, 450^\circ)$ o $(-3, 270^\circ)$.
</details>

---

### Ejercicio 3
¿Dónde está el punto $(0, 50^\circ)$?

<details>
<summary>Ver solución</summary>
En el Polo (Origen). Si $r=0$, el ángulo no importa.
</details>

---

### Ejercicio 4
Convierte el ángulo de $(5, \pi)$ a grados.

<details>
<summary>Ver solución</summary>
$180^\circ$. Punto: $(5, 180^\circ)$.
</details>

---

### Ejercicio 5
Describe la posición de $(4, -180^\circ)$.

<details>
<summary>Ver solución</summary>
A 4 unidades a la izquierda del polo.
</details>

---

### Ejercicio 6
¿El punto $(-2, 0)$ está a la derecha o izquierda?

<details>
<summary>Ver solución</summary>
A la izquierda. (Mira a $0^\circ$, camina atrás).
</details>

---

### Ejercicio 7
¿En qué cuadrante está $(3, 100^\circ)$?

<details>
<summary>Ver solución</summary>
II Cuadrante (entre 90 y 180).
</details>

---

### Ejercicio 8
¿En qué cuadrante está $(2, -10^\circ)$?

<details>
<summary>Ver solución</summary>
IV Cuadrante.
</details>

---

### Ejercicio 9
Suma $2\pi$ al ángulo de $(1, \pi/2)$.

<details>
<summary>Ver solución</summary>
$(1, 5\pi/2)$. Es el mismo punto geométrico.
</details>

---

### Ejercicio 10
Distancia del punto $(r, \theta)$ al polo.

<details>
<summary>Ver solución</summary>
$|r|$.
</details>

---

## 🔑 Resumen

| Característica | Detalle |
| :--- | :--- |
| **Polo** | El origen $(0,0)$. |
| **Eje Polar** | La referencia de $0^\circ$ (Eje X+). |
| **No Unicidad** | Un punto tiene infinitas coordenadas $(r, \theta + 2n\pi)$. |

> **Conclusión:** El sistema polar es circular. Mientras el cartesiano es una cuadrícula de ciudad, el polar es un radar que barre el horizonte.
