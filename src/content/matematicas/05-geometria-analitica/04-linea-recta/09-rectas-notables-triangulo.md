# **Rectas Notables de un Triángulo**

Un triángulo es mucho más que tres lados. Esconde puntos secretos donde ocurren cosas mágicas: el equilibrio perfecto, el centro de su círculo protector, el cruce de sus alturas. Hoy usaremos geometría analítica para encontrar estos tesoros.

---

## 🎯 ¿Qué vas a aprender?

- Qué son las Medianas, Alturas, Mediatrices y Bisectrices.
- Cómo calcular sus ecuaciones usando puntos y pendientes.
- Cómo encontrar el Baricentro, Ortocentro, Circuncentro e Incentro.

---

## 🏆 Los 4 Puntos Fantásticos

| Recta Notable | ¿Qué hace? | Punto de Cruce | Símbolo |
| :--- | :--- | :--- | :--- |
| **Mediana** | Va del vértice al punto medio opuesto. | **Baricentro** (Centro de gravedad). | $G$ |
| **Altura** | Cae perpendicularmente desde el vértice. | **Ortocentro**. | $H$ |
| **Mediatriz** | Perpendicular que divide un lado en dos. | **Circuncentro** (Centro del círculo que lo rodea). | $O$ |
| **Bisectriz** | Divide el ángulo en dos partes iguales. | **Incentro** (Centro del círculo interno). | $I$ |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Puntos Notables</strong>
  </div>
  <img src="/images/geometria/analitica/rectas-notables.svg" alt="Rectas notables del triángulo" style="width: 100%; height: auto;" />
</div>

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Calculando una Mediana
Vértices: $A(0,0), B(6,0), C(4,8)$. Halla la mediana desde $C$.
1.  **Punto Medio de AB:** $M = (\frac{0+6}{2}, \frac{0+0}{2}) = (3, 0)$.
2.  **Recta por C(4,8) y M(3,0):**
    $$ m = \frac{0-8}{3-4} = \frac{-8}{-1} = 8 $$
    $$ y - 0 = 8(x - 3) \Rightarrow y = 8x - 24 $$

### Ejemplo 2: Calculando una Altura
Triángulo $A(1,1), B(4,1), C(2,3)$. Halla la altura desde $C$.
1.  **Pendiente del lado AB:** $m_{AB} = \frac{1-1}{4-1} = 0$. (Horizontal).
2.  **Pendiente de la Altura:** Perpendicular a horizontal es Vertical (indefinida).
3.  **Recta por C(2,3):** Como es vertical, $x = 2$.

### Ejemplo 3: Calculando una Mediatriz
Segmento $A(2,2)$ y $B(6,4)$.
1.  **Punto Medio:** $M = (\frac{2+6}{2}, \frac{2+4}{2}) = (4, 3)$.
2.  **Pendiente AB:** $m_{AB} = \frac{4-2}{6-2} = \frac{2}{4} = 0.5$.
3.  **Pendiente Perpendicular:** $m_{\perp} = -1/0.5 = -2$.
4.  **Ecuación:** Recta por $(4,3)$ con $m=-2$.
    $$ y - 3 = -2(x - 4) $$
    $$ y = -2x + 11 $$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Halla el Baricentro de $A(0,0), B(3,0), C(0,3)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Promedio de coordenadas. $G = (\frac{0+3+0}{3}, \frac{0+0+3}{3})$.

**Respuesta:** $\boxed{(1, 1)}$
</details>

---

### Ejercicio 2
Halla la pendiente de la altura relativa a un lado con pendiente 2.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Inversa negativa. $m = -1/2$.

**Respuesta:** $\boxed{-0.5}$
</details>

---

### Ejercicio 3
La mediatriz pasa por un vértice... ¿Verdadero o Falso?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Solo es cierto en triángulos isósceles o equiláteros.

**Respuesta:** **Falso (generalmente)**
</details>

---

### Ejercicio 4
Calcula el punto medio del lado $A(-2,4)$ y $B(6,-2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$Pm = (2, 1)$.

**Respuesta:** $\boxed{(2, 1)}$
</details>

---

### Ejercicio 5
¿Dónde se cruzan las alturas de un triángulo rectángulo?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
En el vértice del ángulo recto.

**Respuesta:** **En el vértice de 90°**
</details>

---

### Ejercicio 6
Halla la ecuación de la altura sobre el lado horizontal $y=5$ que pasa por $(3,10)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Debe ser vertical y pasar por $x=3$.

**Respuesta:** $\boxed{x = 3}$
</details>

---

### Ejercicio 7
Si el Circuncentro está en el punto medio de la hipotenusa, ¿qué triángulo es?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Propiedad única del triángulo rectángulo.

**Respuesta:** **Rectángulo**
</details>

---

### Ejercicio 8
Halla la pendiente de la mediana desde $(0,0)$ al punto medio $(3,4)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$m = 4/3$.

**Respuesta:** $\boxed{4/3}$
</details>

---

### Ejercicio 9
Calcula el Baricentro si los puntos medios de los lados son $(1,1), (2,2), (3,1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El baricentro del triángulo original es el mismo que el del triángulo de puntos medios.
$G = (\frac{1+2+3}{3}, \frac{1+2+1}{3})$.

**Respuesta:** $\boxed{(2, 4/3)}$
</details>

---

### Ejercicio 10
Halla la ecuación de la mediatriz del segmento con extremos $(0,0)$ y $(10,0)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Punto medio $(5,0)$. Segmento horizontal, mediatriz vertical.

**Respuesta:** $\boxed{x = 5}$
</details>

---

## 🔑 Resumen

| Si buscas... | Necesitas... | ¿Cómo lo haces? |
| :--- | :--- | :--- |
| **Mediana** | Punto Medio. | Recta Vértice $\leftrightarrow$ Punto Medio. |
| **Altura** | Pendiente $\perp$. | Recta Vértice con $m = -1/m_{lado}$. |
| **Mediatriz** | Punto Medio + Pendiente $\perp$. | Recta por Punto Medio con $m = -1/m_{lado}$. |
| **Baricentro** | Promedio. | Sumar coordenadas y dividir entre 3. |

> **Conclusión:** No intentes memorizar dónde va cada punto. Recuerda la definición lógica ("altura es alto/perpendicular", "mediana va al medo"). La geometría analítica hace el resto con simples restas y divisiones.
