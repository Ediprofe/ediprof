# Aplicaciones

La resolución de triángulos oblicuángulos tiene muchas aplicaciones prácticas en topografía, navegación, astronomía e ingeniería.

---

## 📖 Tipos de problemas

1. **Distancias inaccesibles**: medir distancias que no podemos recorrer directamente
2. **Navegación**: calcular rumbos y posiciones
3. **Topografía**: medición de terrenos
4. **Fuerzas**: resolver componentes de vectores

---

## 📖 Problema 1: Ancho de un río

Desde un punto $A$ en la orilla de un río, se observan dos puntos $B$ y $C$ en la otra orilla. El ángulo $\angle BAC = 40°$. Desde $A$, caminando 100 m hasta $D$ paralelo a $BC$, se mide que $\angle BDA = 70°$ y $\angle BDC = 50°$.

### Solución

En el triángulo $ABD$:
- $\angle ABD = 180° - 40° - 70° = 70°$
- $AD = 100$ m

Por Ley de Senos:

$$
\frac{AB}{\sin 70°} = \frac{100}{\sin 70°}
$$

$AB = 100$ m (triángulo isósceles)

El ancho del río se calcula con la altura del triángulo.

---

## 📖 Problema 2: Dos barcos

Dos barcos parten de un puerto. El primero navega 80 km con rumbo N35°E. El segundo navega 60 km con rumbo S55°E. ¿A qué distancia están entre sí?

### Solución

El ángulo entre las trayectorias es $35° + 55° = 90°$.

Por Ley de Cosenos (o Pitágoras, ya que es 90°):

$$
d^2 = 80^2 + 60^2 = 6400 + 3600 = 10000
$$

$$
d = 100 \text{ km}
$$

---

## 📖 Problema 3: Torre inclinada

Desde un punto a 50 m de la base de una torre inclinada, el ángulo de elevación a la cima es 35°. Desde el lado opuesto, a 80 m de la base, el ángulo es 25°. ¿Cuál es la altura de la torre?

### Solución

En el triángulo formado:
- Un lado de 50 m, ángulo opuesto a la torre
- Otro lado de 80 m, ángulo opuesto
- Los ángulos en la base son 35° y 25°
- El ángulo en la cima es $180° - 35° - 25° = 120°$

Por Ley de Senos, podemos encontrar la altura.

---

## 📖 Problema 4: Área de un triángulo

El **área de un triángulo** se puede calcular con:

$$
\text{Área} = \frac{1}{2}ab\sin C
$$

### Ejemplo

Calculemos el área de un triángulo con $a = 8$, $b = 10$ y $C = 60°$:

$$
\text{Área} = \frac{1}{2}(8)(10)\sin 60° = 40 \times \frac{\sqrt{3}}{2} = 20\sqrt{3} \approx 34.6 \text{ u}^2
$$

---

## 📖 Fórmula de Herón

Para un triángulo con lados $a$, $b$, $c$:

$$
s = \frac{a + b + c}{2} \quad \text{(semiperímetro)}
$$

$$
\text{Área} = \sqrt{s(s-a)(s-b)(s-c)}
$$

### Ejemplo

Triángulo con lados 5, 6, 7:

$s = \frac{5 + 6 + 7}{2} = 9$

$$
\text{Área} = \sqrt{9 \times 4 \times 3 \times 2} = \sqrt{216} = 6\sqrt{6} \approx 14.7 \text{ u}^2
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Distancia

Dos observadores separados por 500 m ven un globo aerostático. Desde un observador, el ángulo de elevación es 40°. Desde el otro, es 35°. ¿A qué altura está el globo?

<details>
<summary><strong>Ver respuesta</strong></summary>

En el triángulo formado, el ángulo en el globo es $180° - 40° - 35° = 105°$.

Por Ley de Senos, encontramos la distancia del primer observador al globo:

$$
\frac{d}{\sin 35°} = \frac{500}{\sin 105°}
$$

$d = \frac{500 \times 0.574}{0.966} \approx 297$ m

La altura: $h = 297 \times \sin 40° \approx 191$ m

</details>

---

### Ejercicio 2: Área

Calcula el área de un triángulo con:
1. $a = 12$, $b = 15$, $C = 50°$
2. Lados 8, 9, 11

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\text{Área} = \frac{1}{2}(12)(15)\sin 50° = 90 \times 0.766 \approx 68.9$ u²

2. $s = 14$

   $\text{Área} = \sqrt{14 \times 6 \times 5 \times 3} = \sqrt{1260} \approx 35.5$ u²

</details>

---

### Ejercicio 3: Navegación

Un barco navega 40 km al norte, luego gira 60° a la derecha y navega 30 km más. ¿A qué distancia está del punto de partida?

<details>
<summary><strong>Ver respuesta</strong></summary>

El ángulo en el vértice es $180° - 60° = 120°$.

$$
d^2 = 40^2 + 30^2 - 2(40)(30)\cos 120°
$$

$$
d^2 = 1600 + 900 - 2400(-0.5) = 2500 + 1200 = 3700
$$

$d \approx 60.8$ km

</details>

---
