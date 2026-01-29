# **Introducción a las Transformaciones Geométricas**

¿Alguna vez has jugado un videojuego? Cuando tu personaje camina, salta, gira o se hace pequeño al tomar una poción, el motor gráfico está aplicando matemáticas puras: **transformaciones geométricas**. Sin ellas, nada se movería en la pantalla.

---

## 🎯 ¿Qué vas a aprender?

- Definir qué es una transformación geométrica (mover puntos de un lugar a otro).
- Distinguir entre movimientos rígidos (**isometrías**) y cambios de tamaño (**semejanzas**).
- Identificar los 4 tipos principales: Traslación, Rotación, Reflexión y Homotecia.
- Entender qué propiedades se conservan en cada caso.

---

## 🔄 ¿Qué es una Transformación?

Imagina el plano cartesiano como una lámina elástica infinita. Una transformación es una regla que toma cada punto $P$ (punto original) y lo mueve a una nueva posición $P'$ (imagen).

$$
T(P) = P'
$$

Puede deslizarse, girar, voltearse o estirarse.

---

## 📏 Tipos de Transformaciones

Las clasificamos según **qué le hacen a la figura**:

### 1. Isometrías (Movimientos Rígidos)
La figura **mantiene su tamaño y forma exacta**. Si recortaras la figura original, encajaría perfectamente sobre la nueva.
*   **Traslación** (Deslizar)
*   **Rotación** (Girar)
*   **Reflexión** (Espejar)

> **Propiedades que conservan:** Distancias, Ángulos, Áreas, Rectas paralelas.

### 2. Semejanzas (Cambios de Escala)
La figura **mantiene su forma**, pero **cambia de tamaño**.
*   **Homotecia** (Ampliación o Reducción)

> **Propiedades que conservan:** Ángulos, Rectas paralelas.
> **Propiedades que NO conservan:** Distancias, Áreas.

---

## 🕵️ Galería de Transformaciones

### A. Traslación (Deslizar)
Mueve todos los puntos en la misma dirección y distancia.
*   *Ejemplo:* Un ascensor subiendo, un coche avanzando en línea recta.

### B. Rotación (Girar)
Gira la figura alrededor de un punto fijo (centro).
*   *Ejemplo:* Las manecillas del reloj, una rueda de la fortuna.

### C. Reflexión (Reflejar)
Crea una imagen de espejo al otro lado de una línea (eje).
*   *Ejemplo:* Tu reflejo en un espejo, una mariposa abriendo las alas.

### D. Homotecia (Escalar)
Hace la figura más grande (Zoom In) o más pequeña (Zoom Out) desde un punto central.
*   *Ejemplo:* Un proyector de cine, la pupila dilatándose.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Identificación

Un cuadrado de lado 4 cm se transforma en otro cuadrado de lado 4 cm, pero desplazado 10 cm a la derecha. ¿Qué transformación es?

**Razonamiento:**
1.  ¿Cambió de tamaño? No ($4 \to 4$). Es una isometría.
2.  ¿Giró o se reflejó? No, solo se desplazó.

**Resultado:**
$$
\boxed{\text{Traslación}}
$$

### Ejemplo 2: Propiedades

Una transformación convierte un triángulo de área 10 m² en uno de área 40 m². ¿Es una isometría?

**Razonamiento:**
Las isometrías conservan el área (el tamaño no cambia).
Aquí el área aumentó ($10 \to 40$).

**Resultado:**
$$
\boxed{\text{No, es una semejanza (Homotecia)}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si giras tu teléfono para ver un video horizontalmente, ¿qué transformación aplicaste a la pantalla?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Rotación}
$$

</details>

### Ejercicio 2
Un arquitecto hace una maqueta a escala de un edificio. ¿Qué transformación relaciona la maqueta con el edificio real?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Homotecia (Semejanza)}
$$

</details>

### Ejercicio 3
Miras tu mano derecha en el espejo y parece una mano izquierda. ¿Qué transformación es?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El espejo invierte lateralmente la imagen.

**Resultado:**
$$
\boxed{\text{Reflexión}}
$$

</details>

### Ejercicio 4
Verdadero o Falso: Una rotación cambia la longitud de los lados de un polígono.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Falso. La rotación es una isometría (rígida).

**Resultado:**
$$
\boxed{\text{Falso}}
$$

</details>

### Ejercicio 5
Si mueves una silla de la cocina a la sala arrastrándola, ¿es una traslación o una homotecia?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Traslación}
$$

</details>

### Ejercicio 6
¿Qué tipo de transformación es "Copiar y Pegar" un archivo en el escritorio (si lo mueves de lugar)?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Traslación}
$$

</details>

### Ejercicio 7
En una isometría, si el segmento $AB$ mide 5 metros, ¿cuánto mide el segmento $A'B'$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La distancia se conserva.

**Resultado:**
$$
\boxed{5 \text{ metros}}
$$

</details>

### Ejercicio 8
Nombra la única transformación que tiene un "Eje de simetría".

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Reflexión}
$$

</details>

### Ejercicio 9
Si duplicas el tamaño de una foto digital, ¿es una isometría?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No, porque cambias el tamaño.

**Resultado:**
$$
\boxed{\text{No}}
$$

</details>

### Ejercicio 10
¿Qué punto permanece quieto en una rotación?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{El Centro de Rotación}
$$

</details>

---

## 🔑 Resumen

| Transformación | Acción | ¿Conserva tamaño? |
| :--- | :--- | :---: |
| **Traslación** | Deslizar | Sí |
| **Rotación** | Girar | Sí |
| **Reflexión** | Espejar | Sí |
| **Homotecia** | Escalar | No |

> Las isometrías son como mover muebles rígidos. La homotecia es como inflar globos.
