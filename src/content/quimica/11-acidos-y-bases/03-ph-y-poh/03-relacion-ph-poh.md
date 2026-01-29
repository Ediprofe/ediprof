# Relación pH y pOH

El pH y el pOH están relacionados de manera que siempre suman 14 (a 25°C). Esta relación fundamental permite convertir fácilmente entre las dos escalas.

---

## 🎯 ¿Qué vas a aprender?

- La relación pH + pOH = 14
- De dónde viene esta relación
- Cómo usarla en cálculos
- Relación con Kw

---

## 📊 La Relación Fundamental

$$
\boxed{\text{pH} + \text{pOH} = 14} \quad \text{(a 25°C)}
$$

$$
\boxed{[\text{H}^+] \times [\text{OH}^-] = K_w = 10^{-14}}
$$

---

## 📖 ¿De Dónde Viene?

### 💡 Producto iónico del agua (Kw):

$$
\text{H}_2\text{O} \rightleftharpoons \text{H}^+ + \text{OH}^-
$$

$$
K_w = [\text{H}^+][\text{OH}^-] = 1 \times 10^{-14}
$$

### 💡 Aplicando logaritmos:

$$
\log([\text{H}^+][\text{OH}^-]) = \log(10^{-14})
$$

$$
\log[\text{H}^+] + \log[\text{OH}^-] = -14
$$

$$
-\text{pH} + (-\text{pOH}) = -14
$$

$$
\text{pH} + \text{pOH} = 14
$$

---

## 📖 Diagrama de la Relación

```
    pH    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14
          ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
    pOH  14  13  12  11  10   9   8   7   6   5   4   3   2   1   0
                                    │
                                 Neutro
```

---

## 📖 Ejemplo 1: De pOH a pH

### Problema:
Si pOH = 3, ¿cuál es el pH?

### Solución:

$$
\text{pH} = 14 - \text{pOH} = 14 - 3 = \boxed{11}
$$

---

## 📖 Ejemplo 2: De [OH⁻] a pH

### Problema:
Si [OH⁻] = 10⁻⁵ M, ¿cuál es el pH?

### Solución:

**Paso 1:** pOH
$$
\text{pOH} = -\log(10^{-5}) = 5
$$

**Paso 2:** pH
$$
\text{pH} = 14 - 5 = \boxed{9}
$$

---

## 📖 Ejemplo 3: Verificación

### Problema:
Verifica que [H⁺] = 10⁻³ M y [OH⁻] = 10⁻¹¹ M son consistentes.

### Solución:

**Verificar Kw:**
$$
[\text{H}^+] \times [\text{OH}^-] = 10^{-3} \times 10^{-11} = 10^{-14} = K_w \checkmark
$$

**Verificar pH + pOH:**
$$
\text{pH} = 3, \quad \text{pOH} = 11
$$

$$
3 + 11 = 14 \checkmark
$$

---

## 📖 Tabla Resumen

| Si conoces | Puedes encontrar |
|------------|------------------|
| pH | pOH = 14 - pH |
| pOH | pH = 14 - pOH |
| [H⁺] | [OH⁻] = Kw / [H⁺] |
| [OH⁻] | [H⁺] = Kw / [OH⁻] |

---

## 📖 Clasificación de Soluciones

| Tipo | pH vs pOH | [H⁺] vs [OH⁻] |
|------|-----------|---------------|
| **Ácida** | pH < pOH | [H⁺] > [OH⁻] |
| **Neutra** | pH = pOH = 7 | [H⁺] = [OH⁻] |
| **Básica** | pH > pOH | [H⁺] < [OH⁻] |

---

## 📖 Efecto de la Temperatura

### ⚠️ Importante:

Kw cambia con la temperatura:

| T (°C) | Kw | pH neutro |
|--------|-----|-----------|
| 0 | 1.1 × 10⁻¹⁵ | 7.47 |
| 25 | 1.0 × 10⁻¹⁴ | 7.00 |
| 50 | 5.5 × 10⁻¹⁴ | 6.63 |
| 100 | 5.1 × 10⁻¹³ | 6.14 |

A 100°C, el agua neutra tiene pH = 6.14, no 7.

---

## 🔑 Resumen

$$
\text{pH} + \text{pOH} = 14 \quad \text{(a 25°C)}
$$

$$
[\text{H}^+][\text{OH}^-] = 10^{-14}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si pH = 4.5, ¿cuál es pOH?

<details>
<summary>Ver solución</summary>

$$
\text{pOH} = 14 - 4.5 = \boxed{9.5}
$$

</details>

### Ejercicio 2
Si [OH⁻] = 2 × 10⁻⁴ M, ¿cuál es [H⁺]?

<details>
<summary>Ver solución</summary>

$$
[\text{H}^+] = \frac{K_w}{[\text{OH}^-]} = \frac{10^{-14}}{2 \times 10^{-4}} = \boxed{5 \times 10^{-11} \text{ M}}
$$

</details>

### Ejercicio 3
Una solución tiene pH = 8.3. ¿Es ácida, neutra o básica?

<details>
<summary>Ver solución</summary>

**Básica**, porque pH > 7.

También: pOH = 14 - 8.3 = 5.7

Como pH > pOH, [H⁺] < [OH⁻], confirmando que es básica.

</details>

### Ejercicio 4
¿Puede existir una solución acuosa con pH = 3 y pOH = 12?

<details>
<summary>Ver solución</summary>

Verifiquemos:
$$
\text{pH} + \text{pOH} = 3 + 12 = 15
$$

**No**, esto viola la relación pH + pOH = 14.

Si pH = 3, entonces pOH debe ser 11, no 12.

</details>
