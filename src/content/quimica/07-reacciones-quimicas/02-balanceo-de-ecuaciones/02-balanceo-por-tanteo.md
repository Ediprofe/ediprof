# Balanceo por Tanteo

El **balanceo por tanteo** (también llamado "por inspección" o "ensayo y error") es el método más básico y práctico para balancear ecuaciones químicas sencillas. Consiste en ajustar los coeficientes hasta que los átomos se conserven.

---

## 🎯 ¿Qué vas a aprender?

- El método paso a paso para balancear por tanteo
- Estrategias para hacer el proceso más eficiente
- Ejercicios progresivos de balanceo
- Errores comunes y cómo evitarlos

---

## 📊 Los 5 Pasos del Método

| Paso | Acción |
|------|--------|
| 1 | Escribir la ecuación sin balancear |
| 2 | Contar átomos de cada elemento |
| 3 | Empezar por el elemento más complejo |
| 4 | Ajustar coeficientes hasta equilibrar |
| 5 | Verificar el balance final |

---

## 📖 Reglas Importantes

### 💡 Lo que SÍ puedes hacer:

- Cambiar los **coeficientes** (números delante de las fórmulas)
- Usar números enteros (evitar fracciones al final)

### 💡 Lo que NO puedes hacer:

- Cambiar los **subíndices** de las fórmulas
- Añadir o quitar sustancias

### 💡 Consejos:

1. Empieza por los elementos que aparecen en **menos lugares**
2. Deja el **hidrógeno** y **oxígeno** para el final
3. Si un elemento aparece en un solo reactivo y un solo producto, empieza por ahí

---

## 📖 Ejemplo 1: Reacción Simple

### Ecuación: H₂ + O₂ → H₂O

**Paso 1:** Ecuación sin balancear
$$
\text{H}_2 + \text{O}_2 \rightarrow \text{H}_2\text{O}
$$

**Paso 2:** Contar átomos

| Elemento | Reactivos | Productos |
|----------|-----------|-----------|
| H | 2 | 2 ✓ |
| O | 2 | 1 ✗ |

**Paso 3-4:** El O no está balanceado. Ponemos 2 delante del H₂O:

$$
\text{H}_2 + \text{O}_2 \rightarrow 2\text{H}_2\text{O}
$$

| Elemento | Reactivos | Productos |
|----------|-----------|-----------|
| H | 2 | 4 ✗ |
| O | 2 | 2 ✓ |

Ahora H no está balanceado. Ponemos 2 delante del H₂:

$$
2\text{H}_2 + \text{O}_2 \rightarrow 2\text{H}_2\text{O}
$$

**Paso 5:** Verificar

| Elemento | Reactivos | Productos |
|----------|-----------|-----------|
| H | 4 | 4 ✓ |
| O | 2 | 2 ✓ |

**Ecuación balanceada:**
$$
\boxed{2\text{H}_2 + \text{O}_2 \rightarrow 2\text{H}_2\text{O}}
$$

---

## 📖 Ejemplo 2: Tres Elementos

### Ecuación: Fe + O₂ → Fe₂O₃

**Paso 1-2:** Contar átomos

| Elemento | Reactivos | Productos |
|----------|-----------|-----------|
| Fe | 1 | 2 ✗ |
| O | 2 | 3 ✗ |

**Paso 3-4:** Balancear Fe primero:

$$
2\text{Fe} + \text{O}_2 \rightarrow \text{Fe}_2\text{O}_3
$$

| Fe | 2 | 2 ✓ |
| O | 2 | 3 ✗ |

Para O, necesitamos MCM(2,3) = 6:
- Ponemos 3 en O₂: 3×2 = 6 oxígenos
- Ponemos 2 en Fe₂O₃: 2×3 = 6 oxígenos

$$
2\text{Fe} + 3\text{O}_2 \rightarrow 2\text{Fe}_2\text{O}_3
$$

Verificar Fe: 2 Fe a la izquierda, 2×2 = 4 Fe a la derecha ✗

Corregir:
$$
4\text{Fe} + 3\text{O}_2 \rightarrow 2\text{Fe}_2\text{O}_3
$$

**Verificación final:**

| Elemento | Reactivos | Productos |
|----------|-----------|-----------|
| Fe | 4 | 2×2 = 4 ✓ |
| O | 3×2 = 6 | 2×3 = 6 ✓ |

**Ecuación balanceada:**
$$
\boxed{4\text{Fe} + 3\text{O}_2 \rightarrow 2\text{Fe}_2\text{O}_3}
$$

---

## 📖 Ejemplo 3: Combustión

### Ecuación: C₃H₈ + O₂ → CO₂ + H₂O

**Paso 1-2:** Contar átomos

| Elemento | Reactivos | Productos |
|----------|-----------|-----------|
| C | 3 | 1 |
| H | 8 | 2 |
| O | 2 | 3 |

**Paso 3-4:** Empezar por C (solo aparece una vez en cada lado):

$$
\text{C}_3\text{H}_8 + \text{O}_2 \rightarrow 3\text{CO}_2 + \text{H}_2\text{O}
$$

Ahora H:
$$
\text{C}_3\text{H}_8 + \text{O}_2 \rightarrow 3\text{CO}_2 + 4\text{H}_2\text{O}
$$

Ahora O: tenemos 3×2 + 4×1 = 10 oxígenos en productos
$$
\text{C}_3\text{H}_8 + 5\text{O}_2 \rightarrow 3\text{CO}_2 + 4\text{H}_2\text{O}
$$

