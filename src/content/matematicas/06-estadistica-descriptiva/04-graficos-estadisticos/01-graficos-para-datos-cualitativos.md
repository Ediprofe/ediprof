# Gráficos para Datos Cualitativos

Los números y tablas son útiles, pero a veces **una imagen dice más que mil datos**. Los gráficos nos permiten ver patrones, comparaciones y proporciones de un vistazo.

Empecemos con los gráficos más adecuados para datos **cualitativos** (categóricos).

---

## 🎯 ¿Qué vas a aprender?

- Cuándo usar cada tipo de gráfico
- Cómo construir e interpretar diagramas de barras
- Cómo construir e interpretar diagramas circulares (de pastel)
- Qué son los pictogramas y cuándo usarlos

---

## 📊 Resumen de Gráficos para Datos Cualitativos

| Gráfico | Mejor para | Ejemplo |
|---------|------------|---------|
| **Diagrama de barras** | Comparar categorías | Votos por candidato |
| **Diagrama circular** | Mostrar proporciones del todo | Distribución del presupuesto |
| **Pictograma** | Comunicación visual simple | Infografías |

---

## 📖 Diagrama de Barras

> El **diagrama de barras** usa rectángulos de igual ancho pero diferente altura para representar la frecuencia de cada categoría.

### 💡 Características:
- Cada categoría tiene una barra
- La **altura** de la barra representa la frecuencia (o porcentaje)
- Las barras están **separadas** (no se tocan)
- Puede ser vertical u horizontal

### ⚙️ Ejemplo 1: Transporte al trabajo

| Medio | f | % |
|-------|---|---|
| Bus | 45 | 45% |
| Metro | 25 | 25% |
| Carro | 20 | 20% |
| Bicicleta | 7 | 7% |
| A pie | 3 | 3% |
| **Total** | **100** | **100%** |

**Cómo construirlo:**

1. Eje horizontal (X): Las categorías (Bus, Metro, Carro...)
2. Eje vertical (Y): La frecuencia (0 a 45 o más)
3. Para cada categoría, dibujar una barra hasta su frecuencia
4. Dejar espacio entre barras

### 💡 Reglas importantes:

- **El eje Y debe empezar en cero** (si no, las comparaciones visuales son engañosas)
- Todas las barras deben tener el **mismo ancho**
- Las barras deben estar **separadas** (esto las distingue del histograma)
- Añadir **título** y **etiquetas** a los ejes

### ⚙️ Ejemplo 2: Barras horizontales

A veces las barras horizontales son mejores:
- Cuando los nombres de las categorías son largos
- Cuando hay muchas categorías

| Carrera | Estudiantes |
|---------|-------------|
| Ingeniería de Sistemas | 350 |
| Medicina | 280 |
| Administración de Empresas | 420 |
| Derecho | 310 |
| Psicología | 190 |

Con barras horizontales, los nombres largos son más fáciles de leer.

---

## 📖 Diagrama Circular (de Pastel)

> El **diagrama circular** divide un círculo en sectores, donde cada sector representa una categoría y su **área** es proporcional a su frecuencia.

### 💡 Características:
- El círculo completo = 100% (el total)
- Cada "rebanada" = porcentaje de esa categoría
- Ideal para mostrar **partes de un todo**

### 💡 Fórmula para el ángulo:

$$
\text{Ángulo} = \frac{f}{n} \times 360° = f_r \times 360°
$$

### ⚙️ Ejemplo: Distribución de gastos mensuales

| Categoría | Gasto | % | Ángulo |
|-----------|-------|---|--------|
| Vivienda | $800,000 | 40% | 144° |
| Alimentación | $400,000 | 20% | 72° |
| Transporte | $300,000 | 15% | 54° |
| Servicios | $200,000 | 10% | 36° |
| Otros | $300,000 | 15% | 54° |
| **Total** | $2,000,000 | 100% | 360° |

