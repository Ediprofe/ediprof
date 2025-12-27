# **Resolución de Triángulos Rectángulos**

En el mundo real, rara vez te dan todos los datos. Un arquitecto puede saber la altura del techo y el ancho de la casa, pero no la longitud de la viga inclinada. "Resolver un triángulo" significa encontrar los 3 lados y los 3 ángulos usando las pistas que tienes.

---

## 🎯 ¿Qué vas a aprender?

- Cómo encontrar lados desconocidos usando SOH-CAH-TOA.
- Cómo encontrar ángulos desconocidos usando funciones inversas ($\sin^{-1}, \cos^{-1}, \tan^{-1}$).
- La estrategia paso a paso para resolver cualquier triángulo rectángulo.

---

## 🕵️‍♂️ El Arte de ser Detective

Para resolver un triángulo rectángulo, necesitas al menos **dos pistas** (además del ángulo recto):
1.  Un lado y un ángulo.
2.  Dos lados.

### Herramienta 1: Encontrar Lados
Si tienes el ángulo, usas las razones normales ($\sin, \cos, \tan$).

### Herramienta 2: Encontrar Ángulos
Si buscas el ángulo, usas las funciones **inversas** (Arco-funciones). En tu calculadora aparecen como $\sin^{-1}$, $\cos^{-1}$, $\tan^{-1}$.

> **Nota:** $\sin^{-1}(0.5)$ se lee "el ángulo cuyo seno es 0.5".

![Resolver un triángulo: θ = 35°, Adyacente = 10](/images/geometria/trigonometria/06-resolver-triangulo.svg)

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Tengo un lado y un ángulo (Caso Arquitecto)

Ángulo $\theta = 30^{\circ}$, Hipotenusa = 10. Queremos el cateto opuesto ($x$).

**Razonamiento:**
1.  **Identificar:** Tengo ángulo (30°), quiero Opuesto ($x$), tengo Hipotenusa (10).
2.  **Elegir:** ¿Qué razón usa O e H? $\rightarrow$ **Seno**.
3.  **Plantear:** $\sin(30^{\circ}) = \frac{x}{10}$.
4.  **Despejar:** $x = 10 \cdot \sin(30^{\circ})$.
5.  **Calcular:** $x = 10 \cdot 0.5 = 5$.

**Resultado:**
$$
\boxed{x = 5}
$$

### Ejemplo 2: Tengo dos lados (Caso Topógrafo)

Opuesto = 3, Adyacente = 4. Queremos el ángulo $\theta$.

**Razonamiento:**
1.  **Identificar:** Tengo Opuesto y Adyacente.
2.  **Elegir:** ¿Qué razón usa O y A? $\rightarrow$ **Tangente**.
3.  **Plantear:** $\tan(\theta) = \frac{3}{4} = 0.75$.
4.  **Despejar:** $\theta = \tan^{-1}(0.75)$.
5.  **Calcular:** $\theta \approx 36.87^{\circ}$.

**Resultado:**
$$
\boxed{\theta \approx 36.87^{\circ}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Encuentra el cateto opuesto si $\theta=45^{\circ}$ y la hipotenusa es $10\sqrt{2}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sin(45) = O / 10\sqrt{2}$.
$O = 10\sqrt{2} \cdot (\sqrt{2}/2) = 10(2)/2 = 10$.

**Resultado:**
$$
\boxed{10}
$$

</details>

### Ejercicio 2
Encuentra $\theta$ si $\sin(\theta) = 0.5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sabemos de memoria que $\sin(30)=0.5$.

**Resultado:**
$$
\boxed{30^{\circ}}
$$

</details>

### Ejercicio 3
Tienes un triángulo rectángulo. Un ángulo es 20°. ¿Cuánto mide el otro ángulo agudo?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Deben sumar 90°. $90 - 20 = 70$.

**Resultado:**
$$
\boxed{70^{\circ}}
$$

</details>

### Ejercicio 4
Si $\tan(\theta) = 1$, halla $\theta$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan^{-1}(1) = 45^{\circ}$.

**Resultado:**
$$
\boxed{45^{\circ}}
$$

</details>

### Ejercicio 5
Calcula la hipotenusa si Adyacente=5 y $\theta=60^{\circ}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\cos(60) = 5/H$.
$0.5 = 5/H \Rightarrow H = 5/0.5 = 10$.

**Resultado:**
$$
\boxed{10}
$$

</details>

### Ejercicio 6
Encuentra $\theta$ si Opuesto=4 e Hipotenusa=5.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sin(\theta) = 4/5 = 0.8$.
$\theta = \sin^{-1}(0.8) \approx 53.13^{\circ}$.

**Resultado:**
$$
\boxed{\approx 53.13^{\circ}}
$$

</details>

### Ejercicio 7
Una escalera de 6 m se apoya en una pared haciendo un ángulo de 60° con el suelo. ¿A qué altura llega?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Hipotenusa=6, Ángulo=60°, buscamos Opuesto.
$O = 6 \cdot \sin(60) = 6 \cdot (\sqrt{3}/2) = 3\sqrt{3}$.

**Resultado:**
$$
\boxed{3\sqrt{3} \approx 5.2 \text{ m}}
$$

</details>

### Ejercicio 8
Si los catetos miden 1 y $\sqrt{3}$, ¿cuánto mide el ángulo opuesto al cateto de 1?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\tan(\theta) = 1/\sqrt{3} = \sqrt{3}/3$.
Corresponde a 30°.

**Resultado:**
$$
\boxed{30^{\circ}}
$$

</details>

### Ejercicio 9
Calcula el cateto adyacente si Opuesto=10 y $\tan(\theta)=2$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2 = 10/A \Rightarrow A = 10/2 = 5$.

**Resultado:**
$$
\boxed{5}
$$

</details>

### Ejercicio 10
Si conoces los 3 lados, ¿puedes encontrar los ángulos?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Sí, usando cualquier función inversa ($\sin^{-1}, \cos^{-1}$ o $\tan^{-1}$).

**Resultado:**
$$
\boxed{\text{Sí}}
$$

</details>

---

## 🔑 Resumen

| ¿Qué buscas? | Herramienta | Ejemplo |
| :--- | :--- | :--- |
| **Un Lado** | Razones directas | $x = H \cdot \sin(\theta)$ |
| **Un Ángulo** | Funciones inversas | $\theta = \tan^{-1}(O/A)$ |
| **El otro ángulo** | Resta | $90^{\circ} - \text{conocido}$ |

> No olvides comprobar: los lados más grandes deben estar frente a los ángulos más grandes.
