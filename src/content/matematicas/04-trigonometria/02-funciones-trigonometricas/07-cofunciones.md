# **Cofunciones**

¿Alguna vez notaste que $\sin(30°) = 0.5$ y $\cos(60°) = 0.5$? No es una coincidencia. El seno y el coseno son como hermanos gemelos que funcionan en espejo. A esta relación la llamamos **Cofunciones**, porque una es el **complemento** de la otra.

---

## 🎯 ¿Qué vas a aprender?

- Qué son las cofunciones y por qué existen.
- La relación entre un ángulo y su complemento ($90° - \theta$).
- Cómo transformar senos en cosenos, tangentes en cotangentes, etc.
- Cómo usar esto para simplificar expresiones complicadas.

---

## 🤝 El Prefijo "CO" Significa Complementario

El nombre lo dice todo:
*   **Co**seno = Seno del **Co**mplemento.
*   **Co**tangente = Tangente del **Co**mplemento.
*   **Co**secante = Secante del **Co**mplemento.

> **Definición:** Dos ángulos son complementarios si suman 90°.
> Si tienes un ángulo $\theta$, su complemento es $90° - \theta$.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Cofunciones en el triángulo rectángulo</strong>
  </div>

![Cofunciones](/images/trigonometria/circulo-unitario/cofunciones.svg)

</div>

Geométricamente, en un triángulo rectángulo, los dos ángulos agudos siempre suman 90°. El cateto **opuesto** para uno es el cateto **adyacente** para el otro.

---

## 🔄 Las Identidades

Para cualquier ángulo $\theta$:

### 1. Seno y Coseno

$$
\sin(\theta) = \cos(90° - \theta)
$$

$$
\cos(\theta) = \sin(90° - \theta)
$$

### 2. Tangente y Cotangente

$$
\tan(\theta) = \cot(90° - \theta)
$$

$$
\cot(\theta) = \tan(90° - \theta)
$$

### 3. Secante y Cosecante

$$
\sec(\theta) = \csc(90° - \theta)
$$

$$
\csc(\theta) = \sec(90° - \theta)
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Escribe $\sin(20°)$ en términos de coseno.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sin(\theta) = \cos(90° - \theta)$.
$\cos(90° - 20°) = \cos(70°)$.

**Respuesta:** $\boxed{\cos(70°)}$
</details>

---

### Ejercicio 2
Escribe $\tan(50°)$ en términos de cofunción.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La cofunción de tangente es cotangente.
$\cot(90° - 50°) = \cot(40°)$.

**Respuesta:** $\boxed{\cot(40°)}$
</details>

---

### Ejercicio 3
Simplifica la expresión: $\sin(35°) - \cos(55°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Convertimos el coseno a seno:
$\cos(55°) = \sin(90° - 55°) = \sin(35°)$.
La expresión queda: $\sin(35°) - \sin(35°)$.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 4
Si $\sec(75°) = x$, ¿cuánto vale $\csc(15°)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\csc(15°) = \sec(90° - 15°) = \sec(75°)$.
Como $\sec(75°) = x$, entonces $\csc(15°) = x$.

**Respuesta:** $\boxed{x}$
</details>

---

### Ejercicio 5
Encuentra el valor de $\frac{\tan(20°)}{\cot(70°)}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cot(70°) = \tan(90° - 70°) = \tan(20°)$.
La fracción queda $\frac{\tan(20°)}{\tan(20°)}$.
Cualquier cosa dividida por sí misma es 1.

**Respuesta:** $\boxed{1}$
</details>

---

### Ejercicio 6
Escribe $\cos(\frac{\pi}{3})$ usando su cofunción en radianes.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
En radianes, 90° es $\frac{\pi}{2}$.
$\cos(\frac{\pi}{3}) = \sin(\frac{\pi}{2} - \frac{\pi}{3})$.
$\frac{3\pi}{6} - \frac{2\pi}{6} = \frac{\pi}{6}$.

**Respuesta:** $\boxed{\sin\left(\frac{\pi}{6}\right)}$
</details>

---

### Ejercicio 7
Resuelve para $x$: $\sin(2x) = \cos(x)$ donde $2x$ es agudo.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Para que sean iguales, sus ángulos deben ser complementarios (sumar 90°).
$2x + x = 90°$.
$3x = 90° \rightarrow x = 30°$.

**Respuesta:** $\boxed{x = 30°}$
</details>

---

### Ejercicio 8
Simplifica $\sin^2(40°) + \sin^2(50°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sabemos que $\sin(50°) = \cos(40°)$.
La expresión se convierte en: $\sin^2(40°) + \cos^2(40°)$.
Por la identidad pitagórica, esto siempre es 1.

**Respuesta:** $\boxed{1}$
</details>

---

### Ejercicio 9
Determina si es verdadero: $\cot(10°) = \tan(80°)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Calculamos el complemento de 10°: $90 - 10 = 80$.
La cofunción de cotangente es tangente.
La igualdad es correcta.

**Respuesta:** **Verdadero**
</details>

---

### Ejercicio 10
Si $\csc(A) = \sec(B)$, ¿qué relación hay entre A y B?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si función y cofunción son iguales, los ángulos deben ser complementarios.
$A + B = 90°$ (o $\frac{\pi}{2}$ radianes).

**Respuesta:** **Suman 90°**
</details>

---

## 🔑 Resumen

| Función | Se convierte en... | Ángulo resultante |
| :---: | :---: | :---: |
| **Seno** | Coseno | Complementario ($90 - x$) |
| **Tangente** | Cotangente | Complementario ($90 - x$) |
| **Secante** | Cosecante | Complementario ($90 - x$) |

> **Conclusión:** Las cofunciones son la razón por la que solo necesitas memorizar la mitad de las tablas trigonométricas. Si sabes el seno de 30°, automáticamente sabes el coseno de 60°.
