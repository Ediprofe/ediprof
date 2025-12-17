# Soluciones Amortiguadoras (Buffer)

Una **solución buffer** (o tampón) es capaz de resistir cambios de pH cuando se le agregan pequeñas cantidades de ácido o base. Son esenciales en sistemas biológicos y químicos.

---

## 🎯 ¿Qué vas a aprender?

- Qué es un buffer y cómo funciona
- Composición de un buffer
- La ecuación de Henderson-Hasselbalch
- Aplicaciones biológicas

---

## 📊 Definición

| Aspecto | Descripción |
|---------|-------------|
| **Buffer** | Solución que resiste cambios de pH |
| **Composición** | Ácido débil + su base conjugada |
| **O también** | Base débil + su ácido conjugado |

---

## 📖 ¿Cómo Funciona un Buffer?

### 💡 Componentes:

Un buffer de ácido acético contiene:
- CH₃COOH (ácido débil)
- CH₃COO⁻ (base conjugada, como acetato de sodio)

### 💡 Si se agrega ácido (H⁺):

$$
\text{CH}_3\text{COO}^- + \text{H}^+ \rightarrow \text{CH}_3\text{COOH}
$$

La base conjugada **neutraliza** el H⁺ agregado.

### 💡 Si se agrega base (OH⁻):

$$
\text{CH}_3\text{COOH} + \text{OH}^- \rightarrow \text{CH}_3\text{COO}^- + \text{H}_2\text{O}
$$

El ácido débil **neutraliza** el OH⁻ agregado.

### 💡 Resultado:

El pH cambia muy poco porque el equilibrio se ajusta.

---

## 📖 Ecuación de Henderson-Hasselbalch

$$
\boxed{\text{pH} = \text{pK}_a + \log\frac{[\text{A}^-]}{[\text{HA}]}}
$$

Donde:
- pKa = -log(Ka)
- [A⁻] = concentración de base conjugada
- [HA] = concentración de ácido débil

### 💡 Casos especiales:

| Razón [A⁻]/[HA] | pH |
|-----------------|-----|
| 1:1 | pH = pKa |
| 10:1 | pH = pKa + 1 |
| 1:10 | pH = pKa - 1 |

---

## 📖 Ejemplo 1: Calcular pH del Buffer

### Problema:
Un buffer contiene 0.2 M de ácido acético (pKa = 4.74) y 0.3 M de acetato de sodio. ¿Cuál es el pH?

### Solución:

$$
\text{pH} = \text{pK}_a + \log\frac{[\text{A}^-]}{[\text{HA}]}
$$

$$
\text{pH} = 4.74 + \log\frac{0.3}{0.2}
$$

$$
\text{pH} = 4.74 + \log(1.5) = 4.74 + 0.18 = \boxed{4.92}
$$

---

## 📖 Ejemplo 2: Preparar un Buffer

### Problema:
¿Qué razón [A⁻]/[HA] necesitas para hacer un buffer de pH = 5.74 usando ácido acético (pKa = 4.74)?

### Solución:

$$
5.74 = 4.74 + \log\frac{[\text{A}^-]}{[\text{HA}]}
$$

$$
\log\frac{[\text{A}^-]}{[\text{HA}]} = 1
$$

$$
\frac{[\text{A}^-]}{[\text{HA}]} = 10^1 = \boxed{10:1}
$$

Necesitas 10 veces más acetato que ácido acético.

---

## 📖 Capacidad Buffer

### 💡 Definición:

Es la cantidad de ácido o base que un buffer puede neutralizar antes de que el pH cambie significativamente.

### 💡 Depende de:

1. **Concentraciones** de los componentes (mayor = más capacidad)
2. **Razón** [A⁻]/[HA] (óptimo cuando es cercana a 1)

### 💡 Rango efectivo:

Un buffer es efectivo en el rango:

$$
\text{pH} = \text{pK}_a \pm 1
$$

---

## 📖 Buffers Biológicos Importantes

| Buffer | pH | Función |
|--------|-----|---------|
| Bicarbonato | 7.4 | Sangre |
| Fosfato | 7.2 | Células |
| Proteínas | Variable | Tejidos |
| Hemoglobina | 7.4 | Glóbulos rojos |

### 💡 El buffer del bicarbonato en sangre:

$$
\text{H}_2\text{CO}_3 \rightleftharpoons \text{H}^+ + \text{HCO}_3^-
$$

Mantiene el pH de la sangre entre **7.35 y 7.45**.

---

## 📖 Para Bases Débiles

$$
\text{pOH} = \text{pK}_b + \log\frac{[\text{BH}^+]}{[\text{B}]}
$$

Luego: pH = 14 - pOH

---

## 🔑 Resumen

$$
\text{pH} = \text{pK}_a + \log\frac{[\text{base conjugada}]}{[\text{ácido}]}
$$

| Condición | pH |
|-----------|-----|
| [A⁻] = [HA] | pH = pKa |
| [A⁻] > [HA] | pH > pKa |
| [A⁻] < [HA] | pH < pKa |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Un buffer de NH₃/NH₄⁺ tiene [NH₃] = 0.1 M y [NH₄⁺] = 0.1 M. Si pKb = 4.74, ¿cuál es el pH?

<details>
<summary>Ver solución</summary>

pKa del ácido conjugado (NH₄⁺):
pKa = 14 - pKb = 14 - 4.74 = 9.26

$$
\text{pH} = 9.26 + \log\frac{0.1}{0.1} = 9.26 + 0 = \boxed{9.26}
$$

</details>

### Ejercicio 2
¿Cuál es el pKa de un ácido si un buffer con razón [A⁻]/[HA] = 2 tiene pH = 5.0?

<details>
<summary>Ver solución</summary>

$$
5.0 = \text{pK}_a + \log(2)
$$

$$
\text{pK}_a = 5.0 - 0.30 = \boxed{4.70}
$$

</details>

### Ejercicio 3
¿Por qué la sangre necesita un sistema buffer?

<details>
<summary>Ver solución</summary>

La sangre necesita buffers porque:

1. El metabolismo produce **ácidos** constantemente (CO₂ → H₂CO₃)
2. Las enzimas solo funcionan en un **rango estrecho de pH** (7.35-7.45)
3. Cambios de pH afectan:
   - Forma de proteínas
   - Afinidad de hemoglobina por O₂
   - Función de enzimas
   - Potenciales de membrana

Sin buffers, el pH cambiaría drásticamente y las células morirían.

El sistema bicarbonato/ácido carbónico es el principal buffer de la sangre:
$$
\text{CO}_2 + \text{H}_2\text{O} \rightleftharpoons \text{H}_2\text{CO}_3 \rightleftharpoons \text{H}^+ + \text{HCO}_3^-
$$

</details>

### Ejercicio 4
Un buffer de fosfato (pKa₂ = 7.2) tiene pH = 7.0. ¿Cuál es la razón [HPO₄²⁻]/[H₂PO₄⁻]?

<details>
<summary>Ver solución</summary>

$$
7.0 = 7.2 + \log\frac{[\text{HPO}_4^{2-}]}{[\text{H}_2\text{PO}_4^-]}
$$

$$
\log\frac{[\text{HPO}_4^{2-}]}{[\text{H}_2\text{PO}_4^-]} = -0.2
$$

$$
\frac{[\text{HPO}_4^{2-}]}{[\text{H}_2\text{PO}_4^-]} = 10^{-0.2} = \boxed{0.63}
$$

Hay menos base conjugada que ácido (lo que tiene sentido porque pH < pKa).

</details>
