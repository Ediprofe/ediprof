# **Polígono de Frecuencias**

Imagina las siluetas de dos montañas a lo lejos. Si te pregunto cuál es más alta o cuál es más ancha, puedes responder al instante solo mirando el contorno. El **polígono de frecuencias** es exactamente eso: el perfil delineado de tus datos. A diferencia del histograma que son "bloques", el polígono es una línea continua que conecta los puntos medios, permitiéndonos superponer varias montañas (distribuciones) en un mismo dibujo para compararlas.

---

## 🎯 ¿Qué vas a aprender?

- Construir un polígono de frecuencias usando las marcas de clase ($x_i$).
- Cerrar correctamente el polígono con frecuencias cero reales o imaginarias.
- Comparar visualmente dos o más grupos de datos en el mismo gráfico.
- Diferenciar cuándo usar un polígono y cuándo un histograma.

---

## Construcción: Uniendo los Puntos

La clave del polígono es la **Marca de Clase ($x_i$)**. En lugar de dibujar una barra ancha, ponemos un punto justo en el centro del techo de esa barra (altura = frecuencia). Luego, unimos los puntos.

**Coordenadas:** $(x_i, f_i)$

### ⚙️ Ejemplos Resueltos: Hallando las Coordenadas

#### Ejemplo 1: Intervalos simples
**Datos:**
- [10-20): $f=5$
- [20-30): $f=12$
**Puntos Medios ($x_i$):**
- De 10 a 20, centro = 15. Punto: $(15, 5)$.
- De 20 a 30, centro = 25. Punto: $(25, 12)$.
**Cierre:** Agregamos puntos en 5 (antes) y 35 (después) con altura 0.

#### Ejemplo 2: Notas (0-5)
**Datos:** Intervalo [3.0 - 4.0] con frecuencia 20.
**Punto Medio:** $3.5$.
**Coordenada:** $(3.5, 20)$.

#### Ejemplo 3: Temperatura
**Datos:** Clase 15°C-17°C, frecuencia 8 días.
**Punto Medio:** 16°C.
**Coordenada:** $(16, 8)$.

#### Ejemplo 4: Salarios (Millones)
**Datos:** Clase 2-4 Millones, frecuencia 50 empleados.
**Punto Medio:** 3 Millones.
**Coordenada:** $(3, 50)$.

#### Ejemplo 5: Tiempo de carrera
**Datos:** Clase 50s-60s, frecuencia 5 corredores.
**Punto Medio:** 55s.
**Coordenada:** $(55, 5)$.

---

## Comparación Visual de Distribuciones

La superpotencia del polígono de frecuencias es la comparación.

### ⚙️ Ejemplos Resueltos: Interpretación de Gráficos Superpuestos

#### Ejemplo 1: Hombres vs Mujeres (Estatura)
**Visual:** La curva de las mujeres tiene su pico en 1.65m. La de los hombres en 1.75m.
**Interpretación:** La curva de los hombres está **desplazada a la derecha**, indicando que, en promedio, son más altos.

#### Ejemplo 2: Examen Mañana vs Tarde
**Visual:** La curva de la mañana es alta y estrecha. La de la tarde es baja y ancha.
**Interpretación:** Los de la mañana tuvieron notas muy parecidas (baja dispersión). Los de la tarde tuvieron notas muy variadas (alta dispersión), aunque el promedio pueda ser similar.

#### Ejemplo 3: Antes y Después de un entrenamiento
**Visual:** Curva "Antes": pico en bajo rendimiento. Curva "Después": pico en alto rendimiento.
**Interpretación:** El entrenamiento funcionó; toda la montaña se movió hacia la derecha.

#### Ejemplo 4: Dos máquinas de fábrica
**Visual:** Máquina A: curva picuda (leptocúrtica). Máquina B: curva plana.
**Interpretación:** La Máquina A es más precisa (produce piezas más iguales). La Máquina B tiene problemas de calibración (mucha variación).

#### Ejemplo 5: Clima en dos ciudades
**Visual:** Ciudad A (Pico en 20°C). Ciudad B (Pico en 30°C).
**Interpretación:** Ciudad B es claramente más calurosa.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si tienes el intervalo [0-10] con frecuencia 8, ¿cuál es el punto que graficas en el polígono?

