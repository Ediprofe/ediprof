# Densidad

¿Por qué el hielo flota en el agua? ¿Por qué una pelota de plomo se hunde mientras una de plástico flota? La respuesta está en una propiedad que combina masa y volumen: la **densidad**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es la densidad y cómo se calcula
- Las unidades de densidad más comunes
- Por qué algunos objetos flotan y otros se hunden
- Cómo usar la densidad para identificar sustancias

---

## 📊 Densidades de Sustancias Comunes

| Sustancia | Densidad (g/cm³) | ¿Flota en agua? |
|-----------|------------------|-----------------|
| Aire | 0.0012 | Sí (es gas) |
| Corcho | 0.24 | Sí |
| Madera de pino | 0.5 | Sí |
| Aceite | 0.9 | Sí |
| **Agua** | **1.00** | -- (referencia) |
| Plástico (PVC) | 1.3 | No |
| Aluminio | 2.7 | No |
| Hierro | 7.9 | No |
| Cobre | 8.9 | No |
| Plomo | 11.3 | No |
| Oro | 19.3 | No |

---

## 📖 Definición de Densidad

> La **densidad** es la cantidad de masa contenida en un volumen determinado. Mide qué tan "compacta" está la materia.

### 💡 La fórmula de la densidad

$$
\rho = \frac{m}{V}
$$

Donde:
- $\rho$ (rho) = densidad
- $m$ = masa
- $V$ = volumen

### 📋 Unidades de Densidad

| Sistema | Unidad | Equivalencia |
|---------|--------|--------------|
| CGS (más común) | g/cm³ | 1 g/cm³ |
| SI | kg/m³ | 1 g/cm³ = 1,000 kg/m³ |
| Líquidos | g/mL | 1 g/mL = 1 g/cm³ |

### 💡 Dato clave

La densidad del **agua pura** a 4°C es exactamente:

$$
\rho_{\text{agua}} = 1.00 \text{ g/cm}^3 = 1{,}000 \text{ kg/m}^3
$$

Esta es la referencia para comparar otras sustancias.

---

## 📖 Cálculos con Densidad

De la fórmula básica podemos despejar masa y volumen:

### 💡 Las tres fórmulas relacionadas

| Para encontrar | Fórmula |
|----------------|---------|
| Densidad | $\rho = \dfrac{m}{V}$ |
| Masa | $m = \rho \times V$ |
| Volumen | $V = \dfrac{m}{\rho}$ |

### ⚙️ Ejemplo 1: Calcular la densidad

Un bloque de metal tiene masa de 540 g y volumen de 200 cm³.

$$
\rho = \frac{m}{V} = \frac{540 \text{ g}}{200 \text{ cm}^3} = \boxed{2.7 \text{ g/cm}^3}
$$

Comparando con la tabla, el metal es probablemente **aluminio**.

### ⚙️ Ejemplo 2: Calcular la masa

¿Cuál es la masa de 50 cm³ de hierro? (densidad del hierro = 7.9 g/cm³)

$$
m = \rho \times V = 7.9 \text{ g/cm}^3 \times 50 \text{ cm}^3 = \boxed{395 \text{ g}}
$$

### ⚙️ Ejemplo 3: Calcular el volumen

Si tienes 100 g de mercurio (densidad = 13.6 g/cm³), ¿qué volumen ocupa?

$$
V = \frac{m}{\rho} = \frac{100 \text{ g}}{13.6 \text{ g/cm}^3} = \boxed{7.35 \text{ cm}^3}
$$

---

## 📖 Flotabilidad

