---
title: "La Moda"
---

# **La Moda**

¿Cuál es la canción número 1 en Spotify esta semana? ¿Qué color de camiseta se vendió más? Estas preguntas no buscan un "promedio" matemático ni un "centro" geográfico. Buscan lo **popular**, lo **frecuente**. En estadística, el valor que gana el concurso de popularidad se llama **Moda**. Es la única medida que funciona incluso si tus datos no son números (como "colores" o "marcas").

---

## 🎯 ¿Qué vas a aprender?

- Identificar la moda en conjuntos de datos simples (unimodal).
- Reconocer casos especiales: bimodal, multimodal y amodal.
- Encontrar la moda en tablas de frecuencia.
- Diferenciar cuándo la moda es más útil que la media.

---

## Identificando la Moda

Es simple: busca el dato que más se repite.
- **Unimodal:** Un solo ganador.
- **Bimodal:** Dos ganadores empatados.
- **Multimodal:** Tres o más ganadores.
- **Amodal:** Nadie gana (todos aparecen igual).

### ⚙️ Ejemplo Resueltos

#### Ejemplo 1: Unimodal (El Ganador)
**Datos:** 5, 8, 2, 5, 5, 9.
**Conteo:** El 5 aparece tres veces. Los demás solo una vez.
**Moda:** $\boxed{5}$

#### Ejemplo 2: Bimodal (Empate)
**Datos:** 1, 2, 1, 2, 3.
**Conteo:** El 1 aparece dos veces. El 2 aparece dos veces.
**Moda:** $\boxed{1 \text{ y } 2}$

#### Ejemplo 3: Multimodal (Triple Empate)
**Datos:** A, B, C, A, B, C, D.
**Conteo:** A(2), B(2), C(2), D(1).
**Moda:** $\boxed{\text{A, B y C}}$

#### Ejemplo 4: Amodal (Todos iguales)
**Datos:** 10, 20, 30, 40.
**Conteo:** Todos aparecen una sola vez. No hay ningún dato que "destaque".
**Moda:** $\boxed{\text{No tiene}}$

#### Ejemplo 5: Falsa Alarma
**Datos:** 1, 2, 3, 3, 4, 5 (Moda=3). Si agregamos otro 4...
**Datos:** 1, 2, 3, 3, 4, 4, 5. (Moda=3 y 4).
**Lección:** La moda es muy sensible a cambios pequeños en los datos.

---

## Moda en Tablas de Frecuencia

Aquí no tienes que contar, ¡ya contaron por ti! Solo busca el número más grande en la columna de Frecuencia ($f_i$) y mira a quién pertenece.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Tallas de Ropa
**Tabla:**
- S: 50
- M: 120
- L: 80
**Análisis:** 120 es la frecuencia mayor.
**Moda:** $\boxed{\text{Talla M}}$

#### Ejemplo 2: Hijos por familia
**Tabla:**
- 0 hijos: 5 familias
- 1 hijo: 20 familias
- 2 hijos: 20 familias
- 3 hijos: 2 familias
**Análisis:** Empate en 20.
**Moda:** $\boxed{1 \text{ y } 2 \text{ hijos}}$

#### Ejemplo 3: Fruta favorita
**Tabla:**
- Manzana: 10
- Pera: 5
- Banano: 2
**Mayor Frecuencia:** 10.
**Moda:** $\boxed{\text{Manzana}}$

#### Ejemplo 4: Notas (0-10)
**Tabla:**
- Nota 8: 15 alumnos
- Nota 9: 4 alumnos
- Nota 10: 1 alumno
**Mayor Frecuencia:** 15.
**Moda:** $\boxed{8}$

#### Ejemplo 5: Color de ojos
**Tabla:**
- Café: 80%
- Azul: 10%
- Verde: 10%
**Mayor Porcentaje:** 80%.
**Moda:** $\boxed{\text{Café}}$

---

## ¿Cuándo es la Mejor Opción?

La moda brilla donde las matemáticas fallan.

1.  **Datos Cualitativos:** No puedes promediar "Rojo" y "Azul". La moda es tu única opción.
2.  **Inventarios:** Saber la talla más vendida es más útil que la "talla promedio".
3.  **Votaciones:** El presidente es la "Moda" de los candidatos.

### ⚙️ Ejemplos Resueltos: Casos de Uso

#### Ejemplo 1: Elecciones
**Datos:** Candidato A (40%), B (30%), C (30%).
**Análisis:** No existe "Candidato 1.5".
**Mejor Medida:** Moda (Candidato A).

