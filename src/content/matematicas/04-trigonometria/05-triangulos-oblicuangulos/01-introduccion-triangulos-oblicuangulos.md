# **Introducción a los Triángulos Oblicuángulos**

Hasta ahora, la trigonometría ha sido fácil porque siempre había un ángulo de $90°$ (triángulo rectángulo) que nos permitía usar Pitágoras y SOH-CAH-TOA. Pero el mundo real no es perfecto. ¿Qué pasa cuando el triángulo está "chueco" o inclinado? Ahí es donde entran los **triángulos oblicuángulos**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es exactamente un triángulo oblicuángulo (y qué NO lo es).
- La notación estándar para lados y ángulos ($A$ opuesto a $a$).
- Los 4 casos de resolución (ALA, LAL, LLA, LLL).
- Por qué Pitágoras ya no funciona aquí (y qué usaremos en su lugar).

---

## 📐 ¿Qué es un Triángulo Oblicuángulo?

Simplemente, es cualquier triángulo que **NO tiene un ángulo recto ($90°$)**.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Tipos de triángulos oblicuángulos</strong>
  </div>

![Tipos de triángulos oblicuángulos](/images/trigonometria/triangulos-oblicuangulos/tipos-triangulos.svg)

</div>

Se dividen en dos tipos:
1.  **Acutángulos:** Los tres ángulos son menores de $90°$. (Todos agudos).
2.  **Obtusángulos:** Uno de los ángulos es mayor de $90°$. (Un obtuso).

> **Recuerda:** La suma de los ángulos internos SIEMPRE es $180°$, sin importar el tipo.
> $$ A + B + C = 180° $$

---

## 🏷️ Notación Estándar

Para no perdernos, usamos una convención universal:
*   **Ángulos:** Letras mayúsculas ($A, B, C$).
*   **Lados:** Letras minúsculas ($a, b, c$).

**La Regla de Oro:** El lado $a$ siempre está **frente** al ángulo $A$. El lado $b$ frente al ángulo $B$, y el $c$ frente al $C$.

---

## 🛠️ Las Nuevas Herramientas

Como no hay ángulo recto, **SOH-CAH-TOA NO FUNCIONA**.
Tampoco funciona $a^2 + b^2 = c^2$.

Necesitamos armas más poderosas:
1.  **Ley de Senos:** Para cuando conoces una "pareja" completa (lado y ángulo opuesto).
2.  **Ley de Cosenos:** Para cuando conoces los tres lados o dos lados y el ángulo del medio.

---

## 🧩 Los 4 Casos de Resolución

Para resolver un triángulo (encontrar todos sus lados y ángulos), necesitas conocer al menos **3 datos** (y uno de ellos debe ser un lado).

| Caso | Significado | Herramienta Sugerida |
| :--- | :--- | :--- |
| **ALA** (AAL) | Ángulo-Lado-Ángulo | Ley de Senos |
| **LAL** | Lado-Ángulo-Lado | Ley de Cosenos |
| **LLL** | Lado-Lado-Lado | Ley de Cosenos |
| **LLA** | Lado-Lado-Ángulo | Ley de Senos (¡Cuidado! Caso Ambiguo) |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si un triángulo tiene ángulos de $40°$ y $60°$, ¿cuánto mide el tercer ángulo?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La suma es $180°$.
$180° - (40° + 60°) = 180° - 100° = 80°$.

**Respuesta:** $\boxed{80°}$
</details>

---

### Ejercicio 2
¿Es posible resolver un triángulo si solo te dan los tres ángulos (AAA)?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No. Podría ser un triángulo pequeño o uno gigante (semejantes). Necesitas al menos un lado para fijar el tamaño.

**Respuesta:** **No**
</details>

---

### Ejercicio 3
Clasifica un triángulo con lados 3, 4, 5. ¿Es oblicuángulo?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$3^2 + 4^2 = 9 + 16 = 25 = 5^2$.
Cumple Pitágoras, así que es Rectángulo.
Por definición, **NO** es oblicuángulo.

**Respuesta:** **No, es Rectángulo**
</details>

---

### Ejercicio 4
En un triángulo $ABC$, el lado opuesto al ángulo $B$ se llama...

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Según la notación estándar.

**Respuesta:** $\boxed{b}$
</details>

---

### Ejercicio 5
¿Qué herramienta usarías para el caso LLL (conoces los 3 lados)?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sin ángulos, la Ley de Senos no arranca. Necesitas Ley de Cosenos.

**Respuesta:** **Ley de Cosenos**
</details>

---

### Ejercicio 6
Un triángulo tiene ángulos de $30°$ y $20°$. ¿Es acutángulo u obtusángulo?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Tercer ángulo: $180 - 50 = 130°$.
Como $130° > 90°$, tiene un ángulo obtuso.

**Respuesta:** **Obtusángulo**
</details>

---

### Ejercicio 7
Si usas SOH-CAH-TOA en un triángulo oblicuángulo, ¿qué sucede?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Obtendrás resultados incorrectos, porque las definiciones de opuesto/adyacente/hipotenusa dependen de un ángulo recto que no existe.

**Respuesta:** **Da error / Es incorrecto**
</details>

---

### Ejercicio 8
¿Cuál es la suma de los ángulos exteriores de cualquier triángulo?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Propiedad geométrica universal para polígonos convexos.

**Respuesta:** $\boxed{360°}$
</details>

---

### Ejercicio 9
Identifica el caso: Conoces Lado $a$, Lado $b$ y Ángulo $C$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Tienes dos lados y el ángulo $C$ (que está entre $a$ y $b$).
Es Lado-Ángulo-Lado.

**Respuesta:** **LAL**
</details>

---

### Ejercicio 10
¿Por qué el caso LLA se llama "Ambiguo"?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Porque con esos datos se pueden formar 0, 1 o 2 triángulos diferentes posibles.

**Respuesta:** **Puede tener múltiples soluciones**
</details>

---

## 🔑 Resumen

| Concepto | Descripción |
| :--- | :--- |
| **Oblicuángulo** | Sin ángulo de 90°. |
| **Ley de Senos** | Para parejas (Lado/Ángulo opuesto). |
| **Ley de Cosenos** | El general de Pitágoras ($c^2 = a^2 + b^2 - 2ab\cos C$). |
| **Objetivo** | Hallar los 3 lados y 3 ángulos. |

> **Conclusión:** Bienvenido al mundo real de la geometría. Aquí no hay ángulos rectos fáciles, pero con la Ley de Senos y Cosenos, podrás medir cualquier triángulo, desde la altura de una montaña hasta la distancia a una estrella.