**Verificación:**

| Elemento | Reactivos | Productos |
|----------|-----------|-----------|
| C | 3 | 3 ✓ |
| H | 8 | 8 ✓ |
| O | 10 | 6+4=10 ✓ |

**Ecuación balanceada:**
$$
\boxed{\text{C}_3\text{H}_8 + 5\text{O}_2 \rightarrow 3\text{CO}_2 + 4\text{H}_2\text{O}}
$$

---

## 📖 Trucos y Estrategias

### 💡 1. Elementos únicos primero:

Si un elemento aparece solo en un reactivo y un producto, empieza ahí.

### 💡 2. Deja O y H para el final:

Suelen aparecer en múltiples sustancias, son más fáciles de ajustar al final.

### 💡 3. Fracciones temporales:

Puedes usar ½, ³⁄₂, etc. temporalmente y multiplicar todo al final.

### 💡 4. Verifica siempre:

Un error pequeño invalida todo el balance.

---

## 🔑 Resumen del Método

| Paso | Acción |
|------|--------|
| 1 | Escribe la ecuación |
| 2 | Cuenta cada elemento |
| 3 | Balancea elementos que aparecen una vez primero |
| 4 | Ajusta H y O al final |
| 5 | Verifica que todos los elementos estén balanceados |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Balancea: N₂ + H₂ → NH₃

<details>
<summary>Ver solución</summary>

| Elemento | Sin balancear |
|----------|---------------|
| N | 2 vs 1 |
| H | 2 vs 3 |

Ponemos 2 en NH₃:
$$
\text{N}_2 + \text{H}_2 \rightarrow 2\text{NH}_3
$$

| N | 2 | 2 ✓ |
| H | 2 | 6 ✗ |

Ponemos 3 en H₂:
$$
\text{N}_2 + 3\text{H}_2 \rightarrow 2\text{NH}_3
$$

**Verificación:** N: 2=2 ✓, H: 6=6 ✓

$$
\boxed{\text{N}_2 + 3\text{H}_2 \rightarrow 2\text{NH}_3}
$$

</details>

### Ejercicio 2
Balancea: Al + HCl → AlCl₃ + H₂

<details>
<summary>Ver solución</summary>

Empezamos con Cl (único elemento complejo):

Necesitamos 3 Cl en productos, así que:
$$
\text{Al} + 3\text{HCl} \rightarrow \text{AlCl}_3 + \text{H}_2
$$

| Elemento | Reactivos | Productos |
|----------|-----------|-----------|
| Al | 1 | 1 ✓ |
| H | 3 | 2 ✗ |
| Cl | 3 | 3 ✓ |

Para H, usamos 6 (MCM de 2 y 3):
$$
2\text{Al} + 6\text{HCl} \rightarrow 2\text{AlCl}_3 + 3\text{H}_2
$$

**Verificación:** Al: 2=2 ✓, H: 6=6 ✓, Cl: 6=6 ✓

$$
\boxed{2\text{Al} + 6\text{HCl} \rightarrow 2\text{AlCl}_3 + 3\text{H}_2}
$$

</details>

### Ejercicio 3
Balancea: Ca(OH)₂ + HCl → CaCl₂ + H₂O

<details>
<summary>Ver solución</summary>

| Elemento | Sin balancear |
|----------|---------------|
| Ca | 1 vs 1 ✓ |
| O | 2 vs 1 ✗ |
| H | 2+1=3 vs 2 ✗ |
| Cl | 1 vs 2 ✗ |

Ponemos 2 en HCl y 2 en H₂O:
$$
\text{Ca(OH)}_2 + 2\text{HCl} \rightarrow \text{CaCl}_2 + 2\text{H}_2\text{O}
$$

**Verificación:**
- Ca: 1 = 1 ✓
- O: 2 = 2 ✓
- H: 2+2=4 = 4 ✓
- Cl: 2 = 2 ✓

$$
\boxed{\text{Ca(OH)}_2 + 2\text{HCl} \rightarrow \text{CaCl}_2 + 2\text{H}_2\text{O}}
$$

</details>

### Ejercicio 4
Balancea: C₂H₆ + O₂ → CO₂ + H₂O

<details>
<summary>Ver solución</summary>

**Paso 1:** C primero
$$
\text{C}_2\text{H}_6 + \text{O}_2 \rightarrow 2\text{CO}_2 + \text{H}_2\text{O}
$$

**Paso 2:** H
$$
\text{C}_2\text{H}_6 + \text{O}_2 \rightarrow 2\text{CO}_2 + 3\text{H}_2\text{O}
$$

**Paso 3:** O (4 + 3 = 7 oxígenos en productos)
$$
\text{C}_2\text{H}_6 + \frac{7}{2}\text{O}_2 \rightarrow 2\text{CO}_2 + 3\text{H}_2\text{O}
$$

**Paso 4:** Multiplicar todo por 2 para eliminar la fracción:
$$
2\text{C}_2\text{H}_6 + 7\text{O}_2 \rightarrow 4\text{CO}_2 + 6\text{H}_2\text{O}
$$

**Verificación:** C: 4=4 ✓, H: 12=12 ✓, O: 14=14 ✓

$$
\boxed{2\text{C}_2\text{H}_6 + 7\text{O}_2 \rightarrow 4\text{CO}_2 + 6\text{H}_2\text{O}}
$$

</details>
