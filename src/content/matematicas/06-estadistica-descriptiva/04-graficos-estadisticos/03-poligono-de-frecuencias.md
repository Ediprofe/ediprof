# Polígono de Frecuencias

El histograma es excelente para ver la distribución de datos. Pero ¿qué pasa si queremos **comparar dos distribuciones** en el mismo gráfico? Ahí es donde el **polígono de frecuencias** brilla.

---

## 🎯 ¿Qué vas a aprender?

- Qué es un polígono de frecuencias
- Cómo construirlo a partir de un histograma
- Cuándo es mejor que el histograma
- Cómo usarlo para comparar distribuciones

---

## 📖 ¿Qué es un Polígono de Frecuencias?

> El **polígono de frecuencias** es un gráfico de líneas que conecta los **puntos medios** (marcas de clase) de las barras de un histograma.

### 💡 Características:
- Cada punto representa el centro de una clase y su frecuencia
- Los puntos se conectan con líneas rectas
- Se "cierra" en los extremos para formar un polígono

---

## 📖 Construcción del Polígono de Frecuencias

### ⚙️ Ejemplo: Pesos de 40 estudiantes

Usemos la tabla de frecuencias:

| Clase | Intervalo | Marca de Clase ($x_i$) | f |
|-------|-----------|----------------------|---|
| 1 | 52 - 58 | 55 | 7 |
| 2 | 59 - 65 | 62 | 8 |
| 3 | 66 - 72 | 69 | 9 |
| 4 | 73 - 79 | 76 | 8 |
| 5 | 80 - 86 | 83 | 4 |
| 6 | 87 - 93 | 90 | 4 |

### Paso 1: Identificar los puntos

Cada punto tiene coordenadas $(x_i, f)$:

| Punto | $x_i$ (marca de clase) | f (frecuencia) |
|-------|----------------------|----------------|
| P1 | 55 | 7 |
| P2 | 62 | 8 |
| P3 | 69 | 9 |
| P4 | 76 | 8 |
| P5 | 83 | 4 |
| P6 | 90 | 4 |

### Paso 2: Agregar puntos de cierre

Para "cerrar" el polígono, agregamos puntos con frecuencia 0 en los extremos:

- **Punto inicial:** Una clase **antes** de la primera → $(48, 0)$
- **Punto final:** Una clase **después** de la última → $(97, 0)$

La distancia es igual a la amplitud de clase (7 en este caso).

### Paso 3: Conectar los puntos

Unir todos los puntos con líneas rectas:

$(48, 0) → (55, 7) → (62, 8) → (69, 9) → (76, 8) → (83, 4) → (90, 4) → (97, 0)$

---

## 📖 Relación con el Histograma

El polígono de frecuencias se puede construir **sobre** el histograma:

1. Dibujar el histograma
2. Marcar un punto en el **centro superior** de cada barra
3. Conectar los puntos
4. Extender las líneas a los extremos (eje X)

### 💡 El polígono y el histograma tienen la misma área

Cuando "cerramos" el polígono con el eje X, el área encerrada es **igual** al área total del histograma. Esto es porque lo que "perdemos" de las barras en un lado, lo "ganamos" en el otro.

---

## 📖 Ventajas del Polígono de Frecuencias

### ✅ Para comparar distribuciones

El polígono permite poner **varias distribuciones en el mismo gráfico** sin que se tape una a otra.

### ⚙️ Ejemplo: Comparar notas de dos grupos

**Grupo A:**
| $x_i$ | f |
|-------|---|
| 3 | 2 |
| 5 | 5 |
| 7 | 10 |
| 9 | 3 |

**Grupo B:**
| $x_i$ | f |
|-------|---|
| 3 | 1 |
| 5 | 3 |
| 7 | 8 |
| 9 | 8 |

Con un histograma, las barras se taparían. Con polígonos de frecuencias, podemos ver ambas curvas claramente usando diferentes colores o estilos de línea.

### ✅ Para ver tendencias

El polígono muestra claramente:
- Dónde están los picos
- Cómo cambia la frecuencia
- La forma general de la distribución

### ✅ Es más limpio visualmente

Para presentaciones o informes, el polígono es menos "pesado" visualmente que el histograma.

---

## 📖 Polígono de Frecuencias Relativas

También podemos hacer el polígono con **frecuencias relativas** o porcentajes:

| $x_i$ | f | $f_r$ |
|-------|---|-------|
| 55 | 7 | 0.175 |
| 62 | 8 | 0.200 |
| 69 | 9 | 0.225 |
| 76 | 8 | 0.200 |
| 83 | 4 | 0.100 |
| 90 | 4 | 0.100 |

### 💡 ¿Cuándo usar frecuencias relativas?

Cuando comparas grupos de **diferente tamaño**:
- Grupo A tiene 40 personas
- Grupo B tiene 100 personas

Usar frecuencias absolutas no sería justo. Con frecuencias relativas (proporciones), la comparación es válida.

---

## 💡 Diferencias: Histograma vs Polígono

| Aspecto | Histograma | Polígono de Frecuencias |
|---------|------------|------------------------|
| Tipo de gráfico | Barras | Líneas |
| Mejor para | Ver UNA distribución | Comparar VARIAS distribuciones |
| Muestra | Frecuencia por clase | Tendencia de frecuencias |
| Espacio visual | Ocupa más espacio | Más compacto |
| Construcción | Directo desde la tabla | Requiere calcular marcas de clase |

