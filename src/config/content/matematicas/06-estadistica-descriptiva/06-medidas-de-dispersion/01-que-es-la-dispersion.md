---
title: "¿Qué es la Dispersión?"
---

# **¿Qué es la Dispersión?**

Imagina que quieres cruzar un río. Un letrero dice: *"Profundidad promedio: 1 metro"*. ¿Cruzas tranquilo? Depende. Si todo el río mide 1 metro de hondo, sí. Pero si la orilla mide 10 cm y el centro mide 3 metros, te ahogarás. El promedio te mintió (o te contó una verdad a medias). La **dispersión** te dice qué tanto varían los datos reales respecto a ese promedio.

---

## 🎯 ¿Qué vas a aprender?

- Comprender que el promedio no cuenta toda la historia.
- Diferenciar entre datos "homogéneos" (compactos) y "heterogéneos" (dispersos).
- Identificar situaciones de riesgo ocultas por la media.
- Conocer el mapa de las medidas que estudiaremos (Rango, Varianza, Desviación).

---

## El Engaño del Promedio

Dos conjuntos de datos pueden tener el mismo centro, pero formas muy distintas.

### ⚙️ Ejemplos Resueltos: Misma Media, Diferente Vida

#### Ejemplo 1: El Clima
- **Ciudad A:** Siempre hace 25°C. (Media: 25°C).
- **Ciudad B:** Día 40°C, Noche 10°C. (Media: 25°C).
**Análisis:** En A vives feliz. En B te congelas y te quemas el mismo día. La dispersión en B es alta.

#### Ejemplo 2: El Francotirador
- **Tirador 1:** Da siempre en el borde del blanco (arriba, abajo, izq, der). Promedio: Centro.
- **Tirador 2:** Da siempre en el centro. Promedio: Centro.
**Análisis:** El Tirador 2 es preciso (baja dispersión). El 1 es terrible (alta dispersión), aunque matemáticamente su promedio es perfecto.

#### Ejemplo 3: La Montaña Rusa vs El Tren
- **Tren:** Velocidad constante 80 km/h.
- **Montaña Rusa:** Sube a 10 km/h, baja a 150 km/h. Promedio 80 km/h.
**Análisis:** La experiencia es totalmente diferente.

#### Ejemplo 4: Notas de Clase
- **Alumno Constante:** 3.0, 3.0, 3.0. (Media 3.0).
- **Alumno Irregular:** 1.0, 5.0, 3.0. (Media 3.0).
**Análisis:** El irregular es impredecible.

#### Ejemplo 5: Inversiones
- **Bono Gobierno:** Gana 5% fijo. Riesgo nulo (Dispersión 0).
- **Criptomoneda:** Sube 100%, baja 90%. Promedio 5%.
**Análisis:** La dispersión aquí se llama **Riesgo**.

---

## ¿Por qué varían los datos?

La variación es natural, pero entender su fuente es vital.

### ⚙️ Ejemplos Resueltos: Fuentes de Dispersión

#### Ejemplo 1: Error de Medición
Mides tu altura 5 veces. 170.1, 169.9, 170.0...
**Fuente:** Imprecisión del instrumento. Dispersión pequeña y esperada.

#### Ejemplo 2: Variabilidad Biológica
Mides la altura de 5 personas. 150, 190, 165...
**Fuente:** Genética. Dispersión natural grande.

#### Ejemplo 3: Proceso Industrial
Llenado de botellas de refresco. 500ml, 501ml, 499ml.
**Fuente:** Calibración de la máquina. Se busca reducirla a cero (Six Sigma).

#### Ejemplo 4: Diferencias de Mercado
Precios de una Coca-Cola en diferentes barrios.
**Fuente:** Poder adquisitivo, ubicación.

#### Ejemplo 5: Clima
Lluvia diaria en abril.
**Fuente:** Caos atmosférico. Dispersión alta.

---

## Mapa de Medidas de Dispersión

Para medir este "desorden", usaremos cuatro herramientas principales en las próximas lecciones:

1.  **Rango:** Distancia entre el máximo y mínimo. (Lo más básico). 
    *Ej: De 10 a 40°C.*
