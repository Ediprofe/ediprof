---
title: "Representación Gráfica de Funciones"
---

# Representación Gráfica de Funciones

Una gráfica es la "foto" de una función. Mientras que la ecuación nos da la lógica, la gráfica nos permite ver el comportamiento de un vistazo: si algo crece rápido, si se mantiene estable o si cae. Aprender a graficar es aprender a visualizar datos.

---

## 🎯 ¿Qué vas a aprender?

- Cómo construir una tabla de valores paso a paso.
- El método de los interceptos (usar los cortes con los ejes).
- Cómo usar la pendiente y el intercepto para graficar sin tablas.
- La importancia de la precisión al ubicar puntos en el plano.

---

## Método 1: La Tabla de Valores

Es el método más seguro. Consiste en elegir valores para $x$, calcular su $y$ y unir los puntos resultantes.

### Ejemplo 1: Graficar y = 2x - 1

**Paso 1: Crear la tabla**

Elegimos valores sencillos para $x$:

| x | Cálculo | Punto (x, y) |
|:---:|:---|:---:|
| -1 | 2(-1) - 1 = -3 | (-1, -3) |
| 0 | 2(0) - 1 = -1 | (0, -1) |
| 1 | 2(1) - 1 = 1 | (1, 1) |
| 2 | 2(2) - 1 = 3 | (2, 3) |

**Paso 2: Ubicar y unir**

Ubicamos esos cuatro puntos en el plano y trazamos la línea recta que los une todos.

<div style="width: 100%; margin-top: 1.5rem; margin-bottom: 2rem;">
  <img src="/images/funciones/algebra/representacion_grafica/ejemplo-1-tabla.svg" alt="Gráfica de y = 2x - 1" style="width: 100%; height: auto; border-radius: 8px; border: 1px solid #e2e8f0;">
</div>

---

### Ejemplo 2: Graficar y = -x + 4

**Paso 1: Crear la tabla**

| x | Cálculo | Punto (x, y) |
|:---:|:---|:---:|
| 0 | -(0) + 4 = 4 | (0, 4) |
| 1 | -(1) + 4 = 3 | (1, 3) |
| 2 | -(2) + 4 = 2 | (2, 2) |
| 3 | -(3) + 4 = 1 | (3, 1) |

**Paso 2: Ubicar y unir**

Al unir los puntos, notarás que la recta baja conforme avanzas a la derecha porque la pendiente es negativa.

<div style="width: 100%; margin-top: 1.5rem; margin-bottom: 2rem;">
  <img src="/images/funciones/algebra/representacion_grafica/ejemplo-2-tabla.svg" alt="Gráfica de y = -x + 4" style="width: 100%; height: auto; border-radius: 8px; border: 1px solid #e2e8f0;">
</div>

---

## Método 2: Interceptos

Buscamos los dos puntos donde la recta cruza los ejes. Es el método más rápido.

- **Corte con Y:** Hacemos $x = 0$.
- **Corte con X:** Hacemos $y = 0$.

### Ejemplo 3: Graficar y = 3x - 6

**Corte con Y (x=0):**

$$
y = 3(0) - 6 = -6 \implies (0, -6)
$$

**Corte con X (y=0):**

$$
0 = 3x - 6 \implies 3x = 6 \implies x = 2 \implies (2, 0)
$$

Solo marcamos $(0, -6)$ y $(2, 0)$ y trazamos la recta.

<div style="width: 100%; margin-top: 1.5rem; margin-bottom: 2rem;">
  <img src="/images/funciones/algebra/representacion_grafica/ejemplo-3-interceptos.svg" alt="Gráfica de y = 3x - 6" style="width: 100%; height: auto; border-radius: 8px; border: 1px solid #e2e8f0;">
</div>

---

### Ejemplo 4: Graficar y = 2x + 4

**Corte con Y (x=0):**

$$
y = 2(0) + 4 = 4 \implies (0, 4)
$$

**Corte con X (y=0):**

$$
0 = 2x + 4 \implies 2x = -4 \implies x = -2 \implies (-2, 0)
$$

Marcamos el 4 en el eje vertical y el -2 en el eje horizontal, luego unimos.

<div style="width: 100%; margin-top: 1.5rem; margin-bottom: 2rem;">
  <img src="/images/funciones/algebra/representacion_grafica/ejemplo-4-interceptos.svg" alt="Gráfica de y = 2x + 4" style="width: 100%; height: auto; border-radius: 8px; border: 1px solid #e2e8f0;">
</div>

---

