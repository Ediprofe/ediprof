# **Introducción a los Promedios**

Imagina que quieres comprar un celular y ves precios en 10 tiendas diferentes: algunos muy baratos, otros carísimos y la mayoría en un rango medio. Si tu amigo te pregunta *"¿Cuánto cuesta ese celular?"*, no le vas a dictar los 10 precios. Probablemente le darás un solo número que represente a todos: un **promedio**.

En estadística, a estos números "representantes" los llamamos **Medidas de Tendencia Central**. Son el corazón de los datos.

---

## 🎯 ¿Qué vas a aprender?

- Comprender la necesidad intuitiva de resumir datos.
- Identificar las tres formas principales de encontrar el "centro": Media, Mediana y Moda.
- Elegir la medida más adecuada según el contexto (simetría vs sesgo).
- Diferenciar entre mirar el equilibrio (media), la posición (mediana) y la frecuencia (moda).

---

## El Concepto de "Centro"

No existe una única forma de definir el centro. Depende de *cómo* miramos los datos.

1.  **Centro de Gravedad (Media):** Si los datos fueran pesas en una balanza, ¿dónde pongo el dedo para que no se caiga?
2.  **Centro de Orden (Mediana):** Si formamos a todos en una fila, ¿quién está justo en la mitad?
3.  **Centro de Popularidad (Moda):** ¿Qué valor se repite más?

### ⚙️ Ejemplos Resueltos: ¿Qué centro buscamos?

#### Ejemplo 1: Salarios en una Startup
**Situación:** 4 empleados ganan $1,000 y el dueño gana $100,000.
**Análisis:**
- Si usamos el promedio (media), saldría $20,800. ¡Falso! Casi nadie gana eso.
- Si usamos el "del medio" (mediana), sale $1,000. ¡Más realista!
**Lección:** A veces el centro "matemático" miente.

#### Ejemplo 2: Tallas de zapatos
**Situación:** Una tienda quiere saber qué talla pedir más.
**Análisis:**
- El promedio de tallas podría ser 39.5. Pero no existen zapatos 39.5.
- Lo útil es saber cuál se vende más (Moda): la talla 40.
**Lección:** Para inventario, la popularidad manda.

#### Ejemplo 3: Calificaciones
**Situación:** Sacaste 4.0, 4.2 y 3.8.
**Análisis:**
- Aquí los datos son equilibrados. El promedio (media) de 4.0 representa perfectamente tu rendimiento.
**Lección:** Cuando no hay extremos locos, el promedio clásico es ideal.

#### Ejemplo 4: Tiempo de carrera
**Situación:** Corriste 5 veces. Tiempos: 10s, 11s, 10s, 12s, 50s (te caíste).
**Análisis:**
- Ese 50s arruina tu promedio.
- Mejor decir "suelo correr en 10-11s" (mediana o moda) para ignorar la caída.
**Lección:** Los errores (outliers) ensucian el promedio.

#### Ejemplo 5: Elecciones presidenciales
**Situación:** Candidato A: 40%, B: 30%, C: 30%.
**Análisis:**
- No puedes calcular un "promedio de candidatos".
- Solo te importa quién tuvo más votos (Moda): el Candidato A.
**Lección:** Con nombres (datos cualitativos), solo existe la moda.

---

## Comparación Rápida

| Medida | Esencia | ¿Cuándo falla? |
|--------|---------|----------------|
| **Media** ($\bar{x}$) | Democracia (todos los datos cuentan). | Cuando hay un dato millonario (extremo) que distorsiona todo. |
| **Mediana** ($\tilde{x}$) | Jerarquía (el del medio manda). | Cuando necesitamos hacer operaciones matemáticas complejas después. |
| **Moda** ($\hat{x}$) | Popularidad (la mayoría gana). | Cuando todos los datos son diferentes (no hay moda). |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Situación:** Quieres comprar una casa en un barrio. La mayoría cuesta \$100 millones, pero hay un castillo de \$5,000 millones. ¿Qué medida preguntas para no asustarte falsamente?

