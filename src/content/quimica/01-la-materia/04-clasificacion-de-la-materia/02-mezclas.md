# Mezclas

El aire que respiras, el jugo que tomas, la tierra del jardín... todos son ejemplos de **mezclas**. A diferencia de las sustancias puras, las mezclas combinan diferentes sustancias sin que estas se unan químicamente.

---

## 🎯 ¿Qué vas a aprender?

- Qué es una mezcla y cómo difiere de una sustancia pura
- La diferencia entre mezclas homogéneas y heterogéneas
- Ejemplos cotidianos de cada tipo de mezcla
- Cómo identificar el tipo de mezcla

---

## 📊 Comparación: Sustancias Puras vs Mezclas

| Característica | Sustancia Pura | Mezcla |
|----------------|----------------|--------|
| Composición | Fija y definida | Variable |
| Propiedades | Constantes | Dependen de la proporción |
| Separación | Por métodos químicos (compuestos) | Por métodos físicos |
| Ejemplos | H₂O, NaCl, O₂ | Aire, agua de mar, ensalada |

---

## 📖 ¿Qué es una Mezcla?

> Una **mezcla** está formada por dos o más sustancias que **no están unidas químicamente** y conservan sus propiedades individuales.

### 💡 Características de las mezclas:

- Composición **variable**
- Cada componente conserva sus propiedades
- Se pueden separar por **métodos físicos**
- No hay reacción química entre los componentes

### ⚙️ Ejemplo: Agua con sal

- Puedes agregar mucha o poca sal (composición variable)
- La sal sigue siendo NaCl, el agua sigue siendo H₂O
- Puedes separar la sal evaporando el agua (método físico)
- No se formó ninguna sustancia nueva

---

## 📖 Tipos de Mezclas

Las mezclas se clasifican en dos tipos según su apariencia:

| Tipo | Apariencia | Componentes visibles | Ejemplo |
|------|------------|---------------------|---------|
| **Homogénea** | Uniforme | No se distinguen | Agua salada |
| **Heterogénea** | No uniforme | Se distinguen | Ensalada |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-mezclas-tipos" width="700" height="320" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-mezclas-tipos')) {
    var canvas = document.getElementById('roughjs-mezclas-tipos');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título
    ctx.font = 'bold 15px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Tipos de Mezclas', 350, 22);
    
    // === MEZCLA HOMOGÉNEA ===
    var x1 = 180;
    var yBase = 150;
    
    // Vaso
    rc.path('M ' + (x1-60) + ' 70 L ' + (x1-50) + ' 250 L ' + (x1+50) + ' 250 L ' + (x1+60) + ' 70 Z', 
      { stroke: '#64748b', strokeWidth: 2, fill: '#dbeafe', fillStyle: 'solid', roughness: 0.5 });
    
    // Partículas uniformemente distribuidas (sal en agua)
    var homoPos = [];
    for (var i = 0; i < 25; i++) {
      homoPos.push([x1 - 40 + Math.random() * 80, 90 + Math.random() * 140]);
    }
    homoPos.forEach(function(p) {
      rc.circle(p[0], p[1], 8, { fill: '#3b82f6', fillStyle: 'solid', stroke: '#1e40af', roughness: 0.3 });
    });
    
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('HOMOGÉNEA', x1, 275);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Agua salada', x1, 295);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillText('Se ve uniforme', x1, 310);
    
    // Etiqueta
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('✓ No se distinguen', x1, 55);
    ctx.fillText('los componentes', x1, 67);
    
    // === MEZCLA HETEROGÉNEA ===
    var x2 = 520;
    
    // Vaso
    rc.path('M ' + (x2-60) + ' 70 L ' + (x2-50) + ' 250 L ' + (x2+50) + ' 250 L ' + (x2+60) + ' 70 Z', 
      { stroke: '#64748b', strokeWidth: 2, fill: 'none', roughness: 0.5 });
    
    // Capa de aceite (arriba)
    rc.rectangle(x2-55, 75, 110, 60, { fill: '#fef3c7', fillStyle: 'solid', stroke: 'none', roughness: 0 });
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('Aceite', x2, 110);
    
    // Línea de separación
    rc.line(x2-55, 135, x2+55, 135, { stroke: '#94a3b8', strokeWidth: 1, roughness: 0.3 });
    
    // Capa de agua (abajo)
    rc.rectangle(x2-52, 135, 104, 110, { fill: '#dbeafe', fillStyle: 'solid', stroke: 'none', roughness: 0 });
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Agua', x2, 195);
    
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('HETEROGÉNEA', x2, 275);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Agua + Aceite', x2, 295);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillText('Se ven las capas', x2, 310);
    
    // Etiqueta
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('✗ Se distinguen', x2, 55);
    ctx.fillText('los componentes', x2, 67);
    
    // Flecha VS
    ctx.font = 'bold 20px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('vs', 350, 165);
  }
});
</script>

