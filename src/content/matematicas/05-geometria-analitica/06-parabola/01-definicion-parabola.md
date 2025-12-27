# **Definición de la Parábola**

Seguramente has visto antenas parabólicas o el vuelo de un balón de baloncesto. Esa curva perfecta y simétrica es una parábola. Matemáticamente, nace de una relación de distancias muy estricta, pero increíblemente útil en el mundo real.

---

## 🎯 ¿Qué vas a aprender?

- La definición exacta como lugar geométrico: Distancia Foco = Distancia Directriz.
- Los elementos clave: Foco, Directriz, Vértice, Eje y Lado Recto.
- Por qué el "foco" se llama así (propiedad reflectiva).

---

## 📖 El Club de la Equidistancia

Una parábola es como un diplomático que intenta complacer a dos bandos opuestos.
Sus puntos $P(x,y)$ siempre se mantienen a **la misma distancia** de:
1.  Un punto fijo llamado **Foco ($F$)**.
2.  Una recta fija llamada **Directriz ($\ell$)**.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Elementos de la Parábola</strong>
  </div>
  <img src="/images/geometria/analitica/elementos-parabola.svg" alt="Elementos de la parábola" style="width: 100%; height: auto;" />
</div>

$$
d(P, F) = d(P, \ell)
$$

---

## 📐 Elementos Fundamentales

| Elemento | Símbolo | Qué es en palabras sencillas |
| :--- | :--- | :--- |
| **Vértice** | $V$ | El punto donde la curva da la vuelta. Está justo a la mitad entre el Foco y la Directriz. |
| **Foco** | $F$ | El "corazón" de la parábola. Está adentro de la curva. |
| **Directriz** | $\ell$ | Una línea recta "espalda" de la parábola. La curva siempre le da la espalda. |
| **Parámetro** | $p$ | La distancia del Vértice al Foco. (Es la unidad de medida clave). |
| **Lado Recto** | $LR$ | El ancho de la parábola a la altura del foco. Mide exactamente $4p$. |
| **Eje Focal** | - | La línea que corta la parábola en dos mitades iguales (pasa por V y F). |

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Verificando la Definición
Tenemos un Foco en $(0, 2)$ y Directriz $y = -2$.
El Vértice debe estar en el punto medio: $(0, 0)$.
La distancia $p$ (Vértice a Foco) es 2.
El Lado Recto ($4p$) debe medir $4(2) = 8$.

### Ejemplo 2: Distancias Iguales
Considera la parábola $x^2 = 8y$.
Foco en $(0, 2)$. Directriz $y = -2$.
Tomemos un punto de la parábola, por ejemplo $(4, 2)$.
1.  **Distancia al Foco $(0,2)$:**
    $$ d = \sqrt{(4-0)^2 + (2-2)^2} = \sqrt{16} = 4 $$
2.  **Distancia a la Directriz ($y=-2$):**
    La altura del punto es 2. La directriz está en -2.
    $$ d = |2 - (-2)| = |4| = 4 $$
    ¡Son iguales! ($4=4$). El punto pertenece a la parábola.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si el Vértice está en el origen y el Foco es $(0, 3)$, ¿cuánto vale $p$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$p$ es la distancia $V \to F$.

**Respuesta:** $\boxed{3}$
</details>

---

### Ejercicio 2
Si $p=5$, ¿cuánto mide el Lado Recto?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$LR = 4p = 4(5)$.

**Respuesta:** $\boxed{20}$
</details>

---

### Ejercicio 3
Define "Directriz" con tus palabras.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es la recta fija exterior de la cual escapan los puntos.

**Respuesta:** **Recta fija equidistante a la parábola**
</details>

---

### Ejercicio 4
Si el Foco está en $(0, -4)$ y $V(0,0)$, ¿hacia dónde abre la parábola?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El foco "jala" a la curva. Si está abajo del vértice, abre abajo.

**Respuesta:** **Hacia abajo**
</details>

---

### Ejercicio 5
Calcula la distancia del Vértice a la Directriz si $p=2.5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es la misma que al foco, $p$.

**Respuesta:** $\boxed{2.5}$
</details>

---

### Ejercicio 6
¿El Foco puede estar sobre la Directriz?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No, la parábola colapsaría en una recta.

**Respuesta:** **No**
</details>

---

### Ejercicio 7
Si el Lado Recto mide 12, halla $p$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$4p = 12 \Rightarrow p = 3$.

**Respuesta:** $\boxed{3}$
</details>

---

### Ejercicio 8
¿Cuál es la excentricidad de una parábola?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Por definición es siempre 1. (Distancia Foco / Distancia Directriz = 1).

**Respuesta:** $\boxed{1}$
</details>

---

### Ejercicio 9
Si la directriz es vertical $x=-3$, ¿cómo es el eje de la parábola?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El eje es perpendicular a la directriz.

**Respuesta:** **Horizontal**
</details>

---

### Ejercicio 10
Distancia total desde el Foco a un extremo del Lado Recto.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El Lado Recto total es $4p$. La mitad (del foco al extremo) es $2p$.

**Respuesta:** $\boxed{2p}$
</details>

---

## 🔑 Resumen

| Elemento | Definición Clave | Fórmula Relacionada |
| :--- | :--- | :--- |
| **Definición** | Equidistancia | $d(P,F) = d(P, \ell)$ |
| **Parámetro $p$** | Unidad base | Distancia $V \to F$ |
| **Ancho** | Lado Recto | $4p$ |

> **Conclusión:** La parábola no es solo una curva bonita. Es una máquina geométrica perfecta que convierte líneas rectas (directriz) en un punto focal concentrado. Por eso tu antena satelital tiene esa forma.