**Cálculo del ángulo para Vivienda:**
$$
\text{Ángulo} = 0.40 \times 360° = 144°
$$

### 💡 ¿Cuándo usar el diagrama circular?

| ✅ Usar cuando... | ❌ Evitar cuando... |
|-------------------|---------------------|
| Quieres mostrar partes de un todo | Hay más de 6-7 categorías |
| Las proporciones son lo importante | Los valores son muy similares |
| Hay pocas categorías (3-6 ideal) | Quieres comparar valores exactos |
| Suman 100% | Las categorías no son exhaustivas |

### ⚠️ Limitaciones del diagrama circular

- **Difícil comparar valores similares:** ¿35% vs 37%? Difícil de ver
- **Muchas categorías = confusión:** Más de 7 rebanadas es difícil de leer
- **No muestra valores exactos:** Necesitas etiquetas

---

## 📖 Pictogramas

> Un **pictograma** usa símbolos o imágenes para representar cantidades. Cada símbolo representa un valor fijo.

### 💡 Características:
- Muy visual y atractivo
- Fácil de entender para público general
- Común en infografías y reportes

### ⚙️ Ejemplo: Ventas de helados por día

**Escala:** 🍦 = 10 helados

| Día | Ventas | Representación |
|-----|--------|----------------|
| Lunes | 30 | 🍦🍦🍦 |
| Martes | 45 | 🍦🍦🍦🍦½ |
| Miércoles | 50 | 🍦🍦🍦🍦🍦 |
| Jueves | 35 | 🍦🍦🍦½ |
| Viernes | 80 | 🍦🍦🍦🍦🍦🍦🍦🍦 |

### 💡 Reglas del pictograma:

1. **Especificar la escala:** "Cada 🍦 = 10 helados"
2. Usar **el mismo símbolo** para todas las categorías
3. Usar **medio símbolo** para valores intermedios
4. El símbolo debe ser **relevante** al tema

### ⚠️ Cuidado con pictogramas en 3D

Algunos pictogramas usan símbolos más grandes para valores mayores. Esto puede ser **engañoso** porque:
- Si duplicas el tamaño del símbolo, el área se cuadruplica
- La percepción visual exagera las diferencias

**Regla:** Mejor usar **más símbolos** que **símbolos más grandes**.

---

## 💡 ¿Cuál Gráfico Elegir?

| Pregunta | Gráfico recomendado |
|----------|---------------------|
| "¿Cuál categoría es más frecuente?" | Diagrama de barras |
| "¿Qué proporción del total es cada categoría?" | Diagrama circular |
| "¿Cómo comunicar a un público general?" | Pictograma |
| "Hay muchas categorías (> 7)" | Diagrama de barras |
| "Las categorías tienen orden (ordinal)" | Diagrama de barras (ordenado) |

---

## 📖 Errores Comunes a Evitar

### ❌ Error 1: No empezar el eje Y en cero

**Problema:** Exagera visualmente las diferencias

| Categoría | Valor real | Parece que... |
|-----------|------------|---------------|
| A | 100 | Es enorme |
| B | 95 | Es muy pequeño |

Si el eje empieza en 90, la diferencia parece enorme cuando es solo 5%.

### ❌ Error 2: Usar colores sin propósito

- No uses 15 colores diferentes sin razón
- Usa color para destacar, no para confundir
- Considera personas con daltonismo

### ❌ Error 3: Gráficos 3D innecesarios

- Los efectos 3D distorsionan las proporciones
- Una rebanada de pastel "al frente" parece más grande
- Preferir gráficos 2D para precisión

---

## 🔑 Resumen

| Gráfico | Cuándo usarlo | Cuándo evitarlo |
|---------|---------------|-----------------|
| **Barras** | Comparar categorías, muchas categorías | Mostrar partes de un todo |
| **Circular** | Mostrar proporciones, pocas categorías | Más de 7 categorías, valores similares |
| **Pictograma** | Comunicación visual, público general | Datos precisos, análisis técnico |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Una encuesta sobre redes sociales favoritas dio estos resultados:

