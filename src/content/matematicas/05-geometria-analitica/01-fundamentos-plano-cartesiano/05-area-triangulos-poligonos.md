# **Área de Triángulos y Polígonos**

¿Cómo calculas el área de un terreno irregular que tiene forma de pentágono? ¿Vas a dividirlo en triangulitos y medir cada altura? ¡Qué pereza! La Geometría Analítica tiene un truco sucio y maravilloso llamado la **Fórmula de la Agujeta** (Shoelace Formula) que resuelve esto en segundos usando solo coordenadas.

---

## 🎯 ¿Qué vas a aprender?

- Cómo calcular el área de cualquier triángulo dadas sus 3 coordenadas.
- El algoritmo del "Cordón de Zapato" para polígonos de $n$ lados.
- Por qué el área puede darte negativa (y qué significa).
- Cómo saber si tres puntos están alineados (colineales) usando áreas.

---

## 👟 La Fórmula de la Agujeta

Imagina que escribes las coordenadas de los vértices en una lista vertical, y repites el primer punto al final. Luego multiplicas en cruz.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Algoritmo Shoelace</strong>
  </div>
  <img src="/images/geometria/analitica/area-triangulo.svg" alt="Área de un triángulo usando coordenadas" style="width: 100%; height: auto;" />
</div>

$$
\text{Área} = \frac{1}{2} | \sum \text{(Flechas Abajo)} - \sum \text{(Flechas Arriba)} |
$$

Para un triángulo con puntos $(x_1, y_1), (x_2, y_2), (x_3, y_3)$:

$$
A = \frac{1}{2} | x_1 y_2 + x_2 y_3 + x_3 y_1 - (y_1 x_2 + y_2 x_3 + y_3 x_1) |
$$

> **Nota:** ¡Siempre toma el valor absoluto al final! El área no puede ser negativa.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Área de un Triángulo
Calcula el área del triángulo $A(1, 1)$, $B(4, 2)$, $C(2, 5)$.

**Paso 1: Armar la matriz (repitiendo el 1º punto al final)**
$(1, 1)$
$(4, 2)$
$(2, 5)$
$(1, 1)$ <-- Repetición

**Paso 2: Suma de bajada (Azul)**
$1 \cdot 2 = 2$
$4 \cdot 5 = 20$
$2 \cdot 1 = 2$
**Suma Bajada = 24**

**Paso 3: Suma de subida (Rojo)**
$1 \cdot 4 = 4$
$2 \cdot 2 = 4$
$5 \cdot 1 = 5$
**Suma Subida = 13**

**Paso 4: Fórmula**
$$ A = \frac{1}{2} | 24 - 13 | = \frac{1}{2} (11) = 5.5 $$

**Resultado:** $\boxed{5.5 \text{ u}^2}$.

### Ejemplo 2: Puntos Colineales
Verifica si $A(1, 1)$, $B(2, 2)$ y $C(3, 3)$ forman un triángulo.
Si los puntos están en línea recta, "aplastan" al triángulo y su área será 0.

**Cálculo:**
Bajada: $1(2) + 2(3) + 3(1) = 2 + 6 + 3 = 11$.
Subida: $1(2) + 2(3) + 3(1) = 2 + 6 + 3 = 11$.
Área $= \frac{1}{2} |11 - 11| = 0$.

**Resultado:** Son **colineales** (forman una línea, no un triángulo).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el área de $A(0, 0)$, $B(4, 0)$, $C(0, 3)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Bajada: $0+12+0 = 12$. Subida: $0+0+0 = 0$.
Área: $12/2 = 6$.
(Es un triángulo rectángulo base 4, altura 3).

**Respuesta:** $\boxed{6}$
</details>

---

### Ejercicio 2
Calcula el área de $A(2, 3)$, $B(5, 7)$, $C(-3, 4)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Matriz: $(2,3) \to (5,7) \to (-3,4) \to (2,3)$.
Bajada: $14 + 20 - 9 = 25$.
Subida: $15 - 21 + 8 = 2$.
Área: $|25-2|/2 = 11.5$.

**Respuesta:** $\boxed{11.5}$
</details>

---

### Ejercicio 3
Calcula el área del cuadrado con vértices $(0,0), (2,0), (2,2), (0,2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Lado 2. Área $2 \times 2 = 4$.
Usa agujeta para practicar.

**Respuesta:** $\boxed{4}$
</details>

---

### Ejercicio 4
Si el área es cero, ¿qué significa geométricamente?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Que no hay superficie. Los puntos están alineados.

**Respuesta:** **Son Colineales**
</details>

---

### Ejercicio 5
Calcula el área de $A(1, 1)$, $B(2, 2)$, $C(3, 1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Bajada: $2+2+3=7$.
Subida: $2+6+1=9$.
$|7-9|/2 = 2/2 = 1$.

**Respuesta:** $\boxed{1}$
</details>

---

### Ejercicio 6
¿Importa el orden en que pones los puntos?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Debes ponerlos en orden consecutivo (siguiendo el perímetro). Si saltas vértices en un polígono (cruzado), dará mal. Para triángulos no importa (solo cambiará el signo).

**Respuesta:** **Sí, deben ser ordenados**
</details>

---

### Ejercicio 7
Halla $k$ para que los puntos $(1, 1), (2, k), (3, 3)$ estén alineados.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Área debe ser 0.
Bajada: $k + 6 + 3$. Subida: $2 + 3k + 3$.
$k+9 = 3k+5 \Rightarrow 2k=4 \Rightarrow k=2$.

**Respuesta:** $\boxed{2}$
</details>

---

### Ejercicio 8
Calcula el área de un triángulo con vértices en el origen, $(5, 0)$ y $(0, 5)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Bajada: $0+25+0=25$. Subida: $0$.
$25/2 = 12.5$.

**Respuesta:** $\boxed{12.5}$
</details>

---

### Ejercicio 9
¿Qué pasa si olvidas repetir el primer punto al final de la lista?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Te falta cerrar el polígono. El cálculo será incorrecto (como si fuera una línea abierta).

**Respuesta:** **El cálculo falla**
</details>

---

### Ejercicio 10
Calcula el área de $P(-1, -1), Q(2, -2), R(0, 3)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Bajada: $2 + 6 + 0 = 8$.
Subida: $-2 + 0 - 3 = -5$.
$|8 - (-5)|/2 = 13/2 = 6.5$.

**Respuesta:** $\boxed{6.5}$
</details>

---

## 🔑 Resumen

| Método | Fórmula Mental |
| :--- | :--- |
| **Bajada (Azul)** | Multiplica $x \cdot y_{\text{siguiente}}$ y suma todo. |
| **Subida (Rojo)** | Multiplica $y \cdot x_{\text{siguiente}}$ y suma todo. |
| **Final** | $\frac{1}{2} | \text{Azul} - \text{Rojo} |$. |

> **Conclusión:** Esta fórmula convierte un problema de geometría difícil en una simple lista de multiplicaciones y restas. ¡Es tan poderosa que las computadoras la usan para dibujar mapas!
