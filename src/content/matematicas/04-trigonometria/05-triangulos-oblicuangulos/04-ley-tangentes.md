# Ley de Tangentes

La **Ley de Tangentes** es una alternativa a las leyes de Senos y Cosenos, aunque se usa con menos frecuencia.

<div style="background: linear-gradient(135deg, #fef3c7 0%, #fce7f3 100%); border: 2px solid #f97316; border-radius: 12px; padding: 1.2rem; margin: 1.5rem 0;">
<div style="font-weight: bold; color: #c2410c; margin-bottom: 0.8rem;">📋 Fórmula de la Ley de Tangentes</div>
<div style="font-size: 1.1rem; text-align: center; color: #1e293b; margin: 0.5rem 0;">
(a - b) / (a + b) = tan[(A - B)/2] / tan[(A + B)/2]
</div>
<div style="margin-top: 0.8rem; font-size: 0.9rem; color: #64748b;">
💡 Útil para caso LAL: encuentra los ángulos directamente sin calcular el tercer lado primero.
</div>
</div>

---

## 📖 Enunciado

En cualquier triángulo $ABC$:

$$
\frac{a - b}{a + b} = \frac{\tan\frac{A - B}{2}}{\tan\frac{A + B}{2}}
$$

De forma similar para otros pares de lados y ángulos:

$$
\frac{b - c}{b + c} = \frac{\tan\frac{B - C}{2}}{\tan\frac{B + C}{2}}
$$

$$
\frac{a - c}{a + c} = \frac{\tan\frac{A - C}{2}}{\tan\frac{A + C}{2}}
$$

---

## 📖 Cuándo usar la Ley de Tangentes

Es útil en el caso **LAL** (dos lados y el ángulo incluido) para encontrar los otros ángulos **directamente**, sin calcular primero el tercer lado.

---

## 📖 Ejemplo

En un triángulo, $a = 8$, $b = 5$ y $C = 60°$. Encuentra los ángulos $A$ y $B$.

### Paso 1: Calcular $A + B$

$$
A + B = 180° - C = 180° - 60° = 120°
$$

### Paso 2: Aplicar Ley de Tangentes

$$
\frac{a - b}{a + b} = \frac{\tan\frac{A - B}{2}}{\tan\frac{A + B}{2}}
$$

$$
\frac{8 - 5}{8 + 5} = \frac{\tan\frac{A - B}{2}}{\tan 60°}
$$

$$
\frac{3}{13} = \frac{\tan\frac{A - B}{2}}{\sqrt{3}}
$$

$$
\tan\frac{A - B}{2} = \frac{3\sqrt{3}}{13} \approx 0.4
$$

$$
\frac{A - B}{2} = \arctan(0.4) \approx 21.8°
$$

$$
A - B \approx 43.6°
$$

### Paso 3: Resolver el sistema

$$
A + B = 120°
$$

$$
A - B = 43.6°
$$

Sumando: $2A = 163.6°$, entonces $A \approx 81.8°$

Restando: $2B = 76.4°$, entonces $B \approx 38.2°$

---

## 📖 Verificación

Usemos la Ley de Senos para verificar:

$$
\frac{8}{\sin 81.8°} = \frac{5}{\sin 38.2°}
$$

$$
\frac{8}{0.990} \approx 8.08 \quad \text{y} \quad \frac{5}{0.618} \approx 8.09
$$

¡Correcto! (La pequeña diferencia es por redondeo)

---

## 📖 Comparación con otras leyes

| Ley | Ventaja | Desventaja |
|-----|---------|------------|
| Senos | Simple para ALA/LAA | No funciona para LAL/LLL directamente |
| Cosenos | Funciona para LAL/LLL | Requiere raíz cuadrada |
| Tangentes | Da ángulos directamente en LAL | Fórmula más compleja |

---

## 📝 Ejercicios de práctica

### Ejercicio 1

En un triángulo, $a = 12$, $b = 8$ y $C = 50°$. Usa la Ley de Tangentes para encontrar $A$ y $B$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$A + B = 130°$, así que $\frac{A+B}{2} = 65°$

$$
\frac{12 - 8}{12 + 8} = \frac{\tan\frac{A - B}{2}}{\tan 65°}
$$

$$
\frac{4}{20} = \frac{\tan\frac{A - B}{2}}{2.145}
$$

$$
\tan\frac{A - B}{2} = 0.2 \times 2.145 = 0.429
$$

$$
\frac{A - B}{2} = \arctan(0.429) \approx 23.2°
$$

$A - B \approx 46.4°$

Sistema:
- $A + B = 130°$
- $A - B = 46.4°$

$A = 88.2°$, $B = 41.8°$

</details>

---

### Ejercicio 2

Verifica tu respuesta del ejercicio anterior usando la Ley de Cosenos para encontrar $c$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
c^2 = 144 + 64 - 2(12)(8)\cos 50°
$$

$$
c^2 = 208 - 192(0.643) = 208 - 123.5 = 84.5
$$

$c \approx 9.19$

Verificando con Ley de Senos:

$$
\frac{9.19}{\sin 50°} = \frac{12}{\sin 88.2°}
$$

$$
12 \approx 12 \quad ✓
$$

</details>

---
