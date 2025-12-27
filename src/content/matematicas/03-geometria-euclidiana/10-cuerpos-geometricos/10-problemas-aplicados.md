# **Problemas Aplicados de Cuerpos Geométricos**

Aquí es donde todo cobra sentido. ¿Cuánto helado cabe en un cono? ¿Qué volumen tiene un silo? Vamos a resolver problemas del mundo real combinando todo lo que hemos aprendido.

---

## 🎯 ¿Qué vas a aprender?

- Combinar cuerpos (cilindro + cono, cubo + pirámide) para resolver problemas complejos.
- Calcular volúmenes de objetos cotidianos (latas, pelotas, silos).
- Realizar conversiones de unidades (metros cúbicos a litros).
- Calcular costes basados en volumen o superficie.

---

## 🧩 Estrategia de Resolución

1.  **Divide y Vencerás:** Descompón el objeto complejo en cuerpos simples (cilindros, conos, etc.).
2.  **Identifica la Pregunta:** ¿Te piden "cuánto cabe" (Volumen) o "cuánto material" (Superficie)?
3.  **Unifica Unidades:** Asegúrate de que todo esté en cm o m antes de calcular. 
    *   Recuerda: $1 \text{ m}^3 = 1000 \text{ Litros}$.

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: El Silo de Grano

Un silo está formado por un cilindro de 10 m de alto y un techo cónico de 3 m de alto. El radio es 4 m. ¿Cuál es su volumen total?

**Razonamiento:**
*   **Cilindro:** $V_c = \pi r^2 h = \pi(16)(10) = 160\pi$.
*   **Cono:** $V_{cono} = \frac{\pi r^2 h}{3} = \frac{\pi(16)(3)}{3} = 16\pi$.
*   **Total:** $160\pi + 16\pi = 176\pi$.

**Resultado:**
$$
\boxed{176\pi \approx 552.9 \text{ m}^3}
$$

### Ejemplo 2: Pelotas en un Tubo

Tres pelotas de tenis (radio $r$) se venden en un tubo cilíndrico que las contiene exactamente. ¿Qué fracción del volumen del tubo está ocupada por las pelotas?

**Razonamiento:**
*   **Altura Tubo:** $h = 6r$ (tres diámetros). Base Tubo: $\pi r^2$.
    *   $V_{tubo} = \pi r^2 (6r) = 6\pi r^3$.
*   **Volumen Pelotas (3):**
    *   $3 \times (\frac{4}{3}\pi r^3) = 4\pi r^3$.
*   **Fracción:** $\frac{4\pi r^3}{6\pi r^3} = \frac{4}{6} = \frac{2}{3}$.

**Resultado:**
$$
\boxed{\text{Ocupan } \frac{2}{3} \text{ del volumen (66.6\%)}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Volumen de una casa de perro: Cubo de lado 1 m + techo piramidal de 0.5 m de alto.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cubo: $1^3 = 1$. Pirámide: $\frac{1 \cdot 0.5}{3} = 0.166$.
Total: $1.166$.

**Resultado:**
$$
\boxed{\approx 1.17 \text{ m}^3}
$$

</details>

### Ejercicio 2
Un camión cisterna cilíndrico mide 10 m de largo y tiene un diámetro de 2 m. ¿Cuántos litros carga? ($r=1$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$V = \pi(1)^2(10) = 10\pi$ m³.
$10\pi \approx 31.41$ m³.
En litros ($\times 1000$): 31,416 L.

**Resultado:**
$$
\boxed{\approx 31,416 \text{ Litros}}
$$

</details>

### Ejercicio 3
Una bola de helado ($r=3$ cm) se derrite dentro de un cono ($r=3$ cm, $h=10$ cm). ¿Se rebalsará?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Bola: $\frac{4}{3}\pi(27) = 36\pi$.
Cono: $\frac{\pi(9)(10)}{3} = 30\pi$.
La bola ($36\pi$) es mayor que el cono ($30\pi$).

**Resultado:**
$$
\boxed{\text{Sí, se rebalsará}}
$$

</details>

### Ejercicio 4
Cubo de plomo de 10 cm se funde para hacer esferas de 1 cm de radio. ¿Cuántas salen?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cubo: $1000$ cm³.
Esfera: $\frac{4}{3}\pi(1) \approx 4.19$ cm³.
$1000 / 4.19 \approx 238$.

**Resultado:**
$$
\boxed{\approx 238 \text{ esferas}}
$$

</details>

### Ejercicio 5
Coste de pintar una cúpula semiesférica de radio 5 m a 10€ el m².

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Área: $2\pi(25) = 50\pi \approx 157$ m².
Coste: $157 \times 10$.

**Resultado:**
$$
\boxed{\approx 1,570 \text{ euros}}
$$

</details>

### Ejercicio 6
Volumen de un lápiz cilíndrico ($r=0.5, h=10$) con punta cónica ($h=2$).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cilindro: $\pi(0.25)(10) = 2.5\pi$.
Cono: $\frac{\pi(0.25)(2)}{3} \approx 0.16\pi$.
Total: $2.66\pi$.

**Resultado:**
$$
\boxed{2.66\pi \approx 8.35 \text{ cm}^3}
$$

</details>

### Ejercicio 7
Un cubo de hielo de 4 cm se mete en un vaso cilíndrico de radio 4 cm. Al derretirse, ¿qué altura sube el agua?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Vol. Hielo: $64$.
En el cilindro: $64 = \pi(16)h \Rightarrow 4 = \pi h \Rightarrow h = 4/\pi$.

**Resultado:**
$$
\boxed{\approx 1.27 \text{ cm}}
$$

</details>

### Ejercicio 8
Área de etiqueta de una lata de tomate ($d=10$ cm, $h=10$ cm). ¿Es cuadrada?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Base rectángulo: $2\pi(5) = 10\pi \approx 31.4$ cm. Altura: $10$ cm.
Es rectangular ($31.4 \times 10$).

**Resultado:**
$$
\boxed{\text{No, es rectangular. Area } \approx 314 \text{ cm}^2}
$$

</details>

### Ejercicio 9
Diferencia de volumen entre una naranja ($d=10$) y su piel si la piel tiene 0.5 cm de grosor.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Esfera grande ($r=5$), esfera chica ($r=4.5$).
$V_{piel} = \frac{4}{3}\pi (5^3 - 4.5^3) = \frac{4}{3}\pi (125 - 91.125)$.

**Resultado:**
$$
\boxed{\approx 141.9 \text{ cm}^3}
$$

</details>

### Ejercicio 10
Si construyes una pirámide con 1 m³ de arena y base cuadrada de 2 m de lado, ¿qué altura alcanzará?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$1 = \frac{(2 \times 2) \cdot h}{3} \Rightarrow 1 = \frac{4h}{3} \Rightarrow 3 = 4h$.

**Resultado:**
$$
\boxed{0.75 \text{ m}}
$$

</details>

---

## 🔑 Resumen

| Objeto | Estrategia |
| :--- | :--- |
| **Silo / Cohete** | Cilindro + Cono |
| **Cápsula** | Cilindro + 2 Semiesferas |
| **Helado** | Cono + Semiesfera |

> Trata cada parte por separado y suma (o resta) al final. ¡Cuidado con las unidades!
