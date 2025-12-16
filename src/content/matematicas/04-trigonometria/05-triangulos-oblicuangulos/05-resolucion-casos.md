# Resolución de Casos

Esta lección resume cómo resolver triángulos oblicuángulos según los datos disponibles.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Los 4 casos de resolución</strong>
  </div>

![Casos de resolución](/images/trigonometria/triangulos-oblicuangulos/casos-resolucion.svg)

</div>

---

## 📖 Resumen de casos

| Caso | Datos | Herramienta principal |
|------|-------|----------------------|
| ALA/LAA | 2 ángulos + 1 lado | Ley de Senos |
| LAL | 2 lados + ángulo incluido | Ley de Cosenos |
| LLL | 3 lados | Ley de Cosenos |
| LLA | 2 lados + ángulo no incluido | Ley de Senos (caso ambiguo) |

---

## 📖 Caso ALA/LAA

Conocemos **dos ángulos y un lado**.

### Procedimiento

1. Encontrar el tercer ángulo: $C = 180° - A - B$
2. Usar Ley de Senos para los lados faltantes

### Ejemplo

$A = 45°$, $B = 70°$, $a = 10$

$C = 180° - 45° - 70° = 65°$

$$
b = \frac{10 \times \sin 70°}{\sin 45°} = \frac{10 \times 0.940}{0.707} \approx 13.3
$$

$$
c = \frac{10 \times \sin 65°}{\sin 45°} = \frac{10 \times 0.906}{0.707} \approx 12.8
$$

---

## 📖 Caso LAL

Conocemos **dos lados y el ángulo entre ellos**.

### Procedimiento

1. Usar Ley de Cosenos para el tercer lado
2. Usar Ley de Senos o Cosenos para los ángulos restantes

### Ejemplo

$a = 8$, $b = 6$, $C = 50°$

$$
c^2 = 64 + 36 - 2(8)(6)\cos 50° = 100 - 61.7 = 38.3
$$

$c \approx 6.19$

$$
\cos A = \frac{36 + 38.3 - 64}{2(6)(6.19)} = \frac{10.3}{74.3} = 0.139
$$

$A \approx 82°$, $B = 180° - 50° - 82° = 48°$

---

## 📖 Caso LLL

Conocemos **los tres lados**.

### Procedimiento

1. Usar Ley de Cosenos para el ángulo mayor (opuesto al lado mayor)
2. Usar Ley de Cosenos o Senos para otro ángulo
3. Calcular el tercero por resta

### Ejemplo

$a = 7$, $b = 9$, $c = 11$

El lado mayor es $c$, encontramos $C$:

$$
\cos C = \frac{49 + 81 - 121}{2(7)(9)} = \frac{9}{126} = 0.071
$$

$C \approx 85.9°$

$$
\cos A = \frac{81 + 121 - 49}{2(9)(11)} = \frac{153}{198} = 0.773
$$

$A \approx 39.4°$, $B = 180° - 85.9° - 39.4° = 54.7°$

---

## 📖 Caso LLA (Ambiguo)

Conocemos **dos lados y el ángulo opuesto a uno de ellos**.

### Análisis

Sea $A$ el ángulo dado y $a$ su lado opuesto, con otro lado $b$:

| Condición | Soluciones |
|-----------|------------|
| $a < b\sin A$ | Ninguna |
| $a = b\sin A$ | Una (ángulo recto) |
| $b\sin A < a < b$ | Dos |
| $a \geq b$ | Una |

### Ejemplo con dos soluciones

$a = 8$, $b = 10$, $A = 40°$

$$
\sin B = \frac{10 \times \sin 40°}{8} = \frac{6.43}{8} = 0.804
$$

$B_1 = \arcsin(0.804) \approx 53.5°$

$B_2 = 180° - 53.5° = 126.5°$

Verificar: $A + B_2 = 40° + 126.5° = 166.5° < 180°$ ✓

Hay **dos triángulos** posibles.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Identificar y resolver

Para cada problema, identifica el caso y resuelve:

1. $A = 55°$, $B = 45°$, $c = 20$
2. $a = 9$, $b = 12$, $C = 72°$
3. $a = 5$, $b = 7$, $c = 10$

<details>
<summary><strong>Ver respuestas</strong></summary>

**1. Caso ALA:**
$C = 80°$

$a = \frac{20 \times \sin 55°}{\sin 80°} \approx 16.6$

$b = \frac{20 \times \sin 45°}{\sin 80°} \approx 14.4$

**2. Caso LAL:**
$c^2 = 81 + 144 - 2(9)(12)\cos 72° = 225 - 66.8 = 158.2$

$c \approx 12.6$

**3. Caso LLL:**
$\cos C = \frac{25 + 49 - 100}{70} = \frac{-26}{70} = -0.371$

$C \approx 111.8°$ (obtusángulo)

</details>

---
