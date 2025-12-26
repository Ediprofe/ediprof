# **Fórmulas del MRU**

Cuando algo se mueve con velocidad constante, las matemáticas se vuelven muy sencillas. Solo necesitas manejar tres conceptos clave: dónde está, qué tan rápido va y cuánto tiempo ha pasado.

---

## 🎯 ¿Qué vas a aprender?

- La fórmula maestra que conecta posición, velocidad y tiempo.
- Cómo despejar esta fórmula para encontrar cualquier dato que te falte.
- Cómo manejar la "Posición Inicial" cuando no empiezas desde cero.
- Cómo resolver problemas de encuentro y persecución.

---

## 📐 **La Ecuación Fundamental**

En el Movimiento Rectilíneo Uniforme, todo se reduce a una sola lógica: **La distancia crece uniformemente con el tiempo**.

La fórmula base es:

$$
x = v \cdot t
$$

Donde:
- **$x$**: Distancia o Desplazamiento ($\mathrm{m}, \mathrm{km}$)
- **$v$**: Velocidad constante ($\mathrm{m/s}, \mathrm{km/h}$)
- **$t$**: Tiempo transcurrido ($\mathrm{s}, \mathrm{h}$)

> **Nota:** Esta fórmula asume que partes del origen ($0$).

---

## 🔄 **El Triángulo del Despeje**

Dependiendo de qué dato tengas y cuál busques, puedes reorganizar la fórmula. Una técnica visual muy útil es el **Triángulo de Fórmulas**:

1. Tapas la letra que buscas.
2. Las letras restantes te indican la operación matemática.