| Red Social | Usuarios |
|------------|----------|
| TikTok | 150 |
| Instagram | 120 |
| YouTube | 100 |
| Facebook | 50 |
| Twitter | 30 |
| Otras | 50 |
| **Total** | **500** |

a) ¿Qué tipo de gráfico usarías para comparar las redes?
b) ¿Qué tipo de gráfico usarías para mostrar qué proporción usa cada red?
c) Calcula el ángulo que tendría TikTok en un diagrama circular.

<details>
<summary>Ver solución</summary>

a) **Diagrama de barras** - Ideal para comparar categorías visualmente

b) **Diagrama circular** - Muestra cada red como proporción del total

c) **Ángulo de TikTok:**
$$f_r = \frac{150}{500} = 0.30 = 30\%$$
$$\text{Ángulo} = 0.30 \times 360° = 108°$$

</details>

### Ejercicio 2
Explica por qué un diagrama circular NO sería adecuado para representar:

"Los géneros musicales favoritos de una clase donde cada estudiante podía elegir hasta 3 géneros"

<details>
<summary>Ver solución</summary>

El diagrama circular **NO funcionaría** porque:

1. **Los porcentajes no suman 100%:** Si cada estudiante elige 3 géneros, los porcentajes sumarán más del 100%.

2. **No son partes de un todo:** El círculo representa "el total", pero aquí un estudiante está contado en múltiples categorías.

3. **Ejemplo:** Si 80% eligió reggaetón, 60% eligió pop y 50% eligió rock, ¿cuánto sería el círculo? 80 + 60 + 50 = 190%, ¡no tiene sentido!

**Mejor opción:** Diagrama de barras, donde cada barra puede exceder y las barras no necesitan sumar ningún total específico.

</details>

### Ejercicio 3
Una empresa tiene empleados en 4 departamentos:

| Departamento | Empleados |
|--------------|-----------|
| Ventas | 48 |
| Producción | 72 |
| Administración | 24 |
| Logística | 36 |

Calcula el ángulo para cada departamento en un diagrama circular.

<details>
<summary>Ver solución</summary>

**Total:** $48 + 72 + 24 + 36 = 180$ empleados

| Departamento | f | $f_r$ | Ángulo |
|--------------|---|-------|--------|
| Ventas | 48 | $\frac{48}{180} = 0.267$ | $0.267 \times 360° = 96°$ |
| Producción | 72 | $\frac{72}{180} = 0.400$ | $0.400 \times 360° = 144°$ |
| Administración | 24 | $\frac{24}{180} = 0.133$ | $0.133 \times 360° = 48°$ |
| Logística | 36 | $\frac{36}{180} = 0.200$ | $0.200 \times 360° = 72°$ |
| **Total** | 180 | 1.000 | 360° |

**Verificación:** $96 + 144 + 48 + 72 = 360°$ ✓

</details>

### Ejercicio 4
Crea un pictograma para representar los libros leídos por 5 amigos, usando la escala: 📚 = 4 libros

| Persona | Libros leídos |
|---------|---------------|
| Ana | 12 |
| Luis | 8 |
| María | 16 |
| Carlos | 6 |
| Sofía | 10 |

<details>
<summary>Ver solución</summary>

**Escala:** 📚 = 4 libros

| Persona | Libros | Pictograma |
|---------|--------|------------|
| Ana | 12 | 📚📚📚 |
| Luis | 8 | 📚📚 |
| María | 16 | 📚📚📚📚 |
| Carlos | 6 | 📚½ (1.5 símbolos) |
| Sofía | 10 | 📚📚½ (2.5 símbolos) |

**Nota:** Carlos leyó 6 libros = $\frac{6}{4} = 1.5$ símbolos
Sofía leyó 10 libros = $\frac{10}{4} = 2.5$ símbolos

</details>
