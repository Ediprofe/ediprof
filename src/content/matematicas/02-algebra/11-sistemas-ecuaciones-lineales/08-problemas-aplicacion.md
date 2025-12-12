# 🔧 Problemas de Aplicación con Sistemas

En esta lección resolveremos problemas del mundo real que requieren sistemas de ecuaciones.

---

## 📖 Estrategia general

1. **Leer** cuidadosamente el problema
2. **Identificar** las incógnitas y asignarles variables
3. **Plantear** las ecuaciones basándose en las condiciones
4. **Resolver** el sistema
5. **Verificar** e interpretar la respuesta

---

## 📖 Problemas de números

### Ejemplo 1

La suma de dos números es 25 y su diferencia es 7. Encuentra los números.

**Variables:**
- $x$ = número mayor
- $y$ = número menor

**Ecuaciones:**
$$
\begin{cases}
x + y = 25 \\
x - y = 7
\end{cases}
$$

**Solución:** Sumamos las ecuaciones:
$$
2x = 32 \quad \Rightarrow \quad x = 16
$$
$$
y = 25 - 16 = 9
$$

$$
\boxed{\text{Los números son 16 y 9}}
$$

---

### Ejemplo 2

Un número es el triple de otro. Si la suma de ambos es 48, ¿cuáles son?

$$
\begin{cases}
x = 3y \\
x + y = 48
\end{cases}
$$

Sustituyendo:
$$
3y + y = 48 \quad \Rightarrow \quad y = 12, \quad x = 36
$$

$$
\boxed{\text{Los números son 36 y 12}}
$$

---

## 📖 Problemas de edades

### Ejemplo 3

Juan tiene el doble de la edad de María. Hace 5 años, Juan tenía el triple de la edad de María. ¿Cuántos años tiene cada uno?

**Variables:**
- $j$ = edad actual de Juan
- $m$ = edad actual de María

**Ecuaciones:**
$$
\begin{cases}
j = 2m \\
j - 5 = 3(m - 5)
\end{cases}
$$

Sustituimos en la segunda:
$$
2m - 5 = 3m - 15
$$
$$
10 = m
$$
$$
j = 20
$$

$$
\boxed{\text{Juan tiene 20 años, María tiene 10 años}}
$$

---

## 📖 Problemas de mezclas

### Ejemplo 4

Un comerciante mezcla café de $\$8$/kg con café de $\$12$/kg para obtener 50 kg de mezcla a $\$9$/kg. ¿Cuántos kg de cada tipo necesita?

**Variables:**
- $x$ = kg de café a $\$8$
- $y$ = kg de café a $\$12$

**Ecuaciones:**
$$
\begin{cases}
x + y = 50 \\
8x + 12y = 9(50)
\end{cases}
$$

De la primera: $y = 50 - x$

$$
8x + 12(50 - x) = 450
$$
$$
8x + 600 - 12x = 450
$$
$$
-4x = -150
$$
$$
x = 37.5, \quad y = 12.5
$$

$$
\boxed{37.5 \text{ kg a } \$8 \text{ y } 12.5 \text{ kg a } \$12}
$$

---

## 📖 Problemas de movimiento

### Ejemplo 5

Un bote viaja 30 km río abajo en 2 horas y 30 km río arriba en 3 horas. Encuentra la velocidad del bote en agua quieta y la velocidad de la corriente.

**Variables:**
- $b$ = velocidad del bote
- $c$ = velocidad de la corriente

**Ecuaciones:**
- Río abajo: velocidad = $b + c$, entonces $(b + c) \cdot 2 = 30$
- Río arriba: velocidad = $b - c$, entonces $(b - c) \cdot 3 = 30$

$$
\begin{cases}
b + c = 15 \\
b - c = 10
\end{cases}
$$

Sumando:
$$
2b = 25 \quad \Rightarrow \quad b = 12.5 \text{ km/h}
$$
$$
c = 2.5 \text{ km/h}
$$

$$
\boxed{b = 12.5 \text{ km/h}, \quad c = 2.5 \text{ km/h}}
$$

---

## 📖 Problemas de dinero

### Ejemplo 6

María tiene 25 monedas de $\$1$ y $\$5$. El total es $\$65$. ¿Cuántas monedas de cada tipo tiene?

$$
\begin{cases}
x + y = 25 \\
1x + 5y = 65
\end{cases}
$$

De la primera: $x = 25 - y$

$$
(25 - y) + 5y = 65
$$
$$
4y = 40
$$
$$
y = 10, \quad x = 15
$$

$$
\boxed{15 \text{ monedas de } \$1 \text{ y } 10 \text{ monedas de } \$5}
$$

---

### Ejemplo 7

Se invirtieron $\$10,000$ en dos cuentas: una al 5% anual y otra al 8% anual. El interés total anual fue $\$650$. ¿Cuánto se invirtió en cada cuenta?

$$
\begin{cases}
x + y = 10000 \\
0.05x + 0.08y = 650
\end{cases}
$$

Multiplicamos la segunda por 100:
$$
5x + 8y = 65000
$$

De la primera: $x = 10000 - y$

$$
5(10000 - y) + 8y = 65000
$$
$$
50000 - 5y + 8y = 65000
$$
$$
3y = 15000
$$
$$
y = 5000, \quad x = 5000
$$

$$
\boxed{\$5000 \text{ al } 5\% \text{ y } \$5000 \text{ al } 8\%}
$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** La suma de dos números es 50 y uno es 4 veces el otro. Encuéntralos.

<details>
<summary>Ver solución</summary>

$x + y = 50$, $x = 4y$

$5y = 50$, $y = 10$, $x = 40$

</details>

---

**Ejercicio 2:** Pedro tiene el triple de la edad de Ana. La suma de sus edades es 32. ¿Cuántos años tiene cada uno?

<details>
<summary>Ver solución</summary>

$p = 3a$, $p + a = 32$

$4a = 32$, $a = 8$, $p = 24$

</details>

---

**Ejercicio 3:** Un avión vuela 600 km a favor del viento en 2 horas y 600 km en contra del viento en 3 horas. Encuentra la velocidad del avión y del viento.

<details>
<summary>Ver solución</summary>

$a + v = 300$, $a - v = 200$

$a = 250$ km/h, $v = 50$ km/h

</details>

---
