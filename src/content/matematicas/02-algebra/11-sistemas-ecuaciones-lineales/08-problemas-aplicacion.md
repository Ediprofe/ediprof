# **Problemas de Aplicación**

Las matemáticas no son solo números flotando en una pizarra; están en tu billetera, en tu velocidad al correr y en la mezcla de tu café. Los sistemas de ecuaciones son la herramienta perfecta para resolver acertijos donde tienes varias piezas de información conectadas.

---

## 🎯 ¿Qué vas a aprender?

- Cómo traducir palabras a ecuaciones matemáticas ("Lenguaje Algebraico").
- Resolver problemas de mezclas y costos.
- Calcular velocidades con viento a favor o en contra.
- Descifrar edades según pistas del pasado y el presente.

---

## 🧠 La Estrategia de Traducción

Para no perderte en el texto, sigue este protocolo:

1.  **Bautizar:** Asigna una letra a cada cosa que no sepas (ej: $x=$ precio de la manzana, $y=$ precio de la pera).
2.  **Traducir:** Convierte cada frase en una ecuación.
    - "Suman 10" $\rightarrow x + y = 10$
    - "El doble de uno es el otro" $\rightarrow 2x = y$
3.  **Resolver:** Usa cualquier método (sustitución, reducción, igualación) para hallar $x$ e $y$.
4.  **Verificar:** ¿Tiene sentido que la edad sea negativa o que el coche vaya a 10000 km/h? Usa el sentido común.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El Acertijo de los Números
La suma de dos números es 25 y su diferencia es 7. ¿Cuáles son?

**Paso 1: Bautizar**
- $x$: Número mayor
- $y$: Número menor

**Paso 2: Traducir**
1.  "Suma es 25": $x + y = 25$
2.  "Diferencia es 7": $x - y = 7$

**Paso 3: Resolver (Reducción)**
Sumamos las ecuaciones:
$$
2x = 32 \implies x = 16
$$
Hallamos $y$:
$$
16 + y = 25 \implies y = 9
$$

**Resultado:**
$$
\boxed{\text{Los números son 16 y 9}}
$$

---

### Ejemplo 2: Cine y Palomitas
Ayer, 2 entradas y 1 palomita costaron 200 pesos. Hoy, 1 entrada y 3 palomitas costaron 250 pesos. ¿Cuánto cuesta cada cosa?

