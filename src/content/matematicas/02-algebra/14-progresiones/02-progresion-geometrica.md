# **Progresiones Geométricas**

¿Alguna vez has escuchado sobre el "efecto bola de nieve" o cómo se hacen virales los videos? Eso es crecimiento geométrico. A diferencia de las escaleras (que suben paso a paso), aquí las cosas se multiplican. Empezamos despacio, y de repente... ¡BOOM! Números gigantes.

---

## 🎯 ¿Qué vas a aprender?

- Identificar patrones de multiplicación (llamados Razón Común).
- Calcular números enormes sin multiplicar uno por uno.
- La leyenda del ajedrez y los granos de arroz (Suma finita).
- Sumar infinitos números y obtener un resultado normal (Suma infinita).

---

## 🚀 El Patrón Explosivo

Una progresión geométrica (PG) es una secuencia donde cada término se obtiene **multiplicando** al anterior por un número fijo llamado **razón común** ($$r$$).

### Ejemplo Inductivo
Mira esta secuencia:

$$
3, 6, 12, 24, 48, \dots
$$

1.  
$$
3 \cdot 2 = 6
$$
2.  
$$
6 \cdot 2 = 12
$$
3.  
$$
12 \cdot 2 = 24
$$

¡La razón es $$r = 2$$! Cada paso es el doble del anterior.

---

## 🔍 La Fórmula General: Entendiendo el Exponente

Si queremos encontrar un término lejano (como el décimo), no es práctico multiplicar manualmente muchas veces. Necesitamos una regla que nos lleve directamente al resultado. 

Observemos cómo se construye la secuencia paso a paso:

- **Primer término ($$a_1$$):**
$$
a_1 = a_1 \cdot r^0
$$
- **Segundo término ($$a_2$$):** Es el primero multiplicado por la razón 1 vez.
$$
a_2 = a_1 \cdot r^1
$$
- **Tercer término ($$a_3$$):** Es el primero multiplicado por la razón 2 veces.
$$
a_3 = a_2 \cdot r = (a_1 \cdot r) \cdot r = a_1 \cdot r^2
$$
- **Cuarto término ($$a_4$$):** Multiplicamos por la razón 3 veces.
$$
a_4 = a_1 \cdot r^3
$$

**¿Por qué el exponente es $$n-1$$?**
Si te fijas, para llegar a cualquier posición, siempre aplicamos la multiplicación **una vez menos** que el número de la posición. Para el término 4, usamos el exponente 3. Por lo tanto, para la posición $$n$$, el exponente debe ser $$n-1$$.

$$
a_n = a_1 \cdot r^{n-1}
$$

### 📋 ¿Qué significa cada variable?

| Variable | Nombre | Significado |
| :--- | :--- | :--- |
| **$$a_n$$** | Término general | El valor de la posición que estamos buscando. |
| **$$a_1$$** | Primer término | El valor donde inicia nuestra secuencia. |
| **$$r$$** | Razón común | El número por el cual multiplicamos en cada paso. |
| **$$n$$** | Posición | El número de lugar que ocupa el término (1º, 2º, 100º...). |

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Encontrar un término
En la secuencia $$2, 6, 18, 54, \dots$$, halla el 7º término ($$a_7$$).

**Datos:**
- $$a_1 = 2$$
- $$r = 6/2 = 3$$
- $$n = 7$$

**Cálculo:**
$$
a_7 = 2 \cdot 3^{(7-1)}
$$
$$
a_7 = 2 \cdot 3^6
$$
$$
a_7 = 2 \cdot 729 = 1458
$$

**Resultado:**
$$
\boxed{1458}
$$

---

### Ejemplo 2: Razón Fraccionaria (Decrecimiento)
Encuentra el 5º término de: $$80, 40, 20, 10, \dots$$

**Datos:**
- $$a_1 = 80$$
- $$r = 40/80 = 0.5$$ (o $$1/2$$)

**Cálculo:**
$$
a_5 = 80 \cdot (0.5)^4
$$
$$
a_5 = 80 \cdot 0.0625 = 5
$$

**Resultado:**
$$
\boxed{5}
$$

---

### Ejemplo 3: Hallar la razón
Si el primer término es 5 y el cuarto es 40, ¿cuál es la razón?

**Planteamiento:**
Del 1º al 4º hay 3 saltos (multiplicaciones).
$$
a_4 = a_1 \cdot r^3
$$
$$
40 = 5 \cdot r^3
$$
$$
8 = r^3
$$
¿Qué número al cubo da 8? ¡El 2!

**Resultado:**
$$
\boxed{r = 2}
$$

---

## ➕ Suma de Términos (La Leyenda del Ajedrez)

Cuenta la leyenda que el inventor del ajedrez pidió como pago un grano de trigo por la primera casilla, 2 por la segunda, 4 por la tercera, y así sucesivamente. El rey aceptó riendo, sin saber que la suma total arruinaría al reino.

La fórmula para sumar $n$ términos es:

$$
S_n = \frac{a_1(r^n - 1)}{r - 1}
$$

### Ejemplo 4: Suma Finita
Suma los primeros 8 términos de: $1, 3, 9, 27, \dots$

**Datos:** $a_1=1, r=3, n=8$.

$$
S_8 = \frac{1(3^8 - 1)}{3 - 1}
$$
$$
S_8 = \frac{6561 - 1}{2} = \frac{6560}{2}
$$

