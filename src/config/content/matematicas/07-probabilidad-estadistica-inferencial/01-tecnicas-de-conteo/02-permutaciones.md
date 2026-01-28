---
title: "Permutaciones"
---

# **Permutaciones**

Imagina una ensalada de frutas con manzana, pera y banano. Si cambias el orden (banano, manzana, pera), sigue siendo la misma ensalada. El orden no importa.
Ahora imagina la clave de tu celular: 1-2-3-4. Si pones 4-3-2-1, no desbloquea. El orden SÍ importa.
Cuando el **orden importa**, hablamos de **Permutaciones**.

---

## 🎯 ¿Qué vas a aprender?

- Calcular el factorial de un número ($n!$).
- Diferenciar cuándo el orden importa (Permutación) y cuándo no.
- Calcular permutaciones de un grupo completo ($n!$).
- Calcular permutaciones parciales ($nPr$).
- Resolver casos especiales como mesas redondas y elementos repetidos.

---

## El Factorial ($n!$)

Es el motor de las permutaciones. Multiplicas el número por todos sus antecesores hasta el 1.
$$ n! = n \times (n-1) \times ... \times 1 $$

- $3! = 3 \times 2 \times 1 = 6$
- $5! = 120$
- **Ojo:** $0! = 1$ (por definición matemática).

---

## Tipos de Permutaciones

### 1. Permutación Lineal (Usar todos los elementos)
Tienes $n$ objetos y quieres ordenarlos todos en una fila.
$$ P_n = n! $$

#### ⚙️ Ejemplos Resueltos
1.  **Fila de Personas:** 5 amigos en el cine. ¿Formas de sentarse?
    $5! = 120$ formas.
2.  **Libros en Repisa:** 4 libros de Harry Potter.
    $4! = 24$ órdenes posibles.
3.  **Anagramas Simples:** Palabra "SOL". (S-O-L, S-L-O, O-S-L...).
    $3! = 6$ palabras.
4.  **Banderas:** 3 banderas de colores distintos en un asta.
    $3! = 6$.
5.  **Ranking:** 2 corredores. ¿Podios posibles?
    (A-B, B-A) $\to 2! = 2$.

### 2. Permutación Parcial ($nPr$) (Usar solo algunos)
Tienes $n$ objetos, pero solo vas a ordenar $r$ de ellos.
$$ _nP_r = \frac{n!}{(n-r)!} $$

#### ⚙️ Ejemplos Resueltos
1.  **El Podio:** 10 corredores, solo 3 medallas (Oro, Plata, Bronce).
    $_10P_3 = 10 \cdot 9 \cdot 8 = 720$. (O $\frac{10!}{7!}$).
2.  **La Directiva:** 20 alumnos. Elegir Presidente y Vicepresidente.
    $_20P_2 = 20 \cdot 19 = 380$.
3.  **Claves:** Digitos 0-9. Clave de 4 dígitos sin repetir.
    $_10P_4 = 10 \cdot 9 \cdot 8 \cdot 7 = 5,040$.
4.  **Rifas:** 50 boletas. 1er premio (Carro), 2do premio (Moto).
    $_50P_2 = 50 \cdot 49 = 2,450$.
5.  **Fotos:** Familia de 6, pero la foto es solo para 4.
    $_6P_4 = 6 \cdot 5 \cdot 4 \cdot 3 = 360$.

### 3. Permutación con Repetición
Cuando algunos elementos son idénticos (ej: dos fichas rojas iguales).
$$ P = \frac{n!}{k_1! \cdot k_2! ...} $$

#### ⚙️ Ejemplos Resueltos
1.  **Palabra "MAMA":** 4 letras, pero la M se repite (2) y la A se repite (2).
    $4! / (2! \cdot 2!) = 24 / 4 = 6$.
2.  **Palabra "BEBE":** Similar. $24 / 4 = 6$.
3.  **Banderas:** 5 banderas: 3 rojas, 2 azules.
    $5! / (3! \cdot 2!) = 120 / (6 \cdot 2) = 10$.
4.  **Moneda:** Lanzas 4 veces. ¿Formas de obtener 3 caras y 1 sello?
    $4! / (3! \cdot 1!) = 4$.
