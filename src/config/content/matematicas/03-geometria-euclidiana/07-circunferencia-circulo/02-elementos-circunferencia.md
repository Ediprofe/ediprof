---
title: "Elementos de la Circunferencia"
---

# **Elementos de la Circunferencia**

Una circunferencia es mucho más que un simple centro y un radio. Tiene una anatomía propia con cuerdas, líneas que la cortan, y regiones que se forman dentro de ella. Conocer estos elementos es clave para resolver problemas de ingeniería y diseño.

---

## 🎯 ¿Qué vas a aprender?

- Diferenciar entre recta secante, tangente y exterior.
- Identificar cuerdas, arcos y saetas.
- Calcular el área de sectores circulares (rebanadas de pizza) y coronas (anillos).
- Entender propiedades clave de las tangentes.

---

## 📏 Líneas en la Circunferencia

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1.5rem 0;">
  <div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem;">
    <div style="margin-bottom: 0.5rem;">
      <span style="font-size: 1rem;">📊</span>
      <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Radio</strong>
    </div>
    <img src="/images/geometria/circulos/elemento-radio.svg" alt="Radio" style="width: 100%; height: auto;">
  </div>
  <div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem;">
    <div style="margin-bottom: 0.5rem;">
      <span style="font-size: 1rem;">📊</span>
      <strong style="color: #1e293b; font-size: 0.9rem; margin-left: 0.3rem;">Diámetro</strong>
    </div>
    <img src="/images/geometria/circulos/elemento-diametro.svg" alt="Diámetro" style="width: 100%; height: auto;">
  </div>
</div>

### 1. Cuerda
Es cualquier segmento de recta que une **dos puntos** de la circunferencia sin pasar necesariamente por el centro.
*   **Dato Curioso:** El diámetro es la cuerda más larga posible.

<div style="width: 100%; margin-bottom: 20px;">
  <img src="/images/geometria/circulos/elemento-cuerda.svg" alt="Cuerda que une dos puntos" style="width: 100%; height: auto;">
</div>

### 2. Arco ($\frown$)
Es un trozo de la propia circunferencia. Es la parte curva que queda entre dos puntos.

<div style="width: 100%; margin-bottom: 20px;">
  <img src="/images/geometria/circulos/elemento-arco.svg" alt="Arco de circunferencia" style="width: 100%; height: auto;">
</div>

---

## 📐 Rectas y la Circunferencia

### 1. Recta Secante
Es una línea infinita que **corta** a la circunferencia en dos puntos. (Como una brocheta atravesando una aceituna).

### 2. Recta Tangente
Es una línea que **toca** a la circunferencia en un único punto y no la atraviesa.
> **Propiedad de Oro:** El radio que va al punto de tangencia es **siempre perpendicular** ($90^\circ$) a la recta tangente.

---

## 🍕 Regiones del Círculo

### Sector Circular
Es la región comprendida entre dos radios y un arco.
*   *Analogía:* Una rebanada de pizza o de pastel.

<div style="width: 100%; margin-bottom: 20px;">
  <img src="/images/geometria/circulos/elemento-sector.svg" alt="Sector Circular" style="width: 100%; height: auto;">
</div>

**Fórmula de Área:**
Depende del ángulo central $\alpha$:

$$
A = \frac{\pi r^2 \cdot \alpha}{360^\circ}
$$

### Segmento Circular
Es la región entre una **cuerda** y su arco correspondiente.
*   *Analogía:* La parte de la pizza que queda si le cortas el borde recto con un cuchillo (sin llegar al centro).

<div style="width: 100%; margin-bottom: 20px;">
  <img src="/images/geometria/circulos/elemento-segmento.svg" alt="Segmento Circular" style="width: 100%; height: auto;">
</div>

### Corona Circular
Es la región entre dos circunferencias concéntricas (mismo centro).
*   *Analogía:* Una dona o una arandela.

<div style="width: 100%; margin-bottom: 20px;">
  <img src="/images/geometria/circulos/elemento-corona.svg" alt="Corona Circular" style="width: 100%; height: auto;">
</div>

**Fórmula de Área:**
Restas el círculo pequeño ($r$) del grande ($R$):

