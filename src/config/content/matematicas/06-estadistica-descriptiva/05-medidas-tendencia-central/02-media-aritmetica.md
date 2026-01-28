---
title: "Media Aritmética"
---

# **Media Aritmética**

Imagina que tú tienes 5 caramelos y tu amigo tiene 1. No es justo, ¿cierto? Si juntan todos los caramelos ($5+1=6$) y los reparten en partes iguales ($6 \div 2 = 3$), ahora ambos tienen 3. Ese "3" es la **media aritmética**. Es el valor que tendrían todos los datos si fueran **iguales** manteniendo el mismo total.

---

## 🎯 ¿Qué vas a aprender?

- Calcular la media ($\bar{x}$) para datos sueltos.
- Calcular la media usando tablas de frecuencia ($f_i$).
- Comprender las propiedades clave: centro de gravedad y sensibilidad.
- Resolver problemas de promedios ponderados implícitos.

---

## Cálculo con Datos Simples

La fórmula es intuitiva: suma todo y divide entre la cantidad.
$$ \bar{x} = \frac{\sum x_i}{n} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Notas de semestre
**Datos:** 3.0, 4.0, 5.0.
**Suma:** $3+4+5 = 12$.
**División:** $12 / 3 = 4.0$.
**Media:** $\boxed{4.0}$

#### Ejemplo 2: Goles en 4 partidos
**Datos:** 0, 0, 2, 6.
**Suma:** 8.
**División:** $8 / 4 = 2$.
**Media:** $\boxed{2 \text{ goles por partido}}$

#### Ejemplo 3: Temperatura (con negativos)
**Datos:** -2°C, 0°C, 5°C.
**Suma:** $-2 + 0 + 5 = 3$.
**División:** $3 / 3 = 1$.
**Media:** $\boxed{1^\circ\text{C}}$

#### Ejemplo 4: Edades (decimales)
**Datos:** 10.5, 11.5.
**Suma:** 22.
**División:** $22 / 2 = 11$.
**Media:** $\boxed{11 \text{ años}}$

#### Ejemplo 5: Dato constante
**Datos:** 5, 5, 5, 5.
**Suma:** 20.
**División:** $20 / 4 = 5$.
**Media:** $\boxed{5}$ (Si todos son iguales, la media es ese valor).

---

## Cálculo con Tablas de Frecuencia

Cuando los datos se repiten, no sumamos uno por uno (2+2+2...). Multiplicamos el valor por cuántas veces aparece ($2 \times 3$).
$$ \bar{x} = \frac{\sum (x_i \cdot f_i)}{n} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Encuesta de hijos
**Tabla:**
- 0 hijos: 3 familias ($0 \times 3 = 0$)
- 1 hijo: 5 familias ($1 \times 5 = 5$)
- 2 hijos: 2 familias ($2 \times 2 = 4$)
**Total Datos ($n$):** $3+5+2 = 10$.
**Suma Total:** $0+5+4 = 9$.
**Media:** $\boxed{0.9 \text{ hijos}}$

#### Ejemplo 2: Calificación de servicio (1 a 3)
**Tabla:**
- 1 estrella: 10 personas (10)
- 2 estrellas: 0 personas (0)
- 3 estrellas: 10 personas (30)
**Total ($n$):** 20.
**Suma:** 40.
**Media:** $40/20 = \boxed{2.0}$

#### Ejemplo 3: Edades en un grupo
**Tabla:**
- 15 años: 4 alumnos (60)
- 16 años: 6 alumnos (96)
**Total ($n$):** 10.
**Suma:** 156.
**Media:** $\boxed{15.6 \text{ años}}$

#### Ejemplo 4: Lanzamiento de moneda (Cara=1, Sello=0)
**Datos:** 3 Caras, 7 Sellos.
**Cálculo:** $(1\times3 + 0\times7) = 3$.
**Total:** 10 lanzamientos.
**Media:** $\boxed{0.3}$ (Indica proporción de caras).

#### Ejemplo 5: Salarios simplificados
**Tabla:**
- \$100: 2 personas (200)
- \$200: 8 personas (1600)
**Total:** 10 personas.
**Suma:** 1800.
**Media:** $\boxed{\$180}$

---

## Propiedades Importantes

1.  **Suma de desviaciones es Cero:** Si restas la media a cada dato y sumas esos resultados, siempre da 0.
2.  **Sensibilidad:** Un solo dato gigante arrastra la media hacia él.

### ⚙️ Ejemplos Resueltos: Propiedades

#### Ejemplo 1: Desviación Cero
**Datos:** 1, 2, 3. Media = 2.
**Restas:**
- $1 - 2 = -1$
- $2 - 2 = 0$
- $3 - 2 = 1$
**Suma:** $-1 + 0 + 1 = 0$. ¡Comprobado!

#### Ejemplo 2: El efecto millonario (Sensibilidad)
**Datos:** 1, 1, 1, 100.
**Media sin el 100:** 1.0.
**Media con el 100:** $103/4 = 25.75$.
**Lección:** Un dato cambió la media de 1 a 25. La media no es robusta.

