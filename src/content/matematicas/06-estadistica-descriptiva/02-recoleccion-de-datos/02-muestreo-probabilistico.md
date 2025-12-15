# Muestreo Probabilístico

Ya sabes que el muestreo es estudiar una parte para inferir sobre el todo. Pero ¿cómo **seleccionar** esa parte de manera justa y confiable?

El **muestreo probabilístico** garantiza que cada miembro de la población tenga una **probabilidad conocida** de ser seleccionado. Es como un sorteo justo donde todos tienen oportunidad.

---

## 🎯 ¿Qué vas a aprender?

- Qué hace que un muestreo sea "probabilístico"
- Los 4 métodos principales: aleatorio simple, sistemático, estratificado y por conglomerados
- Cuándo usar cada método

---

## 📊 Resumen de Métodos

| Método | Idea Principal | Mejor Para |
|--------|---------------|------------|
| **Aleatorio Simple** | Cada individuo tiene igual probabilidad | Poblaciones homogéneas |
| **Sistemático** | Seleccionar cada k-ésimo elemento | Listas ordenadas |
| **Estratificado** | Dividir en grupos, muestrear cada grupo | Poblaciones con subgrupos |
| **Por Conglomerados** | Dividir en grupos, seleccionar grupos completos | Poblaciones dispersas geográficamente |

---

## 📖 Muestreo Aleatorio Simple

> En el **muestreo aleatorio simple**, cada individuo de la población tiene **exactamente la misma probabilidad** de ser seleccionado. Es como sacar nombres de un sombrero.

### 💡 Características:
- Todos tienen igual oportunidad
- La selección es completamente al azar
- Es el método más básico y fundamental

### ⚙️ Ejemplo 1: Lotería

**Población:** 500 empleados de una empresa
**Muestra deseada:** 50 empleados

**Proceso:**
1. Asignar un número del 1 al 500 a cada empleado
2. Usar un generador de números aleatorios (o papelitos en una bolsa)
3. Seleccionar 50 números al azar
4. Los empleados con esos números forman la muestra

**Probabilidad de ser seleccionado:** $\frac{50}{500} = \frac{1}{10} = 10\%$ para cada empleado.

### ⚙️ Ejemplo 2: Encuesta en el salón

**Población:** 35 estudiantes del salón
**Muestra deseada:** 7 estudiantes

**Proceso:**
1. Escribir los 35 nombres en papelitos iguales
2. Mezclar bien los papelitos en una bolsa
3. Sacar 7 papelitos sin ver
4. Esos 7 estudiantes son la muestra

### 💡 ¿Cómo generar números aleatorios?
- Tabla de números aleatorios (método tradicional)
- Calculadora científica con función RAND
- Hojas de cálculo (función ALEATORIO)
- Aplicaciones en línea

### ✅ Ventajas y ❌ Desventajas

| ✅ Ventajas | ❌ Desventajas |
|-------------|---------------|
| Muy simple de entender | Necesitas lista completa de la población |
| Libre de sesgo del investigador | Puede no representar bien subgrupos pequeños |
| Base para métodos estadísticos | Difícil si la población está dispersa |

---

## 📖 Muestreo Sistemático

> En el **muestreo sistemático**, se selecciona un punto de inicio al azar y luego se elige **cada k-ésimo elemento** de la lista.

### 💡 La fórmula del intervalo:

$$
k = \frac{N}{n}
$$

Donde:
- $N$ = tamaño de la población
- $n$ = tamaño de la muestra deseada
- $k$ = intervalo de selección

### ⚙️ Ejemplo 1: Lista de clientes

**Población:** 1,000 clientes en una base de datos
**Muestra deseada:** 100 clientes

**Cálculo del intervalo:**
$$
k = \frac{1000}{100} = 10
$$

**Proceso:**
1. Elegir un número aleatorio entre 1 y 10 (supongamos que sale el 3)
2. Seleccionar: cliente 3, 13, 23, 33, 43, 53... (cada 10)
3. Continuar hasta tener 100 clientes

**Resultado:** Se seleccionan los clientes: 3, 13, 23, 33, 43, 53, 63, 73, 83, 93, 103, 113...

### ⚙️ Ejemplo 2: Fila de producción

Una fábrica produce tornillos en una línea de producción. Para control de calidad:

- **Población:** Todos los tornillos del día
- **Muestra deseada:** Cada tornillo número 50

**Proceso:**
1. Punto de inicio aleatorio: tornillo #23
2. Luego: #73, #123, #173, #223...
3. Se revisa la calidad de cada tornillo seleccionado

### ⚠️ Cuidado con patrones

El muestreo sistemático puede fallar si hay un **patrón** en la lista que coincida con el intervalo.

