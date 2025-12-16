# Problemas de Contenedores

Los problemas de contenedores son clásicos en optimización: diseñar cajas, latas, tanques con mínimo material o máximo volumen.

---

## 🎯 ¿Qué vas a aprender?

- Optimizar cajas rectangulares
- Diseñar cilindros óptimos
- Contenedores con restricciones
- Estrategias de modelado

---

## ⚙️ Ejemplo 1: Caja con base cuadrada

Diseña una caja abierta (sin tapa) con base cuadrada y volumen de 500 cm³ que use el mínimo material.

**Variables:** $x$ = lado de la base, $h$ = altura

**Restricción:** $V = x^2 h = 500$ → $h = \frac{500}{x^2}$

**Superficie (material):**
$$S = x^2 + 4xh = x^2 + 4x \cdot \frac{500}{x^2} = x^2 + \frac{2000}{x}$$

**Optimización:**
$$S'(x) = 2x - \frac{2000}{x^2} = 0$$
$$2x^3 = 2000$$
$$x^3 = 1000 \Rightarrow x = 10 \text{ cm}$$

$$h = \frac{500}{100} = 5 \text{ cm}$$

**Dimensiones óptimas:** base 10×10 cm, altura 5 cm

---

## ⚙️ Ejemplo 2: Caja cerrada

Una caja rectangular con tapa tiene volumen de 32 m³. La base es cuadrada. Minimiza el material.

**Restricción:** $x^2 h = 32$ → $h = \frac{32}{x^2}$

**Superficie total:**
$$S = 2x^2 + 4xh = 2x^2 + \frac{128}{x}$$

$$S'(x) = 4x - \frac{128}{x^2} = 0$$
$$x^3 = 32 \Rightarrow x = \sqrt[3]{32} \approx 3.17 \text{ m}$$

$$h = \frac{32}{x^2} \approx 3.17 \text{ m}$$

**Resultado:** La caja óptima es un **cubo**.

---

## ⚙️ Ejemplo 3: Cilindro sin tapa

Un tanque cilíndrico abierto debe contener 1000 litros (1 m³). Minimiza el material.

**Restricción:** $V = \pi r^2 h = 1$ → $h = \frac{1}{\pi r^2}$

**Superficie:**
$$S = \pi r^2 + 2\pi r h = \pi r^2 + \frac{2}{r}$$

$$S'(r) = 2\pi r - \frac{2}{r^2} = 0$$
$$r^3 = \frac{1}{\pi}$$
$$r = \sqrt[3]{\frac{1}{\pi}} \approx 0.68 \text{ m}$$

$$h = \frac{1}{\pi r^2} \approx 0.68 \text{ m}$$

**Resultado:** Radio = Altura (para cilindro abierto óptimo)

---

## ⚙️ Ejemplo 4: Cilindro con tapa

Para un cilindro cerrado de volumen $V$ fijo:

$$S = 2\pi r^2 + 2\pi rh$$

Con $\pi r^2 h = V$:

$$S = 2\pi r^2 + \frac{2V}{r}$$

$$S' = 4\pi r - \frac{2V}{r^2} = 0$$

$$r^3 = \frac{V}{2\pi} \Rightarrow r = \sqrt[3]{\frac{V}{2\pi}}$$

Sustituyendo en $h$:

$$h = \frac{V}{\pi r^2} = 2r$$

**Resultado:** La altura es igual al diámetro.

---

## ⚙️ Ejemplo 5: Caja de hoja de aluminio

De una lámina de 50×30 cm se cortan cuadrados de las esquinas para formar una caja. ¿Qué corte maximiza el volumen?

**Sea $x$ el lado del cuadrado cortado.**

**Dimensiones de la caja:** $(50-2x) \times (30-2x) \times x$

**Volumen:**
$$V = x(50-2x)(30-2x) = x(1500 - 100x - 60x + 4x^2)$$
$$= x(1500 - 160x + 4x^2) = 4x^3 - 160x^2 + 1500x$$

**Dominio:** $0 < x < 15$

$$V' = 12x^2 - 320x + 1500 = 0$$
$$3x^2 - 80x + 375 = 0$$

$$x = \frac{80 \pm \sqrt{6400 - 4500}}{6} = \frac{80 \pm \sqrt{1900}}{6}$$

$$x \approx \frac{80 - 43.6}{6} \approx 6.07 \text{ cm}$$

(El otro valor está fuera del dominio)

---

## 📊 Patrones de diseño óptimo

| Contenedor | Condición óptima |
|------------|------------------|
| Caja abierta, base cuadrada | $h = \frac{x}{2}$ |
| Caja cerrada, base cuadrada | Cubo: $h = x$ |
| Cilindro abierto | $h = r$ |
| Cilindro cerrado | $h = 2r$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Una lata cilíndrica abierta debe tener volumen de 250π cm³. Encuentra las dimensiones que minimizan el aluminio.

<details>
<summary>Ver solución</summary>

$\pi r^2 h = 250\pi$ → $h = \frac{250}{r^2}$

$S = \pi r^2 + 2\pi rh = \pi r^2 + \frac{500\pi}{r}$

$S' = 2\pi r - \frac{500\pi}{r^2} = 0$

$r^3 = 250$ → $r = \sqrt[3]{250} \approx 6.3$ cm

$h \approx 6.3$ cm (igual al radio)
</details>

---

**Ejercicio 2:** Un acuario rectangular tiene base cuadrada y capacidad de 500 litros (500,000 cm³). El vidrio del fondo cuesta el doble que el de los lados. Minimiza el costo.

<details>
<summary>Ver solución</summary>

$C = 2x^2 + 4xh$ (fondo cuesta doble)

$x^2 h = 500{,}000$ → $h = \frac{500{,}000}{x^2}$

$C = 2x^2 + \frac{2{,}000{,}000}{x}$

$C' = 4x - \frac{2{,}000{,}000}{x^2} = 0$

$x^3 = 500{,}000$ → $x \approx 79.4$ cm
</details>
