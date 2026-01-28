---
title: "Posiciones entre Circunferencias"
---

# **Posiciones entre Circunferencias**

Dos burbujas de jabón flotando pueden hacer tres cosas: mantenerse separadas, unirse compartiendo una pared, o que una se "coma" a la otra. Así se comportan también las circunferencias.

---

## 🎯 ¿Qué vas a aprender?

- Clasificar la posición de dos circunferencias comparando la distancia ($d$) entre sus centros con la suma o resta de sus radios ($R$ y $r$).
- Distinguir entre tangentes exteriores e interiores.
- Identificar cuándo dos circunferencias son secantes o concéntricas.

---

## 📏 Clasificación por Distancia entre Centros ($d$)

Para saber qué hacen dos circunferencias, comparamos la distancia entre sus centros con sus radios.
Sean $R$ el radio mayor y $r$ el radio menor.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Posiciones Relativas</strong>
  </div>
  <img src="/images/geometria/circulos/posiciones-circunferencias.svg" alt="Diagrama de posiciones relativas entre circunferencias" style="width: 100%; height: auto;">
</div>

### 1. Exteriores (Separadas)
Están lejos una de la otra. No se tocan.
*   **Condición:** La distancia es mayor que la suma de sus radios.
$$ d > R + r $$

### 2. Tangentes Exteriores (Se besan por fuera)
Se tocan en un solo punto, pero una está fuera de la otra.
*   **Condición:** La distancia es exactamente la suma de los radios.
$$ d = R + r $$

### 3. Secantes (Se cruzan)
Tienen dos puntos en común, como los aros olímpicos.
*   **Condición:** La distancia es menor que la suma, pero mayor que la diferencia.
$$ R - r < d < R + r $$

### 4. Tangentes Interiores (Se besan por dentro)
Se tocan en un punto, pero una está dentro de la otra.
*   **Condición:** La distancia es exactamente la diferencia de los radios.
$$ d = R - r $$

### 5. Interiores (Una dentro de otra)
Una está flotando dentro de la otra sin tocarla.
*   **Condición:** La distancia es menor que la diferencia de los radios.
$$ d < R - r $$

### 6. Concéntricas (Mismo centro)
Comparten el mismo centro ("Ojo de buey").
*   **Condición:** La distancia es cero.
$$ d = 0 $$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Identificación

Dos circunferencias tienen radios de 8 cm y 3 cm. La distancia entre centros es de 11 cm. ¿Cómo están posicionadas?

**Razonamiento:**
Sumamos radios: $8 + 3 = 11$.
Restamos radios: $8 - 3 = 5$.
La distancia ($d=11$) es igual a la suma.

**Resultado:**
$$
\boxed{\text{Tangentes Exteriores}}
$$

### Ejemplo 2: Cálculo de Distancia

¿Cuál debe ser la distancia entre centros para que dos circunferencias de radios 10 cm y 6 cm sean tangentes interiores?

**Razonamiento:**
Para tangencia interior, $d = R - r$.
$$
d = 10 - 6 = 4
$$

**Resultado:**
$$
\boxed{4 \text{ cm}}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
$R=10, r=5, d=20$. ¿Posición?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$R+r = 15$.
$d=20 > 15$. Estan muy lejos.

**Resultado:**
$$
\boxed{\text{Exteriores}}
$$

</details>

### Ejercicio 2
$R=7, r=3, d=2$. ¿Posición?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$R-r = 4$.
$d=2 < 4$. Está muy adentro.

**Resultado:**
$$
\boxed{\text{Interiores}}
$$

</details>

### Ejercicio 3
$R=6, r=4, d=8$. ¿Posición?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Suma = 10. Resta = 2.
$2 < 8 < 10$. Está en el medio.

**Resultado:**
$$
\boxed{\text{Secantes}}
$$

</details>

### Ejercicio 4
Si dos circunferencias comparten el mismo centro, ¿cómo se llaman?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Concéntricas}
$$

</details>

### Ejercicio 5
Calcula la distancia de centros para que circunferencias de radio 12 y 5 sean tangentes interiores.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
d = 12 - 5
$$

**Resultado:**
$$
\boxed{7}
$$

</details>

### Ejercicio 6
$d=0$. ¿Posición?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Concéntricas}
$$

</details>

### Ejercicio 7
¿Cuántos puntos de contacto tienen dos circunferencias secantes?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
2
$$

</details>

### Ejercicio 8
Si $R=5$ y $r=5$, y son tangentes exteriores, ¿cuánto es $d$?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$$
d = 5 + 5
$$

**Resultado:**
$$
\boxed{10}
$$

</details>

### Ejercicio 9
Para que sean interiores, la distancia debe ser menor que...

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
R - r
$$

</details>

### Ejercicio 10
Dos engranajes se tocan por fuera. Uno tiene radio 20 cm y el otro 30 cm. ¿A qué distancia están sus ejes?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Engranajes tangentes exteriores.
$$
d = 20 + 30
$$

**Resultado:**
$$
\boxed{50 \text{ cm}}
$$

</details>

---

## 🔑 Resumen

| Posición | Distancia ($d$) | Puntos |
| :--- | :--- | :---: |
| **Exteriores** | $> R+r$ | 0 |
| **Tangentes Ext.** | $= R+r$ | 1 |
| **Secantes** | Entre resta y suma | 2 |
| **Tangentes Int.** | $= R-r$ | 1 |
| **Interiores** | $< R-r$ | 0 |

> La distancia te cuenta la historia completa de su relación.
