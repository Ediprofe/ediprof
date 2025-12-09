# 🔄 Conversión entre Fracciones y Decimales

En este tema aprenderemos a convertir fracciones a decimales y viceversa.

---

## 📖 De fracción a decimal

Para convertir una fracción a decimal, **dividimos** el numerador entre el denominador.

$$
\frac{a}{b} = a \div b
$$

### Ejemplo 1: Decimal exacto

$$
\frac{3}{4} = 3 \div 4 = 0.75
$$

### Ejemplo 2: Decimal periódico

$$
\frac{1}{3} = 1 \div 3 = 0.333... = 0.\overline{3}
$$

---

## 📖 De decimal exacto a fracción

Para convertir un decimal exacto a fracción:

1. **Escribir** el número sin punto como numerador
2. **Colocar** como denominador $10^n$ donde $n$ es el número de cifras decimales
3. **Simplificar** si es posible

### Fórmula

$$
0.\underbrace{d_1 d_2 ... d_n}_{n \text{ cifras}} = \frac{d_1 d_2 ... d_n}{10^n}
$$

### Ejemplo

$$
0.75 = \frac{75}{100} = \frac{3}{4}
$$

---

## 📖 De decimal periódico puro a fracción

Un decimal periódico puro tiene la forma $0.\overline{abc}$ donde $abc$ se repite.

$$
0.\overline{abc} = \frac{abc}{999...} \quad \text{(tantos 9 como cifras en el período)}
$$

### Ejemplo

$$
0.\overline{3} = \frac{3}{9} = \frac{1}{3}
$$

$$
0.\overline{12} = \frac{12}{99} = \frac{4}{33}
$$

---

## 📖 De decimal periódico mixto a fracción

Un decimal periódico mixto tiene la forma $0.ab\overline{cd}$.

$$
0.ab\overline{cd} = \frac{\text{todo} - \text{no periódico}}{\underbrace{99...00...}_{\text{9s y 0s}}}
$$

### Ejemplo

Convertir $0.1\overline{6}$ a fracción:

* Número completo sin punto: $16$
* Parte no periódica sin punto: $1$
* Período tiene 1 cifra → un $9$
* Parte no periódica tiene 1 cifra → un $0$

$$
0.1\overline{6} = \frac{16 - 1}{90} = \frac{15}{90} = \frac{1}{6}
$$

---

## 📖 Fracciones decimales comunes

| Fracción | Decimal |
|----------|---------|
| $\frac{1}{2}$ | $0.5$ |
| $\frac{1}{4}$ | $0.25$ |
| $\frac{3}{4}$ | $0.75$ |
| $\frac{1}{5}$ | $0.2$ |
| $\frac{1}{8}$ | $0.125$ |
| $\frac{1}{3}$ | $0.\overline{3}$ |
| $\frac{2}{3}$ | $0.\overline{6}$ |

---

## ⚙️ Ejercicio 1 — Fracción a decimal

Convierte a decimal:

1. $\frac{7}{8}$
2. $\frac{5}{6}$
3. $\frac{11}{4}$

### ✅ Solución

**1.** $\frac{7}{8} = 7 \div 8 = \boxed{0.875}$

**2.** $\frac{5}{6} = 5 \div 6 = \boxed{0.8\overline{3}}$

**3.** $\frac{11}{4} = 11 \div 4 = \boxed{2.75}$

---

## ⚙️ Ejercicio 2 — Decimal exacto a fracción

Convierte a fracción simplificada:

1. $0.6$
2. $0.125$
3. $0.45$

### ✅ Solución

**1.** $0.6 = \frac{6}{10} = \boxed{\frac{3}{5}}$

**2.** $0.125 = \frac{125}{1000} = \boxed{\frac{1}{8}}$

**3.** $0.45 = \frac{45}{100} = \boxed{\frac{9}{20}}$

---

## ⚙️ Ejercicio 3 — Decimal periódico a fracción

Convierte a fracción:

1. $0.\overline{7}$
2. $0.\overline{45}$
3. $0.2\overline{5}$

### ✅ Solución

**1.** $0.\overline{7} = \frac{7}{9} = \boxed{\frac{7}{9}}$

**2.** $0.\overline{45} = \frac{45}{99} = \boxed{\frac{5}{11}}$

**3.** $0.2\overline{5}$

$$
\frac{25 - 2}{90} = \frac{23}{90} = \boxed{\frac{23}{90}}
$$

---

## ⚙️ Ejercicio 4 — Problema aplicado

Si un estudiante responde correctamente $18$ de $24$ preguntas, ¿cuál es su calificación en decimal?

### ✅ Solución

$$
\frac{18}{24} = \frac{3}{4} = 0.75
$$

$$
\boxed{\text{Calificación: } 0.75 \text{ o } 75\%}
$$

---