**Ejemplo problemático:**
- Una tienda ordena sus ventas por día de la semana
- Si k = 7, siempre seleccionarías el mismo día de la semana
- La muestra estaría sesgada hacia ese día

**Solución:** Asegurarse de que la lista no tenga patrones periódicos.

### ✅ Ventajas y ❌ Desventajas

| ✅ Ventajas | ❌ Desventajas |
|-------------|---------------|
| Más fácil de aplicar que el aleatorio simple | Puede coincidir con patrones en los datos |
| No necesitas lista completa al inicio | Requiere que la lista esté disponible |
| Garantiza distribución uniforme | Menos aleatorio que el simple |

---

## 📖 Muestreo Estratificado

> En el **muestreo estratificado**, la población se divide en **grupos homogéneos** (estratos) y se toma una muestra aleatoria de **cada estrato**.

### 💡 ¿Qué es un estrato?
Un subgrupo de la población donde los miembros son **similares entre sí** respecto a alguna característica importante.

### ⚙️ Ejemplo 1: Encuesta universitaria

**Población:** 10,000 estudiantes universitarios
**Estratos:** Por facultad (Ingeniería, Medicina, Derecho, etc.)

| Facultad | Estudiantes | Proporción | Muestra (de 500) |
|----------|-------------|------------|------------------|
| Ingeniería | 3,000 | 30% | 150 |
| Medicina | 2,000 | 20% | 100 |
| Derecho | 2,500 | 25% | 125 |
| Humanidades | 2,500 | 25% | 125 |
| **Total** | 10,000 | 100% | 500 |

**Proceso:**
1. Dividir la población por facultad
2. Calcular cuántos seleccionar de cada una (proporcional)
3. Hacer muestreo aleatorio simple dentro de cada facultad

**Resultado:** La muestra respeta la proporción de cada facultad en la población.

### ⚙️ Ejemplo 2: Encuesta nacional por regiones

**Población:** Habitantes de un país
**Estratos:** Regiones geográficas

| Región | Población | Muestra proporcional |
|--------|-----------|---------------------|
| Norte | 5 millones (25%) | 250 encuestados |
| Centro | 10 millones (50%) | 500 encuestados |
| Sur | 5 millones (25%) | 250 encuestados |
| **Total** | 20 millones | 1,000 encuestados |

### 💡 ¿Cuándo usar estratificación?

Cuando la población tiene **subgrupos importantes** que queremos asegurar que estén representados:
- Niveles socioeconómicos
- Géneros
- Grupos de edad
- Regiones geográficas
- Departamentos de una empresa

### ✅ Ventajas y ❌ Desventajas

| ✅ Ventajas | ❌ Desventajas |
|-------------|---------------|
| Garantiza representación de todos los subgrupos | Necesitas conocer los estratos de antemano |
| Más preciso que el aleatorio simple | Más complejo de administrar |
| Permite análisis por subgrupos | Requiere información previa de la población |

---

## 📖 Muestreo por Conglomerados

> En el **muestreo por conglomerados**, la población se divide en grupos (conglomerados) y se seleccionan **algunos grupos completos** para estudiar.

### 💡 Diferencia con estratificado:
- **Estratificado:** Muestra de TODOS los estratos
- **Conglomerados:** Muestra de ALGUNOS grupos (pero completos)

### ⚙️ Ejemplo 1: Colegios de una ciudad

**Población:** Todos los estudiantes de bachillerato de una ciudad
**Conglomerados:** Los 100 colegios de la ciudad

**Proceso:**
1. Seleccionar aleatoriamente 10 colegios de los 100
2. Encuestar a TODOS los estudiantes de esos 10 colegios
3. Los otros 90 colegios no participan

### ⚙️ Ejemplo 2: Barrios para estudio de salud

**Población:** Todos los habitantes de una ciudad
**Conglomerados:** Los 50 barrios de la ciudad

**Proceso:**
1. Seleccionar aleatoriamente 5 barrios
2. Visitar y encuestar hogares en esos 5 barrios
3. Los otros 45 barrios no se visitan

### 💡 ¿Cuándo usar conglomerados?

- Cuando la población está **naturalmente dividida** en grupos
- Cuando es **costoso o difícil** llegar a toda la población
- Cuando los grupos (conglomerados) son **internamente heterogéneos** (tienen variedad dentro)

### ⚙️ Ejemplo 3: Muestreo en dos etapas

A veces se combina:
1. **Primera etapa:** Seleccionar conglomerados (ej: 10 colegios)
2. **Segunda etapa:** Dentro de cada conglomerado, hacer muestreo aleatorio (ej: 30 estudiantes por colegio)

**Resultado:** 10 colegios × 30 estudiantes = 300 estudiantes

### ✅ Ventajas y ❌ Desventajas

