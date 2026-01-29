# Reglas de Probabilidad

Ahora que conocemos los conceptos básicos, aprendamos las reglas para calcular probabilidades de eventos compuestos: la unión (A o B) y la intersección (A y B).

---

## 🎯 ¿Qué vas a aprender?

- La regla de la suma (A o B)
- La regla de la multiplicación (A y B)
- Eventos mutuamente excluyentes
- Eventos independientes

---

## 📊 Resumen de Reglas

| Operación | Símbolo | Regla General | Caso Especial |
|-----------|---------|---------------|---------------|
| Unión (O) | $A \cup B$ | $P(A) + P(B) - P(A \cap B)$ | $P(A) + P(B)$ si excluyentes |
| Intersección (Y) | $A \cap B$ | $P(A) \cdot P(B|A)$ | $P(A) \cdot P(B)$ si independientes |

---

## 📖 Operaciones con Eventos

### 💡 Unión (A ∪ B): "A o B"

Ocurre A, o B, o ambos.

### 💡 Intersección (A ∩ B): "A y B"

Ocurren A y B simultáneamente.

### 💡 Complemento (A'): "No A"

No ocurre A.

### ⚙️ Ejemplo con dados:

Si A = "número par" = {2, 4, 6} y B = "número > 3" = {4, 5, 6}:

- $A \cup B$ = {2, 4, 5, 6} (par O mayor que 3)
- $A \cap B$ = {4, 6} (par Y mayor que 3)
- $A'$ = {1, 3, 5} (impar)

---

## 📖 Regla de la Suma (Unión)

### 💡 Fórmula general:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

### 💡 ¿Por qué restar P(A ∩ B)?

Porque si simplemente sumamos P(A) + P(B), contamos dos veces los resultados que están en ambos.

### ⚙️ Ejemplo: Dado

A = "par" = {2, 4, 6}, P(A) = 3/6 = 0.5
B = "> 3" = {4, 5, 6}, P(B) = 3/6 = 0.5
A ∩ B = {4, 6}, P(A ∩ B) = 2/6 = 1/3

$$
P(A \cup B) = 0.5 + 0.5 - \frac{1}{3} = 1 - \frac{1}{3} = \frac{2}{3}
$$

**Verificación:** A ∪ B = {2, 4, 5, 6}, que tiene 4 elementos.
$P = \frac{4}{6} = \frac{2}{3}$ ✓

---

## 📖 Eventos Mutuamente Excluyentes

> Dos eventos son **mutuamente excluyentes** si no pueden ocurrir al mismo tiempo.

$$
P(A \cap B) = 0
$$

### 💡 Regla de la suma simplificada:

$$
P(A \cup B) = P(A) + P(B)
$$

### ⚙️ Ejemplo: Color de carta

A = "carta roja", B = "carta negra"

Son mutuamente excluyentes (una carta no puede ser roja Y negra).

$$
P(\text{roja o negra}) = P(\text{roja}) + P(\text{negra}) = \frac{26}{52} + \frac{26}{52} = 1
$$

### ⚙️ Contraejemplo:

A = "carta de corazones", B = "carta es As"

**No** son mutuamente excluyentes (existe el As de corazones).

---

## 📖 Regla de la Multiplicación (Intersección)

### 💡 Fórmula general:

$$
P(A \cap B) = P(A) \cdot P(B|A)
$$

Donde $P(B|A)$ es la probabilidad de B **dado que** A ya ocurrió.

### ⚙️ Ejemplo: Sacar 2 cartas sin reemplazo

¿Cuál es la probabilidad de sacar 2 ases consecutivos sin devolver la primera carta?

A = "primera carta es As"
B = "segunda carta es As"

$$
P(A) = \frac{4}{52}
$$

$$
P(B|A) = \frac{3}{51} \text{ (quedan 3 ases de 51 cartas)}
$$

$$
P(A \cap B) = \frac{4}{52} \times \frac{3}{51} = \frac{12}{2652} = \frac{1}{221} \approx 0.0045
$$

---

## 📖 Eventos Independientes

