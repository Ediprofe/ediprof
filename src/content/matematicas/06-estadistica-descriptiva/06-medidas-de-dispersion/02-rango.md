# **El Rango**

Si te digo que la temperatura de hoy variará entre 10°C y 12°C, sabes qué ropa ponerte. Si te digo que variará entre -10°C y 40°C, estás en problemas. Esa "distancia" entre el extremo más bajo y el más alto es el **Rango**. Es la medida de dispersión más primitiva, pero también la más rápida de calcular.

---

## 🎯 ¿Qué vas a aprender?

- Calcular el Rango para datos sueltos ($R = Max - Min$).
- Estimar el Rango en tablas de frecuencias (Límite Superior - Límite Inferior).
- Entender por qué el Rango es extremadamente sensible (y a veces engañoso).
- Usarlo para una primera impresión rápida de la variabilidad.

---

## Cálculo con Datos Simples

$$ R = X_{max} - X_{min} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Temperaturas diurnas
**Datos:** 20, 22, 25, 21.
- Max: 25. Min: 20.
- Rango: $25 - 20 = \boxed{5}$

#### Ejemplo 2: Notas (0 a 10)
**Datos:** 1, 5, 8, 10.
- Max: 10. Min: 1.
- Rango: $10 - 1 = \boxed{9}$

#### Ejemplo 3: Con Negativos
**Datos:** -5, 0, 5, 10.
- Max: 10. Min: -5.
- Rango: $10 - (-5) = 10 + 5 = \boxed{15}$

#### Ejemplo 4: Datos Constantes
**Datos:** 8, 8, 8, 8.
- Max: 8. Min: 8.
- Rango: $8 - 8 = \boxed{0}$ (Sin dispersión).

#### Ejemplo 5: Edad en una fiesta familiar
**Datos:** Bebé (1 año), Abuelo (90 años), Tío (40).
- Max: 90. Min: 1.
- Rango: $90 - 1 = \boxed{89}$

---

## Cálculo con Datos Agrupados

Usamos los límites de los intervalos extremos.
$$ R \approx L_{sup\_final} - L_{inf\_inicial} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Estaturas
**Clases:** [150-160], [160-170], [170-180].
- Límite final: 180.
- Límite inicial: 150.
- Rango: $180 - 150 = \boxed{30}$

#### Ejemplo 2: Edades (Límites abiertos)
**Clases:** [10-20), [20-30), [30-40).
- Asumimos el rango teórico cubierto.
- Rango: $40 - 10 = \boxed{30}$

#### Ejemplo 3: Tiempos de carrera
**Clases:** 0-10 min, 10-20 min.
- Rango: $20 - 0 = \boxed{20}$

#### Ejemplo 4: Salarios (Millones)
**Clases:** [1-2], [2-3], [3-5], [5-10].
- Rango: $10 - 1 = \boxed{9 \text{ Millones}}$

#### Ejemplo 5: Frecuencias cero
**Clases:** [0-10] (f=5), [10-20] (f=0), [20-30] (f=5).
- Aunque el centro esté vacío, el rango cubre todo el espectro observado.
- Rango: $30 - 0 = \boxed{30}$

---

## Limitaciones del Rango

El Rango solo ve los bordes y es ciego a lo que pasa en el medio.

### ⚙️ Ejemplos Resueltos: ¿Por qué falla?

#### Ejemplo 1: El Outlier Solitario
**Grupo A:** 5, 5, 5, 5, 5. ($R=0$).
**Grupo B:** 5, 5, 5, 5, 1000. ($R=995$).
**Análisis:** Un solo dato disparó la dispersión a niveles absurdos.

#### Ejemplo 2: Distribución Interna
**Grupo A:** 0, 0, 0, 10, 10, 10. ($R=10$).
**Grupo B:** 0, 2, 4, 6, 8, 10. ($R=10$).
**Análisis:** Tienen el mismo rango, pero B está mucho más distribuido. A está polarizado.

