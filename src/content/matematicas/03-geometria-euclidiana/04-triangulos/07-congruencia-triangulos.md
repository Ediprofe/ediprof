# **Congruencia de Triángulos**

Imagina que estás fabricando baldosas para un piso. Necesitas que todas sean copias exactas unas de otras para que encajen perfectamente. En geometría, cuando dos figuras tienen exactamente la misma forma y el mismo tamaño, decimos que son **congruentes**.

---

## 🎯 ¿Qué vas a aprender?

- Comprender el concepto intuitivo y geométrico de congruencia.
- Identificar lados y ángulos correspondientes en figuras congruentes.
- Aplicar el criterio Lado-Lado-Lado (LLL).
- Aplicar el criterio Lado-Ángulo-Lado (LAL).
- Aplicar el criterio Ángulo-Lado-Ángulo (ALA).

---

## 📐 Concepto de Congruencia

Dos triángulos son congruentes si son "gemelos idénticos". Si recortas uno y lo pones encima del otro, deben coincidir perfectamente en todos sus lados y todos sus ángulos.

El símbolo para la congruencia es $\cong$.

**Definición:**
Si el triángulo $ABC$ es congruente con el triángulo $DEF$, escribimos:

$$
\triangle ABC \cong \triangle DEF
$$

Esto implica seis igualdades (3 lados y 3 ángulos):

$$
AB = DE
$$

$$
BC = EF
$$

$$
AC = DF
$$

$$
\angle A = \angle D
$$

$$
\angle B = \angle E
$$

$$
\angle C = \angle F
$$

![congruence-definition](/images/geometria/triangulos/congruence-definition.svg)

---

## 🔍 Criterios de Congruencia

Para saber si dos triángulos son congruentes, no necesitamos medir todo. Basta con verificar ciertas condiciones mínimas llamadas **criterios**.

### 1. Criterio LLL (Lado-Lado-Lado)

Si los tres lados de un triángulo son iguales a los tres lados de otro triángulo, entonces son congruentes.

$$
\text{Si } a=a', b=b', c=c' \implies \text{Congruentes}
$$

![criterion-lll](/images/geometria/triangulos/criterion-lll.svg)

### 2. Criterio LAL (Lado-Ángulo-Lado)

Si dos triángulos tienen dos lados iguales y el **ángulo comprendido** entre ellos también es igual, entonces son congruentes.

**Importante:** El ángulo debe estar **entre** los dos lados.

$$
\text{Si } a=a', \angle B=\angle B', c=c' \implies \text{Congruentes}
$$

![criterion-lal](/images/geometria/triangulos/criterion-lal.svg)

### 3. Criterio ALA (Ángulo-Lado-Ángulo)

Si dos triángulos tienen dos ángulos iguales y el **lado comprendido** entre ellos también es igual, entonces son congruentes.

$$
\text{Si } \angle A=\angle A', c=c', \angle B=\angle B' \implies \text{Congruentes}
$$

![criterion-ala](/images/geometria/triangulos/criterion-ala.svg)

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Aplicando el Criterio LLL

Compara el triángulo $PQR$ con lados 3, 4, 5 y el triángulo $STU$ con lados 3, 4, 5. ¿Son congruentes?

**Datos:**

$$
PQ = 3, QR = 4, RP = 5
$$

$$
ST = 3, TU = 4, US = 5
$$

![example-lll-345](/images/geometria/triangulos/example-lll-345.svg)

**Razonamiento:**

Observamos que los lados coinciden uno a uno:

$$
PQ = ST = 3
$$

$$
QR = TU = 4
$$

$$
RP = US = 5
$$

Como los tres lados son iguales, aplicamos el criterio **Lado-Lado-Lado**.

**Resultado:**

$$
\boxed{\text{Sí, } \triangle PQR \cong \triangle STU \text{ por LLL}}
$$

---

### Ejemplo 2: Verificando el Criterio LAL