<details>
<summary>Ver solución</summary>

**Razonamiento:** El castillo elevará el promedio (media) artificialmente. Necesitas el valor típico real.
**Resultado:** $\boxed{\text{La Mediana}}$

</details>

### Ejercicio 2
**Situación:** Un profesor quiere saber si el examen fue muy difícil. La mitad del salón sacó menos de 3.0. ¿Qué medida está usando?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Al hablar de "la mitad por debajo" y "la mitad por encima", se refiere al dato central ordenado.
**Resultado:** $\boxed{\text{La Mediana}}$

</details>

### Ejercicio 3
**Situación:** Estás organizando una fiesta y necesitas comprar la gaseosa que le guste a la mayoría.

<details>
<summary>Ver solución</summary>

**Razonamiento:** No puedes promediar "Coca-Cola" con "Sprite". Necesitas la opción con más votos.
**Resultado:** $\boxed{\text{La Moda}}$

</details>

### Ejercicio 4
**Situación:** Estás midiendo la temperatura de un horno cada min: 180°, 182°, 179°, 181°. No hay valores raros.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Datos numéricos simétricos sin extremos. El promedio aritmético es el más preciso.
**Resultado:** $\boxed{\text{La Media}}$

</details>

### Ejercicio 5
**Análisis:** Tienes los datos: 2, 2, 2, 2, 2. Calcula las tres medidas.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
- Suma/5 = 2.
- El del medio = 2.
- El que más se repite = 2.
**Resultado:** $\boxed{\text{Todas son 2}}$

</details>

### Ejercicio 6
**Situación:** En una carrera de 100 metros, Usain Bolt corre contra 9 tortugas. ¿Qué pasa con el tiempo promedio del grupo?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Las tortugas (tiempos muy altos) harán que el promedio sea lentísimo, haciendo parecer que Usain Bolt también es lento.
**Resultado:** $\boxed{\text{La Media se dispara (sesgada)}}$

</details>

### Ejercicio 7
**Pregunta:** ¿Cuál es la única medida de tendencia central que se puede usar con datos cualitativos (como "Color Favorito")?

<details>
<summary>Ver solución</summary>

**Razonamiento:** No puedes sumar colores ni ordenarlos de menor a mayor. Solo puedes contar frecuencias.
**Resultado:** $\boxed{\text{La Moda}}$

</details>

### Ejercicio 8
**Situación:** Una distribución es "Simétrica". ¿Dónde están la media, mediana y moda?

<details>
<summary>Ver solución</summary>

**Concepto:** En una campana perfecta, todo coincide en el centro.
**Resultado:** $\boxed{\text{En el mismo punto}}$

</details>

### Ejercicio 9
**Situación:** El salario promedio es \$5,000, pero el salario mediano es \$2,000. ¿Qué significa esto sobre la riqueza?

<details>
<summary>Ver solución</summary>

**Análisis:** Si la media es mucho mayor que la mediana, hay gente muy rica "jalando" el promedio hacia arriba.
**Resultado:** $\boxed{\text{Hay desigualdad (sesgo positivo)}}$

</details>

### Ejercicio 10
**Caso:** Tienes datos: 1, 2, 3, 100. ¿Cuál medida es MENOR, la media o la mediana?

<details>
<summary>Ver solución</summary>

**Cálculo:**
- Media: $(1+2+3+100)/4 = 26.5$.
- Mediana: Promedio de 2 y 3 = $2.5$.
**Resultado:** $\boxed{\text{La Mediana es menor}}$

</details>

---

## 🔑 Resumen

| Concepto | "Alias" | Mejor uso |
|----------|---------|-----------|
| **Media** | El Promedio | Datos estables, simétricos, para fórmulas. |
| **Mediana** | El Centro Físico | Datos con valores locos (extremos) o ingresos. |
| **Moda** | El Más Popular | Votaciones, ventas, datos no numéricos. |

> **Conclusión:** No hay un "mejor" promedio. La Media es el más matemático, la Mediana el más honesto socialmente, y la Moda el más útil comercialmente.