![despeje-mru](https://cdn.ediprofe.com/img/fisica/llj9-despeje-mru.webp)


| ¿Qué buscas? | Fórmula | Lógica |
| :--- | :--- | :--- |
| **Distancia ($x$)** | $$x = v \cdot t$$ | Velocidad por Tiempo |
| **Velocidad ($v$)** | $$v = \frac{x}{t}$$ | Distancia entre Tiempo |
| **Tiempo ($t$)** | $$t = \frac{x}{v}$$ | Distancia entre Velocidad |

---

## ⚙️ **El Caso General: Posición Inicial ($x_i$)**

En la vida real, no siempre empezamos a contar desde la línea de partida. A veces el objeto ya está adelantado.

Para saber la **Posición Final ($x_f$)**, tomamos la posición donde empezamos y le sumamos lo que recorrimos:

$$
x_f = x_i + v \cdot t
$$

- **$x_f$**: Posición Final (¿Dónde terminó?)
- **$x_i$**: Posición Inicial (¿Dónde empezó?)
- **$v \cdot t$**: Lo que avanzó.

---

## ⚙️ **Ejemplos Resueltos**

### **Ejemplo 1: Cálculo de Tiempo**

Un sonido viaja por el agua a **$1500\,\mathrm{m/s}$**. ¿Cuánto tarda en recorrer **3000 metros**?

**Datos:**
- Velocidad ($v$) = $1500\,\mathrm{m/s}$
- Distancia ($x$) = $3000\,\mathrm{m}$
- Tiempo ($t$) = ?

**Razonamiento:**
Necesitamos el tiempo. Usamos la fórmula de despeje correspondiente.

$$
t = \frac{x}{v}
$$

**Cálculo:**

$$
t = \frac{3000}{1500}
$$

**Resultado:**

$$
\boxed{2\,\mathrm{s}}
$$

---

### **Ejemplo 2: Posición con Inicio Adelantado**

Un ciclista está en el kilómetro 10 de una carretera ($x_i = 10$). Avanza a **$20\,\mathrm{km/h}$** durante **3 horas**. ¿En qué kilómetro termina?

**Datos:**
- Inicio ($x_i$) = $10\,\mathrm{km}$
- Velocidad ($v$) = $20\,\mathrm{km/h}$
- Tiempo ($t$) = $3\,\mathrm{h}$

**Razonamiento:**
Su posición final es donde estaba más lo que avanzó.

$$
x_f = 10 + (20 \times 3)
$$

**Cálculo:**

$$
x_f = 10 + 60
$$

**Resultado:**

$$
\boxed{70\,\mathrm{km}}
$$

(Termina en el kilómetro 70).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Un avión vuela a $800\,\mathrm{km/h}$. ¿Qué distancia recorre en 0.5 horas?**

<details>
<summary>Ver solución</summary>

**Datos:**
- $v = 800\,\mathrm{km/h}$
- $t = 0.5\,\mathrm{h}$

**Razonamiento:**
Distancia = Velocidad $\times$ Tiempo.

$$
x = 800 \times 0.5
$$

**Resultado:**

$$
\boxed{400\,\mathrm{km}}
$$

</details>

### Ejercicio 2
**Un atleta corre 200 metros en 25 segundos. ¿Cuál es su velocidad media?**

<details>
<summary>Ver solución</summary>

**Datos:**
- $x = 200\,\mathrm{m}$
- $t = 25\,\mathrm{s}$

**Razonamiento:**
Velocidad = Distancia / Tiempo.

$$
v = \frac{200}{25}
$$

**Resultado:**

$$
\boxed{8\,\mathrm{m/s}}
$$

</details>

### Ejercicio 3
**¿Cuánto tiempo tarda un coche a $20\,\mathrm{m/s}$ en recorrer 1000 metros?**

<details>
<summary>Ver solución</summary>

**Datos:**
- $v = 20\,\mathrm{m/s}$
- $x = 1000\,\mathrm{m}$

**Razonamiento:**
Tiempo = Distancia / Velocidad.

$$
t = \frac{1000}{20}
$$

**Resultado:**

$$
\boxed{50\,\mathrm{s}}
$$

</details>

### Ejercicio 4
**Un tren parte del km 50 y avanza 100 km. ¿Cuál es su posición final?**

<details>
<summary>Ver solución</summary>

**Datos:**
- $x_i = 50\,\mathrm{km}$
- Avanza = $100\,\mathrm{km}$

**Razonamiento:**
Se suma el avance a la posición inicial.

$$
x_f = 50 + 100
$$

**Resultado:**

$$
\boxed{150\,\mathrm{km}}
$$

</details>

### Ejercicio 5
**Dos autos salen de ciudades separadas por 500 km y van uno hacia el otro a $50\,\mathrm{km/h}$ cada uno. ¿En cuánto tiempo se encuentran?**

<details>
<summary>Ver solución</summary>

**Datos:**
- Distancia total = $500\,\mathrm{km}$
- Velocidad combinada (se acercan) = $50 + 50 = 100\,\mathrm{km/h}$

**Razonamiento:**
El tiempo es la distancia dividido entre la velocidad de acercamiento.

$$
t = \frac{500}{100}
$$

**Resultado:**

$$
\boxed{5\,\mathrm{h}}
$$

</details>

### Ejercicio 6
**La luz viaja a $300\,000\,\mathrm{km/s}$. El Sol está a $150\,000\,000\,\mathrm{km}$. ¿Cuánto tarda la luz en llegar?**

<details>
<summary>Ver solución</summary>

**Datos:**
- $v = 300\,000\,\mathrm{km/s}$
- $x = 150\,000\,000\,\mathrm{km}$

**Razonamiento:**
$t = x / v$.

$$
t = \frac{150\,000\,000}{300\,000} = \frac{1500}{3}
$$

**Resultado:**

$$
\boxed{500\,\mathrm{s}}
$$
(8 minutos y 20 segundos).

</details>

### Ejercicio 7
**Un caracol avanza a $5\,\mathrm{mm/s}$. ¿Cuántos milímetros recorre en un minuto?**

<details>
<summary>Ver solución</summary>

**Datos:**
- $v = 5\,\mathrm{mm/s}$
- $t = 1\,\mathrm{min} = 60\,\mathrm{s}$

**Razonamiento:**
Usamos segundos para que coincidan las unidades.

$$
x = 5 \times 60
$$

**Resultado:**

$$
\boxed{300\,\mathrm{mm}}
$$

</details>

### Ejercicio 8
**Un corredor está en la marca de 50m y corre hacia atrás (hacia el origen) a $5\,\mathrm{m/s}$ por 4 segundos. ¿Dónde termina?**

<details>
<summary>Ver solución</summary>

**Datos:**
- $x_i = 50\,\mathrm{m}$
- $v = -5\,\mathrm{m/s}$ (negativo porque retrocede)
- $t = 4\,\mathrm{s}$

**Razonamiento:**
$x_f = x_i + v \cdot t$.

$$
x_f = 50 + (-5 \times 4) = 50 - 20
$$

**Resultado:**

$$
\boxed{30\,\mathrm{m}}
$$

</details>

### Ejercicio 9
**¿A qué velocidad debes ir para recorrer 10 km en 10 minutos?**

<details>
<summary>Ver solución</summary>

**Datos:**
- $x = 10\,\mathrm{km}$
- $t = 10\,\mathrm{min} = \frac{1}{6}\,\mathrm{h}$

**Razonamiento:**
$v = x / t$.

$$
v = \frac{10}{1/6} = 10 \times 6
$$

**Resultado:**

$$
\boxed{60\,\mathrm{km/h}}
$$

</details>

### Ejercicio 10
**Un coche A viaja a $60\,\mathrm{km/h}$ y un coche B a $90\,\mathrm{km/h}$ en la misma dirección. ¿Cuánto se aleja B de A en una hora?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La velocidad relativa de alejamiento es la diferencia.

$$
v_{dif} = 90 - 60 = 30\,\mathrm{km/h}
$$

En 1 hora, se alejan:

$$
x = 30 \times 1
$$

**Resultado:**

$$
\boxed{30\,\mathrm{km}}
$$

</details>

---

## 🔑 Resumen

| Variable | Descripción | Fórmula Clave |
|----------|-------------|---------------|
| **Posición ($x$)** | Distancia recorrida o ubicación. | $$x = v \cdot t$$ |
| **Velocidad ($v$)** | Rapidez constante. | $$v = \frac{x}{t}$$ |
| **Tiempo ($t$)** | Duración del movimiento. | $$t = \frac{x}{v}$$ |
| **Posición Final ($x_f$)** | Ubicación final considerando inicio. | $$x_f = x_i + v \cdot t$$ |

> Estas tres fórmulas son solo una misma ecuación reorganizada. Si sabes una, ¡sabes todas! Lo importante es identificar qué dato tienes y cuál te falta.