---

## 📖 Curva de Frecuencias

Si tenemos **muchos datos** y **muchas clases pequeñas**, el polígono de frecuencias se aproxima a una **curva suave**.

Esta curva suave es importante porque:
- Representa la **distribución teórica** de los datos
- Es la base de conceptos como la **distribución normal** (campana de Gauss)
- Permite calcular probabilidades como áreas bajo la curva

### 💡 El caso límite

Imagina que:
1. El tamaño de la muestra crece (más y más datos)
2. La amplitud de clase disminuye (clases más pequeñas)

El polígono se vuelve cada vez más suave, hasta parecer una **curva continua**.

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Polígono de frecuencias** | Línea que une las marcas de clase |
| **Puntos del polígono** | $(x_i, f)$ para cada clase |
| **Cierre del polígono** | Extender a frecuencia 0 en los extremos |
| **Ventaja principal** | Permite comparar varias distribuciones |
| **Curva de frecuencias** | Límite suave del polígono con muchos datos |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Dada la siguiente tabla, identifica los puntos para construir el polígono de frecuencias:

| Intervalo | $x_i$ | f |
|-----------|-------|---|
| 10 - 19 | 14.5 | 5 |
| 20 - 29 | 24.5 | 12 |
| 30 - 39 | 34.5 | 18 |
| 40 - 49 | 44.5 | 10 |
| 50 - 59 | 54.5 | 5 |

a) Lista los puntos del polígono (incluyendo los de cierre)
b) ¿Cuál es la amplitud de clase?
c) ¿Cuáles son las coordenadas de los puntos de cierre?

<details>
<summary>Ver solución</summary>

a) **Puntos del polígono:**
1. (4.5, 0) - punto de cierre inicial
2. (14.5, 5)
3. (24.5, 12)
4. (34.5, 18)
5. (44.5, 10)
6. (54.5, 5)
7. (64.5, 0) - punto de cierre final

b) **Amplitud de clase:** 
$10$ (de 10 a 19 hay 10 unidades)

c) **Puntos de cierre:**
- Inicial: $14.5 - 10 = 4.5$ → (4.5, 0)
- Final: $54.5 + 10 = 64.5$ → (64.5, 0)

</details>

### Ejercicio 2
¿Por qué el polígono de frecuencias es mejor que el histograma para comparar las edades de empleados de dos empresas diferentes?

<details>
<summary>Ver solución</summary>

El polígono es mejor porque:

1. **No se tapan:** Con histogramas, las barras de una empresa taparían las de la otra. Con polígonos, las líneas se pueden ver claramente usando colores diferentes.

2. **Comparación directa:** Es fácil ver dónde un grupo tiene más o menos frecuencia que el otro:
   - Donde una línea está arriba, ese grupo tiene más empleados en esa edad
   - Donde se cruzan, tienen frecuencias iguales

3. **Diferentes tamaños:** Si una empresa tiene 100 empleados y otra 500, podemos usar frecuencias relativas y comparar válidamente.

4. **Visualmente limpio:** Dos líneas son más fáciles de interpretar que barras superpuestas o lado a lado.

</details>

### Ejercicio 3
Un polígono de frecuencias tiene estos puntos:
(15, 0), (25, 8), (35, 15), (45, 15), (55, 7), (65, 5), (75, 0)

a) ¿Cuántas clases hay en la distribución?
b) ¿Cuál es la moda (clase modal)?
c) ¿La distribución parece simétrica o sesgada?

<details>
<summary>Ver solución</summary>

a) **Número de clases:** 5
(sin contar los puntos de cierre en 15 y 75)
- Clases: 20-30, 30-40, 40-50, 50-60, 60-70

b) **Clase modal:** 
Hay dos clases con la misma frecuencia máxima (15):
- 30-40 ($x_i = 35$)
- 40-50 ($x_i = 45$)
Es una distribución **bimodal** o tiene una meseta.

c) **Forma de la distribución:**
Ligeramente sesgada a la derecha (positiva)
- El pico está hacia la izquierda-centro
- La cola es más larga hacia la derecha (55, 7) y (65, 5)
- La subida es más pronunciada que la bajada

</details>

### Ejercicio 4
Explica por qué usamos frecuencias relativas en lugar de absolutas cuando comparamos distribuciones de grupos de diferente tamaño.

<details>
<summary>Ver solución</summary>

Usamos **frecuencias relativas** porque permiten una comparación **justa**:

**Ejemplo:**
- Grupo A: 40 personas, 10 tienen cierta característica → f = 10
- Grupo B: 100 personas, 10 tienen esa característica → f = 10

Con frecuencia **absoluta**: Ambos grupos tienen f = 10. Parecen iguales.

Con frecuencia **relativa**:
- Grupo A: $f_r = 10/40 = 0.25 = 25\%$
- Grupo B: $f_r = 10/100 = 0.10 = 10\%$

La realidad es que en el Grupo A, una **proporción mucho mayor** (25%) tiene esa característica, comparado con el Grupo B (10%).

**Conclusión:** Las frecuencias relativas normalizan los datos, permitiendo comparar grupos sin importar cuántos miembros tenga cada uno.

</details>
