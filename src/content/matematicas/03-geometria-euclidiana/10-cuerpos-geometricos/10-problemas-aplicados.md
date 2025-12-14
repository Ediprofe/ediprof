# Problemas Aplicados de Cuerpos Geométricos

En esta lección resolvemos problemas que combinan diferentes cuerpos geométricos y aplican los conceptos aprendidos a situaciones del mundo real.

---

## 📖 Estrategia general para problemas

1. **Identificar** los cuerpos geométricos involucrados
2. **Extraer** los datos del problema
3. **Seleccionar** las fórmulas apropiadas
4. **Calcular** paso a paso
5. **Verificar** que la respuesta tenga sentido

---

## 📖 Problema 1: Tanque cilíndrico

Un tanque cilíndrico tiene diámetro 2 m y altura 3 m. ¿Cuántos litros de agua puede contener?

### Solución

Radio: $r = 1$ m

$$
V = \pi r^2 h = \pi(1)^2(3) = 3\pi \approx 9.42 \text{ m}^3
$$

Conversión: $1 \text{ m}^3 = 1000 \text{ L}$

$$
V = 9420 \text{ litros}
$$

---

## 📖 Problema 2: Helado en cono

Un cono de helado tiene radio 3 cm y altura 10 cm. Encima tiene una semiesfera de helado del mismo radio. ¿Cuál es el volumen total de helado?

### Solución

**Volumen del cono:**

$$
V_{cono} = \frac{\pi(9)(10)}{3} = 30\pi \text{ cm}^3
$$

**Volumen de la semiesfera:**

$$
V_{semiesfera} = \frac{1}{2} \times \frac{4}{3}\pi(27) = 18\pi \text{ cm}^3
$$

**Total:**

$$
V_{total} = 30\pi + 18\pi = 48\pi \approx 150.8 \text{ cm}^3
$$

---

## 📖 Problema 3: Silo de granos

Un silo tiene forma de cilindro coronado por un hemisferio. El radio es 5 m y la altura del cilindro es 12 m. Calcula su capacidad.

### Solución

**Volumen del cilindro:**

$$
V_{cil} = \pi(25)(12) = 300\pi \text{ m}^3
$$

**Volumen del hemisferio:**

$$
V_{hem} = \frac{2}{3}\pi(125) = \frac{250\pi}{3} \text{ m}^3
$$

**Total:**

$$
V = 300\pi + \frac{250\pi}{3} = \frac{900\pi + 250\pi}{3} = \frac{1150\pi}{3} \approx 1204.28 \text{ m}^3
$$

---

## 📖 Problema 4: Pintura

¿Cuánta pintura se necesita para pintar el exterior de un cilindro de radio 2 m y altura 5 m, incluyendo las tapas? (Asume que 1 litro cubre 10 m²)

### Solución

**Área total:**

$$
A = 2\pi r(h + r) = 2\pi(2)(7) = 28\pi \approx 87.96 \text{ m}^2
$$

**Pintura necesaria:**

$$
\frac{87.96}{10} \approx 8.8 \text{ litros}
$$

---

## 📖 Problema 5: Casa con techo piramidal

Una casa tiene base cuadrada de 10 m de lado y paredes de 3 m. El techo es una pirámide de 4 m de altura. Calcula el volumen total del espacio interior.

### Solución

**Volumen del prisma (paredes):**

$$
V_{prisma} = 100 \times 3 = 300 \text{ m}^3
$$

**Volumen de la pirámide (techo):**

$$
V_{pir} = \frac{100 \times 4}{3} = \frac{400}{3} \approx 133.33 \text{ m}^3
$$

**Total:**

$$
V = 300 + 133.33 = 433.33 \text{ m}^3
$$

---

## 📝 Problemas de práctica

### Problema 1: Lata de refresco

Una lata cilíndrica tiene diámetro 6.6 cm y altura 12.2 cm. Calcula:

1. Su volumen en cm³
2. Su capacidad en ml

<details>
<summary><strong>Ver respuesta</strong></summary>

$r = 3.3$ cm

$$
V = \pi(10.89)(12.2) \approx 417.5 \text{ cm}^3 = 417.5 \text{ ml}
$$

(Aproximadamente una lata de 330 ml tiene un poco menos de altura real)

</details>

---

### Problema 2: Pelota de tenis

Una pelota de tenis tiene diámetro 6.7 cm. Una caja cilíndrica contiene exactamente 3 pelotas apiladas. ¿Cuánto espacio vacío queda en la caja?

<details>
<summary><strong>Ver respuesta</strong></summary>

$r = 3.35$ cm, cada pelota: $V = \frac{4}{3}\pi(3.35)^3 \approx 157.48$ cm³

Caja: $r = 3.35$, $h = 3 \times 6.7 = 20.1$ cm

$$
V_{caja} = \pi(11.22)(20.1) \approx 708.5 \text{ cm}^3
$$

$$
V_{pelotas} = 3 \times 157.48 = 472.44 \text{ cm}^3
$$

$$
V_{vacío} = 708.5 - 472.44 \approx 236 \text{ cm}^3
$$

</details>

---

### Problema 3: Piscina

Una piscina tiene forma de prisma rectangular de 25 m × 10 m × 2 m. ¿Cuántos litros de agua caben?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
V = 25 \times 10 \times 2 = 500 \text{ m}^3 = 500,000 \text{ litros}
$$

</details>

---

### Problema 4: Vela cónica

Una vela cónica tiene radio 4 cm y altura 15 cm. ¿Cuántas velas se pueden hacer con 2 litros de cera? (1 L = 1000 cm³)

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
V_{vela} = \frac{\pi(16)(15)}{3} = 80\pi \approx 251.33 \text{ cm}^3
$$

$$
\text{Velas} = \frac{2000}{251.33} \approx 7.96
$$

Se pueden hacer **7 velas** completas.

</details>

---

### Problema 5: Embudo

Un embudo tiene forma de cono con radio 6 cm y altura 10 cm. Se llena de agua y luego se vierte en un cilindro de radio 3 cm. ¿Hasta qué altura llega el agua?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
V_{cono} = \frac{\pi(36)(10)}{3} = 120\pi \text{ cm}^3
$$

$$
h_{cilindro} = \frac{V}{\pi r^2} = \frac{120\pi}{\pi(9)} = \frac{120}{9} = 13.33 \text{ cm}
$$

</details>

---
