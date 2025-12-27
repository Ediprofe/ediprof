# **Demostración de Identidades**

Demostrar una identidad es como resolver un rompecabezas: sabes cómo debe verse la imagen final, pero tienes que mover las piezas para llegar ahí. En matemáticas, significa probar que un lado de la ecuación es **idéntico** al otro para cualquier valor del ángulo.

---

## 🎯 ¿Qué vas a aprender?

- La regla de oro: nunca cruzar el "muro" del signo igual.
- Las 3 estrategias maestras para atacar cualquier demostración.
- Cómo usar el conjugado para desbloquear fracciones difíciles.
- Cómo convertir todo a senos y cosenos cuando te quedes atascado.

---

## 🏗️ Las 3 Reglas del Juego

1.  **Elige un lado:** Empieza siempre por el lado más **complicado** (el que tenga más sumas, restas o fracciones). Es más fácil simplificar que construir.
2.  **No cruces el río:** Trata el signo "=" como un muro. No puedes pasar términos de un lado al otro. Debes transformar un solo lado hasta que se vea igual al otro.
3.  **Ten la meta a la vista:** Mira siempre a dónde quieres llegar para saber qué pasos tomar.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Estrategias para Demostrar Identidades</strong>
  </div>

![Estrategias de demostración](/images/trigonometria/identidades/estrategias-demostracion.svg)

</div>

---

## 🛠️ Herramientas de Combate

### 1. El comodín (Seno y Coseno)
Si ves $\tan, \cot, \sec, \csc$ y te confundes, conviértelo todo a $\sin$ y $\cos$.

### 2. Fracciones
Si hay dos fracciones, súmalas buscando un denominador común.
$$
\frac{1}{\sin x} + \frac{1}{\cos x} = \frac{\cos x + \sin x}{\sin x \cos x}
$$

### 3. Conjugados
Si ves $1-\sin x$ en el denominador, multiplica arriba y abajo por su "gemelo bueno" $1+\sin x$. Esto creará una **diferencia de cuadrados** ($1-\sin^2x = \cos^2x$) que simplifica todo.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Suma de fracciones
Demuestra: $\tan x + \cot x = \sec x \csc x$

**Paso 1: Convertir a Seno/Coseno (Lado Izquierdo)**
$$
\frac{\sin x}{\cos x} + \frac{\cos x}{\sin x}
$$

**Paso 2: Denominador Común**
$$
\frac{\sin x(\sin x) + \cos x(\cos x)}{\cos x \sin x} = \frac{\sin^2 x + \cos^2 x}{\cos x \sin x}
$$

**Paso 3: Identidad Pitagórica**
$$
\frac{1}{\cos x \sin x}
$$

**Paso 4: Separar**
$$
\frac{1}{\cos x} \cdot \frac{1}{\sin x} = \sec x \csc x
$$

**Resultado:** Q.E.D.

---

### Ejemplo 2: Diferencia de Cuadrados
Demuestra: $\cos^4 x - \sin^4 x = \cos(2x)$

**Paso 1: Factorizar (Lado Izquierdo)**
Es una diferencia de cuadrados $(a^2 - b^2)(a^2 + b^2)$.
$$
(\cos^2 x - \sin^2 x)(\cos^2 x + \sin^2 x)
$$

**Paso 2: Simplificar**
Sabemos que $\cos^2 x + \sin^2 x = 1$.
$$
(\cos^2 x - \sin^2 x)(1)
$$

**Paso 3: Identidad de Ángulo Doble**
$$
\cos^2 x - \sin^2 x = \cos(2x)
$$

**Resultado:** Q.E.D.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Demuestra que $(1 - \cos^2 x)\csc^2 x = 1$.

<details>
<summary>Ver demostración</summary>

**Razonamiento:**
1.  Sustituir $1-\cos^2x = \sin^2x$.
2.  $\sin^2x \cdot \frac{1}{\sin^2x}$.
3.  $1$.

**Respuesta:** **Q.E.D.**
</details>

---

### Ejercicio 2
Demuestra que $\tan x \cos x = \sin x$.

<details>
<summary>Ver demostración</summary>

**Razonamiento:**
1.  $\frac{\sin x}{\cos x} \cdot \cos x$.
2.  Cancelamos cosenos.
3.  $\sin x$.

**Respuesta:** **Q.E.D.**
</details>

---

