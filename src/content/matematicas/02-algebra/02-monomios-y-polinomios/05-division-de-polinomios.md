# **División de Polinomios**

Dividir un polinomio es como repartir una herencia o un gran cargamento de suministros entre varias personas. Si tienes un total de recursos (el dividendo) y quieres saber cuánto le toca a cada uno (el cociente) y cuánto sobra (el resto), la división de polinomios es tu herramienta ideal. En esta lección, aprenderemos desde el reparto más simple hasta el método de Ruffini, un "atajo" matemático sorprendente.

---

## 🎯 **¿Qué vas a aprender?**

*   A dividir un polinomio entre un monomio simplificando término a término.
*   La **división larga** para realizar divisiones de polinomios.
*   Cómo usar la **Regla de Ruffini** para dividir más rápido.
*   A predecir el sobrante de una división usando el Teorema del Resto.

---

## 🔄 **La Fórmula de Verificación**

¿Recuerdas la división de números que aprendiste en primaria? Por ejemplo, si divides $17 \div 5$:

| Dividendo | Divisor | Cociente | Resto |
| :---: | :---: | :---: | :---: |
| 17 | 5 | 3 | 2 |

Y la prueba era: $5 \times 3 + 2 = 17$ ✓

**¡Con polinomios funciona exactamente igual!** La fórmula de verificación es:

$$
\boxed{P(x) = D(x) \cdot C(x) + R(x)}
$$

Donde:
- $P(x)$ = **Dividendo** (el polinomio que dividimos)
- $D(x)$ = **Divisor** (el polinomio entre el que dividimos)
- $C(x)$ = **Cociente** (el resultado)
- $R(x)$ = **Resto** o residuo (lo que sobra)

> 💡 **Tip:** Siempre puedes verificar tu división multiplicando $D(x) \cdot C(x)$ y sumándole $R(x)$. Si obtienes $P(x)$, ¡tu división está correcta!

---

## 📦 **División entre un Monomio**

Esta es la forma más sencilla de dividir. Imagina que tienes un paquete con varios artículos y quieres repartirlos entre un grupo único.

**La Regla:** Divide cada término del polinomio entre el monomio de abajo por separado.
1.  Divide los coeficientes (números).
2.  Resta los exponentes de las letras iguales.

### **Ejemplo: El Reparto Simple**
Calcula: $\frac{6x^3 + 9x^2 - 3x}{3x}$

**Paso a paso:**
1.  $\frac{6x^3}{3x} = 2x^2$
2.  $\frac{9x^2}{3x} = 3x$
3.  $\frac{-3x}{3x} = -1$

**Resultado:** $\boxed{2x^2 + 3x - 1}$

---

## 🏚️ **División Larga**

Cuando el divisor tiene más de un término (como $x+2$), usamos un proceso similar al que aprendiste en primaria con números grandes.

**Los Pasos Clave:**
1.  **Dividir:** El primer término de adentro entre el primero de afuera.
2.  **Multiplicar:** Ese resultado por todo el divisor.
3.  **Restar:** Cambia los signos del resultado y súmalo abajo.
4.  **Repetir:** Baja el siguiente término y vuelve a empezar.

## ⚙️ **Ejemplos Resueltos**

---

### 🏚️ **1. División Larga**