**Resultado:**
$$
\boxed{3280}
$$

---

## ♾️ Suma Infinita (La Magia)

Si la secuencia se va haciendo más pequeña ($$-1 < r < 1$$), podemos sumar **infinitos** números y obtener un resultado finito. Es como caminar hacia una pared dando pasos cada vez más cortos (mitad, mitad, mitad...): nunca te pasas de la pared.

$$
S_{\infty} = \frac{a_1}{1 - r}
$$

### Ejemplo 5: Sumando hasta el infinito
Suma: $100 + 50 + 25 + 12.5 + \dots$

**Datos:** $a_1 = 100, r = 0.5$.

$$
S_{\infty} = \frac{100}{1 - 0.5}
$$
$$
S_{\infty} = \frac{100}{0.5} = 200
$$

**Resultado:**
$$
\boxed{200}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el siguiente término de $$3, 12, 48, \dots$$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$
r = 12/3 = 4
$$
$$
48 \cdot 4 = 192
$$

**Resultado:** 
$$
\boxed{192}
$$

</details>

---

### Ejercicio 2
Halla el término general de $$2, 10, 50, \dots$$.

<details>
<summary>Ver solución</summary>

**Datos:**
- $$a_1 = 2$$
- $$r = 5$$

**Resultado:** 
$$
\boxed{a_n = 2 \cdot 5^{n-1}}
$$

</details>

---

### Ejercicio 3
Calcula la suma de los primeros 5 términos de $$1, 2, 4, 8 \dots$$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$
S_5 = \frac{1(2^5 - 1)}{2 - 1}
$$
$$
S_5 = 32 - 1 = 31
$$

**Resultado:** 
$$
\boxed{31}
$$

</details>

---

### Ejercicio 4
Encuentra la suma infinita de $$1 + 1/3 + 1/9 + 1/27 \dots$$.

<details>
<summary>Ver solución</summary>

**Datos:**
- $$a_1 = 1$$
- $$r = 1/3$$

**Cálculo:**
$$
S_{\infty} = \frac{1}{1 - 1/3}
$$
$$
S_{\infty} = \frac{1}{2/3} = 3/2 = 1.5
$$

**Resultado:** 
$$
\boxed{1.5}
$$

</details>

---

### Ejercicio 5
Si $$a_1 = 3$$ y $$r = 2$$, ¿cuál es el 6º término?

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$
a_6 = 3 \cdot 2^{6-1}
$$
$$
a_6 = 3 \cdot 2^5
$$
$$
a_6 = 3 \cdot 32 = 96
$$

**Resultado:** 
$$
\boxed{96}
$$

</details>

---

### Ejercicio 6
Una pelota rebota a la mitad de su altura anterior. Si cae de 20 m, ¿cuánto sube en el primer rebote? ¿Y en el segundo?

<details>
<summary>Ver solución</summary>

**Datos:**
- $$r = 0.5$$

**Cálculo:**
$$
\text{Rebote 1} = 20 \cdot 0.5 = 10
$$
$$
\text{Rebote 2} = 10 \cdot 0.5 = 5
$$

**Resultado:** 
$$
\boxed{10 \text{ m y } 5 \text{ m}}
$$

</details>

---

### Ejercicio 7
Calcula el 4º término de $$81, 27, 9 \dots$$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$
r = 27/81 = 1/3
$$
$$
9 \cdot 1/3 = 3
$$

**Resultado:** 
$$
\boxed{3}
$$

</details>

---

### Ejercicio 8
¿Cuál es la razón de $$5, -10, 20, -40 \dots$$?

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$
-10 / 5 = -2
$$

**Resultado:** 
$$
\boxed{-2}
$$

</details>

---

### Ejercicio 9
Suma infinitos términos: $$16 + 8 + 4 + 2 \dots$$.

<details>
<summary>Ver solución</summary>

**Datos:**
- $$a_1 = 16$$
- $$r = 0.5$$

**Cálculo:**
$$
S_{\infty} = \frac{16}{1 - 0.5}
$$
$$
S_{\infty} = \frac{16}{0.5} = 32
$$

**Resultado:** 
$$
\boxed{32}
$$

</details>

---

### Ejercicio 10
Si ahorras 1 peso hoy, 3 mañana, 9 pasado... ¿cuánto ahorras el día 5?

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$
a_5 = 1 \cdot 3^{5-1}
$$
$$
a_5 = 1 \cdot 3^4 = 81
$$

**Resultado:** 
$$
\boxed{81 \text{ pesos}}
$$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula | Notas |
| :--- | :--- | :--- |
| **Término General** | $$a_n = a_1 \cdot r^{n-1}$$ | Crecimiento exponencial. |
| **Suma Finita** | $$S_n = \frac{a_1(r^n - 1)}{r - 1}$$ | Crece muy rápido si $$r > 1$$. |
| **Suma Infinita** | $$S_{\infty} = \frac{a_1}{1 - r}$$ | Solo si el valor se reduce ($$|r| < 1$$). |

![progresiones-geometricas](https://cdn.ediprofe.com/img/matematicas/uf7p-progresiones-geometricas.webp)

> **Conclusión:** Las progresiones geométricas explican desde los intereses bancarios hasta la viralidad en redes sociales. Pequeños cambios multiplicativos llevan a resultados gigantescos.
