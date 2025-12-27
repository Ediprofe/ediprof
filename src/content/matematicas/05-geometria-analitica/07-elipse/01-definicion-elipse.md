# **Definición de la Elipse**

Si estiras un círculo o aplastas una pelota de goma, obtienes una elipse. Es la ruta que siguen la Tierra alrededor del Sol y la Luna alrededor de la Tierra. A diferencia del círculo (que tiene un centro), la elipse tiene **dos corazones** llamados focos.

---

## 🎯 ¿Qué vas a aprender?

- La definición del jardinero: Distancia 1 + Distancia 2 = Constante.
- Los elementos "sagrados": $a$ (mayor), $b$ (menor), $c$ (focal).
- La relación pitagórica mágica: $a^2 = b^2 + c^2$.

---

## 🧵 La Definición del Jardinero

Imagina que clavas dos estacas en el suelo (los **Focos**), atas una cuerda holgada entre ellas y estiras la cuerda con un lápiz mientras dibujas alrededor. La figura que se forma es una **Elipse**.
Matemáticamente:
$$ d(P, F_1) + d(P, F_2) = 2a $$
La suma de las distancias a los dos focos es siempre igual a la longitud del eje largo ($2a$).

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Elementos de la Elipse</strong>
  </div>
  <img src="/images/geometria/analitica/elementos-elipse.svg" alt="Elementos de la elipse" style="width: 100%; height: auto;" />
</div>

---

## 📐 El Triángulo Sagrado ($a, b, c$)

En la elipse, tres longitudes gobiernan todo. Forman un triángulo rectángulo clave:

| Letra | Nombre | Significado | Relación Visual |
| :--- | :--- | :--- | :--- |
| **$a$** | Semieje Mayor | La mitad del largo total. | Es la Hipotenusa (la más larga). |
| **$b$** | Semieje Menor | La mitad del ancho total. | Un cateto. |
| **$c$** | Semidistancia Focal | Del centro a un foco. | El otro cateto. |

**La Fórmula Maestra:**
$$ a^2 = b^2 + c^2 $$
*(Ojo: Aquí $a$ es la hipotenusa, a diferencia de Pitágoras estándar donde suele ser $c$. En la elipse, $a$ siempre gana).*

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Hallar $c$
Una elipse mide 10 de largo ($2a=10$) y 8 de ancho ($2b=8$). ¿Dónde están los focos?
1.  $a = 5$.
2.  $b = 4$.
3.  $c = \sqrt{a^2 - b^2} = \sqrt{25 - 16} = \sqrt{9} = 3$.
    Los focos están a 3 unidades del centro.

### Ejemplo 2: Excentricidad ($e$)
Con los datos anteriores ($a=5, c=3$).
$$ e = \frac{c}{a} = \frac{3}{5} = 0.6 $$
La excentricidad nos dice qué tan "achatada" está. 0 es círculo, 0.99 es casi una línea.

### Ejemplo 3: Verificar un Punto
Si los focos están en $(\pm 3, 0)$ y $2a = 10$. ¿El punto $(0, 4)$ pertenece?
1.  Distancia $F_1(-3,0)$ a $P(0,4)$: $\sqrt{3^2+4^2}=5$.
2.  Distancia $F_2(3,0)$ a $P(0,4)$: $\sqrt{(-3)^2+4^2}=5$.
3.  Suma: $5+5=10$.
    ¡Sí! La suma es 10, que es igual a $2a$. El punto pertenece.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Si $a=13$ y $c=5$, halla $b$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$b = \sqrt{169 - 25} = 12$.

**Respuesta:** $\boxed{12}$
</details>

---

### Ejercicio 2
Si $2a = 20$, ¿cuánto vale la "Cuerda" del jardinero?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La longitud de la cuerda es la constante $2a$.

**Respuesta:** $\boxed{20}$
</details>

---

### Ejercicio 3
Excentricidad si $a=b$ (Círculo).

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si $a=b$, entonces $c=0$. $e = 0/a = 0$.

**Respuesta:** $\boxed{0}$
</details>

---

### Ejercicio 4
Eje Menor si $a=10, c=8$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$b=6$. Eje Menor $= 2b = 12$.

**Respuesta:** $\boxed{12}$
</details>

---

### Ejercicio 5
¿Puede ser $c > a$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
No, la hipotenusa $a$ siempre es mayor.

**Respuesta:** **No**
</details>

---

### Ejercicio 6
Distancia entre focos si $c=4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$2c = 8$.

**Respuesta:** $\boxed{8}$
</details>

---

### Ejercicio 7
Si los vértices están en $\pm 5$ y focos en $\pm 4$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$a=5, c=4 \Rightarrow b=3$.

**Respuesta:** **b = 3**
</details>

---

### Ejercicio 8
Área de una elipse con $a=2, b=1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Fórmula extra: $A = \pi a b$.

**Respuesta:** $\boxed{2\pi}$
</details>

---

### Ejercicio 9
Definición de Lado Recto en Elipses.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Cuerda perpendicular al eje mayor que pasa por el foco. $2b^2/a$.

**Respuesta:** $\boxed{2b^2/a}$
</details>

---

### Ejercicio 10
Si $e = 1$, ¿qué figura es?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Ya no es elipse, es parábola (o segmento). Límite plano.

**Respuesta:** **Parábola (o degenerada)**
</details>

---

## 🔑 Resumen

| Letra | Rol Geométrico | Fórmula Maestra |
| :--- | :--- | :--- |
| **$a$** | El jefe (Hipotenusa). Distancia Centro $\to$ Vertice lejano. | $a^2 = b^2+c^2$ |
| **$b$** | El ancho (Cateto). Distancia Centro $\to$ Vertice cercano. | |
| **$c$** | El foco (Cateto). Distancia Centro $\to$ Foco. | |

> **Conclusión:** La elipse es la madre de las órbitas. Sin esta relación $a, b, c$, no podríamos calcular viajes espaciales ni entender las estaciones del año.
