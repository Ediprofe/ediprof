# **La Mediana**

Imagina que estás en una fila de 5 personas ordenadas por estatura. La persona que está exactamente en el medio es la referencia central. Si llega un jugador de baloncesto de 2.20m al final de la fila, la persona del medio sigue siendo la misma. Esa es la magia de la **Mediana**: es el valor central de los datos ordenados, y es inmune a los exagerados.

---

## 🎯 ¿Qué vas a aprender?

- Calcular la mediana para un número impar de datos (el del medio).
- Calcular la mediana para un número par de datos (el promedio de los dos del medio).
- Encontrar la mediana en una tabla de frecuencias acumuladas.
- Entender por qué la mediana es "honesta" frente a datos extremos.

---

## Datos Simples: El Arte de Ordenar

**Regla de Oro:** ¡ORDENA PRIMERO! Sin orden, no hay mediana.
Posición del centro: $\frac{n+1}{2}$.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Datos Impares (El solitario)
**Datos:** 5, 2, 9, 1, 6. ($n=5$).
**1. Ordenar:** 1, 2, **5**, 6, 9.
**2. Posición:** $(5+1)/2 = 3$. Buscamos el 3er dato.
**Mediana:** $\boxed{5}$

#### Ejemplo 2: Datos Pares (La pareja)
**Datos:** 10, 20, 30, 40. ($n=4$).
**1. Ordenar:** Ya están ordenados.
**2. Posición:** $(4+1)/2 = 2.5$. El centro está entre el dato 2 y 3.
**3. Promedio:** $(20+30)/2 = 25$.
**Mediana:** $\boxed{25}$

#### Ejemplo 3: El Intruso (Outlier)
**Datos:** 1, 2, 3, 1000. ($n=4$).
**Centro:** Entre 2 y 3.
**Cálculo:** $(2+3)/2 = 2.5$.
**Mediana:** $\boxed{2.5}$ (Nota cómo el 1000 no afectó el resultado).

#### Ejemplo 4: Muchos datos iguales
**Datos:** 7, 7, 7, 7, 8. ($n=5$).
**1. Ordenar:** 7, 7, **7**, 7, 8.
**Mediana:** $\boxed{7}$

#### Ejemplo 5: Decimales
**Datos:** 1.5, 0.2, 3.1, 2.2, 1.8.
**1. Ordenar:** 0.2, 1.5, **1.8**, 2.2, 3.1.
**Mediana:** $\boxed{1.8}$

---

## Mediana en Tablas de Frecuencia

Aquí no vemos "una fila", vemos una lista de cantidades. Usamos la **Frecuencia Acumulada ($F_i$)** para encontrar la posición central $n/2$.
Buscamos el primer valor cuya $F_i$ sea **mayor o igual** a $n/2$.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Notas (1-5)
**Tabla:**
- 1: 2 personas ($F_1 = 2$)
- 3: 5 personas ($F_2 = 7$)
- 5: 3 personas ($F_3 = 10$)
**Total ($n$):** 10. **Mitad ($n/2$):** 5.
**Búsqueda:**
- ¿$F_1 (2) \ge 5$? No.
- ¿$F_2 (7) \ge 5$? Sí.
**Mediana:** $\boxed{3}$ (El dato 5 vive en la categoría "3").

#### Ejemplo 2: Encuesta rápida
**Tabla:**
- "No": 40 ($F=40$)
- "Sí": 60 ($F=100$)
**Total:** 100. **Mitad:** 50.
**Búsqueda:**
- ¿$40 \ge 50$? No.
- ¿$100 \ge 50$? Sí.
**Mediana:** $\boxed{\text{Sí}}$

#### Ejemplo 3: Camisas (S, M, L)
**Tabla:**
- S: 10 ($F=10$)
- M: 10 ($F=20$)
- L: 10 ($F=30$)
**Total:** 30. **Mitad:** 15.
**Búsqueda:** La posición 15 está en el segundo grupo ($F=20$).
**Mediana:** $\boxed{\text{M}}$

#### Ejemplo 4: Caso Borde (Exacto)
**Tabla:**
- A: 2 ($F=2$)
- B: 2 ($F=4$)
**Total:** 4. **Mitad:** 2.
**Análisis:**
- El dato 2 es "A".
- El dato 3 es "B".
- Como es par y cae en el límite, en variables cualitativas ordinales a veces se dice "entre A y B", pero en numéricas se promedia.
**Mediana:** $\boxed{\text{Entre A y B}}$

