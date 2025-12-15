# Principio de Multiplicación y Adición

Antes de calcular probabilidades, necesitamos saber **contar**: ¿cuántos resultados posibles hay? Las **técnicas de conteo** nos dan herramientas sistemáticas para responder esta pregunta sin tener que listar todo.

---

## 🎯 ¿Qué vas a aprender?

- El principio fundamental de conteo (multiplicación)
- El principio de adición
- Cuándo usar cada uno
- Aplicaciones prácticas

---

## 📊 Resumen de Principios

| Principio | Cuándo usarlo | Fórmula |
|-----------|---------------|---------|
| **Multiplicación** | Etapas **consecutivas** (Y) | $n_1 \times n_2 \times ... \times n_k$ |
| **Adición** | Opciones **excluyentes** (O) | $n_1 + n_2 + ... + n_k$ |

---

## 📖 Principio de Multiplicación

> Si una tarea se puede realizar en **k etapas**, donde la etapa 1 tiene $n_1$ opciones, la etapa 2 tiene $n_2$ opciones, y así sucesivamente, entonces el **total de maneras** de completar la tarea es:

$$
\text{Total} = n_1 \times n_2 \times n_3 \times ... \times n_k
$$

### 💡 Palabra clave: "Y"

El principio de multiplicación aplica cuando las etapas ocurren **consecutivamente** (primero esto Y luego aquello).

### ⚙️ Ejemplo 1: Vestirse

Tienes:
- 4 camisas
- 3 pantalones
- 2 pares de zapatos

¿De cuántas maneras diferentes puedes vestirte?

**Etapa 1:** Elegir camisa → 4 opciones
**Etapa 2:** Elegir pantalón → 3 opciones
**Etapa 3:** Elegir zapatos → 2 opciones

$$
\text{Total} = 4 \times 3 \times 2 = 24 \text{ combinaciones}
$$

### ⚙️ Ejemplo 2: Placas de vehículos

Una placa tiene formato: 3 letras seguidas de 3 dígitos (ABC-123).

- Letras: 26 opciones para cada una
- Dígitos: 10 opciones para cada uno (0-9)

$$
\text{Total} = 26 \times 26 \times 26 \times 10 \times 10 \times 10 = 26^3 \times 10^3
$$
$$
= 17,576 \times 1,000 = 17,576,000 \text{ placas posibles}
$$

### ⚙️ Ejemplo 3: Contraseñas

Una contraseña tiene 4 caracteres:
- Posición 1: debe ser letra mayúscula (26 opciones)
- Posiciones 2-3: cualquier letra o dígito (36 opciones cada una)
- Posición 4: debe ser dígito (10 opciones)

$$
\text{Total} = 26 \times 36 \times 36 \times 10 = 336,960 \text{ contraseñas}
$$

---

## 📖 Principio de Adición

> Si una tarea se puede realizar de **manera A** (con $n_A$ opciones) **O** de **manera B** (con $n_B$ opciones), y las maneras son **mutuamente excluyentes**, entonces:

$$
\text{Total} = n_A + n_B
$$

### 💡 Palabra clave: "O"

El principio de adición aplica cuando hay opciones **alternativas** que se excluyen mutuamente (esto O aquello, pero no ambos).

### ⚙️ Ejemplo 1: Transporte al trabajo

Puedes ir al trabajo:
- En metro: 3 rutas posibles
- En bus: 5 rutas posibles
- En bicicleta: 2 rutas posibles

¿De cuántas maneras puedes llegar?

$$
\text{Total} = 3 + 5 + 2 = 10 \text{ maneras}
$$

### ⚙️ Ejemplo 2: Elegir representante

De un grupo de 12 hombres y 8 mujeres, ¿de cuántas formas puedes elegir UN representante?

$$
\text{Total} = 12 + 8 = 20 \text{ formas}
$$

---

## 📖 Combinando Ambos Principios

Muchos problemas requieren usar **ambos principios**.

### ⚙️ Ejemplo: Menú de restaurante

Un restaurante ofrece:
- **Entrada:** Ensalada (2 tipos) O sopa (3 tipos)
- **Plato fuerte:** 4 opciones
- **Postre:** 3 opciones

¿Cuántos menús diferentes hay?

**Paso 1:** Opciones de entrada (Adición porque es O)
$2 + 3 = 5$ opciones

**Paso 2:** Menú completo (Multiplicación porque es Y)
$5 \times 4 \times 3 = 60$ menús diferentes

### ⚙️ Ejemplo: Comités

De 5 profesores y 8 estudiantes, ¿de cuántas formas puedes elegir un comité de 2 personas que incluya 1 profesor Y 1 estudiante?

