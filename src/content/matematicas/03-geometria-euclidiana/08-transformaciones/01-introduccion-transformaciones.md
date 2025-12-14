# Introducción a las Transformaciones Geométricas

Las **transformaciones geométricas** son operaciones que cambian la posición, tamaño u orientación de las figuras en el plano, preservando ciertas propiedades.

---

## 📖 ¿Qué es una transformación geométrica?

> **Definición:** Una transformación geométrica es una regla que asigna a cada punto del plano un nuevo punto, llamado su **imagen**.

Si el punto $P$ se transforma en $P'$:
- $P$ es el **original** (o preimagen)
- $P'$ es la **imagen**

---

## 📖 Tipos de transformaciones

### Por conservación de tamaño

| Tipo | ¿Conserva tamaño? | ¿Conserva forma? |
|------|-------------------|------------------|
| Isometría | Sí | Sí |
| Semejanza | No | Sí |
| Otras | No | No |

### Isometrías (movimientos rígidos)

Las **isometrías** conservan la forma y el tamaño de la figura:
- Traslación
- Rotación
- Reflexión (simetría)

### Semejanzas

Las **semejanzas** conservan solo la forma:
- Homotecia (ampliación/reducción)
- Composición de isometrías con homotecia

---

## 📖 Propiedades que conservan las isometrías

| Propiedad | ¿Se conserva? |
|-----------|---------------|
| Distancias | Sí |
| Ángulos | Sí |
| Paralelismo | Sí |
| Perpendicularidad | Sí |
| Área | Sí |
| Forma | Sí |

---

## 📖 Las cuatro transformaciones principales

### 1. Traslación

Mueve todos los puntos la **misma distancia** en la **misma dirección**.

### 2. Rotación

Gira todos los puntos alrededor de un **centro** un **cierto ángulo**.

### 3. Reflexión (Simetría)

Refleja los puntos respecto a una **recta eje** (como en un espejo).

### 4. Homotecia

Amplía o reduce la figura desde un **centro** con una **razón** dada.

---

## 📖 Notación

Para indicar que aplicamos una transformación $T$ a un punto $P$:

$$
T(P) = P'
$$

Para una figura $F$:

$$
T(F) = F'
$$

---

## 📖 Composición de transformaciones

Podemos aplicar una transformación después de otra. Si aplicamos $T_1$ y luego $T_2$:

$$
(T_2 \circ T_1)(P) = T_2(T_1(P))
$$

Se lee: "Primero $T_1$, luego $T_2$"

### Ejemplo

Rotar 90° y luego trasladar es diferente de trasladar y luego rotar 90°.

> **Nota:** En general, el orden importa.

---

## 📖 Elementos invariantes

Un **punto invariante** (o fijo) es un punto que no cambia con la transformación:

$$
T(P) = P
$$

### Ejemplos

- En una **rotación**: solo el centro es invariante
- En una **reflexión**: todos los puntos del eje son invariantes
- En una **traslación**: ningún punto es invariante (excepto si el vector es cero)

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificar transformaciones

¿Cuál transformación se aplicó?

1. Una figura se movió 5 cm a la derecha sin girar ni cambiar de tamaño
2. Una figura giró 90° alrededor de un punto
3. Una figura se ve como en un espejo
4. Una figura se amplió al doble de su tamaño

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Traslación**
2. **Rotación**
3. **Reflexión**
4. **Homotecia**

</details>

---

### Ejercicio 2: Isometría o no

Indica si cada transformación es una isometría:

1. Rotar 45°
2. Ampliar al triple
3. Trasladar 10 unidades
4. Reducir a la mitad

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Sí** (conserva tamaño y forma)
2. **No** (cambia el tamaño)
3. **Sí** (conserva tamaño y forma)
4. **No** (cambia el tamaño)

</details>

---

### Ejercicio 3: Verdadero o Falso

1. Todas las isometrías conservan las distancias.
2. La composición de dos traslaciones es siempre una traslación.
3. En una rotación, solo el centro permanece fijo.
4. Las transformaciones siempre se aplican en el mismo orden.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero** - Por definición de isometría
2. **Verdadero** - La suma de vectores da otro vector
3. **Verdadero** - El centro es el único punto fijo
4. **Falso** - El orden puede variar y afecta el resultado

</details>

---
