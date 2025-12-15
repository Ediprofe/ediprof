# Comparación: Media, Mediana y Moda

Ya conoces las tres medidas de tendencia central. Ahora es momento de juntarlas, compararlas y aprender a elegir la correcta para cada situación.

---

## 🎯 ¿Qué vas a aprender?

- Cómo se relacionan las tres medidas
- Qué indica cuando coinciden o difieren
- Cómo elegir la mejor medida para cada caso
- Interpretar el sesgo usando la relación entre ellas

---

## 📊 Resumen Comparativo

| Característica | Media | Mediana | Moda |
|----------------|-------|---------|------|
| Cálculo | Suma / n | Valor central | Más frecuente |
| Usa todos los valores | ✅ Sí | ❌ No | ❌ No |
| Sensible a extremos | ✅ Muy | ❌ No | ❌ No |
| Datos cualitativos | ❌ No | ❌ No | ✅ Sí |
| Siempre existe | ✅ Sí | ✅ Sí | ❌ No siempre |
| Valor único | ✅ Sí | ✅ Sí* | ❌ Puede haber varias |

*En datos pares, la mediana puede ser un promedio de dos valores.

---

## 📖 Cuando las Tres Coinciden: Distribución Simétrica

En una distribución **perfectamente simétrica**:

$$
\text{Media} = \text{Mediana} = \text{Moda}
$$

### 💡 Visualización:

```
        Moda
          ▼
      ▄▄█▄▄
    ▄██████▄
  ▄██████████▄
▄██████████████▄
        ▲
    Media = Mediana
```

### ⚙️ Ejemplo: Datos simétricos

Datos: 2, 4, 6, 6, 6, 8, 10

- **Media:** $\frac{2+4+6+6+6+8+10}{7} = \frac{42}{7} = 6$
- **Mediana:** Valor en posición 4 → **6**
- **Moda:** El 6 aparece 3 veces → **6**

Las tres son iguales porque los datos son simétricos alrededor del 6.

---

## 📖 Cuando Difieren: Distribución Sesgada

### 📐 Sesgo a la Derecha (Positivo)

```
█▄
██▄
████▄
██████▄▄▄▄▄
```

**Orden:** Moda < Mediana < Media

La "cola" hacia la derecha jala la media hacia arriba.

### ⚙️ Ejemplo: Ingresos

Datos (en millones): 1, 1, 1, 2, 2, 3, 3, 4, 15

- **Moda:** 1 (aparece 3 veces)
- **Mediana:** 2 (valor en posición 5)
- **Media:** $\frac{32}{9} = 3.56$

**Orden:** 1 < 2 < 3.56 ✓ (sesgo a la derecha)

### 📐 Sesgo a la Izquierda (Negativo)

```
         ▄█
        ▄██
       ▄████
▄▄▄▄▄▄██████
```

**Orden:** Media < Mediana < Moda

La "cola" hacia la izquierda jala la media hacia abajo.

### ⚙️ Ejemplo: Notas de un examen fácil

Datos: 3, 7, 8, 8, 9, 9, 9, 10, 10

- **Media:** $\frac{73}{9} = 8.11$
- **Mediana:** 9 (valor en posición 5)
- **Moda:** 9 (aparece 3 veces)

**Orden:** 8.11 < 9 = 9 ✓ (sesgo a la izquierda)

---

## 💡 Guía Rápida: ¿Cuál Usar?

| Situación | Mejor opción | Razón |
|-----------|--------------|-------|
| Datos simétricos, sin extremos | **Media** | Usa toda la información |
| Hay valores extremos (outliers) | **Mediana** | Resistente a extremos |
| Distribución muy sesgada | **Mediana** | Más representativa |
| Datos cualitativos | **Moda** | Única opción |
| Buscar lo más común | **Moda** | Define lo "típico" |
| Decisiones de inventario | **Moda** | ¿Qué producir más? |
| Planificación financiera | **Mediana** | Ingresos son sesgados |

---

## ⚙️ Ejemplos de Decisión

### Caso 1: Tiempo de espera en un banco

Tiempos (min): 2, 3, 3, 4, 5, 5, 6, 7, 8, 45

- Media: 8.8 minutos (distorsionada por 45)
- Mediana: 5 minutos (mejor representativa)
- Moda: 3 y 5 minutos

**Mejor:** Mediana. El tiempo "típico" es 5 minutos, no 8.8.

### Caso 2: Tallas de uniformes

Tallas pedidas: S, M, M, M, L, L, L, L, XL

- Media: No aplica (dato cualitativo)
- Mediana: L (valor central)
- Moda: L (la más frecuente)

**Mejor:** Moda. Para producción, importa cuál es más demandada.

### Caso 3: Temperaturas del mes

Temperaturas similares entre 18°C y 25°C, sin extremos.

**Mejor:** Media. Datos numéricos, simétricos, sin outliers.

---

## 📖 El Coeficiente de Asimetría (Sesgo)

Una forma de medir el sesgo numéricamente:

