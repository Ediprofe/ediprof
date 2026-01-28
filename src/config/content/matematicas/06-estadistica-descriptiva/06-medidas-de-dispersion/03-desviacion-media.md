---
title: "Desviación Media"
---

# **Desviación Media**

Imagina que quedas de verte con un amigo a las 3:00 PM. Si llegas a las 3:10 PM, llegaste 10 minutos tarde. Si llegas a las 2:50 PM, llegaste 10 minutos temprano. En ambos casos, el "error" o la distancia al objetivo fue de 10 minutos. No importa si fue antes (-) o después (+), la magnitud del error es la misma. De eso trata la **Desviación Media**: promediar los errores sin importar su dirección.

---

## 🎯 ¿Qué vas a aprender?

- Comprender por qué no podemos simplemente sumar las restas $(x - \bar{x})$.
- Aplicar el valor absoluto $|x|$ para medir distancias reales.
- Calcular la Desviación Media ($DM$) para datos sueltos y tablas.
- Interpretar qué significa que una $DM$ sea grande o pequeña.

---

## El Problema de los Signos

La **desviación** es qué tan lejos está un dato del promedio.
- Si el dato es mayor que la media, la resta es positiva (+).
- Si el dato es menor, la resta es negativa (-).

El problema es que, por una propiedad matemática, si sumas todas esas restas **siempre da cero**. Los positivos se cancelan con los negativos.

### 💡 Solución: El Valor Absoluto
Usamos $|x|$ para volver todo positivo.
- $|-5| = 5$
- $|+5| = 5$
Ahora sí podemos sumar distancias reales.

---

## Cálculo con Datos Simples

$$ DM = \frac{\sum |x_i - \bar{x}|}{n} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Notas de Quiz
**Datos:** 2, 4, 6.
1.  **Media ($\bar{x}$):** $(2+4+6)/3 = 4$.
2.  **Desviaciones:**
    - $|2 - 4| = |-2| = 2$
    - $|4 - 4| = |0| = 0$
    - $|6 - 4| = |2| = 2$
3.  **Promedio de Desviaciones:** $(2+0+2)/3 = 1.33$.
**Resultado:** $\boxed{1.33}$

#### Ejemplo 2: Edades
**Datos:** 10, 15, 20, 25, 30.
1.  **Media:** 20.
2.  **Distancias:** $|10-20|=10$, $|15-20|=5$, $|20-20|=0$, $|25-20|=5$, $|30-20|=10$.
3.  **Suma:** $10+5+0+5+10 = 30$.
4.  **DM:** $30/5 = 6$.
**Resultado:** $\boxed{6 \text{ años}}$

#### Ejemplo 3: Temperaturas Bajo Cero
**Datos:** -5, -2, 1.
1.  **Media:** $(-5-2+1)/3 = -6/3 = -2$.
2.  **Distancias:**
    - $|-5 - (-2)| = |-3| = 3$
    - $|-2 - (-2)| = |0| = 0$
    - $|1 - (-2)| = |3| = 3$
3.  **DM:** $(3+0+3)/3 = 2$.
**Resultado:** $\boxed{2^\circ\text{C}}$

#### Ejemplo 4: Datos Idénticos
**Datos:** 8, 8, 8, 8.
1.  **Media:** 8.
2.  **Distancias:** Todas son 0.
3.  **DM:** 0.
**Resultado:** $\boxed{0}$ (Sin dispersión).

#### Ejemplo 5: Con un Outlier
**Datos:** 10, 10, 10, 50.
1.  **Media:** $(10+10+10+50)/4 = 20$.
2.  **Distancias:**
    - $|10-20| = 10$ (x3 veces)
    - $|50-20| = 30$
3.  **Suma:** $10+10+10+30 = 60$.
4.  **DM:** $60/4 = 15$.
**Resultado:** $\boxed{15}$

---

## Cálculo con Tablas de Frecuencia

$$ DM = \frac{\sum (f_i \cdot |x_i - \bar{x}|)}{n} $$

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: Hijos por familia
- **0 hijos:** 2 familias.
- **2 hijos:** 2 familias.
- **Media:** 1 hijo.
1.  **Distancias:**
    - Dato 0 dista 1 de la media. ($1 \times 2 \text{ fam} = 2$).
    - Dato 2 dista 1 de la media. ($1 \times 2 \text{ fam} = 2$).
2.  **Suma:** 4. **Total datos:** 4.
3.  **DM:** $4/4 = 1$.
**Resultado:** $\boxed{1}$

#### Ejemplo 2: Calificaciones (1-5)
- **1.0:** 1 persona.
- **5.0:** 1 persona.
- **3.0:** 8 personas.
1.  **Media:** 3.0.
2.  **Distancias:**
    - $|1-3|=2$ (x1) = 2.
    - $|5-3|=2$ (x1) = 2.
    - $|3-3|=0$ (x8) = 0.
3.  **Suma:** 4. **Total:** 10.
4.  **DM:** $0.4$.
**Resultado:** $\boxed{0.4}$

