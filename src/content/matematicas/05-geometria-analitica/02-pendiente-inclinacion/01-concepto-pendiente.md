# Concepto de Pendiente

¿Por qué algunas calles son más empinadas que otras? ¿Cómo medimos qué tan "inclinada" está una rampa o una escalera? La respuesta está en un concepto fundamental de la geometría analítica: la **pendiente**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la pendiente de una recta
- Qué nos indica su valor
- Los casos especiales de pendiente

---

## 📖 Lo Esencial de la Pendiente

| Pendiente $m$ | Tipo de recta | Descripción |
|---------------|---------------|-------------|
| $m > 0$ | Ascendente ↗ | Sube de izquierda a derecha |
| $m < 0$ | Descendente ↘ | Baja de izquierda a derecha |
| $m = 0$ | Horizontal → | Paralela al eje X |
| $m$ no existe | Vertical ↑ | Paralela al eje Y |
| $\|m\| > 1$ | Empinada | Más vertical que horizontal |
| $\|m\| < 1$ | Suave | Más horizontal que vertical |
| $\|m\| = 1$ | 45° | Igual de inclinada |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/tipos-pendiente.svg" alt="Tipos de pendiente: positiva, negativa y horizontal" style="width: 100%; height: auto;" />
</div>

> 💡 **Observa:** La recta verde "sube" (pendiente positiva), la roja "baja" (negativa) y la azul es horizontal (pendiente cero).

---

## 📖 ¿Qué es la Pendiente?

> La **pendiente** de una recta mide su **inclinación** respecto a la horizontal. Nos dice cuánto "sube" o "baja" la recta por cada unidad que avanzamos hacia la derecha.

Matemáticamente:

$$
m = \frac{\text{cambio vertical}}{\text{cambio horizontal}} = \frac{\Delta y}{\Delta x} = \frac{\text{subida}}{\text{avance}}
$$

### La Pendiente en la Vida Real

La pendiente está en todas partes:

| Situación | Interpretación de la pendiente |
|-----------|-------------------------------|
| Carretera | El porcentaje de inclinación |
| Escalera | Relación altura/profundidad de los escalones |
| Rampa de silla de ruedas | Qué tan empinada es |
| Techo | La inclinación para que escurra el agua |
| Gráfica de velocidad | La aceleración |

> 💡 Cuando ves un letrero que dice "pendiente del 10%", significa que por cada 100 metros horizontales, subes 10 metros verticalmente.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/concepto-pendiente.svg" alt="Concepto de pendiente: subida/avance" style="width: 100%; height: auto;" />
</div>

> 💡 **Observa el triángulo:** La línea verde es el "avance" ($\Delta x = 1$) y la naranja es la "subida" ($\Delta y = 2$). La pendiente es $m = \frac{2}{1} = 2$.

---

## 📖 Interpretación del Signo de la Pendiente

El **signo** de la pendiente nos dice la dirección:

### Pendiente Positiva ($m > 0$)

La recta **sube** de izquierda a derecha.

**Ejemplo:** Si $m = 2$, por cada unidad que avanzamos a la derecha, subimos 2 unidades.

### Pendiente Negativa ($m < 0$)

La recta **baja** de izquierda a derecha.

**Ejemplo:** Si $m = -3$, por cada unidad que avanzamos a la derecha, bajamos 3 unidades.

### Pendiente Cero ($m = 0$)

La recta es **horizontal**, no sube ni baja.

Todas las rectas horizontales tienen pendiente $m = 0$.

### Pendiente No Definida (o infinita)

Las rectas **verticales** tienen pendiente **indefinida** porque el cambio horizontal es cero, y no podemos dividir entre cero.

---

## 📖 Interpretación del Valor Absoluto

El **valor absoluto** de la pendiente nos dice qué tan empinada es la recta:

| Valor de $\lvert m \rvert$ | Interpretación                   |
|--------------------------|-----------------------------------|
| $\lvert m \rvert < 1$    | Recta "suave", más horizontal     |
| $\lvert m \rvert = 1$    | Recta a 45°                       |
| $\lvert m \rvert > 1$    | Recta "empinada", más vertical    |

### ⚙️ Ejemplo 1: Comparar pendientes

¿Cuál recta es más empinada, una con $m = 2$ o una con $m = -5$?

**Análisis:**
- $|m_1| = |2| = 2$
- $|m_2| = |-5| = 5$

Como $5 > 2$, la recta con pendiente $m = -5$ es **más empinada**.

> 💡 El signo indica la dirección (sube o baja), pero el valor absoluto indica la inclinación.

### ⚙️ Ejemplo 2: Describir la pendiente

