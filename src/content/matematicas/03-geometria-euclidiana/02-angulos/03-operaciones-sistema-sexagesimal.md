# Operaciones en Sistema Sexagesimal

Ahora que conocemos el sistema sexagesimal (grados, minutos y segundos), aprenderemos a realizar **operaciones aritméticas** con ángulos y a **convertir** entre diferentes formatos.

---

## 📖 Suma de ángulos

Para sumar ángulos en sistema sexagesimal, sumamos por separado: grados con grados, minutos con minutos, segundos con segundos.

### Regla de acarreo

- Si los segundos suman **60 o más**, restamos 60 y añadimos 1 al minuto
- Si los minutos suman **60 o más**, restamos 60 y añadimos 1 al grado

### Ejemplo 1

Sumar $25° \, 30' \, 40''$ + $18° \, 20' \, 15''$

**Paso 1:** Sumar cada columna

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| Primer ángulo | 25 | 30 | 40 |
| Segundo ángulo | 18 | 20 | 15 |
| **Suma** | 43 | 50 | 55 |

**Resultado:**
$$
25° \, 30' \, 40'' + 18° \, 20' \, 15'' = 43° \, 50' \, 55''
$$

---

### Ejemplo 2 (con acarreo)

Sumar $45° \, 50' \, 45''$ + $30° \, 25' \, 30''$

**Paso 1:** Sumar cada columna

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| Primer ángulo | 45 | 50 | 45 |
| Segundo ángulo | 30 | 25 | 30 |
| **Suma parcial** | 75 | 75 | 75 |

**Paso 2:** Ajustar los segundos (75'' ≥ 60)

$$
75'' = 60'' + 15'' = 1' + 15''
$$

Llevamos 1 a los minutos: $75' + 1' = 76'$

**Paso 3:** Ajustar los minutos (76' ≥ 60)

$$
76' = 60' + 16' = 1° + 16'
$$

Llevamos 1 a los grados: $75° + 1° = 76°$

**Resultado:**
$$
45° \, 50' \, 45'' + 30° \, 25' \, 30'' = 76° \, 16' \, 15''
$$

---

## 📖 Resta de ángulos

Para restar ángulos, restamos columna por columna. Si necesitamos, "pedimos prestado".

### Regla de préstamo

- Si no podemos restar los segundos, pedimos 1 minuto (= 60 segundos)
- Si no podemos restar los minutos, pedimos 1 grado (= 60 minutos)

### Ejemplo 1

Restar $50° \, 40' \, 30''$ - $20° \, 15' \, 10''$

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| Primer ángulo | 50 | 40 | 30 |
| Segundo ángulo | 20 | 15 | 10 |
| **Resta** | 30 | 25 | 20 |

**Resultado:**
$$
50° \, 40' \, 30'' - 20° \, 15' \, 10'' = 30° \, 25' \, 20''
$$

---

### Ejemplo 2 (con préstamo)

Restar $60° \, 20' \, 15''$ - $35° \, 45' \, 30''$

**Problema:** No podemos restar 30'' de 15'', ni 45' de 20'.

**Paso 1:** Pedir prestado para los segundos

Pedimos 1 minuto de los 20 minutos:
- Los minutos quedan: $20' - 1' = 19'$
- Los segundos quedan: $15'' + 60'' = 75''$

**Paso 2:** Pedir prestado para los minutos

Pedimos 1 grado de los 60 grados:
- Los grados quedan: $60° - 1° = 59°$
- Los minutos quedan: $19' + 60' = 79'$

**Paso 3:** Realizar la resta

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| Ángulo ajustado | 59 | 79 | 75 |
| Segundo ángulo | 35 | 45 | 30 |
| **Resta** | 24 | 34 | 45 |

**Resultado:**
$$
60° \, 20' \, 15'' - 35° \, 45' \, 30'' = 24° \, 34' \, 45''
$$

---

## 📖 Conversión: Sexagesimal a Decimal

A veces necesitamos expresar un ángulo solo en grados (con decimales).

### Fórmula

$$
\text{Grados decimales} = g + \frac{m}{60} + \frac{s}{3600}
$$

Donde $g$ = grados, $m$ = minutos, $s$ = segundos.

### Ejemplo 1

Convertir $45° \, 30'$ a decimal:

$$
45 + \frac{30}{60} = 45 + 0.5 = 45.5°
$$

### Ejemplo 2

Convertir $30° \, 15' \, 36''$ a decimal:

$$
30 + \frac{15}{60} + \frac{36}{3600} = 30 + 0.25 + 0.01 = 30.26°
$$

### Ejemplo 3

Convertir $90° \, 0' \, 0''$ a decimal:

$$
90 + \frac{0}{60} + \frac{0}{3600} = 90°
$$

---

## 📖 Conversión: Decimal a Sexagesimal

Para convertir de decimal a sexagesimal, separamos la parte entera (grados) y convertimos la parte decimal.

### Procedimiento

1. Los **grados** son la parte entera
2. Multiplica la parte decimal por 60 → los **minutos** (parte entera)
3. Multiplica la nueva parte decimal por 60 → los **segundos**

### Ejemplo 1

Convertir $45.5°$ a sexagesimal:

**Paso 1:** Grados = 45

**Paso 2:** $0.5 \times 60 = 30$ minutos

**Resultado:** $45° \, 30'$

### Ejemplo 2

Convertir $72.625°$ a sexagesimal:

**Paso 1:** Grados = 72

**Paso 2:** $0.625 \times 60 = 37.5$ → Minutos = 37

**Paso 3:** $0.5 \times 60 = 30$ → Segundos = 30

**Resultado:** $72° \, 37' \, 30''$

### Ejemplo 3

Convertir $123.75°$ a sexagesimal:

**Paso 1:** Grados = 123

**Paso 2:** $0.75 \times 60 = 45$ → Minutos = 45

**Resultado:** $123° \, 45'$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Suma

Realiza las siguientes sumas:

1. $35° \, 20' \, 15''$ + $42° \, 30' \, 25''$
2. $55° \, 45' \, 50''$ + $28° \, 30' \, 40''$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $77° \, 50' \, 40''$
2. $84° \, 16' \, 30''$ (hay que llevar en segundos y minutos)

</details>

---

### Ejercicio 2: Resta

Realiza las siguientes restas:

1. $80° \, 45' \, 30''$ - $25° \, 20' \, 10''$
2. $90° \, 0' \, 0''$ - $35° \, 25' \, 40''$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $55° \, 25' \, 20''$
2. $54° \, 34' \, 20''$

</details>

---

### Ejercicio 3: Conversión a decimal

Convierte a grados decimales:

1. $60° \, 30'$
2. $45° \, 15' \, 0''$
3. $90° \, 0' \, 36''$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $60.5°$
2. $45.25°$
3. $90.01°$

</details>

---

### Ejercicio 4: Conversión a sexagesimal

Convierte a grados, minutos y segundos:

1. $35.5°$
2. $120.25°$
3. $75.75°$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $35° \, 30'$
2. $120° \, 15'$
3. $75° \, 45'$

</details>

---
