---
title: "Teorema de Tales"
---

# **Teorema de Tales**

Hace más de 2500 años, un faraón egipcio desafió al sabio griego Tales de Mileto a medir la altura de la Gran Pirámide de Guiza. Tales no se subió a la pirámide; simplemente clavó su bastón en la arena, esperó a que la sombra del bastón fuera igual a su altura, y dedujo que en ese instante la sombra de la pirámide también sería igual a su altura. Este principio de proporcionalidad es lo que hoy llamamos el **Teorema de Tales**.

---

## 🎯 ¿Qué vas a aprender?

- Comprender la relación de proporcionalidad cuando rectas paralelas cortan a transversales.
- Aplicar el Teorema de Tales en triángulos (recta paralela a un lado).
- Calcular alturas inalcanzables usando sombras y proporciones.
- Determinar si dos rectas son paralelas usando el recíproco del teorema.

---

## 📐 El Teorema General

Si tres o más rectas paralelas son cortadas por dos transversales (rectas secantes), los segmentos que se forman en una transversal son **proporcionales** a los segmentos correspondientes en la otra.

Si las rectas $L_1, L_2, L_3$ son paralelas:

$$
\frac{A}{B} = \frac{A'}{B'}
$$

Donde $A$ y $B$ son segmentos de la primera línea, y $A'$ y $B'$ son sus correspondientes en la segunda.

![Teorema General de Tales](/images/content/matematicas/geometria/tales/thales_general.svg)

---

## 📐 Teorema de Tales en Triángulos

Este es el caso más útil en la práctica.

Si trazamos una línea paralela a cualquiera de los lados de un triángulo, se forma un nuevo triángulo que es **semejante** al original.

Si la recta $DE$ es paralela a la base $BC$:

$$
\frac{AD}{AB} = \frac{AE}{AC} = \frac{DE}{BC}
$$

También se cumple la proporción de los segmentos cortados:

$$
\frac{AD}{DB} = \frac{AE}{EC}
$$

> ⚠️ **Error Común:** ¡Cuidado con las bases!
> La proporción $\frac{\text{Arriba}}{\text{Abajo}}$ **NO** es igual a $\frac{\text{Base Pequeña}}{\text{Base Grande}}$.
> Si necesitas calcular una base ($DE$ o $BC$), **siempre** debes usar los lados completos del triángulo (Triángulo Pequeño vs Triángulo Grande).


### Ejemplo de Advertencia: ¡Cuidado con la Base!

Este es el error más frecuente en exámenes. Calcula $x$ (la base del triángulo pequeño).

![Error Común Base](/images/content/matematicas/geometria/tales/thales_base_trap.svg)

**Datos:**
- Lado izquierdo: $AD=2$, $DB=3$.
- Bases: $DE=4$, $BC=x$.

**❌ Razonamiento Incorrecto (ERROR):**
Decir que "pedacito es a pedacito como base es a base":
$$
\frac{2}{3} = \frac{4}{x} \implies 2x = 12 \implies x = 6 \quad (\text{FALSO})
$$

**✅ Razonamiento Correcto:**
Para relacionar las BASES, usamos los LADOS COMPLETOS (Triángulo Pequeño vs Grande).
- Lado pequeño del triángulo: $2$
- Lado grande del triángulo: $2 + 3 = 5$

$$
\frac{\text{Lado Pequeño}}{\text{Lado Grande}} = \frac{\text{Base Pequeña}}{\text{Base Grande}}
$$

$$
\frac{2}{5} = \frac{4}{x}
$$

$$
2x = 5 \cdot 4
$$

$$
2x = 20
$$

**Resultado:**

$$
\boxed{x = 10}
$$

![Tales en Triángulo](/images/content/matematicas/geometria/tales/thales_triangle_concept.svg)


---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Rectas Paralelas

Tres estantes horizontales son cortados por dos soportes inclinados. En el soporte izquierdo, la distancia entre el primer y segundo estante es 50 cm, y entre el segundo y tercero es 80 cm. En el soporte derecho, la distancia superior es 60 cm. ¿Cuánto mide la distancia inferior ($x$)?

