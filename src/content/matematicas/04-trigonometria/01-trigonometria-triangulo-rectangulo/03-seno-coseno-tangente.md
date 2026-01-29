# **Seno, Coseno y Tangente**

Si tuvieras que escalar una montaña, el **Seno** te diría cuánto subes y el **Coseno** cuánto avanzas horizontalmente. Estas no son solo operaciones matemáticas abstractas; son las herramientas que usan tu teléfono para rotar la pantalla o los ingenieros para construir puentes.

---

## 🎯 ¿Qué vas a aprender?

- Entender profundamente qué miden el Seno, Coseno y Tangente.
- La identidad sagrada: $\sin^2 + \cos^2 = 1$.
- Cómo se comportan estas funciones cuando el ángulo cambia.
- Relacionar la Tangente con las otras dos ($\tan = \sin / \cos$).

---

## 📈 Comportamiento Visual

Antes de entrar en fórmulas, mira cómo se "mueven" estas funciones cuando el ángulo va de $0^{\circ}$ a $90^{\circ}$.

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0;">
  <div style="margin-bottom: 0.5rem;">
    <span style="font-size: 1.1rem;">📈</span> <strong style="color: #1e293b;">La Carrera de las Razones</strong>
  </div>
  <div id="echarts-sincostan" style="width: 100%; height: 380px; border-radius: 8px;"></div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof echarts !== 'undefined' && document.getElementById('echarts-sincostan')) {
    var chart = echarts.init(document.getElementById('echarts-sincostan'));
    var sinData = [], cosData = [], tanData = [];
    for (var deg = 0; deg <= 90; deg += 2) {
      var rad = deg * Math.PI / 180;
      sinData.push([deg, Math.sin(rad)]);
      cosData.push([deg, Math.cos(rad)]);
      if (deg < 85) tanData.push([deg, Math.tan(rad)]);
    }
    chart.setOption({
      animation: true,
      legend: { data: ['sin θ', 'cos θ', 'tan θ'], top: 10 },
      grid: { left: '12%', right: '5%', top: '18%', bottom: '15%' },
      xAxis: { type: 'value', name: 'θ (grados)', min: 0, max: 90, axisLabel: { formatter: '{value}°' } },
      yAxis: { type: 'value', min: 0, max: 3 },
      series: [
        { name: 'sin θ', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#3b82f6' }, data: sinData },
        { name: 'cos θ', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#22c55e' }, data: cosData },
        { name: 'tan θ', type: 'line', symbol: 'none', lineStyle: { width: 3, color: '#f97316' }, data: tanData }
      ]
    });
    window.addEventListener('resize', function() { chart.resize(); });
  }
});
</script>

---

## 🔍 Análisis Profundo

### 1. Seno ($\sin$)
Míralo como el porcentaje de "altura".
*   Si el ángulo es pequeño ($0^{\circ}$), la altura es nada ($\sin(0) = 0$).
*   Si el ángulo es recto ($90^{\circ}$), toda la hipotenusa es vertical ($\sin(90) = 1$).

### 2. Coseno ($\cos$)
Míralo como el porcentaje de "suelo" o ancho.
*   Si el ángulo es $0^{\circ}$, todo es suelo ($\cos(0) = 1$).
*   Si el ángulo es $90^{\circ}$, no hay ancho ($\cos(90) = 0$).

### 3. Tangente ($\tan$)
Es la relación de aspecto (Altura / Ancho).
*   En $45^{\circ}$, la altura es igual al ancho, así que $\tan(45) = 1$.
*   Cerca de $90^{\circ}$, la altura es enorme comparada con el ancho, así que la tangente se dispara al infinito.

![Triángulo con razones trigonométricas](/images/geometria/trigonometria/03-triangulo-345.svg)

---

## 🔗 Relaciones Fundamentales

### La Identidad Pitagórica
Esta ecuación nunca falla. Es el Teorema de Pitágoras disfrazado.

$$
\sin^2(\theta) + \cos^2(\theta) = 1
$$

Significa que la suma de los cuadrados de las "porciones" siempre completa el triángulo.

### La Tangente como Cociente
Si sabes cuánto valen el seno y el coseno, no necesitas calcular la tangente por separado.

