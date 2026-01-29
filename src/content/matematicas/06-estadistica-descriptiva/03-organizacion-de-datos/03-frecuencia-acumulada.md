# **Frecuencia Acumulada**

Imagina que estás ahorrando monedas en una alcancía.
- Día 1: pones 2 monedas. (Total acumulado: 2)
- Día 2: pones 3 monedas. (Total acumulado: 5)
- Día 3: pones 4 monedas. (Total acumulado: 9)

La cantidad de monedas que pones cada día es la **frecuencia absoluta**. El total que tienes guardado hasta ese momento es la **frecuencia acumulada**. En estadística, esto nos sirve para responder preguntas como "¿Cuántos ganan *menos de* cierto valor?" o "¿Qué porcentaje sacó *máximo* cierta nota?".

---

## 🎯 ¿Qué vas a aprender?

- Calcular la frecuencia acumulada absoluta ($F_i$) sumando paso a paso.
- Calcular la frecuencia acumulada relativa ($H_i$) y porcentual.
- Interpretar tablas acumuladas para responder preguntas de tipo "menor que" o "hasta".
- Entender la lógica de la acumulación de datos.

---

## Frecuencia Acumulada Absoluta ($F_i$ o $N_i$)

Es la suma de las frecuencias absolutas de todos los valores iguales o inferiores al considerado. Se calcula sumando progresivamente:
$$ F_1 = f_1 $$
$$ F_2 = f_1 + f_2 $$
$$ F_3 = f_1 + f_2 + f_3 $$
... y así sucesivamente.

### ⚙️ Ejemplos Resueltos: Calculando $F_i$

#### Ejemplo 1: Goles en 5 partidos
**Datos ($f_i$):** 2, 1, 0, 3, 1
**Cálculo Acumulado:**
- Partido 1: 2
- Partido 2: 2 + 1 = 3
- Partido 3: 3 + 0 = 3
- Partido 4: 3 + 3 = 6
- Partido 5: 6 + 1 = 7
**Tabla:**
| Goles | $f_i$ | $F_i$ |
|-------|-------|-------|
| P1 | 2 | 2 |
| P2 | 1 | 3 |
| P3 | 0 | 3 |
| P4 | 3 | 6 |
| P5 | 1 | 7 |

#### Ejemplo 2: Hijos por familia (Muestra de 4 familias)
**Datos ($f_i$):** 1, 2, 4, 1
**Cálculo:**
- 1 + 2 = 3
- 3 + 4 = 7
- 7 + 1 = 8
**Tabla:**
| Fam | $f_i$ | $F_i$ |
|-----|-------|-------|
| A | 1 | 1 |
| B | 2 | 3 |
| C | 4 | 7 |
| D | 1 | 8 |

#### Ejemplo 3: Ventas diarias
**Datos ($f_i$):** Lun: 10, Mar: 15, Mie: 20
**Cálculo:**
- Lun: 10
- Mar: 25
- Mie: 45
**Resultado Final:** 45 ventas acumuladas al miércoles.

#### Ejemplo 4: Notas (1 a 5) de 5 alumnos
**Datos ($f_i$):** 1, 1, 1, 1, 1 (Todos diferentes)
**Cálculo:**
- Alumno 1: 1
- Alumno 2: 2
- Alumno 3: 3
- Alumno 4: 4
- Alumno 5: 5

#### Ejemplo 5: Clientes por hora
**Datos ($f_i$):** 8am: 5, 9am: 10, 10am: 2
**Cálculo:**
- Hasta 8am: 5
- Hasta 9am: 15
- Hasta 10am: 17

---

## Frecuencia Acumulada Relativa ($H_i$)

Es la proporción acumulada. Se puede calcular sumando las frecuencias relativas ($h_i$) o dividiendo la acumulada absoluta entre el total ($F_i / n$).
$$ H_i = \frac{F_i}{n} $$

### ⚙️ Ejemplos Resueltos: Calculando $H_i$

#### Ejemplo 1: Datos cualitativos ordinales (Satisfacción)
**Datos:** Malo (2), Regular (5), Bueno (3). Total $n=10$.
**Acumulada Absoluta ($F_i$):** 2, 7, 10.
**Acumulada Relativa ($H_i$):**
- Malo: $2/10 = 0.2$
- Regular: $7/10 = 0.7$
- Bueno: $10/10 = 1.0$

#### Ejemplo 2: Encuesta rápida (Sí/No)
**Datos:** No (4), Sí (6). Total $n=10$. (Orden lógico: No, luego Sí para acumular total).
**Acumulada ($F_i$):** 4, 10.
**Relativa:**
- No: $0.4$
- Sí: $1.0$

#### Ejemplo 3: Monedas (Lanzamiento 4 veces)
**Datos:** Cara (1), Sello (3). Total $n=4$.
**Acumulada ($F_i$):** 1, 4.
**Relativa:**
- $1/4 = 0.25$
- $4/4 = 1.00$

#### Ejemplo 4: Grados escolares
**Datos:** 6° (5), 7° (15). Total $n=20$.
**Acumulada ($F_i$):** 5, 20.
**Relativa:**
- 6°: $5/20 = 0.25$
- 7°: $20/20 = 1.00$

#### Ejemplo 5: Tallas S, M, L
**Datos:** S (10), M (30), L (10). Total $n=50$.
**Acumulada ($F_i$):** 10, 40, 50.
**Relativa:**
- S: $10/50 = 0.2$
- M: $40/50 = 0.8$ (¡Ojo! El 80% es talla M o menor)
- L: $50/50 = 1.0$

---

## Interpretación: ¿Qué significan los números?

La clave de la frecuencia acumulada es leerla como "hasta aquí".

