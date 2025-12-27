# **Construcción de Ecuaciones**

Ahora que entendemos qué es un lugar geométrico, es momento de ponernos manos a la obra. Vamos a aprender a leer una descripción en español ("puntos que están al doble de distancia de A que de B") y convertirla en una ecuación algebraica rígida y exacta. Es como traducir poesía a código de computadora.

---

## 🎯 ¿Qué vas a aprender?

- El método paso a paso para construir cualquier ecuación.
- Cómo usar la fórmula de distancia como herramienta principal.
- Cómo simplificar ecuaciones con raíces (y no morir en el intento).
- Cómo identificar si la ecuación resultante es una recta, un círculo o algo más exótico.

---

## 🏗️ El Algoritmo de Construcción

Para encontrar la ecuación de un Lugar Geométrico (LG), sigue siempre estos 4 pasos sagrados:

1.  **Declara el Punto Genérico:** Sea $P(x, y)$ un punto cualquiera que cumple la regla.
2.  **Escribe la Condición:** Traduce la frase del problema a una igualdad matemática (ej: $d_{PA} = d_{PB}$).
3.  **Sustituye las Fórmulas:** Reemplaza las distancias, pendientes o áreas con sus fórmulas en función de $x$ y $y$.
4.  **Simplifica:** Elimina raíces, agrupa términos semejantes e iguala a cero si puedes.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">De la Condición a la Ecuación</strong>
  </div>
  <img src="/images/geometria/analitica/mediatriz.svg" alt="Mediatriz como lugar geométrico" style="width: 100%; height: auto;" />
</div>

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Circunferencia
**Problema:** Halla la ecuación de los puntos cuya distancia al origen es 7.

1.  **Punto Genérico:** $P(x, y)$.
2.  **Condición:** $d(P, O) = 7$.
3.  **Fórmula:** $\sqrt{(x-0)^2 + (y-0)^2} = 7$.
4.  **Simplificar:** Elevamos al cuadrado.
    $x^2 + y^2 = 49$.
    **Resultado:** $\boxed{x^2 + y^2 - 49 = 0}$.

### Ejemplo 2: Mediatriz (Equidistante de 2 puntos)
**Problema:** Puntos que equidistan de $A(1, 1)$ y $B(5, 1)$.

1.  **Punto Genérico:** $P(x, y)$.
2.  **Condición:** $d(P, A) = d(P, B)$.
3.  **Fórmula:** $\sqrt{(x-1)^2 + (y-1)^2} = \sqrt{(x-5)^2 + (y-1)^2}$.
4.  **Simplificar:**
    *   Elevamos al cuadrado para matar raíces: $(x-1)^2 + (y-1)^2 = (x-5)^2 + (y-1)^2$.
    *   Cancelamos $(y-1)^2$ (está en ambos lados): $(x-1)^2 = (x-5)^2$.
    *   Expandimos: $x^2 - 2x + 1 = x^2 - 10x + 25$.
    *   Cancelamos $x^2$: $-2x + 1 = -10x + 25$.
    *   Agrupamos $x$: $8x = 24 \Rightarrow x=3$.
    **Resultado:** $\boxed{x - 3 = 0}$ (Una recta vertical).

### Ejemplo 3: Razón de Distancias (Círculo de Apolonio)
**Problema:** La distancia de $P$ al origen es el DOBLE que su distancia a $(3, 0)$.