| ✅ Ventajas | ❌ Desventajas |
|-------------|---------------|
| Muy económico (concentra esfuerzos) | Menos preciso que estratificado |
| No necesitas lista de toda la población | Los conglomerados deben ser heterogéneos |
| Ideal para poblaciones dispersas | Mayor error de muestreo |

---

## 💡 ¿Cuál Método Elegir?

| Situación | Método Recomendado |
|-----------|-------------------|
| Población pequeña y accesible | Aleatorio Simple |
| Tienes una lista ordenada | Sistemático |
| Hay subgrupos importantes a representar | Estratificado |
| Población dispersa geográficamente | Por Conglomerados |
| Presupuesto muy limitado | Por Conglomerados |
| Necesitas máxima precisión | Estratificado |

---

## 🔑 Resumen

| Método | Proceso | Clave |
|--------|---------|-------|
| **Aleatorio Simple** | Selección al azar de individuos | Todos tienen igual probabilidad |
| **Sistemático** | Cada k-ésimo elemento | Punto de inicio aleatorio |
| **Estratificado** | Muestra de cada estrato | Garantiza representación de subgrupos |
| **Por Conglomerados** | Grupos completos seleccionados | Económico para poblaciones dispersas |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Una universidad tiene 5,000 estudiantes. El investigador quiere una muestra de 200 usando muestreo sistemático.

a) ¿Cuál es el intervalo de selección (k)?
b) Si el número aleatorio inicial es 7, ¿cuáles son los primeros 5 estudiantes seleccionados?

<details>
<summary>Ver solución</summary>

a) **Intervalo:**
$$k = \frac{N}{n} = \frac{5000}{200} = 25$$

b) **Primeros 5 seleccionados:**
- Inicio: 7
- Luego: 7+25=32, 32+25=57, 57+25=82, 82+25=107

**Respuesta:** Estudiantes 7, 32, 57, 82, 107

</details>

### Ejercicio 2
¿Qué tipo de muestreo se está usando en cada caso?

a) Se asigna un número a cada empleado y se usa una app para seleccionar 50 números al azar.
b) Se divide a los votantes por departamento y se encuesta proporcionalmente en cada uno.
c) Se seleccionan 5 hospitales de una ciudad y se encuestan todos los médicos de esos hospitales.
d) En una línea de producción, se inspecciona cada producto número 100.

<details>
<summary>Ver solución</summary>

a) **Aleatorio Simple** - Cada empleado tiene igual probabilidad

b) **Estratificado** - Se divide en grupos y se muestrea de cada uno

c) **Por Conglomerados** - Se seleccionan grupos completos

d) **Sistemático** - Se selecciona cada k-ésimo elemento (k=100)

</details>

### Ejercicio 3
Un investigador quiere estudiar a los estudiantes de secundaria de un país. Tiene tiempo y presupuesto limitados.

a) ¿Sería práctico un muestreo aleatorio simple? ¿Por qué?
b) ¿Qué método de muestreo recomendarías y cómo lo implementarías?

<details>
<summary>Ver solución</summary>

a) **No sería práctico** porque:
- Necesitaría una lista de TODOS los estudiantes del país
- Si selecciona al azar, podría tener que viajar a muchas ciudades diferentes
- Sería muy costoso y lento

b) **Muestreo por conglomerados (en dos etapas):**

**Primera etapa:** 
- Conglomerados = colegios
- Seleccionar aleatoriamente 20 colegios del país

**Segunda etapa:**
- En cada colegio seleccionado, hacer muestreo aleatorio de 30 estudiantes
- Total: 20 × 30 = 600 estudiantes

**Ventajas:**
- Solo visita 20 colegios en lugar de cientos
- Más económico y manejable
- Aún así obtiene diversidad geográfica si los colegios están bien distribuidos

</details>

### Ejercicio 4
Una empresa tiene 1,000 empleados distribuidos así:

| Departamento | Empleados |
|--------------|-----------|
| Producción | 500 |
| Ventas | 300 |
| Administración | 200 |

Si quieren encuestar a 100 empleados usando muestreo estratificado proporcional, ¿cuántos deben seleccionar de cada departamento?

<details>
<summary>Ver solución</summary>

**Paso 1:** Calcular las proporciones:
- Producción: $\frac{500}{1000} = 50\%$
- Ventas: $\frac{300}{1000} = 30\%$
- Administración: $\frac{200}{1000} = 20\%$

**Paso 2:** Aplicar proporciones a la muestra de 100:

| Departamento | Proporción | Muestra |
|--------------|------------|---------|
| Producción | 50% | 50 empleados |
| Ventas | 30% | 30 empleados |
| Administración | 20% | 20 empleados |
| **Total** | 100% | **100 empleados** |

**Respuesta:** 50 de Producción, 30 de Ventas, 20 de Administración

</details>
