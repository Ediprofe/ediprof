# **Operaciones en Sistema Sexagesimal**

Sumar y restar ángulos no es tan sencillo como sumar números normales "decimales". Como el sistema sexagesimal se reinicia cada 60, es parecido a sumar horas y minutos. Si sumas 50 minutos más 20 minutos, no tienes "70 minutos", tienes "1 hora y 10 minutos".

---

## 🎯 ¿Qué vas a aprender?

- Cómo sumar ángulos llevando los sobrantes (acarreo).
- Cómo restar ángulos "pidiendo prestado" a los grados.
- Convertir de grados con decimales ($45.5^\circ$) a grados con minutos ($45^\circ 30'$).

---

## ➕ Suma de Ángulos

Sumamos columnas con columnas (segundos con segundos, minutos con minutos, grados con grados). Si una columna se pasa de 60, convertimos el exceso a la unidad superior.

### Regla de Oro
$$
60'' = 1'
$$
$$
60' = 1^\circ
$$

---

## ➖ Resta de Ángulos

Si el número de arriba es menor que el de abajo, no podemos restar directamente. Debemos "pedir prestado" a la unidad de la izquierda.

### Regla del Préstamo
- Si pido $1^\circ$, recibo **$60'$**.
- Si pido $1'$, recibo **$60''$**.

---

## ➕ Sección 1: Suma de Ángulos

Sumar ángulos es agrupar. La clave es recordar que cada vez que acumulas 60 en una columna (segundos o minutos), eso se convierte en 1 unidad de la columna siguiente (izquierda).

### Ejemplo 1.1: Suma Directa (Sin Acarreo)
Sumar $10^\circ \, 20' + 20^\circ \, 10'$.

**Razonamiento:**
Ordenamos en columnas y sumamos.

| | Grados ($^\circ$) | Minutos ($'$) |
| :--- | :---: | :---: |
| | $10$ | $20$ |
| **(+)** | $20$ | $10$ |
| **Total** | **$30$** | **$30$** |

**Resultado:**
$$
\boxed{30^\circ \, 30'}
$$

### Ejemplo 1.2: Suma con Acarreo Simple
Sumar $32^\circ \, 45' \, 50'' + 10^\circ \, 20' \, 30''$.

**Paso 1: Suma por columnas**

| | Grados | Minutos | Segundos |
| :--- | :---: | :---: | :---: |
| | $32$ | $45$ | $50$ |
| **(+)** | $10$ | $20$ | $30$ |
| **Suma Inicial** | **$42$** | **$65$** | **$80$** |

**Paso 2: Ajuste de Acarreo (Llevadas)**
Siempre empezamos ajustando de derecha a izquierda (desde los segundos).

1.  **Segundos:** Tenemos **$80''$**.
    *   Como $60'' = 1'$, nos llevamos 1 a los minutos.
    *   Sobran $20''$.
    *   *Minutos ahora:* $65 + 1 = 66'$.
2.  **Minutos:** Tenemos **$66'$**.
    *   Como $60' = 1^\circ$, nos llevamos 1 a los grados.
    *   Sobran $6'$.
    *   *Grados ahora:* $42 + 1 = 43^\circ$.

**Resultado:**
$$
\boxed{43^\circ \, 6' \, 20''}
$$

![suma-de-angulos](https://cdn.ediprofe.com/img/matematicas/zjmm-suma-de-angulos.webp)

### Ejemplo 1.3: Suma de Minutos que completan grado
Sumar $40^\circ \, 50' + 10^\circ \, 30'$.

**Razonamiento:**

| | Grados | Minutos |
| :--- | :---: | :---: |
| | $40$ | $50$ |
| **(+)** | $10$ | $30$ |
| **Total** | **$50$** | **$80$** |

Ajustamos los $80'$:
*   $80' = 60' + 20' = 1^\circ + 20'$.
*   Sumamos ese grado extra: $50^\circ + 1^\circ = 51^\circ$.

**Resultado:**
$$
\boxed{51^\circ \, 20'}
$$

### Ejemplo 1.4: Suma llevando dos veces (Solo Segundos)
Suma $50'' + 50''$.

**Razonamiento:**
$50'' + 50'' = 100''$.

$$
100 \div 60 = 1 \text{ (minuto) y sobran } 40 \text{ (segundos)}
$$

**Resultado:**
$$
\boxed{1' \, 40''}
$$

![suma-llevando-dos-veces](https://cdn.ediprofe.com/img/matematicas/0mjx-suma-llevando-dos-veces.webp)

### Ejemplo 1.5: Suma Triple
Sumar tres ángulos: $10^\circ + 15^\circ \, 40' + 5^\circ \, 30'$.

**Razonamiento:**

| | Grados | Minutos |
| :--- | :---: | :---: |
| | $10$ | $00$ |
| | $15$ | $40$ |
| **(+)** | $5$ | $30$ |
| **Suma** | **$30$** | **$70$** |

Ajustamos los $70'$:
*   $70' = 1^\circ$ y sobran $10'$.
*   Total grados: $30 + 1 = 31^\circ$.

**Resultado:**
$$
\boxed{31^\circ \, 10'}
$$

---

## ➖ Sección 2: Resta de Ángulos

La resta suele ser más desafiante porque a veces "no nos alcanza". En esos casos, rompemos 1 grado para obtener 60 minutos (o 1 minuto para 60 segundos).

### Ejemplo 2.1: Resta Simple
Restar $50^\circ \, 30'$ de $80^\circ \, 45'$.

**Razonamiento:**

| | Grados | Minutos |
| :--- | :---: | :---: |
| | $80$ | $45$ |
| **(-)** | $50$ | $30$ |
| **Resta** | **$30$** | **$15$** |

Aquí no hubo problema porque los de arriba eran mayores.

**Resultado:**
$$
\boxed{30^\circ \, 15'}
$$

![resta-simple](https://cdn.ediprofe.com/img/matematicas/aoqx-resta-simple.webp)

### Ejemplo 2.2: Resta pidiendo prestado a Grados
Restar $90^\circ - 35^\circ \, 20'$.

**El Problema:**
Al intentar ponerlo en tabla, vemos un hueco arriba.

| | Grados | Minutos |
| :--- | :---: | :---: |
| | $90$ | $00$ ⚠️ |
| **(-)** | $35$ | $20$ |

No podemos restar $0 - 20$.

**La Solución (El Préstamo):**
Quitamos 1 grado al 90 y se lo damos a los minutos como 60.

| | Grados | Minutos |
| :--- | :---: | :---: |
| *Antes* | $90$ | $00$ |
| **TRANSFORMACIÓN** | $\downarrow -1$ | $\downarrow +60$ |
| *Ahora* | **$89$** | **$60$** |
| **(-)** | $35$ | $20$ |
| **Resta Final** | **$54$** | **$40$** |

**Resultado:**
$$
\boxed{54^\circ \, 40'}
$$

![resta-de-angulos](https://cdn.ediprofe.com/img/matematicas/lonv-resta-de-angulos.webp)

### Ejemplo 2.3: Resta pidiendo prestado a Minutos
Restar $10^\circ \, 15' - 5^\circ \, 40'$.

**Razonamiento:**

| | Grados | Minutos |
| :--- | :---: | :---: |
| *Inicial* | $10$ | $15$ |
| **Ajuste** | $9$ | $75$ |
| **(-)** | $5$ | $40$ |
| **Resta** | **$4$** | **$35$** |

*Nota del ajuste:* El $10$ bajó a $9$. El $15$ sumó $60$ y se volvió $75$.

**Resultado:**
$$
\boxed{4^\circ \, 35'}
$$

### Ejemplo 2.4: Resta Doble (El Préstamo en Cadena)
Restar $20^\circ - 5^\circ \, 10' \, 10''$.

**Razonamiento:**
Necesitamos segundos y minutos arriba, pero tenemos ceros. El préstamo va en cadena como una cascada.

1.  **Grados a Minutos:** $20^\circ \to 19^\circ$ y pasamos $60'$.
2.  **Minutos a Segundos:** De esos $60'$, tomamos 1 (quedan $59'$) y pasamos $60''$.

**Tabla Final de Resta:**

| | Grados | Minutos | Segundos |
| :--- | :---: | :---: | :---: |
| *Transformado* | $19$ | $59$ | $60$ |
| **(-)** | $5$ | $10$ | $10$ |
| **Resta** | **$14$** | **$49$** | **$50$** |

**Resultado:**
$$
\boxed{14^\circ \, 49' \, 50''}
$$

### Ejemplo 2.5: Resta de Suplemento
Calcular el suplemento de $125^\circ \, 45'$.

**Razonamiento:**
Operación: $180^\circ - 125^\circ \, 45'$.

| | Grados | Minutos |
| :--- | :---: | :---: |
| *Transformado ($180^\circ$)* | $179$ | $60$ |
| **(-)** | $125$ | $45$ |
| **Resta** | **$54$** | **$15$** |

**Resultado:**
$$
\boxed{54^\circ \, 15'}
$$

---

## ✖️ Sección 3: Multiplicación, División y Conversión

Aquí veremos cómo manipular ángulos cambiándolos de escala o de formato.

### Ejemplo 3.1: Conversión de Decimal a Sexagesimal
Convertir $12.755^\circ$ a grados, minutos y segundos.

**Razonamiento:**
Descomponemos la parte decimal multiplicando por 60 sucesivamente.
1.  Entero: $12^\circ$. Sobra $0.755$.
2.  Minutos: $0.755 \times 60 = 45.3'$. Tenemos $45'$ y sobra $0.3$.
3.  Segundos: $0.3 \times 60 = 18''$. Exactos.

**Resultado:**
$$
\boxed{12^\circ \, 45' \, 18''}
$$

![conversion-decimal-a-sexagesimal](https://cdn.ediprofe.com/img/matematicas/52ci-conversion-decimal-a-sexagesimal.webp)

### Ejemplo 3.2: Conversión de Sexagesimal a Decimal
Convertir $30^\circ \, 30'$ a grados decimales.

**Razonamiento:**
Hacemos el proceso inverso: dividimos por 60.
1.  Tomamos los minutos: $30'$.
2.  Dividimos: $30 \div 60 = 0.5$.
3.  Sumamos a los grados: $30 + 0.5 = 30.5$.

**Resultado:**
$$
\boxed{30.5^\circ}
$$

### Ejemplo 3.3: Multiplicación Mental (Escalar simple)
Si tienes un ángulo de $10^\circ \, 30'$ y lo duplicas.

**Razonamiento:**
Multiplicamos cada parte por 2.
1.  $10^\circ \times 2 = 20^\circ$.
2.  $30' \times 2 = 60'$.
3.  Ajustamos: $60'$ es exactamente $1^\circ$. Lo sumamos a los 20.

**Resultado:**
$$
\boxed{21^\circ}
$$

![multiplicacion-mental](https://cdn.ediprofe.com/img/matematicas/q8nx-multiplicacion-mental.webp)

### Ejemplo 3.4: Multiplicación con Acarreo
Multiplicar $20^\circ \, 40' \times 3$.

**Razonamiento:**
1.  Minutos: $40 \times 3 = 120'$.
2.  Grados: $20 \times 3 = 60^\circ$.
3.  Ajuste: $120'$ son exactamente $2^\circ$ ($120 \div 60 = 2$).
4.  Sumamos: $60^\circ + 2^\circ = 62^\circ$.

**Resultado:**
$$
\boxed{62^\circ}
$$

### Ejemplo 3.5: División Simple
Dividir $45^\circ$ entre 2 (Bisecar el ángulo).

**Razonamiento:**
1.  $45 \div 2 = 22.5^\circ$.
2.  Pero en sexagesimal no solemos dejar decimales si podemos usar minutos.
3.  El $0.5^\circ$ restante lo multiplicamos por 60 para volverlo minutos: $0.5 \times 60 = 30'$.

**Resultado:**
$$
\boxed{22^\circ \, 30'}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Suma: $20^\circ 30' + 10^\circ 40'$.

<details>
<summary>Ver solución</summary>

$30' + 40' = 70' = 1^\circ 10'$.
$20^\circ + 10^\circ + 1^\circ = 31^\circ$.
**Resultado:** $\boxed{31^\circ 10'}$

</details>

---

### Ejercicio 2
Resta: $50^\circ 15' - 10^\circ 30'$.

<details>
<summary>Ver solución</summary>

Pido prestado: $49^\circ 75' - 10^\circ 30'$.
**Resultado:** $\boxed{39^\circ 45'}$

</details>

---

### Ejercicio 3
Convertir $10.5^\circ$ a sexagesimal.

<details>
<summary>Ver solución</summary>

$0.5 \times 60 = 30$.
**Resultado:** $\boxed{10^\circ 30'}$

</details>

---

### Ejercicio 4
Convertir $20^\circ 15'$ a decimal.

<details>
<summary>Ver solución</summary>

$15/60 = 0.25$.
**Resultado:** $\boxed{20.25^\circ}$

</details>

---

### Ejercicio 5
Suma: $45^\circ 10' 10'' + 5^\circ 50' 50''$.

<details>
<summary>Ver solución</summary>

$60'' \to 1'$, suman $10'+50'+1' = 61' \to 1^\circ 1'$.
$45^\circ + 5^\circ + 1^\circ = 51^\circ$.
**Resultado:** $\boxed{51^\circ 1' 0''}$

</details>

---

### Ejercicio 6
Calcula el suplemento de $100^\circ 20'$ ($180^\circ - \text{ángulo}$).

<details>
<summary>Ver solución</summary>

$179^\circ 60' - 100^\circ 20'$.
**Resultado:** $\boxed{79^\circ 40'}$

</details>

---

### Ejercicio 7
Multiplicación: $10^\circ 20' \times 3$.

<details>
<summary>Ver solución</summary>

$30^\circ 60' = 31^\circ$.
**Resultado:** $\boxed{31^\circ}$

</details>

---

### Ejercicio 8
División: $45^\circ 30' \div 2$.

<details>
<summary>Ver solución</summary>

$45/2 = 22.5^\circ$.
$0.5^\circ = 30'$.
$30' + 30' = 60'$.
$60' / 2 = 30'$.
**Resultado:** $\boxed{22^\circ 45'}$

</details>

---

### Ejercicio 9
Resta: $1^\circ - 1''$.

<details>
<summary>Ver solución</summary>

$1^\circ = 59' 60''$.
$60'' - 1'' = 59''$.
**Resultado:** $\boxed{0^\circ 59' 59''}$

</details>

---

### Ejercicio 10
Convierte $30.1^\circ$ a sexagesimal.

<details>
<summary>Ver solución</summary>

$0.1 \times 60 = 6$.
**Resultado:** $\boxed{30^\circ 6'}$

</details>

---

## 🔑 Resumen

| Operación | Clave |
|:--- |:--- |
| **Suma** | Si te pasas de 60, lleva 1 a la siguiente unidad. |
| **Resta** | Si te falta, rompe 1 grado en 60 minutos (o 1 minuto en 60 segundos). |
| **Decimal a Sexagesimal** | Multiplica la parte decimal por 60. |
| **Sexagesimal a Decimal** | Divide minutos por 60 y segundos por 3600. |

> **Conclusión:** Operar con ángulos exige orden. Mantén las columnas alineadas y recuerda siempre que el "número mágico" de cambio es 60, no 100.
