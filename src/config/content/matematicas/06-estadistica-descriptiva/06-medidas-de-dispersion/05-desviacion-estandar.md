---
title: "Desviación Estándar"
---

# **Desviación Estándar**

La **Varianza** nos dejaba con un problema: si medimos estaturas en metros, el resultado nos daba en "metros cuadrados". ¡Nadie mide $\text{m}^2$ de altura! Para corregir esto, usamos la **Desviación Estándar** ($\sigma$ o $S$), que es simplemente la raíz cuadrada de la varianza. Con esto, volvemos al mundo real y podemos decir: "La estatura promedio es 1.70m con una variación de 0.10m".

---

## 🎯 ¿Qué vas a aprender?

- Calcular la Desviación Estándar sacando la raíz cuadrada de la varianza.
- Interpretar el resultado en las mismas unidades que tus datos.
- Diferenciar entre la fórmula poblacional ($\sigma$) y muestral ($S$).
- Conocer la **Regla Empírica** (lo que pasa a 1, 2 y 3 desviaciones de distancia).

---

## Volviendo a la Realidad

$$ \text{Desviación Estándar} = \sqrt{\text{Varianza}} $$

Si la varianza te dio 25 "unidades cuadradas", la desviación estándar es 5 "unidades normales".

---

## Cálculo y Fórmulas

Igual que la varianza, tiene dos sabores:

1.  **Poblacional ($\sigma$):** $\sqrt{\frac{\sum(x-\mu)^2}{N}}$
2.  **Muestral ($S$):** $\sqrt{\frac{\sum(x-\bar{x})^2}{n-1}}$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Datos Simples ($N$)
**Varianza calculada:** $\sigma^2 = 4$.
**Cálculo:** $\sigma = \sqrt{4} = 2$.
**Interpretación:** Los datos se alejan, en promedio, 2 unidades del centro.

#### Ejemplo 2: Datos Muestrales ($n$)
**Datos:** 2, 4, 6.
**Varianza Muestral:** $S^2 = 4$. (Ver lección anterior).
**Desviación Estándar:** $S = \sqrt{4} = 2$.

#### Ejemplo 3: Unidades Físicas
**Datos:** 10m, 20m. ($\text{Varianza} = 25 \text{m}^2$).
**Desviación:** $\sqrt{25 \text{m}^2} = \boxed{5 \text{m}}$. 
(Ahora sí tiene sentido físico).

#### Ejemplo 4: Precisión de Máquinas
- **Máquina A:** $S = 0.1$ mm.
- **Máquina B:** $S = 1.0$ mm.
**Análisis:** La Máquina A es 10 veces más precisa (menos dispersa) que la B.

#### Ejemplo 5: Sin Dispersión
**Datos:** 7, 7, 7. ($\sigma^2=0$).
**Desviación:** $\sqrt{0} = \boxed{0}$.

---

## Interpretación: La Regla Empírica

Si tus datos se parecen a una campana (Normal):
- **68%** de los datos están a **1 desviación** ($\bar{x} \pm \sigma$).
- **95%** de los datos están a **2 desviaciones** ($\bar{x} \pm 2\sigma$).
- **99.7%** de los datos están a **3 desviaciones** ($\bar{x} \pm 3\sigma$).

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Coeficiente Intelectual (CI)
**Media:** 100. **Desviación:** 15.
- Entre 85 y 115 ($100 \pm 15$) está el **68%** de la gente (promedio).
- Entre 70 y 130 ($100 \pm 30$) está el **95%** (casi todos).
- Tener más de 145 es ser un genio (top 0.15%).

#### Ejemplo 2: Estatura Hombres
**Media:** 175 cm. **Desviación:** 5 cm.
- **68%** mide entre 170 y 180 cm.
- **95%** mide entre 165 y 185 cm.

#### Ejemplo 3: Duración de Batería
**Media:** 10 horas. **Desviación:** 1 hora.
- Es muy probable (68%) que dure entre 9 y 11 horas.
- Es rarísimo (0.3%) que dure menos de 7 horas o más de 13.

