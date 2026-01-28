---
title: "Coeficiente de Variación"
---

# **Coeficiente de Variación**

Si te dicen que una máquina tiene un error de 1 cm, ¿es mucho o poco?
- En un **microchip** de 2 cm, un error de 1 cm es desastroso (50% de error).
- En un **edificio** de 100 metros (10,000 cm), un error de 1 cm es irrelevante (0.01% de error).

La **Desviación Estándar** ($S=1$ cm) es la misma en ambos casos, pero el impacto es muy diferente. Para medir la dispersión **relativa** al tamaño de la cosa, usamos el **Coeficiente de Variación (CV)**.

---

## 🎯 ¿Qué vas a aprender?

- Calcular el Coeficiente de Variación para comparar peras con manzanas.
- Interpretar el resultado como un porcentaje de variación.
- Clasificar datos como "homogéneos" o "heterogéneos" según su CV.
- Entender por qué no funciona con temperaturas (escalas sin cero absoluto).

---

## La Fórmula de la Relatividad Estadística

Simplemente dividimos la desviación entre el promedio.

$$ CV = \frac{s}{|\bar{x}|} \times 100\% $$

Este número nos dice qué tan grande es la dispersión en comparación con el tamaño promedio de los datos.

---

## Cálculo y Comparación

### ⚙️ Ejemplos Resueltos

#### Ejemplo 1: El Pan vs El Carro
- **Pan:** Precio \$2,000. Desviación \$200.
  $$CV = \frac{200}{2000} \times 100\% = 10\%$$
- **Carro:** Precio \$50,000,000. Desviación \$200.
  $$CV = \frac{200}{50,000,000} \times 100\% = 0.0004\%$$
**Conclusión:** Aunque la desviación es la misma (\$200), el precio del pan varía muchísimo más en términos relativos.

#### Ejemplo 2: Hormiga vs Elefante
- **Hormigas:** Peso medio 5 mg ($S=1$ mg). $CV = 20\%$.
- **Elefantes:** Peso medio 5,000,000 mg ($S=10,000$ mg). $CV = 0.2\%$.
**Conclusión:** Las hormigas son más "diversas" en peso que los elefantes, aun si la desviación del elefante es gigante.

#### Ejemplo 3: Dólares vs Euros
- **Grupo A (Dólares):** Media \$100, $S=10$. $CV = 10\%$.
- **Grupo B (Euros):** Media €90, $S=9$. $CV = 10\%$.
**Conclusión:** Ambos grupos tienen la misma variabilidad relativa. El CV no tiene unidades (es adimensional), perfecto para comparar monedas.

#### Ejemplo 4: Inversiones
- **Acción A:** Retorno 10%, Riesgo ($S$) 2%. $CV = 20\%$.
- **Acción B:** Retorno 20%, Riesgo ($S$) 6%. $CV = 30\%$.
**Conclusión:** La Acción A es más segura (menos volátil en relación a lo que ganas).

#### Ejemplo 5: Adultos vs Niños
- **Niños:** Altura media 100 cm, $S=10$ cm. $CV=10\%$.
- **Adultos:** Altura media 170 cm, $S=10$ cm. $CV=5.8\%$.
**Conclusión:** La dispersión es la misma (10 cm), pero en los niños se nota más (representa una mayor porción de su cuerpo).

---

## Interpretación: ¿Homogéneo o Heterogéneo?

Aunque no hay una regla sagrada, se suele usar este semáforo comúnmente en ciencias sociales y biológicas:

1.  **CV < 10%:** Datos **Homogéneos**. (Muy parecidos entre sí. El promedio es muy confiable).
2.  **CV 10% - 30%:** Dispersión Moderada.
3.  **CV > 30%:** Datos **Heterogéneos**. (Muy distintos. El promedio es poco representativo).

### ⚙️ Ejemplos Resueltos: Calidad de Datos

#### Ejemplo 1: Laboratorio Clínico
Un análisis de sangre da $CV=2\%$.
**Interpretación:** Altísima precisión. Datos muy homogéneos.

#### Ejemplo 2: Ingresos de un País
El $CV$ de los salarios suele ser alto (ej: 60% o más).
**Interpretación:** Muy Heterogéneo. Hay mucha desigualdad. El "sueldo promedio" no representa a la mayoría.

