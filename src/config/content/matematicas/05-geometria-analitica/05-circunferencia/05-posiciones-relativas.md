---
title: "Posiciones Relativas entre Circunferencias y Rectas"
---

# **Posiciones Relativas entre Circunferencias y Rectas**

En el billar, una bola (circunferencia) puede rodar libremente, rozar la banda (recta tangente) o chocar contra ella (recta secante). Estas son las tres posiciones relativas. Hoy aprenderemos a predecir qué va a pasar usando ecuaciones.

---

## 🎯 ¿Qué vas a aprender?

- Las tres interacciones posibles entre una recta y una circunferencia: Exterior, Tangente, Secante.
- Cómo usar la distancia para diagnosticar la posición.
- Cómo interactúan dos circunferencias entre sí (el eclipse solar).

---

## 🎱 Recta vs. Circunferencia

Imagina que la circunferencia es una fortaleza con un muro a distancia $r$ del centro. Una recta enemiga se acerca.
Calculamos $d$, la distancia del Centro a la Recta.

| Caso | Comparación | Interpretación | Puntos de Contacto |
| :--- | :--- | :--- | :--- |
| **Exterior** | $d > r$ | La recta pasa lejos. | 0 |
| **Tangente** | $d = r$ | La recta besa el borde. | 1 |
| **Secante** | $d < r$ | La recta atraviesa el interior. | 2 |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Posiciones Relativas</strong>
  </div>
  <img src="/images/geometria/analitica/posiciones-recta-circ.svg" alt="Posiciones recta-circunferencia" style="width: 100%; height: auto;" />
</div>

---

## 🔵 Circunferencia vs. Circunferencia

Sean dos circunferencias con radios $R$ y $r$, y distancia entre centros $d$.

1.  **Exteriores:** $d > R+r$. (Lejos).
2.  **Tangentes Exteriores:** $d = R+r$. (Se tocan por fuera, como un "8").
3.  **Secantes:** $R-r < d < R+r$. (Se cruzan en dos puntos, como un diagrama de Venn).
4.  **Tangentes Interiores:** $d = R-r$. (Una dentro de otra, tocándose en un punto).
5.  **Interiores:** $d < R-r$. (Una flota dentro de la otra).
6.  **Concéntricas:** $d = 0$. (Mismo centro).

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Diagnóstico Recta
Circunferencia $x^2 + y^2 = 25$ ($C(0,0), r=5$). Recta $x=6$.
1.  Distancia del centro $(0,0)$ a la recta vertical $x=6$ es $d=6$.
2.  Comparar: $d=6, r=5$.
3.  $6 > 5$.
    **Resultado:** Recta Exterior.

### Ejemplo 2: Diagnóstico Circunferencias
$C_1$ radio 5, $C_2$ radio 3. Distancia entre centros $d=2$.
1.  Suma radios: $5+3=8$.
2.  Resta radios: $5-3=2$.
3.  Comparar $d=2$ con la resta.
    **Resultado:** Tangentes Interiores. (El pequeño está justo tocando el borde interno del grande).

### Ejemplo 3: Cálculo Algebraico (Intersección)
Intersección de $x^2+y^2=1$ y recta $y=2$.
Sustituir: $x^2 + (2)^2 = 1 \Rightarrow x^2 + 4 = 1 \Rightarrow x^2 = -3$.
No hay solución real para $x$.
**Resultado:** No se tocan (Exterior).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Posición de la recta $y=5$ respecto a $x^2+y^2=9$ ($r=3$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Distancia al centro $(0,0)$ es 5. Radio 3. $5 > 3$.

**Respuesta:** **Exterior**
</details>

---

### Ejercicio 2
Posición de $y=3$ respecto a $x^2+y^2=9$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Distancia 3. Radio 3. $d=r$.

**Respuesta:** **Tangente**
</details>

---

### Ejercicio 3
Dos circunferencias con radios 10 y 2, distancia 15.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$10+2=12$. Distancia $15 > 12$.

**Respuesta:** **Exteriores**
</details>

---

### Ejercicio 4
Dos circunferencias con radios 5 y 5, distancia 0.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Mismo centro, mismo radio.

**Respuesta:** **Coincidentes (La misma)**
</details>

---

### Ejercicio 5
Recta $3x+4y=0$ y círculo $x^2+y^2=25$ ($r=5$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Recta pasa por el origen (centro).

**Respuesta:** **Secante (Diámetro)**
</details>

---

### Ejercicio 6
Circunferencias tangentes exteriormente, radios 4 y 6. ¿Distancia?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$d = R+r = 4+6$.

**Respuesta:** $\boxed{10}$
</details>

---

### Ejercicio 7
Si el discriminante de la ecuación de intersección es positivo, ¿posición?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Dos soluciones reales $\to$ dos puntos.

**Respuesta:** **Secante**
</details>

---

### Ejercicio 8
Recta $y=x$ y círculo unitario. ¿Corta?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Pasa por el centro. Corta en 2 puntos.

**Respuesta:** **Sí, Secante**
</details>

---

### Ejercicio 9
Círculo dentro de otro sin tocarse.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$d < R-r$.

**Respuesta:** **Interiores**
</details>

---

### Ejercicio 10
Posición de $x=10$ con $x^2+y^2=1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$d=10, r=1$. Muy lejos.

**Respuesta:** **Exterior**
</details>

---

## 🔑 Resumen

| Método | Herramienta |
| :--- | :--- |
| **Geométrico** | Comparar distancia $d$ con radio $r$. (Más rápido). |
| **Algebraico** | Resolver el sistema de ecuaciones. (Más preciso, da los puntos exactos). |

> **Conclusión:** Antes de resolver ecuaciones complejas, calcula siempre la distancia $d$. A menudo te ahorra mucho trabajo saber de antemano si la recta ni siquiera toca al círculo.