Tienes dos triángulos.
Triángulo 1: Lados de 5 cm y 7 cm, con un ángulo de 40° entre ellos.
Triángulo 2: Lados de 5 cm y 7 cm, con un ángulo de 40° entre ellos.

![example-lal-5740](/images/geometria/triangulos/example-lal-5740.svg)

**Razonamiento:**

Verificamos las condiciones:
1. Primer lado igual ($5$ cm).
2. Segundo lado igual ($7$ cm).
3. El ángulo de $40^\circ$ está formado por estos dos lados.

Cumple con **Lado-Ángulo-Lado**.

**Resultado:**

$$
\boxed{\text{Son congruentes por LAL}}
$$

---

### Ejemplo 3: ¿LAL o no?

Triángulo A: Lados 6 y 8, ángulo opuesto al lado 8 es 30°.
Triángulo B: Lados 6 y 8, ángulo opuesto al lado 8 es 30°.

![example-lla-ambiguous](/images/geometria/triangulos/example-lla-ambiguous.svg)

**Razonamiento:**

El criterio LAL exige que el ángulo esté **entre** los lados conocidos. Aquí el ángulo es opuesto a uno de ellos, no el comprendido. Por lo tanto, **NO** podemos asegurar congruencia con LAL (este es el caso ambiguo LLA, que no garantiza congruencia general).

**Resultado:**