#### Ejemplo 4: Calidad Six Sigma
En la industria, buscan que los errores ocurran solo más allá de **6 desviaciones** estándar ($6\sigma$). Eso es casi imposible (3.4 defectos por millón).

#### Ejemplo 5: Notas de Examen
**Media:** 3.5. **Desviación:** 0.5.
- La mayoría (68%) sacó entre 3.0 y 4.0.
- Casi nadie sacó menos de 2.0 o más de 5.0 (a 3 desviaciones).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si la varianza es 100, ¿cuánto vale la desviación estándar?

<details>
<summary>Ver solución</summary>

**Cálculo:** $\sqrt{100} = 10$.
**Resultado:** $\boxed{10}$

</details>

### Ejercicio 2
Si la desviación estándar es 3, ¿cuánto vale la varianza?

<details>
<summary>Ver solución</summary>

**Cálculo:** $3^2 = 9$.
**Resultado:** $\boxed{9}$

</details>

### Ejercicio 3
Calcula $S$ para la muestra: 1, 3, 5.

<details>
<summary>Ver solución</summary>

**Media:** 3.
**Restas:** -2, 0, 2.
**Cuadrados:** 4, 0, 4. Suma=8.
**Var ($n-1$):** $8/2 = 4$.
**Desviación:** $\sqrt{4} = 2$.
**Resultado:** $\boxed{2}$

</details>

### Ejercicio 4
En una fábrica, ¿prefieres una desviación estándar grande o pequeña?

<details>
<summary>Ver solución</summary>

**Contexto:** Quieres consistencia.
**Resultado:** $\boxed{\text{Pequeña}}$

</details>

### Ejercicio 5
Si $\text{Media}=50$ y $\sigma=10$, ¿entre qué valores está el 68% de los datos?

<details>
<summary>Ver solución</summary>

**Rango:** $50 \pm 10$.
**Resultado:** $\boxed{40 \text{ y } 60}$

</details>

### Ejercicio 6
Tienes datos en "Kilogramos". ¿En qué unidad está la desviación estándar?

<details>
<summary>Ver solución</summary>

**Teoría:** Misma unidad.
**Resultado:** $\boxed{\text{Kilogramos}}$

</details>

### Ejercicio 7
Si todos los datos son iguales a 10, ¿cuánto vale $\sigma$?

<details>
<summary>Ver solución</summary>

**Análisis:** No hay dispersión.
**Resultado:** $\boxed{0}$

</details>

### Ejercicio 8
Compara $\sigma$ de A:[4,5,6] y B:[1,5,9].

<details>
<summary>Ver solución</summary>

**A:** Distancia a media es 1.
**B:** Distancia a media es 4.
**Resultado:** $\boxed{B > A}$

</details>

### Ejercicio 9
Si sumas 1000 a todos los datos, ¿la desviación estándar cambia?

<details>
<summary>Ver solución</summary>

**Análisis:** La varianza no cambiaba. La raíz tampoco.
**Resultado:** $\boxed{\text{No cambia}}$

</details>

### Ejercicio 10
Si multiplicas todos los datos por 10, ¿qué le pasa a la desviación estándar?

<details>
<summary>Ver solución</summary>

**Análisis:** Varianza se multiplicaba por $10^2$. Raíz de $10^2$ es 10.
**Resultado:** $\boxed{\text{Se multiplica por 10}}$

</details>

---

## 🔑 Resumen

| Estadístico | Símbolo | Relación | Unidad |
|-------------|---------|----------|--------|
| **Varianza** | $\sigma^2$ | Madre de la dispersión. | Cuadrada ($u^2$). |
| **Desv. Estándar** | $\sigma$ | Hija (Raíz cuadrada). | Lineal ($u$). |

> **Conclusión:** La Desviación Estándar es la reina de la estadística práctica. Nos dice cuán confiable es el promedio y cuán "normal" es un dato.