#### Ejemplo 3: Cambio de escala (Suma)
**Situación:** La media de notas es 3.5. El profesor regala 0.5 a todos.
**Nueva Media:** $3.5 + 0.5 = 4.0$. (No necesitas recalcular todo).

#### Ejemplo 4: Cambio de escala (Multiplicación)
**Situación:** La media de sueldos es \$100. Se sube el sueldo un 10% (multiplicar por 1.1).
**Nueva Media:** $100 \times 1.1 = 110$.

#### Ejemplo 5: Media de Medias (Ponderada)
**Situación:** Salón A (20 alumnos, media 3.0). Salón B (30 alumnos, media 4.0).
**Error Común:** $(3+4)/2 = 3.5$. ¡Incorrecto! Son tamaños diferentes.
**Correcto:** $( (20\times3) + (30\times4) ) / 50 = (60+120)/50 = 3.6$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la media de: 12, 15, 18, 12, 13.

<details>
<summary>Ver solución</summary>

**Suma:** $12+15+18+12+13 = 70$.
**Cantidad:** 5.
**Cálculo:** $\frac{70}{5} = 14$.
**Resultado:** $\boxed{14}$

</details>

### Ejercicio 2
Si la suma de 10 datos es 450, ¿cuál es su media?

<details>
<summary>Ver solución</summary>

**Fórmula:** $\bar{x} = \text{Suma} / n$.
**Cálculo:** $450 / 10 = 45$.
**Resultado:** $\boxed{45}$

</details>

### Ejercicio 3
Tienes 4 notas: 3.0, 3.5, 4.0. ¿Qué nota necesitas en el cuarto examen para promediar 4.0?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Para promediar 4.0 en 4 notas, necesitas sumar $4 \times 4.0 = 16$.
**Suma actual:** $3.0 + 3.5 + 4.0 = 10.5$.
**Faltante:** $16 - 10.5 = 5.5$.
**Resultado:** $\boxed{5.5}$

</details>

### Ejercicio 4
Calcula la media de la tabla:
- $x=2, f=3$
- $x=4, f=2$

<details>
<summary>Ver solución</summary>

**Productos:** $2\times3=6$, $4\times2=8$.
**Suma Productos:** $6+8=14$.
**Total Datos:** $3+2=5$.
**Media:** $14/5 = 2.8$.
**Resultado:** $\boxed{2.8}$

</details>

### Ejercicio 5
Demuestra que la suma de desviaciones de 2, 4, 6 (Media=4) es cero.

<details>
<summary>Ver solución</summary>

**Desviaciones:** $(2-4)=-2$, $(4-4)=0$, $(6-4)=2$.
**Suma:** $-2+0+2 = 0$.
**Resultado:** $\boxed{0}$

</details>

### Ejercicio 6
Si multiplicas todos los datos originales por 3, ¿qué le pasa a la media?

<details>
<summary>Ver solución</summary>

**Propiedad:** Linealidad.
**Resultado:** $\boxed{\text{La media también se multiplica por 3}}$

</details>

### Ejercicio 7
Encuentra la media de: 100, 200, 300, 10000. ¿Representa bien a los datos?

<details>
<summary>Ver solución</summary>

**Cálculo:** $10600 / 4 = 2650$.
**Análisis:** 3 de los 4 datos son $\le 300$. El promedio 2650 está lejisimos de ellos.
**Resultado:** $\boxed{2650, \text{ No representa bien (sesgo)}}$

</details>

### Ejercicio 8
El promedio de edad de 3 personas es 20 años. Si se une una persona de 40 años, ¿cuál es el nuevo promedio?

<details>
<summary>Ver solución</summary>

**Suma original:** $3 \times 20 = 60$.
**Nueva suma:** $60 + 40 = 100$.
**Nuevo total ($n$):** 4.
**Media:** $100 / 4 = 25$.
**Resultado:** $\boxed{25 \text{ años}}$

</details>

### Ejercicio 9
Calcula la media de los primeros 5 números pares (2, 4, 6, 8, 10).

<details>
<summary>Ver solución</summary>

**Suma:** 30.
**Media:** $30/5 = 6$. (Nota: es justo el del medio por ser simétrico).
**Resultado:** $\boxed{6}$

</details>

### Ejercicio 10
Si en una empresa el salario medio hombres (10 personas) es \$1000 y mujeres (90 personas) es \$500. ¿Cuál es el promedio global?

<details>
<summary>Ver solución</summary>

**Ponderado:**
- Hombres: $10 \times 1000 = 10,000$.
- Mujeres: $90 \times 500 = 45,000$.
- Suma Global: 55,000.
- Total Personas: 100.
- Media: $55,000 / 100 = 550$.
**Resultado:** $\boxed{\$550}$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula | Clave |
|----------|---------|-------|
| **Media Simple** | $\bar{x} = \frac{\sum x}{n}$ | Repartición equitativa. |
| **Media Ponderada** | $\bar{x} = \frac{\sum (x \cdot f)}{n}$ | Usar con tablas de frecuencia. |
| **Outliers** | N/A | La media es "jalada" fuertemente por valores extremos. |

> **Conclusión:** La media es el centro de gravedad de los datos. Úsala cuando quieras repartir todo por igual, pero ten cuidado si hay "datos gigantes" que rompan el equilibrio.
