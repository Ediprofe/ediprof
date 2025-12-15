# Diagrama de Caja (Box Plot)

El **diagrama de caja** (o box plot) es una representación visual poderosa que muestra los cuartiles, la mediana y los valores atípicos de un vistazo. Es una de las herramientas más útiles para resumir y comparar distribuciones.

---

## 🎯 ¿Qué vas a aprender?

- Qué es un diagrama de caja y qué partes tiene
- Cómo construirlo paso a paso
- Cómo interpretar la información que muestra
- Cómo detectar valores atípicos

---

## 📊 Partes del Diagrama de Caja

| Parte | Representa | Significado |
|-------|------------|-------------|
| **Línea central** | Mediana (Q2) | El 50% central |
| **Caja** | De Q1 a Q3 | El 50% central de los datos (IQR) |
| **Bigotes** | Rango sin outliers | Datos típicos |
| **Puntos aislados** | Outliers | Valores atípicos |

---

## 📖 Estructura del Diagrama de Caja

```
                 Valor mínimo        Valor máximo
                 (sin outliers)       (sin outliers)
                      │                     │
Outliers  ○     ├─────┼─────────────────────┼─────┤     ○  Outliers
bajos           │     │                     │     │        altos
                │     │                     │     │
           Bigote   Q1     Q2 (mediana)    Q3   Bigote
           inferior        │                    superior
                      └────────────┘
                           IQR
                       (50% central)
```

---

## 📖 Construcción del Diagrama de Caja

### Paso 1: Calcular las estadísticas

Necesitas:
- Q1 (primer cuartil)
- Q2 (mediana)
- Q3 (tercer cuartil)
- IQR = Q3 - Q1

### Paso 2: Calcular los límites para outliers

- Límite inferior: $Q_1 - 1.5 \times IQR$
- Límite superior: $Q_3 + 1.5 \times IQR$

### Paso 3: Identificar los bigotes

- **Bigote inferior:** Valor mínimo que NO es outlier
- **Bigote superior:** Valor máximo que NO es outlier

### Paso 4: Marcar outliers

Cualquier valor fuera de los límites se marca como punto aislado.

---

## ⚙️ Ejemplo Completo

### Datos: Tiempos de espera (minutos)

2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 15, 18, 35

**Paso 1: Estadísticas básicas**

n = 16 datos

- Q1 (posición 4.25): $\approx 6.25$
- Q2 (mediana, posición 8.5): $\frac{10+11}{2} = 10.5$
- Q3 (posición 12.75): $\approx 13.75$
- IQR = 13.75 - 6.25 = 7.5

**Paso 2: Límites para outliers**

- Inferior: $6.25 - 1.5(7.5) = 6.25 - 11.25 = -5$ (ningún dato menor)
- Superior: $13.75 + 1.5(7.5) = 13.75 + 11.25 = 25$

**Paso 3: Identificar outliers**

¿Hay valores > 25? Sí, el 35 es un **outlier superior**.

**Paso 4: Definir bigotes**

- Bigote inferior: valor mínimo = 2
- Bigote superior: máximo sin outlier = 18 (el 35 es outlier)

**Resumen para el gráfico:**

| Elemento | Valor |
|----------|-------|
| Bigote inferior | 2 |
| Q1 | 6.25 |
| Mediana (Q2) | 10.5 |
| Q3 | 13.75 |
| Bigote superior | 18 |
| Outlier | 35 |

---

## 📖 Interpretación del Diagrama de Caja

### 💡 Información que obtenemos:

| Característica | Cómo verla |
|----------------|------------|
| **Centro** | Posición de la línea mediana |
| **Dispersión** | Tamaño de la caja (IQR) |
| **Simetría** | ¿Mediana centrada en la caja? |
| **Outliers** | Puntos fuera de los bigotes |
| **Rango** | Extensión total (bigotes + outliers) |

### 💡 Simetría vs Sesgo:

**Distribución simétrica:**
```
        ├───┬───────┬───┤
            ↑
        Mediana centrada
```

**Sesgo a la derecha:**
```
    ├──┬─────────────────┤
       ↑
    Mediana cerca de Q1
```

**Sesgo a la izquierda:**
```
├─────────────────┬──┤
                  ↑
          Mediana cerca de Q3
```

---

## 📖 Comparación de Distribuciones

Una ventaja del diagrama de caja es comparar **varios grupos** lado a lado.

### ⚙️ Ejemplo: Notas de tres cursos

```
Curso A: ├────┬─────────┤     (7 a 9, mediana 8)
Curso B:   ├─┬───────────────┤   (6 a 10, mediana 7)
Curso C:       ├────┬────┤        (8 a 9, mediana 8.5)
         ─────────────────────────
         5    6    7    8    9    10
```