![estantes-y-teorema-de-thales](https://cdn.ediprofe.com/img/matematicas/3kr8-estantes-y-teorema-de-thales.webp)

![Ejemplo de Estantes](/images/content/matematicas/geometria/tales/thales_shelves.svg)


**Datos:**
Izquierda: 50 y 80.
Derecha: 60 y $x$.

**Razonamiento:**
Por el Teorema de Tales, los segmentos son proporcionales.

$$
\frac{50}{80} = \frac{60}{x}
$$

Despejamos $x$:

$$
x = \frac{60 \cdot 80}{50}
$$

$$
x = \frac{4800}{50}
$$

**Resultado:**
$$
\boxed{x = 96 \text{ cm}}
$$

---

### Ejemplo 2: En un Triángulo

En el triángulo $ABC$, cortamos con una recta paralela a la base $BC$.
El segmento de arriba $AD = 4$ cm.
El segmento de abajo $DB = 6$ cm.
En el otro lado, el segmento de arriba $AE = 8$ cm.
¿Cuánto mide el segmento de abajo $EC$?

![Ejemplo Numérico Triángulo](/images/content/matematicas/geometria/tales/thales_triangle_ex2.svg)


**Razonamiento:**
Establecemos la proporción entre los trozos de los lados.

$$
\frac{AD}{DB} = \frac{AE}{EC}
$$

$$
\frac{4}{6} = \frac{8}{EC}
$$

Despejamos $EC$:

$$
EC = \frac{8 \cdot 6}{4}
$$

$$
EC = \frac{48}{4}
$$

**Resultado:**
$$
\boxed{12 \text{ cm}}
$$

---

### Ejemplo 3: Midiendo la Pirámide (Sombras)

Supón que el bastón de Tales mide 1.5 m y proyecta una sombra de 2 m. Al mismo tiempo, la pirámide proyecta una sombra de 180 m (desde el centro de su base). ¿Cuál es la altura ($H$) de la pirámide?

![Ejemplo Sombras](/images/content/matematicas/geometria/tales/thales_shadows.svg)


**Razonamiento:**
Los rayos del sol son paralelos, creando triángulos semejantes entre el objeto y su sombra.

$$
\frac{\text{Altura Objeto}}{\text{Sombra Objeto}} = \frac{\text{Altura Bastón}}{\text{Sombra Bastón}}
$$

$$
\frac{H}{180} = \frac{1.5}{2}
$$

$$
H = \frac{1.5 \cdot 180}{2}
$$

$$
H = \frac{270}{2}
$$

**Resultado:**
$$
\boxed{135 \text{ m}}
$$

---


### Ejemplo 4: El Teorema Recíproco (¿Son Paralelas?)

En un triángulo, tenemos los segmentos $AD=3$, $DB=6$, $AE=4$ y $EC=8$. ¿Es la línea $DE$ paralela a la base $BC$?

![¿Son Paralelas?](/images/content/matematicas/geometria/tales/thales_reciprocal.svg)

**Datos:**
- Lado Izquierdo: $\frac{3}{6}$
- Lado Derecho: $\frac{4}{8}$

**Razonamiento:**
Calculamos las razones de cada lado por separado:

$$
\frac{AD}{DB} = \frac{3}{6} = 0.5
$$

$$
\frac{AE}{EC} = \frac{4}{8} = 0.5
$$

Como las razones son iguales, el Teorema Recíproco asegura que la línea es paralela.

**Resultado:**

$$
\boxed{\text{Sí, DE } \parallel \text{ BC}}
$$

---




## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $x$ sabiendo que las rectas horizontales son paralelas.
Lado Izquierdo: segmentos de 3 y 4.
Lado Derecho: segmentos de $x$ y 8.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
\frac{3}{4} = \frac{x}{8}
$$

$$
x = \frac{3 \cdot 8}{4}
$$

**Resultado:**
$$
\boxed{x = 6}
$$

</details>

### Ejercicio 2
En un triángulo, una paralela a la base divide un lado en segmentos de 2 cm y 5 cm. Si el otro lado mide 14 cm en total, ¿cuánto miden sus segmentos?

<details>
<summary>Ver solución</summary>

**Datos:**
Lado 1: 2 y 5 (Total 7).
Lado 2: Total 14.
Razón de escala: $\frac{14}{7} = 2$.

**Razonamiento:**
Los segmentos del segundo lado conservan la proporción pero multiplicados por la escala.

$$
2 \cdot 2 = 4
$$

$$
5 \cdot 2 = 10
$$

**Resultado:**
$$
\boxed{4 \text{ cm y } 10 \text{ cm}}
$$

</details>

### Ejercicio 3
Un edificio proyecta una sombra de 15 m. Un poste vertical de 4 m proyecta una sombra de 3 m a la misma hora. Calcula la altura del edificio.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
\frac{H}{15} = \frac{4}{3}
$$

$$
H = \frac{4 \cdot 15}{3}
$$

**Resultado:**
$$
\boxed{20 \text{ m}}
$$

</details>

### Ejercicio 4
Calcula el valor de $x$ si $\frac{x}{4} = \frac{15}{10}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
x = \frac{15 \cdot 4}{10}
$$

$$
x = \frac{60}{10}
$$

**Resultado:**
$$
\boxed{x = 6}
$$

</details>

### Ejercicio 5
Si $AD=3$, $DB=x$, $AE=5$, $EC=10$. Hallar $x$ asumiendo $DE \parallel BC$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Propiedad de segmentos proporcionales:

$$
\frac{3}{x} = \frac{5}{10}
$$

$$
\frac{3}{x} = \frac{1}{2}
$$

$$
x = 3 \cdot 2
$$

**Resultado:**
$$
\boxed{x = 6}
$$

</details>

### Ejercicio 6
En un triángulo con base 12, trazamos una paralela media (uniendo los puntos medios de los lados). ¿Cuánto mide este segmento paralelo?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si une los puntos medios, la razón de semejanza entre el triángulo pequeño y el grande es $\frac{1}{2}$.
La base del pequeño será la mitad de la base del grande.

$$
\text{Base}' = \frac{12}{2}
$$

**Resultado:**
$$
\boxed{6}
$$

</details>

### Ejercicio 7
¿Para qué sirve el Teorema de Tales en la vida real si no eres matemático?

<details>
<summary>Ver solución</summary>

**Respuesta:**
Permite medir distancias inaccesibles, como la altura de un árbol, un edificio o el ancho de un río, usando solo un objeto pequeño de referencia (como tu propia altura) y proporciones simples.

**Resultado:**
$$
\boxed{\text{Estimación de distancias remotas}}
$$

</details>

### Ejercicio 8
Tenemos dos rectas cortadas por transversales.
Segmentos: $3, 6, 9$ en la primera.
En la segunda el primer segmento mide 4.
¿Cuánto mide el segmento total de la segunda recta?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Razón entre lados correspondientes del primer tramo: $\frac{4}{3}$.
El total de la primera recta es $3+6+9 = 18$.
El total de la segunda recta será $18 \cdot \frac{4}{3}$.

$$
Total = \frac{72}{3}
$$

**Resultado:**
$$
\boxed{24}
$$

</details>

### Ejercicio 9 (Recíproco)
En un triángulo, $AD=2, DB=4, AE=3, EC=6$. ¿Es la línea $DE$ paralela a la base?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Comprobamos si las proporciones son iguales.

$$
\frac{2}{4} = 0.5
$$

$$
\frac{3}{6} = 0.5
$$

Son iguales.

**Resultado:**
$$
\boxed{\text{Sí, es paralela}}
$$

</details>

### Ejercicio 10
Un farol de 5 m de altura proyecta la sombra de una persona. Si la persona mide 1.80 m y está a 3 metros de la base del farol, ¿cuánto mide su sombra?

<details>
<summary>Ver solución</summary>

**Datos:**
Triángulos semejantes formados por la luz.
Altura grande: 5. Altura pequeña: 1.8.
Base grande: $3 + x$ (distancia farol-persona + sombra). Base pequeña: $x$ (sombra).

**Razonamiento:**
$$
\frac{5}{1.8} = \frac{3+x}{x}
$$

$$
5x = 1.8(3+x)
$$

$$
5x = 5.4 + 1.8x
$$

$$
3.2x = 5.4
$$

$$
x = \frac{5.4}{3.2}
$$

**Resultado:**
$$
\boxed{1.6875 \text{ m}}
$$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula Clave | Aplicación |
|----------|---------------|------------|
| **Teorema General** | $\frac{A}{B} = \frac{A'}{B'}$ | Paralelas cortando rectas cualesquiera. |
| **En Triángulos** | $\frac{Pequeño}{Grande} = k$ | Triángulos encajados (semejanza). |
| **Recíproco** | Igualdad de razón $\implies$ Paralelismo | Verificar si dos líneas son paralelas. |

> "Lo que pasa en un lado, pasa proporcionalmente en el otro". Esa es la esencia de Tales.

![Resumen Visual Tales](/images/content/matematicas/geometria/tales/thales_summary.svg)

