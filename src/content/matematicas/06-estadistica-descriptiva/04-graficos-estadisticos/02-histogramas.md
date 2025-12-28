# **Histogramas**

Imagina una fotografía de un estadio lleno. Si quisieras entender la edad de las personas, tomar el promedio no te dice mucho (podría ser 35 años, pero porque hay muchos niños y muchos ancianos, o porque todos tienen 35). Para ver la **estructura real** de la población, necesitas agruparlos en "contenedores" (de 0-10, 10-20, etc.) y levantar una torre con la cantidad de gente en cada grupo. Al poner esas torres juntas, se forma un **histograma**, la silueta de tus datos.

---

## 🎯 ¿Qué vas a aprender?

- Diferenciar un histograma de un diagrama de barras.
- Construir un histograma a partir de una tabla de frecuencias agrupadas.
- Interpretar la forma de la distribución (simétrica, sesgada, bimodal).
- Identificar valores atípicos y patrones de concentración.

---

## Construcción del Histograma

A diferencia del diagrama de barras donde las categorías "Gatos" y "Perros" están separadas porque son cosas distintas, en un histograma los intervalos numéricos [0-10) y [10-20) son continuos. Por eso, **las barras del histograma van pegadas**.

![Histograma de Pesos](/images/funciones/estadistica/histograma-pesos.svg)

### ⚙️ Ejemplos Resueltos: De la Tabla al Gráfico

#### Ejemplo 1: Estaturas
**Tabla:**
- [1.50 - 1.60): 5 personas
- [1.60 - 1.70): 20 personas
- [1.70 - 1.80): 10 personas
**Construcción:**
Dibujamos tres torres pegadas. La del centro (1.60-1.70) es el doble de alta que la de la derecha. Muestra una concentración clara en el medio.

#### Ejemplo 2: Puntajes (0-100)
**Tabla:**
- [0-50): 2
- [50-100): 48
**Visualización:**
Una barra casi invisible a la izquierda y una torre enorme a la derecha. Indica que casi todos pasaron la mitad.

#### Ejemplo 3: Llamadas por hora
**Tabla:**
- 8-9am: 10
- 9-10am: 50
- 10-11am: 100
- 11-12pm: 20
**Visualización:**
Las barras suben como una escalera hasta las 11am y luego caen bruscamente. Muestra la hora pico.

#### Ejemplo 4: Distribución Uniforme (Dado)
**Tabla:**
- Caras 1-2: 30 veces
- Caras 3-4: 31 veces
- Caras 5-6: 29 veces
**Visualización:**
Tres barras prácticamente de la misma altura. "Techo plano". Indica aleatoriedad pura.

#### Ejemplo 5: Clases vacías
**Tabla:**
- [0-10]: 50
- [10-20]: 0
- [20-30]: 50
**Visualización:**
Dos torres separadas por un hueco. Este hueco ("gap") es información vital: ¡nadie está en el rango medio!

---

## Interpretación de Formas

La forma del histograma nos cuenta la historia detrás de los datos sin ver los números.

### ⚙️ Ejemplos Resueltos: Leyendo la Silueta

#### Ejemplo 1: Salarios (Sesgada a la Derecha)

![Distribución Sesgada a la Derecha](/images/funciones/estadistica/distribucion-sesgada-derecha.svg)
**Forma:** Una torre alta al principio (muchos ganan salario mínimo) y una cola larga, muy larga hacia la derecha (pocos ganan millones).
**Nombre:** Asimetría Positiva.

#### Ejemplo 2: Edad de Muerte (Sesgada a la Izquierda)

![Distribución Sesgada a la Izquierda](/images/funciones/estadistica/distribucion-sesgada-izquierda.svg)
**Forma:** Una cola larga a la izquierda (pocos mueren jóvenes) y una torre alta a la derecha (la mayoría muere anciana).
**Nombre:** Asimetría Negativa.

#### Ejemplo 3: Peso al nacer (Simétrica / Campana)

![Distribución Simétrica](/images/funciones/estadistica/distribucion-simetrica.svg)
**Forma:** Una montaña perfecta en el centro. Pocos bebés muy livianos, pocos muy pesados, la mayoría en el promedio.
**Nombre:** Distribución Normal (Gaussiana).

#### Ejemplo 4: Clientes en restaurante (Bimodal)

![Distribución Bimodal](/images/funciones/estadistica/distribucion-bimodal.svg)
**Forma:** Un pico a las 12pm (almuerzo) y otro pico a las 8pm (cena). Valle en la tarde.
**Interpretación:** Hay dos fenómenos distintos ocurriendo.

#### Ejemplo 5: Lotería (Rectangular / Uniforme)

