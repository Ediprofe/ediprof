# Desviación Estándar

La varianza tiene un problema: sus unidades están al cuadrado. Si medimos estaturas en cm, la varianza está en cm². Para volver a las unidades originales, usamos la **desviación estándar**: la medida de dispersión más usada en la práctica.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la desviación estándar y cómo calcularla
- Por qué es preferida sobre la varianza
- Cómo interpretarla en contexto
- La regla empírica para distribuciones normales

---

## 📊 Fórmulas de la Desviación Estándar

| Tipo | Símbolo | Fórmula |
|------|---------|---------|
| **Poblacional** | $\sigma$ | $\sigma = \sqrt{\sigma^2} = \sqrt{\frac{\sum (x_i - \mu)^2}{N}}$ |
| **Muestral** | $s$ | $s = \sqrt{s^2} = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}}$ |

---

## 📖 ¿Qué es la Desviación Estándar?

> La **desviación estándar** es la **raíz cuadrada** de la varianza. Representa la dispersión típica de los datos respecto a la media.

### 💡 Ventaja principal:

$$
\text{Desviación estándar tiene las MISMAS UNIDADES que los datos}
$$

- Si los datos están en cm → la desviación estándar está en cm
- Si los datos están en pesos → la desviación estándar está en pesos

---

## 📖 Cálculo de la Desviación Estándar

### ⚙️ Ejemplo: Estaturas de 6 estudiantes

Datos: 160, 165, 170, 175, 180, 190 cm

Ya calculamos antes que $s^2 = 116.67$ cm²

**Desviación estándar:**
$$
s = \sqrt{116.67} = 10.80 \text{ cm}
$$

**Interpretación:** Las estaturas se desvían, en promedio, aproximadamente **10.8 cm** de la media (173.3 cm).

---

## 📖 Interpretación de la Desviación Estándar

### 💡 ¿Qué significa en términos prácticos?

La desviación estándar nos dice "qué tan lejos" están típicamente los datos de la media.

### ⚙️ Ejemplo comparativo:

**Clase A:** Media = 7, $s = 0.5$
**Clase B:** Media = 7, $s = 2.5$

| Clase | Interpretación |
|-------|----------------|
| A | Las notas están típicamente a 0.5 puntos de 7 (entre 6.5 y 7.5) |
| B | Las notas están típicamente a 2.5 puntos de 7 (entre 4.5 y 9.5) |

La Clase B tiene **5 veces más variabilidad** que la Clase A.

---

## 📖 La Regla Empírica (68-95-99.7)

Para distribuciones **aproximadamente normales** (en forma de campana):

| Intervalo | Porcentaje de datos |
|-----------|---------------------|
| $\bar{x} \pm 1s$ | Aproximadamente **68%** |
| $\bar{x} \pm 2s$ | Aproximadamente **95%** |
| $\bar{x} \pm 3s$ | Aproximadamente **99.7%** |

### ⚙️ Ejemplo:

Si la estatura media es 170 cm con $s = 10$ cm:

| Intervalo | Rango | % esperado |
|-----------|-------|------------|
| $170 \pm 10$ | 160 - 180 cm | 68% |
| $170 \pm 20$ | 150 - 190 cm | 95% |
| $170 \pm 30$ | 140 - 200 cm | 99.7% |

**Interpretación:**
- El 68% de las personas mide entre 160 y 180 cm
- Casi todos (95%) miden entre 150 y 190 cm
- Es muy raro (<0.3%) medir menos de 140 cm o más de 200 cm

---

## 📖 Comparación: Varianza vs Desviación Estándar

| Aspecto | Varianza ($s^2$) | Desviación Estándar ($s$) |
|---------|------------------|---------------------------|
| Fórmula | Promedio de cuadrados | Raíz de la varianza |
| Unidades | Cuadrado de originales | Mismas que originales |
| Interpretación directa | ❌ Difícil | ✅ Fácil |
| Uso matemático | ✅ Propiedades útiles | ⚠️ Menos propiedades |
| Uso en reportes | ❌ Menos común | ✅ Muy común |

---

## 📖 Desviación Estándar con Datos Agrupados

Para tablas de frecuencias:

$$
s = \sqrt{\frac{\sum f_i (x_i - \bar{x})^2}{n-1}}
$$

O simplemente: calcular la varianza y sacar la raíz.

### ⚙️ Ejemplo:

Si la varianza con datos agrupados es $s^2 = 25$, entonces:

$$
s = \sqrt{25} = 5
$$

---