1.  **Condición:** $d(P, O) = 2 \cdot d(P, A)$.
2.  **Fórmula:** $\sqrt{x^2+y^2} = 2 \sqrt{(x-3)^2 + y^2}$.
3.  **Simplificar:**
    *   Cuadrado (¡OJO! El 2 se vuelve 4): $x^2 + y^2 = 4 \left( (x-3)^2 + y^2 \right)$.
    *   Expandir: $x^2 + y^2 = 4(x^2 - 6x + 9 + y^2)$.
    *   $x^2 + y^2 = 4x^2 - 24x + 36 + 4y^2$.
    *   Pasar todo a la derecha: $0 = 3x^2 + 3y^2 - 24x + 36$.
    *   Dividir todo por 3: $x^2 + y^2 - 8x + 12 = 0$.
    **Resultado:** $\boxed{x^2 + y^2 - 8x + 12 = 0}$ (Es una circunferencia).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Puntos a distancia 4 de $(2, 3)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{(x-2)^2+(y-3)^2}=4$. Cuadrado: $(x-2)^2+(y-3)^2=16$.

**Respuesta:** $\boxed{(x-2)^2+(y-3)^2=16}$
</details>

---

### Ejercicio 2
Puntos equidistantes de $y=2$ y el Eje X ($y=0$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Distancia a $y=2$ es $|y-2|$. Distancia a $y=0$ es $|y|$.
$|y-2| = |y|$. Punto medio es $y=1$.

**Respuesta:** $\boxed{y = 1}$
</details>

---

### Ejercicio 3
Puntos cuya suma de cuadrados de coordenadas es 25.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x^2 + y^2 = 25$.

**Respuesta:** $\boxed{x^2 + y^2 = 25}$
</details>

---

### Ejercicio 4
Puntos cuya abscisa es igual a su ordenada.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$x = y$.

**Respuesta:** $\boxed{x - y = 0}$
</details>

---

### Ejercicio 5
Puntos a distancia 1 del Eje Y.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Distancia al eje Y es $|x|$.
$|x| = 1 \Rightarrow x = 1$ o $x = -1$.

**Respuesta:** $\boxed{x = \pm 1}$
</details>

---

### Ejercicio 6
Puntos equidistantes de $(0,4)$ y $(0,-4)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Están en el eje Y. El punto medio es el origen.
La mediatriz es el Eje X ($y=0$).

**Respuesta:** $\boxed{y = 0}$
</details>

---

### Ejercicio 7
Distancia a $(1,0)$ igual a distancia a $(0,1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(x-1)^2 + y^2 = x^2 + (y-1)^2$.
$x^2-2x+1+y^2 = x^2+y^2-2y+1$.
$-2x = -2y \Rightarrow y=x$.

**Respuesta:** $\boxed{y = x}$
</details>

---

### Ejercicio 8
Puntos cuyo producto de coordenadas es 10.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$xy = 10$.

**Respuesta:** $\boxed{xy - 10 = 0}$
</details>

---

### Ejercicio 9
Puntos cuya distancia al origen es la mitad de su distancia a $(6,0)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sqrt{x^2+y^2} = 0.5 \sqrt{(x-6)^2+y^2}$.
$4(x^2+y^2) = (x-6)^2+y^2$. (Elevando cuadrado y pasando el 0.5 como 4 al otro lado).
$3x^2 + 3y^2 + 12x - 36 = 0$.

**Respuesta:** **Una circunferencia**
</details>

---

### Ejercicio 10
Puntos donde la ordenada es el cuadrado de la abscisa más 1.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$y = x^2 + 1$.

**Respuesta:** $\boxed{y - x^2 - 1 = 0}$
</details>

---

## 🔑 Resumen

| Condición | Fórmula Base |
| :--- | :--- |
| **Distancia a punto** | Pitágoras $\sqrt{\Delta x^2 + \Delta y^2}$. |
| **Distancia a recta H/V** | Valor absoluto $|x-k|$ o $|y-k|$. |
| **Equidistancia** | Igualar dos fórmulas de distancia. |
| **Razón ($d_1 = k \cdot d_2$)** | Elevar al cuadrado con cuidado ($d_1^2 = k^2 d_2^2$). |

> **Conclusión:** Construir una ecuación es como armar un mueble. Tienes las piezas (condiciones) y las herramientas (fórmulas). Solo necesitas ensamblarlas con cuidado y apretar los tornillos (simplificar algebraicamente).