![Distribución Uniforme](/images/funciones/estadistica/distribucion-uniforme.svg)
**Forma:** Todas las barras iguales.
**Interpretación:** Todos los números tienen la misma probabilidad de salir.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si las barras de tu gráfico están separadas por espacios, ¿es un histograma?

<details>
<summary>Ver solución</summary>

**Análisis:** Los histogramas representan continuidad numérica, por lo que las barras deben tocarse. Si están separadas, es un diagrama de barras (categorías).
**Resultado:** $\boxed{\text{No, es un diagrama de barras}}$

</details>

### Ejercicio 2
Tienes datos de "Edades de participantes en un retiro de jubilados". ¿Hacia dónde esperas que esté la cola del histograma?

<details>
<summary>Ver solución</summary>

**Razonamiento:** La mayoría serán mayores (torre a la derecha). Habrá muy pocos jóvenes (cola a la izquierda).
**Resultado:** $\boxed{\text{Sesgada a la izquierda (Asimetría Negativa)}}$

</details>

### Ejercicio 3
En un histograma, la clase [10-20) tiene altura 5 y la clase [20-30) tiene altura 10. ¿Cuál intervalo tiene más frecuencia?

<details>
<summary>Ver solución</summary>

**Lectura:** La altura es directamente proporcional a la frecuencia. 10 > 5.
**Resultado:** $\boxed{\text{[20-30)}}$

</details>

### Ejercicio 4
Describe la forma de un histograma de "Resultados de lanzar una moneda 10,000 veces" (Cara vs Sello no es histograma, pensemos en "Suma de dos dados").

<details>
<summary>Ver solución</summary>
*Corrección: Suma de dos dados*.
**Razonamiento:** La suma 7 es la más probable. 2 y 12 las menos probables. Sube y baja simétricamente.
**Resultado:** $\boxed{\text{Simétrica (Triangular o Campana)}}$
</details>

### Ejercicio 5
¿Qué significa un "hueco" (espacio vacío sin barra) en medio de un histograma?

<details>
<summary>Ver solución</summary>

**Interpretación:** Significa que la frecuencia de ese intervalo es cero. No hubo ningún dato en ese rango.
**Resultado:** $\boxed{\text{Ausencia de datos en ese rango}}$

</details>

### Ejercicio 6
Interpretando ingresos: ¿Por qué el promedio suele ser mayor que la mediana en un histograma de salarios?

<details>
<summary>Ver solución</summary>

**Análisis:** Es una distribución sesgada a la derecha. Los multimillonarios (cola derecha) jalan el promedio hacia arriba, pero la gente común (la torre) mantiene la mediana baja.
**Resultado:** $\boxed{\text{Por el sesgo a la derecha}}$

</details>

### Ejercicio 7
Si un histograma tiene dos picos de igual altura separados, ¿cómo se llama?

<details>
<summary>Ver solución</summary>

**Definición:** Dos modas claras.
**Resultado:** $\boxed{\text{Bimodal}}$

</details>

### Ejercicio 8
¿El eje X de un histograma puede tener categorías como "Rojo", "Verde", "Azul"?

<details>
<summary>Ver solución</summary>

**Concepto:** El histograma es para variables cuantitativas continuas. Colores son cualitativos.
**Resultado:** $\boxed{\text{No (eso sería diagrama de barras)}}$

</details>

### Ejercicio 9
Si duplicas el ancho de los intervalos al construir el histograma, ¿qué pasa con la altura de las barras?

<details>
<summary>Ver solución</summary>

**Lógica:** Al hacer el intervalo más ancho, atrapas más datos dentro de él.
**Resultado:** $\boxed{\text{La altura (frecuencia) aumenta}}$

</details>

### Ejercicio 10
Dibuja mentalmente: Intervalos 0-5, 5-10, 10-15. Frecuencias 2, 8, 2. ¿Qué forma tiene?

<details>
<summary>Ver solución</summary>

**Visual:** Bajo, Alto, Bajo. Simétrico.
**Resultado:** $\boxed{\text{Simétrica centrada}}$

</details>

---

## 🔑 Resumen

| Característica | Histograma | Diagrama de Barras |
|----------------|------------|--------------------|
| **Tipo de dato** | Cuantitativo Continuo (Números) | Cualitativo (Categorías) |
| **Separación** | Barras pegadas | Barras separadas |
| **Eje X** | Recta numérica real | Etiquetas no ordenadas necesariamente |
| **Área** | Representa frecuencia total | Solo importa la altura |

> **Conclusión:** El histograma es como una radiografía de tus datos numéricos. Te dice dónde está el grueso de la información, qué tan dispersa está y si hay anomalías, todo en un solo golpe de vista.