#### Ejemplo 3: Tamaño de la Muestra
**Pequeña:** 10 datos. Probable Rango pequeño.
**Gigante:** 1 millón de datos. Probable que aparezca un valor raro muy alto y uno muy bajo.
**Análisis:** El rango tiende a crecer con el tamaño de la muestra ($n$).

#### Ejemplo 4: Comparación injusta
**Clase A:** Todos sacaron 3.0, excepto un genio (5.0) y uno que faltó (0.0). $R=5.0$.
**Clase B:** Todos sacaron entre 2.0 y 4.0. $R=2.0$.
**Análisis:** La Clase A parece más dispersa, pero es solo por dos alumnos.

#### Ejemplo 5: Datos Abiertos
**Encuesta:** "¿Cuánto ganas? Menos de 1M, Entre 1-2M, **Más de 2M**".
**Análisis:** No podemos calcular el rango porque no tenemos un límite superior cerrado ("Más de 2M" es infinito).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Halla el rango de: 5, 10, 15, 20.

<details>
<summary>Ver solución</summary>

**Cálculo:** $20 - 5 = 15$.
**Resultado:** $\boxed{15}$

</details>

### Ejercicio 2
Si el dato mínimo es 50 y el rango es 40, ¿cuál es el dato máximo?

<details>
<summary>Ver solución</summary>

**Fórmula:** $Max = Min + R$.
**Cálculo:** $50 + 40 = 90$.
**Resultado:** $\boxed{90}$

</details>

### Ejercicio 3
Calcula el rango de temperaturas: -10°C, -5°C, 0°C, 2°C.

<details>
<summary>Ver solución</summary>

**Max:** 2. **Min:** -10.
**Resta:** $2 - (-10) = 12$.
**Resultado:** $\boxed{12}$

</details>

### Ejercicio 4
¿Qué rango es más preocupante para la presión arterial sistólica?
A: [110, 130]. B: [90, 180].

<details>
<summary>Ver solución</summary>

**Análisis:** B tiene mucha variabilidad (inestable).
**Resultado:** $\boxed{\text{B}}$

</details>

### Ejercicio 5
Calcula el rango para la tabla: [0-5], [5-10], [10-15].

<details>
<summary>Ver solución</summary>

**Sup:** 15. **Inf:** 0.
**Resultado:** $\boxed{15}$

</details>

### Ejercicio 6
Si todos los estudiantes sacan la misma nota, ¿cuál es el rango?

<details>
<summary>Ver solución</summary>

**Diff:** $X - X = 0$.
**Resultado:** $\boxed{0}$

</details>

### Ejercicio 7
Tienes el rango [10, 50]. Si eliminas el 50 y el nuevo máximo es 40, ¿qué pasa con el rango?

<details>
<summary>Ver solución</summary>

**Antes:** 40. **Ahora:** $40-10=30$.
**Resultado:** $\boxed{\text{Disminuye}}$

</details>

### Ejercicio 8
¿Es posible tener un rango negativo?

<details>
<summary>Ver solución</summary>

**Teoría:** No, porque Max $\ge$ Min.
**Resultado:** $\boxed{\text{Falso}}$

</details>

### Ejercicio 9
Si multiplicas todos los datos por 2, ¿qué le pasa al rango?

<details>
<summary>Ver solución</summary>

**Prueba:** [2, 4] (R=2) $\to$ [4, 8] (R=4).
**Resultado:** $\boxed{\text{Se duplica}}$

</details>

### Ejercicio 10
¿El rango se ve afectado si sumas 100 a todos los datos?

<details>
<summary>Ver solución</summary>

**Prueba:** [2, 4] (R=2) $\to$ [102, 104] (R=2).
**Resultado:** $\boxed{\text{No cambia}}$

</details>

---

## 🔑 Resumen

| Estadístico | Fórmula | Ventaja | Desventaja |
|-------------|---------|---------|------------|
| **Rango ($R$)** | $X_{max} - X_{min}$ | Cálculo mental instantáneo. | Ignora el 99% de los datos. Muy sensible a outliers. |

> **Conclusión:** El Rango es como juzgar un libro por su portada y contraportada. Te dice qué tan grueso es, pero no qué dice en medio. Úsalo con precaución.
