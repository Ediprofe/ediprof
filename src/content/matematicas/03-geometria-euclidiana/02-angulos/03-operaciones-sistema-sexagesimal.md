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

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Suma con Acarreo
Sumar $32^\circ \, 45' \, 50'' + 10^\circ \, 20' \, 30''$.

**Paso 1: Suma vertical directa**
- Segundos: $50 + 30 = 80''$
- Minutos: $45 + 20 = 65'$
- Grados: $32 + 10 = 42^\circ$

**Resultado provisional:** $42^\circ \, 65' \, 80''$.

**Paso 2: Ajuste de Segundos**
$80''$ se pasan de 60. Son $1'$ y sobran $20''$.
- Sumamos $1'$ a los $65'$ que teníamos $\to 66'$.
- Quedan $20''$.
**Nuevo estado:** $42^\circ \, 66' \, 20''$.

**Paso 3: Ajuste de Minutos**
$66'$ se pasan de 60. Son $1^\circ$ y sobran $6'$.
- Sumamos $1^\circ$ a los $42^\circ \to 43^\circ$.
- Quedan $6'$.

**Resultado Final:**
$$
\boxed{43^\circ \, 6' \, 20''}
$$

### Ejemplo 2: Resta pidiendo prestado
Restar $90^\circ - 35^\circ \, 20'$.

**Planteamiento:**
$$
 \begin{array}{r}
   90^\circ \quad 00' \\
 - 35^\circ \quad 20' \\
 \hline
 \end{array}
$$

**Paso 1: Préstamo**
A $00'$ no le puedo quitar $20'$. Pido $1^\circ$ prestado al 90.
- El $90^\circ$ se vuelve $89^\circ$.
- El $1^\circ$ prestado se convierte en $60'$.

**Nuevo planteamiento:**
$$
 \begin{array}{r}
   89^\circ \quad 60' \\
 - 35^\circ \quad 20' \\
 \hline
   54^\circ \quad 40'
 \end{array}
$$

**Resultado Final:**
$$
\boxed{54^\circ \, 40'}
$$

### Ejemplo 3: De Decimal a Sexagesimal
Convertir $12.755^\circ$ a grados, minutos y segundos.

**Paso 1: Grados enteros**
Tenemos **$12^\circ$**. Sobra $0.755^\circ$.

**Paso 2: Minutos**
Multiplicamos el sobrante por 60.
$$
0.755 \times 60 = 45.3'
$$
Tenemos **$45'$**. Sobra $0.3'$.

**Paso 3: Segundos**
Multiplicamos el nuevo sobrante por 60.
$$
0.3 \times 60 = 18''
$$
Tenemos **$18''$**.

**Resultado Final:**
$$
\boxed{12^\circ \, 45' \, 18''}
$$

### Ejemplo 4: Resta Simple
Restar $50^\circ \, 30'$ de $80^\circ \, 45'$.

**Razonamiento:**
Aquí no necesitamos pedir prestado porque los números de arriba son mayores.
- Minutos: $45 - 30 = 15'$
- Grados: $80 - 50 = 30^\circ$

**Resultado:**
$$
\boxed{30^\circ \, 15'}
$$

### Ejemplo 5: Suma llevando dos veces
Suma $50'' + 50''$.

**Razonamiento:**
$50 + 50 = 100''$.
Como $100''$ es mayor que 60:
$$
100 \div 60 = 1 \text{ (minuto) y sobran } 40 \text{ (segundos)}
$$

**Resultado:**
$$
\boxed{1' \, 40''}
$$

### Ejemplo 6: Multiplicación Mental
Si tienes un ángulo de $10^\circ \, 30'$ y lo duplicas, ¿cuánto tienes?

**Razonamiento:**
- Doble de $10^\circ = 20^\circ$.
- Doble de $30' = 60'$.
- Pero $60'$ es $1^\circ$.

Total: $20^\circ + 1^\circ = 21^\circ$.

**Resultado:**
$$
\boxed{21^\circ}
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
