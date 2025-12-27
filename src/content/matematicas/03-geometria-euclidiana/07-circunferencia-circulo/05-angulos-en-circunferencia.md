# **Ángulos en la Circunferencia**

¿Has notado que en el cine, sin importar si te sientas en el centro o al costado, el ángulo de visión cambia? En una circunferencia, la posición desde donde observas un arco determina matemáticamente el ángulo que ves.

---

## 🎯 ¿Qué vas a aprender?

- Diferenciar entre ángulo central, inscrito, semi-inscrito, interior y exterior.
- Calcular la medida de ángulos basándose en los arcos que interceptan.
- Aplicar la propiedad fundamental de que el ángulo inscrito es la mitad del central.
- Usar las fórmulas de semisuma y semidiferencia para ángulos interiores y exteriores.

---

## 📍 Ángulos según el Vértice

La clave para saber qué fórmula usar es mirar **dónde está el vértice** (la punta del ángulo).

### 1. Ángulo Central (Vértice en el Centro)
Es el jefe. Su medida es exactamente igual a la del arco que abarca.

<div style="width: 100%; margin-bottom: 20px;">
  <img src="/images/geometria/circulos/angulo-central.svg" alt="Ángulo central" style="width: 100%; height: auto;">
</div>

$$
\text{Ángulo Central} = \text{Arco}
$$

### 2. Ángulo Inscrito (Vértice en el Borde)
Es el más común. Su vértice toca la circunferencia y sus lados la cortan.
> **Propiedad de Oro:** Mide la **mitad** del arco que tiene enfrente.

<div style="width: 100%; margin-bottom: 20px;">
  <img src="/images/geometria/circulos/angulo-inscrito.svg" alt="Ángulo inscrito" style="width: 100%; height: auto;">
</div>

$$
\text{Ángulo Inscrito} = \frac{\text{Arco}}{2}
$$

### 3. Ángulo Semi-Inscrito (Vértice en el Borde, Tangente)
Tiene un pie dentro (cuerda) y otro fuera (tangente). Su vértice es el punto de tangencia.
Funciona igual que el inscrito: mide la **mitad** del arco.

<div style="width: 100%; margin-bottom: 20px;">
  <img src="/images/geometria/circulos/angulo-semi-inscrito.svg" alt="Ángulo semi-inscrito" style="width: 100%; height: auto;">
</div>

$$
\text{Ángulo Semi-Inscrito} = \frac{\text{Arco}}{2}
$$

---

## ➕➖ Ángulos Interior y Exterior

### 4. Ángulo Interior (Vértice Adentro)
Se forma cuando dos cuerdas se cruzan en un punto interior (no el centro).
Mira a dos arcos (uno al frente y otro a su espalda).
> **Fórmula:** La **Semisuma** de los arcos.

<div style="width: 100%; margin-bottom: 20px;">
  <img src="/images/geometria/circulos/angulo-interior.svg" alt="Ángulo interior" style="width: 100%; height: auto;">
</div>

$$
\text{Interior} = \frac{\text{Arco Mayor} + \text{Arco Menor}}{2}
$$

### 5. Ángulo Exterior (Vértice Afuera)
Se forma cuando dos líneas se encuentran fuera de la circunferencia.
Atrapa dos arcos entre sus "brazos" (uno grande lejos y uno pequeño cerca).
> **Fórmula:** La **Semidiferencia** de los arcos.

<div style="width: 100%; margin-bottom: 20px;">
  <img src="/images/geometria/circulos/angulo-exterior.svg" alt="Ángulo exterior" style="width: 100%; height: auto;">
</div>

$$
\text{Exterior} = \frac{\text{Arco Mayor} - \text{Arco Menor}}{2}
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Cálculo de Ángulo Inscrito

Si un arco mide $80^\circ$, ¿cuánto mide el ángulo inscrito que lo mira?

**Razonamiento:**
El ángulo inscrito es la mitad del arco.

