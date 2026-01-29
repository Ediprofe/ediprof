# Introducción a la Inferencia Estadística

Hasta ahora hemos descrito datos (estadística descriptiva) y calculado probabilidades. Ahora damos el salto más importante: **inferir** características de una **población** a partir de una **muestra**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la inferencia estadística
- Diferencia entre parámetros y estadísticos
- Concepto de distribución muestral
- Tipos de inferencia: estimación e hipótesis

---

## 📖 ¿Qué es la Inferencia Estadística?

> La **inferencia estadística** es el proceso de usar datos de una **muestra** para hacer conclusiones sobre una **población**.

### 💡 El problema fundamental:

- Queremos conocer algo sobre la **población** (todos)
- Solo tenemos acceso a una **muestra** (algunos)
- ¿Cómo generalizar de la muestra a la población?

### ⚙️ Ejemplo:

- **Población:** Todos los 50 millones de colombianos
- **Pregunta:** ¿Qué porcentaje aprueba al presidente?
- **Muestra:** Encuesta a 1,200 personas
- **Inferencia:** Usar el resultado de la muestra para estimar el valor poblacional

---

## 📖 Parámetros vs Estadísticos

| Concepto | Descripción | Notación |
|----------|-------------|----------|
| **Parámetro** | Valor fijo de la **población** (desconocido) | μ, σ, p |
| **Estadístico** | Valor calculado de la **muestra** | $\bar{x}$, s, $\hat{p}$ |

### 💡 Objetivo:

Usar el estadístico para **estimar** el parámetro.

| Parámetro | Estadístico |
|-----------|-------------|
| μ (media poblacional) | $\bar{x}$ (media muestral) |
| σ (desv. estándar poblacional) | s (desv. estándar muestral) |
| p (proporción poblacional) | $\hat{p}$ (proporción muestral) |

---

## 📖 Distribución Muestral

> La **distribución muestral** de un estadístico es la distribución de todos los valores posibles de ese estadístico si tomáramos muchas muestras.

### 💡 Idea clave:

Si tomaras 1000 muestras diferentes de la misma población, cada una te daría una media $\bar{x}$ diferente. La distribución de esas 1000 medias es la distribución muestral.

### 💡 Distribución muestral de la media:

Si tomamos muestras de tamaño n de una población con media μ y desviación σ:

$$
\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)
$$

### 💡 Error estándar:

$$
SE = \frac{\sigma}{\sqrt{n}}
$$

Es la desviación estándar de la distribución muestral (cuánto varían las medias muestrales).

---

## 📖 Tipos de Inferencia

### 💡 Estimación puntual:

Dar un solo valor como estimación del parámetro.

Ejemplo: "La media poblacional es aproximadamente 175 cm"

### 💡 Estimación por intervalos:

Dar un rango de valores probables.

Ejemplo: "La media poblacional está entre 173 y 177 cm con 95% de confianza"

### 💡 Pruebas de hipótesis:

Evaluar afirmaciones sobre parámetros.

Ejemplo: "¿Es la media poblacional igual a 180 cm?"

---

## 📖 Intervalos de Confianza

> Un **intervalo de confianza** es un rango de valores que, con cierto nivel de confianza, contiene el parámetro poblacional.

### 💡 Fórmula general para la media:

$$
\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
$$

### 💡 Valores críticos comunes:

| Confianza | $z_{\alpha/2}$ |
|-----------|----------------|
| 90% | 1.645 |
| 95% | 1.960 |
| 99% | 2.576 |

### ⚙️ Ejemplo:

Una muestra de 100 personas tiene $\bar{x} = 172$ cm y σ = 10 cm.

Intervalo de 95% de confianza:

$$
172 \pm 1.96 \times \frac{10}{\sqrt{100}} = 172 \pm 1.96 = [170.04, 173.96]
$$

"Con 95% de confianza, la media poblacional está entre 170 y 174 cm."

---

## 📖 Introducción a Pruebas de Hipótesis

### 💡 Estructura:

1. **Hipótesis nula (H₀):** Lo que asumimos verdadero (status quo)
2. **Hipótesis alternativa (H₁):** Lo que queremos demostrar
3. **Estadístico de prueba:** Mide la evidencia contra H₀
4. **Valor p:** Probabilidad de obtener resultados tan extremos si H₀ es verdadera
5. **Decisión:** Si valor p < α, rechazamos H₀

### ⚙️ Ejemplo simplificado:

- **H₀:** La media de estaturas es 170 cm
- **H₁:** La media es diferente de 170 cm
- **Datos:** n = 100, $\bar{x}$ = 173, σ = 10
- **Estadístico:** $z = \frac{173 - 170}{10/\sqrt{100}} = 3$
- **Valor p:** P(|Z| > 3) ≈ 0.0027
- **Decisión:** Como 0.0027 < 0.05, rechazamos H₀

---

## 📖 Errores en Inferencia

| Error | Descripción | Probabilidad |
|-------|-------------|--------------|
| **Tipo I** | Rechazar H₀ cuando es verdadera | α |
| **Tipo II** | No rechazar H₀ cuando es falsa | β |

### 💡 Analogía judicial:

- Error Tipo I = Condenar a un inocente
- Error Tipo II = Absolver a un culpable

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Inferencia** | Conclusiones de muestra a población |
| **Parámetro** | Valor poblacional (desconocido) |
| **Estadístico** | Valor muestral (calculado) |
| **IC** | Rango de valores probables para el parámetro |
| **Prueba de hipótesis** | Evaluar afirmaciones sobre parámetros |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
¿Por qué el error estándar disminuye cuando n aumenta?

<details>
<summary>Ver solución</summary>

$SE = \frac{\sigma}{\sqrt{n}}$

Al aumentar n:
- El denominador $\sqrt{n}$ aumenta
- El SE disminuye

**Interpretación:** Con muestras más grandes, las medias muestrales están más cercanas a la media poblacional (menos variabilidad entre muestras).

Ejemplo numérico:
- n = 25: SE = σ/5
- n = 100: SE = σ/10
- n = 400: SE = σ/20

</details>

### Ejercicio 2
Si el intervalo de confianza del 95% para μ es [42, 48], ¿podemos afirmar con 95% de certeza que μ está en ese intervalo?

<details>
<summary>Ver solución</summary>

**Interpretación correcta:**
Si repitiéramos el muestreo muchas veces, el 95% de los intervalos calculados contendrían μ.

**Interpretación incorrecta:**
NO significa que hay 95% de probabilidad de que μ esté en [42, 48].

μ es un valor fijo (aunque desconocido). O está en el intervalo o no está. El 95% se refiere a la confiabilidad del **método**, no a la probabilidad de este intervalo específico.

</details>

### Ejercicio 3
¿Cuál es la diferencia entre σ y el error estándar?

<details>
<summary>Ver solución</summary>

**σ (desviación estándar poblacional):**
- Mide la variabilidad de los **datos individuales** en la población
- No cambia con el tamaño de la muestra

**SE (error estándar):**
- Mide la variabilidad de las **medias muestrales**
- $SE = \sigma/\sqrt{n}$
- Disminuye con n más grande

**Ejemplo:**
Si σ = 10 y n = 25:
- Los datos individuales varían típicamente 10 unidades de μ
- Las medias muestrales varían típicamente 10/5 = 2 unidades de μ

</details>