#### Ejemplo 3: Llenado de Botellas
Fábrica de refrescos. Media 500ml, $S=5$ml.
$$CV = \frac{5}{500} = 1\%$$
**Interpretación:** Proceso controlado y homogéneo.

#### Ejemplo 4: Edad en un concierto de Rock
Media 25 años, $S=10$ años.
$$CV = \frac{10}{25} = 40\%$$
**Interpretación:** Público Heterogéneo (hay desde adolescentes hasta abuelos).

#### Ejemplo 5: Temperatura Corporal
Media 37°C. $S=0.5$°C.
$$CV = \frac{0.5}{37} = 1.3\%$$
**Interpretación:** El cuerpo humano regula su temperatura de forma muy homogénea.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el CV si $\bar{x}=50$ y $S=5$.

<details>
<summary>Ver solución</summary>

**Cálculo:** $(5/50) \times 100 = 10\%$.
**Resultado:** $\boxed{10\%}$

</details>

### Ejercicio 2
¿Qué grupo es más variable relativamente?
A: Media 100, $S=10$.
B: Media 10, $S=2$.

<details>
<summary>Ver solución</summary>

- **A:** $10/100 = 10\%$.
- **B:** $2/10 = 20\%$.
**Resultado:** $\boxed{\text{Grupo B}}$

</details>

### Ejercicio 3
Si el CV es 0%, ¿qué significa?

<details>
<summary>Ver solución</summary>

**Análisis:** $S$ debe ser 0.
**Resultado:** $\boxed{\text{Todos los datos son iguales}}$

</details>

### Ejercicio 4
En un examen, el curso A tiene CV=5% y el curso B tiene CV=25%. ¿En cuál curso es más justo usar el promedio para calificar al grupo?

<details>
<summary>Ver solución</summary>

**Lógica:** Menor CV = Más representativo.
**Resultado:** $\boxed{\text{Curso A}}$

</details>

### Ejercicio 5
Calcula el CV de: 10, 10, 10.

<details>
<summary>Ver solución</summary>

**S:** 0. Media: 10.
**Resultado:** $\boxed{0\%}$

</details>

### Ejercicio 6
Si multiplicas todos los datos por 10, ¿cambia el CV?

<details>
<summary>Ver solución</summary>

**Análisis:**
- Media se multiplica por 10.
- Desviación se multiplica por 10.
- La división cancela el 10.
**Resultado:** $\boxed{\text{No cambia}}$

</details>

### Ejercicio 7
¿Por qué no se usa CV con temperaturas en Celsius?

<details>
<summary>Ver solución</summary>

**Razón:** El 0°C es arbitrario. Si la media es 0, divides por 0. Si es negativa, da CV negativo (raro).
**Resultado:** $\boxed{\text{Falta de cero absoluto}}$

</details>

### Ejercicio 8
Si el CV es 100%, ¿qué relación hay entre la media y la desviación?

<details>
<summary>Ver solución</summary>

**Ecuación:** $S / \bar{x} = 1$.
**Resultado:** $\boxed{S = \bar{x}}$ (Son iguales).

</details>

### Ejercicio 9
Una acción tiene retorno esperado 0% y riesgo 5%. ¿Cuál es el CV?

<details>
<summary>Ver solución</summary>

**Cálculo:** $5/0 \to \infty$.
**Resultado:** $\boxed{\text{Indefinido (No sirve aquí)}}$

</details>

### Ejercicio 10
Si sumas 100 a todos los datos, ¿el CV mejora (baja) o empeora (sube)?

<details>
<summary>Ver solución</summary>

**Análisis:**
- $S$ no cambia.
- $\bar{x}$ aumenta.
- Fracción $S/(\bar{x}+100)$ se hace más pequeña.
**Resultado:** $\boxed{\text{Baja (Mejora)}}$

</details>

---

## 🔑 Resumen

| Estadístico | Fórmula | Unidades | Uso Principal |
|-------------|---------|----------|---------------|
| **Desv. Estándar ($S$)** | $\sqrt{Var}$ | Metros, Kilos, etc. | Medir dispersión absoluta. |
| **Coef. Variación ($CV$)** | $S / \bar{x}$ | % (Adimensional). | Comparar dispersión relativa. |

> **Conclusión:** El Coeficiente de Variación es el "igualador". Nos permite comparar la precisión de un relojero suizo con la de un constructor de puentes, hablando un idioma común: el porcentaje.
