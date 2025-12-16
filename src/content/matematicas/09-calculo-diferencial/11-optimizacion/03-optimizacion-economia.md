# Optimización en Economía

Las aplicaciones económicas del cálculo incluyen maximizar ganancias, minimizar costos y encontrar puntos de equilibrio. Los conceptos marginales son derivadas disfrazadas.

---

## 🎯 ¿Qué vas a aprender?

- Funciones de costo, ingreso y ganancia
- Conceptos marginales
- Maximización de ganancias
- Minimización de costo promedio

---

## 📖 Funciones económicas

| Función | Notación | Significado |
|---------|----------|-------------|
| Costo | $C(x)$ | Costo de producir $x$ unidades |
| Ingreso | $R(x)$ o $I(x)$ | Ingreso por vender $x$ unidades |
| Ganancia | $P(x)$ o $G(x)$ | Beneficio: $P(x) = R(x) - C(x)$ |
| Precio | $p(x)$ | Precio por unidad cuando se venden $x$ |

**Relación:** $R(x) = x \cdot p(x)$

---

## 📖 Conceptos marginales

El **costo marginal** es la derivada del costo:

$$C'(x) = \text{costo de producir una unidad adicional}$$

Similarmente:
- **Ingreso marginal:** $R'(x)$
- **Ganancia marginal:** $P'(x) = R'(x) - C'(x)$

---

## 📖 Condición de máxima ganancia

La ganancia se maximiza cuando:

$$P'(x) = 0 \quad \Rightarrow \quad R'(x) = C'(x)$$

**Ingreso marginal = Costo marginal**

---

## ⚙️ Ejemplo 1: Maximizar ganancia

Una empresa tiene:
- Costo: $C(x) = 0.1x^2 + 10x + 100$
- Precio: $p = 50 - 0.2x$

Encuentra el nivel de producción que maximiza la ganancia.

**Ingreso:**
$$R(x) = x \cdot p = x(50 - 0.2x) = 50x - 0.2x^2$$

**Ganancia:**
$$P(x) = R(x) - C(x) = 50x - 0.2x^2 - 0.1x^2 - 10x - 100$$
$$= 40x - 0.3x^2 - 100$$

**Optimización:**
$$P'(x) = 40 - 0.6x = 0$$
$$x = \frac{40}{0.6} \approx 66.67$$

**Producción óptima:** aproximadamente 67 unidades

**Ganancia máxima:** $P(66.67) \approx 1{,}233.33$

---

## ⚙️ Ejemplo 2: Verificar con marginales

Del ejemplo anterior:
$$R'(x) = 50 - 0.4x$$
$$C'(x) = 0.2x + 10$$

Igualando:
$$50 - 0.4x = 0.2x + 10$$
$$40 = 0.6x$$
$$x \approx 66.67$$ ✓

---

## 📖 Costo promedio

El **costo promedio** (o unitario) es:

$$\bar{C}(x) = \frac{C(x)}{x}$$

Se minimiza cuando:
$$\bar{C}'(x) = 0$$

---

## ⚙️ Ejemplo 3: Minimizar costo promedio

$C(x) = x^3 - 6x^2 + 15x + 10$

$$\bar{C}(x) = \frac{x^3 - 6x^2 + 15x + 10}{x} = x^2 - 6x + 15 + \frac{10}{x}$$

$$\bar{C}'(x) = 2x - 6 - \frac{10}{x^2} = 0$$

$$2x^3 - 6x^2 - 10 = 0$$

$$x^3 - 3x^2 - 5 = 0$$

Por métodos numéricos: $x \approx 3.57$ unidades

---

## 📖 Propiedad importante

El costo promedio se minimiza cuando:
$$\bar{C}(x) = C'(x)$$

**El costo promedio iguala al costo marginal.**

---

## ⚙️ Ejemplo 4: Precio óptimo

La demanda de un producto es $x = 1000 - 20p$ (donde $p$ es el precio).

Despejando: $p = 50 - 0.05x$

Si el costo es $C(x) = 10x + 500$, ¿qué precio maximiza la ganancia?

**Ingreso:** $R = px = (50 - 0.05x)x = 50x - 0.05x^2$

**Ganancia:** $P = 50x - 0.05x^2 - 10x - 500 = 40x - 0.05x^2 - 500$

$$P'(x) = 40 - 0.1x = 0 \Rightarrow x = 400$$

**Precio:** $p = 50 - 0.05(400) = 50 - 20 = 30$

---

## 📖 Elasticidad de la demanda

La **elasticidad** mide la sensibilidad de la demanda al precio:

$$E = -\frac{p}{x} \cdot \frac{dx}{dp}$$

| Valor | Tipo | Significado |
|-------|------|-------------|
| $E > 1$ | Elástica | La demanda es sensible al precio |
| $E < 1$ | Inelástica | La demanda es poco sensible |
| $E = 1$ | Unitaria | Ingreso máximo |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Si $C(x) = 50 + 3x$ y $R(x) = 10x - 0.01x^2$, encuentra la producción que maximiza la ganancia.

<details>
<summary>Ver solución</summary>

$P(x) = 10x - 0.01x^2 - 50 - 3x = 7x - 0.01x^2 - 50$

$P'(x) = 7 - 0.02x = 0$

$x = 350$ unidades
</details>

---

**Ejercicio 2:** Si el costo de producir $x$ artículos es $C(x) = 500 + 2x + 0.01x^2$, encuentra el nivel de producción que minimiza el costo promedio.

<details>
<summary>Ver solución</summary>

$\bar{C}(x) = \frac{500}{x} + 2 + 0.01x$

$\bar{C}'(x) = -\frac{500}{x^2} + 0.01 = 0$

$x^2 = 50{,}000$

$x \approx 224$ unidades
</details>