<details>
<summary>Ver solución</summary>

**Marca de clase:** $(0+10)/2 = 5$.
**Coordenada:** $(5, 8)$.
**Resultado:** $\boxed{(5, 8)}$

</details>

### Ejercicio 2
¿Por qué debemos "cerrar" el polígono tocando el eje X al principio y al final?

<details>
<summary>Ver solución</summary>

**Razón:** Para formar un polígono cerrado cuya área represente el 100% de los datos y sea visualmente comparable con el área del histograma.
**Resultado:** $\boxed{\text{Para cerrar el área bajo la curva}}$

</details>

### Ejercicio 3
Si comparas dos polígonos de salarios y el de la Empresa A está más a la derecha que el de la Empresa B, ¿quién paga mejor?

<details>
<summary>Ver solución</summary>

**Lógica:** Eje X = Salario. Más a la derecha = Mayor valor.
**Resultado:** $\boxed{\text{Empresa A}}$

</details>

### Ejercicio 4
En un gráfico tienes un histograma de barras rojas y quieres poner encima los datos del año pasado. ¿Usas otro histograma de barras azules o un polígono?

<details>
<summary>Ver solución</summary>

**Práctica:** Dos histogramas se tapan entre sí. Un polígono (línea) sobre las barras permite ver ambos claramente.
**Resultado:** $\boxed{\text{Un polígono (línea)}}$

</details>

### Ejercicio 5
Calcula la marca de clase para el intervalo [100 - 150].

<details>
<summary>Ver solución</summary>

**Cálculo:** $(100+150)/2 = 125$.
**Resultado:** $\boxed{125}$

</details>

### Ejercicio 6
Si dos polígonos tienen la misma forma exacta, pero uno es más alto que el otro en todas partes, ¿qué está mal?

<details>
<summary>Ver solución</summary>

**Análisis:** Probablemente uno tiene más datos totales ($n$) y están usando frecuencia absoluta. Para comparar formas, deberían usar frecuencia relativa para que las áreas sean comparables.
**Resultado:** $\boxed{\text{Deberían usar frecuencia relativa}}$

</details>

### Ejercicio 7
¿Qué punto del eje X corresponde al pico más alto del polígono?

<details>
<summary>Ver solución</summary>

**Definición:** El valor con mayor frecuencia es la Moda. En datos agrupados, es la marca de clase modal.
**Resultado:** $\boxed{\text{La Moda}}$

</details>

### Ejercicio 8
Dibuja mentalmente: Intervalo 1 (f=2), Intervalo 2 (f=5), Intervalo 3 (f=2). ¿Qué forma tiene el polígono?

<details>
<summary>Ver solución</summary>

**Forma:** Sube al centro y baja. Forma de triángulo o campana. Simétrico.
**Resultado:** $\boxed{\text{Triángulo simétrico}}$

</details>

### Ejercicio 9
Si la amplitud es 5 y el primer intervalo empieza en 10 ($x_i=12.5$), ¿dónde pones el punto de cierre inicial?

<details>
<summary>Ver solución</summary>

**Lógica:** Restas la amplitud a la primera marca de clase.
$12.5 - 5 = 7.5$. (Frecuencia 0).
**Resultado:** $\boxed{(7.5, 0)}$

</details>

### Ejercicio 10
Verdadero o Falso: El polígono de frecuencias une los límites superiores de cada clase.

<details>
<summary>Ver solución</summary>

**Concepto:** Une las **marcas de clase** (centros), no los límites. (Unir límites superiores se usa para la Ojiva acumulada).
**Resultado:** $\boxed{\text{Falso}}$

</details>

---

## 🔑 Resumen

| Concepto | Definición | Uso Principal |
|----------|------------|---------------|
| **Polígono de Frecuencias** | Gráfico lineal que une marcas de clase. | Comparación de múltiples grupos. |
| **Marca de Clase** | Punto medio del intervalo. | Representa al intervalo en el eje X. |
| **Cierre** | Puntos extra con $f=0$. | Define el área del polígono. |

> **Conclusión:** Cuando quieras contar una historia sobre cómo un grupo es diferente de otro (más rico, más alto, más rápido), el polígono de frecuencias es tu mejor herramienta visual.
