# √ Propiedades de los Radicales (II)

En esta lección estudiaremos más propiedades de los radicales: la potencia de un radical, la raíz de una raíz, y la simplificación de índice y exponente.

---

## 📖 Potencia de un radical

Cuando elevamos un radical a una potencia, el exponente se aplica al radicando:

$$
\left(\sqrt[n]{a}\right)^m = \sqrt[n]{a^m}
$$

### Demostración

$$
\left(\sqrt[n]{a}\right)^m = \left(a^{\frac{1}{n}}\right)^m = a^{\frac{m}{n}} = \sqrt[n]{a^m}
$$

---

### Ejemplo 1

Simplificar $\left(\sqrt{3}\right)^4$.

$$
\left(\sqrt{3}\right)^4 = \sqrt{3^4} = \sqrt{81} = 9
$$

$$
\boxed{\left(\sqrt{3}\right)^4 = 9}
$$

---

### Ejemplo 2

Simplificar $\left(\sqrt[3]{2}\right)^6$.

$$
\left(\sqrt[3]{2}\right)^6 = \sqrt[3]{2^6} = \sqrt[3]{64} = 4
$$

$$
\boxed{\left(\sqrt[3]{2}\right)^6 = 4}
$$

---

### Ejemplo 3

Simplificar $\left(\sqrt{x}\right)^6$.

$$
\left(\sqrt{x}\right)^6 = \sqrt{x^6} = x^3
$$

(Asumiendo $x \geq 0$)

$$
\boxed{\left(\sqrt{x}\right)^6 = x^3}
$$

---

## 📖 Raíz de una raíz

Para calcular la raíz de una raíz, se **multiplican los índices**:

$$
\sqrt[m]{\sqrt[n]{a}} = \sqrt[m \cdot n]{a}
$$

### Demostración

$$
\sqrt[m]{\sqrt[n]{a}} = \left(a^{\frac{1}{n}}\right)^{\frac{1}{m}} = a^{\frac{1}{mn}} = \sqrt[mn]{a}
$$

---

### Ejemplo 4

Simplificar $\sqrt{\sqrt{16}}$.

$$
\sqrt{\sqrt{16}} = \sqrt[2 \cdot 2]{16} = \sqrt[4]{16} = 2
$$

Verificación: $\sqrt{16} = 4$, luego $\sqrt{4} = 2$ ✓

$$
\boxed{\sqrt{\sqrt{16}} = 2}
$$

---

### Ejemplo 5

Simplificar $\sqrt[3]{\sqrt{64}}$.

$$
\sqrt[3]{\sqrt{64}} = \sqrt[3 \cdot 2]{64} = \sqrt[6]{64}
$$

Como $64 = 2^6$, entonces $\sqrt[6]{64} = 2$

$$
\boxed{\sqrt[3]{\sqrt{64}} = 2}
$$

---

### Ejemplo 6

Simplificar $\sqrt{\sqrt[3]{a^6}}$.

$$
\sqrt{\sqrt[3]{a^6}} = \sqrt[2 \cdot 3]{a^6} = \sqrt[6]{a^6} = a
$$

$$
\boxed{\sqrt{\sqrt[3]{a^6}} = a}
$$

---

## 📖 Simplificación de índice y exponente

Si el índice y el exponente del radicando tienen un factor común, se puede simplificar:

$$
\sqrt[n]{a^m} = \sqrt[\frac{n}{d}]{a^{\frac{m}{d}}}
$$

donde $d = \text{MCD}(n, m)$

### En términos de exponentes

$$
\sqrt[n]{a^m} = a^{\frac{m}{n}}
$$

Si $\text{MCD}(m, n) = d$, entonces:

$$
a^{\frac{m}{n}} = a^{\frac{m/d}{n/d}}
$$

---

### Ejemplo 7

Simplificar $\sqrt[6]{x^4}$.

$$
\sqrt[6]{x^4} = x^{\frac{4}{6}} = x^{\frac{2}{3}} = \sqrt[3]{x^2}
$$

$$
\boxed{\sqrt[6]{x^4} = \sqrt[3]{x^2}}
$$

---

### Ejemplo 8

Simplificar $\sqrt[4]{a^2}$.

$$
\sqrt[4]{a^2} = a^{\frac{2}{4}} = a^{\frac{1}{2}} = \sqrt{a}
$$

$$
\boxed{\sqrt[4]{a^2} = \sqrt{a}}
$$

---

### Ejemplo 9

Simplificar $\sqrt[9]{b^6}$.

$$
\sqrt[9]{b^6} = b^{\frac{6}{9}} = b^{\frac{2}{3}} = \sqrt[3]{b^2}
$$

$$
\boxed{\sqrt[9]{b^6} = \sqrt[3]{b^2}}
$$

---

### Ejemplo 10

Simplificar $\sqrt[12]{x^8y^4}$.

$$
\sqrt[12]{x^8y^4} = x^{\frac{8}{12}} \cdot y^{\frac{4}{12}} = x^{\frac{2}{3}} \cdot y^{\frac{1}{3}}
$$

$$
= \sqrt[3]{x^2} \cdot \sqrt[3]{y} = \sqrt[3]{x^2y}
$$

$$
\boxed{\sqrt[12]{x^8y^4} = \sqrt[3]{x^2y}}
$$

---

## 📖 Resumen

| Propiedad | Fórmula |
|:----------|:-------:|
| Potencia de un radical | $\left(\sqrt[n]{a}\right)^m = \sqrt[n]{a^m}$ |
| Raíz de una raíz | $\sqrt[m]{\sqrt[n]{a}} = \sqrt[mn]{a}$ |
| Simplificación | $\sqrt[n]{a^m} = \sqrt[n/d]{a^{m/d}}$ donde $d = \text{MCD}(n,m)$ |

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Simplifica $\left(\sqrt{5}\right)^6$.

<details>
<summary>Ver solución</summary>

$$
\left(\sqrt{5}\right)^6 = \sqrt{5^6} = \sqrt{15625} = 125
$$

O bien: $(\sqrt{5})^6 = 5^3 = 125$

</details>

---

**Ejercicio 2:** Simplifica $\sqrt{\sqrt[4]{256}}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt{\sqrt[4]{256}} = \sqrt[8]{256} = \sqrt[8]{2^8} = 2
$$

</details>

---

**Ejercicio 3:** Simplifica $\sqrt[8]{x^6}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt[8]{x^6} = x^{\frac{6}{8}} = x^{\frac{3}{4}} = \sqrt[4]{x^3}
$$

</details>

---

**Ejercicio 4:** Simplifica $\left(\sqrt[4]{3}\right)^8$.

<details>
<summary>Ver solución</summary>

$$
\left(\sqrt[4]{3}\right)^8 = 3^{\frac{8}{4}} = 3^2 = 9
$$

</details>

---

**Ejercicio 5:** Simplifica $\sqrt[3]{\sqrt{a^{12}}}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt[3]{\sqrt{a^{12}}} = \sqrt[6]{a^{12}} = a^{\frac{12}{6}} = a^2
$$

</details>

---

**Ejercicio 6:** Simplifica $\sqrt[10]{m^4n^6}$.

<details>
<summary>Ver solución</summary>

$$
\sqrt[10]{m^4n^6} = m^{\frac{4}{10}}n^{\frac{6}{10}} = m^{\frac{2}{5}}n^{\frac{3}{5}} = \sqrt[5]{m^2n^3}
$$

</details>

---
