---
title: "Problemas con K"
---

# Problemas con K

Resolver problemas de equilibrio implica usar la constante K junto con las concentraciones. Los problemas típicos incluyen calcular K a partir de datos experimentales o encontrar concentraciones conociendo K.

---

## 🎯 ¿Qué vas a aprender?

- Calcular K a partir de concentraciones de equilibrio
- Calcular concentraciones a partir de K
- Resolver problemas tipo con tabla ICE
- Estrategias de solución

---

## 📊 Tipos de Problemas

| Tipo | Datos | Incógnita |
|------|-------|-----------|
| **Tipo 1** | Concentraciones de equilibrio | K |
| **Tipo 2** | K y concentraciones iniciales | Concentraciones de equilibrio |
| **Tipo 3** | K y algunas concentraciones de eq. | Otras concentraciones |

---

## 📖 Tipo 1: Calcular K

### Problema:

En equilibrio para N₂ + O₂ ⇌ 2NO:
- [N₂] = 0.033 M
- [O₂] = 0.0810 M
- [NO] = 0.00250 M

¿Cuál es Kc?

### Solución:

$$
K_c = \frac{[\text{NO}]^2}{[\text{N}_2][\text{O}_2]} = \frac{(0.00250)^2}{(0.033)(0.0810)}
$$

$$
K_c = \frac{6.25 \times 10^{-6}}{2.67 \times 10^{-3}} = \boxed{2.34 \times 10^{-3}}
$$

---

## 📖 Tipo 2: Calcular Concentraciones

### Problema:

Para H₂ + I₂ ⇌ 2HI, Kc = 54.3 a 430°C. Si [H₂]₀ = [I₂]₀ = 0.5 M, ¿cuáles son las concentraciones de equilibrio?

### Solución:

**Paso 1: Tabla ICE**

|  | H₂ | I₂ | HI |
|--|----|----|-----|
| **I** | 0.5 | 0.5 | 0 |
| **C** | -x | -x | +2x |
| **E** | 0.5-x | 0.5-x | 2x |

**Paso 2: Expresión de K**

$$
54.3 = \frac{(2x)^2}{(0.5-x)^2} = \frac{4x^2}{(0.5-x)^2}
$$

**Paso 3: Tomar raíz cuadrada**

$$
\sqrt{54.3} = \frac{2x}{0.5-x}
$$

$$
7.37 = \frac{2x}{0.5-x}
$$

**Paso 4: Resolver**

$$
7.37(0.5-x) = 2x
$$

$$
3.685 - 7.37x = 2x
$$

$$
3.685 = 9.37x
$$

$$
x = 0.393 \text{ M}
$$

**Paso 5: Concentraciones de equilibrio**

- [H₂] = [I₂] = 0.5 - 0.393 = **0.107 M**
- [HI] = 2(0.393) = **0.786 M**

---

## 📖 Tipo 3: Encontrar una Concentración

### Problema:

Para la reacción A ⇌ 2B, Kc = 0.25. Si [A] = 0.50 M en equilibrio, ¿cuál es [B]?

### Solución:

$$
K_c = \frac{[\text{B}]^2}{[\text{A}]}
$$

$$
0.25 = \frac{[\text{B}]^2}{0.50}
$$

$$
[\text{B}]^2 = 0.125
$$

$$
[\text{B}] = \boxed{0.354 \text{ M}}
$$

---

## 📖 Estrategias de Solución

### 💡 1. Identifica el tipo de problema

¿Tienes K o necesitas calcularlo?

### 💡 2. Escribe la expresión de K correctamente

Verifica coeficientes y fases.

### 💡 3. Usa tabla ICE si hay incógnitas

Organiza las concentraciones sistemáticamente.

### 💡 4. Simplifica si es posible

- Si K es muy grande o muy pequeño, usa aproximaciones
- Busca formas de tomar raíz cuadrada

### 💡 5. Verifica tu respuesta

Sustituye las concentraciones finales en K para confirmar.

---

## 📖 Verificación

### 💡 Siempre verifica:

Después de resolver, calcula K con tus valores de equilibrio y compara con el K dado.

### ⚙️ Del ejemplo anterior:

$$
K = \frac{(0.786)^2}{(0.107)(0.107)} = \frac{0.618}{0.0114} = 54.2 \approx 54.3 \checkmark
$$

---

## 🔑 Resumen

| Paso | Acción |
|------|--------|
| 1 | Identificar datos e incógnita |
| 2 | Escribir expresión de K |
| 3 | Armar tabla ICE si es necesario |
| 4 | Resolver algebraicamente |
| 5 | Verificar el resultado |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Para 2SO₂ + O₂ ⇌ 2SO₃, en equilibrio: [SO₂] = 0.1 M, [O₂] = 0.2 M, [SO₃] = 0.4 M. Calcula Kc.

<details>
<summary>Ver solución</summary>

$$
K_c = \frac{[SO_3]^2}{[SO_2]^2[O_2]} = \frac{(0.4)^2}{(0.1)^2(0.2)}
$$

$$
K_c = \frac{0.16}{0.002} = \boxed{80}
$$

</details>

### Ejercicio 2
Para A ⇌ B, Kc = 4. Si [A]₀ = 1 M, ¿cuál es [B] en equilibrio?

<details>
<summary>Ver solución</summary>

Tabla ICE:

|  | A | B |
|--|---|---|
| I | 1 | 0 |
| C | -x | +x |
| E | 1-x | x |

$$
4 = \frac{x}{1-x}
$$

$$
4 - 4x = x
$$

$$
x = 0.8 \text{ M}
$$

[B] = **0.8 M**, [A] = **0.2 M**

</details>

### Ejercicio 3
Si Kc = 100 para una reacción y en equilibrio [productos] = 50 M², ¿cuál es [reactivos]?

<details>
<summary>Ver solución</summary>

$$
K = \frac{[\text{productos}]}{[\text{reactivos}]}
$$

$$
100 = \frac{50}{[\text{reactivos}]}
$$

$$
[\text{reactivos}] = \frac{50}{100} = \boxed{0.5 \text{ M}}
$$

(Nota: Las "unidades" dependen de la estequiometría específica)

</details>
