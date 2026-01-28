---
title: "Kp: Constante con Presiones Parciales"
---

# Kp: Constante con Presiones Parciales

La **Kp** es la constante de equilibrio expresada en términos de **presiones parciales**. Se usa exclusivamente para equilibrios que involucran **gases**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es Kp y cuándo usarla
- La relación entre Kp y Kc
- Cómo calcular Kp
- El significado de Δn

---

## 📊 Definición

$$
\boxed{K_p = \frac{P_C^c \cdot P_D^d}{P_A^a \cdot P_B^b}}
$$

Donde Pₓ es la **presión parcial** del gas X, generalmente en atmósferas (atm).

---

## 📖 ¿Cuándo Usar Kp?

### 💡 Solo para gases:

Kp se usa cuando todos los reactivos y productos son **gases**.

### ⚠️ Importante:

- Sólidos y líquidos **no tienen presión parcial**
- Por lo tanto, no aparecen en la expresión de Kp

---

## 📖 Ejemplo: Síntesis de Amoníaco

### Reacción:

$$
\text{N}_2\text{(g)} + 3\text{H}_2\text{(g)} \rightleftharpoons 2\text{NH}_3\text{(g)}
$$

### Expresión de Kp:

$$
K_p = \frac{P_{\text{NH}_3}^2}{P_{\text{N}_2} \cdot P_{\text{H}_2}^3}
$$

---

## 📖 Relación entre Kp y Kc

### 💡 Fórmula:

$$
\boxed{K_p = K_c \cdot (RT)^{\Delta n}}
$$

Donde:
- R = 0.0821 L·atm/(mol·K)
- T = temperatura en Kelvin
- Δn = (moles gaseosos de productos) - (moles gaseosos de reactivos)

---

## 📖 Cálculo de Δn

### 💡 Fórmula:

$$
\Delta n = \sum \text{coef. productos} - \sum \text{coef. reactivos}
$$

(Solo contar las especies **gaseosas**)

### ⚙️ Ejemplo 1:

$$
\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3
$$

$$
\Delta n = 2 - (1 + 3) = 2 - 4 = -2
$$

### ⚙️ Ejemplo 2:

$$
2\text{SO}_2 + \text{O}_2 \rightleftharpoons 2\text{SO}_3
$$

$$
\Delta n = 2 - (2 + 1) = 2 - 3 = -1
$$

### ⚙️ Ejemplo 3:

$$
\text{H}_2 + \text{I}_2 \rightleftharpoons 2\text{HI}
$$

$$
\Delta n = 2 - (1 + 1) = 2 - 2 = 0
$$

---

## 📖 Casos Especiales

### 💡 Cuando Δn = 0:

$$
K_p = K_c
$$

Las constantes son numéricamente iguales.

### 💡 Cuando Δn ≠ 0:

$$
K_p \neq K_c
$$

Las constantes tienen valores diferentes.

---

## 📖 Ejemplo: Calcular Kp desde Kc

### Problema:

Para N₂ + 3H₂ ⇌ 2NH₃ a 500 K, Kc = 0.5. ¿Cuál es Kp?

### Solución:

Δn = 2 - 4 = -2

$$
K_p = K_c \cdot (RT)^{\Delta n}
$$

$$
K_p = 0.5 \times (0.0821 \times 500)^{-2}
$$

$$
K_p = 0.5 \times (41.05)^{-2} = 0.5 \times 0.000594
$$

$$
K_p = \boxed{2.97 \times 10^{-4}}
$$

---

## 📖 Tabla Comparativa

| Aspecto | Kc | Kp |
|---------|----|----|
| Unidades | mol/L | atm (generalmente) |
| Se aplica a | Cualquier fase | Solo gases |
| Incluye sólidos | No | No |
| Incluye líquidos | Sí (en solución) | No |

---

## 🔑 Resumen

$$
K_p = \frac{\text{Presiones productos}}{\text{Presiones reactivos}}
$$

$$
K_p = K_c \cdot (RT)^{\Delta n}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe la expresión de Kp para:
2NO₂(g) ⇌ N₂O₄(g)

<details>
<summary>Ver solución</summary>

$$
K_p = \frac{P_{\text{N}_2\text{O}_4}}{P_{\text{NO}_2}^2}
$$

</details>

### Ejercicio 2
Calcula Δn para: PCl₅(g) ⇌ PCl₃(g) + Cl₂(g)

<details>
<summary>Ver solución</summary>

$$
\Delta n = (1 + 1) - 1 = 2 - 1 = \boxed{1}
$$

</details>

### Ejercicio 3
Si Kc = 1.2 × 10⁻² a 300 K para una reacción con Δn = 2, ¿cuál es Kp?

<details>
<summary>Ver solución</summary>

$$
K_p = K_c \cdot (RT)^2 = 1.2 \times 10^{-2} \times (0.0821 \times 300)^2
$$

$$
K_p = 1.2 \times 10^{-2} \times (24.63)^2 = 1.2 \times 10^{-2} \times 606.6
$$

$$
K_p = \boxed{7.28}
$$

</details>

### Ejercicio 4
¿Por qué Kp = Kc cuando Δn = 0?

<details>
<summary>Ver solución</summary>

Porque cualquier número elevado a la potencia 0 es igual a 1:

$$
K_p = K_c \cdot (RT)^0 = K_c \cdot 1 = K_c
$$

Esto ocurre cuando hay igual número de moles gaseosos a ambos lados de la ecuación, como en H₂+ I₂ ⇌ 2HI.

</details>