## 💡 ¿Cuándo es "Alta" o "Baja"?

No hay un número mágico. Depende del contexto.

### ⚙️ Comparaciones útiles:

| Contexto | s = 5 es... |
|----------|-------------|
| Temperatura corporal (°C) | **Alta** (5°C de variación es mucho) |
| Precio de casas (millones) | **Baja** (5 millones de variación es poco) |
| Notas (escala 0-10) | **Moderada** |

### 💡 Regla práctica:

Usar el **coeficiente de variación** (próxima lección) para comparar dispersiones entre fenómenos diferentes.

---

## 📖 Cálculo Paso a Paso Completo

### ⚙️ Ejemplo: Horas de estudio diario

Datos: 2, 3, 3, 4, 4, 4, 5, 5, 6 horas (n = 9)

**Paso 1:** Media
$$
\bar{x} = \frac{2+3+3+4+4+4+5+5+6}{9} = \frac{36}{9} = 4
$$

**Paso 2:** Desviaciones al cuadrado

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
|-------|-----------------|---------------------|
| 2 | -2 | 4 |
| 3 | -1 | 1 |
| 3 | -1 | 1 |
| 4 | 0 | 0 |
| 4 | 0 | 0 |
| 4 | 0 | 0 |
| 5 | 1 | 1 |
| 5 | 1 | 1 |
| 6 | 2 | 4 |
| **Suma** | | **12** |

**Paso 3:** Varianza muestral
$$
s^2 = \frac{12}{9-1} = \frac{12}{8} = 1.5
$$

**Paso 4:** Desviación estándar
$$
s = \sqrt{1.5} = 1.22 \text{ horas}
$$

**Interpretación:** Los estudiantes estudian en promedio 4 horas, con una desviación típica de 1.22 horas.

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Desviación estándar** | $s = \sqrt{s^2}$ |
| **Unidades** | Las mismas que los datos originales |
| **Interpretación** | Dispersión típica respecto a la media |
| **Regla 68-95-99.7** | Para distribuciones normales |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si la varianza de un conjunto de datos es 36, ¿cuál es la desviación estándar?

<details>
<summary>Ver solución</summary>

$$s = \sqrt{s^2} = \sqrt{36} = 6$$

La desviación estándar es **6**.

</details>

### Ejercicio 2
Los pesos de 5 productos son: 98, 100, 102, 104, 106 gramos.
Calcula la desviación estándar muestral.

<details>
<summary>Ver solución</summary>

**Paso 1:** Media
$\bar{x} = \frac{510}{5} = 102$ g

**Paso 2:** Desviaciones al cuadrado

| $x_i$ | $(x_i - 102)^2$ |
|-------|-----------------|
| 98 | 16 |
| 100 | 4 |
| 102 | 0 |
| 104 | 4 |
| 106 | 16 |
| **Suma** | **40** |

**Paso 3:** Varianza
$s^2 = \frac{40}{4} = 10$

**Paso 4:** Desviación estándar
$s = \sqrt{10} = 3.16$ g

**Interpretación:** Los pesos se desvían típicamente 3.16 g de la media de 102 g.

</details>

### Ejercicio 3
Las notas de un examen tienen media 75 y desviación estándar 8. Suponiendo distribución normal, ¿entre qué valores está aproximadamente el 95% de los estudiantes?

<details>
<summary>Ver solución</summary>

Usando la regla empírica: 95% está en $\bar{x} \pm 2s$

$75 \pm 2(8) = 75 \pm 16$

**Intervalo:** [59, 91]

**El 95% de los estudiantes tiene notas entre 59 y 91.**

</details>

### Ejercicio 4
¿Por qué preferimos reportar la desviación estándar en lugar de la varianza?

<details>
<summary>Ver solución</summary>

Preferimos la desviación estándar porque:

1. **Mismas unidades:** Si medimos en cm, la desviación estándar está en cm. La varianza estaría en cm² (difícil de interpretar).

2. **Interpretación directa:** "Las estaturas varían típicamente 10 cm" es más claro que "la varianza es 100 cm²".

3. **Comparabilidad:** Podemos decir "la desviación estándar de estaturas es 10 cm y de pesos es 5 kg". Con varianza serían "100 cm² y 25 kg²", difíciles de comparar.

4. **Regla empírica:** Las reglas del 68-95-99.7 se expresan en términos de desviación estándar.

**Resumen:** La desviación estándar es más intuitiva y comunicable, aunque matemáticamente la varianza tiene propiedades más convenientes.

</details>
