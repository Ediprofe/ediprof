# Diagrama de Dispersión

Hasta ahora hemos analizado **una variable** a la vez. Pero muchas preguntas interesantes involucran **dos variables**: ¿Hay relación entre horas de estudio y notas? ¿Entre altura y peso? El **diagrama de dispersión** nos ayuda a visualizar estas relaciones.

---

## 🎯 ¿Qué vas a aprender?

- Qué es un diagrama de dispersión
- Cómo construirlo e interpretarlo
- Identificar tipos de relación entre variables
- Detectar patrones y valores atípicos

---

## 📖 ¿Qué es un Diagrama de Dispersión?

> Un **diagrama de dispersión** (o nube de puntos) es un gráfico donde cada punto representa un par de valores $(x_i, y_i)$ de dos variables.

### 💡 Estructura:
- **Eje X (horizontal):** Variable explicativa o independiente
- **Eje Y (vertical):** Variable respuesta o dependiente
- **Cada punto:** Un caso u observación

---

## 📖 Construcción del Diagrama

### ⚙️ Ejemplo: Horas de estudio vs Nota

| Estudiante | Horas (X) | Nota (Y) |
|------------|-----------|----------|
| Ana | 2 | 55 |
| Luis | 4 | 65 |
| María | 3 | 60 |
| Carlos | 5 | 75 |
| Sofía | 6 | 80 |
| Pedro | 1 | 45 |
| Laura | 7 | 90 |
| Diego | 4 | 70 |

**Paso 1:** Definir ejes
- Eje X: Horas de estudio (0 a 8)
- Eje Y: Nota (0 a 100)

**Paso 2:** Ubicar cada punto
- Ana: (2, 55)
- Luis: (4, 65)
- ... y así sucesivamente

**Resultado:** Una nube de puntos que muestra la relación entre horas y notas.

---

## 📖 Tipos de Relación

### 💡 Relación Positiva (Directa)

```
    Y ↑
      │         ●
      │       ●
      │     ●
      │   ●
      │ ●
      └─────────→ X
```

**Cuando X aumenta, Y también aumenta.**

Ejemplos:
- Horas de estudio → Notas
- Altura → Peso
- Años de experiencia → Salario

### 💡 Relación Negativa (Inversa)

```
    Y ↑
      │ ●
      │   ●
      │     ●
      │       ●
      │         ●
      └─────────→ X
```

**Cuando X aumenta, Y disminuye.**

Ejemplos:
- Precio → Cantidad demandada
- Velocidad → Tiempo de viaje
- Ejercicio → Peso corporal

### 💡 Sin Relación (Dispersión aleatoria)

```
    Y ↑
      │  ●    ●
      │    ●
      │ ●      ●
      │   ●  ●
      │  ●  ●
      └─────────→ X
```

**No hay patrón claro; X e Y no están relacionadas.**

Ejemplos:
- Número de zapato → Nota en matemáticas
- Color de ojos → Altura

---

## 📖 Fuerza de la Relación

### 💡 Relación fuerte:

Los puntos están **muy cerca** de una línea imaginaria.

```
      │        /●
      │      /●
      │    /●
      │  /●
      │/●
      └─────────→
```

### 💡 Relación débil:

Los puntos están **dispersos** alrededor de una tendencia.

```
      │      ●  ●
      │    ●  ●
      │  ●  ●
      │    ●
      │  ●
      └─────────→
```

### 💡 Sin relación:

Dispersión **aleatoria** sin ningún patrón.

---

## 📖 Forma de la Relación

### 💡 Relación lineal:

Los puntos siguen aproximadamente una **línea recta**.

### 💡 Relación curvilínea:

Los puntos siguen una **curva**.

```
      │         ●●●
      │       ●
      │     ●
      │   ●
      │ ●●
      └─────────→
```

Ejemplo: Rendimiento vs horas de trabajo (al principio mejora, luego el cansancio lo reduce)

---

## 📖 Valores Atípicos (Outliers)

En un diagrama de dispersión, un **outlier** es un punto que está **muy alejado** del patrón general.