$$
A = \pi(R^2 - r^2)
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Cálculo de Cuerda

A una distancia de 3 cm del centro de una circunferencia de radio 5 cm, se traza una cuerda. ¿Cuánto mide?

**Razonamiento:**
Se forma un triángulo rectángulo donde la hipotenusa es el radio (5) y un cateto es la distancia al centro (3).
El otro cateto es la mitad de la cuerda ($x$).

$$
x = \sqrt{5^2 - 3^2} = \sqrt{25 - 9} = \sqrt{16} = 4
$$

La mitad mide 4. La cuerda completa mide el doble.

$$
L = 2 \cdot 4
$$

**Resultado:**
$$
\boxed{8 \text{ cm}}
$$

### Ejemplo 2: Área de una Corona

Calcula el área de una arandela con radio interior 2 cm y radio exterior 4 cm.

**Razonamiento:**
$$
A = \pi(4^2 - 2^2)
$$
$$
A = \pi(16 - 4)
$$
$$
A = 12\pi
$$

**Resultado:**
$$
\boxed{12\pi \approx 37.7 \text{ cm}^2}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica: Línea que toca la circunferencia en UN solo punto.

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Tangente}
$$

</details>

### Ejercicio 2
Calcula el área de un sector circular de $90^\circ$ en un círculo de radio 10.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$90^\circ$ es la cuarta parte de $360^\circ$.
$$
A = \frac{\pi \cdot 10^2}{4} = \frac{100\pi}{4}
$$

**Resultado:**
$$
\boxed{25\pi}
$$

</details>

### Ejercicio 3
Una cuerda de 16 cm está a 6 cm del centro. ¿Cuál es el radio de la circunferencia?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Mitad de cuerda = 8 cm. Distancia = 6 cm.
Triángulo rectángulo (6, 8, $r$).
$$
r = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100}
$$

**Resultado:**
$$
\boxed{10 \text{ cm}}
$$

</details>

### Ejercicio 4
¿Qué ángulo forma una recta tangente con el radio en el punto de contacto?

<details>
<summary>Ver solución</summary>

**Resultado:**
$$
\boxed{90^\circ \text{ (Perpendicular)}}
$$

</details>

### Ejercicio 5
Calcula el área de una corona circular formada por círculos de radio 3 y 5.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
A = \pi(5^2 - 3^2) = \pi(25 - 9)
$$

**Resultado:**
$$
\boxed{16\pi}
$$

</details>

### Ejercicio 6
Verdadero o Falso: El diámetro es una cuerda.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cumple la definición (une dos puntos de la circunferencia). Es la cuerda máxima.

**Resultado:**
$$
\boxed{\text{Verdadero}}
$$

</details>

### Ejercicio 7
Si un sector circular abarca $180^\circ$, ¿cómo se llama esa región comúnmente?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Semicírculo}
$$

</details>

### Ejercicio 8
Desde un punto exterior, ¿cuántas tangentes se pueden trazar a una circunferencia?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Se pueden trazar dos líneas que "rocen" la circunferencia, una por "arriba" y otra por "abajo".

**Resultado:**
$$
\boxed{2}
$$

</details>

### Ejercicio 9
Calcula la longitud del arco correspondiente a un ángulo de $60^\circ$ y radio 6.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$60^\circ$ es la sexta parte de $360^\circ$.
Longitud total = $2\pi(6) = 12\pi$.
Arco = $12\pi / 6$.

**Resultado:**
$$
\boxed{2\pi}
$$

</details>

### Ejercicio 10
Nombra la región limitada por una cuerda y un arco.

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Segmento Circular}
$$

</details>

---

## 🔑 Resumen

| Elemento | Tipo | Descripción clave |
| :--- | :--- | :--- |
| **Cuerda** | Línea | Une dos puntos (ej. Diámetro). |
| **Secante** | Recta | Atraviesa y sale (2 puntos). |
| **Tangente** | Recta | Solo toca y sigue (1 punto). |
| **Sector** | Región | "Rebanada de pizza". |
| **Corona** | Región | "Dona" (entre dos círculos). |

> Recuerda: La tangente es "tímida", solo toca un punto. La secante es "atrevida", cruza sin miedo.
