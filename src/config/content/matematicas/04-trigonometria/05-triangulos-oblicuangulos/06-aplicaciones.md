---
title: "Aplicaciones de Triángulos Oblicuángulos"
---

# **Aplicaciones de Triángulos Oblicuángulos**

¿Para qué sirve todo esto? Pues bien, a menos que seas un topógrafo o un capitán de barco, raro vez medirás triángulos por diversión. Pero en el mundo real, los triángulos oblicuángulos están en todas partes: desde medir montañas inaccesibles hasta calcular rutas de aviones que se desvían por el viento.

---

## 🎯 ¿Qué vas a aprender?

- Cómo medir la altura de un objeto sin acercarte a él (el problema de los dos observadores).
- Cómo calcular distancias en navegación usando rumbos y brújulas.
- Cómo calcular el área de cualquier terreno irregular.
- La súper Fórmula de Herón para áreas (sin saber la altura).

---

## 🗺️ Problema 1: Navegación y Rumbos

En el mar y en el aire, casi nunca vas en línea recta. El viento te empuja, o tienes que esquivar una tormenta.

**El Problema:**
Un avión vuela 300 km hacia el Este, y luego gira 60° hacia el Norte y vuela otros 400 km. ¿A qué distancia está del punto de partida?

**Solución:**
1.  Dibuja el trayecto. Tienes dos lados (300 y 400).
2.  El ángulo de giro es exterior. El ángulo interior del triángulo es $180° - 60° = 120°$.
3.  Tienes Lado-Ángulo-Lado. Usa **Ley de Cosenos**.

$$
d^2 = 300^2 + 400^2 - 2(300)(400)\cos(120°)
$$
$$
d^2 = 90,000 + 160,000 - 240,000(-0.5)
$$
$$
d^2 = 250,000 + 120,000 = 370,000
$$
$$
d = \sqrt{370,000} \approx 608 \text{ km}
$$

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
    <strong style="color: #1e293b; font-size: 0.95rem; margin-left: 0.3rem;">Aplicación: Navegación</strong>
  </div>

![Aplicación de navegación](/images/trigonometria/triangulos-oblicuangulos/aplicacion-navegacion.svg)

</div>

---

## 🏔️ Problema 2: Alturas Inaccesibles

Quieres medir la altura de una montaña, pero no puedes llegar a la base (hay un río o un precipicio). ¿Qué haces?

**El Método de los Dos Observadores:**
1.  Mides el ángulo de elevación desde el punto A ($30°$).
2.  Caminas 100 metros hacia la montaña hasta el punto B.
3.  Vuelves a medir el ángulo ($45°$).

¡Ahora tienes un triángulo oblicuángulo con un lado conocido (100 m) y muchos ángulos!
1.  Usas la Ley de Senos para hallar la distancia de B a la cima.
2.  Usas seno básico (SOH) para hallar la altura.

---

## 📐 Problema 3: Áreas de Terrenos

¿Cómo mides el área de un parque triangular si no sabes la altura?

### Opción A: Fórmula del Seno
Si conoces dos lados y el ángulo del medio:
$$
\text{Área} = \frac{1}{2} a b \sin C
$$

### Opción B: Fórmula de Herón
Si solo conoces los tres lados ($a, b, c$), primero calculas el semiperímetro ($s$):
$$
s = \frac{a + b + c}{2}
$$
Y luego:
$$
\text{Área} = \sqrt{s(s-a)(s-b)(s-c)}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula el área de un triángulo con lados 3, 4 y 5 usando Herón.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$s = (3+4+5)/2 = 6$.
Área $= \sqrt{6(6-3)(6-4)(6-5)} = \sqrt{6 \cdot 3 \cdot 2 \cdot 1} = \sqrt{36} = 6$.

**Respuesta:** $\boxed{6}$
</details>

---

### Ejercicio 2
Un barco navega 50 km al Norte y luego 50 km al Este. ¿Distancia al origen?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es un triángulo rectángulo (Norte y Este son perpendiculares).
$d = \sqrt{50^2 + 50^2} = 50\sqrt{2} \approx 70.7$.

**Respuesta:** $\boxed{70.7 \text{ km}}$
</details>

---

### Ejercicio 3
Dos fuerzas de 10 N y 20 N tiran de un objeto con un ángulo de 60° entre ellas. Halla la fuerza resultante.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
En vectores, el ángulo en el triángulo de suma es el suplementario ($180-60=120$).
$R^2 = 10^2 + 20^2 - 2(10)(20)\cos(120)$.
$R = \sqrt{100+400+200} = \sqrt{700} \approx 26.46$.

**Respuesta:** $\boxed{26.46 \text{ N}}$
</details>

---

### Ejercicio 4
Calcula el área si $a=10, b=10, C=30°$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Área $= 0.5(10)(10)\sin 30° = 50(0.5) = 25$.

**Respuesta:** $\boxed{25}$
</details>

---

### Ejercicio 5
Para medir el ancho de un río, un topógrafo mide una base de 100m paralela al río. Los ángulos hacia un árbol en la otra orilla son 40° y 60°. ¿Qué ley usas primero?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Tienes un lado y dos ángulos adyacentes. Puedes hallar el tercer ángulo. Es caso ALA. Ley de Senos.

**Respuesta:** **Ley de Senos**
</details>

---

### Ejercicio 6
Calcula el semiperímetro ($s$) de un triángulo equilátero de lado 10.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$s = (10+10+10)/2 = 15$.

**Respuesta:** $\boxed{15}$
</details>

---

### Ejercicio 7
Si dos lados miden 100 y el ángulo entre ellos es 90°, ¿cuál es el área?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Triángulo rectángulo. Área = base $\cdot$ altura / 2.
$100 \cdot 100 / 2 = 5000$.

**Respuesta:** $\boxed{5000}$
</details>

---

### Ejercicio 8
¿Qué fórmula usarías para el área si solo tienes los 3 lados?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
La de Herón, porque no requiere ángulos.

**Respuesta:** **Fórmula de Herón**
</details>

---

### Ejercicio 9
Un poste se inclina 10° respecto a la vertical hacia el sol. Proyecta una sombra de 20m cuando el sol está a 60°. ¿Cuál es la longitud del poste?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Es un problema clásico de Ley de Senos.
Ángulo del poste con el suelo: $90+10 = 100°$ (o $80$, depende de la orientación).
Ángulo del sol: $60°$. Triple ángulo: $180-100-60 = 20°$.
$L/\sin 60 = 20/\sin 20$.

**Respuesta:** **Usar Ley de Senos**
</details>

---

### Ejercicio 10
Si caminas 10m, giras 90°, caminas 10m, giras 90°, caminas 10m. ¿A qué distancia estás del inicio?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Hiciste 3 lados de un cuadrado. Te falta 1 lado de 10m para cerrar.
Distancia = 10m.

**Respuesta:** $\boxed{10 \text{ m}}$
</details>

---

## 🔑 Resumen

| Problema | Herramienta Clave |
| :--- | :--- |
| **Navegación** | Ley de Cosenos (casi siempre LAL). |
| **Áreas (lados y ángulo)** | Fórmula del Seno ($0.5 a b \sin C$). |
| **Áreas (solo lados)** | Fórmula de Herón ($\sqrt{s(s-a)\dots}$). |
| **Alturas inaccesibles** | Ley de Senos (Dos observadores). |

> **Conclusión:** La trigonometría no se queda en el papel. Es la base del GPS, la arquitectura y hasta de los videojuegos 3D. ¡Donde hay una distancia, hay un triángulo!
