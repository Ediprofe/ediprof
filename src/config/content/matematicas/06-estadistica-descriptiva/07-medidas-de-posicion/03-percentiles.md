---
title: "Percentiles"
---

# **Percentiles**

Estás en la fila de un concierto con 100 personas. Si estás en la posición 99, casi todos están detrás de ti. Si estás en la posición 1, todos están delante. Los **Percentiles** son exactamente eso: tu lugar en una fila de 100 datos. Es la medida más precisa para saber "a cuántos les ganaste".

---

## 🎯 ¿Qué vas a aprender?

- Calcular cualquier percentil ($P_{1}$ a $P_{99}$) con precisión milimétrica.
- Interpretar resultados de exámenes estandarizados y curvas de crecimiento.
- Relacionar los percentiles con la "normalidad" y los casos extremos.
- Usar la fórmula de posición $kn/100$.

---

## La Regla de los 100

Dividimos los datos en 100 partes iguales.
- **$P_{1}$:** Superas al 1% (estás en la cola inferior).
- **$P_{50}$:** Superas al 50% (estás justo en la mediana del medio).
- **$P_{99}$:** Superas al 99% (eres parte de la élite superior).

---

## Cálculo con Datos Simples

Ordena y busca la posición:
$$ Posición = \frac{k(n+1)}{100} $$
Donde $k$ va de 1 a 99.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: El Percentil 50 ($P_{50}$)
**Datos:** 2, 4, 6, 8, 10. ($n=5$).
**Posición:** $50(6)/100 = 300/100 = 3$.
**Valor:** Dato 3 (6).
**Confirmación:** Es la mediana.

#### Ejemplo 2: El Percentil 25 ($P_{25}$)
**Posición:** $25(6)/100 = 150/100 = 1.5$.
**Valor:** Entre 2 y 4. Promedio = 3.
**Confirmación:** Es $Q_1$.

#### Ejemplo 3: El Percentil 90 ($P_{90}$)
**Datos:** 10, 20... 90, 100. ($n=10$).
**Posición:** $90(11)/100 = 990/100 = 9.9$.
**Valor:** Entre dato 9 (90) y 10 (100).
**Interpolación:** $90 + 0.9(100-90) = 90 + 9 = 99$.
**Interpretación:** El 90% de los datos es menor a 99.

#### Ejemplo 4: Percentil Bajo ($P_{5}$)
**Datos:** 100 datos del 1 al 100.
**Posición:** $5(101)/100 = 5.05$.
**Valor:** Dato 5 (aprox). 5.
**Interpretación:** "Bajo rendimiento" o "valor pequeño".

#### Ejemplo 5: El "1% más rico" ($P_{99}$)
**Datos:** Ingresos de un país.
**Posición:** Casi al final de la lista ordenada.
**Valor:** Si $P_{99} = \$10,000$, significa que el 99% de la gente gana menos de \$10,000.

---

## Casos de Uso en la Vida Real

Los percentiles brillan cuando $n$ es muy grande.

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Curvas de Crecimiento
Un bebé está en el **$P_{10}$** de peso.
**Interpretación:** De cada 100 bebés sanos, 90 pesan más que él. Es pequeñito, pero puede ser normal si se mantiene en su carril.

#### Ejemplo 2: Exámenes (ICFES / SAT)
Tu puntaje dice **Percentil 95**.
**Interpretación:** No significa que sacaste 9.5/10. Significa que le ganaste al 95% de los estudiantes del país.

#### Ejemplo 3: Tiempos de Carga Web
Google monitorea el **$P_{99}$**.
Si $P_{99} = 2s$, significa que el 99% de las visitas cargan en menos de 2 segundos. Se enfocan en mejorar ese 1% lento.

#### Ejemplo 4: Detección de Fraude
Transacciones bancarias. Si gastas \$5000 y el $P_{99}$ de tus gastos es \$200, el banco bloquea la tarjeta por comportamiento anómalo (outlier).

#### Ejemplo 5: Salarios de Programadores
Si $P_{25} = \$1000$ y $P_{75} = \$3000$.
El 50% central ("junior a senior normales") gana entre \$1000 y \$3000.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra $P_{50}$ de 10, 20, 30.

<details>
<summary>Ver solución</summary>

**Concepto:** Mediana.
**Resultado:** $\boxed{20}$

</details>

### Ejercicio 2
Si estás en el $P_{100}$, ¿es posible?

<details>
<summary>Ver solución</summary>

**Teoría:** Técnicamente se usa hasta $P_{99}$. Si fueras el 100, superarías al 100% (incluso a ti mismo), lo cual es paradójico.
**Resultado:** $\boxed{\text{No, máximo P99}}$

</details>

### Ejercicio 3
En una carrera, ¿prefieres el percentil 1 o 99 de tiempo?

<details>
<summary>Ver solución</summary>

**Contexto:** Menos tiempo es mejor (ganar). Quieres estar en los tiempos bajos.
**Resultado:** $\boxed{P_1}$

</details>

### Ejercicio 4
En un examen de conocimientos, ¿prefieres el percentil 1 o 99?

<details>
<summary>Ver solución</summary>

**Contexto:** Más nota es mejor.
**Resultado:** $\boxed{P_{99}}$

</details>

### Ejercicio 5
Calcula la posición de $P_{20}$ si $n=49$.

<details>
<summary>Ver solución</summary>

**Cálculo:** $20(50)/100 = 1000/100 = 10$.
**Resultado:** $\boxed{10}$

</details>

### Ejercicio 6
Si $Q_1 = 50$, ¿cuánto vale $P_{25}$?

<details>
<summary>Ver solución</summary>

**Equivalencia:** Son lo mismo.
**Resultado:** $\boxed{50}$

</details>

### Ejercicio 7
¿Qué porcentaje de datos es mayor que $P_{80}$?

<details>
<summary>Ver solución</summary>

**Resta:** $100\% - 80\% = 20\%$.
**Resultado:** $\boxed{20\%}$

</details>

### Ejercicio 8
Si todos los datos son 5, ¿cuánto vale $P_{90}$?

<details>
<summary>Ver solución</summary>

**Análisis:** No hay variación.
**Resultado:** $\boxed{5}$

</details>

### Ejercicio 9
¿Qué percentil corresponde a la Mediana?

<details>
<summary>Ver solución</summary>

**Mitad:** 50.
**Resultado:** $\boxed{P_{50}}$

</details>

### Ejercicio 10
Si $P_{10} = 20$ y $P_{20} = 20$. ¿Qué pasa entre el 10% y el 20%?

<details>
<summary>Ver solución</summary>

**Análisis:** Los datos son iguales (planos) en ese tramo.
**Resultado:** $\boxed{\text{No hay variación}}$

</details>

---

## 🔑 Resumen

| Percentil | Cuartil | Decil | Significado |
|-----------|---------|-------|-------------|
| $P_{25}$ | $Q_1$ | - | Cuartil Inferior. |
| $P_{50}$ | $Q_2$ | $D_5$ | Mediana. |
| $P_{75}$ | $Q_3$ | - | Cuartil Superior. |
| $P_{10}$ | - | $D_1$ | Top 90% (o Fondo 10%). |
| $P_{90}$ | - | $D_9$ | Top 10%. |

> **Conclusión:** Los percentiles son el lenguaje universal de la comparación masiva. Nos permiten ubicar a cualquier individuo en el contexto de su población con máxima precisión.