### Ejercicio 3
Demuestra que $\frac{\sin x}{1+\cos x} = \frac{1-\cos x}{\sin x}$.

<details>
<summary>Ver demostración</summary>

**Razonamiento:**
1.  Multiplica el lado izquierdo por el conjugado $\frac{1-\cos x}{1-\cos x}$.
2.  Arriba: $\sin x(1-\cos x)$. Abajo: $1-\cos^2x = \sin^2x$.
3.  Simplifica un seno: $\frac{1-\cos x}{\sin x}$.

**Respuesta:** **Q.E.D.**
</details>

---

### Ejercicio 4
Demuestra que $\sec x - \tan x \sin x = \cos x$.

<details>
<summary>Ver demostración</summary>

**Razonamiento:**
1.  $\frac{1}{\cos x} - \frac{\sin x}{\cos x}\sin x$.
2.  $\frac{1 - \sin^2x}{\cos x}$.
3.  $\frac{\cos^2x}{\cos x} = \cos x$.

**Respuesta:** **Q.E.D.**
</details>

---

### Ejercicio 5
Demuestra que $(\sin x + \cos x)^2 = 1 + \sin(2x)$.

<details>
<summary>Ver demostración</summary>

**Razonamiento:**
1.  Expandir binomio: $\sin^2x + 2\sin x \cos x + \cos^2x$.
2.  Agrupar $(\sin^2x + \cos^2x) + (2\sin x \cos x)$.
3.  $1 + \sin(2x)$.

**Respuesta:** **Q.E.D.**
</details>

---

### Ejercicio 6
Demuestra que $\frac{1}{\sec^2 x} + \frac{1}{\csc^2 x} = 1$.

<details>
<summary>Ver demostración</summary>

**Razonamiento:**
1.  Convertir a recíprocos: $\cos^2 x + \sin^2 x$.
2.  Identidad fundamental: $1$.

**Respuesta:** **Q.E.D.**
</details>

---

### Ejercicio 7
Demuestra que $\cot x + \tan x = \sec x \csc x$.

<details>
<summary>Ver demostración</summary>

**Razonamiento:**
1.  $\frac{\cos}{\sin} + \frac{\sin}{\cos}$.
2.  $\frac{\cos^2 + \sin^2}{\sin \cos}$.
3.  $\frac{1}{\sin \cos} = \csc x \sec x$.

**Respuesta:** **Q.E.D.**
</details>

---

### Ejercicio 8
Demuestra que $\sin^2 x \cot^2 x + \cos^2 x \tan^2 x = 1$. (Ojo: esta es falsa, vamos a verificar).

<details>
<summary>Ver demostración</summary>

**Razonamiento:**
1.  $\sin^2 \frac{\cos^2}{\sin^2} + \cos^2 \frac{\sin^2}{\cos^2}$.
2.  $\cos^2 x + \sin^2 x = 1$.
3.  ¡Sí, es verdadera!

**Respuesta:** **Q.E.D.**
</details>

---

### Ejercicio 9
Demuestra que $\frac{\tan x}{\sec x} = \sin x$.

<details>
<summary>Ver demostración</summary>

**Razonamiento:**
1.  $\frac{\sin/\cos}{1/\cos}$.
2.  Multiplicamos internos y externos o cancelamos cosenos.
3.  $\sin x$.

**Respuesta:** **Q.E.D.**
</details>

---

### Ejercicio 10
Demuestra que $\cos(2x) = 2\cos^2 x - 1$.

<details>
<summary>Ver demostración</summary>

**Razonamiento:**
1.  Partimos de $\cos(2x) = \cos^2 x - \sin^2 x$.
2.  Sustituimos $\sin^2 x = 1 - \cos^2 x$.
3.  $\cos^2 x - (1 - \cos^2 x) = 2\cos^2 x - 1$.

**Respuesta:** **Q.E.D.**
</details>

---

## 🔑 Resumen

| Herramienta | Cuándo usarla |
| :--- | :--- |
| **Pitagóricas** | Cuando ves cuadrados ($\sin^2, \tan^2 \dots$). |
| **Seno/Coseno** | Cuando hay muchas funciones mezcladas. |
| **Conjugado** | Cuando hay denominadores como $1-\cos x$. |
| **Factorización** | Cuando hay términos comunes o diferencias de cuadrados. |

> **Conclusión:** Demostrar es un arte. Requiere paciencia y saber elegir la herramienta correcta. ¡No te rindas si el primer intento no funciona!
