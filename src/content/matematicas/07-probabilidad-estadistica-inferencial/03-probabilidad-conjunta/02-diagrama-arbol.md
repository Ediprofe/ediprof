# Diagrama de Árbol

Los **diagramas de árbol** son una herramienta visual poderosa para organizar experimentos con múltiples etapas y calcular probabilidades de secuencias de eventos.

---

## 🎯 ¿Qué vas a aprender?

- Cómo construir un diagrama de árbol
- Calcular probabilidades en cada rama
- Usar el árbol para resolver problemas complejos
- La regla del producto a lo largo de ramas

---

## 📖 ¿Qué es un Diagrama de Árbol?

> Un **diagrama de árbol** representa gráficamente todas las secuencias posibles de resultados de un experimento en múltiples etapas.

### 💡 Estructura:

- Cada **nodo** representa un punto de decisión o evento
- Cada **rama** representa un resultado posible
- Las **hojas** (extremos) representan los resultados finales
- Cada rama tiene una **probabilidad** asociada

---

## 📖 Construcción del Diagrama

### ⚙️ Ejemplo: Dos lanzamientos de moneda

```
                    Inicio
                   /      \
               C(1/2)    S(1/2)
               /    \    /    \
           C(1/2) S(1/2) C(1/2) S(1/2)
             |      |      |      |
            CC     CS     SC     SS
          (1/4)  (1/4)  (1/4)  (1/4)
```

### 💡 Regla del producto:

La probabilidad de un camino completo es el **producto** de las probabilidades de cada rama.

$$
P(CC) = P(C_1) \times P(C_2) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}
$$

---

## 📖 Ejemplo: Extracción sin Reemplazo

Una urna tiene 3 bolas rojas y 2 azules. Se extraen 2 sin reemplazo.

```
                     Inicio
                   /        \
               R(3/5)      A(2/5)
              /     \      /     \
          R(2/4)  A(2/4) R(3/4) A(1/4)
            |       |      |       |
           RR      RA     AR      AA
```

### 💡 Cálculo de probabilidades:

$P(RR) = \frac{3}{5} \times \frac{2}{4} = \frac{6}{20} = \frac{3}{10}$

$P(RA) = \frac{3}{5} \times \frac{2}{4} = \frac{6}{20} = \frac{3}{10}$

$P(AR) = \frac{2}{5} \times \frac{3}{4} = \frac{6}{20} = \frac{3}{10}$

$P(AA) = \frac{2}{5} \times \frac{1}{4} = \frac{2}{20} = \frac{1}{10}$

**Verificación:** $\frac{3}{10} + \frac{3}{10} + \frac{3}{10} + \frac{1}{10} = 1$ ✓

### 💡 Pregunta: P(al menos una roja)

$$
P(\text{al menos una R}) = P(RR) + P(RA) + P(AR) = \frac{3}{10} + \frac{3}{10} + \frac{3}{10} = \frac{9}{10}
$$

---

## 📖 Ejemplo con Probabilidades Condicionales

Una fábrica tiene 3 máquinas:
- Máquina A produce 50% de las piezas, 2% defectuosas
- Máquina B produce 30% de las piezas, 3% defectuosas
- Máquina C produce 20% de las piezas, 5% defectuosas

### 💡 Diagrama de árbol:

```
                 Inicio
            /      |      \
         A(0.5)  B(0.3)  C(0.2)
         /  \    /  \    /  \
      D    D'  D    D'  D    D'
    (0.02)(0.98)(0.03)(0.97)(0.05)(0.95)
```

### 💡 ¿Cuál es P(defectuosa)?

$$
P(D) = P(A) \cdot P(D|A) + P(B) \cdot P(D|B) + P(C) \cdot P(D|C)
$$
$$
= 0.5 \times 0.02 + 0.3 \times 0.03 + 0.2 \times 0.05
$$
$$
= 0.01 + 0.009 + 0.01 = 0.029 = 2.9\%
$$

### 💡 Si una pieza es defectuosa, ¿de qué máquina probablemente vino? (Bayes)

