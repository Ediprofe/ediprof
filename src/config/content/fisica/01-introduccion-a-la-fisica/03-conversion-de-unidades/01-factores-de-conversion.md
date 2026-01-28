---
title: "Factores de conversión"
---

# Factores de conversión

> **🎯 ¿Qué vas a aprender?**
>
> - Qué son los factores de conversión y por qué son iguales a 1.
> - Cómo escribir un factor de conversión en sus dos formas.
> - A elegir la forma correcta para cancelar unidades.

---

## ⚙️ ¿Qué es un factor de conversión?

Un **factor de conversión** es una **fracción igual a 1** que se construye a partir de una **equivalencia entre unidades**.

Por ejemplo, si sabemos que:

$$
1\,\mathrm{ft} = 12\,\mathrm{in}
$$

Podemos escribir **dos fracciones equivalentes a 1**:

$$
\dfrac{1\,\mathrm{ft}}{12\,\mathrm{in}} = 1 \qquad \text{y} \qquad \dfrac{12\,\mathrm{in}}{1\,\mathrm{ft}} = 1
$$

> **💡 Nota:** Como estas fracciones son iguales a 1, al multiplicar cualquier cantidad por ellas **no cambiamos su valor**, solo cambiamos las **unidades** en que se expresa.

---

## 🔄 ¿Cómo elegir la forma correcta?

La clave está en **colocar la unidad que quieres cancelar en el lado opuesto** de donde aparece en el dato original.

| Si quieres convertir de... | Coloca esa unidad en... | Para que se cancele con... |
| :---: | :---: | :---: |
| **ft** a **in** | el denominador | los ft del dato |
| **in** a **ft** | el denominador | los in del dato |

---

## ✏️ Ejemplo 1: Longitud (pies a pulgadas)

Convertir $3\,\mathrm{ft}$ a $\mathrm{in}$.

**Equivalencia:**

$$
1\,\mathrm{ft} = 12\,\mathrm{in}
$$

**Factor de conversión (se elige para cancelar ft):**

$$
\dfrac{12\,\mathrm{in}}{1\,\mathrm{ft}}
$$

**Operación:**

$$
3\,\mathrm{ft} \times \dfrac{12\,\mathrm{in}}{1\,\mathrm{ft}} = 3 \times 12\,\mathrm{in} = 36\,\mathrm{in}
$$

$$
\boxed{36\,\mathrm{in}}
$$

> Observa cómo la unidad **ft** aparece arriba en el dato y abajo en el factor, permitiendo que **se cancele**.

---

## ✏️ Ejemplo 2: Masa (libras a kilogramos)

Convertir $12.5\,\mathrm{lb}$ a $\mathrm{kg}$.

**Equivalencia:**

$$
1\,\mathrm{lb} = 0.4536\,\mathrm{kg}
$$

**Factor de conversión (se elige para cancelar lb):**

$$
\dfrac{0.4536\,\mathrm{kg}}{1\,\mathrm{lb}}
$$

**Operación:**

$$
12.5\,\mathrm{lb} \times \dfrac{0.4536\,\mathrm{kg}}{1\,\mathrm{lb}} = 12.5 \times 0.4536\,\mathrm{kg} = 5.67\,\mathrm{kg}
$$

$$
\boxed{5.67\,\mathrm{kg}}
$$

---

## ✏️ Ejemplo 3: Tiempo (horas a segundos)

Convertir $2\,\mathrm{h}$ a $\mathrm{s}$.

**Equivalencias (conversión en dos pasos):**

$$
1\,\mathrm{h} = 60\,\mathrm{min} \qquad \text{y} \qquad 1\,\mathrm{min} = 60\,\mathrm{s}
$$

**Factores de conversión en cadena:**

$$
2\,\mathrm{h} \times \dfrac{60\,\mathrm{min}}{1\,\mathrm{h}} \times \dfrac{60\,\mathrm{s}}{1\,\mathrm{min}}
$$

**Operación:**

$$
2 \times 60 \times 60\,\mathrm{s} = 7200\,\mathrm{s}
$$

$$
\boxed{7200\,\mathrm{s}}
$$

> **Tip:** Puedes encadenar varios factores de conversión para conversiones que requieran más de un paso.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**Convierte 8 kilogramos a libras.**

Equivalencia: $1\,\mathrm{kg} = 2.205\,\mathrm{lb}$

<details>
<summary>Ver solución</summary>

$$
8\,\mathrm{kg} \times \dfrac{2.205\,\mathrm{lb}}{1\,\mathrm{kg}} = 17.64\,\mathrm{lb}
$$

</details>

---

### Ejercicio 2
**Convierte 36 pulgadas a pies.**

Equivalencia: $1\,\mathrm{ft} = 12\,\mathrm{in}$

<details>
<summary>Ver solución</summary>

$$
36\,\mathrm{in} \times \dfrac{1\,\mathrm{ft}}{12\,\mathrm{in}} = 3\,\mathrm{ft}
$$

</details>

---

### Ejercicio 3
**Convierte 500 mililitros a litros.**

Equivalencia: $1\,\mathrm{L} = 1000\,\mathrm{mL}$

<details>
<summary>Ver solución</summary>

$$
500\,\mathrm{mL} \times \dfrac{1\,\mathrm{L}}{1000\,\mathrm{mL}} = 0.5\,\mathrm{L}
$$

</details>

---

## 🔑 Resumen

| Concepto | Descripción |
| :--- | :--- |
| **Equivalencia** | Relación entre dos unidades (ej: $1\,\mathrm{ft} = 12\,\mathrm{in}$) |
| **Factor de conversión** | Fracción igual a 1 construida con la equivalencia |
| **Dos formas** | Toda equivalencia genera 2 factores inversos |
| **Elegir la forma** | La unidad a cancelar va en el lado opuesto al dato |

![Factores de conversión](/images/fisica/introduccion/t-factores-de-conversion.png)

> **Recuerda:** El factor de conversión se elige de tal manera que la unidad inicial quede en posición de **cancelarse**, dejando solo la unidad deseada en el resultado.