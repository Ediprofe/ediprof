---
title: "La Varianza"
---

# **La Varianza**

¿Recuerdas el valor absoluto en la Desviación Media? Es útil, pero matemáticamente "torpe" (su derivada es un lío). Los estadísticos prefieren otra forma de eliminar los signos negativos: **multiplicar por sí mismo**. Así nace la **Varianza**, que penaliza mucho más los errores grandes (porque $10^2=100$, mientras que $2^2=4$). Es la medida reina en la teoría, aunque sus unidades (ej: "años cuadrados") sean difíciles de imaginar.

---

## 🎯 ¿Qué vas a aprender?

- Comprender por qué elevamos al cuadrado las desviaciones.
- Calcular la Varianza Poblacional ($\sigma^2$) y Muestral ($s^2$).
- Diferenciar cuándo dividir por $N$ y cuándo por $n-1$.
- Interpretar cómo los valores extremos influyen más aquí que en la Desviación Media.

---

## El Poder del Cuadrado

Al elevar al cuadrado $(x - \bar{x})^2$:
1.  **Eliminamos el signo:** $(-5)^2 = 25$.
2.  **Castigamos lo lejano:** Si la distancia se duplica, la varianza se cuadruplica. Esto resalta mucho a los datos raros (outliers).

---

## Cálculo de Varianza Poblacional ($\sigma^2$)

Usamos esto cuando tenemos TODOS los datos del universo que nos interesa.
$$ \sigma^2 = \frac{\sum (x_i - \mu)^2}{N} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Datos Simples
**Datos:** 2, 4, 6. ($\mu=4$).
1.  **Restas:** $2-4=-2$, $4-4=0$, $6-4=2$.
2.  **Cuadrados:** $(-2)^2=4$, $0^2=0$, $2^2=4$.
3.  **Promedio:** $(4+0+4)/3 = 8/3 = 2.67$.
**Varianza:** $\boxed{2.67}$

#### Ejemplo 2: Datos Negativos
**Datos:** -10, 0, 10. ($\mu=0$).
1.  **Restas:** -10, 0, 10.
2.  **Cuadrados:** $100, 0, 100$.
3.  **Promedio:** $200/3 = 66.67$.
**Varianza:** $\boxed{66.67}$

#### Ejemplo 3: Sin Variación
**Datos:** 5, 5, 5, 5.
1.  **Restas:** Todas 0.
2.  **Cuadrados:** Todos 0.
**Varianza:** $\boxed{0}$

#### Ejemplo 4: El efecto del Outlier
**Datos:** 1, 1, 1, 9. ($\mu=3$).
1.  **Restas:** -2, -2, -2, 6.
2.  **Cuadrados:** 4, 4, 4, 36.
3.  **Promedio:** $(12+36)/4 = 48/4 = 12$.
**Varianza:** $\boxed{12}$ (Observa cómo el 9 influyó masivamente).

#### Ejemplo 5: Comparación A vs B
**A:** [10, 12]. **B:** [0, 22]. (Ambos $\mu=11$).
- **Var A:** Restas $\pm 1$. Cuadrados $1$. Promedio $\boxed{1}$.
- **Var B:** Restas $\pm 11$. Cuadrados $121$. Promedio $\boxed{121}$.
**Conclusión:** B es 121 veces más variada (en términos de varianza).

---

## Cálculo de Varianza Muestral ($s^2$)

Usamos esto cuando los datos son solo una **muestra** de una población mayor. Dividimos por $n-1$ (Corrección de Bessel) para no subestimar la dispersión real.
$$ s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Muestra Pequeña
**Muestra:** 2, 4, 6. ($\bar{x}=4$).
1.  **Suma de Cuadrados:** $4+0+4 = 8$.
2.  **División:** $8 / (3-1) = 8/2 = 4$.
**Varianza Muestral:** $\boxed{4}$ (Mayor que la poblacional 2.67).

#### Ejemplo 2: Hijos
**Muestra:** 0, 2. ($\bar{x}=1$).
1.  **Cuadrados:** $(0-1)^2=1$, $(2-1)^2=1$. Suma = 2.
2.  **División:** $2 / (2-1) = 2$.
**Varianza $s^2$:** $\boxed{2}$

#### Ejemplo 3: Errores de medición
**Muestra:** 10.1, 10.2, 10.3. ($\bar{x}=10.2$).
1.  **Restas:** -0.1, 0, 0.1.
2.  **Cuadrados:** 0.01, 0, 0.01. Suma = 0.02.
3.  **División:** $0.02 / 2 = 0.01$.
**Varianza $s^2$:** $\boxed{0.01}$