#### Ejemplo 3: Tallas (X=Talla numérica)
- **Talla 30:** 5 unidades.
- **Talla 40:** 5 unidades.
1.  **Media:** 35.
2.  **Distancias:**
    - $|30-35|=5$. ($5 \times 5 = 25$).
    - $|40-35|=5$. ($5 \times 5 = 25$).
3.  **Suma:** 50. **Total:** 10.
4.  **DM:** 5.
**Resultado:** $\boxed{5}$

#### Ejemplo 4: Dispersión Asimétrica
- **Dato 10:** 9 veces.
- **Dato 20:** 1 vez.
1.  **Media:** 11.
2.  **Distancias:**
    - $|10-11|=1$. ($1 \times 9 = 9$).
    - $|20-11|=9$. ($9 \times 1 = 9$).
3.  **Suma:** 18. **Total:** 10.
4.  **DM:** $1.8$.
**Resultado:** $\boxed{1.8}$

#### Ejemplo 5: Tabla agrupada (Marca de clase)
- **[0-10]:** Marca 5. $f=10$.
- **[10-20]:** Marca 15. $f=10$.
1.  **Media:** 10.
2.  **Distancias:**
    - $|5-10|=5$. ($5 \times 10 = 50$).
    - $|15-10|=5$. ($5 \times 10 = 50$).
3.  **Suma:** 100. **Total:** 20.
4.  **DM:** 5.
**Resultado:** $\boxed{5}$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula la DM de: 3, 7, 8.

<details>
<summary>Ver solución</summary>

**Media:** $(3+7+8)/3 = 6$.
**Distancias:** $|3-6|=3$, $|7-6|=1$, $|8-6|=2$.
**Promedio:** $(3+1+2)/3 = 2$.
**Resultado:** $\boxed{2}$

</details>

### Ejercicio 2
Si todos los datos distan exactamente 4 unidades de la media, ¿cuál es la DM?

<details>
<summary>Ver solución</summary>

**Concepto:** La DM es el promedio de esas distancias. Si todas son 4, el promedio es 4.
**Resultado:** $\boxed{4}$

</details>

### Ejercicio 3
Calcula la DM de: -10, 0, 10.

<details>
<summary>Ver solución</summary>

**Media:** 0.
**Distancias:** 10, 0, 10.
**Promedio:** $20/3 = 6.66$.
**Resultado:** $\boxed{6.67}$

</details>

### Ejercicio 4
¿Por qué $|-5|$ es igual a $5$?

<details>
<summary>Ver solución</summary>

**Definición:** El valor absoluto mide la distancia al cero en la recta numérica, y las distancias no son negativas.
**Resultado:** $\boxed{\text{Es una distancia}}$

</details>

### Ejercicio 5
Calcula la DM si $\sum|x - \bar{x}| = 50$ y $n=10$.

<details>
<summary>Ver solución</summary>

**Fórmula:** $DM = \text{Suma} / n$.
**Cálculo:** $50/10 = 5$.
**Resultado:** $\boxed{5}$

</details>

### Ejercicio 6
Tienes datos: 100, 100, 100. ¿Cuál es la DM?

<details>
<summary>Ver solución</summary>

**Análisis:** No hay variación respecto a la media.
**Resultado:** $\boxed{0}$

</details>

### Ejercicio 7
Si duplicas todos los datos (Ej: 2,4 $\to$ 4,8), ¿qué le pasa a la DM?

<details>
<summary>Ver solución</summary>

**Prueba:**
- DM(2,4) Media=3. Dist=1. DM=1.
- DM(4,8) Media=6. Dist=2. DM=2.
**Resultado:** $\boxed{\text{Se duplica}}$

</details>

### Ejercicio 8
Sumas 10 a todos los datos. ¿Qué le pasa a la DM?

<details>
<summary>Ver solución</summary>

**Análisis:** Los datos se mueven, pero la distancia entre ellos (y a la media) se mantiene igual.
**Resultado:** $\boxed{\text{No cambia}}$

</details>

### Ejercicio 9
¿Puede la DM ser negativa?

<details>
<summary>Ver solución</summary>

**Teoría:** Promedias valores absolutos (positivos). Imposible que dé negativo.
**Resultado:** $\boxed{\text{No}}$

</details>

### Ejercicio 10
Compara DM de A:[0, 10] y B:[4, 6]. (Ambos media 5).

<details>
<summary>Ver solución</summary>

**A:** Distancias 5 y 5. DM=5.
**B:** Distancias 1 y 1. DM=1.
**Resultado:** $\boxed{A \text{ es mayor}}$

</details>

---

## 🔑 Resumen

| Símbolo | Significado | Fórmula |
|---------|-------------|---------|
| **$|x|$** | Valor Absoluto | Quitar el signo negativo. |
| **$DM$** | Desviación Media | $\frac{\sum |x_i - \bar{x}|}{n}$ |

> **Conclusión:** La Desviación Media es la medida más intuitiva de la dispersión: es simplemente el promedio de los errores.