### ⚙️ Ejemplo:

```
      │           ● (outlier)
      │
      │    /●
      │  /●
      │/●
      └─────────→
```

El punto superior derecho puede ser:
- Un error de medición
- Un caso genuinamente diferente
- Un valor que merece investigación

---

## 📖 Interpretación: Lo que NO muestra el diagrama

### ⚠️ Correlación no implica causalidad

Que dos variables estén relacionadas **no significa** que una cause la otra.

### ⚙️ Ejemplo:

Hay correlación entre ventas de helados y muertes por ahogamiento.

¿Los helados causan ahogamientos? **No.**

Ambas variables están relacionadas con una **tercera variable**: el calor del verano.

---

## 💡 Preguntas que Responde el Diagrama

| Pregunta | Cómo responderla |
|----------|------------------|
| ¿Hay relación? | ¿Los puntos siguen algún patrón? |
| ¿Es positiva o negativa? | ¿Suben juntos o uno sube y otro baja? |
| ¿Qué tan fuerte es? | ¿Los puntos están cerca o dispersos? |
| ¿Es lineal o curva? | ¿Siguen una línea recta u otra forma? |
| ¿Hay outliers? | ¿Hay puntos muy alejados del patrón? |

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Diagrama de dispersión** | Gráfico de puntos $(x_i, y_i)$ |
| **Relación positiva** | X e Y aumentan juntas |
| **Relación negativa** | Una aumenta, otra disminuye |
| **Sin relación** | Puntos dispersos aleatoriamente |
| **Outlier** | Punto alejado del patrón general |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Indica si esperarías una relación positiva, negativa o ninguna entre:

a) Temperatura exterior y consumo de aire acondicionado
b) Edad de un carro y su precio de reventa
c) Número de hermanos y estatura
d) Horas de sueño y nivel de cansancio

<details>
<summary>Ver solución</summary>

a) **Positiva:** Más calor → más uso de A/C

b) **Negativa:** Más viejo → menor precio

c) **Sin relación:** No hay conexión lógica entre ambas

d) **Negativa:** Más sueño → menos cansancio

</details>

### Ejercicio 2
Observa esta descripción de puntos y determina el tipo de relación:

"Los puntos forman una línea que baja de izquierda a derecha, y están bastante cerca de esa línea imaginaria."

<details>
<summary>Ver solución</summary>

**Relación negativa fuerte**

- "Baja de izquierda a derecha" → Negativa (cuando X sube, Y baja)
- "Bastante cerca de la línea" → Fuerte (poco dispersos)

</details>

### Ejercicio 3
En un estudio, se encuentra que los países con más consumo de chocolate también tienen más premios Nobel. ¿El chocolate hace más inteligentes a las personas?

<details>
<summary>Ver solución</summary>

**No podemos concluir causalidad.**

**Correlación ≠ Causalidad**

Posibles explicaciones:
1. **Variable oculta:** Los países ricos tienen más acceso tanto a chocolate como a educación de calidad
2. **Coincidencia estadística:** Podría ser solo azar
3. **Causalidad inversa:** Quizás los países con más premios Nobel celebran más con chocolate (absurdo, pero ilustra el punto)

**Conclusión:** El diagrama de dispersión muestra que existe una relación, pero no puede demostrar que una variable CAUSA la otra.

</details>

### Ejercicio 4
¿Por qué es importante buscar outliers en un diagrama de dispersión antes de calcular correlaciones?

<details>
<summary>Ver solución</summary>

Es importante porque:

1. **Distorsionan la correlación:** Un solo outlier puede hacer que una correlación parezca más fuerte o más débil de lo real.

2. **Pueden indicar errores:** El outlier podría ser un dato mal registrado.

3. **Pueden ser casos especiales:** Merecen investigación individual (¿por qué es diferente?).

4. **Afectan la línea de regresión:** Si calculamos una recta de mejor ajuste, el outlier la "jala" hacia él.

**Mejor práctica:** Siempre graficar primero, identificar outliers, investigarlos, y luego decidir si incluirlos en el análisis.

</details>
