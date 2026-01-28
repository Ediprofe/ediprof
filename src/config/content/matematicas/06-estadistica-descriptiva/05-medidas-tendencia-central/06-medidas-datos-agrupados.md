---
title: "Medidas para Datos Agrupados"
---

# **Medidas para Datos Agrupados**

Imagina que encuentras un reporte antiguo que dice: *"100 personas ganan entre \$500 y \$1000, 20 personas ganan entre \$1000 y \$1500"*. No tienes la lista exacta de sueldos, pero necesitas calcular el promedio. ¿Te rindes? ¡No! Usamos técnicas de estimación para recuperar las medidas de tendencia central usando "marcas de clase" y suposiciones inteligentes.

---

## 🎯 ¿Qué vas a aprender?

- Calcular la Media ($\bar{x}$) usando la marca de clase como representante.
- Estimar la Mediana usando la fórmula de interpolación lineal.
- Estimar la Moda usando las frecuencias vecinas.
- Entender que todos estos valores son **aproximaciones**.

---

## Media: El método de la Marca de Clase

Como no sabemos cuánto vale cada dato del intervalo, asumimos que todos valen lo mismo: el centro del intervalo (Marca de Clase, $x_i$).

$$ \bar{x} = \frac{\sum (f_i \cdot x_i)}{n} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Datos Básicos
- Int [0-10], $f=5$. Marca $x_1=5$. Producto: 25.
- Int [10-20], $f=5$. Marca $x_2=15$. Producto: 75.
- Suma: 100. Total $n=10$.
- Media: $100/10 = \boxed{10}$

#### Ejemplo 2: Intervalos Asimétricos
- [0-4], $f=10$. Marca 2. Prod: 20.
- [4-6], $f=20$. Marca 5. Prod: 100.
- Suma: 120. $n=30$.
- Media: $120/30 = \boxed{4}$

#### Ejemplo 3: Calificaciones
- [3.0 - 4.0), $f=2$. Marca 3.5. Prod: 7.0.
- [4.0 - 5.0], $f=8$. Marca 4.5. Prod: 36.0.
- Suma: 43. $n=10$.
- Media: $\boxed{4.3}$

#### Ejemplo 4: Edades
- [10-20], $f=100$. Marca 15. Prod: 1500.
- [20-30], $f=0$.
- Suma: 1500. $n=100$.
- Media: $\boxed{15}$

#### Ejemplo 5: Caso Unico
- [100-200], $f=1$.
- Media = Marca de clase = $\boxed{150}$

---

## Mediana: El método de Interpolación

Primero hallamos la posición $P = n/2$. Luego buscamos el intervalo que contiene esa posición y aplicamos zoom (interpolación).

$$ Me = L_i + \left( \frac{\frac{n}{2} - F_{ant}}{f_{med}} \right) \cdot A $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Interpolación simple
- $n=20$, $n/2=10$.
- Intervalo mediano [20-30]. $F_{ant}=5$. $f_{med}=10$. $A=10$.
- $Me = 20 + \frac{10 - 5}{10} \cdot 10 = 20 + 0.5 \cdot 10 = \boxed{25}$

#### Ejemplo 2: Al inicio del intervalo
- Posición mediana cae justo en el borde inferior.
- Entonces $n/2 - F_{ant} = 0$.
- $Me = L_i + 0 = \boxed{L_i}$

#### Ejemplo 3: Al final del intervalo
- Posición mediana casi completa la frecuencia.
- La fracción se acerca a 1.
- $Me \approx \boxed{L_{sup}}$

#### Ejemplo 4: Intervalo amplio
- Clase mediana [100-200], $A=100$.
- Fracción de interpolación calculada: $0.4$.
- $Me = 100 + 0.4 \cdot 100 = \boxed{140}$

#### Ejemplo 5: Distribución Uniforme
- Intervalo [0-10], $f=10$. $F_{ant}=0$. Bscamos dato 5 (mitad).
- $Me = 0 + \frac{5-0}{10} \cdot 10 = \boxed{5}$ (Justo el centro).

---

## Moda: El método de diferencias

La Moda vive en la clase con más frecuencia ($f_{max}$). Para hallarla exacta, vemos qué vecinos la "jalan" más fuerte.

$$ Mo = L_i + \left( \frac{\Delta_1}{\Delta_1 + \Delta_2} \right) \cdot A $$

Donde $\Delta_1$ es la diferencia con el vecino anterior y $\Delta_2$ con el siguiente.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Vecinos Simétricos
- Clase Modal $f=10$. Anterior $f=5$. Siguiente $f=5$.
- $\Delta_1=5, \Delta_2=5$.
- Fracción $= 5/10 = 0.5$.
- La moda está en el puro medio del intervalo.