2.  **Varianza ($\sigma^2$):** Promedio de las distancias al cuadrado. (Matemáticamente potente, pero unidades raras).
3.  **Desviación Estándar ($\sigma$):** La reina de la dispersión. Nos dice cuánto se aleja un dato "típico" del promedio.
4.  **Coeficiente de Variación:** Para comparar peras con manzanas. (Ej: ¿Qué varía más, el precio de un chicle o el de un avión?).

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Tienes dos grupos con Media=50.
Grupo A: [48, 50, 52]. Grupo B: [0, 50, 100].
¿Cuál tiene mayor dispersión?

<details>
<summary>Ver solución</summary>

**Análisis:** El grupo B se aleja muchísimo más del 50.
**Resultado:** $\boxed{\text{Grupo B}}$

</details>

### Ejercicio 2
Si todos los datos son iguales (ej: 5, 5, 5), ¿cuánto vale la dispersión?

<details>
<summary>Ver solución</summary>

**Concepto:** No hay variación.
**Resultado:** $\boxed{0}$

</details>

### Ejercicio 3
En medicina, ¿prefieres un monitor cardíaco con alta o baja dispersión en sus lecturas (asumiendo paciente sano)?

<details>
<summary>Ver solución</summary>

**Lógica:** Quieres estabilidad y precisión.
**Resultado:** $\boxed{\text{Baja dispersión}}$

</details>

### Ejercicio 4
¿Qué medida usarías para saber la diferencia entre el estudiante más joven y el más viejo de un salón?

<details>
<summary>Ver solución</summary>

**Concepto:** Diferencia Max - Min.
**Resultado:** $\boxed{\text{El Rango}}$

</details>

### Ejercicio 5
Verdadero o Falso: Si la dispersión es alta, el promedio es muy representativo del grupo.

<details>
<summary>Ver solución</summary>

**Lógica:** Al contrario. Si hay mucho caos, el promedio representa a pocos.
**Resultado:** $\boxed{\text{Falso}}$

</details>

### Ejercicio 6
Un reloj se adelanta 5 minutos un día y se atrasa 5 minutos el otro. Su error promedio es 0. ¿Es un buen reloj?

<details>
<summary>Ver solución</summary>

**Análisis:** No, porque su variabilidad es alta. Nunca sabes la hora real.
**Resultado:** $\boxed{\text{No}}$

</details>

### Ejercicio 7
¿Qué grupo es más "homogéneo"?
A: [10, 11, 12]. B: [10, 20, 30].

<details>
<summary>Ver solución</summary>

**Definición:** Homogéneo significa "parecido".
**Resultado:** $\boxed{\text{Grupo A}}$

</details>

### Ejercicio 8
En finanzas, ¿cómo se le llama a la dispersión de los precios de una acción?

<details>
<summary>Ver solución</summary>

**Vocabulario:** Incertidumbre en el retorno.
**Resultado:** $\boxed{\text{Volatilidad o Riesgo}}$

</details>

### Ejercicio 9
Si sumas 10 a todos los datos, ¿la dispersión cambia?
Ej: [1, 3] pasa a [11, 13].

<details>
<summary>Ver solución</summary>

**Análisis:** La distancia entre ellos sigue siendo 2. Se movieron juntos.
**Resultado:** $\boxed{\text{No cambia}}$

</details>

### Ejercicio 10
Si multiplicas todos los datos por 10, ¿la dispersión cambia?
Ej: [1, 3] pasa a [10, 30].

<details>
<summary>Ver solución</summary>

**Análisis:** Antes la distancia era 2. Ahora es 20. Se "estiraron".
**Resultado:** $\boxed{\text{Sí, aumenta}}$

</details>

---

## 🔑 Resumen

| Término | Significado | Sinónimo |
|---------|-------------|----------|
| **Dispersión** | Grado de separación de los datos. | Variabilidad. |
| **Homogéneo** | Datos muy parecidos (poca dispersión). | Consistente. |
| **Heterogéneo** | Datos muy distintos (mucha dispersión). | Irregular. |

> **Conclusión:** La media nos dice el destino, pero la dispersión nos dice qué tan turbulento será el viaje.
