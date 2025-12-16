# Función Mayor Entero (Parte Entera)

La función mayor entero "redondea hacia abajo" cualquier número real al entero más cercano que no lo exceda. Es una función escalonada con aplicaciones en computación, economía y conteo.

---

## 🎯 ¿Qué vas a aprender?

- La definición de la función piso (mayor entero)
- La función techo como complemento
- Propiedades de estas funciones
- Gráfica escalonada y características

---

## 📖 Función mayor entero (piso)

La **función mayor entero** o **función piso** se define como:

$$
\lfloor x \rfloor = \text{el mayor entero menor o igual que } x
$$

También se denota como $[x]$ o $\text{floor}(x)$.

### Interpretación

"Redondea hacia $-\infty$", es decir, hacia abajo en la recta numérica.

### Ejemplos

| $x$ | $\lfloor x \rfloor$ |
|-----|---------------------|
| $3.7$ | $3$ |
| $3.0$ | $3$ |
| $-2.3$ | $-3$ |
| $-5.0$ | $-5$ |
| $\pi$ | $3$ |

### ⚠️ Cuidado con negativos

Para números negativos, $\lfloor x \rfloor$ es **menor** que $x$:

$$\lfloor -2.3 \rfloor = -3 \neq -2$$

No es simplemente "quitar decimales".

---

## 📖 Función techo

La **función techo** es el complemento:

$$
\lceil x \rceil = \text{el menor entero mayor o igual que } x
$$

"Redondea hacia $+\infty$", es decir, hacia arriba.

### Ejemplos

| $x$ | $\lceil x \rceil$ |
|-----|-------------------|
| $3.7$ | $4$ |
| $3.0$ | $3$ |
| $-2.3$ | $-2$ |
| $-5.0$ | $-5$ |

---

## 📖 Relación entre piso y techo

Para cualquier $x$ no entero:
$$
\lceil x \rceil = \lfloor x \rfloor + 1
$$

Para $x$ entero:
$$
\lceil x \rceil = \lfloor x \rfloor = x
$$

También:
$$
\lceil x \rceil = -\lfloor -x \rfloor
$$

---

## 📖 Propiedades de la función piso

| Propiedad | Valor |
|-----------|-------|
| **Dominio** | $\mathbb{R}$ |
| **Rango** | $\mathbb{Z}$ (enteros) |
| **Paridad** | Ninguna |
| **Continua** | No (saltos en cada entero) |
| **Tipo** | Función escalonada |

### Propiedades algebraicas

Para todo $x \in \mathbb{R}$ y $n \in \mathbb{Z}$:

1. $\lfloor x \rfloor \leq x < \lfloor x \rfloor + 1$

2. $\lfloor x + n \rfloor = \lfloor x \rfloor + n$

3. $x - 1 < \lfloor x \rfloor \leq x$

4. $\lfloor x \rfloor + \lfloor -x \rfloor = \begin{cases} 0 & \text{si } x \in \mathbb{Z} \\ -1 & \text{si } x \notin \mathbb{Z} \end{cases}$

---

## ⚙️ Ejemplo 1: Cálculo sistemático

Calcula $\lfloor x \rfloor$ y $\lceil x \rceil$ para:

| $x$ | $\lfloor x \rfloor$ | $\lceil x \rceil$ |
|-----|---------------------|-------------------|
| $4.99$ | $4$ | $5$ |
| $-0.1$ | $-1$ | $0$ |
| $7$ | $7$ | $7$ |
| $-3.8$ | $-4$ | $-3$ |

---

## 📖 La gráfica escalonada

La gráfica de $f(x) = \lfloor x \rfloor$ tiene forma de escalera:

- Segmentos horizontales en cada valor entero
- Saltos en cada número entero
- Punto **cerrado** a la izquierda, **abierto** a la derecha

Para cada intervalo $[n, n+1)$ donde $n \in \mathbb{Z}$:
$$f(x) = n$$

```
     y
     ↑
   3 ●━━━━━○
   2   ●━━━━━○
   1     ●━━━━━○
─────┼──┼──┼──┼──┼──→ x
     0  1  2  3  4
  -1 ●━━━━━○
```

---

## ⚙️ Ejemplo 2: Aplicación práctica

Una empresa de taxis cobra **5,000 pesos** fijos más **2,000 pesos** por cada kilómetro **completo** recorrido.

$$C(x) = 5000 + 2000 \lfloor x \rfloor$$

donde $x$ es la distancia en km.

| Distancia | Costo |
|-----------|-------|
| $2.3$ km | $5000 + 2000(2) = 9{,}000$ pesos |
| $2.9$ km | $5000 + 2000(2) = 9{,}000$ pesos |
| $3.0$ km | $5000 + 2000(3) = 11{,}000$ pesos |

---

## ⚙️ Ejemplo 3: Transformaciones

Grafica $g(x) = \lfloor x - 2 \rfloor + 1$

**Transformaciones:**
1. Desplazamiento 2 unidades a la derecha
2. Desplazamiento 1 unidad hacia arriba

**En el intervalo $[2, 3)$:** $g(x) = \lfloor x - 2 \rfloor + 1 = 0 + 1 = 1$

**En el intervalo $[3, 4)$:** $g(x) = 1 + 1 = 2$

---

## 📖 Parte fraccionaria

La **parte fraccionaria** de $x$ es:

$$
\{x\} = x - \lfloor x \rfloor
$$

Siempre satisface: $0 \leq \{x\} < 1$

### Ejemplos

| $x$ | $\{x\}$ |
|-----|---------|
| $3.7$ | $0.7$ |
| $-2.3$ | $0.7$ (porque $-2.3 - (-3) = 0.7$) |
| $5$ | $0$ |

---

## 📊 Resumen comparativo

| Función | Notación | Comportamiento |
|---------|----------|----------------|
| **Piso** | $\lfloor x \rfloor$ | Redondea hacia $-\infty$ |
| **Techo** | $\lceil x \rceil$ | Redondea hacia $+\infty$ |
| **Truncamiento** | $\text{trunc}(x)$ | Elimina decimales (hacia 0) |
| **Redondeo** | $\text{round}(x)$ | Al entero más cercano |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Calcula:

a) $\lfloor 5.9 \rfloor$
b) $\lfloor -4.2 \rfloor$
c) $\lceil 3.01 \rceil$
d) $\lceil -7.8 \rceil$

<details>
<summary>Ver soluciones</summary>

a) $5$

b) $-5$

c) $4$

d) $-7$
</details>

---

**Ejercicio 2:** Un estacionamiento cobra **3,000 pesos** por cada hora o fracción. Expresa el costo como función del tiempo $t$ (en horas).

<details>
<summary>Ver solución</summary>

$$C(t) = 3000 \lceil t \rceil$$

Por ejemplo:
- $1.5$ horas → $\lceil 1.5 \rceil = 2$ → 6,000 pesos
- $3$ horas → $\lceil 3 \rceil = 3$ → 9,000 pesos
</details>

---

**Ejercicio 3:** Calcula la parte fraccionaria:

a) $\{4.75\}$
b) $\{-1.3\}$

<details>
<summary>Ver soluciones</summary>

a) $\{4.75\} = 4.75 - 4 = 0.75$

b) $\{-1.3\} = -1.3 - \lfloor -1.3 \rfloor = -1.3 - (-2) = 0.7$
</details>