**Ecuaciones:**
$$
\left\{
\begin{array}{ll}
2e + p = 200 \\
e + 3p = 250
\end{array}
\right.
$$

**Resolver (Sustitución):**
De la 2ª: $e = 250 - 3p$.
En la 1ª:
$$
2(250 - 3p) + p = 200
$$
$$
500 - 6p + p = 200
$$
$$
-5p = -300 \implies p = 60
$$
Hallamos $e$:
$$
e = 250 - 3(60) = 250 - 180 = 70
$$

**Resultado:**
$$
\boxed{\text{Entrada: } 70 \text{ pesos, Palomita: } 60 \text{ pesos}}
$$

---

### Ejemplo 3: Edades en el Tiempo
Juan tiene el doble de la edad de Ana. Hace 10 años, la suma de sus edades era igual a la edad actual de Juan.

**Variables:**
- $J$: Edad actual de Juan
- $A$: Edad actual de Ana

**Traducción:**
1.  "Juan tiene el doble de Ana": $J = 2A$.
2.  "Hace 10 años": $(J-10)$ y $(A-10)$.
3.  "La suma era igual a Juan hoy": $(J-10) + (A-10) = J$.

**Resolver:**
$$
J + A - 20 = J
$$
Cancelamos $J$ de ambos lados:
$$
A - 20 = 0 \implies A = 20
$$
Como $J = 2A$:
$$
J = 2(20) = 40
$$

**Resultado:**
$$
\boxed{\text{Juan: 40 años, Ana: 20 años}}
$$

---

### Ejemplo 4: El Barista Matemático
Tienes café de 80 pesos/kg y café premium de 120 pesos/kg. Quieres hacer una mezcla de 20 kg que cueste 90 pesos/kg. ¿Cuánto pones de cada uno?

**Variables:**
- $x$: kg de café barato
- $y$: kg de café caro

**Sistema:**
1.  **Cantidad:** $x + y = 20$ (Total de kilos)
2.  **Valor:** $80x + 120y = 90(20)$ (Valor total de la mezcla)

Simplificamos la 2ª ($80x + 120y = 1800$). Dividimos por 40:
$$
2x + 3y = 45
$$
Sistema:
$$
\left\{
\begin{array}{ll}
x + y = 20 \\
2x + 3y = 45
\end{array}
\right.
$$

**Resolver:**
Multiplicamos la 1ª por -2:
$$
-2x - 2y = -40
$$
Sumamos con la 2ª:
$$
y = 5
$$
Hallamos $x$:
$$
x + 5 = 20 \implies x = 15
$$

**Resultado:**
$$
\boxed{15 \text{ kg barato y } 5 \text{ kg caro}}
$$

---

### Ejemplo 5: Viento a Favor
Un avión vuela a 600 km/h con viento a favor, pero solo a 500 km/h cuando vuelve contra el viento. Halla la velocidad del avión ($a$) y la del viento ($v$).

**Sistema:**
$$
\left\{
\begin{array}{ll}
a + v = 600 & (\text{Ayuda}) \\
a - v = 500 & (\text{Frena})
\end{array}
\right.
$$

**Resolver (Reducción):**
Sumamos:
$$
2a = 1100 \implies a = 550
$$
Hallamos $v$:
$$
550 + v = 600 \implies v = 50
$$

**Resultado:**
$$
\boxed{\text{Avión: } 550 \text{ km/h, Viento: } 50 \text{ km/h}}
$$

---

### Ejemplo 6: Conteo de Dinero
En una alcancía hay 30 monedas, solo de 5 y 10 pesos. En total hay 200 pesos. ¿Cuántas hay de cada una?

**Variables:**
- $c$: monedas de cinco ($5$)
- $d$: monedas de diez ($10$)

**Sistema:**
1.  **Cantidad:** $c + d = 30$
2.  **Valor:** $5c + 10d = 200$

**Resolver:**
De la 1ª: $c = 30 - d$.
$$
5(30 - d) + 10d = 200
$$
$$
150 - 5d + 10d = 200
$$
$$
5d = 50 \implies d = 10
$$
Hallamos $c$:
$$
c = 30 - 10 = 20
$$

**Resultado:**
$$
\boxed{20 \text{ monedas de 5 y } 10 \text{ monedas de 10}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
En un corral hay gallinas y conejos. Hay 10 cabezas y 28 patas. ¿Cuántos animales hay de cada tipo?

<details>
<summary>Ver solución</summary>

$g+c=10$.
$2g+4c=28$.
Resolviendo: $g=6, c=4$.
**Resultado:** $\boxed{6 \text{ gallinas, } 4 \text{ conejos}}$

</details>

---

### Ejercicio 2
La suma de dos números es 100 y el mayor excede al menor en 12.

<details>
<summary>Ver solución</summary>

$x+y=100$.
$x-y=12$.
$2x = 112 \implies x=56$.
$y=44$.
**Resultado:** $\boxed{56 \text{ y } 44}$

</details>

---

### Ejercicio 3
Dos hamburguesas y un refresco cuestan 150 pesos. Una hamburguesa y dos refrescos cuestan 120 pesos. Precio de cada uno.

<details>
<summary>Ver solución</summary>

$2h+r=150$.
$h+2r=120$.
Multiplicar 2ª por -2 $\implies -2h-4r=-240$.
$-3r = -90 \implies r=30$.
$h=60$.
**Resultado:** $\boxed{\text{H: 60, R: 30}}$

</details>

---

### Ejercicio 4
Un padre tiene el triple de edad que su hijo. En 12 años solo tendrá el doble.

<details>
<summary>Ver solución</summary>

$P = 3H$.
$P+12 = 2(H+12)$.
$3H + 12 = 2H + 24 \implies H = 12$.
$P = 36$.
**Resultado:** $\boxed{\text{Padre 36, Hijo 12}}$

</details>

---

### Ejercicio 5
Un barco recorre 40 km ría abajo en 2 horas, y regresa (río arriba) en 4 horas. Velocidad del barco y corriente.

<details>
<summary>Ver solución</summary>

Velocidad abajo: $40/2 = 20$. Velocidad arriba: $40/4 = 10$.
$b+c=20$.
$b-c=10$.
$2b=30 \implies b=15$.
$c=5$.
**Resultado:** $\boxed{\text{Barco 15, Corriente 5}}$

</details>

---

### Ejercicio 6
Tienes 5000 pesos en billetes de 200 y 500. Si tienes 16 billetes en total, ¿cuántos de cada uno?

<details>
<summary>Ver solución</summary>

$x+y=16$.
$200x + 500y = 5000$.
Simplificando 2ª: $2x+5y=50$.
Multiplico 1ª por -2: $-2x-2y=-32$.
$3y=18 \implies y=6$.
$x=10$.
**Resultado:** $\boxed{10 \text{ de 200, } 6 \text{ de 500}}$

</details>

---

### Ejercicio 7
El perímetro de un rectángulo es 40 cm. La base es 4 cm más larga que la altura.

<details>
<summary>Ver solución</summary>

$2b + 2h = 40 \implies b+h=20$.
$b = h+4$.
$(h+4)+h=20 \implies 2h=16 \implies h=8$.
$b=12$.
**Resultado:** $\boxed{12 \times 8 \text{ cm}}$

</details>

---

### Ejercicio 8
Una solución salina al 10% se mezcla con una al 20% para obtener 10 litros al 14%.

<details>
<summary>Ver solución</summary>

$x+y=10$.
$0.1x + 0.2y = 0.14(10) = 1.4$.
$x + 2y = 14$.
Restando las ec: $y=4$.
$x=6$.
**Resultado:** $\boxed{6 \text{ litros al 10\%, } 4 \text{ litros al 20\%}}$

</details>

---

### Ejercicio 9
La diferencia de dos números es 10. Si al mayor le restas el doble del menor, obtienes -5.

<details>
<summary>Ver solución</summary>

$x-y=10 \implies x=y+10$.
$x-2y=-5$.
$(y+10)-2y=-5 \implies -y=-15 \implies y=15$.
$x=25$.
**Resultado:** $\boxed{25 \text{ y } 15}$

</details>

---

### Ejercicio 10
Dos ángulos son suplementarios (suman 180°). Uno es 30° mayor que el otro.

<details>
<summary>Ver solución</summary>

$x+y=180$.
$x = y+30$.
$2y+30=180 \implies 2y=150 \implies y=75$.
$x=105$.
**Resultado:** $\boxed{105^\circ \text{ y } 75^\circ}$

</details>

---

## 🔑 Resumen

| Tipo de Problema | Clave |
|:--- |:--- |
| **Mezclas** | Una ecuación es para la cantidad total (kg, litros), la otra para el valor/concentración. |
| **Movimiento** | A favor sumas velocidades ($v_{objeto} + v_{medio}$), en contra restas. |
| **Dígitos/Números** | Lee con cuidado "excede", "diferencia", "suma". |

> **Conclusión:** El mundo no te da ecuaciones listas, te da problemas. Tu superpoder matemático es convertirlos en $x$ e $y$ para encontrar las respuestas.
