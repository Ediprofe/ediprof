---
title: "Repartos Proporcionales"
---

# **Repartos Proporcionales**

Si tres amigos compran un boleto de lotería, pero uno pone $10$ pesos, otro $20$ y el tercero $70$, no sería justo repartir el premio en partes iguales, ¿verdad? El que más apostó merece más premio. Esto es un **reparto proporcional**.

---

## 🎯 ¿Qué vas a aprender?

- Repartir una cantidad de forma justa según lo que cada quien aportó (Directo).
- Repartir cantidades "al revés" (Inverso), donde el que tiene menos recibe más (como en un concurso de quién llega primero).
- Usar la constante de reparto ($k$) para simplificar todo.

---

## Reparto Directamente Proporcional

Aquí, **más es más**. Si aportas más dinero, recibes más ganancia. Si trabajas más horas, recibes más sueldo.

**Método de la Constante ($k$):**
1. Sumamos todos los índices de reparto ($a + b + c...$).
2. Dividimos el Total a Repartir ($T$) entre esa suma para hallar la constante $k$.
3. Multiplicamos cada índice por $k$.

$$ k = \frac{\text{Total}}{a + b + c} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: La Lotería
El premio es de $1000$ pesos.
- Ana aportó $2$ pesos.
- Beto aportó $3$ pesos.
- Carla aportó $5$ pesos.

1.  **Suma:** $2 + 3 + 5 = 10$.
2.  **Constante:** $k = \frac{1000}{10} = 100$. (Cada peso invertido gana 100).
3.  **Reparto:**
    -   Ana: $2 \times 100 = \boxed{200}$
    -   Beto: $3 \times 100 = \boxed{300}$
    -   Carla: $5 \times 100 = \boxed{500}$

#### Ejemplo 2: Herencia por Edades
Un abuelo reparte $450$ caramelos entre sus nietos de $8, 12$ y $16$ años, proporcional a sus edades.
1.  **Suma:** $8 + 12 + 16 = 36$.
2.  **Constante:** $k = \frac{450}{36} = 12.5$.
3.  **Reparto:**
    -   Nieto 8: $8 \times 12.5 = \boxed{100}$
    -   Nieto 12: $12 \times 12.5 = \boxed{150}$
    -   Nieto 16: $16 \times 12.5 = \boxed{200}$

#### Ejemplo 3: Inversión en Negocio
Socios invierten: A (1000), B (3000), C (5000). Ganancia: 1800.
Simplificamos los ceros: 1, 3, 5.
1.  **Suma:** $1 + 3 + 5 = 9$.
2.  **Constante:** $k = \frac{1800}{9} = 200$.
3.  **Reparto:**
    -   A: $1 \times 200 = \boxed{200}$
    -   B: $3 \times 200 = \boxed{600}$
    -   C: $5 \times 200 = \boxed{1000}$

#### Ejemplo 4: Horas Trabajadas
Pago total: $600$. Trabajador 1 (7 horas), Trabajador 2 (5 horas).
1.  **Suma:** $7 + 5 = 12$.
2.  **Constante:** $k = \frac{600}{12} = 50$.
3.  **Reparto:**
    -   T1: $7 \times 50 = \boxed{350}$
    -   T2: $5 \times 50 = \boxed{250}$

#### Ejemplo 5: Propinas
Tres meseros atienden mesas. A (4 mesas), B (5 mesas), C (6 mesas). Propinas: 300.
1.  **Suma:** $4+5+6=15$.
2.  **Constante:** $k = 300/15 = 20$.
3.  **Reparto:** $A=80, B=100, C=120$.

---

## Reparto Inversamente Proporcional

Aquí, **más es menos**. Se usa en competencias (el que tarda menos tiempo gana más premio) o accidentes (el que cometió menos errores recibe más bono).

**Método:**
1.  Invertimos los números ($N \to \frac{1}{N}$).
2.  Hacemos un **Común Denominador** para convertir esas fracciones en números enteros sencillos.
3.  Repartimos Directamente usando esos nuevos números enteros.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 6: La Carrera
Premio de $6200$ pesos para los 3 primeros. Tiempos: 2 min, 3 min, 5 min.
1.  **Inversos:** $\frac{1}{2}, \frac{1}{3}, \frac{1}{5}$.
2.  **Común Denominador (MCM 30):**
    -   $\frac{1}{2} \to \frac{15}{30}$
    -   $\frac{1}{3} \to \frac{10}{30}$
    -   $\frac{1}{5} \to \frac{6}{30}$
3.  **Nuevos Índices:** 15, 10, 6.
4.  **Suma:** $15 + 10 + 6 = 31$.
5.  **Constante:** $k = \frac{6200}{31} = 200$.
6.  **Reparto:**
    -   Corredor 2 min: $15 \times 200 = \boxed{3000}$. (Fue el más rápido, gana más).
    -   Corredor 3 min: $10 \times 200 = \boxed{2000}$.
    -   Corredor 5 min: $6 \times 200 = \boxed{1200}$.

#### Ejemplo 7: Faltas al trabajo
Bono de $2200$.
-   Juan: 1 falta.
-   Pedro: 2 faltas.
-   Luis: 3 faltas.
1.  **Inversos:** $1, \frac{1}{2}, \frac{1}{3}$.
2.  **MCM (6):**
    -   $1 = \frac{6}{6}$
    -   $\frac{1}{2} = \frac{3}{6}$
    -   $\frac{1}{3} = \frac{2}{6}$
