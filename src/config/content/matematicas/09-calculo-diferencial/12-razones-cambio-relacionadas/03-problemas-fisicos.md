---
title: "Problemas Físicos de Razones Relacionadas"
---

# Problemas Físicos de Razones Relacionadas

Los problemas físicos involucran movimiento, fuerzas, circuitos y otros fenómenos donde las cantidades cambian con el tiempo. Las leyes de la física proporcionan las ecuaciones.

---

## 🎯 ¿Qué vas a aprender?

- Problemas de movimiento y distancia
- Aplicaciones con ley de los gases
- Circuitos eléctricos
- Otros fenómenos físicos

---

## ⚙️ Ejemplo 1: Dos autos acercándose

Dos autos viajan hacia una intersección. Uno viene del norte a 60 km/h y está a 0.5 km. El otro viene del este a 80 km/h y está a 0.4 km. ¿A qué razón se acercan?

**Relación:** $d^2 = x^2 + y^2$

**Derivando:**
$$2d\frac{dd}{dt} = 2x\frac{dx}{dt} + 2y\frac{dy}{dt}$$

**Datos:** 
- $x = 0.4$, $\frac{dx}{dt} = -80$ (se acerca)
- $y = 0.5$, $\frac{dy}{dt} = -60$ (se acerca)
- $d = \sqrt{0.16 + 0.25} = \sqrt{0.41}$

$$\frac{dd}{dt} = \frac{x\frac{dx}{dt} + y\frac{dy}{dt}}{d} = \frac{(0.4)(-80) + (0.5)(-60)}{\sqrt{0.41}}$$
$$= \frac{-32 - 30}{\sqrt{0.41}} = \frac{-62}{\sqrt{0.41}} \approx -96.8 \text{ km/h}$$

**Se acercan a 96.8 km/h.**

---

## ⚙️ Ejemplo 2: Ley de Boyle

Para un gas ideal a temperatura constante: $PV = k$ (constante)

Si el volumen de un gas es 600 cm³ a 150 kPa y el volumen disminuye a 20 cm³/min, ¿a qué razón cambia la presión?

**Relación:** $PV = k$

**Derivando:**
$$\frac{dP}{dt} \cdot V + P \cdot \frac{dV}{dt} = 0$$

**Datos:** $V = 600$, $P = 150$, $\frac{dV}{dt} = -20$

$$\frac{dP}{dt}(600) + (150)(-20) = 0$$
$$\frac{dP}{dt} = \frac{3000}{600} = 5 \text{ kPa/min}$$

**La presión aumenta a 5 kPa/min.**

---

## ⚙️ Ejemplo 3: Fuerza gravitacional

La fuerza gravitacional entre dos objetos es $F = \frac{GMm}{r^2}$.

Si un satélite se aleja de la Tierra a 2 km/s cuando está a 10,000 km del centro, ¿a qué razón disminuye la fuerza gravitacional?

**Derivando:**
$$\frac{dF}{dt} = -\frac{2GMm}{r^3}\frac{dr}{dt}$$

Podemos escribir esto como:
$$\frac{dF}{dt} = -\frac{2F}{r}\frac{dr}{dt}$$

Si $F_0$ es la fuerza cuando $r = 10{,}000$ km:
$$\frac{dF}{dt} = -\frac{2F_0}{10{,}000}(2) = -\frac{4F_0}{10{,}000} = -0.0004F_0$$

**La fuerza disminuye a razón de 0.04% por segundo.**

---

## ⚙️ Ejemplo 4: Circuito eléctrico

En un circuito, $V = IR$ (Ley de Ohm). Si la resistencia es constante a 10 Ω y el voltaje aumenta a 2 V/s, ¿a qué razón cambia la corriente?

**Relación:** $I = \frac{V}{R} = \frac{V}{10}$

**Derivando:**
$$\frac{dI}{dt} = \frac{1}{10}\frac{dV}{dt} = \frac{2}{10} = 0.2 \text{ A/s}$$

---

## ⚙️ Ejemplo 5: Barco y muelle

Un barco está atado a un muelle con una cuerda de 12 m. La cuerda se recoge a 1 m/s. ¿Qué tan rápido se acerca el barco cuando está a 5 m del muelle (horizontalmente)?

**Relación:** $c^2 = x^2 + h^2$

donde $c$ = longitud de cuerda, $x$ = distancia horizontal, $h$ = altura del muelle (constante).

Cuando $x = 5$ y el muelle tiene altura $h$:
$12^2 = 5^2 + h^2$ → $h^2 = 119$ (solo para verificar)

En cualquier momento: $c^2 = x^2 + h^2$

**Derivando:**
$$2c\frac{dc}{dt} = 2x\frac{dx}{dt}$$

**Datos:** $\frac{dc}{dt} = -1$ (se recoge), $x = 5$, $c^2 = 25 + 119 = 144$ → $c = 12$

$$12(-1) = 5\frac{dx}{dt}$$
$$\frac{dx}{dt} = -\frac{12}{5} = -2.4 \text{ m/s}$$

**El barco se acerca a 2.4 m/s.**

---

## ⚙️ Ejemplo 6: Faro rotatorio

Un faro gira a 2 revoluciones por minuto. Está a 1 km de la costa (línea recta). ¿A qué velocidad se mueve el haz de luz a lo largo de la costa cuando está a 500 m del punto más cercano?

**Relación:** $x = 1000\tan\theta$ (donde x está en metros)

**Derivando:**
$$\frac{dx}{dt} = 1000\sec^2\theta \cdot \frac{d\theta}{dt}$$

**Datos:** $\frac{d\theta}{dt} = 2(2\pi) = 4\pi$ rad/min

Cuando $x = 500$: $\tan\theta = 0.5$, $\sec^2\theta = 1 + 0.25 = 1.25$

$$\frac{dx}{dt} = 1000(1.25)(4\pi) = 5000\pi \approx 15{,}708 \text{ m/min}$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Dos botes parten del mismo punto. Uno va al norte a 15 km/h y otro al este a 20 km/h. ¿A qué razón se separan después de 2 horas?

<details>
<summary>Ver solución</summary>

Después de 2 horas: $x = 40$ km, $y = 30$ km, $d = 50$ km

$\frac{dd}{dt} = \frac{40(20) + 30(15)}{50} = \frac{800 + 450}{50} = 25$ km/h
</details>

---

**Ejercicio 2:** La potencia en un circuito es $P = I^2R$. Si la corriente aumenta a 0.5 A/s cuando es 3 A, y la resistencia es 4 Ω, ¿a qué razón cambia la potencia?

<details>
<summary>Ver solución</summary>

$\frac{dP}{dt} = 2IR\frac{dI}{dt} = 2(3)(4)(0.5) = 12$ W/s
</details>
