# **División de Polinomios**

Dividir un polinomio es como repartir una herencia o un gran cargamento de suministros entre varias personas. Si tienes un total de recursos (el dividendo) y quieres saber cuánto le toca a cada uno (el cociente) y cuánto sobra (el resto), la división de polinomios es tu herramienta ideal. En esta lección, aprenderemos desde el reparto más simple hasta el método de Ruffini, un "atajo" matemático sorprendente.

---

## 🎯 **¿Qué vas a aprender?**

*   A dividir un polinomio entre un monomio simplificando término a término.
*   El método de la "casita" para realizar divisiones largas de polinomios.
*   Cómo usar la **Regla de Ruffini** para dividir más rápido.
*   A predecir el sobrante de una división usando el Teorema del Resto.

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

## 🏚️ **División Larga (Método de la Casita)**

Cuando el divisor tiene más de un término (como $x+2$), usamos un proceso similar al que aprendiste en primaria con números grandes.

**Los Pasos Clave:**
1.  **Dividir:** El primer término de adentro entre el primero de afuera.
2.  **Multiplicar:** Ese resultado por todo el divisor.
3.  **Restar:** Cambia los signos del resultado y súmalo abajo.
4.  **Repetir:** Baja el siguiente término y vuelve a empezar.

### **Ejemplo: División Paso a Paso**
Divide $(x^2 + 5x + 6)$ entre $(x + 2)$.

**Razonamiento:**
¿Qué le falta a $x$ para ser $x^2$? Le falta otra $x$.
1.  Multiplicamos $x \cdot (x + 2) = x^2 + 2x$.
2.  Restamos (cambiamos signos): $-x^2 - 2x$.
3.  Al sumar queda $3x + 6$.
4.  ¿Qué le falta a $x$ para ser $3x$? Un $+3$.
5.  Multiplicamos $3 \cdot (x + 2) = 3x + 6$, restamos y el residuo es $0$.

**Resultado:** $\boxed{\text{Cociente: } x + 3}$

---

## ⚡ **Regla de Ruffini: El Atajo**

Ruffini es un método "mágico" que solo usa los números (coeficientes) para dividir cuando el divisor es algo simple como $(x - 2)$ o $(x + 3)$.

**Condición:** El divisor debe ser de la forma $(x \pm a)$.

### **Ejemplo: Usando Ruffini**
Divide $(x^2 - 5x + 6)$ por $(x - 3)$.

**Esquema de Ruffini:**
1. Escribimos los coeficientes: $1, -5, 6$.
2. A la izquierda ponemos el $3$ (signo cambiado del divisor).
3. Bajamos el $1$.
4. $1 \cdot 3 = 3$. Lo sumamos al $-5 \to -2$.
5. $-2 \cdot 3 = -6$. Lo sumamos al $6 \to 0$.

**Interpretación:** El resultado es $1x - 2$ y el resto es $0$.

**Resultado:** $\boxed{x - 2}$

---

## ⚙️ **Ejemplos Resueltos**

### **Ejemplo 1: Completando Huecos**
Divide $(x^3 - 8)$ entre $(x - 2)$.

**Datos:** El dividendo no tiene términos de $x^2$ ni de $x$.
**Razonamiento:** Para que la división funcione, debemos rellenar con ceros: $x^3 + 0x^2 + 0x - 8$.

**Cálculo (Ruffini):**
$$
\begin{array}{c|rrrr}
2 & 1 & 0 & 0 & -8 \\
  &   & 2 & 4 & 8 \\
\hline
  & 1 & 2 & 4 & \boxed{0}
\end{array}
$$

**Resultado:** $\boxed{x^2 + 2x + 4}$

---

### **Ejemplo 2: Teorema del Resto**
Calcula el resto de $(x^3 - 2x + 5) \div (x - 2)$ sin dividir.

**Razonamiento:** El resto es igual a evaluar el polinomio en el número del divisor con signo cambiado ($a=2$).

**Cálculo:**
$$ P(2) = (2)^3 - 2(2) + 5 = 8 - 4 + 5 = 9 $$

**Resultado:** $\boxed{\text{Resto} = 9}$

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

---

## 🔑 **Resumen**

| Método | Cuándo usarlo | Ventaja |
| :--- | :--- | :--- |
| **Por Monomio** | Divisor de un solo término ($3x^2$). | Rápido y directo. |
| **Casita** | Cualquier división entre polinomios. | Universal (sirve para todo). |
| **Ruffini** | Divisor tipo $(x \pm a)$. | No requiere variables, solo números. |
| **T. del Resto** | Solo si quieres saber el sobrante. | Evita hacer toda la división. |

> 💡 **Conclusión:** La división de polinomios nos permite simplificar estructuras matemáticas complejas. Ya sea usando el método largo o el atajo de Ruffini, lo importante es mantener el orden de los grados para que cada pieza encaje en su lugar.
