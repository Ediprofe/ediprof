---
title: "Muestreo Probabilístico"
---

# **Muestreo Probabilístico**

Si vas a elegir una muestra, no lo hagas "a dedo". Para que la estadística funcione, la elección debe ser dejada al azar. Esto garantiza que todos tengan la misma oportunidad y elimina tus prejuicios.

---

## 🎯 ¿Qué vas a aprender?

- Aleatorio Simple vs Sistemático.
- Técnicas avanzadas: Estratificado y Conglomerados.
- Cómo usar un generador de números aleatorios.

---

## 🎲 Concepto 1: Métodos Básicos (Simple y Sistemático)

Son los más fáciles de entender. Requieren tener una lista completa de la población (Marco Muestral).

### 1. Aleatorio Simple
Es la lotería pura. Nombres en un sombrero o Excel `RAND()`.

### 2. Sistemático
Eliges uno al azar y luego saltas de $k$ en $k$ (ej. cada 10 personas).

**5 Ejemplos de Aplicación:**

### Ejemplo 1.1: Rifas (Simple)
Tienes 100 boletas. Sacas 3 papeles de una bolsa.
*   Totalmente al azar.

### Ejemplo 1.2: Control de Calidad (Sistemático)
En una banda transportadora de botellas, un robot revisa la botella #5, #105, #205...
*   Intervalo $k=100$.

### Ejemplo 1.3: Encuesta a Empleados (Simple)
La empresa tiene 500 empleados. Usas Excel para elegir 50 ID al azar.

### Ejemplo 1.4: Entrada al Cine (Sistemático)
Encuestas a la persona #10, #20, #30... que entra a la sala.
*   Riesgo: Si entran parejas (2 en 2), podrías encuestar siempre al hombre o siempre a la mujer si tu intervalo sincroniza con el patrón.

### Ejemplo 1.5: Bingo (Simple)
Las balotas salen de la máquina. No hay orden ni patrón.

---

## 🏗️ Concepto 2: Métodos Estructurados (Estratificado y Conglomerados)

Cuando la población es compleja o gigante, el azar simple no basta o es muy caro.

### 3. Estratificado
Divides la población en grupos "estratos" (Homogéneos adentro) y sacas muestra de **todos**. Asegura representatividad perfecta.

### 4. Conglomerados
Divides en grupos "clusters" (Heterogéneos adentro) y eliges **algunos** grupos completos. Ahorra dinero.

**5 Ejemplos Comparativos:**

### Ejemplo 2.1: Encuesta Universitaria (Estratificado)
Quieres representar bien a todas las carreras.
*   Estratos: Ingeniería, Artes, Medicina.
*   Sacas el 10% de Ingenieros, 10% de Artistas, 10% de Médicos.
*   *Garantía:* Ninguna carrera queda fuera.

### Ejemplo 2.2: Estudio de Barrios (Conglomerados)
Quieres estudiar familias en Bogotá. No puedes ir a todas las casas.
*   Conglomerados: Manzanas (Cuadras).
*   Eliges 20 manzanas al azar y encuestas a **todas** las casas de esas 20 manzanas.
*   *Ahorro:* Menos desplazamiento.

### Ejemplo 2.3: Sondeo Nacional (Multi-etápico)
Primero eliges Departamentos (Conglomerado), luego Municipios, luego Barrios, luego Casas.

### Ejemplo 2.4: Brecha Salarial (Estratificado)
Estratas por Género (Hombre/Mujer) para asegurar que tienes suficientes datos de ambos para comparar.

### Ejemplo 2.5: Calidad de Cajas de Fruta (Conglomerados)
Llegan 100 camiones con cajas de naranjas.
*   Eliges 5 cajas al azar (Conglomerados).
*   Revisas las 50 naranjas de esas 5 cajas.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Diferencia entre Estratificado y Conglomerados.

<details>
<summary>Ver solución</summary>
Estratificado = Muestra de TODOS los grupos. Conglomerados = Muestra de ALGUNOS grupos.
</details>

---

### Ejercicio 2
¿Qué método usa una tómbola?

<details>
<summary>Ver solución</summary>
Aleatorio Simple.
</details>

---

### Ejercicio 3
Riesgo del muestreo sistemático.

<details>
<summary>Ver solución</summary>
Periodicidad. Si el intervalo coincide con un patrón oculto en la lista (ej. siempre lunes).
</details>

---

### Ejercicio 4
Si quiero dividir por estratos socioeconómicos (1 a 6).

<details>
<summary>Ver solución</summary>
Muestreo Estratificado.
</details>

---

### Ejercicio 5
¿Cuál método es más barato geográficamente?

<details>
<summary>Ver solución</summary>
Conglomerados (concentra el trabajo de campo).
</details>

---

### Ejercicio 6
Fórmula del intervalo sistemático ($k$).

<details>
<summary>Ver solución</summary>
$k = N/n$. (Población / Muestra deseada).
</details>

---

### Ejercicio 7
¿Qué significa "Probabilístico"?

<details>
<summary>Ver solución</summary>
Que se conoce la probabilidad de elección de cada sujeto ($P > 0$).
</details>

---

### Ejercicio 8
Ejemplo de muestreo NO probabilístico (Malo).

<details>
<summary>Ver solución</summary>
Muestreo por Conveniencia (preguntar al que pase por la calle).
</details>

---

### Ejercicio 9
Si en un estrato hay más gente, ¿saco más muestra?

<details>
<summary>Ver solución</summary>
Sí, se llama Afijación Proporcional. (Más gente = Más muestra).
</details>

---

### Ejercicio 10
Herramienta tecnológica para muestrear.

<details>
<summary>Ver solución</summary>
Generadores de números pseudoaleatorios (R, Python, Excel).
</details>

---

## 🔑 Resumen

| Método | Lema |
| :--- | :--- |
| **Aleatorio Simple** | "La suerte es loca". |
| **Sistemático** | "Cuenta pasos (1, 2, 3... Tú)". |
| **Estratificado** | "Un poco de todo (Ensalada)". |
| **Conglomerados** | "Toma el paquete completo". |

> **Conclusión:** El azar bien diseñado es la única forma de eliminar el sesgo humano. Confía en los dados.
