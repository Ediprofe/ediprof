# pH de Ácidos y Bases Débiles

Calcular el pH de ácidos y bases débiles requiere trabajar con equilibrios, usando la constante de ionización (Ka o Kb).

---

## 🎯 ¿Qué vas a aprender?

- Cómo calcular [H⁺] desde Ka
- Cómo calcular [OH⁻] desde Kb
- La aproximación del 5%
- Ejercicios paso a paso

---

## 📊 Las Ecuaciones de Equilibrio

### Ácido débil:

$$
\text{HA} \rightleftharpoons \text{H}^+ + \text{A}^-
$$

$$
K_a = \frac{[\text{H}^+][\text{A}^-]}{[\text{HA}]}
$$

### Base débil:

$$
\text{B} + \text{H}_2\text{O} \rightleftharpoons \text{BH}^+ + \text{OH}^-
$$

$$
K_b = \frac{[\text{BH}^+][\text{OH}^-]}{[\text{B}]}
$$

---

## 📖 Método ICE

### 💡 Tabla ICE (Initial, Change, Equilibrium):

|  | HA | H⁺ | A⁻ |
|--|----|----|-----|
| **I** | C₀ | 0 | 0 |
| **C** | -x | +x | +x |
| **E** | C₀-x | x | x |

### 💡 Sustituyendo en Ka:

$$
K_a = \frac{x \cdot x}{C_0 - x} = \frac{x^2}{C_0 - x}
$$

---

## 📖 Aproximación del 5%

### 💡 Si Ka es pequeño y C₀ es grande:

$$
C_0 - x \approx C_0
$$

### 💡 La fórmula simplificada:

$$
\boxed{[\text{H}^+] = x = \sqrt{K_a \times C_0}}
$$

### 💡 ¿Cuándo es válida?

Si x < 5% de C₀, la aproximación es aceptable.

$$
\frac{x}{C_0} \times 100\% < 5\%
$$

---

## 📖 Ejemplo 1: Ácido Débil

### Problema:
Calcular el pH de ácido acético 0.1 M (Ka = 1.8 × 10⁻⁵).

### Solución:

**Paso 1:** Usar la aproximación
$$
[\text{H}^+] = \sqrt{K_a \times C_0} = \sqrt{1.8 \times 10^{-5} \times 0.1}
$$

$$
[\text{H}^+] = \sqrt{1.8 \times 10^{-6}} = 1.34 \times 10^{-3} \text{ M}
$$

**Paso 2:** Verificar aproximación
$$
\frac{1.34 \times 10^{-3}}{0.1} \times 100 = 1.34\% < 5\% \checkmark
$$

**Paso 3:** Calcular pH
$$
\text{pH} = -\log(1.34 \times 10^{-3}) = \boxed{2.87}
$$

---

## 📖 Ejemplo 2: Base Débil

### Problema:
Calcular el pH de NH₃ 0.1 M (Kb = 1.8 × 10⁻⁵).

### Solución:

**Paso 1:** Calcular [OH⁻]
$$
[\text{OH}^-] = \sqrt{K_b \times C_0} = \sqrt{1.8 \times 10^{-5} \times 0.1}
$$

$$
[\text{OH}^-] = 1.34 \times 10^{-3} \text{ M}
$$

**Paso 2:** Calcular pOH
$$
\text{pOH} = -\log(1.34 \times 10^{-3}) = 2.87
$$

**Paso 3:** Calcular pH
$$
\text{pH} = 14 - 2.87 = \boxed{11.13}
$$

---

## 📖 Ejemplo 3: Sin Aproximación

### Problema:
Calcular pH de HF 0.01 M (Ka = 6.8 × 10⁻⁴).

### Solución:

**Intentar aproximación:**
$$
x = \sqrt{6.8 \times 10^{-4} \times 0.01} = 2.6 \times 10^{-3}
$$

**Verificar:**
$$
\frac{2.6 \times 10^{-3}}{0.01} = 26\% > 5\%
$$

No es válida. Usar ecuación cuadrática:

$$
6.8 \times 10^{-4} = \frac{x^2}{0.01 - x}
$$

$$
x^2 + 6.8 \times 10^{-4}x - 6.8 \times 10^{-6} = 0
$$

Resolviendo: x = [H⁺] = 2.3 × 10⁻³ M

$$
\text{pH} = \boxed{2.64}
$$

---

## 📖 Resumen de Fórmulas

| Caso | Fórmula |
|------|---------|
| Ácido débil (aproximación) | [H⁺] = √(Ka × C₀) |
| Base débil (aproximación) | [OH⁻] = √(Kb × C₀) |
| Verificación | x/C₀ < 5% |

---

## 🔑 Resumen

$$
[\text{H}^+] = \sqrt{K_a \times C_0} \quad \text{(si Ka pequeño)}
$$

$$
[\text{OH}^-] = \sqrt{K_b \times C_0} \quad \text{(si Kb pequeño)}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el pH de ácido fórmico 0.5 M (Ka = 1.8 × 10⁻⁴).

<details>
<summary>Ver solución</summary>

$$
[\text{H}^+] = \sqrt{1.8 \times 10^{-4} \times 0.5} = \sqrt{9 \times 10^{-5}}
$$

$$
[\text{H}^+] = 9.5 \times 10^{-3} \text{ M}
$$

Verificación: 9.5×10⁻³/0.5 = 1.9% < 5% ✓

$$
\text{pH} = -\log(9.5 \times 10^{-3}) = \boxed{2.02}
$$

</details>

### Ejercicio 2
Calcula el pH de metilamina 0.2 M (Kb = 4.4 × 10⁻⁴).

<details>
<summary>Ver solución</summary>

$$
[\text{OH}^-] = \sqrt{4.4 \times 10^{-4} \times 0.2} = 9.4 \times 10^{-3} \text{ M}
$$

pOH = 2.03

$$
\text{pH} = 14 - 2.03 = \boxed{11.97}
$$

</details>

### Ejercicio 3
¿Por qué el pH de un ácido débil depende de su concentración, pero no simplemente igual a la concentración?

<details>
<summary>Ver solución</summary>

Porque un ácido débil **no se ioniza completamente**.

Si tienes CH₃COOH 0.1 M:
- [H⁺] **no** es 0.1 M
- Solo ~1% se ioniza
- [H⁺] ≈ 0.001 M

La concentración real de H⁺ depende de:
1. La **concentración inicial** (C₀)
2. La **constante Ka**

La fórmula [H⁺] = √(Ka × C₀) captura esta dependencia.

</details>