---

## 📖 Mezclas Homogéneas (Soluciones)

> En una mezcla **homogénea**, la composición es **uniforme** en toda la muestra. Se ve como una sola fase.

### 💡 También llamadas "soluciones"

| Término | Definición |
|---------|------------|
| **Soluto** | Sustancia que se disuelve (menor cantidad) |
| **Solvente** | Sustancia que disuelve (mayor cantidad) |

### 📋 Ejemplos de Mezclas Homogéneas

| Mezcla | Soluto | Solvente | Estado |
|--------|--------|----------|--------|
| Agua salada | Sal | Agua | Líquido-líquido |
| Aire | O₂, CO₂, otros | N₂ | Gas-gas |
| Bronce | Estaño | Cobre | Sólido-sólido |
| Vinagre | Ácido acético | Agua | Líquido-líquido |
| Agua azucarada | Azúcar | Agua | Sólido-líquido |

### 💡 ¿Cómo saber si es homogénea?

- Se ve **igual** en todas partes
- No puedes distinguir los componentes a simple vista
- Si tomas una muestra de cualquier punto, es idéntica

### ⚙️ Ejemplo: El aire

El aire es una mezcla homogénea de gases:

| Gas | Porcentaje |
|-----|------------|
| Nitrógeno (N₂) | 78% |
| Oxígeno (O₂) | 21% |
| Argón (Ar) | 0.9% |
| CO₂ y otros | 0.1% |

Aunque tiene varios componentes, no los distingues: el aire se ve y se siente uniforme.

---

## 📖 Mezclas Heterogéneas

> En una mezcla **heterogénea**, se pueden **distinguir** los componentes a simple vista o con un microscopio.

### 💡 Características:

- Tiene dos o más **fases** visibles
- La composición varía según el punto de la muestra
- Los componentes son visualmente distinguibles

### 📋 Ejemplos de Mezclas Heterogéneas

| Mezcla | Componentes visibles |
|--------|---------------------|
| Ensalada | Lechuga, tomate, cebolla |
| Granito | Cuarzo, mica, feldespato |
| Pizza | Masa, queso, pepperoni |
| Agua + aceite | Dos capas líquidas |
| Leche (al microscopio) | Grasa dispersa en agua |
| Arena en agua | Sólido disperso en líquido |

### 💡 Subtipos de mezclas heterogéneas

| Subtipo | Descripción | Ejemplo |
|---------|-------------|---------|
| **Suspensión** | Partículas sólidas que sedimentan | Arena en agua |
| **Coloide** | Partículas pequeñas que no sedimentan | Leche, gelatina |
| **Emulsión** | Líquido disperso en otro líquido | Mayonesa |

---

## 📖 ¿Cómo Identificar el Tipo de Mezcla?

### 💡 Pregunta clave

¿Puedes distinguir los componentes mirando la muestra?

| Respuesta | Tipo de mezcla |
|-----------|----------------|
| **No** (se ve uniforme) | Homogénea |
| **Sí** (se ven partes diferentes) | Heterogénea |

### ⚙️ El truco del rayo de luz

En algunas mezclas que parecen homogéneas (como la leche), puedes pasar un rayo de luz:

- Si la luz **pasa directamente** → Solución verdadera (homogénea)
- Si la luz **se dispersa** (efecto Tyndall) → Coloide (heterogénea al microscopio)

---

## 🔑 Resumen

| Concepto | Definición | Ejemplos |
|----------|------------|----------|
| **Mezcla** | Combinación física de sustancias | Aire, agua de mar |
| **Mezcla homogénea** | Composición uniforme, no se distinguen partes | Café, bronce |
| **Mezcla heterogénea** | Se distinguen las partes | Ensalada, granito |
| **Soluto/Solvente** | Componente menor/mayor en soluciones | Sal/Agua |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Clasifica cada mezcla como **homogénea (HO)** o **heterogénea (HE)**:

a) Agua con azúcar disuelta
b) Ensalada de frutas
c) Aire
d) Agua con aceite
e) Acero (hierro + carbono)
f) Sopa con vegetales flotando

<details>
<summary>Ver solución</summary>

a) **HO** - El azúcar está disuelto, no se ve
b) **HE** - Se distinguen las frutas
c) **HO** - Los gases están uniformemente mezclados
d) **HE** - Se ven dos capas
e) **HO** - El carbono está disperso uniformemente (aleación)
f) **HE** - Se ven los vegetales

</details>

### Ejercicio 2
Tienes un vaso con agua y arena. Después de agitar, la arena se asienta en el fondo. ¿Es homogénea o heterogénea? ¿Por qué?

<details>
<summary>Ver solución</summary>

Es una mezcla **heterogénea**.

**Razones:**
1. Puedes **ver** la arena separada del agua
2. Hay **dos fases** distintas: sólida (arena) y líquida (agua)
3. La arena **sedimenta** (se deposita en el fondo)
4. La composición es **diferente** en la parte superior (solo agua) que en el fondo (arena + agua)

Este tipo de mezcla heterogénea se llama **suspensión**.

</details>

### Ejercicio 3
El bronce está hecho de cobre y estaño. ¿Por qué es una mezcla homogénea y no un compuesto?

<details>
<summary>Ver solución</summary>

El bronce es una **mezcla homogénea** (aleación) porque:

1. **Composición variable:** Puede tener diferentes proporciones
   - Bronce de campana: 80% Cu + 20% Sn
   - Bronce fosforoso: 90% Cu + 10% Sn

2. **No hay enlaces químicos específicos:** Los átomos están mezclados, no unidos en una estructura molecular definida

3. **Los metales conservan sus propiedades:** Cada átomo sigue siendo lo que es

4. **Se ve uniforme:** A simple vista, parece una sola sustancia

Si fuera un compuesto, tendría una fórmula fija (como H₂O o NaCl).

</details>

### Ejercicio 4
Da un ejemplo de mezcla homogénea para cada combinación de estados:

a) Gas + Gas
b) Sólido + Líquido
c) Sólido + Sólido
d) Líquido + Líquido

<details>
<summary>Ver solución</summary>

a) **Gas + Gas:** Aire (N₂, O₂, Ar, CO₂ mezclados)

b) **Sólido + Líquido:** Agua salada (sal disuelta en agua)

c) **Sólido + Sólido:** Bronce (cobre + estaño)

d) **Líquido + Líquido:** Vinagre (ácido acético + agua)

</details>

### Ejercicio 5
Explica por qué la leche parece homogénea a simple vista, pero se considera heterogénea científicamente.

<details>
<summary>Ver solución</summary>

La leche parece homogénea porque:
- Es blanca uniforme
- No ves partículas flotando
- Parece una sola fase

Pero científicamente es **heterogénea** (un coloide) porque:
- Al microscopio, se ven **gotas de grasa** dispersas en agua
- Si la dejas reposar, la crema (grasa) tiende a subir
- Dispersa la luz (efecto Tyndall)

La leche es un tipo especial de mezcla heterogénea llamada **emulsión**, donde pequeñas gotas de un líquido (grasa) están dispersas en otro líquido (agua).

</details>