### 💡 Coeficiente de Pearson (simplificado):

$$
As = \frac{3(\bar{x} - Me)}{\sigma}
$$

Donde:
- $\bar{x}$ = media
- $Me$ = mediana
- $\sigma$ = desviación estándar

### 💡 Interpretación:

| Valor de As | Interpretación |
|-------------|----------------|
| As ≈ 0 | Distribución simétrica |
| As > 0 | Sesgo a la derecha (positivo) |
| As < 0 | Sesgo a la izquierda (negativo) |

---

## 📖 Resumen Visual

```
SIMÉTRICA:          SESGO DERECHA:      SESGO IZQUIERDA:
   ▲                 ▲                           ▲
Moda=Me=x̄          Mo < Me < x̄            x̄ < Me < Mo
   │                 │     └→              ←┘     │
   ▼                 ▼                           ▼
```

---

## 🔑 Resumen

| Concepto | Resumen |
|----------|---------|
| **Distribución simétrica** | Media = Mediana = Moda |
| **Sesgo a la derecha** | Moda < Mediana < Media |
| **Sesgo a la izquierda** | Media < Mediana < Moda |
| **Mejor para datos normales** | Media |
| **Mejor para datos sesgados** | Mediana |
| **Mejor para cualitativos** | Moda |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Para cada conjunto de datos, calcula media, mediana y moda, y determina el tipo de sesgo:

a) 5, 6, 6, 7, 7, 7, 8, 8, 9
b) 10, 10, 10, 11, 12, 15, 20, 25, 50

<details>
<summary>Ver solución</summary>

**a) Datos: 5, 6, 6, 7, 7, 7, 8, 8, 9**

- **Media:** $\frac{63}{9} = 7$
- **Mediana:** Posición 5 → **7**
- **Moda:** 7 (aparece 3 veces)

**Resultado:** Media = Mediana = Moda = 7
**Sesgo:** Distribución **simétrica**

---

**b) Datos: 10, 10, 10, 11, 12, 15, 20, 25, 50**

- **Media:** $\frac{163}{9} = 18.1$
- **Mediana:** Posición 5 → **12**
- **Moda:** 10 (aparece 3 veces)

**Resultado:** Moda (10) < Mediana (12) < Media (18.1)
**Sesgo:** **Positivo** (a la derecha) - el 50 jala la media

</details>

### Ejercicio 2
Un profesor tiene las siguientes notas: 2, 3, 7, 7, 8, 8, 8, 9, 9

a) ¿Qué medida debería usar para reportar el rendimiento "típico"?
b) ¿Por qué?

<details>
<summary>Ver solución</summary>

**Cálculos:**
- Media: $\frac{61}{9} = 6.78$
- Mediana: 8 (posición 5)
- Moda: 8 (aparece 3 veces)

**a) Debería usar la MEDIANA (o la moda)**

**b) Razón:**
- Las notas 2 y 3 son valores extremos bajos
- Estos valores "jalan" la media hacia abajo (6.78)
- Pero 7 de 9 estudiantes sacaron 7 o más
- La mediana (8) representa mejor al grupo "típico"
- La media (6.78) sugiere un rendimiento peor del real

</details>

### Ejercicio 3
En cada situación, ¿qué medida de tendencia central usaría un experto?

a) Un economista reportando el ingreso típico de un país
b) Un fabricante decidiendo qué talla de camiseta producir más
c) Un meteorólogo calculando la temperatura media mensual
d) Un hospital analizando tiempos de espera en emergencias

<details>
<summary>Ver solución</summary>

a) **Mediana** - Los ingresos tienen distribución sesgada (pocos ganan mucho). La mediana es el estándar internacional.

b) **Moda** - Necesita saber cuál es la más demandada, no un promedio de tallas.

c) **Media** - Las temperaturas son datos numéricos continuos, generalmente sin extremos absurdos en un mes típico.

d) **Mediana** - Los tiempos de espera suelen tener distribución sesgada (algunos casos muy largos). La mediana representa mejor el tiempo "típico".

</details>

### Ejercicio 4
Si en un conjunto de datos: Media = 50, Mediana = 55, Moda = 60

a) ¿Cuál es el tipo de sesgo?
b) ¿Hacia qué lado está la "cola" larga?
c) Dibuja un histograma aproximado

<details>
<summary>Ver solución</summary>

a) **Sesgo NEGATIVO (a la izquierda)**
Media (50) < Mediana (55) < Moda (60)

b) La **cola larga está hacia la IZQUIERDA** (valores bajos)

c) **Histograma aproximado:**

```
         ▄█   ← Moda (60)
        ▄██
       ▄███   ← Mediana (55)
      ▄████
     ▄█████
▄▄▄▄██████    ← Media (50) jalada por cola izquierda
     ↑
Cola larga
hacia valores bajos
```

**Interpretación:** La mayoría de los datos están en valores altos (cerca de 60), pero hay algunos valores muy bajos que jalan la media hacia abajo.

</details>
