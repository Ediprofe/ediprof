---
title: "Resolución de Casos"
---

# **Resolución de Casos**

Has aprendido la Ley de Senos, de Cosenos y hasta la de Tangentes. Ahora el reto es saber **cuál usar** en cada situación. Un carpintero no usa un martillo para atornillar; tú no deberías usar la Ley de Senos cuando necesitas la de Cosenos.

---

## 🎯 ¿Qué vas a aprender?

- Cómo identificar rápidamente qué caso tienes (ALA, LAL, LLL, LLA).
- Un diagrama de flujo mental para elegir la herramienta correcta.
- Estrategias para evitar errores comunes (como perder soluciones en el caso LLA).
- Cómo resolver cualquier triángulo oblicuángulo de principio a fin.

---

## 🗺️ El Mapa de Decisiones

Para resolver un triángulo, necesitas **3 datos** (y al menos uno debe ser un lado).

### Paso 1: ¿Tengo una pareja completa?
Busca si tienes un **Lado** y su **Ángulo Opuesto** (ej: $a$ y $A$).

*   **SÍ tengo pareja:** ¡Genial! Usa la **Ley de Senos**. (Es más rápida).
    *   *Casos: ALA, LAA, LLA.*
*   **NO tengo pareja:** Te toca usar la **Ley de Cosenos**. (Es más robusta).
    *   *Casos: LAL, LLL.*

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Guía de Resolución de Triángulos</strong>
  </div>

![Casos de resolución](/images/trigonometria/triangulos-oblicuangulos/casos-resolucion.svg)

</div>

---

## 🛠️ Resumen de Estrategias

| Caso | Datos Conocidos | Herramienta | Estrategia |
| :---: | :--- | :--- | :--- |
| **AAL / ALA** | 2 Ángulos, 1 Lado | **Senos** | Halla el 3º ángulo ($180-A-B$), luego los lados. |
| **LLA** | 2 Lados, Ángulo Op. | **Senos** | **¡PELIGRO!** Caso Ambiguo. Puede haber 0, 1 o 2 soluciones. |
| **LAL** | 2 Lados, Ángulo Medio | **Cosenos** | Halla el 3º lado, luego usa Senos o Cosenos para ángulos. |
| **LLL** | 3 Lados | **Cosenos** | Halla el ángulo **mayor** primero para ver si es obtuso. |

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Caso LAL
Datos: $a=10, b=20, C=30°$.
¿Tengo pareja? No ($a$ va con $A$, $b$ con $B$, $C$ está solo).
$\rightarrow$ **Ley de Cosenos**.

1.  **Lado $c$:** $c^2 = 10^2 + 20^2 - 2(10)(20)\cos 30° = 100 + 400 - 400(0.866) = 153.6$.
    $c \approx 12.4$.
2.  **Ángulo $A$:** Ahora tengo pareja ($c$ y $C$). Uso Senos.
    $\frac{\sin A}{10} = \frac{\sin 30°}{12.4}$.
    $\sin A = 0.403 \rightarrow A \approx 23.8°$.
3.  **Ángulo $B$:** $180 - 30 - 23.8 = 126.2°$.

### Ejemplo 2: Caso LLA (Ambiguo)
Datos: $a=10, b=15, A=30°$.
¿Tengo pareja? Sí ($a$ y $A$).
$\rightarrow$ **Ley de Senos**.

1.  **Ángulo $B$:** $\frac{\sin B}{15} = \frac{\sin 30°}{10}$.
    $\sin B = 0.75$.
2.  **Posibilidad 1:** $B_1 = \sin^{-1}(0.75) \approx 48.6°$.
3.  **Posibilidad 2:** $B_2 = 180° - 48.6° = 131.4°$.
4.  **Verificación:**
    *   $30° + 48.6° < 180°$ (Válido).
    *   $30° + 131.4° < 180°$ (Válido).
    ¡Hay dos triángulos posibles!

---

## 📝 Ejercicios de Práctica

Identifica el caso y el primer paso para resolver.

### Ejercicio 1
Datos: $A=40°, B=60°, c=20$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Tengo 2 ángulos. Es caso ALA.
1. Hallar ángulo $C = 180 - 100 = 80°$.
2. Usar Ley de Senos.

**Respuesta:** **ALA (Ley de Senos)**
</details>

---

### Ejercicio 2
Datos: $a=5, b=6, c=7$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Tres lados. No hay parejas.
Es caso LLL. Ley de Cosenos para hallar un ángulo (preferiblemente el mayor, $C$).

**Respuesta:** **LLL (Ley de Cosenos)**
</details>

---

### Ejercicio 3
Datos: $a=10, b=10, A=100°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Dos lados, ángulo opuesto. LLA.
Pareja $a, A$. Ley de Senos.

**Respuesta:** **LLA (Ley de Senos)**
</details>

---

### Ejercicio 4
Datos: $b=8, c=12, A=45°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Dos lados y el ángulo entre ellos ($A$ está entre $b$ y $c$).
LAL. Ley de Cosenos para hallar $a$.

**Respuesta:** **LAL (Ley de Cosenos)**
</details>

---

### Ejercicio 5
Calcula el lado $c$ si $a=3, b=4, C=90°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es un triángulo rectángulo (Pitágoras).
$c = \sqrt{3^2+4^2} = 5$.

**Respuesta:** $\boxed{5}$
</details>

---

### Ejercicio 6
En el caso LLL, ¿por qué se recomienda hallar primero el ángulo mayor?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Para saber si es obtuso. El coseno distingue signos (agudo/obtuso), el seno no.

**Respuesta:** **Para detectar ángulos obtusos**
</details>

---

### Ejercicio 7
Si $\sin B = 1.5$ al resolver un triángulo, ¿qué significa?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El seno nunca puede ser mayor que 1.
Significa que no existe tal triángulo (el lado es muy corto para cerrar).

**Respuesta:** **Sin solución (triángulo imposible)**
</details>

---

### Ejercicio 8
¿Cuántos datos mínimos necesitas para resolver un triángulo?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Siempre 3 datos independientes.

**Respuesta:** $\boxed{3}$
</details>

---

### Ejercicio 9
Resuelve para $C$ si $A=50°, B=60°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$180 - (50+60) = 70°$.

**Respuesta:** $\boxed{70°}$
</details>

---

### Ejercicio 10
Si tienes LAL, ¿puedes usar la Ley de Tangentes?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sí, es una alternativa válida a la Ley de Cosenos para encontrar los ángulos primero.

**Respuesta:** **Sí**
</details>

---

## 🔑 Resumen

| ¿Tienes Pareja? | Estrategia |
| :--- | :--- |
| **SÍ** | Vete por la autopista rápida: **Ley de Senos**. |
| **NO** | Toma el camino seguro: **Ley de Cosenos**. |

> **Conclusión:** No te aprendas los casos de memoria. Solo busca la "pareja" (Lado y Ángulo Opuesto). Si la tienes, usas Senos. Si no, usas Cosenos. ¡Así de simple!
