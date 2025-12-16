# Introducción a los Triángulos Oblicuángulos

Los **triángulos oblicuángulos** son aquellos que **no tienen** ángulo recto. Para resolverlos, necesitamos la Ley de Senos y la Ley de Cosenos.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Tipos de triángulos oblicuángulos</strong>
  </div>

![Tipos de triángulos oblicuángulos](/images/trigonometria/triangulos-oblicuangulos/tipos-triangulos.svg)

</div>

---

## 📖 Definición

> **Definición:** Un triángulo oblicuángulo es un triángulo que **no contiene** ningún ángulo de 90°.

### Tipos de triángulos oblicuángulos

| Tipo | Descripción |
|------|-------------|
| Acutángulo | Todos los ángulos son agudos (< 90°) |
| Obtusángulo | Tiene un ángulo obtuso (> 90°) |

---

## 📖 ¿Por qué nuevas herramientas?

Las razones trigonométricas SOH-CAH-TOA solo funcionan con triángulos rectángulos.

Para triángulos oblicuángulos necesitamos:
- **Ley de Senos**
- **Ley de Cosenos**
- **Ley de Tangentes** (opcional)

---

## 📖 Notación estándar

En un triángulo $ABC$:

| Elemento | Símbolo |
|----------|---------|
| Ángulos | $A$, $B$, $C$ |
| Lados opuestos | $a$, $b$, $c$ |

El lado $a$ está **opuesto** al ángulo $A$, y así sucesivamente.

---

## 📖 Propiedad fundamental

En cualquier triángulo:

$$
A + B + C = 180°
$$

Los tres ángulos siempre suman 180°.

---

## 📖 Casos de resolución

Para resolver un triángulo necesitamos **tres datos**, incluyendo al menos un lado.

| Caso | Datos conocidos | Herramienta |
|------|-----------------|-------------|
| ALA | Dos ángulos y un lado | Ley de Senos |
| LAL | Dos lados y el ángulo incluido | Ley de Cosenos |
| LLA | Dos lados y el ángulo opuesto a uno | Ley de Senos (caso ambiguo) |
| LLL | Los tres lados | Ley de Cosenos |

---

## 📖 Resumen de herramientas

### Ley de Senos

$$
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}
$$

Útil cuando conocemos un lado y su ángulo opuesto.

### Ley de Cosenos

$$
c^2 = a^2 + b^2 - 2ab\cos C
$$

Útil cuando conocemos dos lados y el ángulo entre ellos, o los tres lados.

---

## 📖 El caso ambiguo

Cuando conocemos dos lados y un ángulo **no incluido** (LLA), puede haber:
- Ninguna solución
- Una solución
- Dos soluciones

Este es el **caso ambiguo** y requiere análisis cuidadoso.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificar

Clasifica cada triángulo:

1. Ángulos: 60°, 70°, 50°
2. Ángulos: 30°, 60°, 90°
3. Ángulos: 100°, 40°, 40°

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Oblicuángulo acutángulo** - Todos los ángulos < 90°
2. **Rectángulo** - Tiene ángulo de 90°
3. **Oblicuángulo obtusángulo** - Tiene un ángulo > 90°

</details>

---

### Ejercicio 2: Identificar caso

¿Qué caso de resolución es cada problema?

1. $A = 40°$, $B = 60°$, $c = 10$
2. $a = 5$, $b = 7$, $C = 50°$
3. $a = 8$, $b = 6$, $c = 10$

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **ALA** - Dos ángulos y un lado
2. **LAL** - Dos lados y ángulo incluido
3. **LLL** - Los tres lados

</details>

---

### Ejercicio 3: Verdadero o Falso

1. Un triángulo oblicuángulo puede tener dos ángulos rectos.
2. La Ley de Senos solo funciona con triángulos oblicuángulos.
3. Si conocemos dos lados y el ángulo entre ellos, usamos la Ley de Cosenos.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Falso** - Dos ángulos rectos sumarían 180°, sin dejar espacio para el tercero
2. **Falso** - Funciona con cualquier triángulo, pero es especialmente útil para oblicuángulos
3. **Verdadero**

</details>

---
