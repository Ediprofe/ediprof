# Probabilidad Condicional

¿Cómo cambia una probabilidad cuando tenemos **información adicional**? Si sabemos que un dado cayó en número par, ¿cuál es la probabilidad de que sea 6? Esta es la esencia de la **probabilidad condicional**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la probabilidad condicional
- Cómo calcularla e interpretarla
- La relación con la independencia
- El Teorema de Bayes

---

## 📖 ¿Qué es la Probabilidad Condicional?

> La **probabilidad condicional** de B dado A, escrita $P(B|A)$, es la probabilidad de que ocurra B **sabiendo que** A ya ocurrió.

### 💡 Fórmula:

$$
P(B|A) = \frac{P(A \cap B)}{P(A)}
$$

Se lee: "Probabilidad de B dado A".

### 💡 Interpretación:

La información de que A ocurrió **reduce el espacio muestral**. Ahora solo consideramos los casos donde A es verdadero.

---

## 📖 Ejemplo Fundamental

### ⚙️ Dado de 6 caras

Sabemos que cayó **número par**. ¿Cuál es la probabilidad de que sea 6?

**Sin información:**
$P(6) = \frac{1}{6}$

**Con información (dado que es par):**

- Espacio muestral reducido: {2, 4, 6}
- Solo 1 de estos 3 es 6

$$
P(6 | \text{par}) = \frac{1}{3}
$$

**Usando la fórmula:**

- A = "par" = {2, 4, 6}, P(A) = 3/6 = 1/2
- B = "es 6" = {6}
- A ∩ B = {6}, P(A ∩ B) = 1/6

$$
P(6 | \text{par}) = \frac{P(6 \cap \text{par})}{P(\text{par})} = \frac{1/6}{1/2} = \frac{1}{6} \times \frac{2}{1} = \frac{1}{3}
$$

---

## 📖 Otro Ejemplo: Cartas

### ⚙️ De una baraja de 52 cartas:

Sabemos que la carta es **roja**. ¿Cuál es la probabilidad de que sea **As**?

- A = "carta roja", P(A) = 26/52 = 1/2
- B = "carta es As"
- A ∩ B = "As rojo" = {As♥, As♦}, P(A ∩ B) = 2/52

$$
P(\text{As} | \text{roja}) = \frac{2/52}{26/52} = \frac{2}{26} = \frac{1}{13}
$$

**Verificación:** De 26 cartas rojas, 2 son Ases → $\frac{2}{26} = \frac{1}{13}$ ✓

---

## 📖 Regla de Multiplicación (Forma Alternativa)

De la fórmula de probabilidad condicional, despejamos:

$$
P(A \cap B) = P(A) \cdot P(B|A)
$$

O equivalentemente:

$$
P(A \cap B) = P(B) \cdot P(A|B)
$$

### ⚙️ Ejemplo: Dos extracciones sin reemplazo

Urna con 6 bolas blancas y 4 negras. ¿Probabilidad de sacar 2 blancas consecutivas?

$$
P(B_1 \cap B_2) = P(B_1) \cdot P(B_2|B_1) = \frac{6}{10} \times \frac{5}{9} = \frac{30}{90} = \frac{1}{3}
$$

---

## 📖 Independencia: Definición Formal

> A y B son **independientes** si y solo si:

$$
P(B|A) = P(B)
$$

Es decir, saber que A ocurrió **no cambia** la probabilidad de B.

### 💡 Equivalencias (cualquiera implica las otras):

$$
P(B|A) = P(B)
$$
$$
P(A|B) = P(A)
$$
$$
P(A \cap B) = P(A) \cdot P(B)
$$

### ⚙️ Ejemplo de independencia:

Lanzar moneda y dado.
- P(cara) = 1/2
- P(6 | cara) = 1/6 = P(6)

La moneda no afecta al dado → Son independientes.

### ⚙️ Ejemplo de dependencia:

Sacar 2 cartas sin reemplazo.
- P(2da es As) = 4/52
- P(2da es As | 1ra es As) = 3/51

La primera carta **sí** afecta la segunda → Son dependientes.

---

## 📖 Teorema de Bayes

> El **Teorema de Bayes** permite "invertir" una probabilidad condicional.

### 💡 Fórmula:

$$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$$

### 💡 Utilidad:

Cuando conocemos $P(B|A)$ pero necesitamos $P(A|B)$.

### ⚙️ Ejemplo: Diagnóstico médico

Una enfermedad afecta al 1% de la población.
Una prueba tiene:
- 95% de sensibilidad: P(+ | enfermo) = 0.95
- 10% de falsos positivos: P(+ | sano) = 0.10

**Pregunta:** Si la prueba da positivo, ¿cuál es la probabilidad de estar enfermo?

**Datos:**
- P(E) = 0.01 (tiene enfermedad)
- P(E') = 0.99 (sano)
- P(+ | E) = 0.95
- P(+ | E') = 0.10

**Paso 1:** Calcular P(+)
$$
P(+) = P(+|E) \cdot P(E) + P(+|E') \cdot P(E')
$$
$$
= 0.95 \times 0.01 + 0.10 \times 0.99 = 0.0095 + 0.099 = 0.1085
$$

**Paso 2:** Aplicar Bayes
$$
P(E|+) = \frac{P(+|E) \cdot P(E)}{P(+)} = \frac{0.95 \times 0.01}{0.1085} = \frac{0.0095}{0.1085} \approx 0.0875
$$

**Resultado sorprendente:** ¡Solo 8.75% de probabilidad de estar enfermo tras un positivo!

**¿Por qué?** La enfermedad es rara (1%). Los falsos positivos (10% de muchos sanos) superan a los verdaderos positivos (95% de pocos enfermos).

---

## 🔑 Resumen

| Concepto | Fórmula |
|----------|---------|
| **P condicional** | $P(B|A) = \frac{P(A \cap B)}{P(A)}$ |
| **Multiplicación** | $P(A \cap B) = P(A) \cdot P(B|A)$ |
| **Independencia** | $P(B|A) = P(B)$ |
| **Bayes** | $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$ |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
P(A) = 0.6, P(B) = 0.5, P(A ∩ B) = 0.3
¿Son A y B independientes?

<details>
<summary>Ver solución</summary>

Para ser independientes: $P(A \cap B) = P(A) \cdot P(B)$

$$P(A) \cdot P(B) = 0.6 \times 0.5 = 0.30$$

$$P(A \cap B) = 0.3$$

Como $0.30 = 0.30$, **SÍ son independientes**.

</details>

### Ejercicio 2
De 100 estudiantes: 60 estudian matemáticas, 50 estudian física, 30 estudian ambas.
Si se elige uno al azar que estudia matemáticas, ¿cuál es la probabilidad de que estudie física?

<details>
<summary>Ver solución</summary>

$$P(\text{Física} | \text{Mate}) = \frac{P(\text{Mate} \cap \text{Física})}{P(\text{Mate})} = \frac{30/100}{60/100} = \frac{30}{60} = 0.5$$

El 50% de los que estudian matemáticas también estudian física.

</details>

### Ejercicio 3
Una urna tiene 8 bolas: 5 rojas y 3 azules. Se extraen 2 sin reemplazo.
a) P(2da azul | 1ra roja)
b) P(ambas rojas)

<details>
<summary>Ver solución</summary>

a) Si la primera fue roja, quedan 5+3-1 = 7 bolas, de las cuales 3 son azules:
$$P(\text{2da azul} | \text{1ra roja}) = \frac{3}{7}$$

b) $$P(\text{ambas rojas}) = P(R_1) \cdot P(R_2|R_1) = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14}$$

</details>

### Ejercicio 4
Usando el ejemplo del diagnóstico médico, si la prueba da negativo, ¿cuál es la probabilidad de estar sano?

<details>
<summary>Ver solución</summary>

**Datos adicionales:**
- P(- | E) = 0.05 (falso negativo)
- P(- | E') = 0.90 (verdadero negativo)

**P(-):**
$$P(-) = P(-|E) \cdot P(E) + P(-|E') \cdot P(E')$$
$$= 0.05 \times 0.01 + 0.90 \times 0.99 = 0.0005 + 0.891 = 0.8915$$

**Bayes:**
$$P(E'|-) = \frac{P(-|E') \cdot P(E')}{P(-)} = \frac{0.90 \times 0.99}{0.8915} = \frac{0.891}{0.8915} \approx 0.9994$$

**Resultado:** 99.94% de probabilidad de estar sano si la prueba es negativa (muy tranquilizador).

</details>
