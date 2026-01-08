# **Introducción a las Funciones Lineales**

Ahora que dominas el plano cartesiano, es hora de usarlo. Imagina que tomas un taxi. Solo por subirte ya debes pagar una tarifa base, y luego el costo aumenta de forma constante por cada kilómetro que avanzas. O piensa en tu plan de celular: una renta fija mensual más el consumo extra.

Esa combinación de un **punto de partida fijo** y un **ritmo de cambio constante** es la esencia de una **función lineal**.

---

## 🎯 ¿Qué vas a aprender?

- Cómo identificar una función lineal en situaciones cotidianas.
- Qué significan visualmente el **intercepto** ($b$) y la **pendiente** ($m$).
- Cómo construir la fórmula general $y = mx + b$ sin memorizar.

---

## 📖 ¿Qué es una Función?

Antes de entrar en las líneas rectas, recordemos qué es una función básica. 

Imagina una máquina: tú le das una "entrada" (un número) y ella te devuelve una única "salida". En matemáticas, llamamos a la entrada **variable independiente ($x$)** y a la salida **variable dependiente ($y$)**. Decimos que $y$ es una función de $x$ porque el valor de $y$ "depende" totalmente de lo que pongamos en $x$.

![funcion-matematica](https://cdn.ediprofe.com/img/matematicas/b471-funcion-matematica.webp)

Ahora, veamos específicamente el tipo más simple y útil de funciones: las **lineales**.

---

## 🚖 El Ejemplo del Taxi (Entendiendo el Patrón)

Analicemos cómo cobra un taxi para entender las dos piezas clave de toda línea recta.

Supongamos que la tarifa es:
1.  **Banderazo (Inicio):** $3$ pesos (te los cobran solo por subir).
2.  **Tarifa por distancia:** $2$ pesos por cada kilómetro recorrido.

Veamos esto en una gráfica para descubrir el patrón:

<div style="width: 100%; margin-bottom: 2rem;">
  <img src="/images/funciones/algebra/taxi-costo.svg" alt="Gráfica del costo de taxi mostrando pendiente e intercepto" style="width: 100%; height: auto; border-radius: 8px; border: 1px solid #e2e8f0;">
</div>

### 🔎 ¿Qué observamos?

1.  **El Punto de Partida (Intercepto):**
    La línea no empieza en cero, empieza en **$3$**. Este es el valor inicial cuando no has recorrido nada ($0$ km). En matemáticas, a este valor fijo lo llamamos **Intercepto** y usamos la letra **$b$**.
    
    $$
    b = 3
    $$

2.  **El Ritmo de Cambio (Pendiente):**
    Mira los escalones verdes en la gráfica. Por cada **$1$ km** que avanzas a la derecha, la línea sube **$2$ pesos**. Este ritmo constante de crecimiento se llama **Pendiente** y usamos la letra **$m$**.
    
    $$
    m = 2
    $$

---

## 📈 La Fórmula General

Si quisiéramos calcular el costo ($y$) para cualquier número de kilómetros ($x$), haríamos esto:

$$
\text{Costo} = (\text{Costo por km} \cdot \text{Kilómetros}) + \text{Inicio}
$$

Sustituyendo nuestros valores:

$$
y = 2x + 3
$$

¡Esta es una función lineal! Y lo mejor es que **todas** las líneas rectas del universo siguen esta misma estructura, conocida como la forma pendiente-intercepto:

$$
y = mx + b
$$

Donde:
- **$y$**: Es el resultado final (Variable Dependiente).
- **$x$**: Es el valor que cambia (Variable Independiente).
- **$m$**: Es la **Pendiente** (el ritmo de cambio).
- **$b$**: Es el **Intercepto** (el valor inicial).

---

## ⚡ Identificando Patrones

Ahora que conoces el secreto (buscar el "Inicio" $b$ y el "Ritmo" $m$), analicemos otros ejemplos para ver si puedes encontrar la función.

### Ejemplo 1: El Salario por Hora
Trabajas en una biblioteca y ganas **$15$ pesos por hora**. No te pagan nada si no vas (inicio cero).

**Análisis:**
- **Inicio ($b$):** $0$ (si trabajas 0 horas, ganas 0).
- **Ritmo ($m$):** $15$ (ganas 15 por cada hora extra).

**La Función:**
$$
y = 15x + 0 \quad \Rightarrow \quad y = 15x
$$

<div style="width: 100%; margin-top: 1rem; margin-bottom: 2rem;">
  <img src="/images/funciones/algebra/salario-hora.svg" alt="Gráfica del salario por hora" style="width: 100%; height: auto; border-radius: 8px; border: 1px solid #e2e8f0;">
</div>

### Ejemplo 2: El Tanque que se Vacía
Un tanque tiene **$100$ litros** y pierde **$5$ litros por minuto**.

**Análisis:**
- **Inicio ($b$):** $100$ (es la cantidad inicial).
- **Ritmo ($m$):** $-5$ (¡es negativo porque la cantidad disminuye!).

**La Función:**
$$
y = -5x + 100
$$

<div style="width: 100%; margin-top: 1rem; margin-bottom: 2rem;">
  <img src="/images/funciones/algebra/tanque-vaciado.svg" alt="Gráfica del tanque vaciándose" style="width: 100%; height: auto; border-radius: 8px; border: 1px solid #e2e8f0;">
</div>

_(Nota como el ritmo negativo hace que la función "baje" en lugar de subir)._

### Ejemplo 3: La Alcancía
Tienes **$500$ pesos** ahorrados y decides guardar **$100$ pesos cada mes**.

**Análisis:**
- **Inicio ($b$):** $500$.
- **Ritmo ($m$):** $100$.

**La Función:**
$$
y = 100x + 500
$$

<div style="width: 100%; margin-top: 1rem; margin-bottom: 2rem;">
  <img src="/images/funciones/algebra/alcancia-ahorro.svg" alt="Gráfica de ahorro en alcancía" style="width: 100%; height: auto; border-radius: 8px; border: 1px solid #e2e8f0;">
</div>

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica el valor del intercepto ($b$) en la función del taxi: $y = 2x + 3$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** El intercepto es el término que no tiene $x$, o el valor inicial.
**Resultado:** $\boxed{3}$

</details>

---

### Ejercicio 2
Si una función tiene pendiente $m = 4$ y comienza en el origen ($b=0$), escribe su ecuación.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Usamos la forma $y = mx + b$.
$$
y = 4x + 0
$$
**Resultado:** $\boxed{y = 4x}$

</details>

---

### Ejercicio 3
En la ecuación del tanque $y = -5x + 100$, ¿qué representa el número $-5$?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Es el número que acompaña a la $x$, por lo tanto es la pendiente. Al ser negativo, indica que el tanque pierde agua.
**Resultado:** $\boxed{\text{La pendiente (ritmo de vaciado)}}$

</details>

---

### Ejercicio 4
Un técnico cobra 200 pesos por la visita y 50 pesos por cada hora de trabajo. Escribe la función del costo total.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
- Inicio ($b$) = 200 pesos
- Ritmo ($m$) = 50 pesos
$$
y = 50x + 200
$$
**Resultado:** $\boxed{y = 50x + 200}$

</details>

---

### Ejercicio 5
Calcula el valor de $y$ en la función $y = 3x - 2$ cuando $x = 4$.

<details>
<summary>Ver solución</summary>

$$
y = 3(4) - 2
$$
$$
y = 12 - 2
$$
**Resultado:** $\boxed{10}$

</details>

---

### Ejercicio 6
¿Cuál es la pendiente de la función $y = 7 - 2x$?

<details>
<summary>Ver solución</summary>

**Razonamiento:** La pendiente es el número que multiplica a la $x$. Aquí es $-2$ (cuidado con el orden).
**Resultado:** $\boxed{-2}$

</details>

---

### Ejercicio 7
Escribe la función para: "Un árbol mide 1 metro y crece 0.5 metros al año".

<details>
<summary>Ver solución</summary>

**Razonamiento:**
- Inicio ($b$) = $1$
- Crecimiento ($m$) = $0.5$
**Resultado:** $\boxed{y = 0.5x + 1}$

</details>

---

### Ejercicio 8
Si $f(x) = 2x$, ¿cuál es el valor del intercepto $b$?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Como no hay término independiente sumado, $b = 0$.
**Resultado:** $\boxed{0}$

</details>

---

### Ejercicio 9
Identifica la variable dependiente en: "El costo de la luz depende de los kilowatts consumidos".

<details>
<summary>Ver solución</summary>

**Razonamiento:** Lo que "resulta" o "depende" es el costo final.
**Resultado:** $\boxed{\text{El costo de la luz}}$

</details>

---

### Ejercicio 10
Evalúa la función del taxi ($y = 2x + 3$) para un viaje de 10 km.

<details>
<summary>Ver solución</summary>

$$
y = 2(10) + 3
$$
$$
y = 20 + 3
$$
**Resultado:** $\boxed{23}$

</details>

---

## 🔑 Resumen

| Concepto | Símbolo | En el Taxi ($y = 2x + 3$) | Significado General |
|:--- |:---: |:--- |:--- |
| **Intercepto** | $b$ | $3$ (Banderazo) | Punto de partida o valor inicial (cuando $x=0$). |
| **Pendiente** | $m$ | $2$ (Costo por km) | Ritmo de cambio o velocidad con que crece/decrece la función. |
| **Variable Indep.** | $x$ | Distancia (km) | El valor que nosotros controlamos o ingresamos. |
| **Variable Dep.** | $y$ | Costo Total (pesos) | El resultado que depende de la $x$. |

> **Conclusión:** Toda situación donde haya un valor inicial y un ritmo de cambio constante se puede modelar como una línea recta con la fórmula $y = mx + b$. En la siguiente lección, profundizaremos en esta **Fórmula Maestra** y veremos cómo cada parte define la forma de la recta.