## Método 3: Pendiente e Intercepto

Es el método más "profesional".
1. Marcas $b$ en el eje vertical.
2. Desde ahí, caminas según la pendiente $m$ (subida/avance).

### Ejemplo 5: Graficar y = (2/3)x + 1

- **Paso 1:** Marcas el punto $(0, 1)$ porque $b = 1$.
- **Paso 2:** La pendiente es $2/3$. Significa: **sube 2, avanza 3**.
- **Paso 3:** Desde $(0, 1)$, sube 2 y avanza 3 a la derecha. Llegas al punto $(3, 3)$.
- **Paso 4:** Une los dos puntos.

<div style="width: 100%; margin-top: 1.5rem; margin-bottom: 2rem;">
  <img src="/images/funciones/algebra/representacion_grafica/ejemplo-5-pendiente.svg" alt="Gráfica de y = (2/3)x + 1" style="width: 100%; height: auto; border-radius: 8px; border: 1px solid #e2e8f0;">
</div>

---

### Ejemplo 6: Graficar y = -2x + 5

- **Paso 1:** Marcas el punto $(0, 5)$ porque $b = 5$.
- **Paso 2:** La pendiente es $-2$. Significa: **baja 2, avanza 1**.
- **Paso 3:** Desde el 5 en el eje vertical, bajas 2 unidades y avanzas 1 a la derecha. Llegas al punto $(1, 3)$.
- **Paso 4:** Une los puntos para ver la recta descendente.

<div style="width: 100%; margin-top: 1.5rem; margin-bottom: 2rem;">
  <img src="/images/funciones/algebra/representacion_grafica/ejemplo-6-pendiente.svg" alt="Gráfica de y = -2x + 5" style="width: 100%; height: auto; border-radius: 8px; border: 1px solid #e2e8f0;">
</div>

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el valor de $y$ para $x = -5$ en la función $f(x) = x + 10$.

<details>
<summary>Ver solución</summary>

$$
-5 + 10 = 5
$$

**Resultado:** $\boxed{5}$

</details>

---

### Ejercicio 2
Encuentra el intercepto con el eje Y de la función $y = -4x + 12$.

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{(0, 12)}$

</details>

---

### Ejercicio 3
Encuentra el intercepto con el eje X de la función $y = 2x - 10$.

<details>
<summary>Ver solución</summary>

$$
0 = 2x - 10 \implies 2x = 10 \implies x = 5
$$

**Resultado:** $\boxed{(5, 0)}$

</details>

---

### Ejercicio 4
Si una pendiente es $m = -3$, ¿cuántas unidades baja $y$ por cada unidad que avanza $x$?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{3 \text{ unidades}}$

</details>

---

### Ejercicio 5
¿Cuál es el valor de $b$ en $y = x$?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{0}$

</details>

---

### Ejercicio 6
Si graficas $y = 4$, ¿cómo es la recta?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{\text{Horizontal que pasa por } y=4}$

</details>

---

### Ejercicio 7
En el método de pendiente-intercepto, si $m = \frac{1}{2}$ y $b = -3$, ¿cuál es el primer punto que marcas?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{(0, -3)}$

</details>

---

### Ejercicio 8
Completa el punto: para $y = 3x + 1$, si $x = 2$, entonces $y = \dots$

<details>
<summary>Ver solución</summary>

$$
3(2) + 1 = 7
$$

**Resultado:** $\boxed{7}$

</details>

---

### Ejercicio 9
¿Cuántos puntos necesitas, como mínimo, para trazar una recta con seguridad?

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{2 \text{ puntos}}$

</details>

---

### Ejercicio 10
Si una función es $y = -x + 2$, ¿hacia dónde se inclina la recta?

<details>
<summary>Ver solución</summary>

**Razonamiento:** La pendiente es negativa.
**Resultado:** $\boxed{\text{Hacia abajo (decreciente)}}$

</details>

---

## 🔑 Resumen

| Método | Concepto Clave | Ventaja |
|:--- |:--- |:--- |
| **Tabla de Valores** | Sustituir $x$ y hallar $y$. | Muy seguro para principiantes. |
| **Interceptos** | Cortes con los ejes ($x=0$ y $y=0$). | Es el más rápido y limpio. |
| **Pendiente-Intercepto** | Iniciar en $b$, caminar según $m$. | Permite graficar mentalmente. |

> **Conclusión:** Graficar no es solo unir puntos; es entender cómo una relación numérica se convierte en una trayectoria visual. Dominar estos métodos te dará una gran ventaja en física y economía.
