# Coeficiente de Correlación

La covarianza nos dice la dirección de la relación, pero no qué tan fuerte es (porque depende de las unidades). El **coeficiente de correlación de Pearson** soluciona esto: es un número entre -1 y 1 que mide tanto la dirección como la fuerza de la relación lineal.

---

## 🎯 ¿Qué vas a aprender?

- Qué es el coeficiente de correlación de Pearson
- Cómo calcularlo e interpretarlo
- El coeficiente de determinación (r²)
- Errores comunes de interpretación

---

## 📊 Escala del Coeficiente de Correlación

| Valor de r | Interpretación |
|------------|----------------|
| r = 1 | Correlación positiva perfecta |
| 0.7 ≤ r < 1 | Correlación positiva fuerte |
| 0.4 ≤ r < 0.7 | Correlación positiva moderada |
| 0 < r < 0.4 | Correlación positiva débil |
| r = 0 | Sin correlación lineal |
| -0.4 < r < 0 | Correlación negativa débil |
| -0.7 < r ≤ -0.4 | Correlación negativa moderada |
| -1 < r ≤ -0.7 | Correlación negativa fuerte |
| r = -1 | Correlación negativa perfecta |

---

## 📖 ¿Qué es el Coeficiente de Correlación?

> El **coeficiente de correlación de Pearson** ($r$) es una medida estandarizada de la relación lineal entre dos variables. Siempre está entre -1 y 1.

### 💡 Propiedades:

- $-1 \leq r \leq 1$
- No tiene unidades (es adimensional)
- El signo indica la dirección
- El valor absoluto indica la fuerza

---

## 📖 Fórmula del Coeficiente de Correlación

### 💡 Fórmula con covarianza:

$$
r = \frac{s_{XY}}{s_X \cdot s_Y} = \frac{Cov(X,Y)}{\sqrt{Var(X)} \cdot \sqrt{Var(Y)}}
$$

### 💡 Fórmula directa:

$$
r = \frac{n\sum x_i y_i - (\sum x_i)(\sum y_i)}{\sqrt{[n\sum x_i^2 - (\sum x_i)^2][n\sum y_i^2 - (\sum y_i)^2]}}
$$

---

## 📖 Cálculo Paso a Paso

### ⚙️ Ejemplo: Horas de estudio vs Nota

Retomemos los datos anteriores:

| $x_i$ | $y_i$ | $x_i^2$ | $y_i^2$ | $x_i y_i$ |
|-------|-------|---------|---------|-----------|
| 2 | 50 | 4 | 2500 | 100 |
| 4 | 70 | 16 | 4900 | 280 |
| 3 | 60 | 9 | 3600 | 180 |
| 5 | 80 | 25 | 6400 | 400 |
| 6 | 85 | 36 | 7225 | 510 |
| **Σ = 20** | **Σ = 345** | **Σ = 90** | **Σ = 24625** | **Σ = 1470** |

$n = 5$

**Aplicando la fórmula:**

**Numerador:**
$$
n\sum xy - (\sum x)(\sum y) = 5(1470) - (20)(345) = 7350 - 6900 = 450
$$

**Denominador:**
$$
\sqrt{[5(90) - 20^2][5(24625) - 345^2]}
$$
$$
= \sqrt{[450 - 400][123125 - 119025]}
$$
$$
= \sqrt{50 \times 4100} = \sqrt{205000} = 452.77
$$

**Coeficiente de correlación:**
$$
r = \frac{450}{452.77} = 0.994
$$

**Interpretación:** r = 0.994 indica una correlación **positiva muy fuerte**. Las horas de estudio y las notas están casi perfectamente relacionadas linealmente.

---

## 📖 Interpretación Visual

### r = 1: Correlación positiva perfecta
```
    ●
   ●
  ●
 ●
●
```
Todos los puntos en una línea recta ascendente.

### r = -1: Correlación negativa perfecta
```
●
 ●
  ●
   ●
    ●
```
Todos los puntos en una línea recta descendente.

### r = 0: Sin correlación lineal
```
  ●    ●
    ●
 ●      ●
   ●  ●
  ●    ●
```
Puntos dispersos aleatoriamente.

### r = 0.7: Correlación positiva fuerte (pero no perfecta)
```
      ●
     ●
    ● ●
   ●●
  ●●
 ●
```
Tendencia clara, pero con algo de dispersión.

---

## 📖 Coeficiente de Determinación (r²)

> El **coeficiente de determinación** ($r^2$) indica qué proporción de la variación en Y es "explicada" por X.

### 💡 Cálculo:

$$
r^2 = (r)^2
$$

### ⚙️ Ejemplo:

