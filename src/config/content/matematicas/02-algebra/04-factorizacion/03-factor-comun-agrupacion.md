---
title: "Factor Común por Agrupación"
---

# **Factor Común por Agrupación**

Este método se usa cuando la expresión tiene 4 o más términos y no hay un factor común para todos. La idea es formar grupos más pequeños donde sí exista un factor común.

---

## 🎯 ¿Qué vas a aprender?

- A identificar expresiones de 4 o más términos donde aplica este método.
- Cómo agrupar los términos en parejas.
- Cómo extraer factores comunes de cada grupo.
- Cómo manejar los signos negativos al agrupar.

---

## 🧩 ¿Cuándo usar Agrupación?

Este método es ideal cuando:
1.  La expresión tiene un número par de términos (generalmente **4 o 6**).
2.  No existe un factor que esté presente en **todos** los términos.
3.  Al separar la expresión en dos grupos, cada grupo sí tiene su propio factor común.

### **Ejemplo: El patrón escondido**

Observa: $ax + ay + bx + by$
- No hay ninguna letra en los cuatro términos a la vez.
- Pero si tomamos los dos primeros $(ax+ay)$, el factor común es **$a$**.
- Si tomamos los dos últimos $(bx+by)$, el factor común es **$b$**.

$$
a(x + y) + b(x + y)
$$

¡Y ahora el bloque $(x+y)$ es el nuevo factor común!

---

## 🏗️ Pasos para Agrupar Correctamente

1.  **Formar Parejas:** Divide la expresión en dos grupos de dos términos cada uno.
2.  **Primer Factor Común:** Extrae el factor común de cada pareja por separado.
3.  **Segundo Factor Común:** Si las parejas quedaron iguales dentro de sus paréntesis, ¡vas por buen camino! Saca ese paréntesis completo como nuevo factor común.

### **Ejemplo Paso a Paso**

Factoriza: $x^2 + 5x + 2x + 10$

**Razonamiento:**

1. Agrupamos: 

$$
(x^2 + 5x) \quad \text{y} \quad (2x + 10)
$$

2. Factorizamos el grupo 1: 

$$
x(x + 5)
$$

3. Factorizamos el grupo 2: 

$$
2(x + 5)
$$

4. Resultado parcial: 

$$
x(x + 5) + 2(x + 5)
$$

5. Factor común final: El bloque $(x+5)$ se repite.

**Resultado:** $\boxed{(x + 5)(x + 2)}$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El reto de los signos

Factoriza: $3x - 3y - ax + ay$

**Datos:** Hay signos negativos que pueden confundir.

**Razonamiento:**

1. Agrupamos: 

$$
(3x - 3y) + (-ax + ay)
$$

2. Factor común del 1ero: 

$$
3(x - y)
$$

3. Factor común del 2do: Sacamos $-a$ para que el signo de adentro cambie y coincida: 

$$
-a(x - y)
$$

4. Unimos: 

$$
3(x - y) - a(x - y)
$$

**Resultado:** $\boxed{(x - y)(3 - a)}$

---

### Ejemplo 2: Variables y números mezclados

Factoriza: $2x^3 - 4x^2 + 3x - 6$

**Datos:** Exponentes y coeficientes.

**Razonamiento:**

1. Pareja 1: 

$$
(2x^3 - 4x^2) = 2x^2(x - 2)
$$

2. Pareja 2: 

$$
(3x - 6) = 3(x - 2)
$$

3. Factor común binomial: 

$$
(x - 2)
$$

**Resultado:** $\boxed{(x - 2)(2x^2 + 3)}$

---

### Ejemplo 3: El reto de los tres términos iguales

Factoriza: $ax + bx + ay + by + az + bz$

**Razonamiento:**

1. Agrupamos por letras del frente: 

$$
(ax + bx) + (ay + by) + (az + bz)
$$

2. Extraemos el común de cada par: 

$$
x(a + b) + y(a + b) + z(a + b)
$$

3. El bloque $(a+b)$ se repite en los tres. Lo sacamos como factor final.

**Resultado:** $\boxed{(a + b)(x + y + z)}$

---