#### Ejemplo 5: Edades
**Tabla:**
- 10 años: 20 ($F=20$)
- 11 años: 30 ($F=50$)
- 12 años: 10 ($F=60$)
**Total:** 60. **Mitad:** 30.
**Análisis:** La posición 30 es el último dato del grupo "11 años". La posición 31 sería "12 años".
**Promedio:** $(11+12)/2 = 11.5$.
**Mediana:** $\boxed{11.5}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra la mediana de: 8, 4, 10, 2, 6.

<details>
<summary>Ver solución</summary>

**1. Ordenar:** 2, 4, 6, 8, 10.
**2. Centro:** El dato 3 es el 6.
**Resultado:** $\boxed{6}$

</details>

### Ejercicio 2
Encuentra la mediana de: 10, 2, 30, 4, 100, 50.

<details>
<summary>Ver solución</summary>

**1. Ordenar:** 2, 4, 10, 30, 50, 100.
**2. Centro ($n=6$):** Entre 10 y 30.
**3. Promedio:** $(10+30)/2 = 20$.
**Resultado:** $\boxed{20}$

</details>

### Ejercicio 3
Si tienes los datos: 1, 1, 1, 1, 9. ¿Cuál es la mediana?

<details>
<summary>Ver solución</summary>

**Ordenar:** Ya ordenados.
**Centro:** El tercer dato es 1.
**Resultado:** $\boxed{1}$

</details>

### Ejercicio 4
En una tabla tienes $n=50$. ¿Qué posición buscas en la frecuencia acumulada?

<details>
<summary>Ver solución</summary>

**Cálculo:** $n/2 = 25$. Buscas el dato 25 (y el 26 si quieres ser estricto con pares). Generalmente se busca donde $F_i$ supera a 25.
**Resultado:** $\boxed{25}$

</details>

### Ejercicio 5
Calcula la mediana de la tabla:
- $X=10, f=5$
- $X=20, f=10$
- $X=30, f=5$

<details>
<summary>Ver solución</summary>

**Acumuladas:** 5, 15, 20.
**Total ($n=20$):** Mitad = 10.
**Búsqueda:** 10 está contenido en el segundo grupo ($F=15$).
**Resultado:** $\boxed{20}$

</details>

### Ejercicio 6
¿La mediana se ve afectada si cambias el dato más grande por uno un millón de veces más grande?

<details>
<summary>Ver solución</summary>

**Propiedad:** Robustez.
**Resultado:** $\boxed{\text{No, sigue igual}}$

</details>

### Ejercicio 7
Halla la mediana de: -5, -10, 0, 5, 2.

<details>
<summary>Ver solución</summary>

**1. Ordenar:** -10, -5, 0, 2, 5.
**2. Centro:** 0.
**Resultado:** $\boxed{0}$

</details>

### Ejercicio 8
Si la mediana de 5 datos es 20, y multiplicamos todo por 2, ¿cuál es la nueva mediana?

<details>
<summary>Ver solución</summary>

**Propiedad:** El orden se mantiene. El dato central también se duplica.
**Resultado:** $\boxed{40}$

</details>

### Ejercicio 9
Tienes las tallas: S, M, M, L, XL. ¿Cuál es la mediana?

<details>
<summary>Ver solución</summary>

**Centro:** Hay 5 datos. El tercero es M.
**Resultado:** $\boxed{\text{M}}$

</details>

### Ejercicio 10
Si en un grupo de 100 personas, 55 ganan el salario mínimo, ¿cuál es la mediana salarial?

<details>
<summary>Ver solución</summary>

**Lógica:** Si ordenas a los 100, los primeros 55 son "salario mínimo".
El dato 50 y 51 son "salario mínimo".
**Resultado:** $\boxed{\text{El salario mínimo}}$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula Posición | Clave |
|----------|------------------|-------|
| **Impares ($n$)** | $\frac{n+1}{2}$ | El dato exacto del medio. |
| **Pares ($n$)** | $\frac{n}{2}$ y $\frac{n}{2}+1$ | Promedio de la pareja central. |
| **Tablas** | Buscar $F_i \ge n/2$ | Usar la acumulada. |

> **Conclusión:** La mediana es el ancla de la realidad. Ignora el ruido de los extremos y te dice exactamente qué pasa en la mitad de la población.
