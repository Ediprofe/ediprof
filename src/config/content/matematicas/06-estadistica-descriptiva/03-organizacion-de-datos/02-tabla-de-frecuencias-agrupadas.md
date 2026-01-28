---
title: "Tabla de Frecuencias Agrupadas"
---

# **Tabla de Frecuencias Agrupadas**

Imagina que tienes una lista con la estatura exacta de las 1,000 personas de tu colegio. Si haces una tabla simple, tendrías cientos de filas diferentes (1.60m, 1.61m, 1.62m...). Sería inútil. En cambio, si las agrupas por categorías (de 1.50 a 1.60, de 1.60 a 1.70...), la información se vuelve clara y manejable. Eso es una **tabla de frecuencias agrupadas**.

---

## 🎯 ¿Qué vas a aprender?

- Calcular el rango ($R$), número de intervalos ($k$) y amplitud ($A$) de los datos.
- Construir intervalos (clases) y calcular sus marcas de clase ($x_i$).
- Organizar datos continuos o masivos en tablas eficientes.
- Interpretar la información resumida en los intervalos.

---

## Parámetros de Construcción

Para agrupar datos, primero necesitamos definir "el tamaño de la caja" donde los meteremos. Usamos tres medidas clave:

1.  **Rango ($R$):** Qué tanto varían los datos.
    $$ R = X_{max} - X_{min} $$
2.  **Número de Intervalos ($k$):** Cuántas cajas (filas) tendremos. Usamos la Regla de Sturges:
    $$ k = 1 + 3.322 \cdot \log(n) $$
3.  **Amplitud ($A$):** Qué tan ancha es cada caja.
    $$ A = \frac{R}{k} $$

### ⚙️ Ejemplos Resueltos: Cálculo de Parámetros

#### Ejemplo 1: Notas de un examen masivo
**Situación:** 50,000 estudiantes presentaron el examen de estado. Nota mínima 0, máxima 100.
**Cálculo:**
- **Rango:** $100 - 0 = 100$.
- **Intervalos ($k$):** $1 + 3.322 \cdot \log(50000) = 1 + 3.322(4.69) \approx 16.6 \rightarrow 17$ clases.
- **Amplitud:** $100 / 17 \approx 5.88 \rightarrow 6$.
**Resultado:** $\boxed{k=17, A=6}$

#### Ejemplo 2: Temperaturas del mes
**Datos:** 30 días. Temp mínima $12^\circ$C, máxima $28^\circ$C.
**Cálculo:**
- **Rango:** $28 - 12 = 16$.
- **Intervalos:** $1 + 3.322 \cdot \log(30) \approx 1 + 3.322(1.47) = 5.9 \rightarrow 6$ clases.
- **Amplitud:** $16 / 6 = 2.66 \rightarrow 3$.
**Resultado:** $\boxed{k=6, A=3}$

#### Ejemplo 3: Edad de empleados
**Datos:** 100 empleados. El menor tiene 18 años, el mayor 62.
**Cálculo:**
- **Rango:** $62 - 18 = 44$.
- **Intervalos:** $1 + 3.322 \cdot \log(100) = 1 + 3.322(2) = 7.64 \rightarrow 8$ clases.
- **Amplitud:** $44 / 8 = 5.5 \rightarrow 6$.
**Resultado:** $\boxed{k=8, A=6}$

#### Ejemplo 4: Tiempo de espera en banco
**Datos:** 20 clientes. Min 2 min, Max 45 min.
**Cálculo:**
- **Rango:** $45 - 2 = 43$.
- **Intervalos:** $1 + 3.322 \cdot \log(20) \approx 5.32 \rightarrow 5$ clases.
- **Amplitud:** $43 / 5 = 8.6 \rightarrow 9$.
**Resultado:** $\boxed{k=5, A=9}$

#### Ejemplo 5: Peso de paquetes
**Datos:** 200 paquetes. Min 0.5 kg, Max 50 kg.
**Cálculo:**
- **Rango:** $50 - 0.5 = 49.5$.
- **Intervalos:** $1 + 3.322 \cdot \log(200) \approx 8.6 \rightarrow 9$ clases.
- **Amplitud:** $49.5 / 9 = 5.5 \rightarrow 6$.
**Resultado:** $\boxed{k=9, A=6}$

---

## Intervalos y Marca de Clase

Una vez tenemos la amplitud ($A$), construimos los intervalos (Límite Inferior - Límite Superior) y hallamos el representante de cada uno, llamado **Marca de Clase ($x_i$)**.

$$
x_i = \frac{L_{inf} + L_{sup}}{2}
$$

### ⚙️ Ejemplos Resueltos: Marcas de Clase

#### Ejemplo 1: Intervalo de edades
**Intervalo:** [10 - 20)
**Cálculo:**
$$ x_i = \frac{10 + 20}{2} = \frac{30}{2} = 15 $$
**Interpretación:** 15 años representa a todos los del grupo.

#### Ejemplo 2: Intervalo decimal
**Intervalo:** [55.5 - 60.5)
**Cálculo:**
$$ x_i = \frac{55.5 + 60.5}{2} = \frac{116}{2} = 58 $$
**Resultado:** $\boxed{58}$

#### Ejemplo 3: Salarios (Millones)
**Intervalo:** [2 - 4)
**Cálculo:**
$$ x_i = \frac{2 + 4}{2} = 3 $$
**Resultado:** $\boxed{3}$