### Ejemplo 4: Cambiando el orden para agrupar

Factoriza: $x^2 + ab + ax + bx$

**Razonamiento:**

1. Si agrupamos como están $(x^2+ab)$ no tienen nada en común. Reordenamos.

2. Nuevo orden: 

$$
(x^2 + ax) + (bx + ab)
$$

3. Factorizamos el primer par: 

$$
x(x + a)
$$

4. Factorizamos el segundo par: 

$$
b(x + a)
$$

5. Unimos los bloques.

**Resultado:** $\boxed{(x + a)(x + b)}$

---

### Ejemplo 5: Agrupación con potencias altas

Factoriza: $m^5 + m^4 + m^3 + m^2$

**Razonamiento:**

1. Dividimos en dos grupos: 

$$
(m^5 + m^4) + (m^3 + m^2)
$$

2. Factor común del 1er grupo: 

$$
m^4(m + 1)
$$

3. Factor común del 2do grupo: 

$$
m^2(m + 1)
$$

4. Tenemos: 

$$
m^4(m+1) + m^2(m+1) = (m+1)(m^4 + m^2)
$$

5. *Nota:* Se podría factorizar más sacando $m^2$ del segundo paréntesis.

**Resultado:** $\boxed{(m + 1)(m^4 + m^2)}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica cuántos términos tiene una expresión típica para usar este método.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Para poder formar grupos iguales (parejas o tríos), necesitamos un número par de términos.
**Resultado:** $\boxed{\text{4 o más términos (par)}}$

</details>

### Ejercicio 2
Factoriza por grupos: $ay + az + by + bz$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
a(y+z) + b(y+z)
$$

**Resultado:** $\boxed{(y+z)(a+b)}$

</details>

### Ejercicio 3
Factoriza: $x^2 + 2x + 3x + 6$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
x(x+2) + 3(x+2)
$$

**Resultado:** $\boxed{(x+2)(x+3)}$

</details>

### Ejercicio 4
Si al agrupar obtienes $x(a-2) + 5(a-2)$, ¿cuál es el resultado final?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Sacamos el bloque $(a-2)$ como factor común.
**Resultado:** $\boxed{(a-2)(x+5)}$

</details>

### Ejercicio 5
Factoriza: $am - bm + an - bn$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
m(a-b) + n(a-b)
$$

**Resultado:** $\boxed{(a-b)(m+n)}$

</details>

### Ejercicio 6
Factoriza con cuidado los signos: $x^2 - xy + 4x - 4y$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
x(x-y) + 4(x-y)
$$

**Resultado:** $\boxed{(x-y)(x+4)}$

</details>

### Ejercicio 7
Resuelve: $2a^2 + 4ab + 3a + 6b$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
2a(a+2b) + 3(a+2b)
$$

**Resultado:** $\boxed{(a+2b)(2a+3)}$

</details>

### Ejercicio 8
Factoriza: $x^3 + x^2 + x + 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
x^2(x+1) + 1(x+1)
$$

Nota que el segundo grupo tiene un "1" invisible.

**Resultado:** $\boxed{(x+1)(x^2+1)}$

</details>

### Ejercicio 9
¿Qué sucede si al factorizar los grupos, los paréntesis no quedan iguales?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Significa que elegiste mal las parejas. Debes volver al inicio y probar agrupando otros términos.
**Resultado:** $\boxed{\text{Debes reagrupar de otra forma}}$

</details>

### Ejercicio 10
Factoriza: $6ab - 4a + 15b - 10$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 

$$
2a(3b-2) + 5(3b-2)
$$

**Resultado:** $\boxed{(3b-2)(2a+5)}$

</details>

---

## 🔑 Resumen

| Paso | Operación | Resultado |
| :--- | :--- | :--- |
| **1. Agrupar** | $(ax + ay) + (bx + by)$ | Grupos por factor común |
| **2. Extraer** | $a(x + y) + b(x + y)$ | Parentesis idénticos |
| **3. Unir** | $(x + y)(a + b)$ | **Forma Final** |

> La agrupación es como resolver un rompecabezas en dos pasos: primero unes las piezas pequeñas y luego unes los bloques grandes que formaste.
