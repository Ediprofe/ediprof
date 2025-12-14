# Resolución de Triángulos Rectángulos

**Resolver un triángulo** significa encontrar todas sus medidas: los tres lados y los tres ángulos. Con las razones trigonométricas, podemos hacerlo conociendo pocos datos.

---

## 📖 ¿Qué necesitamos para resolver?

Para resolver un triángulo rectángulo necesitamos:
- **Un lado** y **un ángulo agudo**, o
- **Dos lados**

Con estos datos podemos encontrar todo lo demás.

---

## 📖 Estrategia general

1. **Identificar** qué datos tenemos
2. **Elegir** la razón trigonométrica adecuada
3. **Plantear** la ecuación
4. **Resolver** para el elemento desconocido
5. **Verificar** (suma de ángulos = 180°, teorema de Pitágoras)

---

## 📖 Caso 1: Conocemos un lado y un ángulo agudo

### Ejemplo 1

Triángulo rectángulo con $\theta = 35°$ y el cateto adyacente $= 10$ cm.

**Encontrar el cateto opuesto:**

$$
\tan 35° = \frac{O}{10}
$$

$$
O = 10 \times \tan 35° = 10 \times 0.7002 \approx 7.0 \text{ cm}
$$

**Encontrar la hipotenusa:**

$$
\cos 35° = \frac{10}{H}
$$

$$
H = \frac{10}{\cos 35°} = \frac{10}{0.8192} \approx 12.2 \text{ cm}
$$

---

### Ejemplo 2

Triángulo con $\theta = 50°$ e hipotenusa $= 20$ cm.

**Cateto opuesto:**

$$
\sin 50° = \frac{O}{20}
$$

$$
O = 20 \times \sin 50° \approx 20 \times 0.766 \approx 15.3 \text{ cm}
$$

**Cateto adyacente:**

$$
\cos 50° = \frac{A}{20}
$$

$$
A = 20 \times \cos 50° \approx 20 \times 0.643 \approx 12.9 \text{ cm}
$$

---

## 📖 Caso 2: Conocemos dos lados

Usamos funciones trigonométricas inversas (arcsen, arccos, arctan).

### Ejemplo 3

Cateto opuesto = 6, cateto adyacente = 8.

**Encontrar el ángulo:**

$$
\tan\theta = \frac{6}{8} = 0.75
$$

$$
\theta = \arctan(0.75) \approx 36.87°
$$

**Encontrar la hipotenusa:**

$$
H = \sqrt{6^2 + 8^2} = \sqrt{100} = 10
$$

**El otro ángulo agudo:**

$$
90° - 36.87° = 53.13°
$$

---

## 📖 Funciones inversas

| Función | Inversa | Símbolo alternativo |
|---------|---------|---------------------|
| $\sin$ | $\arcsin$ | $\sin^{-1}$ |
| $\cos$ | $\arccos$ | $\cos^{-1}$ |
| $\tan$ | $\arctan$ | $\tan^{-1}$ |

### Uso en calculadora

Para encontrar $\theta$ si $\sin\theta = 0.5$:

$$
\theta = \arcsin(0.5) = 30°
$$

---

## 📖 Verificación

Siempre verifica tus resultados:
- Los ángulos agudos deben sumar 90°
- Aplica Pitágoras: $a^2 + b^2 = c^2$

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Un lado y un ángulo

Triángulo rectángulo con $\theta = 40°$ y cateto opuesto = 12 cm.
Encuentra el cateto adyacente y la hipotenusa.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\tan 40° = \frac{12}{A} \Rightarrow A = \frac{12}{\tan 40°} \approx \frac{12}{0.839} \approx 14.3 \text{ cm}
$$

$$
\sin 40° = \frac{12}{H} \Rightarrow H = \frac{12}{\sin 40°} \approx \frac{12}{0.643} \approx 18.7 \text{ cm}
$$

</details>

---

### Ejercicio 2: Dos lados

Cateto opuesto = 5, hipotenusa = 13. Encuentra el ángulo $\theta$.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\sin\theta = \frac{5}{13} \approx 0.385
$$

$$
\theta = \arcsin(0.385) \approx 22.6°
$$

</details>

---

### Ejercicio 3: Problema completo

En un triángulo rectángulo, un ángulo agudo mide 55° y la hipotenusa mide 25 m. Resuelve el triángulo completamente.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Ángulos:** 90°, 55°, 35°

**Cateto opuesto a 55°:**
$$
O = 25 \times \sin 55° \approx 25 \times 0.819 \approx 20.5 \text{ m}
$$

**Cateto adyacente a 55°:**
$$
A = 25 \times \cos 55° \approx 25 \times 0.574 \approx 14.3 \text{ m}
$$

**Verificación:** $20.5^2 + 14.3^2 = 420.25 + 204.49 = 624.74 \approx 25^2 = 625$ ✓

</details>

---