$$
\boxed{\text{No se puede asegurar congruencia por LAL}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Identifica el criterio de congruencia.
Triángulo 1: Ángulos de 30° y 60°, lado entre ellos de 10 cm.
Triángulo 2: Ángulos de 30° y 60°, lado entre ellos de 10 cm.

<details>
<summary>Ver solución</summary>

**Datos:**
Dos ángulos iguales y el lado común igual.

**Razonamiento:**
El criterio que usa dos ángulos y el lado intermedio es **Ángulo-Lado-Ángulo**.

**Resultado:**
$$
\boxed{\text{ALA}}
$$

</details>

### Ejercicio 2
Si $\triangle ABC \cong \triangle XYZ$, y el lado $AB = 15$ cm, ¿cuánto mide el lado $XY$?

<details>
<summary>Ver solución</summary>

**Datos:**
Triángulos congruentes.
$AB$ corresponde a $XY$.

**Razonamiento:**
En triángulos congruentes, los lados correspondientes son iguales.

$$
AB = XY
$$

$$
15 = XY
$$

**Resultado:**
$$
\boxed{15 \text{ cm}}
$$

</details>

### Ejercicio 3
Determina si son congruentes:
Triángulo 1: Lados 4, 5, 6.
Triángulo 2: Lados 4, 5, 7.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Comparamos los lados correspondientes.

$$
6 \neq 7
$$

No todos los lados son iguales.

**Resultado:**
$$
\boxed{\text{No son congruentes}}
$$

</details>

### Ejercicio 4
En la figura (imagina un rectángulo cortado por una diagonal), se forman dos triángulos. El rectángulo tiene lados opuestos iguales y ángulos de 90°. ¿Por qué criterio son congruentes estos triángulos?

<details>
<summary>Ver solución</summary>

**Datos:**
Lado inferior = Lado superior.
Lado izquierdo = Lado derecho.
La diagonal es lado común (Lado compartido).

**Razonamiento:**
Tenemos tres lados iguales (dos por ser rectángulo, uno compartido).
Criterio Lado-Lado-Lado.
(También podría ser LAL usando el ángulo recto).

**Resultado:**
$$
\boxed{\text{LLL}}
$$

</details>

### Ejercicio 5
Calcula el valor de $x$ si $\triangle ABC \cong \triangle DEF$, $\angle A = 50^\circ$ y $\angle D = x + 10^\circ$.

<details>
<summary>Ver solución</summary>

**Datos:**
Ángulos correspondientes $A$ y $D$ deben ser iguales.

$$
\angle A = 50^\circ
$$

$$
\angle D = x + 10^\circ
$$

**Razonamiento:**
Igualamos los ángulos:

$$
50 = x + 10
$$

Despejamos $x$:

$$
x = 50 - 10
$$

**Resultado:**
$$
\boxed{x = 40}
$$

</details>

### Ejercicio 6
Tienes dos triángulos rectángulos. Ambos tienen un cateto de 3 cm y una hipotenusa de 5 cm. ¿Son congruentes?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Existe un criterio especial para triángulos rectángulos: **Hipotenusa-Cateto**.
Si tienen la hipotenusa igual y un cateto igual, son congruentes.
También podríamos calcular el tercer lado por Pitágoras (daría 4 en ambos), y usar LLL.

**Resultado:**
$$
\boxed{\text{Sí, son congruentes}}
$$

</details>

### Ejercicio 7
Si dos triángulos tienen los tres ángulos iguales (ej. 60, 60, 60), ¿son necesariamente congruentes?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Tres ángulos iguales garantizan la misma **forma**, pero no necesariamente el mismo **tamaño**.
Podría ser un triángulo pequeño y uno gigante. Esto es **semejanza**, no congruencia.

**Resultado:**
$$
\boxed{\text{No necesariamente}}
$$

</details>

### Ejercicio 8
En un triángulo isósceles $ABC$ con $AB = AC$, trazamos la altura desde $A$ hasta la base $BC$ (punto $D$). ¿Son congruentes los triángulos $\triangle ABD$ y $\triangle ACD$?

<details>
<summary>Ver solución</summary>

**Datos:**
$AB = AC$ (Lado).
$AD$ es común (Lado).
$\angle ADB = \angle ADC = 90^\circ$ (Ángulo, pero no entre los lados dados).
Usando criterio Hipotenusa-Cateto para rectángulos (Hipotenusa $AB=AC$, cateto $AD$ común).

**Razonamiento:**
Cumplen el criterio Hipotenusa-Cateto.

**Resultado:**
$$
\boxed{\text{Sí, son congruentes}}
$$

</details>

### Ejercicio 9
Si sabemos que $\triangle MNO \cong \triangle PQR$, ¿cuál ángulo corresponde a $\angle O$?

<details>
<summary>Ver solución</summary>

**Datos:**
El orden de las letras indica la correspondencia.
$M \to P$
$N \to Q$
$O \to R$

**Razonamiento:**
La tercera letra corresponde a la tercera letra.

**Resultado:**
$$
\boxed{\angle R}
$$

</details>

### Ejercicio 10
Dado el $\triangle ABC$ con $A(0,0), B(3,0), C(0,4)$. ¿Es congruente con $\triangle DEF$ con $D(1,1), E(4,1), F(1,5)$?

<details>
<summary>Ver solución</summary>

**Datos:**
Medimos lados de ABC:
$AB = 3$ (horizontal).
$AC = 4$ (vertical).
$BC = 5$ (hipotenusa 3-4-5).

Medimos lados de DEF:
$DE = 3$ (horizontal de 1 a 4).
$DF = 4$ (vertical de 1 a 5).
$EF = 5$ (hipotenusa).

**Razonamiento:**
Los tres lados miden 3, 4 y 5 en ambos triángulos.
Usamos criterio LLL.

**Resultado:**
$$
\boxed{\text{Sí, son congruentes}}
$$

</details>

---

## 🔑 Resumen

![congruencia-de-triangulos](https://cdn.ediprofe.com/img/matematicas/bcpc-congruencia-de-triangulos.webp)

| Criterio | Significado | Clave Visual |
|----------|-------------|--------------|
| **LLL** | Lado-Lado-Lado | Los 3 lados son idénticos. |
| **LAL** | Lado-Ángulo-Lado | El ángulo está "atrapado" entre los lados. |
| **ALA** | Ángulo-Lado-Ángulo | El lado conecta los dos ángulos. |
| **HC** | Hipotenusa-Cateto | Solo para triángulos rectángulos. |

> La congruencia significa identidad geométrica: dos figuras son congruentes si son exactamente iguales en forma y dimensiones, sin importar su posición u orientación.