$$
\alpha = \frac{80^\circ}{2}
$$

**Resultado:**
$$
\boxed{40^\circ}
$$

### Ejemplo 2: Ángulo Exterior

Desde un punto exterior, un ángulo intercepta dos arcos de $100^\circ$ y $30^\circ$. Calcula el ángulo.

**Razonamiento:**
Usamos la semidiferencia.

$$
\alpha = \frac{100 - 30}{2} = \frac{70}{2}
$$

**Resultado:**
$$
\boxed{35^\circ}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
El ángulo central mide $50^\circ$. ¿Cuánto mide el arco correspondiente?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Central = Arco.

**Resultado:**
$$
\boxed{50^\circ}
$$

</details>

### Ejercicio 2
Un ángulo inscrito subtiende (mira a) un diámetro. ¿Cuánto mide?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
El arco de un diámetro es media vuelta ($180^\circ$).
Inscrito = $180 / 2$.

**Resultado:**
$$
\boxed{90^\circ}
$$

</details>

### Ejercicio 3
Dos cuerdas se cruzan. Los arcos miden $40^\circ$ y $80^\circ$. Calcula el ángulo interior.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Semisuma.
$$
\frac{40+80}{2} = \frac{120}{2}
$$

**Resultado:**
$$
\boxed{60^\circ}
$$

</details>

### Ejercicio 4
Si el ángulo inscrito mide $30^\circ$, ¿cuánto mide el arco?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Arco = Doble del inscrito.
$$
2 \times 30
$$

**Resultado:**
$$
\boxed{60^\circ}
$$

</details>

### Ejercicio 5
Calcula el ángulo exterior si los arcos son $120^\circ$ y $40^\circ$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Semidiferencia.
$$
\frac{120-40}{2} = \frac{80}{2}
$$

**Resultado:**
$$
\boxed{40^\circ}
$$

</details>

### Ejercicio 6
Un ángulo semi-inscrito abarca un arco de $140^\circ$. Calcúlalo.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Mitad del arco.

**Resultado:**
$$
\boxed{70^\circ}
$$

</details>

### Ejercicio 7
Todos los ángulos inscritos que miran al mismo arco son iguales. ¿Verdadero o Falso?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Verdadero. Si el arco es constante, su mitad también lo es.

**Resultado:**
$$
\boxed{\text{Verdadero}}
$$

</details>

### Ejercicio 8
Si el ángulo central es $80^\circ$, ¿cuánto mide el ángulo inscrito que mira al mismo arco?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Inscrito es la mitad del central.

**Resultado:**
$$
\boxed{40^\circ}
$$

</details>

### Ejercicio 9
Arco mayor = $200^\circ$, Arco menor = $60^\circ$. Vértice exterior. Calcula.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
\frac{200-60}{2} = \frac{140}{2}
$$

**Resultado:**
$$
\boxed{70^\circ}
$$

</details>

### Ejercicio 10
Si un cuadrilátero está inscrito en una circunferencia, sus ángulos opuestos suman $180^\circ$. ¿Por qué?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Porque entre los dos ángulos inscritos opuestos abarcan la circunferencia completa ($360^\circ$). La suma de sus medidas será $360/2 = 180^\circ$.

**Resultado:**
$$
\boxed{\text{Son suplementarios}}
$$

</details>

---

## 🔑 Resumen

| Ángulo | Ubicación Vértice | Fórmula |
| :--- | :--- | :--- |
| **Central** | Centro | $= \text{Arco}$ |
| **Inscrito** | Borde | $= \text{Arco}/2$ |
| **Semi-Inscrito** | Borde (Tangente) | $= \text{Arco}/2$ |
| **Interior** | Adentro | $= \text{Suma}/2$ |
| **Exterior** | Afuera | $= \text{Resta}/2$ |

> Recuerda: Adentro $\to$ Suma. Afuera $\to$ Resta. Borde $\to$ Mitad.