> Dos eventos son **independientes** si la ocurrencia de uno no afecta la probabilidad del otro.

$$
P(B|A) = P(B)
$$

### 💡 Regla de multiplicación simplificada:

$$
P(A \cap B) = P(A) \cdot P(B)
$$

### ⚙️ Ejemplo: Lanzar moneda y dado

Son independientes (lo que salga en la moneda no afecta al dado).

$$
P(\text{cara y 6}) = P(\text{cara}) \times P(6) = \frac{1}{2} \times \frac{1}{6} = \frac{1}{12}
$$

### ⚙️ Ejemplo: Sacar 2 cartas CON reemplazo

Si devolvemos la primera carta antes de sacar la segunda:

$$
P(\text{2 ases}) = \frac{4}{52} \times \frac{4}{52} = \frac{16}{2704} = \frac{1}{169} \approx 0.0059
$$

---

## 📖 Comparación: Con y Sin Reemplazo

| Tipo | ¿Independiente? | Ejemplo |
|------|-----------------|---------|
| **Con reemplazo** | ✅ Sí | $P(A \cap B) = P(A) \cdot P(B)$ |
| **Sin reemplazo** | ❌ No | $P(A \cap B) = P(A) \cdot P(B|A)$ |

---

## 📖 La Regla del Complemento Aplicada

### 💡 Para eventos "al menos uno":

Es más fácil calcular "ninguno" y restar de 1.

$$
P(\text{al menos uno}) = 1 - P(\text{ninguno})
$$

### ⚙️ Ejemplo: Lanzar dado 3 veces

¿Cuál es la probabilidad de obtener al menos un 6?

**Enfoque difícil:** P(exactamente 1 seis) + P(exactamente 2 seises) + P(3 seises)

**Enfoque fácil:**

$$
P(\text{ningún 6}) = \left(\frac{5}{6}\right)^3 = \frac{125}{216}
$$

$$
P(\text{al menos un 6}) = 1 - \frac{125}{216} = \frac{91}{216} \approx 0.421
$$

---

## 🔑 Resumen

| Regla | Fórmula | Condición |
|-------|---------|-----------|
| **Suma general** | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | Siempre |
| **Suma simplificada** | $P(A \cup B) = P(A) + P(B)$ | Si excluyentes |
| **Multiplicación general** | $P(A \cap B) = P(A) \cdot P(B|A)$ | Siempre |
| **Multiplicación simplificada** | $P(A \cap B) = P(A) \cdot P(B)$ | Si independientes |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
P(A) = 0.4, P(B) = 0.5, P(A ∩ B) = 0.2
Calcula P(A ∪ B)

<details>
<summary>Ver solución</summary>

$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.4 + 0.5 - 0.2 = 0.7$$

</details>

### Ejercicio 2
¿Cuál es la probabilidad de sacar una carta que sea corazón O figura (J, Q, K)?

<details>
<summary>Ver solución</summary>

- P(corazón) = 13/52
- P(figura) = 12/52 (3 figuras × 4 palos)
- P(corazón ∩ figura) = 3/52 (J, Q, K de corazones)

$$P = \frac{13}{52} + \frac{12}{52} - \frac{3}{52} = \frac{22}{52} = \frac{11}{26} \approx 0.423$$

</details>

### Ejercicio 3
Se lanzan 2 dados independientes. ¿Cuál es la probabilidad de que ambos muestren 6?

<details>
<summary>Ver solución</summary>

Son independientes:
$$P(\text{ambos 6}) = P(6) \times P(6) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36} \approx 0.028$$

</details>

### Ejercicio 4
De una urna con 5 bolas rojas y 3 azules, se extraen 2 bolas sin reemplazo. ¿Cuál es la probabilidad de que ambas sean rojas?

<details>
<summary>Ver solución</summary>

Sin reemplazo (no son independientes):

$$P(\text{1ra roja}) = \frac{5}{8}$$

$$P(\text{2da roja} | \text{1ra roja}) = \frac{4}{7}$$

$$P(\text{ambas rojas}) = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14} \approx 0.357$$

</details>