Si $r = 0.994$:
$$
r^2 = (0.994)^2 = 0.988 = 98.8\%
$$

**Interpretación:** El 98.8% de la variación en las notas puede explicarse por las horas de estudio.

### 💡 Escala de r²:

| Valor de r² | Interpretación |
|-------------|----------------|
| r² = 0 | X no explica nada de la variación en Y |
| r² = 0.5 | X explica el 50% de la variación en Y |
| r² = 1 | X explica toda la variación en Y |

---

## ⚠️ Errores Comunes

### Error 1: Correlación implica causalidad

**NUNCA** asumas que porque r es alto, X causa Y.

**Ejemplo:** r = 0.95 entre consumo de helados y ahogamientos. ¿Los helados causan ahogamientos? No. Ambos están relacionados con el verano.

### Error 2: r = 0 significa independencia

$r = 0$ significa que no hay relación **lineal**, pero puede haber relación curvilínea.

### Error 3: Solo mirar r sin graficar

**Siempre** haz el diagrama de dispersión primero. Un solo outlier puede distorsionar r completamente.

### Error 4: Comparar r de diferentes estudios

El valor de r depende del rango de datos. Un estudio con más variación puede mostrar r más alto para la misma relación real.

---

## 💡 Propiedades del Coeficiente de Correlación

1. **Adimensional:** No tiene unidades
2. **Simétrico:** $r_{XY} = r_{YX}$
3. **No afectado por transformaciones lineales:** Si cambiamos unidades, r no cambia
4. **Solo mide relación lineal:** No detecta relaciones curvilíneas

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **r (Pearson)** | Medida de correlación lineal entre -1 y 1 |
| **r positivo** | X e Y aumentan juntas |
| **r negativo** | Una aumenta, otra disminuye |
| **\|r\| cercano a 1** | Relación lineal fuerte |
| **r² (determinación)** | % de variación explicada |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si la covarianza entre X e Y es 28, $s_X = 4$ y $s_Y = 10$, calcula r.

<details>
<summary>Ver solución</summary>

$$r = \frac{s_{XY}}{s_X \cdot s_Y} = \frac{28}{4 \times 10} = \frac{28}{40} = 0.70$$

**r = 0.70** → Correlación positiva moderada-fuerte

</details>

### Ejercicio 2
Si r = -0.85 entre horas de TV y notas:
a) ¿Qué tipo de relación hay?
b) ¿Cuál es r²?
c) Interpreta r² en contexto.

<details>
<summary>Ver solución</summary>

a) **Correlación negativa fuerte.** Más horas de TV se asocian con menores notas.

b) **r² = (-0.85)² = 0.7225 = 72.25%**

c) **Interpretación:** El 72.25% de la variación en las notas puede "explicarse" por las horas de TV.

**Cuidado:** Esto no significa que la TV cause malas notas. Podría haber otras variables (dedicación al estudio, etc.).

</details>

### Ejercicio 3
¿Es posible que dos variables tengan r = 0 pero estén fuertemente relacionadas?

<details>
<summary>Ver solución</summary>

**Sí, es posible.**

r = 0 solo significa que no hay relación **lineal**.

**Ejemplo:** Si Y = X²

| X | Y |
|---|---|
| -2 | 4 |
| -1 | 1 |
| 0 | 0 |
| 1 | 1 |
| 2 | 4 |

Calculando r, obtenemos aproximadamente 0 porque:
- Cuando X es negativo, Y es alto
- Cuando X es 0, Y es bajo
- Cuando X es positivo, Y es alto

Los efectos se cancelan, dando r ≈ 0.

Pero claramente hay una relación: Y depende perfectamente de X (es $X^2$).

**Moraleja:** Siempre graficar primero.

</details>

### Ejercicio 4
¿Por qué r = 0.3 en un estudio médico podría ser muy importante, mientras que r = 0.3 en física podría considerarse muy bajo?

<details>
<summary>Ver solución</summary>

El contexto determina la importancia:

**En medicina:**
- El comportamiento humano tiene muchas variables no controlables
- Una correlación de 0.3 (9% de varianza explicada) podría representar vidas salvadas
- Si r = 0.3 entre ejercicio y reducción de enfermedades cardíacas, es significativo clínicamente

**En física:**
- Las leyes físicas son muy precisas
- Una correlación de 0.3 indicaría una medición muy mala o un modelo incorrecto
- Se esperan correlaciones cercanas a 1 para relaciones físicas conocidas

**Conclusión:** La interpretación de r depende de:
1. El campo de estudio
2. La complejidad del fenómeno
3. El propósito práctico del análisis

</details>
