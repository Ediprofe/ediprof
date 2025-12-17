# Ángulos en la Circunferencia

Los ángulos asociados a la circunferencia tienen propiedades especiales según dónde esté ubicado el vértice. En esta lección estudiamos los tipos principales.

---

## 📖 Tipos de ángulos según la posición del vértice

| Tipo de ángulo | Posición del vértice |
|----------------|---------------------|
| Central | En el centro |
| Inscrito | En la circunferencia |
| Semi-inscrito | En la circunferencia (un lado tangente) |
| Interior | Dentro de la circunferencia |
| Exterior | Fuera de la circunferencia |

---

## 📖 Ángulo central

> **Definición:** Un ángulo central tiene su **vértice en el centro** de la circunferencia y sus lados son radios.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Ángulo Central</strong>
  </div>

![Ángulo central](/images/geometria/circulos/angulo-central.svg)

</div>

### Propiedad

El ángulo central tiene la **misma medida** que el arco que abarca:

$$
\text{Ángulo central} = \text{Arco}
$$

### Ejemplo

Si el ángulo central mide 60°, el arco que abarca también mide 60°.

---

## 📖 Ángulo inscrito

> **Definición:** Un ángulo inscrito tiene su **vértice en la circunferencia** y sus lados son cuerdas.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Ángulo Inscrito</strong>
  </div>

![Ángulo inscrito](/images/geometria/circulos/angulo-inscrito.svg)

</div>

### Propiedad fundamental

El ángulo inscrito mide la **mitad del arco** que abarca:

$$
\text{Ángulo inscrito} = \frac{\text{Arco}}{2}
$$

### Teorema

Un ángulo inscrito es igual a la **mitad del ángulo central** que abarca el mismo arco:

$$
\alpha_{inscrito} = \frac{\alpha_{central}}{2}
$$

### Ejemplo

Si el arco mide 80°, el ángulo inscrito mide $\frac{80°}{2} = 40°$.

---

## 📖 Corolarios importantes

### 1. Ángulos inscritos sobre el mismo arco

Todos los ángulos inscritos que abarcan el **mismo arco** son **iguales**.

### 2. Ángulo inscrito en semicircunferencia

Un ángulo inscrito que abarca un **diámetro** (semicircunferencia = 180°) mide:

$$
\alpha = \frac{180°}{2} = 90°
$$

> **Teorema de Tales:** Todo ángulo inscrito en una semicircunferencia es un ángulo recto.

---

## 📖 Ángulo semi-inscrito

> **Definición:** Un ángulo semi-inscrito tiene su vértice en la circunferencia, un lado es una **cuerda** y el otro es una **tangente**.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Ángulo Semi-inscrito</strong>
  </div>

![Ángulo semi-inscrito](/images/geometria/circulos/angulo-semi-inscrito.svg)

</div>

### Propiedad

El ángulo semi-inscrito mide la **mitad del arco** que determina:

$$
\text{Ángulo semi-inscrito} = \frac{\text{Arco}}{2}
$$

(Igual que el inscrito)

---

## 📖 Ángulo interior (vértice dentro)

> **Definición:** Un ángulo interior tiene su vértice **dentro** de la circunferencia (pero no en el centro).

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 500px;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Ángulo Interior</strong>
  </div>

![Ángulo interior](/images/geometria/circulos/angulo-interior.svg)

</div>

### Propiedad

El ángulo interior mide la **semisuma de los arcos** que abarcan sus lados:

$$
\alpha = \frac{\text{Arco}_1 + \text{Arco}_2}{2}
$$

### Ejemplo

Si los arcos miden 50° y 70°:

$$
\alpha = \frac{50° + 70°}{2} = 60°
$$

---

## 📖 Ángulo exterior (vértice fuera)

> **Definición:** Un ángulo exterior tiene su vértice **fuera** de la circunferencia.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 550px;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Ángulo Exterior</strong>
  </div>

![Ángulo exterior](/images/geometria/circulos/angulo-exterior.svg)

</div>

### Propiedad

El ángulo exterior mide la **semidiferencia de los arcos** que abarcan sus lados:

$$
\alpha = \frac{\text{Arco mayor} - \text{Arco menor}}{2}
$$

### Ejemplo

Si los arcos miden 100° y 40°:

$$
\alpha = \frac{100° - 40°}{2} = 30°
$$

---

## 📖 Tabla resumen

| Tipo de ángulo | Vértice | Fórmula |
|----------------|---------|---------|
| Central | En el centro | = Arco |
| Inscrito | En la circunferencia | = Arco / 2 |
| Semi-inscrito | En la circunferencia | = Arco / 2 |
| Interior | Dentro | = (Arco₁ + Arco₂) / 2 |
| Exterior | Fuera | = (Arco mayor − Arco menor) / 2 |

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Ángulo inscrito

Un arco mide 120°. ¿Cuánto mide el ángulo inscrito que lo abarca?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\alpha = \frac{120°}{2} = 60°
$$

</details>

---

### Ejercicio 2: Encontrar el arco

Un ángulo inscrito mide 35°. ¿Cuánto mide el arco que abarca?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\text{Arco} = 2 \times 35° = 70°
$$

</details>

---

### Ejercicio 3: Ángulo interior

Dos cuerdas se cortan dentro de la circunferencia. Los arcos opuestos miden 80° y 60°. ¿Cuánto mide el ángulo?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\alpha = \frac{80° + 60°}{2} = 70°
$$

</details>

---

### Ejercicio 4: Ángulo exterior

Desde un punto exterior salen dos secantes. Los arcos interceptados miden 110° y 30°. ¿Cuánto mide el ángulo?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
\alpha = \frac{110° - 30°}{2} = 40°
$$

</details>

---

### Ejercicio 5: Teorema de Tales

Un triángulo está inscrito en una circunferencia con la hipotenusa como diámetro. ¿Cuánto mide el ángulo opuesto al diámetro?

<details>
<summary><strong>Ver respuesta</strong></summary>

Por el Teorema de Tales, el ángulo inscrito en una semicircunferencia es **90°**.

</details>

---