**Paso 1:** Elegir profesor → 5 opciones
**Paso 2:** Elegir estudiante → 8 opciones

$$
\text{Total} = 5 \times 8 = 40 \text{ comités posibles}
$$

---

## 📖 El Problema de las Restricciones

### ⚙️ Ejemplo: Números de 3 dígitos sin repetición

¿Cuántos números de 3 dígitos se pueden formar con los dígitos 1, 2, 3, 4, 5 sin repetir?

**Posición 1 (centenas):** 5 opciones (cualquiera)
**Posición 2 (decenas):** 4 opciones (ya usamos uno)
**Posición 3 (unidades):** 3 opciones (ya usamos dos)

$$
\text{Total} = 5 \times 4 \times 3 = 60 \text{ números}
$$

### ⚙️ Ejemplo: Números pares de 3 dígitos sin repetición

Con los mismos dígitos 1, 2, 3, 4, 5, ¿cuántos son **pares**?

Un número es par si termina en dígito par: 2 o 4.

**Estrategia:** Empezar por la restricción más fuerte.

**Paso 1:** Posición 3 (unidades, debe ser par) → 2 opciones (2 o 4)
**Paso 2:** Posición 1 (centenas) → 4 opciones (los 5 menos el usado)
**Paso 3:** Posición 2 (decenas) → 3 opciones (los 5 menos los 2 usados)

$$
\text{Total} = 2 \times 4 \times 3 = 24 \text{ números pares}
$$

---

## 💡 ¿Multiplicación o Adición?

| Pregunta mental | Principio |
|-----------------|-----------|
| "¿Las elecciones son consecutivas?" | **Multiplicación** |
| "¿Las opciones son alternativas excluyentes?" | **Adición** |
| "La palabra clave es Y" | **Multiplicación** |
| "La palabra clave es O" | **Adición** |

---

## 🔑 Resumen

| Principio | Cuándo usarlo | Operación |
|-----------|---------------|-----------|
| **Multiplicación** | Etapas consecutivas (Y) | Multiplicar opciones |
| **Adición** | Alternativas excluyentes (O) | Sumar opciones |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Una pizzería ofrece:
- 3 tamaños
- 8 tipos de masa
- 15 ingredientes principales

¿Cuántas pizzas diferentes puedes pedir?

<details>
<summary>Ver solución</summary>

Cada elección es consecutiva (tamaño Y masa Y ingrediente):

$$\text{Total} = 3 \times 8 \times 15 = 360 \text{ pizzas}$$

</details>

### Ejercicio 2
¿Cuántos números de 4 dígitos hay (desde 1000 hasta 9999)?

<details>
<summary>Ver solución</summary>

- **Posición 1 (miles):** 9 opciones (1-9, no puede ser 0)
- **Posición 2 (centenas):** 10 opciones (0-9)
- **Posición 3 (decenas):** 10 opciones (0-9)
- **Posición 4 (unidades):** 10 opciones (0-9)

$$\text{Total} = 9 \times 10 \times 10 \times 10 = 9,000$$

**Verificación:** 9999 - 1000 + 1 = 9,000 ✓

</details>

### Ejercicio 3
¿De cuántas formas puedes formar una comisión de 3 personas de un grupo de 10, si el orden importa (presidente, vicepresidente, secretario)?

<details>
<summary>Ver solución</summary>

- Presidente: 10 opciones
- Vicepresidente: 9 opciones (ya elegimos presidente)
- Secretario: 8 opciones (ya elegimos 2)

$$\text{Total} = 10 \times 9 \times 8 = 720$$

</details>

### Ejercicio 4
De 6 libros de ficción y 4 de no ficción, ¿de cuántas formas puedes elegir 1 libro para leer?

<details>
<summary>Ver solución</summary>

Puedes elegir un libro de ficción O uno de no ficción:

$$\text{Total} = 6 + 4 = 10$$

</details>

### Ejercicio 5
Con los dígitos 1, 2, 3, 4, 5, 6, ¿cuántos números de 3 dígitos mayores a 400 se pueden formar sin repetir dígitos?

<details>
<summary>Ver solución</summary>

**Restricción:** El primer dígito debe ser 4, 5, o 6 (para ser > 400).

**Paso 1:** Posición 1 (centenas) → 3 opciones (4, 5, 6)
**Paso 2:** Posición 2 → 5 opciones (los 6 menos el usado)
**Paso 3:** Posición 3 → 4 opciones (los 6 menos los 2 usados)

$$\text{Total} = 3 \times 5 \times 4 = 60$$

</details>
