---
title: "Introducción a la Regresión Lineal"
---

# **Introducción a la Regresión Lineal**

La correlación nos dijo *qué tan fuerte* es la relación. Ahora queremos ir un paso más allá: queremos **predecir el futuro**. Si sé cuánto gastas en publicidad, ¿puedo adivinar cuánto venderás? La **Regresión Lineal** consiste en dibujar la "mejor línea recta posible" que pase por en medio de los datos, permitiéndonos hacer estimaciones matemáticas.

---

## 🎯 ¿Qué vas a aprender?

- Encontrar la ecuación de la recta ($\hat{y} = a + bx$).
- Calcular la pendiente ($b$) y el intercepto ($a$).
- Usar la recta para hacer predicciones (Interpolación).
- Entender el peligro de predecir fuera de los límites (Extrapolación).

---

## La Mejor Línea Posible

Imagina una nube de puntos. Podrías dibujar infinitas líneas que pasen "más o menos" por el medio. Pero solo hay **una** línea que es matemáticamente perfecta: la que minimiza la distancia (el error cuadrado) con todos los puntos.

Ecuación de la Recta:
$$ \hat{y} = a + bx $$

- $\hat{y}$: El valor que queremos predecir (Variables dependiente).
- $x$: El valor que conocemos (Variable independiente).
- $b$: La **Pendiente** (Qué tanto cambia $Y$ por cada $X$).
- $a$: El **Intercepto** (Dónde empieza la recta cuando $X=0$).

---

## Cálculo de los Coeficientes

Primero hallamos la pendiente ($b$) usando la Covarianza y Varianza, o correlación:

$$ b = r \cdot \frac{S_y}{S_x} $$

Luego hallamos el intercepto ($a$) obligando a la recta a pasar por el promedio $(\bar{x}, \bar{y})$:

$$ a = \bar{y} - b\bar{x} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Horas de Estudio vs Nota
**Datos:**
- Promedios: $\bar{x}=4$ horas, $\bar{y}=3.5$ nota.
- Desviaciones: $S_x=2, S_y=1$.
- Correlación: $r=0.8$.

1.  **Pendiente ($b$):** $0.8 \cdot (1/2) = 0.4$.
    *Por cada hora extra, la nota sube 0.4.*
2.  **Intercepto ($a$):** $3.5 - (0.4 \cdot 4) = 3.5 - 1.6 = 1.9$.
    *Si estudias 0 horas, sacas 1.9.*
3.  **Ecuación:** $\hat{y} = 1.9 + 0.4x$.

**Predicción:** Si estudias 10 horas...
$\hat{y} = 1.9 + 0.4(10) = 5.9$. (¡Nota excelente!).

#### Ejemplo 2: Velocidad vs Tiempo
Ecuación: $\hat{y} = 100 - 0.5x$.
- **Pendiente -0.5:** Relación negativa. Por cada km/h extra, ahorras 0.5 minutos.

#### Ejemplo 3: Ventas de Helado
Ecuación: $\hat{y} = -20 + 10x$ (donde $x$ es temperatura).
- **Intercepto -20:** Matemáticamente, si la temperatura es 0°C, vendes -20 helados. (Absurdo, el modelo no sirve ahí).
- **Pendiente 10:** Por cada grado que sube el calor, vendes 10 helados más.

#### Ejemplo 4: Predicción segura (Interpolación)
Datos de edad entre 10 y 20 años.
Predecir para 15 años: **Seguro y confiable**.

#### Ejemplo 5: Predicción peligrosa (Extrapolación)
Datos de edad entre 10 y 20 años.
Predecir para 80 años: **Muy peligroso**. La tendencia de crecimiento de altura se detiene a los 18, pero la recta seguiría subiendo infinitamente. ¡Predeciría gigantes de 4 metros!

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si la ecuación es $y = 5 + 2x$, ¿qué pasa si X aumenta en 1?

<details>
<summary>Ver solución</summary>

**Pendiente 2:** Y aumenta en 2.
**Resultado:** $\boxed{\text{Aumenta en 2}}$

</details>

### Ejercicio 2
Si $y = 10 - 3x$, ¿qué pasa si X aumenta en 1?

<details>
<summary>Ver solución</summary>

**Pendiente -3:** Y disminuye en 3.
**Resultado:** $\boxed{\text{Disminuye en 3}}$

</details>

### Ejercicio 3
Calcula $b$ si $r=0.5, S_y=10, S_x=2$.

<details>
<summary>Ver solución</summary>

**Fórmula:** $0.5 \cdot (10/2) = 0.5 \cdot 5 = 2.5$.
**Resultado:** $\boxed{2.5}$

</details>

### Ejercicio 4
Si la recta es $y = 2x$ y $\bar{x}=10$, ¿cuánto vale $\bar{y}$?

<details>
<summary>Ver solución</summary>

**Propiedad:** La recta pasa por el promedio.
$y = 2(10) \to 20$.
**Resultado:** $\boxed{20}$

</details>

### Ejercicio 5
¿Es confiable predecir las ventas del año 2050 usando datos de 2000-2010?

<details>
<summary>Ver solución</summary>

**Concepto:** Extrapolación lejana.
**Resultado:** $\boxed{\text{No (Extrapolación)}}$

</details>

### Ejercicio 6
En la ecuación $y = 100 + 50x$, ¿qué es el 100?

<details>
<summary>Ver solución</summary>

**Termino libre:** Intercepto.
**Resultado:** $\boxed{\text{El valor inicial (a)}}$

</details>

### Ejercicio 7
Si $r=0$, ¿cuánto vale la pendiente $b$?

<details>
<summary>Ver solución</summary>

**Fórmula:** $b = 0 \cdot (...)$.
**Resultado:** $\boxed{0 \text{ (Recta horizontal)}}$

</details>

### Ejercicio 8
Predice $Y$ si $x=4$ en la recta $y = 1 + x$.

<details>
<summary>Ver solución</summary>

**Sustitución:** $1 + 4 = 5$.
**Resultado:** $\boxed{5}$

</details>

### Ejercicio 9
¿Qué minimiza el método de "Mínimos Cuadrados"?

<details>
<summary>Ver solución</summary>

**Teoría:** La suma de los errores al cuadrado.
**Resultado:** $\boxed{\text{Los errores (residuos)}}$

</details>

### Ejercicio 10
Si la pendiente es positiva, ¿la correlación puede ser negativa?

<details>
<summary>Ver solución</summary>

**Teoría:** No. $b$ y $r$ siempre comparten el mismo signo.
**Resultado:** $\boxed{\text{No}}$

</details>

---

## 🔑 Resumen

| Concepto | Símbolo | Fórmula Clave |
|----------|---------|---------------|
| **Pendiente** | $b$ | Determina la inclinación. Depende de $r$. |
| **Intercepto** | $a$ | Punto de partida ($X=0$). |
| **Predicción** | $\hat{y}$ | El valor estimado por la recta. |

> **Conclusión:** La Regresión Lineal convierte datos dispersos en una herramienta predictiva. Pero recuerda: "Un gran poder conlleva una gran responsabilidad". No extrapoles a lo loco.
