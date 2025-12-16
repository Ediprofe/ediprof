# Optimización de Áreas y Volúmenes

Los problemas de optimización de áreas y volúmenes son clásicos en cálculo. Combinan geometría con derivadas para encontrar las dimensiones óptimas.

---

## 🎯 ¿Qué vas a aprender?

- Maximizar áreas con perímetro fijo
- Minimizar perímetro con área fija
- Optimizar volúmenes de sólidos
- Problemas con restricciones geométricas

---

## ⚙️ Ejemplo 1: Rectángulo de área máxima

Una ventana rectangular tiene perímetro de 12 metros. ¿Cuáles dimensiones maximizan el área?

**Restricción:** $2x + 2y = 12$ → $y = 6 - x$

**Área:** $A = xy = x(6-x) = 6x - x^2$

**Dominio:** $0 < x < 6$

$$A'(x) = 6 - 2x = 0 \Rightarrow x = 3$$

$$A''(3) = -2 < 0$$ → Máximo

**Dimensiones óptimas:** $3 \times 3$ metros (cuadrado)

**Área máxima:** 9 m²

---

## ⚙️ Ejemplo 2: Cerca con un lado dado

Una cerca rectangular debe encerrar 800 m². Un lado es un muro existente. ¿Qué dimensiones minimizan la cerca necesaria?

**Sea $x$ los lados perpendiculares al muro, $y$ el paralelo.**

**Restricción:** $xy = 800$ → $y = \frac{800}{x}$

**Cerca:** $L = 2x + y = 2x + \frac{800}{x}$

$$L'(x) = 2 - \frac{800}{x^2} = 0$$
$$x^2 = 400 \Rightarrow x = 20$$

$$y = \frac{800}{20} = 40$$

**Dimensiones:** 20 m × 40 m

**Cerca mínima:** $2(20) + 40 = 80$ metros

---

## ⚙️ Ejemplo 3: Caja sin tapa

De una lámina cuadrada de 60 cm de lado se cortan cuadrados en las esquinas para formar una caja sin tapa. ¿Qué altura maximiza el volumen?

**Sea $x$ el lado del cuadrado cortado (altura de la caja).**

**Base:** $(60 - 2x) \times (60 - 2x)$

**Volumen:**
$$V = x(60-2x)^2$$

**Dominio:** $0 < x < 30$

$$V' = (60-2x)^2 + x \cdot 2(60-2x)(-2)$$
$$= (60-2x)[(60-2x) - 4x]$$
$$= (60-2x)(60-6x)$$

$$V' = 0$$ cuando $x = 30$ (borde) o $x = 10$

**Altura óptima:** $x = 10$ cm

**Volumen máximo:** $V = 10 \cdot 40^2 = 16{,}000$ cm³

---

## ⚙️ Ejemplo 4: Cilindro inscrito en esfera

Un cilindro está inscrito en una esfera de radio $R$. ¿Qué dimensiones maximizan el volumen del cilindro?

**Relación geométrica:** Si $r$ es el radio y $h$ la altura del cilindro:
$$r^2 + \left(\frac{h}{2}\right)^2 = R^2$$

**Despejamos:** $r^2 = R^2 - \frac{h^2}{4}$

**Volumen:**
$$V = \pi r^2 h = \pi\left(R^2 - \frac{h^2}{4}\right)h = \pi R^2 h - \frac{\pi h^3}{4}$$

$$V' = \pi R^2 - \frac{3\pi h^2}{4} = 0$$

$$h^2 = \frac{4R^2}{3} \Rightarrow h = \frac{2R}{\sqrt{3}} = \frac{2R\sqrt{3}}{3}$$

$$r^2 = R^2 - \frac{R^2}{3} = \frac{2R^2}{3} \Rightarrow r = R\sqrt{\frac{2}{3}}$$

---

## ⚙️ Ejemplo 5: Lata cilíndrica

Una lata cilíndrica debe tener volumen de 1000 cm³. ¿Qué dimensiones minimizan el material (superficie total)?

**Volumen:** $V = \pi r^2 h = 1000$ → $h = \frac{1000}{\pi r^2}$

**Superficie:**
$$S = 2\pi r^2 + 2\pi r h = 2\pi r^2 + 2\pi r \cdot \frac{1000}{\pi r^2}$$
$$= 2\pi r^2 + \frac{2000}{r}$$

$$S' = 4\pi r - \frac{2000}{r^2} = 0$$

$$r^3 = \frac{500}{\pi} \Rightarrow r = \sqrt[3]{\frac{500}{\pi}} \approx 5.42 \text{ cm}$$

$$h = \frac{1000}{\pi r^2} \approx 10.84 \text{ cm}$$

**Nota:** $h = 2r$ (el diámetro iguala la altura)

---

## 📊 Patrones comunes

| Problema | Resultado óptimo |
|----------|------------------|
| Rectángulo de perímetro fijo, área máxima | Cuadrado |
| Cerca con un lado dado, cerca mínima | Lado paralelo = 2 × perpendicular |
| Cilindro de volumen fijo, superficie mínima | $h = 2r$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Un rancho rectangular se divide en dos partes iguales con una cerca interior paralela a un lado. Si hay 600 m de cerca total, ¿cuáles dimensiones maximizan el área?

<details>
<summary>Ver solución</summary>

$2y + 3x = 600$ → $y = \frac{600 - 3x}{2}$

$A = xy = x \cdot \frac{600-3x}{2} = 300x - \frac{3x^2}{2}$

$A' = 300 - 3x = 0$ → $x = 100$

$y = 150$

**Dimensiones:** 100 m × 150 m
</details>

---

**Ejercicio 2:** Un cono tiene volumen de 100π cm³. ¿Qué dimensiones minimizan la superficie lateral?

<details>
<summary>Ver solución</summary>

$V = \frac{1}{3}\pi r^2 h = 100\pi$ → $h = \frac{300}{r^2}$

$S_L = \pi r \sqrt{r^2 + h^2}$ 

Minimizar $S_L^2 = \pi^2 r^2(r^2 + h^2)$...

Resultado: $h = r\sqrt{2}$
</details>
