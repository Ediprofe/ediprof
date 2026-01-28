---
title: "Presión Osmótica"
---

# Presión Osmótica

La **presión osmótica** es la presión necesaria para detener el flujo de solvente a través de una membrana semipermeable. Es fundamental en biología y medicina.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la ósmosis y la presión osmótica
- La fórmula π = iMRT
- Aplicaciones biológicas y médicas
- Cálculos con ejemplos

---

## 📊 La Fórmula

$$
\boxed{\pi = i \times M \times R \times T}
$$

| Variable | Significado | Unidades |
|----------|-------------|----------|
| π | Presión osmótica | atm |
| i | Factor de Van't Hoff | (adimensional) |
| M | Molaridad | mol/L |
| R | Constante de gases | 0.0821 L·atm/(mol·K) |
| T | Temperatura | K |

---

## 📖 ¿Qué es la Ósmosis?

> La **ósmosis** es el movimiento de solvente a través de una **membrana semipermeable** desde una solución diluida hacia una más concentrada.

### 💡 Membrana semipermeable:

- Permite pasar el **solvente** (moléculas pequeñas)
- Bloquea el **soluto** (moléculas grandes o iones)
- Ejemplos: membrana celular, membranas de diálisis

---

## 📖 El Fenómeno

```
    Solución           Solvente
    concentrada         puro
    ┌─────┐           ┌─────┐
    │●●●●●│ ← H₂O ←   │     │
    │●●●●●│           │     │
    │●●●●●│ membrana  │     │
    └──┬──┘           └─────┘
       │
       ↓
    El agua fluye hacia la solución concentrada
    para "diluirla"
```

### 💡 Presión osmótica (π):

Es la **presión** que hay que aplicar a la solución concentrada para **detener** el flujo de solvente.

---

## 📖 Ejemplo 1: Cálculo Directo

### Problema:
Calcular la presión osmótica de una solución de glucosa 0.1 M a 25°C.

### Solución:

**Datos:**
- i = 1 (glucosa no se disocia)
- M = 0.1 mol/L
- T = 298 K
- R = 0.0821 L·atm/(mol·K)

**Cálculo:**
$$
\pi = 1 \times 0.1 \times 0.0821 \times 298 = \boxed{2.45 \text{ atm}}
$$

---

## 📖 Ejemplo 2: Con Electrolito

### Problema:
¿Cuál es la presión osmótica de NaCl 0.15 M a 37°C (temperatura corporal)?

### Solución:

$$
\pi = 2 \times 0.15 \times 0.0821 \times 310 = \boxed{7.65 \text{ atm}}
$$

---

## 📖 Ejemplo 3: Determinar Masa Molar

### Problema:
Una solución de 3 g de proteína en 100 mL tiene π = 0.06 atm a 27°C. ¿Cuál es la masa molar?

### Solución:

**Paso 1:** Despejar M
$$
M = \frac{\pi}{iRT} = \frac{0.06}{1 \times 0.0821 \times 300} = 0.00244 \text{ mol/L}
$$

**Paso 2:** Calcular moles en 0.1 L
$$
n = 0.00244 \times 0.1 = 0.000244 \text{ mol}
$$

**Paso 3:** Masa molar
$$
M_m = \frac{3}{0.000244} = \boxed{12,300 \text{ g/mol}}
$$

(Valor típico para proteínas pequeñas)

---

## 📖 Tipos de Soluciones

| Tipo | Comparación | Efecto en célula |
|------|-------------|------------------|
| **Isotónica** | π igual al interior | Célula normal |
| **Hipotónica** | π menor que interior | Célula se hincha |
| **Hipertónica** | π mayor que interior | Célula se encoge |

---

## 📖 Aplicaciones

### 💡 Suero fisiológico (0.9% NaCl):

Es **isotónico** con la sangre. No causa daño a las células.

### 💡 Conservación de alimentos:

Las salmueras concentradas deshidratan bacterias por ósmosis.

### 💡 Diálisis renal:

Usa membrana semipermeable para eliminar toxinas de la sangre.

### 💡 Ósmosis inversa:

Aplicando presión mayor que π, se puede purificar agua (desalinización).

### 💡 Plantas:

La presión osmótica mantiene las células turgentes.

---

## 📖 Ventajas de Medir π

### 💡 Para determinar masas molares:

- La presión osmótica es **muy sensible**
- Útil para **moléculas grandes** (proteínas, polímeros)
- Pequeñas concentraciones dan presiones medibles

$$
\pi = 0.06 \text{ atm para proteína diluida (medible)}
$$

$$
\Delta T_f = 0.00002°C \text{ (imposible de medir)}
$$

---

## 🔑 Resumen

$$
\pi = i \times M \times R \times T
$$

| Tipo de solución | Comparación con célula |
|------------------|------------------------|
| Isotónica | π igual |
| Hipotónica | π menor |
| Hipertónica | π mayor |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
¿Cuál es π para sacarosa 0.5 M a 20°C?

<details>
<summary>Ver solución</summary>

$$
\pi = 1 \times 0.5 \times 0.0821 \times 293 = \boxed{12.0 \text{ atm}}
$$

</details>

### Ejercicio 2
La sangre tiene π ≈ 7.7 atm a 37°C. Si solo NaCl contribuyera, ¿cuál sería su molaridad?

<details>
<summary>Ver solución</summary>

$$
M = \frac{\pi}{iRT} = \frac{7.7}{2 \times 0.0821 \times 310} = \boxed{0.15 \text{ M}}
$$

</details>

### Ejercicio 3
¿Qué pasa si inyectas agua destilada (π = 0) en la sangre?

<details>
<summary>Ver solución</summary>

El agua destilada es **hipotónica** respecto a las células sanguíneas.

Proceso:
1. El agua entra a los glóbulos rojos por ósmosis
2. Los glóbulos se **hinchan**
3. Pueden **reventar** (hemólisis)
4. Esto es **peligroso**

Por eso se usa suero fisiológico (0.9% NaCl) que es isotónico.

</details>

### Ejercicio 4
¿Por qué la ósmosis inversa puede desalinizar agua de mar?

<details>
<summary>Ver solución</summary>

El agua de mar tiene aproximadamente:
- 3.5% sal ≈ 0.6 M NaCl
- π ≈ 2 × 0.6 × 0.0821 × 298 ≈ 29 atm

Si aplicamos **presión mayor que 29 atm** al agua de mar:

1. El agua se ve "forzada" a atravesar la membrana
2. La sal se queda atrás (no pasa)
3. Se obtiene agua pura del otro lado

Se llama "inversa" porque invierte el flujo natural de la ósmosis.

</details>