### ⚙️ Ejemplos Resueltos de Interpretación

#### Ejemplo 1: Notas de examen (0 a 10)
Si para la nota 6, la frecuencia acumulada $F_i$ es 15:
**Interpretación:** 15 estudiantes sacaron una nota de 6 o menos.

#### Ejemplo 2: Salarios
Si para el rango "1-2 Millones", la frecuencia acumulada porcentual es 40%:
**Interpretación:** El 40% de los empleados gana 2 millones o menos.

#### Ejemplo 3: Edades
Si para la edad 18 años, $F_i = 100$ y el total es 200:
**Interpretación:** Hay 100 personas que tienen 18 años o menos (exactamente la mitad de la población).

#### Ejemplo 4: Tiempo de espera
Si la $H_i$ acumulada para "30 minutos" es 0.95:
**Interpretación:** El 95% de los clientes espera 30 minutos o menos. (¡Buen servicio!).

#### Ejemplo 5: Calidad de producto
Si la acumulada hasta "Defectos leves" es del 100%:
**Interpretación:** Todos los productos tienen como máximo defectos leves (no hay defectos graves).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Datos ($f_i$):** 4, 6, 10.
Calcula la serie de frecuencias acumuladas absolutas $F_i$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
1. 4
2. 4 + 6 = 10
3. 10 + 10 = 20
**Resultado:** $\boxed{4, 10, 20}$

</details>

### Ejercicio 2
Si $F_3 = 50$ y $f_4 = 10$, ¿cuánto es $F_4$?

<details>
<summary>Ver solución</summary>

**Razonamiento:** La acumulada siguiente es la anterior más la frecuencia actual.
$$ F_4 = F_3 + f_4 = 50 + 10 = 60 $$
**Resultado:** $\boxed{60}$

</details>

### Ejercicio 3
En una tabla con $n=100$, la frecuencia acumulada relativa del tercer intervalo es $0.45$. ¿Cuántos datos hay acumulados hasta ese intervalo?

<details>
<summary>Ver solución</summary>

**Datos:** $H_i = 0.45, n = 100$.
**Cálculo:**
$$ F_i = H_i \times n = 0.45 \times 100 = 45 $$
**Resultado:** $\boxed{45}$

</details>

### Ejercicio 4
Completa la tabla:
| Dato | $f_i$ | $F_i$ |
|------|-------|-------|
| A | 5 | ? |
| B | ? | 12 |
| C | 8 | ? |

<details>
<summary>Ver solución</summary>

**Paso 1:** $F_1 = f_1 = 5$.
**Paso 2:** $F_2 = F_1 + f_2 \Rightarrow 12 = 5 + f_2 \Rightarrow f_2 = 7$.
**Paso 3:** $F_3 = 12 + 8 = 20$.
**Resultado:** $\boxed{5, 7, 20}$

</details>

### Ejercicio 5
Calcula la acumulada relativa si $F_i = 25$ y $n=50$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$ H_i = \frac{25}{50} = 0.5 $$
**Resultado:** $\boxed{0.5}$

</details>

### Ejercicio 6
**Interpretación:** En una encuesta de satisfacción (1 a 5), la frecuencia acumulada porcentual para el valor 3 es 80%. ¿Qué significa esto?

<details>
<summary>Ver solución</summary>

**Significado:** Que el 80% de los encuestados dio una calificación de 3 o menos (es decir, baja satisfacción). Solo el 20% dio notas de 4 o 5.
**Resultado:** $\boxed{\text{El 80\% calificó con 3 o menos}}$

</details>

### Ejercicio 7
Si $H_{final}$ te da 0.95 en tus cálculos, ¿qué pasó?

<details>
<summary>Ver solución</summary>

**Razonamiento:** La frecuencia acumulada relativa final **siempre** debe ser 1 (o 0.999... por decimales). Si da 0.95, faltó sumar datos.
**Resultado:** $\boxed{\text{Error de cálculo o datos faltantes}}$

</details>

### Ejercicio 8
Dada la serie acumulada $F_i$: 2, 5, 9, 10. Reconstruye las frecuencias absolutas $f_i$.

<details>
<summary>Ver solución</summary>

**Cálculos:**
- $f_1 = 2$
- $f_2 = 5 - 2 = 3$
- $f_3 = 9 - 5 = 4$
- $f_4 = 10 - 9 = 1$
**Resultado:** $\boxed{2, 3, 4, 1}$

</details>

### Ejercicio 9
Calcula qué porcentaje de alumnos sacó menos de 4, si $F_{Nota<4} = 30$ y $n=40$.

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$ \% = \frac{30}{40} \times 100 = 0.75 \times 100 = 75\% $$
**Resultado:** $\boxed{75\%}$

</details>

### Ejercicio 10
Si la ojiva (gráfica de acumuladas) llega hasta una altura de 150 en el eje Y, ¿cuánto es $n$?

<details>
<summary>Ver solución</summary>

**Datos:** La ojiva termina en el total acumulado.
**Resultado:** $\boxed{150}$

</details>

---

## 🔑 Resumen

| Concepto | Símbolo | Fórmula | Significado |
|----------|---------|---------|-------------|
| **Frec. Acumulada Absoluta** | $F_i$ (o $N_i$) | $\sum f_i$ | Total de datos **hasta** ese punto. |
| **Frec. Acumulada Relativa** | $H_i$ (o $F_r$) | $F_i / n$ | Proporción de datos **hasta** ese punto. |
| **Sumatoria** | $\sum$ | - | La acumulada final siempre debe ser igual a $n$ (total). |

> **Conclusión:** La frecuencia acumulada es la herramienta para entender la posición relativa de los datos, permitiéndonos ver "cuántos hay debajo" de cierto límite.
