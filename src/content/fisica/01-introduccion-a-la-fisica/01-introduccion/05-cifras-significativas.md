# 🔢 **Cifras significativas**

Las cifras significativas indican la precisión real de una medición y nos ayudan a comunicar resultados confiables.

---

## 🎯 ¿Qué vas a aprender?

- Qué son las cifras significativas
- Las reglas para identificarlas
- Cómo aplicarlas en operaciones matemáticas
- Las reglas de redondeo

---

## ⚙️ **¿Qué son las cifras significativas?**

Las **cifras significativas** son los **dígitos confiables** de una medición,  
más **uno adicional estimado** que indica la **precisión del instrumento** utilizado.

> En otras palabras, son los **números que realmente aportan información** sobre la medición.

Si una regla graduada en milímetros marca:

$$
12.34\,\mathrm{cm}
$$

Las cifras significativas son **1, 2, 3 y 4**, porque el último dígito (4) es una **estimación**.

---

## 🧮 **¿Por qué son importantes?**

- Indican **cuánta confianza** tenemos en una medición.  
- Permiten **reportar resultados con la precisión adecuada**.  
- Evitan escribir **más dígitos de los que el instrumento puede justificar**.  

---

## 🧩 **Reglas para identificar cifras significativas**

1. **Todos los dígitos distintos de cero** son significativos.  
   ↳ Ejemplo: 
   
$$
245 \to \text{3 cifras significativas}
$$

2. **Los ceros entre dígitos distintos de cero** también son significativos.  
   ↳ Ejemplo: 
   
$$
2003 \to \text{4 cifras significativas}
$$

3. **Los ceros a la izquierda** del primer número distinto de cero **no cuentan**.  
   ↳ Ejemplo: 
   
$$
0.0045 \to \text{2 cifras significativas}
$$

4. **Los ceros a la derecha del número decimal** son significativos.  
   ↳ Ejemplo: 
   
$$
3.200 \to \text{4 cifras significativas}
$$

5. **Los ceros al final sin punto decimal** pueden o no ser significativos.  
   ↳ Ejemplo: 
   
$$
1500 \to \text{puede tener 2, 3 o 4 cifras significativas}
$$

(depende del instrumento o si se expresa como $1.50\times10^3$).

---

## 🧠 **Ejemplos prácticos**

| **Número** | **Cifras significativas** | **Notación científica** |
|:-----------|:-------------------------:|:-----------------------:|
| $0.0045$   | 2                         | $4.5\times10^{-3}$      |
| $3200$     | 2 (o 3 si se especifica)  | $3.2\times10^3$         |
| $0.00320$  | 3                         | $3.20\times10^{-3}$     |
| $450.60$   | 5                         | $4.506\times10^2$       |

---

## ➗ **Reglas para operaciones**

### ✖️ **Multiplicación y división**

El resultado debe tener **tantas cifras significativas como el número con menos cifras significativas**.

$$
2.5\times3.42 = 8.6
$$

> (porque $2.5$ tiene 2 cifras significativas)

---

### ➕ **Suma y resta**

El resultado debe conservar **el mismo número de decimales**  
que la medición con **menos decimales**.

$$
12.11 + 0.3 = 12.4
$$

---

## ✂️ **Redondeo**

Al limitar cifras en un resultado:

- Si el primer dígito que se elimina es **menor que 5**, el último se deja igual.  
  ↳ 
  
$$
3.243 \to 3.24
$$

- Si es **mayor o igual que 5**, el último se incrementa en uno.  
  ↳ 
  
$$
3.246 \to 3.25
$$

---

## 🎓 **Consejo de laboratorio**

> No importa cuántos decimales tenga tu calculadora:  
> **el número de cifras significativas depende del instrumento**,  
> no de la operación matemática.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
**¿Cuántas cifras significativas tienen los siguientes números?**

a) $0.00560$

b) $4050$

c) $7.00$

d) $123.45$

<details>
<summary>Ver solución</summary>

**Razonamiento:**

a) **3** cifras significativas ($5, 6, 0$ al final es significativo).

b) **3** cifras significativas (el $0$ al final es ambiguo, pero mínimo son $4, 0, 5$).

c) **3** cifras significativas ($7, 0, 0$).

d) **5** cifras significativas ($1, 2, 3, 4, 5$).

</details>

---

### Ejercicio 2
**Realiza la siguiente operación y expresa el resultado con las cifras significativas correctas:**

$$
4.52 \times 2.1 = ?
$$

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
4.52 \times 2.1 = 9.492
$$

Pero como $2.1$ tiene **2 cifras significativas**, el resultado debe tener 2:

$$
\boxed{9.5}
$$

</details>

---

### Ejercicio 3
**Realiza la siguiente operación y expresa el resultado correctamente:**

$$
15.23 + 0.7 = ?
$$

<details>
<summary>Ver solución</summary>

**Razonamiento:**

$$
15.23 + 0.7 = 15.93
$$

Pero como $0.7$ tiene **1 decimal**, el resultado debe tener 1 decimal:

$$
\boxed{15.9}
$$

</details>

---

### Ejercicio 4
**Un estudiante mide un objeto con una regla graduada en centímetros y reporta: "La longitud es 12.345 cm". ¿Por qué esto es incorrecto?**

<details>
<summary>Ver solución</summary>

**Razonamiento:**

Es incorrecto porque una regla graduada en centímetros solo puede estimar hasta **décimas de centímetro** (milímetros). El valor correcto debería ser como máximo **12.3 cm** o **12.35 cm** si se estima el último dígito.

Reportar 12.345 cm implica una precisión de **centésimas de milímetro**, que es imposible de obtener con una regla común.

</details>

---

### Ejercicio 5
**Redondea los siguientes números a 3 cifras significativas:**

a) $0.0045678$

b) $12345$

c) $9.9951$

<details>
<summary>Ver solución</summary>

**Razonamiento:**

a) 

$$
0.00457 \to 4.57 \times 10^{-3}
$$

b) 

$$
12300 \to 1.23 \times 10^{4}
$$

c) 

$$
10.0
$$

(el $9.9951$ se redondea a $10.0$).

</details>

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Cifras significativas** | Dígitos confiables de una medición |
| **Regla clave** | Los ceros a la izquierda NO cuentan |
| **× y ÷** | Resultado con el menor número de cifras significativas |
| **+ y −** | Resultado con el menor número de decimales |
| **Redondeo** | < 5 se deja, ≥ 5 se aumenta |

> Las **cifras significativas** expresan la **precisión real** de una medición,  
> nos ayudan a **evitar falsos niveles de exactitud**  
> y son esenciales para **comunicar resultados confiables** en física y otras ciencias experimentales.

---
