---
title: "Coeficiente de Correlación"
---

# **Coeficiente de Correlación**

La Covarianza tenía un defecto fatal: si cambiabas de metros a centímetros, el número se volvía gigante, aunque la relación fuera la misma. Necesitábamos un número que **siempre** estuviera entre -1 y 1, sin importar si medimos en hormigas o galaxias. Karl Pearson lo resolvió con una idea brillante: dividir la covarianza entre las desviaciones estándar. Así nació la $r$ de Pearson, el estándar de oro en la ciencia.

---

## 🎯 ¿Qué vas a aprender?

- Calcular el Coeficiente de Correlación de Pearson ($r$).
- Interpretar la fuerza de la relación usando la escala de -1 a 1.
- Entender por qué es "adimensional" (no tiene unidades).
- Distinguir entre Correlación y Causalidad.

---

## La Fórmula Mágica

Simplemente tomamos la Covarianza y la "normalizamos" dividiéndola por el producto de las desviaciones estándar de X y Y.

$$ r = \frac{S_{xy}}{S_x \cdot S_y} $$

Esto garantiza que el resultado siempre esté "atrapado" entre -1 y +1.

---

## La Escala de Pearson

- **$r = +1$:** Positiva Perfecta. (Línea recta subiendo).
- **$r = 0.8$:** Positiva Fuerte. (Nube estirada subiendo).
- **$r = 0$:** Sin Relación Lineal. (Nube redonda).
- **$r = -0.5$:** Negativa Moderada. (Nube gorda bajando).
- **$r = -1$:** Negativa Perfecta. (Línea recta bajando).

---

## Cálculo y Análisis

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Cálculo Manual
**Datos:**
- Covarianza ($S_{xy}$) = 50.
- Desviación X ($S_x$) = 5.
- Desviación Y ($S_y$) = 12.
**Cálculo:**
$$ r = \frac{50}{5 \cdot 12} = \frac{50}{60} = 0.83 $$
**Interpretación:** Relación Positiva Fuerte.

#### Ejemplo 2: El caso de los Metros vs Centímetros
- **Metros:** $S_{xy}=2, S_x=1, S_y=2 \to r = 2/(1\cdot2) = \boxed{1}$.
- **Centímetros:** $S_{xy}=20000, S_x=100, S_y=200 \to r = 20000/(100\cdot200) = \boxed{1}$.
**Conclusión:** ¡El valor no cambia! Pearson solucionó el problema de las unidades.

#### Ejemplo 3: Relación Inversa
**Datos:** Precio vs Ventas.
- $S_{xy} = -80$.
- $S_x = 4$.
- $S_y = 25$.
$$ r = \frac{-80}{4 \cdot 25} = \frac{-80}{100} = -0.8 $$
**Interpretación:** Relación Negativa Fuerte.

#### Ejemplo 4: Sin Relación
**Datos:**
- $r = 0.05$.
**Interpretación:** Prácticamente cero. Las variables no tienen nada que ver linealmente.

#### Ejemplo 5: Correlación Espuria
**Datos:** Venta de Helados vs Ataques de Tiburón ($r = 0.9$).
**Análisis:** ¿Comer helado atrae tiburones? No.
Ambas suben en verano. Hay una **variable oculta** (Temperatura).
**Lección:** Correlación no implica Causalidad.

---

## El Coeficiente de Determinación ($r^2$)

Si elevas $r$ al cuadrado, obtienes $R^2$. Este número (entre 0% y 100%) te dice **cuánto explica X a Y**.
- Si $r = 0.9$, entonces $R^2 = 0.81$ (81%).
- Significa que el 81% de la variación de Y se debe a X. El otro 19% son otros factores.

### ⚙️ Ejemplos de Interpretación

#### Ejemplo 1: Estudio vs Notas
$r=0.8 \to R^2=0.64$.
El 64% de tu nota depende de cuánto estudias. El 36% restante depende de tu suerte, talento natural o si dormiste bien.

#### Ejemplo 2: Altura Padres vs Hijos
$r=0.5 \to R^2=0.25$.
La genética de altura explica el 25%. El 75% depende de nutrición, ambiente, etc.