Describe qué tipo de recta tiene pendiente $m = -0.5$:

**Análisis:**
- $m < 0$ → La recta es **descendente** (baja de izquierda a derecha)
- $|m| = 0.5 < 1$ → La recta es **suave** (más horizontal que vertical)

**Respuesta:** Es una recta descendente con inclinación suave.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/pendiente-absoluto.svg" alt="Comparación de pendientes por valor absoluto" style="width: 100%; height: auto;" />
</div>

> 💡 **Observa:** Mientras mayor sea $|m|$, más "vertical" se ve la recta. La recta naranja ($m=1$) forma exactamente 45° con el eje X.

---

## 📖 Casos Especiales: Rectas Horizontales y Verticales

### Rectas Horizontales

Una recta horizontal tiene ecuación $y = k$ (donde $k$ es constante).

- Todos sus puntos tienen la misma ordenada
- Cambio vertical: $\Delta y = 0$
- Pendiente: $m = \frac{0}{\Delta x} = 0$

**Ejemplos:** $y = 3$, $y = -2$, $y = 0$ (el eje X)

### Rectas Verticales

Una recta vertical tiene ecuación $x = k$ (donde $k$ es constante).

- Todos sus puntos tienen la misma abscisa
- Cambio horizontal: $\Delta x = 0$
- Pendiente: $m = \frac{\Delta y}{0}$ → **No definida**

**Ejemplos:** $x = 4$, $x = -1$, $x = 0$ (el eje Y)

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <img src="/images/geometria/analitica/rectas-especiales.svg" alt="Rectas horizontales y verticales" style="width: 100%; height: auto;" />
</div>

> 💡 **Observa:** Las rectas horizontales (azul, verde, naranja) tienen $m = 0$. Las rectas verticales (roja, morada) tienen pendiente **indefinida**.

---

## 🔑 Resumen

| Concepto | Significado |
|----------|-------------|
| **Pendiente** | Mide la inclinación de una recta |
| **$m > 0$** | Recta ascendente |
| **$m < 0$** | Recta descendente |
| **$m = 0$** | Recta horizontal |
| **$m$ indefinida** | Recta vertical |
| **$\|m\|$ grande** | Más empinada |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Clasifica cada recta según su pendiente:
a) $m = 4$
b) $m = -1$
c) $m = 0$
d) $m = \frac{1}{3}$

<details>
<summary>Ver solución</summary>

a) $m = 4 > 0$ → **Ascendente, empinada** (sube, $|m| > 1$)
b) $m = -1 < 0$ → **Descendente, 45°** (baja, $|m| = 1$)
c) $m = 0$ → **Horizontal**
d) $m = \frac{1}{3} > 0$ → **Ascendente, suave** (sube, $|m| < 1$)

</details>

### Ejercicio 2
Una rampa tiene pendiente $m = 0.08$. ¿Cuántos metros sube la rampa por cada 10 metros horizontales?

<details>
<summary>Ver solución</summary>

La pendiente es:
$$
m = \frac{\text{subida}}{\text{avance}} = 0.08
$$

Si el avance es 10 metros:
$$
\text{subida} = m \times \text{avance} = 0.08 \times 10 = 0.8 \text{ metros}
$$

**Respuesta:** La rampa sube 0.8 metros (80 cm) por cada 10 metros horizontales.

</details>

### Ejercicio 3
¿Cuál recta es más empinada?
- Recta A: $m = -3$
- Recta B: $m = 2.5$

<details>
<summary>Ver solución</summary>

Comparamos los valores absolutos:
- $|m_A| = |-3| = 3$
- $|m_B| = |2.5| = 2.5$

Como $3 > 2.5$, la **Recta A es más empinada**.

> Nota: La recta A baja (pendiente negativa) y la B sube (positiva), pero A es más inclinada.

</details>

### Ejercicio 4
¿Qué tipo de recta tiene pendiente indefinida? Da un ejemplo de su ecuación.

<details>
<summary>Ver solución</summary>

Las rectas **verticales** tienen pendiente indefinida.

Ejemplos: $x = 5$, $x = -3$, $x = 0$

Estas rectas no pueden escribirse en la forma $y = mx + b$ porque para un mismo valor de $x$, hay infinitos valores de $y$.

</details>

### Ejercicio 5
Un techo tiene pendiente $m = 0.4$. Si el techo tiene 6 metros de base horizontal, ¿cuál es la altura máxima del techo?

<details>
<summary>Ver solución</summary>

$$
\text{altura} = m \times \text{base} = 0.4 \times 6 = 2.4 \text{ metros}
$$

**Respuesta:** La altura máxima del techo es 2.4 metros.

</details>
