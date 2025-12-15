# Covarianza

El diagrama de dispersión nos muestra visualmente si hay relación entre dos variables. La **covarianza** nos da un número que mide esa relación: positivo si suben juntas, negativo si van en direcciones opuestas.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la covarianza y qué mide
- Cómo calcularla paso a paso
- Cómo interpretar su signo
- Sus limitaciones

---

## 📖 ¿Qué es la Covarianza?

> La **covarianza** mide cómo **varían juntas** dos variables. Indica si cuando una variable está por encima de su media, la otra también tiende a estarlo.

### 💡 Interpretación del signo:

| Signo | Significado |
|-------|-------------|
| $Cov(X,Y) > 0$ | Relación positiva: suben y bajan juntas |
| $Cov(X,Y) < 0$ | Relación negativa: una sube cuando la otra baja |
| $Cov(X,Y) \approx 0$ | Sin relación lineal |

---

## 📖 Fórmula de la Covarianza

### 💡 Covarianza poblacional:

$$
\sigma_{XY} = \frac{\sum_{i=1}^{N} (x_i - \mu_X)(y_i - \mu_Y)}{N}
$$

### 💡 Covarianza muestral:

$$
s_{XY} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{n-1}
$$

### 💡 Fórmula alternativa (computacional):

$$
s_{XY} = \frac{\sum x_i y_i - \frac{(\sum x_i)(\sum y_i)}{n}}{n-1}
$$

---

## 📖 Cálculo Paso a Paso

### ⚙️ Ejemplo: Horas de estudio vs Nota

| Estudiante | X (Horas) | Y (Nota) |
|------------|-----------|----------|
| 1 | 2 | 50 |
| 2 | 4 | 70 |
| 3 | 3 | 60 |
| 4 | 5 | 80 |
| 5 | 6 | 85 |

**Paso 1: Calcular las medias**

$$
\bar{x} = \frac{2+4+3+5+6}{5} = \frac{20}{5} = 4
$$

$$
\bar{y} = \frac{50+70+60+80+85}{5} = \frac{345}{5} = 69
$$

**Paso 2: Calcular las desviaciones y sus productos**

| $x_i$ | $y_i$ | $x_i - \bar{x}$ | $y_i - \bar{y}$ | $(x_i - \bar{x})(y_i - \bar{y})$ |
|-------|-------|-----------------|-----------------|----------------------------------|
| 2 | 50 | -2 | -19 | 38 |
| 4 | 70 | 0 | 1 | 0 |
| 3 | 60 | -1 | -9 | 9 |
| 5 | 80 | 1 | 11 | 11 |
| 6 | 85 | 2 | 16 | 32 |
| | | | **Suma** | **90** |

**Paso 3: Calcular la covarianza**

$$
s_{XY} = \frac{90}{5-1} = \frac{90}{4} = 22.5
$$

**Interpretación:** La covarianza es **positiva** (22.5), lo que indica que más horas de estudio se asocian con notas más altas.

---

## 📖 Interpretación Geométrica

### 💡 ¿Qué mide cada producto $(x_i - \bar{x})(y_i - \bar{y})$?

Dividimos el plano en 4 cuadrantes alrededor del punto $(\bar{x}, \bar{y})$:

```
           (-)(+)  │  (+)(+)
         Cuadrante II │ Cuadrante I
                      │
    ──────────────────┼────────────────
                      │
         Cuadrante III│ Cuadrante IV
           (-)(-)    │  (+)(-)
```

- **Cuadrante I:** X alto, Y alto → producto **positivo**
- **Cuadrante II:** X bajo, Y alto → producto **negativo**
- **Cuadrante III:** X bajo, Y bajo → producto **positivo**
- **Cuadrante IV:** X alto, Y bajo → producto **negativo**

**Covarianza positiva:** Mayoría de puntos en cuadrantes I y III
**Covarianza negativa:** Mayoría de puntos en cuadrantes II y IV

---

## ⚠️ Limitación de la Covarianza

### El problema de las unidades

La covarianza depende de las **unidades de medida**.

### ⚙️ Ejemplo:

