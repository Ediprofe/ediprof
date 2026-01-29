# **Comparación: Media, Mediana y Moda**

Tienes un conjunto de datos y tres herramientas para encontrar su centro. ¿Cuál usas? Usar la herramienta equivocada no es solo un error matemático, es una mentira estadística. Decir "el sueldo promedio es alto" cuando la mayoría gana poco (porque un millonario infló la media) es técnicamente cierto pero éticamente falso. Aquí aprenderás a elegir la medida correcta.

---

## 🎯 ¿Qué vas a aprender?

- Relacionar la forma del gráfico (simetría) con la posición de las tres medidas.
- Identificar cuándo la Media miente por culpa de los valores extremos.
- Elegir la medida adecuada según el tipo de variable (Cualitativa vs Cuantitativa).
- Interpretar el sesgo (hacia dónde se "derrite" la montaña de datos).

---

## Simetría vs. Sesgo

Imagina los datos como una montaña.
1.  **Simétrica:** Una montaña perfecta. Las tres medidas coinciden en la cima.
2.  **Sesgada a la Derecha (Positiva):** La montaña tiene una cola larga a la derecha (valores altos escasos). La media persigue a la cola.
3.  **Sesgada a la Izquierda (Negativa):** La montaña tiene una cola larga a la izquierda (valores bajos escasos). La media persigue a la cola.

### ⚙️ Ejemplos Resueltos: Identificando la Forma

#### Ejemplo 1: Simetría Perfecta
**Datos:** 2, 4, 6, 8, 10.
- Media: 6. Mediana: 6. Moda: N/A (o centro 6 si repites).
**Conclusión:** Todo coincide. Es una campana perfecta.

#### Ejemplo 2: Sesgo Derecha (Ingresos)
**Datos:** 1, 1, 2, 10.
- Moda: 1.
- Mediana: 1.5.
- Media: 3.5.
**Orden:** $Mo < Me < \bar{x}$.
**Análisis:** La media (3.5) es la mayor porque el 10 la jaló.

#### Ejemplo 3: Sesgo Izquierda (Examen Fácil)
**Datos:** 2, 8, 9, 10.
- Moda: N/A.
- Mediana: 8.5.
- Media: 7.25.
**Orden:** $\bar{x} < Me$.
**Análisis:** La media (7.25) es la menor porque el 2 la jaló hacia abajo.

#### Ejemplo 4: Salarios de Empresa
**Situación:** Moda = \$1M, Mediana = \$1.2M, Media = \$5M.
**Forma:** Sesgada a la derecha brutalmente.
**Interpretación:** La mayoría gana poco (Moda), pero hay jefes que ganan muchísimo (inflando la Media).

#### Ejemplo 5: Edad de Jubilación
**Situación:** La mayoría se jubila a los 65. Pocos se jubilan jóvenes (40, 50).
**Forma:** Sesgada a la izquierda.
**Orden:** La media será menor que la moda (65).

---

## Sensibilidad y Robustez

¿Qué tan frágil es el dato ante un error o un extremo?

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: El Error de Dedo
**Datos:** 10, 11, 12.
- Media: 11. Mediana: 11.
**Cambio:** Escribes 120 en vez de 12. (10, 11, 120).
- Media: 47 (¡Explotó!). Mediana: 11 (Intacta).
**Ganador:** Mediana (Robusta).

#### Ejemplo 2: Datos Cualitativos
**Datos:** Rojo, Rojo, Azul.
- Media: ¿Rojo + Azul / 3? Imposible.
- Mediana: No se puede ordenar colores.
- Moda: Rojo.
**Ganador:** Moda (Única opción).

#### Ejemplo 3: Datos de Inventario
**Situación:** Vendes tallas S, M, L.
- Media: Talla "M y medio". Inútil para pedir stock.
- Moda: La talla que más se vendió.
**Ganador:** Moda.

#### Ejemplo 4: Récords Olímpicos
**Datos:** Tiempos muy precisos y cercanos.
- Media: Responde bien a pequeñas variaciones.
- Mediana: Puede ignorar mejoras de milisegundos si no cambian el orden.
**Ganador:** Media (Más sensible y precisa para datos compactos).