$$
P(A|D) = \frac{P(A \cap D)}{P(D)} = \frac{0.01}{0.029} = 0.345
$$

$$
P(B|D) = \frac{0.009}{0.029} = 0.310
$$

$$
P(C|D) = \frac{0.01}{0.029} = 0.345
$$

---

## 📖 Reglas del Diagrama de Árbol

### 💡 Regla 1: Ramas de un nodo suman 1

Las probabilidades de todas las ramas que salen del mismo nodo deben sumar 1.

### 💡 Regla 2: Multiplicar a lo largo

Para obtener la probabilidad de un camino, **multiplica** las probabilidades de todas las ramas.

### 💡 Regla 3: Sumar caminos alternativos

Si un evento puede ocurrir por diferentes caminos, **suma** las probabilidades de esos caminos.

---

## 📖 Aplicación: El Problema del Monty Hall

En un concurso hay 3 puertas:
- 1 tiene un carro
- 2 tienen cabras

Eliges una puerta. El presentador (que sabe dónde está el carro) abre otra puerta mostrando una cabra. ¿Deberías cambiar de puerta?

### 💡 Análisis con árbol:

**Si no cambias:** P(ganar) = 1/3

**Si cambias:**
- Si elegiste carro (1/3): cambiar → pierdes
- Si elegiste cabra (2/3): cambiar → ganas

P(ganar | cambias) = 2/3

**Conclusión:** ¡Siempre deberías cambiar! Doblas tu probabilidad de ganar.

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Nodo** | Punto de decisión o evento |
| **Rama** | Resultado posible con su probabilidad |
| **Camino** | Secuencia desde inicio hasta una hoja |
| **P(camino)** | Producto de probabilidades de las ramas |
| **P(evento)** | Suma de P de todos los caminos que llevan al evento |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Se lanzan 3 monedas. Usa un diagrama de árbol para encontrar:
a) P(exactamente 2 caras)
b) P(al menos 1 sello)

<details>
<summary>Ver solución</summary>

Los 8 resultados equiprobables (cada uno con P = 1/8):
CCC, CCS, CSC, CSS, SCC, SCS, SSC, SSS

a) Exactamente 2 caras: CCS, CSC, SCC
$$P = 3/8 = 0.375$$

b) Al menos 1 sello: Todos excepto CCC
$$P = 7/8 = 0.875$$

O usando complemento: $P = 1 - P(\text{ningún sello}) = 1 - 1/8 = 7/8$

</details>

### Ejercicio 2
Una caja tiene 4 bolas blancas y 6 negras. Se extraen 2 sin reemplazo. ¿Cuál es P(una de cada color)?

<details>
<summary>Ver solución</summary>

**Diagrama:**
```
            Inicio
           /      \
        B(4/10)  N(6/10)
        /    \    /    \
     B(3/9) N(6/9) B(4/9) N(5/9)
```

P(BN) = (4/10)(6/9) = 24/90
P(NB) = (6/10)(4/9) = 24/90

P(una de cada) = 24/90 + 24/90 = 48/90 = 8/15 ≈ 0.533

</details>

### Ejercicio 3
Un estudiante tiene 70% de probabilidad de pasar el primer examen. Si lo pasa, tiene 90% de pasar el segundo. Si no pasa el primero, solo tiene 40% de pasar el segundo.

a) ¿Cuál es P(pasa ambos)?
b) ¿Cuál es P(pasa exactamente uno)?

<details>
<summary>Ver solución</summary>

**Diagrama:**
```
       Inicio
      /      \
   P1(0.7)  F1(0.3)
   /    \    /    \
P2(0.9) F2(0.1) P2(0.4) F2(0.6)
```

a) P(pasa ambos) = P(P1) × P(P2|P1) = 0.7 × 0.9 = 0.63

b) P(exactamente uno):
- Pasa 1, falla 2: 0.7 × 0.1 = 0.07
- Falla 1, pasa 2: 0.3 × 0.4 = 0.12

Total = 0.07 + 0.12 = 0.19

</details>