#### Ejemplo 2: Fabricación
**Datos:** Diámetros de tuberías más usados.
**Análisis:** Si el promedio es 2.5cm pero nadie compra esa medida, no sirve. Si la mayoría compra 2.0cm, fabrica eso.
**Mejor Medida:** Moda.

#### Ejemplo 3: Tráfico Web
**Datos:** Páginas más visitadas.
**Análisis:** Necesitas saber qué contenido optimizar.
**Mejor Medida:** Moda (La página con más visitas).

#### Ejemplo 4: Errores comunes
**Datos:** Tipos de quejas de clientes.
**Análisis:** ¿Cuál es la queja más frecuente para arreglarla primero?
**Mejor Medida:** Moda (Pareto).

#### Ejemplo 5: Horas Pico
**Datos:** Hora con más pasajeros en el metro.
**Análisis:** Para programar más trenes.
**Mejor Medida:** Moda.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la moda de: 3, 3, 5, 6, 9, 3, 6.

<details>
<summary>Ver solución</summary>

**Conteo:** El 3 aparece tres veces. El 6 dos veces.
**Resultado:** $\boxed{3}$

</details>

### Ejercicio 2
Si todos los estudiantes de un salón tienen 15 años, ¿cuál es la moda?

<details>
<summary>Ver solución</summary>

**Datos:** 15, 15, 15...
**Análisis:** Al ser el único valor, es el más repetido.
**Resultado:** $\boxed{15}$

</details>

### Ejercicio 3
Encuentra la moda de los colores: Rojo, Azul, Rojo, Verde, Verde, Verde, Azul.

<details>
<summary>Ver solución</summary>

**Conteo:** Verde (3), Rojo (2), Azul (2).
**Resultado:** $\boxed{\text{Verde}}$

</details>

### Ejercicio 4
En una tabla, la Frecuencia más alta es 50 y corresponde al valor $X=10$. ¿Cuál es la moda, 50 o 10?

<details>
<summary>Ver solución</summary>

**Concepto:** La moda es el valor del dato, no su frecuencia.
**Resultado:** $\boxed{10}$

</details>

### Ejercicio 5
Halla la moda de: 1, 2, 3, 4, 5.

<details>
<summary>Ver solución</summary>

**Análisis:** Todos tienen frecuencia 1. No hay ganador.
**Resultado:** $\boxed{\text{Amodal (No tiene)}}$

</details>

### Ejercicio 6
Si tienes dos modas lejanas (ej: notas 1.0 y 5.0), ¿qué te dice esto sobre el grupo?

<details>
<summary>Ver solución</summary>

**Interpretación:** El grupo está polarizado. Hay dos subgrupos muy distintos (los que saben mucho y los que no saben nada).
**Resultado:** $\boxed{\text{Población dividida (Bimodal)}}$

</details>

### Ejercicio 7
Calcula la moda de: 9, 10, 11, 10, 9.

<details>
<summary>Ver solución</summary>

**Conteo:** 9(2), 10(2), 11(1).
**Resultado:** $\boxed{9 \text{ y } 10}$

</details>

### Ejercicio 8
¿Puede la moda ser igual a la media y la mediana?

<details>
<summary>Ver solución</summary>

**Caso:** Distribución perfectamente simétrica y unimodal.
**Resultado:** $\boxed{\text{Sí}}$

</details>

### Ejercicio 9
En una encuesta de satisfacción "Sí/No", hubo 40 Sí y 60 No. ¿Cuál es la moda?

<details>
<summary>Ver solución</summary>

**Mayoría:** No (60).
**Resultado:** $\boxed{\text{No}}$

</details>

### Ejercicio 10
Si agregas un dato que es igual a la moda actual, ¿la moda cambia?

<details>
<summary>Ver solución</summary>

**Análisis:** Si agregas más votos al ganador, sigue ganando.
**Resultado:** $\boxed{\text{No, se refuerza}}$

</details>

---

## 🔑 Resumen

| Concepto | Definición | Clave |
|----------|------------|-------|
| **Moda** | Valor más frecuente ($Max \ f_i$). | Útil para cualitativos ("lo popular"). |
| **Bimodal** | Dos picos de frecuencia. | Indica dos grupos mezclados. |
| **Amodal** | Frecuencias iguales. | Datos planos o insuficientes. |

> **Conclusión:** La moda es simple pero poderosa. Es la reina de la democracia estadística: gana la mayoría simple.
