# Trabajo y Fuerza

La integral calcula el trabajo realizado por una fuerza variable. Esta es una de las aplicaciones más importantes en física.

---

## 🎯 ¿Qué vas a aprender?

- Trabajo con fuerza constante
- Trabajo con fuerza variable
- Ley de Hooke (resortes)
- Bombeo de líquidos

---

## 📖 Trabajo con fuerza constante

$$W = F \cdot d$$

- $W$ = trabajo (Joules o ft-lb)
- $F$ = fuerza (Newtons o libras)
- $d$ = desplazamiento

---

## 📖 Trabajo con fuerza variable

Si la fuerza varía con la posición:

$$\boxed{W = \int_a^b F(x)\,dx}$$

---

## 📖 Ley de Hooke (resortes)

La fuerza necesaria para estirar un resorte es proporcional al desplazamiento:

$$F(x) = kx$$

donde $k$ es la constante del resorte.

---

## ⚙️ Ejemplo 1: Resorte

Un resorte tiene constante $k = 50$ N/m. ¿Cuánto trabajo se necesita para estirarlo de 0.1 m a 0.3 m?

$$W = \int_{0.1}^{0.3} 50x\,dx = 50\left[\frac{x^2}{2}\right]_{0.1}^{0.3}$$

$$= 25(0.09 - 0.01) = 25(0.08) = 2 \text{ J}$$

---

## ⚙️ Ejemplo 2: Encontrar la constante

Se requieren 6 J de trabajo para comprimir un resorte de su longitud natural a 0.1 m menos. Encuentra $k$.

$$W = \int_0^{0.1} kx\,dx = k \cdot \frac{(0.1)^2}{2} = 0.005k = 6$$

$$k = 1200 \text{ N/m}$$

---

## 📖 Levantar objetos

El trabajo para levantar un objeto de peso $w$ una altura $h$:

$$W = wh$$

Para levantar algo con peso variable (como una cadena):

$$W = \int_0^h w(y) \cdot dy$$

---

## ⚙️ Ejemplo 3: Cadena colgante

Una cadena de 10 m pesa 3 kg/m. Está colgando de un edificio. ¿Trabajo para subirla completamente?

A distancia $y$ del tope, queda $(10-y)$ metros de cadena, con peso $3(10-y) \cdot 9.8$ N.

$$W = \int_0^{10} 3(10-y) \cdot 9.8\,dy = 29.4\int_0^{10} (10-y)\,dy$$

$$= 29.4\left[10y - \frac{y^2}{2}\right]_0^{10} = 29.4(100 - 50) = 1470 \text{ J}$$

---

## 📖 Bombear líquidos

Para bombear líquido de un tanque:

$$W = \int \rho g \cdot V(y) \cdot d(y)\,dy$$

donde:
- $\rho$ = densidad
- $g$ = gravedad
- $V(y)$ = volumen de la capa a altura $y$
- $d(y)$ = distancia que debe subir esa capa

---

## ⚙️ Ejemplo 4: Tanque cilíndrico

Tanque cilíndrico (radio 2 m, altura 5 m) lleno de agua. Bombear toda el agua a 2 m sobre el borde.

Una capa a altura $y$ (desde el fondo):
- Área: $\pi(2)^2 = 4\pi$ m²
- Espesor: $dy$
- Volumen: $4\pi\,dy$ m³
- Peso: $1000 \cdot 9.8 \cdot 4\pi\,dy$ N
- Distancia a subir: $(5 - y) + 2 = 7 - y$ m

$$W = \int_0^5 9800 \cdot 4\pi(7-y)\,dy$$

$$= 39200\pi\int_0^5 (7-y)\,dy = 39200\pi\left[7y - \frac{y^2}{2}\right]_0^5$$

$$= 39200\pi(35 - 12.5) = 39200\pi \cdot 22.5 \approx 2.77 \times 10^6 \text{ J}$$

---

## ⚙️ Ejemplo 5: Tanque cónico

Tanque cónico invertido (radio superior 3 m, profundidad 6 m), lleno de agua. Bombear a nivel del borde.

Por semejanza: $\frac{r}{y} = \frac{3}{6} = \frac{1}{2}$, así $r = \frac{y}{2}$

Área de capa: $\pi r^2 = \frac{\pi y^2}{4}$

Distancia: $6 - y$

$$W = \int_0^6 9800 \cdot \frac{\pi y^2}{4}(6-y)\,dy$$

$$= 2450\pi\int_0^6 (6y^2 - y^3)\,dy = 2450\pi\left[2y^3 - \frac{y^4}{4}\right]_0^6$$

$$= 2450\pi(432 - 324) = 2450\pi \cdot 108 \approx 831{,}000 \text{ J}$$

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Un resorte requiere 4 J para estirarse 0.2 m desde su posición natural. ¿Cuánto trabajo para estirarlo de 0.2 m a 0.4 m?

<details>
<summary>Ver solución</summary>

$W = k \cdot \frac{(0.2)^2}{2} = 0.02k = 4$ → $k = 200$ N/m

$W_{0.2 \to 0.4} = \int_{0.2}^{0.4} 200x\,dx = 100[x^2]_{0.2}^{0.4} = 100(0.16 - 0.04) = 12$ J
</details>

---

**Ejercicio 2:** Una cuerda de 20 m pesa 0.5 kg/m y cuelga del techo. Trabajo para subirla completamente.

<details>
<summary>Ver solución</summary>

$W = \int_0^{20} 0.5(20-y)(9.8)\,dy = 4.9\int_0^{20}(20-y)\,dy$

$= 4.9[20y - \frac{y^2}{2}]_0^{20} = 4.9(400 - 200) = 980$ J
</details>