#### Ejemplo 5: Precios de Vivienda
**Datos:** Casas de barrio popular y una mansión.
- Media: Indica que el barrio es de ricos.
- Mediana: Indica el precio real de la casa típica.
**Ganador:** Mediana.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
En una distribución donde $\bar{x} = 100$, $Me = 50$, $Mo = 20$, ¿hacia dónde es el sesgo?

<details>
<summary>Ver solución</summary>

**Análisis:** La media es mucho mayor que la mediana y moda. La cola va hacia la derecha.
**Resultado:** $\boxed{\text{Sesgo Positivo (Derecha)}}$

</details>

### Ejercicio 2
Si quieres impresionar inversores diciendo que tu empresa paga "muy bien", pero en realidad pagas mal a la mayoría y mucho a ti mismo, ¿qué medida publicas?

<details>
<summary>Ver solución</summary>

**Estrategia:** La media se inflará con tu sueldo alto. La mediana revelaría la verdad baja.
**Resultado:** $\boxed{\text{La Media}}$

</details>

### Ejercicio 3
Para decidir qué sabor de helado comprar más para una fiesta, ¿usas la media, mediana o moda?

<details>
<summary>Ver solución</summary>

**Variable:** Sabores (Cualitativa).
**Resultado:** $\boxed{\text{La Moda}}$

</details>

### Ejercicio 4
En una distribución perfectamente simétrica, si la media es 50, ¿cuánto vale la mediana?

<details>
<summary>Ver solución</summary>

**Propiedad:** En simetría, coinciden.
**Resultado:** $\boxed{50}$

</details>

### Ejercicio 5
¿Qué medida es más afectada si el dato más grande se duplica?

<details>
<summary>Ver solución</summary>

**Análisis:** La mediana solo mira posición. La media suma el valor.
**Resultado:** $\boxed{\text{La Media}}$

</details>

### Ejercicio 6
Tienes datos: 1, 2, 3, 100.
Media = 26.5. Mediana = 2.5.
¿Cuál describe mejor al "grupo típico"?

<details>
<summary>Ver solución</summary>

**Análisis:** 3 de los 4 datos están entre 1 y 3. El 2.5 está cerca. El 26.5 está lejísimos.
**Resultado:** $\boxed{\text{La Mediana}}$

</details>

### Ejercicio 7
Verdadero o Falso: En una distribución sesgada a la izquierda, la media es menor que la moda.

<details>
<summary>Ver solución</summary>

**Visualización:** Cola izquierda = valores bajos jalan la media abajo.
**Resultado:** $\boxed{\text{Verdadero}}$

</details>

### Ejercicio 8
Si tus datos son "Rango Militar" (Soldado, Cabo, Sargento, General), ¿puedes calcular la mediana?

<details>
<summary>Ver solución</summary>

**Variable:** Cualitativa Ordinal (tienen orden). Sí se puede hallar el rango central.
**Resultado:** $\boxed{\text{Sí}}$

</details>

### Ejercicio 9
Un conjunto de datos tiene dos picos de frecuencia. ¿Cómo se llama y qué medida lo destaca?

<details>
<summary>Ver solución</summary>

**Nombre:** Bimodal.
**Medida:** La Moda (te dará los dos valores). La media te daría un punto en el medio del valle, donde no hay nadie.
**Resultado:** $\boxed{\text{Bimodal - Moda}}$

</details>

### Ejercicio 10
¿Cuál es la única medida que puede no existir?

<details>
<summary>Ver solución</summary>

**Análisis:** Siempre puedes sumar (media) u ordenar (mediana). Pero si no hay repeticiones...
**Resultado:** $\boxed{\text{La Moda}}$

</details>

---

## 🔑 Resumen

| Característica | Media ($\bar{x}$) | Mediana ($Me$) | Moda ($Mo$) |
|----------------|-------------------|----------------|-------------|
| **Lo mejor** | Precisión matemática. | Honestidad (Robustez). | Popularidad. |
| **Lo peor** | Sensible a extremos. | Ignora magnitudes. | Puede no existir. |
| **Cuándo usar** | Datos normales/simétricos. | Ingresos, precios, sesgos. | Tallas, votos, colores. |

> **Conclusión:** Si los datos son democráticos (sin extremos locos), usa la Media. Si hay dictadores (outliers), usa la Mediana. Si es un concurso de belleza (cualitativo), usa la Moda.
