# Muestreo y Error Muestral

El éxito de la inferencia depende de tener una **buena muestra**. En esta lección exploramos los conceptos fundamentales del muestreo y entendemos de dónde viene el error inherente a toda estimación.

---

## 🎯 ¿Qué vas a aprender?

- Por qué muestreamos y no censamos
- Tipos de muestreo (repaso)
- Qué es el error muestral y de dónde viene
- Cómo reducir el error

---

## 📖 ¿Por qué Muestrear?

| Razón | Descripción |
|-------|-------------|
| **Costo** | Medir a toda la población es muy caro |
| **Tiempo** | Un censo toma mucho tiempo |
| **Imposibilidad** | A veces la población es infinita o inaccesible |
| **Destructivo** | Algunas pruebas destruyen el objeto (control de calidad) |

### 💡 Meta:

Obtener una muestra **representativa** que nos permita hacer inferencias válidas sobre la población.

---

## 📖 Repaso: Tipos de Muestreo

### 💡 Muestreo probabilístico:

| Tipo | Descripción |
|------|-------------|
| **Aleatorio simple** | Cada elemento tiene igual probabilidad |
| **Estratificado** | División en grupos, muestreo dentro de cada grupo |
| **Por conglomerados** | Seleccionar grupos completos aleatoriamente |
| **Sistemático** | Cada k-ésimo elemento después de un inicio aleatorio |

### 💡 Muestreo no probabilístico:

| Tipo | Descripción |
|------|-------------|
| **Por conveniencia** | Los más accesibles |
| **Por cuotas** | Fijar proporciones de subgrupos |
| **Bola de nieve** | Referidos por participantes previos |

### ⚠️ Importante:

Solo el muestreo probabilístico permite calcular márgenes de error y hacer inferencia formal.

---

## 📖 Error Muestral

> El **error muestral** es la diferencia entre el estadístico muestral y el parámetro poblacional.

$$
\text{Error muestral} = \bar{x} - \mu
$$

### 💡 ¿Por qué existe el error?

Porque la muestra **no es** la población. Diferentes muestras darían diferentes resultados.

### 💡 Características:

| Característica | Descripción |
|----------------|-------------|
| **Inevitable** | Siempre hay algún error (a menos que midas a todos) |
| **Aleatorio** | Puede ser positivo o negativo |
| **Cuantificable** | Podemos estimar su magnitud probable |
| **Reducible** | Aumentando n |

---

## 📖 Error Estándar

> El **error estándar** mide la magnitud típica del error muestral.

### 💡 Para la media:

$$
SE_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
$$

### 💡 Para la proporción:

$$
SE_{\hat{p}} = \sqrt{\frac{p(1-p)}{n}}
$$

### ⚙️ Ejemplo:

Si σ = 10 y n = 100:
$$
SE = \frac{10}{\sqrt{100}} = 1
$$

Las medias muestrales típicamente estarán a 1 unidad de la media poblacional.

---

## 📖 Factores que Afectan el Error

| Factor | Efecto en el error |
|--------|-------------------|
| **n (tamaño de muestra)** | Mayor n → Menor error |
| **σ (variabilidad)** | Mayor σ → Mayor error |
| **Método de muestreo** | Mejor método → Menor sesgo |

### 💡 El error se reduce con √n:

| n | Error estándar (σ = 10) |
|---|------------------------|
| 25 | 2.00 |
| 100 | 1.00 |
| 400 | 0.50 |
| 1,600 | 0.25 |

Para reducir el error a la mitad, ¡hay que cuadruplicar n!

---

## 📖 Error Muestral vs Error Sistemático

| Tipo | Descripción | Solución |
|------|-------------|----------|
| **Error muestral** | Variabilidad aleatoria | Aumentar n |
| **Error sistemático (sesgo)** | Desviación consistente en una dirección | Cambiar el método |

### ⚙️ Ejemplo de sesgo:

Si encuestas por teléfono fijo, excluyes a quienes solo tienen celular. Esto introduce sesgo que **no** se reduce aumentando n.

---

## 📖 Margen de Error

> El **margen de error** es la cantidad que suma y resta del estadístico para crear un intervalo de confianza.

$$
ME = z_{\alpha/2} \times SE
$$

### ⚙️ Ejemplo para encuestas:

Si $\hat{p} = 0.52$ y n = 1000 con 95% de confianza:

$$
SE = \sqrt{\frac{0.52 \times 0.48}{1000}} = 0.0158
$$

$$
ME = 1.96 \times 0.0158 = 0.031 \approx 3\%
$$

Resultado: "52% ± 3%"

---

## 📖 Tamaño de Muestra Necesario

### 💡 Para estimar una media con error máximo E:

$$
n = \left(\frac{z_{\alpha/2} \cdot \sigma}{E}\right)^2
$$

### 💡 Para estimar una proporción con error máximo E:

$$
n = \frac{z_{\alpha/2}^2 \cdot p(1-p)}{E^2}
$$

Si p es desconocida, usar p = 0.5 (máxima variabilidad).

### ⚙️ Ejemplo:

Queremos estimar una proporción con error máximo de 3% y 95% de confianza:

$$
n = \frac{1.96^2 \times 0.5 \times 0.5}{0.03^2} = \frac{0.9604}{0.0009} = 1,067
$$

Necesitamos aproximadamente 1,067 personas.

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Error muestral** | Diferencia entre estadístico y parámetro |
| **Error estándar** | Magnitud típica del error |
| **SE para media** | $\sigma/\sqrt{n}$ |
| **Margen de error** | $z \times SE$ |
| **Reducir error** | Aumentar n (costo: cuadrático) |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Una encuesta de 400 personas tiene margen de error de ±5%. ¿Cuántas personas necesitarías para reducirlo a ±2.5%?

<details>
<summary>Ver solución</summary>

Para reducir el error a la mitad, hay que cuadruplicar n:

$n_{nuevo} = 4 \times 400 = 1,600$ personas

**Verificación:**
- Error original ∝ 1/√400 = 1/20
- Error nuevo ∝ 1/√1600 = 1/40
- Razón: (1/40)/(1/20) = 1/2 ✓

</details>

### Ejercicio 2
¿Por qué aumentar el tamaño de muestra no corrige un sesgo de selección?

<details>
<summary>Ver solución</summary>

El sesgo es un **error sistemático** que afecta a todos los datos de la misma manera.

**Ejemplo:** Si solo encuestas a personas en centros comerciales:
- Excluyes a quienes no van a centros comerciales
- Sobre-representas a ciertos grupos demográficos
- Este sesgo existe en cada persona encuestada

Aumentar de 100 a 1000 personas en centros comerciales solo te da una estimación más precisa del grupo **equivocado**.

**Solución:** Cambiar el método de muestreo para que sea más representativo de la población real.

</details>

### Ejercicio 3
Calcula el tamaño de muestra necesario para estimar la media de ingresos con error máximo de $50,000 y 95% de confianza, si σ ≈ $500,000.

<details>
<summary>Ver solución</summary>

$$n = \left(\frac{z \cdot \sigma}{E}\right)^2 = \left(\frac{1.96 \times 500,000}{50,000}\right)^2$$

$$= \left(\frac{980,000}{50,000}\right)^2 = (19.6)^2 = 384.16$$

**Necesitas al menos 385 personas.**

</details>