#### Ejemplo 4: Estatura
**Intervalo:** [150 - 155)
**Cálculo:**
$$ x_i = \frac{150 + 155}{2} = 152.5 $$
**Resultado:** $\boxed{152.5}$

#### Ejemplo 5: Tiempo de carrera
**Intervalo:** [9 s - 12 s)
**Cálculo:**
$$ x_i = \frac{9 + 12}{2} = 10.5 $$
**Resultado:** $\boxed{10.5}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el rango ($R$) para un conjunto de datos donde la venta mínima fue $500 y la máxima $2500.

<details>
<summary>Ver solución</summary>

**Datos:** $X_{max} = 2500, X_{min} = 500$.
**Fórmula:** $R = 2500 - 500$.
**Resultado:** $\boxed{2000}$

</details>

### Ejercicio 2
Si tienes $n=1000$ datos, ¿cuántos intervalos sugiere la Regla de Sturges? (Usa $\log(1000)=3$).

<details>
<summary>Ver solución</summary>

**Fórmula:** $k = 1 + 3.322 \cdot \log(n)$.
**Cálculo:**
$$ k = 1 + 3.322(3) = 1 + 9.966 \approx 10.966 $$
**Redondeo:** A 11.
**Resultado:** $\boxed{11}$

</details>

### Ejercicio 3
Calcula la amplitud ($A$) si $R=40$ y decides usar $k=5$ intervalos.

<details>
<summary>Ver solución</summary>

**Fórmula:** $A = R / k$.
**Cálculo:**
$$ A = \frac{40}{5} = 8 $$
**Resultado:** $\boxed{8}$

</details>

### Ejercicio 4
Determina la marca de clase ($x_i$) para el intervalo [20 - 30).

<details>
<summary>Ver solución</summary>

**Fórmula:** Promedio de límites.
$$ x_i = \frac{20 + 30}{2} = 25 $$
**Resultado:** $\boxed{25}$

</details>

### Ejercicio 5
**Datos:** $R = 50$, $k = 8$. Calcula la amplitud ideal redondeada al entero superior.

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$ A = \frac{50}{8} = 6.25 $$
**Redondeo:** Siempre se redondea hacia arriba para cubrir el rango.
**Resultado:** $\boxed{7}$

</details>

### Ejercicio 6
Si el primer intervalo comienza en 10 y la amplitud es 5, ¿cuál es el segundo intervalo?

<details>
<summary>Ver solución</summary>

**Clase 1:** 10 a (10+5) = 10 - 15.
**Clase 2:** Empieza donde terminó el anterior. 15 a (15+5).
**Resultado:** $\boxed{15 - 20}$

</details>

### Ejercicio 7
Tienes datos de pesos: Min 40kg, Max 100kg. Si haces intervalos de amplitud 10 comenzando en 40, ¿en qué intervalo cae una persona de 63kg?

<details>
<summary>Ver solución</summary>

**Intervalos:**
1. 40 - 50
2. 50 - 60
3. 60 - 70
**Razonamiento:** 63 está entre 60 y 70.
**Resultado:** $\boxed{\text{Tercer intervalo (60-70]}}$

</details>

### Ejercicio 8
¿Cuál es la frecuencia relativa de un intervalo si su frecuencia absoluta es 20 y el total de datos es 200?

<details>
<summary>Ver solución</summary>

**Datos:** $f_i = 20, n = 200$.
**Cálculo:**
$$ f_r = \frac{20}{200} = 0.1 $$
**Resultado:** $\boxed{0.1 \text{ o } 10\%}$

</details>

### Ejercicio 9
Calcula la marca de clase del intervalo [0 - 100).

<details>
<summary>Ver solución</summary>

**Cálculo:**
$$ x_i = \frac{0 + 100}{2} = 50 $$
**Resultado:** $\boxed{50}$

</details>

### Ejercicio 10
Si la marca de clase es 15 y la amplitud es 10, ¿cuáles son los límites del intervalo?

<details>
<summary>Ver solución</summary>

**Razonamiento:** La marca de clase está en el centro.
Si $A=10$, hay 5 unidades hacia abajo y 5 hacia arriba desde el centro.
$L_{inf} = 15 - 5 = 10$.
$L_{sup} = 15 + 5 = 20$.
**Resultado:** $\boxed{[10 - 20]}$

</details>

---

## 🔑 Resumen

| Concepto | Fórmula | Descripción |
|----------|---------|-------------|
| **Datos Agrupados** | N/A | Usados cuando $n$ es grande o la variable es continua. |
| **Rango ($R$)** | $X_{max} - X_{min}$ | Dispersión total de los datos. |
| **Intervalos ($k$)** | $1 + 3.322\log(n)$ | Cantidad de grupos (Regla de Sturges). |
| **Amplitud ($A$)** | $R / k$ | Ancho de cada grupo. |
| **Marca de Clase ($x_i$)** | $(L_i + L_s)/2$ | Valor representativo (promedio) del intervalo. |

> **Conclusión:** Agrupar datos sacrifica precisión individual (ya no sabes si alguien mide 1.61 o 1.62, solo que está en el grupo 1.60-1.65) a cambio de ganar claridad y capacidad de análisis macro.