#### Ejemplo 2: Vecino Anterior es 0
- Clase Modal es la primera ($f_{ant}=0$).
- $\Delta_1 = f_{mod}$.
- La moda se jala hacia la izquierda.

#### Ejemplo 3: Vecino Siguiente es grande
- Clase Modal $f=20$. Siguiente $f=19$. ($\Delta_2=1$).
- $\Delta_1$ (con anterior) digamos que es 10.
- El vecino siguiente jala la moda hacia la derecha (cerca del límite superior).

#### Ejemplo 4: Estimación rápida (Marca de clase)
- A veces, simplemente se usa la **Marca de Clase** como estimador rápido sin fórmula compleja.
- Int [10-20]. Moda estimada $\approx \boxed{15}$

#### Ejemplo 5: Clase Unica
- Solo hay un intervalo [0-10] con datos.
- Moda estimada $\approx \boxed{5}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la media de:
- [0-10], f=4
- [10-20], f=6

<details>
<summary>Ver solución</summary>

**Marcas:** 5 y 15.
**Productos:** $20 + 90 = 110$.
**Total:** 10.
**Media:** $\boxed{11}$

</details>

### Ejercicio 2
Encuentra la clase mediana si $F$ acumuladas son: 5, 15, 25. Total $n=25$.

<details>
<summary>Ver solución</summary>

**Posición:** $12.5$.
**F:** El primer grupo (5) no llega. El segundo (15) sí lo atrapa.
**Clase:** $\boxed{\text{La segunda}}$

</details>

### Ejercicio 3
Calcula $\bar{x}$ si tienes clases de amplitud 10 comenzando en 0, con frecuencias 1, 1, 1.

<details>
<summary>Ver solución</summary>

**Marcas:** 5, 15, 25.
**Suma:** 45.
**Media:** $45/3 = \boxed{15}$

</details>

### Ejercicio 4
Si la moda cae en el intervalo [50-60], ¿puede ser el valor de la moda 65?

<details>
<summary>Ver solución</summary>

**Lógica:** La moda debe estar *dentro* de su intervalo.
**Resultado:** $\boxed{\text{No}}$

</details>

### Ejercicio 5
Interpola la mediana: $L_i=10, A=5$. Necesitas recorrer el 50% del intervalo.

<details>
<summary>Ver solución</summary>

**Cálculo:** $10 + (0.5 \times 5) = 12.5$.
**Resultado:** $\boxed{12.5}$

</details>

### Ejercicio 6
Si la frecuencia modal es 20 y la anterior es 20, ¿cuánto vale $\Delta_1$?

<details>
<summary>Ver solución</summary>

**Resta:** $20 - 20 = 0$.
**Resultado:** $\boxed{0}$

</details>

### Ejercicio 7
¿Qué pasa con la media de datos agrupados si todos los intervalos se desplazan +10 unidades a la derecha?

<details>
<summary>Ver solución</summary>

**Propiedad:** La media también aumenta 10.
**Resultado:** $\boxed{\text{Aumenta 10}}$

</details>

### Ejercicio 8
Calcula la marca de clase del intervalo [19.5 - 29.5].

<details>
<summary>Ver solución</summary>

**Promedio:** $(19.5 + 29.5) / 2 = 49 / 2 = 24.5$.
**Resultado:** $\boxed{24.5}$

</details>

### Ejercicio 9
Si en el intervalo de la mediana $f_{med}$ es muy pequeña, ¿qué pasa con el resultado de la interpolación?

<details>
<summary>Ver solución</summary>

**Análisis:** Al dividir por un $f_{med}$ pequeño, el término de fracción crece rápido, cubriendo el intervalo con pocos "pasos".
**Resultado:** $\boxed{\text{Es sensible (inestable)}}$

</details>

### Ejercicio 10
¿Es posible calcular la media exacta si solo te dan la tabla agrupada?

<details>
<summary>Ver solución</summary>

**Teoría:** No, perdiste los datos individuales.
**Resultado:** $\boxed{\text{No, solo una estimación}}$

</details>

---

## 🔑 Resumen

| Estadístico | Método Agrupado | Precisión |
|-------------|-----------------|-----------|
| **Media** | Ponderado con Marcas de Clase. | Buena ssi la distribución es uniforme. |
| **Mediana** | Interpolación del área acumulada. | Más robusta que la media. |
| **Moda** | Interacción con vecinos ($\Delta$). | Depende mucho del ancho del intervalo elegido. |

> **Conclusión:** Agrupar datos nos ahorra espacio pero nos cobra un precio en precisión. Las fórmulas de datos agrupados son nuestro mejor intento de reconstruir la realidad perdida.