#### Ejemplo 3: Ley Física
$r=1.0 \to R^2=100\%$.
La fuerza explica el 100% de la aceleración (en el vacío ideal).

#### Ejemplo 4: Calidad de Vida
$r^2=10\%$.
La variable que estudias (ej: clima) explica muy poco (10%) de la calidad de vida.

#### Ejemplo 5: Mercado de Valores
$r^2=0.01$.
El modelo no sirve para predecir nada.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si $r = 1.2$, ¿qué significa?

<details>
<summary>Ver solución</summary>

**Análisis:** Es imposible. El rango es [-1, 1]. Hiciste mal el cálculo.
**Resultado:** $\boxed{\text{Error matemático}}$

</details>

### Ejercicio 2
Si $Cov(X,Y) = -10, S_x=2, S_y=5$. Calcula $r$.

<details>
<summary>Ver solución</summary>

**Cálculo:** $-10 / (2 \cdot 5) = -1$.
**Resultado:** $\boxed{-1 \text{ (Negativa Perfecta)}}$

</details>

### Ejercicio 3
¿Qué relación es más fuerte: $r=0.6$ o $r=-0.8$?

<details>
<summary>Ver solución</summary>

**Análisis:** Miramos el valor absoluto (la fuerza). $|-0.8| > |0.6|$.
**Resultado:** $\boxed{-0.8}$

</details>

### Ejercicio 4
Si $r=0$, ¿puedes decir que las variables son independientes?

<details>
<summary>Ver solución</summary>

**Teoría:** Solo dice que no hay relación **lineal**. Podría haber una parábola perfecta ($U$).
**Resultado:** $\boxed{\text{No necesariamente}}$

</details>

### Ejercicio 5
Calcula $R^2$ si $r=0.5$.

<details>
<summary>Ver solución</summary>

**Cálculo:** $0.5 \times 0.5 = 0.25$.
**Resultado:** $\boxed{25\%}$

</details>

### Ejercicio 6
Si todos los puntos forman una línea vertical, ¿cuánto vale $r$?

<details>
<summary>Ver solución</summary>

**Teoría:** $S_x = 0$. Divides por cero. Indefinido.
**Resultado:** $\boxed{\text{Indefinido}}$

</details>

### Ejercicio 7
En ciencias sociales, un $r=0.3$ suele considerarse "interesante". En física, "basura". ¿Por qué?

<details>
<summary>Ver solución</summary>

**Contexto:** Los humanos somos impredecibles (ruido). Los átomos no.
**Resultado:** $\boxed{\text{Depende del contexto}}$

</details>

### Ejercicio 8
Si cambias X de "Años" a "Meses", ¿cambia $r$?

<details>
<summary>Ver solución</summary>

**Propiedad:** $r$ es adimensional e invariante a escala.
**Resultado:** $\boxed{\text{No cambia}}$

</details>

### Ejercicio 9
¿Qué signo tiene $r$ si la Covarianza es negativa?

<details>
<summary>Ver solución</summary>

**Lógica:** $S_x$ y $S_y$ siempre son positivos. El signo lo da la covarianza.
**Resultado:** $\boxed{\text{Negativo}}$

</details>

### Ejercicio 10
Si $r=1$, ¿todos los puntos deben estar en la línea?

<details>
<summary>Ver solución</summary>

**Definición:** Sí, perfección lineal.
**Resultado:** $\boxed{\text{Sí}}$

</details>

---

## 🔑 Resumen

| Estadístico | Fórmula | Rango | Uso |
|-------------|---------|-------|-----|
| **Covarianza** | No sirve para comparar. | $(-\infty, \infty)$ | Solo signo. |
| **Correlación ($r$)** | $\frac{S_{xy}}{S_x S_y}$ | $[-1, 1]$ | Dirección y Fuerza. |
| **Determinación ($R^2$)** | $r^2$ | $[0, 1]$ | Capacidad explicativa. |

> **Conclusión:** Pearson nos dio el traductor universal. Con $r$, un psicólogo puede hablar con un astrónomo sobre qué tan fuertes son sus descubrimientos.