> Un objeto **flota** en un líquido si su densidad es **menor** que la del líquido.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-densidad-flotabilidad" width="700" height="300" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-densidad-flotabilidad')) {
    var canvas = document.getElementById('roughjs-densidad-flotabilidad');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título
    ctx.font = 'bold 15px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Flotabilidad: Densidad vs Agua (1.0 g/cm³)', 350, 22);
    
    // Recipiente con agua
    var waterTop = 100;
    var waterBottom = 240;
    rc.rectangle(80, 50, 540, 210, { stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
    rc.rectangle(80, waterTop, 540, waterBottom - waterTop, { fill: '#dbeafe', fillStyle: 'solid', stroke: 'none', roughness: 0 });
    
    // Línea de nivel del agua
    rc.line(80, waterTop, 620, waterTop, { stroke: '#3b82f6', strokeWidth: 2, roughness: 0.3 });
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.textAlign = 'left';
    ctx.fillText('Nivel del agua', 625, waterTop + 4);
    
    // === CORCHO (flota mucho) ===
    var x1 = 150;
    rc.rectangle(x1-25, waterTop-30, 50, 50, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', strokeWidth: 2, roughness: 0.5 });
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.textAlign = 'center';
    ctx.fillText('Corcho', x1, waterTop-40);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('0.24 g/cm³', x1, 275);
    ctx.fillText('FLOTA', x1, 290);
    
    // === MADERA (flota parcial) ===
    var x2 = 270;
    rc.rectangle(x2-25, waterTop-10, 50, 50, { fill: '#d4a574', fillStyle: 'solid', stroke: '#92400e', strokeWidth: 2, roughness: 0.5 });
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#92400e';
    ctx.fillText('Madera', x2, waterTop-20);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('0.5 g/cm³', x2, 275);
    ctx.fillText('FLOTA', x2, 290);
    
    // === PLÁSTICO (se hunde poco) ===
    var x3 = 390;
    rc.rectangle(x3-25, waterTop+20, 50, 50, { fill: '#e2e8f0', fillStyle: 'solid', stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Plástico', x3, waterTop+10);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillText('1.3 g/cm³', x3, 275);
    ctx.fillText('SE HUNDE', x3, 290);
    
    // === HIERRO (se hunde mucho) ===
    var x4 = 510;
    rc.rectangle(x4-25, waterBottom-60, 50, 50, { fill: '#94a3b8', fillStyle: 'solid', stroke: '#475569', strokeWidth: 2, roughness: 0.5 });
    ctx.font = 'bold 11px Inter, sans-serif';
    ctx.fillStyle = '#475569';
    ctx.fillText('Hierro', x4, waterBottom-70);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('7.9 g/cm³', x4, 275);
    ctx.fillText('SE HUNDE', x4, 290);
    
    // Etiqueta del agua
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Agua: 1.0 g/cm³', 350, waterTop + 30);
  }
});
</script>

### 💡 Regla de flotabilidad

| Si... | Entonces el objeto... |
|-------|----------------------|
| $\rho_{\text{objeto}} < \rho_{\text{líquido}}$ | Flota |
| $\rho_{\text{objeto}} > \rho_{\text{líquido}}$ | Se hunde |
| $\rho_{\text{objeto}} = \rho_{\text{líquido}}$ | Queda suspendido |

### ⚙️ Ejemplo: El hielo flota

| Sustancia | Densidad |
|-----------|----------|
| Hielo | 0.92 g/cm³ |
| Agua líquida | 1.00 g/cm³ |

Como el hielo es **menos denso** que el agua líquida, flota. Esto es inusual: ¡la mayoría de los sólidos se hunden en su forma líquida!

### ⚙️ Ejemplo: El aceite sobre el agua

Si viertes aceite (0.9 g/cm³) en agua (1.0 g/cm³), el aceite flota formando una capa superior.

---

## 📖 La Densidad como Propiedad Intensiva

> La densidad es una **propiedad intensiva**: no depende de la cantidad de sustancia.

### 💡 ¿Qué significa esto?

| Muestra de oro | Masa | Volumen | Densidad |
|----------------|------|---------|----------|
| 1 gramo | 1 g | 0.052 cm³ | 19.3 g/cm³ |
| 100 gramos | 100 g | 5.2 cm³ | 19.3 g/cm³ |
| 1 kilogramo | 1,000 g | 51.8 cm³ | 19.3 g/cm³ |

Sin importar cuánto oro tengas, la densidad siempre es 19.3 g/cm³.

### 💡 Uso para identificar sustancias

Si encuentras un metal desconocido y calculas su densidad como 8.9 g/cm³, puedes identificarlo como **cobre** comparando con tablas de referencia.

---

## 📖 Densidad de Gases

Los gases también tienen densidad, pero es mucho menor que la de sólidos y líquidos.

| Gas | Densidad (g/L) a 0°C y 1 atm |
|-----|------------------------------|
| Hidrógeno | 0.090 |
| Helio | 0.178 |
| Aire | 1.29 |
| Dióxido de carbono | 1.96 |

### 💡 ¿Por qué el helio hace flotar los globos?

El helio (0.178 g/L) es menos denso que el aire (1.29 g/L), así que el globo "flota" en el aire.

---

## 🔑 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Densidad** | Masa por unidad de volumen: $\rho = m/V$ |
| **Unidad común** | g/cm³ o g/mL |
| **Flotación** | Objetos menos densos que el líquido flotan |
| **Propiedad intensiva** | No depende de la cantidad |
| **Identificación** | La densidad ayuda a identificar sustancias |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Un cubo de metal tiene aristas de 4 cm y una masa de 172.8 g. Calcula su densidad e identifica el metal.

<details>
<summary>Ver solución</summary>

**Paso 1:** Calcular el volumen
$$
V = l^3 = 4^3 = 64 \text{ cm}^3
$$

**Paso 2:** Calcular la densidad
$$
\rho = \frac{m}{V} = \frac{172.8 \text{ g}}{64 \text{ cm}^3} = \boxed{2.7 \text{ g/cm}^3}
$$

**Identificación:** Comparando con la tabla, el metal es **aluminio**.

</details>

### Ejercicio 2
¿Cuántos litros de gasolina (densidad = 0.75 g/mL) tienen una masa de 30 kg?

<details>
<summary>Ver solución</summary>

**Paso 1:** Convertir masa a gramos
$$
m = 30 \text{ kg} = 30{,}000 \text{ g}
$$

**Paso 2:** Calcular volumen
$$
V = \frac{m}{\rho} = \frac{30{,}000 \text{ g}}{0.75 \text{ g/mL}} = 40{,}000 \text{ mL}
$$

**Paso 3:** Convertir a litros
$$
V = 40{,}000 \text{ mL} = \boxed{40 \text{ L}}
$$

</details>

### Ejercicio 3
Tienes tres objetos:
- Objeto A: densidad = 0.8 g/cm³
- Objeto B: densidad = 1.2 g/cm³
- Objeto C: densidad = 1.0 g/cm³

Si los colocas en agua (densidad = 1.0 g/cm³), ¿qué sucede con cada uno?

<details>
<summary>Ver solución</summary>

- **Objeto A** (0.8 g/cm³): Densidad menor que el agua → **Flota**

- **Objeto B** (1.2 g/cm³): Densidad mayor que el agua → **Se hunde**

- **Objeto C** (1.0 g/cm³): Densidad igual al agua → **Queda suspendido** (flotación neutra)

</details>

### Ejercicio 4
Una corona de "oro" tiene masa de 500 g. Al sumergirla en agua, desplaza 40 mL. ¿Es oro puro? (densidad del oro = 19.3 g/cm³)

<details>
<summary>Ver solución</summary>

**Paso 1:** El volumen desplazado es el volumen de la corona
$$
V = 40 \text{ mL} = 40 \text{ cm}^3
$$

**Paso 2:** Calcular la densidad de la corona
$$
\rho = \frac{m}{V} = \frac{500 \text{ g}}{40 \text{ cm}^3} = 12.5 \text{ g/cm}^3
$$

**Paso 3:** Comparar con la densidad del oro puro
$$
12.5 \text{ g/cm}^3 \neq 19.3 \text{ g/cm}^3
$$

**Conclusión:** La corona **NO es de oro puro**. Probablemente es una aleación con metales menos densos.

*(Este es el famoso problema que resolvió Arquímedes para el rey Hierón II)*

</details>

### Ejercicio 5
¿Por qué los barcos de acero flotan si el acero (7.9 g/cm³) es más denso que el agua (1.0 g/cm³)?

<details>
<summary>Ver solución</summary>

Los barcos flotan porque lo que importa es la **densidad promedio** del barco completo, no solo del material.

**Explicación:**
1. El barco tiene un casco de acero, pero está **hueco** por dentro
2. El interior contiene principalmente **aire** (muy poco denso)
3. La densidad promedio (acero + aire) es **menor que 1 g/cm³**
4. Por eso el barco flota

**Si el barco se llena de agua** (como en un naufragio), la densidad promedio aumenta y el barco **se hunde**.

</details>