3.  **Índices:** 6, 3, 2.
4.  **Suma:** $6+3+2=11$.
5.  **Constante:** $k = \frac{2200}{11} = 200$.
6.  **Reparto:**
    -   Juan (1 falta): $6 \times 200 = \boxed{1200}$.
    -   Pedro (2 faltas): $3 \times 200 = \boxed{600}$.
    -   Luis (3 faltas): $2 \times 200 = \boxed{400}$.

#### Ejemplo 8: Errores en examen
Premio 110 puntos extra a repartir inverso a errores: 2 y 4 errores.
1.  Inversos: $\frac{1}{2}, \frac{1}{4}$.
2.  MCM 4: $\frac{2}{4}, \frac{1}{4}$.
3.  Índices: 2 y 1.
4.  Suma: 3. k = 110/3 = 36.66.
    -   Alumno A: $2 \times 36.66 = 73.3$.
    -   Alumno B: $1 \times 36.66 = 36.6$.

#### Ejemplo 9: Edades (Bono juvenil)
Repartir 600 inverso a edades: 10 y 20 años.
1.  Inversos: 1/10, 1/20.
2.  Índices: 2, 1. (Porque 1/10 es el doble de 1/20).
3.  Suma: 3. k = 200.
    -   Niño 10: 400.
    -   Joven 20: 200.

#### Ejemplo 10: Velocidad de escritura
Repartir tarea (30 páginas) inverso a velocidad. Lento (1 pág/min), Rápido (2 pág/min).
El rápido debería hacer más.
Inverso de velocidad implicaría directo a tiempo... este caso es mejor pensarlo directo a capacidad.
Pero si el objetivo es premiar la lentitud (absurdo), sería inverso.
Repartamos 300 pesos inverso a velocidad: 10 km/h vs 50 km/h.
Indices: 5, 1.
Suma 6. k=50.
Lento: 250. Rápido: 50.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Repartir 1500 proporcional a 2, 3 y 5.

<details>
<summary>Ver solución</summary>

Suma 10. k=150.
**Resultado:** $\boxed{300, 450, 750}$

</details>

### Ejercicio 2
Repartir 600 inverso a 2 y 4.

<details>
<summary>Ver solución</summary>

Inv: $\frac{1}{2}, \frac{1}{4} \to 2, 1$. Suma 3. k=200.
**Resultado:** $\boxed{400, 200}$

</details>

### Ejercicio 3
Tres socios: $\$100, \$200, \$300$. Ganancia $\$1200$.

<details>
<summary>Ver solución</summary>

Índices simplificados: 1, 2, 3. Suma 6. k=200.
**Resultado:** $\boxed{200, 400, 600}$

</details>

### Ejercicio 4
Repartir 100 proporcional a $\frac{1}{2}$ y $\frac{1}{2}$.

<details>
<summary>Ver solución</summary>

Iguales. 50 y 50.
**Resultado:** $\boxed{50, 50}$

</details>

### Ejercicio 5
Repartir 700 inverso a 1 y 6.

<details>
<summary>Ver solución</summary>

Inv: 1, 1/6 $\to$ 6, 1. Suma 7. k=100.
**Resultado:** $\boxed{600, 100}$

</details>

### Ejercicio 6
Herencia de 50,000 a edades 20 y 30. (Directo).

<details>
<summary>Ver solución</summary>

2, 3. Suma 5. k=10,000.
**Resultado:** $\boxed{20000, 30000}$

</details>

### Ejercicio 7
Repartir 220 inverso a 4, 6, 12.

<details>
<summary>Ver solución</summary>

Inv: $\frac{1}{4}, \frac{1}{6}, \frac{1}{12} \to \frac{3}{12}, \frac{2}{12}, \frac{1}{12}$.
Índices: 3, 2, 1. Suma 6. k=36.66.
**Resultado:** $\boxed{110, 73.3, 36.6}$

</details>

### Ejercicio 8
Repartir 90 proporcional a 2, 2, 5.

<details>
<summary>Ver solución</summary>

Suma 9. k=10.
**Resultado:** $\boxed{20, 20, 50}$

</details>

### Ejercicio 9
Si A pone el triple que B. Repartir 400.

<details>
<summary>Ver solución</summary>

3, 1. Suma 4. k=100.
**Resultado:** $\boxed{300, 100}$

</details>

### Ejercicio 10
Repartir 330 inverso a 1, 10.

<details>
<summary>Ver solución</summary>

1, 1/10 $\to$ 10, 1. Suma 11. k=30.
**Resultado:** $\boxed{300, 30}$

</details>

---

## 🔑 Resumen

| Tipo | Clave | Conversión de Índices |
| :--- | :--- | :--- |
| **Directo** | Quien aporta más, recibe más. | Usar los números tal cual ($a, b, c$). |
| **Inverso** | Quien tiene menos (tiempo/errores), recibe más. | Invertir ($\frac{1}{a}, \frac{1}{b}$) y buscar MCM para usar enteros. |

> **Conclusión:** El Reparto Proporcional es la definición matemática de "Justicia". Dar a cada uno lo que le corresponde según su mérito o aporte.
