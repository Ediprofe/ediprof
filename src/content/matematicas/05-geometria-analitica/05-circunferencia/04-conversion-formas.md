# **Conversión Entre Formas de la Circunferencia**

Eres bilingüe: hablas "Ordinaria" y "General". Pero a veces necesitas traducir. Si quieres graficar rápido, traduces a Ordinaria. Si quieres programar o resolver sistemas, traduces a General. Hoy practicaremos la traducción fluida.

---

## 🎯 ¿Qué vas a aprender?

- De Ordinaria a General: El arte de Expandir (Álgebra fácil).
- De General a Ordinaria: El arte de Completar Cuadrados (El truco ninja).
- Cómo verificar que no rompiste las matemáticas en el proceso.

---

## ➡️ De Ordinaria a General (Expandir)

Solo necesitas saber desarrollar binomios al cuadrado: $(a+b)^2 = a^2 + 2ab + b^2$.

**Algoritmo:**
1.  Expande los paréntesis $(x-h)^2$ y $(y-k)^2$.
2.  Mueve el $r^2$ a la izquierda.
3.  Ordena: Primero cuadrados ($x^2, y^2$), luego lineales ($x, y$), al final el número solo.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">El Proceso de Conversión</strong>
  </div>
  <img src="/images/geometria/analitica/conversion-formas-circ.svg" alt="Conversión entre formas" style="width: 100%; height: auto;" />
</div>

---

## ⬅️ De General a Ordinaria (Completar Cuadrados)

Esta dirección es más técnica. Tienes $x^2 + 6x$ y quieres volver a $(x+3)^2$.

**Algoritmo:**
1.  Agrupa las $x$ con $x$, las $y$ con $y$.
2.  Mueve el número suelto ($F$) a la derecha (cambia signo).
3.  **El Truco:** Toma el número que acompaña a la $x$, divídelo por 2, elévalo al cuadrado y SÚMALO a ambos lados. Repite para $y$.
4.  Factoriza los trinomios perfectos.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Ordinaria $\to$ General
Convertir $(x - 3)^2 + (y + 4)^2 = 25$.
1.  $x^2 - 6x + 9 + y^2 + 8y + 16 = 25$.
2.  Agrupar: $x^2 + y^2 - 6x + 8y + (9 + 16 - 25) = 0$.
3.  $x^2 + y^2 - 6x + 8y = 0$. (Pasa por el origen).

### Ejemplo 2: General $\to$ Ordinaria
Convertir $x^2 + y^2 + 10x - 2y + 10 = 0$.
1.  Agrupar: $(x^2 + 10x) + (y^2 - 2y) = -10$.
2.  **Completar:**
    *   $x$: Mitad de 10 es 5. Cuadrado es 25. Sumo 25.
    *   $y$: Mitad de -2 es -1. Cuadrado es 1. Sumo 1.
    *   Ecuación: $(x^2 + 10x + \mathbf{25}) + (y^2 - 2y + \mathbf{1}) = -10 + \mathbf{25} + \mathbf{1}$.
3.  Factorizar: $(x + 5)^2 + (y - 1)^2 = 16$.
    *   Centro $(-5, 1)$, Radio 4.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Expande $(x+1)^2 + (y-1)^2 = 4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2 + 2x + 1 + y^2 - 2y + 1 - 4 = 0$.

**Respuesta:** $\boxed{x^2 + y^2 + 2x - 2y - 2 = 0}$
</details>

---

### Ejercicio 2
Completa cuadrado para $x^2 - 8x$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Mitad de -8 es -4. Cuadrado 16.

**Respuesta:** $\boxed{(x-4)^2 - 16}$
</details>

---

### Ejercicio 3
Convierte $x^2 + y^2 - 4x = 0$ a Ordinaria.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(x^2 - 4x + 4) + y^2 = 4 \Rightarrow (x-2)^2 + y^2 = 4$.

**Respuesta:** $\boxed{(x-2)^2 + y^2 = 4}$
</details>

---

### Ejercicio 4
Expande $(x-5)^2 + y^2 = 25$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2 - 10x + 25 + y^2 - 25 = 0$.

**Respuesta:** $\boxed{x^2 + y^2 - 10x = 0}$
</details>

---

### Ejercicio 5
Halla el radio de $x^2 + y^2 + 6y = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2 + (y^2 + 6y + 9) = 9 \Rightarrow x^2 + (y+3)^2 = 9$.

**Respuesta:** $\boxed{3}$
</details>

---

### Ejercicio 6
Convierte $x^2 + y^2 + 2x + 2y + 2 = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(x^2+2x+1) + (y^2+2y+1) = -2+1+1 = 0$.
$(x+1)^2 + (y+1)^2 = 0$.

**Respuesta:** **Es un punto (-1, -1)**
</details>

---

### Ejercicio 7
¿Qué sumas a ambos lados para completar $y^2 - 5y$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(5/2)^2 = 25/4$.

**Respuesta:** $\boxed{6.25 \text{ o } 25/4}$
</details>

---

### Ejercicio 8
Expande $(x-0.5)^2 + y^2 = 0.25$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2 - x + 0.25 + y^2 = 0.25$.

**Respuesta:** $\boxed{x^2 + y^2 - x = 0}$
</details>

---

### Ejercicio 9
Convierte $2x^2 + 2y^2 - 8x = 0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Divide por 2 primero. $x^2 + y^2 - 4x = 0$.
$(x-2)^2 + y^2 = 4$.

**Respuesta:** $\boxed{(x-2)^2 + y^2 = 4}$
</details>

---

### Ejercicio 10
Si al completar cuadrados obtienes $= -5$, ¿qué significa?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Radio al cuadrado negativo imposibles.

**Respuesta:** **Circunferencia Imaginaria**
</details>

---

## 🔑 Resumen

| Dirección | Acción Clave | Cuidado con... |
| :--- | :--- | :--- |
| **Ord $\to$ Gen** | Binomio $(a-b)^2 = a^2 - 2ab + b^2$. | Sumar bien los números sueltos. |
| **Gen $\to$ Ord** | Mitad y Cuadrado. | Sumar lo mismo al lado derecho. |

> **Conclusión:** Completar el cuadrado es una técnica de nivel "Jefe Final". Si la dominas, dominas la geometría analítica completa (elipses, parábolas, todo).