#### Ejemplo 4: Tabla de Frecuencia (Muestral)
- **Dato 3:** 2 veces.
- **Dato 5:** 2 veces.
- **Media:** 4.
1.  **Cuadrados:** $|3-4|^2=1$, $|5-4|^2=1$.
2.  **Suma Ponderada:** $(1\times2) + (1\times2) = 4$.
3.  **Divisor:** $n-1 = 4-1 = 3$.
**Varianza:** $4/3 = \boxed{1.33}$

#### Ejemplo 5: Datos en Centímetros
**Muestra:** 100 cm, 200 cm. ($\bar{x}=150$).
1.  **Restas:** -50, 50.
2.  **Cuadrados:** 2500, 2500. Suma = 5000.
3.  **Divisor:** $2-1 = 1$.
**Varianza:** $\boxed{5000 \text{ cm}^2}$. (Nota las unidades extrañas).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la varianza poblacional de: 1, 2, 3.

<details>
<summary>Ver solución</summary>

**Media:** 2.
**Cuadrados:** 1, 0, 1. Suma=2.
**Divisor($N$):** 3.
**Resultado:** $\boxed{0.67}$

</details>

### Ejercicio 2
Calcula la varianza muestral de: 1, 2, 3.

<details>
<summary>Ver solución</summary>

**Suma Cuadrados:** 2 (igual que arriba).
**Divisor($n-1$):** 2.
**Resultado:** $\boxed{1}$

</details>

### Ejercicio 3
Si la varianza es 25, ¿puedes decir algo sobre la media?

<details>
<summary>Ver solución</summary>

**Teoría:** No. La varianza mide dispersión, es independiente del centro.
**Resultado:** $\boxed{\text{No}}$

</details>

### Ejercicio 4
Si multiplicas todos los datos por 2, ¿qué le pasa a la varianza?

<details>
<summary>Ver solución</summary>

**Análisis:** Las distancias se duplican. Al elevar al cuadrado, se cuadruplican.
**Resultado:** $\boxed{\text{Se multiplica por 4}}$

</details>

### Ejercicio 5
Calcula la varianza poblacional de: 10, 10, 10.

<details>
<summary>Ver solución</summary>

**Variación:** Nula.
**Resultado:** $\boxed{0}$

</details>

### Ejercicio 6
Calcula $s^2$ para: 5, 15.

<details>
<summary>Ver solución</summary>

**Media:** 10.
**Cuadrados:** 25, 25. Suma=50.
**Divisor:** 1.
**Resultado:** $\boxed{50}$

</details>

### Ejercicio 7
¿Puede la varianza ser negativa?

<details>
<summary>Ver solución</summary>

**Teoría:** Sumas números al cuadrado (positivos). Imposible.
**Resultado:** $\boxed{\text{No}}$

</details>

### Ejercicio 8
¿Qué tiene más varianza? A:[0, 10] ó B:[4, 6]. (Poblaciones).

<details>
<summary>Ver solución</summary>

**A:** Dist. 5 al cuadrado = 25.
**B:** Dist. 1 al cuadrado = 1.
**Resultado:** $\boxed{A}$

</details>

### Ejercicio 9
Si sumas 100 a todos los datos, ¿cambia la varianza?

<details>
<summary>Ver solución</summary>

**Análisis:** La dispersión relativa no cambia al mover la gráfica.
**Resultado:** $\boxed{\text{No cambia}}$

</details>

### Ejercicio 10
¿Cuáles son las unidades de la varianza si los datos son "Segundos"?

<details>
<summary>Ver solución</summary>

**Logica:** Elevamos al cuadrado todo.
**Resultado:** $\boxed{\text{Segundos cuadrados } (s^2)}$

</details>

---

## 🔑 Resumen

| Tipo | Símbolo | Fórmula | Uso |
|------|---------|---------|-----|
| **Poblacional** | $\sigma^2$ | $\frac{\sum(x-\mu)^2}{N}$ | Tienes todos los datos. |
| **Muestral** | $s^2$ | $\frac{\sum(x-\bar{x})^2}{n-1}$ | Tienes solo una muestra. |

> **Conclusión:** La Varianza es el motor matemático de la estadística, pero sus unidades cuadradas la hacen difícil de leer. Por eso, casi siempre le sacamos la raíz cuadrada al final... para obtener la Desviación Estándar.