$$
\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}
$$

---

## ⚙️ Ejemplos Resueltos

### Ejemplo 1: Usando la Identidad

Si $\sin(\theta) = 0.6$, ¿cuánto vale $\cos(\theta)$?

**Razonamiento:**
Usamos $\sin^2 + \cos^2 = 1$.
$(0.6)^2 + \cos^2 = 1$
$0.36 + \cos^2 = 1$
$\cos^2 = 1 - 0.36 = 0.64$
$\cos = \sqrt{0.64} = 0.8$

**Resultado:**
$$
\boxed{0.8}
$$

### Ejemplo 2: Calculando Tangente desde Seno y Coseno

Si $\sin(\theta) = 0.5$ y $\cos(\theta) \approx 0.866$.

**Razonamiento:**
$\tan(\theta) = 0.5 / 0.866 \approx 0.577$.

**Resultado:**
$$
\boxed{0.577}
$$

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Calcula $\sin^2(30^{\circ}) + \cos^2(30^{\circ})$ sin usar calculadora.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Por identidad pitagórica, siempre es 1.

**Resultado:**
$$
\boxed{1}
$$

</details>

### Ejercicio 2
Si $\sin(\theta) = 0.8$, calcula $\cos(\theta)$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$0.8^2 + \cos^2 = 1 \Rightarrow 0.64 + \cos^2 = 1 \Rightarrow \cos^2 = 0.36$.
$\cos = 0.6$.

**Resultado:**
$$
\boxed{0.6}
$$

</details>

### Ejercicio 3
¿Qué pasa con la Tangente si el Coseno se acerca a 0?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Como $\tan = \sin/\cos$, si divides por algo muy pequeño, el resultado es gigante.

**Resultado:**
$$
\boxed{\text{Tiende a infinito}}
$$

</details>

### Ejercicio 4
Calcula $\tan(\theta)$ si $\sin(\theta)=3/5$ y $\cos(\theta)=4/5$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$(3/5) / (4/5) = 3/4$.

**Resultado:**
$$
\boxed{0.75}
$$

</details>

### Ejercicio 5
¿Por qué el Seno nunca puede ser 2?

<details>
<summary>Ver solución</summary>

**Respuesta:**

$$
\text{Porque el cateto nunca puede ser mayor que la hipotenusa.}
$$

</details>

### Ejercicio 6
Si un ángulo tiene $\sin(\theta) = \cos(\theta)$, ¿cuánto vale su Tangente?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Un número dividido por sí mismo es 1.

**Resultado:**
$$
\boxed{1}
$$

</details>

### Ejercicio 7
En un triángulo, el cateto adyacente es 0. ¿Qué ángulo es?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Si no hay adyacente, la hipotenusa es vertical.

**Resultado:**
$$
\boxed{90^{\circ}}
$$

</details>

### Ejercicio 8
Usa la identidad para calcular $\sin$ si $\cos = 1$.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
$\sin^2 + 1^2 = 1 \Rightarrow \sin^2 = 0$.

**Resultado:**
$$
\boxed{0}
$$

</details>

### Ejercicio 9
Si $\tan(\theta) = 1$, ¿qué tipo de triángulo rectángulo tenemos?

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Opuesto = Adyacente.

**Resultado:**
$$
\boxed{\text{Isósceles}}
$$

</details>

### Ejercicio 10
Verdadero o Falso: $\sin(\theta) + \cos(\theta)$ siempre es 1.

<details>
<summary>Ver solución</summary>

**Razonamiento:**
Falso. Es la suma de los **cuadrados** lo que da 1. Por ejemplo, en $45^{\circ}$, $0.707 + 0.707 = 1.414$.

**Resultado:**
$$
\boxed{\text{Falso}}
$$

</details>

---

## 🔑 Resumen

| Identidad | Significado |
| :--- | :--- |
| $\sin^2 + \cos^2 = 1$ | Pitágoras en el círculo unitario. |
| $\tan = \sin / \cos$ | La pendiente es altura entre avance. |

> Todo está conectado. Si conoces una razón, puedes encontrar las demás con estas fórmulas.