5.  **Palabra "MISSISSIPPI":** 11 letras. (M=1, I=4, S=4, P=2).
    $11! / (1! \cdot 4! \cdot 4! \cdot 2!) = 34,650$.

### 4. Permutación Circular
En una mesa redonda, no hay "primero" ni "último". Solo importa quién está a la derecha de quién. Se fija uno y se ordenan los demás.
$$ P_c = (n-1)! $$

#### ⚙️ Ejemplos Resueltos
1.  **Mesa Redonda:** 5 personas cenando.
    $(5-1)! = 4! = 24$.
2.  **Ronda Infantil:** 10 niños jugando a la ronda.
    $9! = 362,880$.
3.  **Collar:** 6 perlas distintas en un hilo cerrado.
    $(5!) / 2 = 60$. (Dividimos por 2 porque darle la vuelta al collar es lo mismo).
4.  **Llavero:** 4 llaves en una argolla.
    $(3!) / 2 = 3$.
5.  **Reunión:** 3 socios en mesa circular.
    $2! = 2$.

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $6!$.

<details>
<summary>Ver solución</summary>

**Cálculo:** $6 \times 5 \times 4 \times 3 \times 2 \times 1 = 720$.
**Resultado:** $\boxed{720}$

</details>

### Ejercicio 2
Tienes 8 cuadros y quieres colgar 3 en fila. ¿Importa el orden?

<details>
<summary>Ver solución</summary>

**Análisis:** Visualmente, Cuadro A - B - C es distinto de C - B - A. Sí importa.
**Resultado:** $\boxed{\text{Sí, Permutación}}$

</details>

### Ejercicio 3
Calcula $_5P_2$.

<details>
<summary>Ver solución</summary>

**Cálculo:** $5 \times 4$ (los dos primeros factores).
**Resultado:** $\boxed{20}$

</details>

### Ejercicio 4
Palabra "OSO". ¿Cuántas permutaciones tiene?

<details>
<summary>Ver solución</summary>

**Repetición:** 3 letras, O se repite 2 veces.
$3! / 2! = 6/2 = 3$. (OSO, SOO, OOS).
**Resultado:** $\boxed{3}$

</details>

### Ejercicio 5
6 personas en una mesa redonda.

<details>
<summary>Ver solución</summary>

**Circular:** $(6-1)! = 5!$.
**Resultado:** $\boxed{120}$

</details>

### Ejercicio 6
Formas de premiar Campeón y Subcampeón entre 4 equipos.

<details>
<summary>Ver solución</summary>

**Parcial:** $_4P_2 = 4 \times 3$.
**Resultado:** $\boxed{12}$

</details>

### Ejercicio 7
Ordenar 5 libros de matemáticas.

<details>
<summary>Ver solución</summary>

**Total:** $5!$.
**Resultado:** $\boxed{120}$

</details>

### Ejercicio 8
¿Cuántos números de 3 cifras (sin repetir) se hacen con 1, 2, 3?

<details>
<summary>Ver solución</summary>

**Total:** $3!$.
**Resultado:** $\boxed{6}$

</details>

### Ejercicio 9
Si en una carrera de 100 personas solo importa el ganador, ¿es permutación o combinación?

<details>
<summary>Ver solución</summary>

**Análisis:** Importa quién llega de PRIMERO.
**Resultado:** $\boxed{\text{Permutación (de 1)}}$

</details>

### Ejercicio 10
Clave de 3 dígitos (0-9) sin repetir.

<details>
<summary>Ver solución</summary>

**Cálculo:** $10 \times 9 \times 8$.
**Resultado:** $\boxed{720}$

</details>

---

## 🔑 Resumen

| Tipo | Fórmula | Clave |
|------|---------|-------|
| **Lineal ($n$)** | $n!$ | Todos en fila. |
| **Parcial ($r$)** | $\frac{n!}{(n-r)!}$ | Solo algunos importan (Podio). |
| **Circular** | $(n-1)!$ | Sin principio ni fin. |
| **Repetición** | $\frac{n!}{a!b!...}$ | Elementos idénticos. |

> **Conclusión:** Si cambiar de lugar cambia el resultado (como en una contraseña o una carrera), estás ante una **Permutación**. ¡Multiplica en bajada!
