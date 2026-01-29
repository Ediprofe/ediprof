# Problemas de Máximos y Mínimos

Los problemas de optimización buscan el mejor resultado posible: máximo beneficio, mínimo costo, máxima área, etc. El cálculo diferencial nos da herramientas poderosas para resolverlos.

---

## 🎯 ¿Qué vas a aprender?

- Metodología para problemas de optimización
- Extremos absolutos en intervalos cerrados
- Problemas de optimización aplicada
- Estrategias de resolución

---

## 📖 Extremos absolutos

Los **extremos absolutos** son los valores máximo y mínimo de una función en todo su dominio o en un intervalo dado.

### Teorema del valor extremo

Si $f$ es continua en $[a, b]$, entonces $f$ tiene un máximo absoluto y un mínimo absoluto en $[a, b]$.

---

## 📖 Método para encontrar extremos absolutos en $[a, b]$

1. Encontrar todos los puntos críticos en $(a, b)$
2. Evaluar $f$ en los puntos críticos
3. Evaluar $f$ en los extremos $a$ y $b$
4. Comparar todos los valores
5. El mayor es el máximo absoluto, el menor es el mínimo absoluto

---

## ⚙️ Ejemplo 1: Intervalo cerrado

Encuentra los extremos absolutos de $f(x) = x^3 - 3x^2 + 1$ en $[-1, 4]$.

**Paso 1:** $f'(x) = 3x^2 - 6x = 3x(x-2) = 0$

Puntos críticos: $x = 0, 2$ (ambos en $(-1, 4)$)

**Paso 2-3:** Evaluar:
- $f(-1) = -1 - 3 + 1 = -3$
- $f(0) = 1$
- $f(2) = 8 - 12 + 1 = -3$
- $f(4) = 64 - 48 + 1 = 17$

**Paso 4-5:**
- **Máximo absoluto:** $17$ en $x = 4$
- **Mínimo absoluto:** $-3$ en $x = -1$ y $x = 2$

---

## 📖 Metodología para problemas aplicados

1. **Leer** y entender el problema
2. **Dibujar** un diagrama si es posible
3. **Identificar** la cantidad a maximizar/minimizar
4. **Escribir** una fórmula para esa cantidad
5. **Expresar** en términos de una sola variable
6. **Determinar** el dominio práctico
7. **Derivar** y encontrar puntos críticos
8. **Verificar** que es máximo/mínimo
9. **Responder** la pregunta original

---

## ⚙️ Ejemplo 2: Maximizar área

Un granjero tiene 100 metros de cerca para formar un corral rectangular. ¿Qué dimensiones maximizan el área?

**Variables:** $x$ = largo, $y$ = ancho

**Restricción:** $2x + 2y = 100$ → $y = 50 - x$

**Función objetivo:** $A = xy = x(50 - x) = 50x - x^2$

**Dominio práctico:** $0 < x < 50$

**Optimización:**
$$A'(x) = 50 - 2x = 0 \Rightarrow x = 25$$

$$A''(x) = -2 < 0$$ → Máximo

**Respuesta:** $x = 25$ m, $y = 25$ m (cuadrado de 25×25 m)

Área máxima: 625 m²

---

## ⚙️ Ejemplo 3: Minimizar distancia

Encuentra el punto de la parábola $y = x^2$ más cercano al punto $(0, 1)$.

**Distancia:**
$$d = \sqrt{(x-0)^2 + (x^2-1)^2} = \sqrt{x^2 + x^4 - 2x^2 + 1}$$

**Minimizar $d^2$** (equivalente y más fácil):
$$D = x^2 + x^4 - 2x^2 + 1 = x^4 - x^2 + 1$$

$$D'(x) = 4x^3 - 2x = 2x(2x^2 - 1) = 0$$

$$x = 0, \pm\frac{1}{\sqrt{2}}$$

Evaluando: $D(0) = 1$, $D(\pm\frac{1}{\sqrt{2}}) = \frac{1}{4} - \frac{1}{2} + 1 = \frac{3}{4}$

**Mínimo en** $x = \pm\frac{1}{\sqrt{2}}$

Puntos: $\left(\pm\frac{\sqrt{2}}{2}, \frac{1}{2}\right)$

---

## ⚙️ Ejemplo 4: Maximizar producto

Encuentra dos números positivos cuya suma es 100 y cuyo producto es máximo.

**Variables:** $x$ e $y$ con $x + y = 100$

**Producto:** $P = xy = x(100-x) = 100x - x^2$

$$P'(x) = 100 - 2x = 0 \Rightarrow x = 50$$

**Respuesta:** $x = y = 50$, producto máximo = 2500

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Encuentra los extremos absolutos de $f(x) = x^4 - 2x^2$ en $[-2, 2]$.

<details>
<summary>Ver solución</summary>

$f'(x) = 4x^3 - 4x = 4x(x^2-1) = 0$

Puntos críticos: $x = 0, \pm 1$

Evaluando: $f(-2) = 8$, $f(-1) = -1$, $f(0) = 0$, $f(1) = -1$, $f(2) = 8$

Máximo: 8 en $x = \pm 2$; Mínimo: $-1$ en $x = \pm 1$
</details>

---

**Ejercicio 2:** Divide 60 en dos partes tales que el producto de una por el cuadrado de la otra sea máximo.

<details>
<summary>Ver solución</summary>

Sea $x$ y $60-x$ las partes.

$P = x(60-x)^2$

$P' = (60-x)^2 + x \cdot 2(60-x)(-1) = (60-x)[(60-x) - 2x] = (60-x)(60-3x)$

$P' = 0$: $x = 60$ o $x = 20$

En $x = 20$: partes 20 y 40. Producto: $20 \cdot 40^2 = 32{,}000$
</details>
