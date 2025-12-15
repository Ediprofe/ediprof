# 📐 **Operaciones en Sistema Sexagesimal**

Ahora que conocemos el sistema sexagesimal (grados, minutos y segundos), aprenderemos a realizar **operaciones aritméticas** con ángulos y a **convertir** entre diferentes formatos.

---

## 🎯 **Suma de Ángulos**

Para sumar ángulos en sistema sexagesimal, sumamos **columna por columna**: grados con grados, minutos con minutos, segundos con segundos.

### Regla de acarreo

> 💡 **Idea clave:** Si los segundos o minutos suman **60 o más**, debemos "llevar" al siguiente nivel:
> - 60'' = 1' (llevamos 1 al minuto)
> - 60' = 1° (llevamos 1 al grado)

### 📝 Ejemplo detallado: Suma con doble acarreo

**Problema:** $45° \, 50' \, 45'' + 30° \, 25' \, 30''$

**PASO 1:** Sumamos columna por columna

| | Grados (°) | Minutos (') | Segundos ('') |
|:--:|:----------:|:-----------:|:-------------:|
| Primer ángulo | 45 | 50 | 45 |
| Segundo ángulo | +30 | +25 | +30 |
| **Suma parcial** | **75** | **75** | **75** |

**PASO 2:** Revisamos si hay que llevar

- ❌ **Segundos = 75''** → Como 75 ≥ 60, llevamos: $75'' = 60'' + 15'' = 1' + 15''$
- Sumamos el 1' a los minutos: $75' + 1' = 76'$

| | Grados (°) | Minutos (') | Segundos ('') |
|:--:|:----------:|:-----------:|:-------------:|
| Después de ajustar segundos | 75 | 75 + 1 = **76** | **15** |

**PASO 3:** Revisamos los minutos

- ❌ **Minutos = 76'** → Como 76 ≥ 60, llevamos: $76' = 60' + 16' = 1° + 16'$
- Sumamos el 1° a los grados: $75° + 1° = 76°$

| | Grados (°) | Minutos (') | Segundos ('') |
|:--:|:----------:|:-----------:|:-------------:|
| **RESULTADO FINAL** | **76** | **16** | **15** |

$$\boxed{45° \, 50' \, 45'' + 30° \, 25' \, 30'' = 76° \, 16' \, 15''}$$

> ✅ **Resumen del proceso:** Llevamos 1' de los segundos a los minutos, luego llevamos 1° de los minutos a los grados.

---

### ⚙️ Ejemplo 1 — Suma simple

**Sumar:** $25° \, 30' \, 40''$ + $18° \, 20' \, 15''$

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| Primer ángulo | 25 | 30 | 40 |
| Segundo ángulo | 18 | 20 | 15 |
| **Suma** | 43 | 50 | 55 |

$$\boxed{25° \, 30' \, 40'' + 18° \, 20' \, 15'' = 43° \, 50' \, 55''}$$

---

### ⚙️ Ejemplo 2 — Suma con acarreo en segundos

**Sumar:** $40° \, 25' \, 45''$ + $15° \, 20' \, 30''$

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| Suma parcial | 55 | 45 | 75 |

75'' ≥ 60, entonces: $75'' = 1' + 15''$

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| **Resultado** | 55 | 46 | 15 |

$$\boxed{40° \, 25' \, 45'' + 15° \, 20' \, 30'' = 55° \, 46' \, 15''}$$

---

### ⚙️ Ejemplo 3 — Suma con acarreo en minutos

**Sumar:** $70° \, 50' \, 20''$ + $20° \, 25' \, 15''$

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| Suma parcial | 90 | 75 | 35 |

75' ≥ 60, entonces: $75' = 1° + 15'$

$$\boxed{70° \, 50' \, 20'' + 20° \, 25' \, 15'' = 91° \, 15' \, 35''}$$

---

### ⚙️ Ejemplo 4 — Suma con doble acarreo

**Sumar:** $45° \, 50' \, 45''$ + $30° \, 25' \, 30''$

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| Suma parcial | 75 | 75 | 75 |

1. 75'' = 1' + 15'' → minutos = 76
2. 76' = 1° + 16' → grados = 76

$$\boxed{45° \, 50' \, 45'' + 30° \, 25' \, 30'' = 76° \, 16' \, 15''}$$

---

### ⚙️ Ejemplo 5 — Suma de ángulos pequeños

**Sumar:** $5° \, 15' \, 30''$ + $3° \, 10' \, 20''$

$$\boxed{5° \, 15' \, 30'' + 3° \, 10' \, 20'' = 8° \, 25' \, 50''}$$

---

### ⚙️ Ejemplo 6 — Suma de ángulos rectos

**Sumar:** $90° \, 0' \, 0''$ + $45° \, 30' \, 0''$

$$\boxed{90° \, 0' \, 0'' + 45° \, 30' \, 0'' = 135° \, 30' \, 0''}$$

---

### ⚙️ Ejemplo 7 — Suma que da ángulo llano

**Sumar:** $120° \, 45' \, 30''$ + $59° \, 14' \, 30''$

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| Suma parcial | 179 | 59 | 60 |

60'' = 1' → minutos = 60 → 60' = 1° → grados = 180

$$\boxed{120° \, 45' \, 30'' + 59° \, 14' \, 30'' = 180° \, 0' \, 0''}$$

---

### ⚙️ Ejemplo 8 — Suma con solo minutos

**Sumar:** $35° \, 40'$ + $22° \, 35'$

$40' + 35' = 75' = 1° + 15'$

$$\boxed{35° \, 40' + 22° \, 35' = 58° \, 15'}$$

---

### ⚙️ Ejemplo 9 — Suma de tres ángulos

**Sumar:** $30° \, 20' \, 10''$ + $25° \, 15' \, 20''$ + $15° \, 10' \, 30''$

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| **Suma** | 70 | 45 | 60 |

60'' = 1' → minutos = 46

$$\boxed{30° \, 20' \, 10'' + 25° \, 15' \, 20'' + 15° \, 10' \, 30'' = 70° \, 46' \, 0''}$$

---

### ⚙️ Ejemplo 10 — Suma de ángulos grandes

**Sumar:** $150° \, 55' \, 55''$ + $100° \, 50' \, 50''$

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| Suma parcial | 250 | 105 | 105 |

105'' = 1' + 45'' → 106' = 1° + 46'

$$\boxed{150° \, 55' \, 55'' + 100° \, 50' \, 50'' = 251° \, 46' \, 45''}$$

---

## 🎯 **Resta de Ángulos**

Para restar ángulos, restamos columna por columna. Si no alcanza, **"pedimos prestado"**.

### Regla de préstamo

> 💡 **Idea clave:** Si no podemos restar:
> - Pedimos 1' al minuto (= 60'')
> - Pedimos 1° al grado (= 60')

### 📝 Ejemplo detallado: Resta con doble préstamo

**Problema:** $60° \, 20' \, 15'' - 35° \, 45' \, 30''$

**PASO 1:** Intentamos restar columna por columna

| | Grados (°) | Minutos (') | Segundos ('') |
|:--:|:----------:|:-----------:|:-------------:|
| Primer ángulo | 60 | 20 | 15 |
| Segundo ángulo | -35 | -45 | -30 |

**Problema detectado:** ❌ No podemos restar 30'' de 15'' (15 < 30)

**PASO 2:** Pedimos 1' prestado a los minutos

- Quitamos 1' de los minutos: $20' - 1' = 19'$
- Sumamos 60'' a los segundos: $15'' + 60'' = 75''$

| | Grados (°) | Minutos (') | Segundos ('') |
|:--:|:----------:|:-----------:|:-------------:|
| Después del préstamo | 60 | **19** ← (20-1) | **75** ← (15+60) |

**Problema detectado:** ❌ Ahora no podemos restar 45' de 19' (19 < 45)

**PASO 3:** Pedimos 1° prestado a los grados

- Quitamos 1° de los grados: $60° - 1° = 59°$
- Sumamos 60' a los minutos: $19' + 60' = 79'$

| | Grados (°) | Minutos (') | Segundos ('') |
|:--:|:----------:|:-----------:|:-------------:|
| Después del préstamo | **59** ← (60-1) | **79** ← (19+60) | 75 |

**PASO 4:** Ahora sí podemos restar

| | Grados (°) | Minutos (') | Segundos ('') |
|:--:|:----------:|:-----------:|:-------------:|
| Ángulo ajustado | 59 | 79 | 75 |
| Segundo ángulo | -35 | -45 | -30 |
| **Operación** | 59-35 | 79-45 | 75-30 |
| **RESULTADO** | **24** | **34** | **45** |

$$\boxed{60° \, 20' \, 15'' - 35° \, 45' \, 30'' = 24° \, 34' \, 45''}$$

> ✅ **Resumen del proceso:** Pedimos 1' prestado (60'') a los minutos para los segundos, luego pedimos 1° prestado (60') a los grados para los minutos.

---

### ⚙️ Ejemplo 1 — Resta simple

**Restar:** $50° \, 40' \, 30''$ - $20° \, 15' \, 10''$

$$\boxed{50° \, 40' \, 30'' - 20° \, 15' \, 10'' = 30° \, 25' \, 20''}$$

---

### ⚙️ Ejemplo 2 — Resta con préstamo en segundos

**Restar:** $45° \, 30' \, 15''$ - $20° \, 15' \, 40''$

No podemos restar 40'' de 15''. Pedimos 1' a los minutos:
- Minutos: $30' - 1' = 29'$
- Segundos: $15'' + 60'' = 75''$

$75'' - 40'' = 35''$

$$\boxed{45° \, 30' \, 15'' - 20° \, 15' \, 40'' = 25° \, 14' \, 35''}$$

---

### ⚙️ Ejemplo 3 — Resta con préstamo en minutos

**Restar:** $60° \, 10' \, 30''$ - $35° \, 40' \, 20''$

No podemos restar 40' de 10'. Pedimos 1° a los grados:
- Grados: $60° - 1° = 59°$
- Minutos: $10' + 60' = 70'$

$$\boxed{60° \, 10' \, 30'' - 35° \, 40' \, 20'' = 24° \, 30' \, 10''}$$

---

### ⚙️ Ejemplo 4 — Resta con doble préstamo

**Restar:** $60° \, 20' \, 15''$ - $35° \, 45' \, 30''$

1. Pedimos 1' a minutos: $20' - 1' = 19'$, $15'' + 60'' = 75''$
2. Pedimos 1° a grados: $60° - 1° = 59°$, $19' + 60' = 79'$

| | Grados | Minutos | Segundos |
|--|--------|---------|----------|
| Ajustado | 59 | 79 | 75 |
| Restar | 35 | 45 | 30 |
| **Resultado** | 24 | 34 | 45 |

$$\boxed{60° \, 20' \, 15'' - 35° \, 45' \, 30'' = 24° \, 34' \, 45''}$$

---

### ⚙️ Ejemplo 5 — Resta de ángulo recto

**Restar:** $90° \, 0' \, 0''$ - $35° \, 25' \, 40''$

Pedimos prestado desde los grados:
- $90° - 1° = 89°$, $0' + 60' = 60'$
- $60' - 1' = 59'$, $0'' + 60'' = 60''$

$89° - 35° = 54°$, $59' - 25' = 34'$, $60'' - 40'' = 20''$

$$\boxed{90° \, 0' \, 0'' - 35° \, 25' \, 40'' = 54° \, 34' \, 20''}$$

---

### ⚙️ Ejemplo 6 — Resta de ángulo llano

**Restar:** $180° \, 0' \, 0''$ - $90° \, 0' \, 0''$

$$\boxed{180° \, 0' \, 0'' - 90° \, 0' \, 0'' = 90° \, 0' \, 0''}$$

---

### ⚙️ Ejemplo 7 — Resta con solo minutos

**Restar:** $75° \, 20'$ - $40° \, 45'$

Pedimos 1° a los grados: $75° - 1° = 74°$, $20' + 60' = 80'$

$80' - 45' = 35'$

$$\boxed{75° \, 20' - 40° \, 45' = 34° \, 35'}$$

---

### ⚙️ Ejemplo 8 — Resta pequeña

**Restar:** $25° \, 30' \, 40''$ - $10° \, 15' \, 20''$

$$\boxed{25° \, 30' \, 40'' - 10° \, 15' \, 20'' = 15° \, 15' \, 20''}$$

---

### ⚙️ Ejemplo 9 — Resta que da ángulo agudo

**Restar:** $120° \, 30' \, 0''$ - $75° \, 45' \, 30''$

Pedimos 1' a minutos: $30' - 1' = 29'$, $0'' + 60'' = 60''$
Pedimos 1° a grados: $120° - 1° = 119°$, $29' + 60' = 89'$

$119° - 75° = 44°$, $89' - 45' = 44'$, $60'' - 30'' = 30''$

$$\boxed{120° \, 30' \, 0'' - 75° \, 45' \, 30'' = 44° \, 44' \, 30''}$$

---

### ⚙️ Ejemplo 10 — Resta de ángulos iguales

**Restar:** $55° \, 30' \, 45''$ - $55° \, 30' \, 45''$

$$\boxed{55° \, 30' \, 45'' - 55° \, 30' \, 45'' = 0° \, 0' \, 0''}$$

---

## 🎯 **Conversión: Sexagesimal a Decimal**

### Fórmula

$$
\boxed{\text{Grados decimales} = g + \frac{m}{60} + \frac{s}{3600}}
$$

Donde: $g$ = grados, $m$ = minutos, $s$ = segundos

---

### ⚙️ Ejemplo 1 — Solo minutos

**Convertir:** $45° \, 30'$ a decimal

$$45 + \frac{30}{60} = 45 + 0.5 = \boxed{45.5°}$$

---

### ⚙️ Ejemplo 2 — Completo

**Convertir:** $30° \, 15' \, 36''$ a decimal

$$30 + \frac{15}{60} + \frac{36}{3600} = 30 + 0.25 + 0.01 = \boxed{30.26°}$$

---

### ⚙️ Ejemplo 3 — Ángulo recto

**Convertir:** $90° \, 0' \, 0''$ a decimal

$$90 + 0 + 0 = \boxed{90°}$$

---

### ⚙️ Ejemplo 4 — Ángulo con muchos segundos

**Convertir:** $60° \, 0' \, 30''$ a decimal

$$60 + \frac{0}{60} + \frac{30}{3600} = 60 + 0.0083... = \boxed{60.0083°}$$

---

### ⚙️ Ejemplo 5 — Cuarto de grado

**Convertir:** $72° \, 15' \, 0''$ a decimal

$$72 + \frac{15}{60} = 72 + 0.25 = \boxed{72.25°}$$

---

### ⚙️ Ejemplo 6 — Tres cuartos

**Convertir:** $45° \, 45' \, 0''$ a decimal

$$45 + \frac{45}{60} = 45 + 0.75 = \boxed{45.75°}$$

---

### ⚙️ Ejemplo 7 — Ángulo grande

**Convertir:** $180° \, 30' \, 0''$ a decimal

$$180 + \frac{30}{60} = 180 + 0.5 = \boxed{180.5°}$$

---

### ⚙️ Ejemplo 8 — Precisión completa

**Convertir:** $123° \, 27' \, 18''$ a decimal

$$123 + \frac{27}{60} + \frac{18}{3600} = 123 + 0.45 + 0.005 = \boxed{123.455°}$$

---

### ⚙️ Ejemplo 9 — Ángulo pequeño

**Convertir:** $5° \, 6' \, 0''$ a decimal

$$5 + \frac{6}{60} = 5 + 0.1 = \boxed{5.1°}$$

---

### ⚙️ Ejemplo 10 — Latitud de una ciudad

**Convertir:** $4° \, 36' \, 0''$ (latitud de Bogotá) a decimal

$$4 + \frac{36}{60} = 4 + 0.6 = \boxed{4.6°}$$

---

## 🎯 **Conversión: Decimal a Sexagesimal**

### Procedimiento

1. **Grados** = parte entera
2. **Minutos** = (parte decimal) × 60 → tomar parte entera
3. **Segundos** = (nueva parte decimal) × 60

---

### ⚙️ Ejemplo 1 — Simple

**Convertir:** $45.5°$ a sexagesimal

- Grados = 45
- $0.5 \times 60 = 30$ minutos

$$\boxed{45.5° = 45° \, 30'}$$

---

### ⚙️ Ejemplo 2 — Cuarto de grado

**Convertir:** $72.25°$ a sexagesimal

- Grados = 72
- $0.25 \times 60 = 15$ minutos

$$\boxed{72.25° = 72° \, 15'}$$

---

### ⚙️ Ejemplo 3 — Tres cuartos

**Convertir:** $123.75°$ a sexagesimal

- Grados = 123
- $0.75 \times 60 = 45$ minutos

$$\boxed{123.75° = 123° \, 45'}$$

---

### ⚙️ Ejemplo 4 — Con segundos

**Convertir:** $72.625°$ a sexagesimal

- Grados = 72
- $0.625 \times 60 = 37.5$ → Minutos = 37
- $0.5 \times 60 = 30$ → Segundos = 30

$$\boxed{72.625° = 72° \, 37' \, 30''}$$

---

### ⚙️ Ejemplo 5 — Ángulo pequeño

**Convertir:** $5.1°$ a sexagesimal

- Grados = 5
- $0.1 \times 60 = 6$ minutos

$$\boxed{5.1° = 5° \, 6'}$$

---

### ⚙️ Ejemplo 6 — Ángulo recto exacto

**Convertir:** $90°$ a sexagesimal

$$\boxed{90° = 90° \, 0' \, 0''}$$

---

### ⚙️ Ejemplo 7 — Decimal periódico

**Convertir:** $60.333...°$ (o sea $60\frac{1}{3}$) a sexagesimal

- $0.333... \times 60 = 20$ minutos

$$\boxed{60.333...° = 60° \, 20'}$$

---

### ⚙️ Ejemplo 8 — Ángulo grande

**Convertir:** $180.5°$ a sexagesimal

- Grados = 180
- $0.5 \times 60 = 30$ minutos

$$\boxed{180.5° = 180° \, 30'}$$

---

### ⚙️ Ejemplo 9 — Con muchos decimales

**Convertir:** $45.755°$ a sexagesimal

- Grados = 45
- $0.755 \times 60 = 45.3$ → Minutos = 45
- $0.3 \times 60 = 18$ → Segundos = 18

$$\boxed{45.755° = 45° \, 45' \, 18''}$$

---

### ⚙️ Ejemplo 10 — Latitud decimal

**Convertir:** $4.6°$ (latitud de Bogotá) a sexagesimal

- Grados = 4
- $0.6 \times 60 = 36$ minutos

$$\boxed{4.6° = 4° \, 36'}$$

---

## 📋 **Resumen de Fórmulas**

| Operación | Procedimiento |
|-----------|---------------|
| **Suma** | Sumar columnas, llevar si ≥ 60 |
| **Resta** | Restar columnas, pedir prestado si no alcanza |
| **Sexagesimal → Decimal** | $g + \frac{m}{60} + \frac{s}{3600}$ |
| **Decimal → Sexagesimal** | Parte entera = grados, decimal × 60 = minutos/segundos |

---

## 📝 **Ejercicios de Práctica**

### Ejercicio 1: Sumas

1. $35° \, 20' \, 15''$ + $42° \, 30' \, 25''$
2. $55° \, 45' \, 50''$ + $28° \, 30' \, 40''$
3. $80° \, 55' \, 55''$ + $40° \, 50' \, 50''$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $77° \, 50' \, 40''$
2. $84° \, 16' \, 30''$
3. $121° \, 46' \, 45''$

</details>

---

### Ejercicio 2: Restas

1. $80° \, 45' \, 30''$ - $25° \, 20' \, 10''$
2. $90° \, 0' \, 0''$ - $35° \, 25' \, 40''$
3. $120° \, 15' \, 0''$ - $85° \, 40' \, 30''$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $55° \, 25' \, 20''$
2. $54° \, 34' \, 20''$
3. $34° \, 34' \, 30''$

</details>

---

### Ejercicio 3: Conversión a decimal

1. $60° \, 30'$
2. $45° \, 15' \, 0''$
3. $90° \, 0' \, 36''$
4. $120° \, 45' \, 0''$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $60.5°$
2. $45.25°$
3. $90.01°$
4. $120.75°$

</details>

---

### Ejercicio 4: Conversión a sexagesimal

1. $35.5°$
2. $120.25°$
3. $75.75°$
4. $50.625°$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $35° \, 30'$
2. $120° \, 15'$
3. $75° \, 45'$
4. $50° \, 37' \, 30''$

</details>

---
