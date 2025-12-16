# Aplicaciones de Ecuaciones Diferenciales

Las ecuaciones diferenciales modelan fenómenos del mundo real: crecimiento poblacional, circuitos, mezclas, movimiento.

---

## 🎯 ¿Qué vas a aprender?

- Crecimiento y decaimiento exponencial
- Ley de enfriamiento de Newton
- Problemas de mezclas
- Movimiento bajo resistencia

---

## 📖 Crecimiento exponencial

$$\frac{dP}{dt} = kP$$

**Solución:** $P(t) = P_0 e^{kt}$

- $k > 0$: crecimiento
- $k < 0$: decaimiento

---

## ⚙️ Ejemplo 1: Población bacteriana

Una colonia de bacterias crece proporcionalmente a su tamaño. Si hay 1000 bacterias inicialmente y 3000 después de 2 horas, ¿cuántas habrá después de 5 horas?

$P = 1000e^{kt}$

$3000 = 1000e^{2k} \Rightarrow k = \frac{\ln 3}{2}$

$P(5) = 1000e^{5k} = 1000 \cdot 3^{5/2} = 1000 \cdot 9\sqrt{3} \approx 15{,}588$

---

## 📖 Decaimiento radiactivo

$$\frac{dN}{dt} = -\lambda N$$

**Vida media:** $t_{1/2} = \frac{\ln 2}{\lambda}$

---

## ⚙️ Ejemplo 2: Carbono-14

El C-14 tiene vida media de 5730 años. Un fósil tiene 20% del C-14 original. ¿Qué edad tiene?

$0.2N_0 = N_0 e^{-\lambda t}$

$\lambda = \frac{\ln 2}{5730}$

$-\lambda t = \ln(0.2)$

$t = \frac{-\ln(0.2)}{\ln 2/5730} = \frac{5730 \ln 5}{\ln 2} \approx 13{,}300$ años

---

## 📖 Ley de enfriamiento de Newton

$$\frac{dT}{dt} = -k(T - T_m)$$

donde $T_m$ es la temperatura del medio.

**Solución:** $T(t) = T_m + (T_0 - T_m)e^{-kt}$

---

## ⚙️ Ejemplo 3: Café enfriándose

Café a 90°C en ambiente de 20°C. Después de 5 min está a 60°C. ¿Cuándo llegará a 30°C?

$T = 20 + 70e^{-kt}$

$60 = 20 + 70e^{-5k}$

$e^{-5k} = \frac{40}{70} = \frac{4}{7}$

$k = \frac{\ln(7/4)}{5}$

$30 = 20 + 70e^{-kt}$

$e^{-kt} = \frac{1}{7}$

$t = \frac{\ln 7}{k} = \frac{5\ln 7}{\ln(7/4)} \approx 17.5$ min

---

## 📖 Problemas de mezclas

$$\frac{dQ}{dt} = \text{(tasa entrada)} - \text{(tasa salida)}$$

---

## ⚙️ Ejemplo 4: Tanque de salmuera

Un tanque de 100 L contiene agua pura. Entra salmuera con 2 kg/L a 5 L/min. La mezcla sale a 5 L/min. ¿Cantidad de sal $Q(t)$?

$\frac{dQ}{dt} = (2)(5) - \frac{Q}{100}(5) = 10 - \frac{Q}{20}$

Es lineal: $Q' + \frac{Q}{20} = 10$

$\mu = e^{t/20}$

$Q = 200 + Ce^{-t/20}$

$Q(0) = 0$: $C = -200$

$$Q(t) = 200(1 - e^{-t/20})$$

---

## 📖 Modelo logístico

$$\frac{dP}{dt} = kP\left(1 - \frac{P}{M}\right)$$

donde $M$ es la capacidad de carga.

**Solución:** $P(t) = \frac{M}{1 + Ae^{-kt}}$

---

## ⚙️ Ejemplo 5: Población con límite

Una isla puede sostener 10,000 habitantes. La población inicial es 2,000 y crece según el modelo logístico con $k = 0.1$/año.

$P = \frac{10000}{1 + Ae^{-0.1t}}$

$P(0) = 2000$: $2000 = \frac{10000}{1+A}$ → $A = 4$

$$P(t) = \frac{10000}{1 + 4e^{-0.1t}}$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Un cuerpo se enfría de 100°C a 60°C en 10 min en ambiente de 20°C. ¿Cuándo llega a 40°C?

<details>
<summary>Ver solución</summary>

$60 = 20 + 80e^{-10k}$ → $e^{-10k} = 1/2$ → $k = \frac{\ln 2}{10}$

$40 = 20 + 80e^{-kt}$ → $e^{-kt} = 1/4$

$t = \frac{\ln 4}{k} = \frac{10 \cdot 2\ln 2}{\ln 2} = 20$ min
</details>

---

**Ejercicio 2:** Una inversión se duplica en 8 años con interés continuo. ¿En cuánto tiempo se triplica?

<details>
<summary>Ver solución</summary>

$2 = e^{8k}$ → $k = \frac{\ln 2}{8}$

$3 = e^{kt}$ → $t = \frac{\ln 3}{k} = \frac{8\ln 3}{\ln 2} \approx 12.7$ años
</details>