**Ejemplo 1: El Caso Básico**
Divide $(x^2 + 5x + 6)$ entre $(x + 2)$.
*   **Razonamiento:** Buscamos qué multiplicar por $x$ para obtener $x^2$.
*   **Proceso:** $x(x+2) = x^2+2x$. Restamos y queda $3x+6$. Luego $3(x+2)=3x+6$.
*   **Resultado:** $\boxed{x + 3}$ (Residuo: 0).
![division-tradicional-de-polinomios](https://cdn.ediprofe.com/img/matematicas/bcwq-division-tradicional-de-polinomios.webp)

**Ejemplo 2: Con Residuo Polinómico**
Divide $(2x^3 - 3x^2 + 4x - 5)$ entre $(x^2 + 1)$.
*   **Razonamiento:** Dividimos hasta que el grado del resto sea menor al del divisor (grado 2).
*   **Resultado:** Cociente $\boxed{2x - 5}$, Residuo $\boxed{2x}$.

**Ejemplo 3: Divisor con Coeficiente**
Divide $(6x^3 + x^2 - 10x + 4)$ entre $(2x - 1)$.
*   **Proceso:** $6x^3 \div 2x = 3x^2$. Multiplicamos y restamos. Seguimos con $4x^2 \div 2x = 2x$ y finalmente $-8x \div 2x = -4$.
*   **Resultado:** $\boxed{3x^2 + 2x - 4}$

**Ejemplo 4: Dividendo con "Huecos"**
Divide $(x^4 - 1)$ entre $(x^2 - 1)$.
*   **Razonamiento:** Rellenamos: $(x^4 + 0x^3 + 0x^2 + 0x - 1)$.
*   **Proceso:** $x^4 \div x^2 = x^2$. Multiplicamos $(x^4 - x^2)$, restamos y queda $x^2 - 1$. Luego $x^2 \div x^2 = 1$.
*   **Resultado:** $\boxed{x^2 + 1}$

**Ejemplo 5: División de Grado 3 entre Grado 1**
Divide $(x^3 + 2x^2 - 5x - 6)$ entre $(x + 1)$.
*   **Resultado:** $\boxed{x^2 + x - 6}$

---

### ⚡ **2. Regla de Ruffini**

**Ejemplo 1: El Algoritmo Paso a Paso**
Divide $(x^2 - 5x + 6)$ por $(x - 3)$.

**¿Cómo se hace? Sigue este proceso:**
1.  **Alistar los Coeficientes:** Escribimos los números del dividendo en fila: $1$, $-5$ y $6$.
2.  **El "Número Mágico":** Del divisor $(x-3)$, sacamos el $3$ (siempre cambiamos el signo) y lo ponemos a la izquierda de la galera.
3.  **Primer Paso:** Bajamos el primer coeficiente ($1$) directo al resultado.
4.  **Multiplicar y Sumar:** 
    *   Multiplicamos ese $1$ por el $3$ de la izquierda ($1 \cdot 3 = 3$). Colocamos el resultando bajo el $-5$.
    *   Sumamos la columna: $-5 + 3 = -2$.
    *   Multiplicamos el nuevo resultado por el $3$ ($ -2 \cdot 3 = -6$). Colocamos el resultado bajo el $6$.
    *   Sumamos la última columna: $6 - 6 = 0$.

**Visualización del Cálculo:**
$$
\begin{array}{c|rrr}
3 & 1 & -5 & 6 \\
  &   & 3 & -6 \\
\hline
  & 1 & -2 & \boxed{0}
\end{array}
$$
*   **Interpretación:** El último número ($\boxed{0}$) es el **residuo**. Los otros números ($1, -2$) son los coeficientes del cociente. Como el original era grado 2, el resultado es grado 1: $\boxed{x - 2}$.
![ejemplo-ruffini](https://cdn.ediprofe.com/img/matematicas/4rd3-ejemplo-ruffini.webp)

**Ejemplo 2: Completando el Polinomio**
Divide $(x^3 - 8)$ entre $(x - 2)$.
*   **Cálculo:**
$$
\begin{array}{c|rrrr}
2 & 1 & 0 & 0 & -8 \\
  &   & 2 & 4 & 8 \\
\hline
  & 1 & 2 & 4 & \boxed{0}
\end{array}
$$
*   **Resultado:** $\boxed{x^2 + 2x + 4}$

**Ejemplo 3: Resultado con Residuo**
Divide $(3x^3 - 5x^2 + 7)$ entre $(x - 2)$.
*   **Cálculo:**
$$
\begin{array}{c|rrrr}
2 & 3 & -5 & 0 & 7 \\
  &   & 6 & 2 & 4 \\
\hline
  & 3 & 1 & 2 & \boxed{11}
\end{array}
$$
*   **Resultado:** Cociente $\boxed{3x^2 + x + 2}$, Residuo $\boxed{11}$.

**Ejemplo 4: Divisor con suma $(x+a)$**
Divide $(x^4 - 3x^2 - 4)$ entre $(x + 2)$.
*   **Cálculo:** Coeficientes $(1, 0, -3, 0, -4)$ y usamos $a = -2$.
$$
\begin{array}{c|rrrrr}
-2 & 1 & 0 & -3 & 0 & -4 \\
   &   & -2 & 4 & -2 & 4 \\
\hline
   & 1 & -2 & 1 & -2 & \boxed{0}
\end{array}
$$
*   **Resultado:** $\boxed{x^3 - 2x^2 + x - 2}$

**Ejemplo 5: Coeficientes mayores**
Divide $(2x^3 + 5x^2 - x - 6)$ entre $(x + 3)$.
*   **Cálculo:** Use $a = -3$.
$$
\begin{array}{c|rrrr}
-3 & 2 & 5 & -1 & -6 \\
   &   & -6 & 3 & -6 \\
\hline
   & 2 & -1 & 2 & \boxed{-12}
\end{array}
$$
*   **Resultado:** Cociente $\boxed{2x^2 - x + 2}$, Residuo $\boxed{-12}$.

---

### 🎯 **3. Teorema del Resto**

**Ejemplo 1: Evaluación Directa**
Halla el resto de $(x^3 - 2x + 5) \div (x - 2)$.
*   **Cálculo:** Evalúa $P(2) = 2^3 - 2(2) + 5 = 8 - 4 + 5 = 9$.
*   **Resultado:** $\boxed{\text{Resto} = 9}$

**Ejemplo 2: Encontrar una incógnita**
Halla $k$ para que $(x^2 + kx + 8) \div (x - 2)$ sea exacta.
*   **Cálculo:** $P(2) = 2^2 + k(2) + 8 = 0 \to 12 + 2k = 0$.
*   **Resultado:** $\boxed{k = -6}$

**Ejemplo 3: Potencias Grandes**
Calcula el resto de $(x^{50} - 1) \div (x + 1)$.
*   **Cálculo:** Evaluamos en $x = -1$. $P(-1) = (-1)^{50} - 1 = 1 - 1 = 0$.
*   **Resultado:** $\boxed{\text{Resto} = 0}$ (Es una división exacta).

---

## 📝 **Ponte a Prueba**

### **Ejercicio 1**
Divide: $\frac{10x^4 - 20x^2}{5x}$.

<details>
<summary>Ver solución</summary>

**Datos:** Polinomio entre monomio.
**Razonamiento:** Dividimos cada parte: $10/5 = 2$, $x^{4-1}=3$. Luego $-20/5=-4$, $x^{2-1}=1$.
**Resultado:** $\boxed{2x^3 - 4x}$

</details>

### **Ejercicio 2**
¿Cuál es el cociente de $(x^2 + 7x + 10) \div (x + 2)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Usando Ruffini con $a = -2$: Coeficientes $(1, 7, 10)$. Bajamos $1 \to 1(-2)=-2 \to 7-2=5 \to 5(-2)=-10 \to 10-10=0$.
**Resultado:** $\boxed{x + 5}$

</details>

### **Ejercicio 3**
Si dividimos $P(x)$ entre $(x - a)$, ¿cómo se llama el valor $P(a)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Según el Teorema del Resto, el valor numérico del polinomio evaluado en $a$ es igual al residuo de la división.
**Resultado:** $\boxed{\text{Resto o Residuo}}$

</details>

### **Ejercicio 4**
Calcula el resto de $(x^{10} - 1) \div (x - 1)$ usando el Teorema del Resto.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Sustituimos $x=1$ en el polinomio: $(1)^{10} - 1 = 1 - 1 = 0$.
**Resultado:** $\boxed{0}$

</details>

### **Ejercicio 5**
Divide usando Ruffini: $(x^2 - x - 6) \div (x + 2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Usamos $a = -2$. Coeficientes $(1, -1, -6)$. Bajamos $1 \to 1(-2)=-2 \to -1-2=-3 \to -3(-2)=6 \to -6+6=0$.
**Resultado:** $\boxed{x - 3}$

</details>

### **Ejercicio 6**
Simplifica: $\frac{4a^3b^2 - 2a^2b^2}{2a^2b}$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Dividimos términos: $(4/2)a(3-2)b(2-1) = 2ab$. Luego $-(2/2)a(2-2)b(2-1) = -b$.
**Resultado:** $\boxed{2ab - b}$

</details>

### **Ejercicio 7**
En una división larga, ¿cuándo dejamos de dividir?

<details>
<summary>Ver solución</summary>

**Razonamiento:** El proceso se detiene cuando el grado del resto es estrictamente menor que el grado del divisor.
**Resultado:** $\boxed{\text{Grado del Resto } < \text{ Grado del Divisor}}$

</details>

### **Ejercicio 8**
Completa el dividendo para Ruffini si es $x^3 + 5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Debemos poner ceros en los términos de $x^2$ y $x$.
**Resultado:** $\boxed{x^3 + 0x^2 + 0x + 5}$

</details>

### **Ejercicio 9**
Calcula el cociente de $(2x^2 - 8) \div (x - 2)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Ruffini con $a=2$: Coeficientes $(2, 0, -8)$. Bajamos $2 \to 2(2)=4 \to 0+4=4 \to 4(2)=8 \to -8+8=0$.
**Resultado:** $\boxed{2x + 4}$

</details>

### **Ejercicio 10**
Si el resto de una división es $0$, ¿qué podemos decir del divisor?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Una división con resto cero significa que la operación es exacta.
**Resultado:** $\boxed{\text{Es un factor o divisor exacto}}$

</details>

### **Ejercicio 11**
Halla el resto de $(x^2 + 4x + 7) \div (x + 1)$ usando Ruffini.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Coeficientes $(1, 4, 7)$ con $a = -1$.
**Cálculo:** $1 \to 1(-1)=-1 \to 4-1=3 \to 3(-1)=-3 \to 7-3=4$.
**Resultado:** $\boxed{\text{Resto} = 4}$

</details>

### **Ejercicio 12**
Divide $(x^3 - 4x^2 + 5x - 8)$ entre $(x - 2)$ e indica el residuo.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Usamos Ruffini con $a = 2$. Coeficientes: $(1, -4, 5, -8)$.
**Cálculo:** $1 \to 1(2)=2 \to -4+2=-2 \to -2(2)=-4 \to 5-4=1 \to 1(2)=2 \to -8+2=-6$.
**Resultado:** $\boxed{\text{Resto} = -6}$

</details>

### **Ejercicio 13**
Calcula el cociente de $(x^4 + 3x^2 - 4) \div (x^2 + 1)$ por división larga.

<details>
<summary>Ver solución</summary>

**Razonamiento:** 
1. $x^4 \div x^2 = x^2$.
2. Multiplicamos y restamos $\to 2x^2 - 4$.
3. $2x^2 \div x^2 = 2$.
4. Multiplicamos y restamos $\to -6$.
**Resultado:** $\boxed{\text{Cociente } = x^2 + 2}$

</details>

### **Ejercicio 14**
Sin dividir, ¿cuál es el resto de $(x^4 + x^3 + x^2 + x + 1) \div (x + 1)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Teorema del Resto con $x = -1$.
**Cálculo:** $(-1)^4 + (-1)^3 + (-1)^2 + (-1) + 1 = 1 - 1 + 1 - 1 + 1 = 1$.
**Resultado:** $\boxed{1}$

</details>

### **Ejercicio 15**
Calcula el cociente de $(2x^2 + 5x - 3) \div (2x - 1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Por división larga:
1. $2x^2 \div 2x = x$.
2. Multiplicamos $(2x-1)x = 2x^2 - x$. Restamos $\to 6x - 3$.
3. $6x \div 2x = 3$.
4. Multiplicamos $(2x-1)3 = 6x - 3$. Restamos $\to 0$.
**Resultado:** $\boxed{x + 3}$

</details>

### **Ejercicio 16**
Halla $m$ para que $(x^3 - mx + 6) \div (x - 2)$ tenga resto $0$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** $P(2) = 0$.
**Cálculo:** $(2)^3 - m(2) + 6 = 0 \to 8 - 2m + 6 = 0 \to 14 = 2m \to m = 7$.
**Resultado:** $\boxed{m = 7}$

</details>

### **Ejercicio 17**
Calcula el residuo de $(3x^3 + 5x^2 - 1) \div (x^2 + x)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** División larga.
1. $3x^3 \div x^2 = 3x$. Multiplicamos y restamos $\to 2x^2 - 1$.
2. $2x^2 \div x^2 = 2$. Multiplicamos y restamos $\to -2x - 1$.
**Resultado:** $\boxed{-2x - 1}$

</details>

### **Ejercicio 18**
¿Cuál es el cociente de $(x^3 - 1) \div (x - 1)$?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Ruffini con $a=1$ y coeficientes $(1, 0, 0, -1)$.
**Cálculo:** $1 \to 1(1)=1 \to 0+1=1 \to 1(1)=1 \to 0+1=1 \to 1(1)=1 \to -1+1=0$.
**Resultado:** $\boxed{x^2 + x + 1}$

</details>

### **Ejercicio 19**
Calcula el resto de $(x^2 + 1) \div (x + 1)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:** Teorema del Resto con $x = -1$.
**Cálculo:** $(-1)^2 + 1 = 1 + 1 = 2$.
**Resultado:** $\boxed{2}$

</details>

### **Ejercicio 20**
En la división $P(x) \div D(x)$, si el residuo no es cero, ¿cuál es su grado máximo?

<details>
<summary>Ver solución</summary>

**Razonamiento:** Por definición, el grado del resto siempre es menor que el grado del divisor.
**Resultado:** $\boxed{\text{Grado del Divisor} - 1}$

</details>

---

## 🔑 **Resumen**

### ¿Qué método uso?

| Si el divisor es... | Usa este método | ¿Por qué? |
| :--- | :--- | :--- |
| Un **monomio** ($3x$, $5x^2$) | División por monomio | ⚡ Divide término a término |
| De la forma $(x \pm a)$ | **Ruffini** | 🔢 Solo trabajas con números |
| Cualquier otro polinomio | División larga | 📐 Funciona siempre |
| Solo necesitas el **resto** | Teorema del resto | 🎯 Evalúa $P(a)$ sin dividir |

### Fórmula de verificación

$$
\boxed{P(x) = D(x) \cdot C(x) + R(x)}
$$

### Tips importantes

- El **cociente** $C(x)$ siempre tiene un grado **menor** que el dividendo $P(x)$.
- Si el **resto = 0**, el divisor es un **factor** del dividendo.
- En Ruffini: si el divisor es $(x - 3)$, usa $+3$; si es $(x + 2)$, usa $-2$.
- Ordena siempre el polinomio de **mayor a menor grado** antes de dividir.

> 💡 **Conclusión:** La división de polinomios nos permite simplificar estructuras matemáticas complejas. Ya sea usando el método largo o el atajo de Ruffini, lo importante es mantener el orden de los grados para que cada pieza encaje en su lugar.
