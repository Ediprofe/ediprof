# Elementos de la Circunferencia

Además del centro, radio y diámetro, la circunferencia tiene otros elementos importantes: cuerdas, arcos, secantes y tangentes.

---

## 📖 Repaso: Elementos básicos

| Elemento | Definición |
|----------|------------|
| Centro ($O$) | Punto equidistante de todos los puntos de la circunferencia |
| Radio ($r$) | Segmento del centro a la circunferencia |
| Diámetro ($d$) | Segmento que pasa por el centro con extremos en la circunferencia |

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0;">
  <div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem;">
    <div style="margin-bottom: 0.5rem;">
      <span style="font-size: 1rem;">📊</span>
      <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Radio</strong>
    </div>

![Radio](/images/geometria/circulos/elemento-radio.svg)

  </div>
  <div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem;">
    <div style="margin-bottom: 0.5rem;">
      <span style="font-size: 1rem;">📊</span>
      <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Diámetro</strong>
    </div>

![Diámetro](/images/geometria/circulos/elemento-diametro.svg)

  </div>
</div>

---

## 📖 Cuerda

> **Definición:** Una cuerda es un segmento cuyos **extremos están en la circunferencia**.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Cuerda</strong>
  </div>

![Cuerda](/images/geometria/circulos/elemento-cuerda.svg)

</div>

### Propiedades

- El diámetro es la **cuerda más larga** posible
- Cuerdas iguales están a igual distancia del centro
- La perpendicular desde el centro a una cuerda la **biseca** (divide en dos partes iguales)

### Ejemplo

Si una cuerda $\overline{AB}$ está a 3 cm del centro y el radio es 5 cm, la longitud de la cuerda es:

$$
\text{Mitad de cuerda} = \sqrt{5^2 - 3^2} = \sqrt{16} = 4 \text{ cm}
$$

$$
\text{Cuerda} = 2 \times 4 = 8 \text{ cm}
$$

---

## 📖 Arco

> **Definición:** Un arco es una **porción de la circunferencia** comprendida entre dos puntos.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Arco</strong>
  </div>

![Arco](/images/geometria/circulos/elemento-arco.svg)

</div>

### Notación

El arco entre los puntos $A$ y $B$ se escribe:

$$
\overset{\frown}{AB}
$$

### Tipos de arcos

Si una cuerda divide la circunferencia en dos partes:

| Arco | Descripción |
|------|-------------|
| Arco menor | El más pequeño (< semicircunferencia) |
| Arco mayor | El más grande (> semicircunferencia) |
| Semicircunferencia | Exactamente la mitad (= 180°) |

---

## 📖 Secante

> **Definición:** Una secante es una **recta que corta** a la circunferencia en **dos puntos**.

### Propiedades

- Toda cuerda es parte de una recta secante
- La secante divide al círculo en dos regiones

---

## 📖 Tangente

> **Definición:** Una tangente es una **recta que toca** a la circunferencia en **exactamente un punto**.

Ese punto único se llama **punto de tangencia**.

### Propiedades

1. La tangente es **perpendicular** al radio en el punto de tangencia
2. Desde un punto exterior se pueden trazar **dos tangentes**
3. Los segmentos de tangente desde un punto exterior son **iguales**

### Ejemplo

Si dos tangentes desde el punto $P$ tocan la circunferencia en $A$ y $B$:

$$
\overline{PA} = \overline{PB}
$$

---

## 📖 Sector circular

> **Definición:** Un sector circular es la región del círculo limitada por **dos radios y un arco**.

Es como una "rebanada de pizza".

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Sector Circular</strong>
  </div>

![Sector circular](/images/geometria/circulos/elemento-sector.svg)

</div>

### Área del sector

Si el ángulo central es $\theta$ (en grados):

$$
A_{sector} = \frac{\theta}{360°} \times \pi r^2
$$

---

## 📖 Segmento circular

> **Definición:** Un segmento circular es la región limitada por **una cuerda y su arco**.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Segmento Circular</strong>
  </div>

![Segmento circular](/images/geometria/circulos/elemento-segmento.svg)

</div>

### Área del segmento

$$
A_{segmento} = A_{sector} - A_{triángulo}
$$

---

## 📖 Corona circular

> **Definición:** Una corona circular es la región entre **dos circunferencias concéntricas** (mismo centro, radios diferentes).

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem auto; max-width: 450px;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Corona Circular</strong>
  </div>

![Corona circular](/images/geometria/circulos/elemento-corona.svg)

</div>

### Área de la corona

$$
A_{corona} = \pi R^2 - \pi r^2 = \pi(R^2 - r^2)
$$

Donde $R$ es el radio mayor y $r$ el radio menor.

---

## 📝 Ejercicios de práctica

### Ejercicio 1: Clasificar elementos

Indica qué elemento es cada uno:

1. Segmento que une dos puntos de la circunferencia
2. Recta que toca la circunferencia en un solo punto
3. Porción de la circunferencia entre dos puntos
4. Recta que corta la circunferencia en dos puntos

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Cuerda**
2. **Tangente**
3. **Arco**
4. **Secante**

</details>

---

### Ejercicio 2: Cuerda

Una cuerda está a 4 cm del centro de una circunferencia de radio 5 cm. ¿Cuánto mide la cuerda?

<details>
<summary><strong>Ver respuesta</strong></summary>

Usando Pitágoras:
$$
\text{Mitad de cuerda} = \sqrt{5^2 - 4^2} = \sqrt{9} = 3 \text{ cm}
$$

$$
\text{Cuerda} = 2 \times 3 = 6 \text{ cm}
$$

</details>

---

### Ejercicio 3: Corona circular

Una corona circular tiene radio exterior de 10 cm y radio interior de 6 cm. Calcula su área.

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
A = \pi(10^2 - 6^2) = \pi(100 - 36) = 64\pi \approx 201.1 \text{ cm}^2
$$

</details>

---

### Ejercicio 4: Verdadero o Falso

1. El diámetro es la cuerda más larga de la circunferencia.
2. Una tangente corta la circunferencia en dos puntos.
3. La tangente es perpendicular al radio en el punto de tangencia.
4. Un arco es un segmento de recta.

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **Verdadero**
2. **Falso** - La tangente toca en exactamente un punto
3. **Verdadero**
4. **Falso** - Un arco es una porción de la circunferencia (curva)

</details>

---