**Conclusiones:**
- **Curso C** tiene notas más altas y consistentes (caja pequeña)
- **Curso B** tiene más variabilidad (caja grande)
- **Curso A** está en el medio

---

## 📖 Los Cinco Números Resumen

El diagrama de caja visualiza el **resumen de cinco números**:

| Número | Significado |
|--------|-------------|
| Mínimo | Valor más bajo (sin outliers) |
| Q1 | Primer cuartil |
| Mediana | Segundo cuartil |
| Q3 | Tercer cuartil |
| Máximo | Valor más alto (sin outliers) |

---

## 💡 Ventajas del Diagrama de Caja

| Ventaja | Descripción |
|---------|-------------|
| **Compacto** | Resume mucha información en poco espacio |
| **Comparación fácil** | Varios grupos lado a lado |
| **Detecta outliers** | Los muestra claramente |
| **Muestra simetría** | Revela la forma de la distribución |
| **Resistente** | Basado en cuartiles, no en medias |

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Caja** | Desde Q1 hasta Q3 (contiene 50% de datos) |
| **Línea media** | La mediana (Q2) |
| **Bigotes** | Extensión hasta valores no atípicos |
| **Outliers** | Valores fuera de $Q \pm 1.5 \times IQR$ |
| **Uso principal** | Comparar distribuciones visualmente |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Dados: Q1 = 20, Q2 = 30, Q3 = 45, Mín = 5, Máx = 100

a) Calcula el IQR
b) Calcula los límites para outliers
c) ¿El valor 5 es outlier? ¿Y el 100?

<details>
<summary>Ver solución</summary>

a) **IQR:**
$IQR = Q_3 - Q_1 = 45 - 20 = 25$

b) **Límites:**
- Inferior: $20 - 1.5(25) = 20 - 37.5 = -17.5$
- Superior: $45 + 1.5(25) = 45 + 37.5 = 82.5$

c) **¿Son outliers?**
- 5: ¿5 < -17.5? No → **No es outlier**
- 100: ¿100 > 82.5? Sí → **Es outlier**

</details>

### Ejercicio 2
Observa este diagrama de caja y responde:

```
         ├────┬─────────┤     ○
         │    │         │
      ───┼────┼─────────┼─────────
        10   15        25       40
```

a) ¿Cuál es la mediana?
b) ¿Cuál es el IQR?
c) ¿Hay outliers? ¿Cuáles?
d) ¿La distribución es simétrica o sesgada?

<details>
<summary>Ver solución</summary>

a) **Mediana:** 15 (la línea vertical dentro de la caja)

b) **IQR:** 
Q1 ≈ 10, Q3 ≈ 25
$IQR = 25 - 10 = 15$

c) **Outliers:**
El punto en 40 es un outlier (está separado después del bigote)

d) **Sesgo:**
La mediana (15) está más cerca de Q1 (10) que de Q3 (25). La cola es más larga hacia la derecha.
**Distribución sesgada a la derecha (positiva)**

</details>

### Ejercicio 3
¿Por qué el diagrama de caja es mejor que solo reportar la media y desviación estándar para datos con outliers?

<details>
<summary>Ver solución</summary>

El diagrama de caja es mejor porque:

1. **Muestra los outliers explícitamente:** Los ves como puntos separados, no ocultos en un promedio.

2. **Usa medidas resistentes:** Cuartiles y mediana no se distorsionan con outliers (a diferencia de media y desviación estándar).

3. **Revela la forma:** Puedes ver si hay sesgo, cuánta dispersión hay, y dónde está el centro real.

4. **No oculta información:** La media "promedia" todo y puede dar una imagen incorrecta. El box plot muestra dónde realmente están los datos.

**Ejemplo:**
Datos: 10, 11, 12, 13, 14, 100

- Media: 26.7 (parece que el "centro" es 26.7)
- Box plot: Mediana ≈ 12.5, con un outlier visible en 100

El box plot muestra claramente que la mayoría de datos está entre 10-14, con un dato anómalo.

</details>

### Ejercicio 4
¿Qué significa si una caja es muy larga comparada con otra?

<details>
<summary>Ver solución</summary>

Una **caja más larga** significa:

- **Mayor IQR (rango intercuartílico)**
- **Mayor variabilidad** en el 50% central de los datos
- Los datos están **más dispersos**

**Comparación:**

```
Grupo A: ├─┬─┤         (caja pequeña = datos homogéneos)
Grupo B: ├────────┬────────┤  (caja grande = datos heterogéneos)
```

Aunque ambos grupos podrían tener la misma mediana, el Grupo B tiene mucha más variabilidad que el Grupo A.

</details>
