# Transformación de Productos a Sumas

Las **identidades de producto a suma** (y suma a producto) permiten convertir productos de funciones trigonométricas en sumas, y viceversa.

<div style="background: linear-gradient(135deg, #dcfce7 0%, #fef3c7 100%); border: 2px solid #16a34a; border-radius: 12px; padding: 1.2rem; margin: 1.5rem 0;">
<div style="font-weight: bold; color: #166534; margin-bottom: 0.8rem;">📋 Resumen Rápido</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; font-size: 0.9rem;">
<div>
<strong style="color: #3b82f6;">Producto → Suma</strong><br>
sin α cos β = ½[sin(α+β) + sin(α-β)]<br>
cos α cos β = ½[cos(α+β) + cos(α-β)]
</div>
<div>
<strong style="color: #dc2626;">Suma → Producto</strong><br>
sin A + sin B = 2 sin((A+B)/2) cos((A-B)/2)<br>
cos A + cos B = 2 cos((A+B)/2) cos((A-B)/2)
</div>
</div>
<div style="margin-top: 0.8rem; font-size: 0.85rem; color: #64748b;">
💡 Útiles en cálculo integral y análisis de ondas (batimiento)
</div>
</div>

---

## 📖 Producto a suma

### Producto de senos y cosenos

$$
\sin\alpha\cos\beta = \frac{1}{2}[\sin(\alpha + \beta) + \sin(\alpha - \beta)]
$$

$$
\cos\alpha\sin\beta = \frac{1}{2}[\sin(\alpha + \beta) - \sin(\alpha - \beta)]
$$

$$
\cos\alpha\cos\beta = \frac{1}{2}[\cos(\alpha + \beta) + \cos(\alpha - \beta)]
$$

$$
\sin\alpha\sin\beta = \frac{1}{2}[\cos(\alpha - \beta) - \cos(\alpha + \beta)]
$$

---

## 📖 Suma a producto

### Sumas de senos y cosenos

$$
\sin A + \sin B = 2\sin\frac{A + B}{2}\cos\frac{A - B}{2}
$$

$$
\sin A - \sin B = 2\cos\frac{A + B}{2}\sin\frac{A - B}{2}
$$

$$
\cos A + \cos B = 2\cos\frac{A + B}{2}\cos\frac{A - B}{2}
$$

$$
\cos A - \cos B = -2\sin\frac{A + B}{2}\sin\frac{A - B}{2}
$$

---

## 📖 Ejemplo 1: Producto a suma

Expresar $\sin 5x \cos 3x$ como suma:

$$
\sin 5x \cos 3x = \frac{1}{2}[\sin(5x + 3x) + \sin(5x - 3x)]
$$

$$
= \frac{1}{2}[\sin 8x + \sin 2x]
$$

---

## 📖 Ejemplo 2: Suma a producto

Expresar $\sin 7x + \sin 3x$ como producto:

$$
\sin 7x + \sin 3x = 2\sin\frac{7x + 3x}{2}\cos\frac{7x - 3x}{2}
$$

$$
= 2\sin 5x \cos 2x
$$

---

## 📖 Utilidad

### En cálculo

Estas identidades facilitan la integración de productos trigonométricos.

### En física

Útiles para analizar ondas y fenómenos de batimiento (beats).

### Ejemplo: Batimiento

Cuando dos ondas con frecuencias cercanas se suman:

$$
\cos\omega_1 t + \cos\omega_2 t = 2\cos\frac{\omega_1 + \omega_2}{2}t \cos\frac{\omega_1 - \omega_2}{2}t
$$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Producto a suma

Expresa como suma o diferencia:

1. $\cos 4x \cos 2x$
2. $\sin 6x \sin 2x$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\cos 4x \cos 2x = \frac{1}{2}[\cos 6x + \cos 2x]$

2. $\sin 6x \sin 2x = \frac{1}{2}[\cos 4x - \cos 8x]$

</details>

---

### Ejercicio 2: Suma a producto

Expresa como producto:

1. $\cos 5x + \cos 3x$
2. $\sin 4x - \sin 2x$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. $\cos 5x + \cos 3x = 2\cos 4x \cos x$

2. $\sin 4x - \sin 2x = 2\cos 3x \sin x$

</details>

---

### Ejercicio 3: Simplificar

Simplifica: $\frac{\sin 5x + \sin x}{\cos 5x + \cos x}$

<details>
<summary><strong>Ver respuesta</strong></summary>

Numerador: $\sin 5x + \sin x = 2\sin 3x \cos 2x$

Denominador: $\cos 5x + \cos x = 2\cos 3x \cos 2x$

$$
\frac{2\sin 3x \cos 2x}{2\cos 3x \cos 2x} = \frac{\sin 3x}{\cos 3x} = \tan 3x
$$

</details>

---

### Ejercicio 4: Verificar

Verifica que $\cos 3x - \cos x = -2\sin 2x \sin x$.

<details>
<summary><strong>Ver respuesta</strong></summary>

Usando la fórmula:

$$
\cos A - \cos B = -2\sin\frac{A + B}{2}\sin\frac{A - B}{2}
$$

Con $A = 3x$, $B = x$:

$$
= -2\sin\frac{3x + x}{2}\sin\frac{3x - x}{2} = -2\sin 2x \sin x \quad ✓
$$

</details>

---
