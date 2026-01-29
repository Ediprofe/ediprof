# **Definición de la Hipérbola**

La hipérbola es la "rebelde" de las cónicas. Mientras elipse, círculo y parábola son curvas cerradas o de una sola pieza, la hipérbola tiene **dos ramas** infinitas que nunca se tocan. Es la curva de la navegación y de las sombras de las lámparas.

---

## 🎯 ¿Qué vas a aprender?

- La definición exacta como diferencia de distancias.
- Los elementos clave: Focos, Vértices y Centro.
- La diferencia crucial con la elipse ($c^2 = a^2 + b^2$).

---

## ⚔️ La Definición del Navegante

Imagina dos antenas de radio (Focos) emitiendo señales al mismo tiempo. Un barco recibe las señales con un pequeño retraso entre una y otra. Si el barco se mueve manteniendo ese retraso (diferencia de tiempo) constante, dibuja una **Hipérbola** en el mar.

Matemáticamente:
$$ | d(P, F_1) - d(P, F_2) | = 2a $$

La **diferencia** (en valor absoluto) de las distancias a los dos focos es siempre igual al eje transversal ($2a$).

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Elementos de la Hipérbola</strong>
  </div>
  <img src="/images/geometria/analitica/elementos-hiperbola.svg" alt="Elementos de la hipérbola" style="width: 100%; height: auto;" />
</div>

---

## 📐 El Triángulo Pitagórico ($c^2 = a^2 + b^2$)

En la hipérbola, el foco está **más lejos** del centro que el vértice. Por eso $c$ es la hipotenusa.
*   **$a$**: Eje Transversal (distancia del centro al vértice).
*   **$b$**: Eje Conjugado (distancia "imaginaria" perpendicular).
*   **$c$**: Distancia Focal (distancia del centro al foco).

**La Fórmula Maestra:**
$$ c^2 = a^2 + b^2 $$
*(Aquí sí se parece al Teorema de Pitágoras original, porque $c$ es el lado más largo).*

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Cálculo de Focos
Una hipérbola tiene eje transversal 8 ($2a=8$) y eje conjugado 6 ($2b=6$).
1.  **Hallar $a$:** $a = 4$.
2.  **Hallar $b$:** $b = 3$.
3.  **Hallar $c$:**
    $$ c = \sqrt{a^2 + b^2} = \sqrt{16 + 9} = \sqrt{25} = 5 $$
    Los focos están a 5 unidades del centro.

### Ejemplo 2: Excentricidad
Usando los datos anteriores ($a=4, c=5$).
$$ e = \frac{c}{a} = \frac{5}{4} = 1.25 $$
La excentricidad siempre es **mayor que 1** ($e > 1$). Si fuera 1, sería parábola. Si fuera menor a 1, elipse.

### Ejemplo 3: Verificar un Punto
Focos en $(\pm 5, 0)$, Vértices en $(\pm 3, 0)$. ¿El punto $(5, 16/3)$ pertenece? ($a=3, c=5$).
1.  Distancia a $F_1(-5,0)$: $\sqrt{(5+5)^2 + (16/3)^2} = \sqrt{100 + 256/9} = \sqrt{1156/9} = 34/3$.
2.  Distancia a $F_2(5,0)$: $\sqrt{(5-5)^2 + (16/3)^2} = 16/3$.
3.  Resta: $|34/3 - 16/3| = |18/3| = 6$.
4.  Eje Transversal: $2a = 2(3) = 6$.
    ¡Sí! La diferencia (6) es igual a $2a$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si $a=12$ y $c=13$, encuentra $b$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$b = \sqrt{c^2 - a^2} = \sqrt{169 - 144} = 5$.

**Respuesta:** $\boxed{5}$
</details>

---

### Ejercicio 2
Si $a=b=1$, halla $c$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$c = \sqrt{1^2 + 1^2} = \sqrt{2}$.

**Respuesta:** $\boxed{\sqrt{2}}$
</details>

---

### Ejercicio 3
Excentricidad si $a=3, c=6$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$e = 6/3 = 2$.

**Respuesta:** $\boxed{2}$
</details>

---

### Ejercicio 4
Eje Transversal si $a=8$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2a = 16$.

**Respuesta:** $\boxed{16}$
</details>

---

### Ejercicio 5
¿Puede ser $a > c$ en una hipérbola?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No, la diferencia de lados no puede ser mayor que el tercer lado. $c$ es la hipotenusa.

**Respuesta:** **No, c siempre es mayor**
</details>

---

### Ejercicio 6
Si $2a = 10$, ¿cuál es la constante de la definición?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La constante es el eje transversal.

**Respuesta:** $\boxed{10}$
</details>

---

### Ejercicio 7
Distancia entre focos si $c=10$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2c = 20$.

**Respuesta:** $\boxed{20}$
</details>

---

### Ejercicio 8
Si $b=4, c=5$, halla $a$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a = \sqrt{25 - 16} = 3$.

**Respuesta:** $\boxed{3}$
</details>

---

### Ejercicio 9
Lado Recto si $b=4, a=3$. (Fórmula $2b^2/a$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2(16)/3 = 32/3$.

**Respuesta:** $\boxed{10.66}$
</details>

---

### Ejercicio 10
Si $e=1$, ¿es hipérbola?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No, es una parábola. Hipérbola exige $e > 1$.

**Respuesta:** **Es una Parábola**
</details>

---

## 🔑 Resumen

| Letra | Significado | Relación |
| :--- | :--- | :--- |
| **$c$** | Distancia Focal (Hipotenusa) | $c^2 = a^2 + b^2$ |
| **$a$** | Eje Transversal (Vértice) | |
| **$b$** | Eje Conjugado (Auxiliar) | |

> **Conclusión:** En la elipse, $a$ era el jefe (hipotenusa). En la hipérbola, $c$ toma el mando y es el lado más grande (hipotenusa). ¡No confundas las fórmulas!