- Covarianza (horas, nota) = 22.5
- Si medimos en **minutos** en lugar de horas: Covarianza = 22.5 × 60 = 1350

**El mismo fenómeno da números muy diferentes.**

### 💡 Solución:

Usar el **coeficiente de correlación** (próxima lección), que estandariza la covarianza.

---

## 📖 Covarianza = 0

Si $Cov(X,Y) = 0$, las variables **no tienen relación lineal**.

### ⚠️ Cuidado:

- $Cov = 0$ no significa que no haya **ninguna** relación
- Podría haber una relación **curvilínea**

### ⚙️ Ejemplo:

```
    Y │    ●
      │  ●   ●
      │●       ●
      └──────────→ X
```

Esta parábola tiene $Cov \approx 0$ pero claramente hay una relación (curva).

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Covarianza** | Mide cómo varían juntas X e Y |
| **Positiva** | X e Y aumentan/disminuyen juntas |
| **Negativa** | Una aumenta cuando la otra disminuye |
| **Cero** | Sin relación lineal |
| **Limitación** | Depende de las unidades |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la covarianza para estos datos:

| X | Y |
|---|---|
| 1 | 5 |
| 2 | 4 |
| 3 | 3 |
| 4 | 2 |
| 5 | 1 |

<details>
<summary>Ver solución</summary>

**Paso 1: Medias**
$\bar{x} = \frac{15}{5} = 3$
$\bar{y} = \frac{15}{5} = 3$

**Paso 2: Desviaciones y productos**

| $x_i$ | $y_i$ | $x_i - 3$ | $y_i - 3$ | Producto |
|-------|-------|-----------|-----------|----------|
| 1 | 5 | -2 | 2 | -4 |
| 2 | 4 | -1 | 1 | -1 |
| 3 | 3 | 0 | 0 | 0 |
| 4 | 2 | 1 | -1 | -1 |
| 5 | 1 | 2 | -2 | -4 |
| | | | **Suma** | **-10** |

**Paso 3: Covarianza**
$s_{XY} = \frac{-10}{4} = -2.5$

**Interpretación:** Covarianza negativa. Cuando X aumenta, Y disminuye.

</details>

### Ejercicio 2
¿Qué indica una covarianza de -150 entre edad y reflejos?

<details>
<summary>Ver solución</summary>

La covarianza **negativa** (-150) indica:

- **Relación inversa:** A mayor edad, menores reflejos (o viceversa)
- Cuando la edad está por encima de su media, los reflejos tienden a estar por debajo de su media

**Interpretación práctica:** Las personas mayores tienden a tener reflejos más lentos.

**Nota:** El valor -150 en sí no nos dice qué tan fuerte es la relación (por el problema de las unidades). Para eso necesitamos el coeficiente de correlación.

</details>

### Ejercicio 3
Si dos variables tienen covarianza positiva, ¿garantiza que cuando X aumente, Y siempre aumentará?

<details>
<summary>Ver solución</summary>

**No, no lo garantiza.**

Covarianza positiva significa que **en promedio** o **en general**, X e Y tienden a moverse juntas.

Pero puede haber excepciones individuales:
- Algunos puntos pueden estar en cuadrantes II o IV
- La relación describe la **tendencia**, no cada caso

**Ejemplo:** "Más educación se asocia con mayores ingresos" (covarianza positiva). Pero hay personas muy educadas con bajos ingresos y viceversa.

</details>

### Ejercicio 4
¿Por qué una covarianza de 0 no garantiza que las variables sean independientes?

<details>
<summary>Ver solución</summary>

$Cov = 0$ solo indica que no hay **relación lineal**.

**Puede haber otros tipos de relación:**

1. **Relación curvilínea:** Por ejemplo, $Y = X^2$
   - Puntos: (-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4)
   - Covarianza ≈ 0 porque los productos positivos y negativos se cancelan
   - Pero claramente Y depende de X

2. **Relación cíclica o periódica**

**Conclusión:** 
- $Cov \neq 0$ → Hay relación lineal
- $Cov = 0$ → No hay relación lineal (pero podría haber otra)

Para afirmar independencia, necesitamos más análisis.

</details>
