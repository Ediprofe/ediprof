# **Resolución de Problemas Lineales**

Las matemáticas cobran vida cuando resolvemos problemas. Una factura de teléfono, la velocidad de un auto o el ahorro mensual son situaciones que podemos modelar con funciones lineales para tomar mejores decisiones. En esta lección aprenderás a transformar palabras en ecuaciones.

---

## 🎯 ¿Qué vas a aprender?

- Cómo identificar la pendiente y el intercepto en textos reales.
- El método para construir funciones a partir de situaciones cotidianas.
- Cómo predecir resultados futuros evaluando la función.
- El uso de la variable independiente y dependiente en contexto.

---

## 🏗️ La Guía Paso a Paso

Para resolver un problema lineal, sigue siempre este orden:
1. **Identificar:** ¿Quién es $x$ (el tiempo, la cantidad) y quién es $y$ (el costo, la distancia)?
2. **Hallar $b$:** Busca el valor inicial o costo fijo.
3. **Hallar $m$:** Busca el ritmo de cambio (lo que se cobra "por cada...").
4. **Armar:** Escribe la función $y = mx + b$.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El Plan de Celular

Un plan de celular cuesta 20 pesos mensuales de base y 0.50 pesos por cada minuto extra consumido. Escribe la función del costo total.

**Razonamiento:**
- Costo base (fijo): $b = 20$.
- Costo por minuto (cambio): $m = 0.50$.
- Variable $x$: minutos extras.

**Ecuación:**
$$
f(x) = 0.50x + 20
$$

¿Cuánto pagarás si hablas 100 minutos extras?
$$
f(100) = 0.50(100) + 20 = 50 + 20 = 70 \text{ pesos}
$$

---

### Ejemplo 2: El Vaciado de un Tanque

Un tanque con 500 litros de agua se vacía a razón de 25 litros por hora. ¿Cuándo quedarán solo 100 litros?

**Razonamiento:**
- Valor inicial: $b = 500$.
- Ritmo de pérdida: $m = -25$ (es negativo porque disminuye).
- Función: $y = -25x + 500$.

Buscamos $x$ cuando $y = 100$:
$$
100 = -25x + 500
$$
$$
25x = 500 - 100 \implies 25x = 400
$$
$$
x = 16 \text{ horas}
$$

---

### Ejemplo 3: El Ahorro para un Viaje

Tienes 200 pesos ahorrados y decides meter 50 pesos cada semana en tu alcancía. ¿Cuánto dinero tendrás en 10 semanas?

**Razonamiento:**
- $b = 200$.
- $m = 50$.
- Función: $f(x) = 50x + 200$.

Evaluamos para $x = 10$:
$$
f(10) = 50(10) + 200 = 500 + 200 = 700 \text{ pesos}
$$

---

### Ejemplo 4: Depreciación de una Computadora

Una computadora costó 3000 pesos. Cada año pierda 400 pesos de su valor original. ¿Cuál será su valor después de 5 años?

**Razonamiento:**
- $b = 3000$.
- $m = -400$ (pérdida de valor).
- Función: $V(t) = -400t + 3000$.

Evaluamos para $t = 5$:
$$
V(5) = -400(5) + 3000 = -2000 + 3000 = 1000 \text{ pesos}
$$

---

### Ejemplo 5: Distancia en Carretera

Un auto sale de Bogotá hacia Medellín y viaja a una velocidad constante de 80 kilómetros por hora. ¿A qué distancia estará después de 4 horas?

**Razonamiento:**
- Como parte desde el inicio, $b = 0$.
- La velocidad es la pendiente: $m = 80$.
- Función: $d(t) = 80t$.

Evaluamos para $t = 4$:
$$
d(4) = 80(4) = 320 \text{ kilómetros}
$$

---

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Un gimnasio cobra 50 pesos de inscripción y 30 pesos por mes. Escribe la función de costo total.

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{y = 30x + 50}$

</details>

---

### Ejercicio 2
Usando la función del gimnasio ($y = 30x + 50$), ¿cuánto habrás pagado en total después de un año (12 meses)?

<details>
<summary>Ver solución</summary>

$$
30(12) + 50 = 360 + 50 = 410
$$

**Resultado:** $\boxed{410 \text{ pesos}}$

</details>

---

### Ejercicio 3
Una vela de 20 cm se consume 2 cm por cada hora. Escribe su función de altura $h(t)$.

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{h(t) = -2t + 20}$

</details>

---

### Ejercicio 4
Un vendedor de libros gana 800 pesos base más 20 pesos por cada libro vendido. Si este mes ganó 1200 pesos, ¿cuántos libros vendió?

<details>
<summary>Ver solución</summary>

$$
1200 = 20x + 800 \implies 400 = 20x \implies x = 20
$$

**Resultado:** $\boxed{20 \text{ libros}}$

</details>

---

### Ejercicio 5
Un automóvil viaja a una velocidad constante de 90 km/h. Escribe la función de distancia $d(t)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** El valor inicial es 0 ($b=0$).
**Resultado:** $\boxed{d(t) = 90t}$

</details>

---

### Ejercicio 6
Si la función de temperatura en una montaña es $T = -6h + 20$ (donde $h$ es la altura en km), ¿cuál es la temperatura a 2 km de altura?

<details>
<summary>Ver solución</summary>

$$
-6(2) + 20 = -12 + 20 = 8
$$

**Resultado:** $\boxed{8^\circ\text{C}}$

</details>

---

### Ejercicio 7
Un tanque tiene 40 litros y se llena 5 litros cada minuto. ¿Cuánto tiempo tarda en llegar a 100 litros?

<details>
<summary>Ver solución</summary>

$$
100 = 5x + 40 \implies 60 = 5x \implies x = 12
$$

**Resultado:** $\boxed{12 \text{ minutos}}$

</details>

---

### Ejercicio 8
Una cuenta de ahorros inicia con 1000 pesos y cada mes se le depositan 200 pesos. Escribe la función del ahorro total.

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{y = 200x + 1000}$

</details>

---

### Ejercicio 9
Identifica el "ritmo de cambio" en la situación: "Un artesano fabrica 3 sillas cada día".

<details>
<summary>Ver solución</summary>

**Resultado:** $\boxed{m = 3}$

</details>

---

### Ejercicio 10
Un paquete por correo cuesta 15 pesos de envío más 2 pesos por cada kilo. Si el envío costó 25 pesos, ¿cuántos kilos pesaba?

<details>
<summary>Ver solución</summary>

$$
25 = 2x + 15 \implies 10 = 2x \implies x = 5
$$

**Resultado:** $\boxed{5 \text{ kilos}}$

</details>

---

## 🔑 Resumen

| Concepto | Término Real | Papel en la Función |
|:--- |:--- |:--- |
| **Punto Inicial** | Inscripción, Banderazo, Depósito Inicial. | Intercepto ($b$). |
| **Ritmo de Cambio** | Velocidad, Precio por unidad, Consumo horario. | Pendiente ($m$). |
| **Variable X** | Tiempo, Minutos, Distancia, Unidades vendidas. | Independiente. |
| **Variable Y** | Costo Total, Altura final, Ahorro total. | Dependiente. |

> **Conclusión:** Las funciones lineales son el puente que conecta el razonamiento lógico con la resolución de problemas en la vida diaria. ¡Úsalas para planificar tu éxito!
