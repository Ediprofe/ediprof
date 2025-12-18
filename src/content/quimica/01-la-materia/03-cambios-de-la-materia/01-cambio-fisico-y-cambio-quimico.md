# Cambio Físico y Cambio Químico

Cuando rompes un papel, ¿sigue siendo papel? Sí. Cuando quemas un papel, ¿sigue siendo papel? No, ahora es ceniza, humo y gases. Esta diferencia fundamental distingue los dos tipos de cambios que puede experimentar la materia: los **cambios físicos** y los **cambios químicos**.

---

## 🎯 ¿Qué vas a aprender?

- Qué es un cambio físico y cómo identificarlo
- Qué es un cambio químico (reacción química)
- Las evidencias que indican un cambio químico
- Cómo distinguir entre ambos tipos de cambios

---

## 📊 Comparación Rápida

| Característica | Cambio Físico | Cambio Químico |
|----------------|---------------|----------------|
| **¿Cambia la composición?** | No | Sí |
| **¿Se forma algo nuevo?** | No | Sí |
| **¿Es reversible?** | Generalmente sí | Generalmente no |
| **¿Hay reacción química?** | No | Sí |
| **Ejemplos** | Fundir, cortar, disolver | Quemar, oxidar, fermentar |

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-cambios-comparacion" width="700" height="300" style="width: 100%; height: auto; display: block;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-cambios-comparacion')) {
    var canvas = document.getElementById('roughjs-cambios-comparacion');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    // Título
    ctx.font = 'bold 15px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Cambio Físico vs Cambio Químico', 350, 22);
    
    // === CAMBIO FÍSICO (Hielo → Agua) ===
    var x1 = 175;
    
    // Cubo de hielo (antes)
    rc.rectangle(x1-80, 70, 50, 50, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5 });
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Hielo', x1-55, 135);
    ctx.fillText('H₂O', x1-55, 148);
    
    // Flecha
    rc.line(x1-20, 95, x1+20, 95, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.3 });
    rc.line(x1+20, 95, x1+12, 88, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.3 });
    rc.line(x1+20, 95, x1+12, 102, { stroke: '#22c55e', strokeWidth: 2, roughness: 0.3 });
    ctx.font = '9px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('+calor', x1, 85);
    
    // Charco de agua (después)
    rc.ellipse(x1+55, 105, 60, 30, { fill: '#dbeafe', fillStyle: 'solid', stroke: '#3b82f6', strokeWidth: 2, roughness: 0.5 });
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#3b82f6';
    ctx.fillText('Agua', x1+55, 135);
    ctx.fillText('H₂O', x1+55, 148);
    
    // Etiqueta
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('CAMBIO FÍSICO', x1, 175);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Misma sustancia', x1, 195);
    ctx.fillText('Solo cambia el estado', x1, 210);
    
    // Check verde
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#22c55e';
    ctx.fillText('✓ Reversible', x1, 235);
    
    // Línea divisoria
    rc.line(350, 50, 350, 270, { stroke: '#cbd5e1', strokeWidth: 1, roughness: 0.3 });
    
    // === CAMBIO QUÍMICO (Papel → Ceniza) ===
    var x2 = 525;
    
    // Papel (antes)
    rc.rectangle(x2-80, 65, 45, 60, { fill: '#fef3c7', fillStyle: 'solid', stroke: '#f59e0b', strokeWidth: 2, roughness: 0.5 });
    // Líneas de texto en el papel
    rc.line(x2-75, 80, x2-45, 80, { stroke: '#d97706', strokeWidth: 1, roughness: 0.3 });
    rc.line(x2-75, 90, x2-45, 90, { stroke: '#d97706', strokeWidth: 1, roughness: 0.3 });
    rc.line(x2-75, 100, x2-45, 100, { stroke: '#d97706', strokeWidth: 1, roughness: 0.3 });
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('Papel', x2-57, 140);
    
    // Flecha con fuego
    rc.line(x2-25, 95, x2+15, 95, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.3 });
    rc.line(x2+15, 95, x2+7, 88, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.3 });
    rc.line(x2+15, 95, x2+7, 102, { stroke: '#ef4444', strokeWidth: 2, roughness: 0.3 });
    ctx.font = '9px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('🔥', x2-5, 85);
    
    // Ceniza + humo (después)
    rc.ellipse(x2+55, 115, 50, 20, { fill: '#94a3b8', fillStyle: 'solid', stroke: '#64748b', strokeWidth: 2, roughness: 0.5 });
    // Humo
    ctx.font = '16px Inter, sans-serif';
    ctx.fillStyle = '#94a3b8';
    ctx.fillText('〰️', x2+55, 80);
    ctx.font = '10px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Ceniza + CO₂', x2+55, 145);
    
    // Etiqueta
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('CAMBIO QUÍMICO', x2, 175);
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Nueva sustancia', x2, 195);
    ctx.fillText('Reacción química', x2, 210);
    
    // X roja
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = '#ef4444';
    ctx.fillText('✗ Irreversible', x2, 235);
  }
});
</script>

---

## 📖 Cambio Físico

> Un **cambio físico** altera la forma, el tamaño o el estado de la materia, pero **no cambia su composición química**. La sustancia sigue siendo la misma.

### 💡 Característica clave

Después de un cambio físico, puedes (al menos en teoría) **regresar** al estado original.

### 📋 Ejemplos de Cambios Físicos

| Cambio | ¿Qué ocurre? | ¿Por qué es físico? |
|--------|--------------|---------------------|
| Romper un vidrio | Cambia la forma | Sigue siendo vidrio |
| Derretir hielo | Cambia de estado | Sigue siendo H₂O |
| Disolver sal en agua | Se dispersa | NaCl sigue existiendo |
| Doblar un alambre | Cambia la forma | Sigue siendo metal |
| Evaporar perfume | Cambia de estado | Las moléculas son las mismas |
| Cortar madera | Cambia el tamaño | Sigue siendo madera |

### ⚙️ Ejemplo: El ciclo del agua

El agua puede pasar por muchos cambios físicos:
- Hielo (sólido) → Agua (líquido) → Vapor (gas)

En todos los casos, la sustancia sigue siendo **H₂O**. Solo cambia el estado.

---

## 📖 Cambio Químico (Reacción Química)

> Un **cambio químico** transforma una sustancia en otra diferente, con nuevas propiedades. Se forman nuevos enlaces entre los átomos.

### 💡 Característica clave

Después de un cambio químico, **no puedes regresar** fácilmente al estado original. Se ha creado algo nuevo.

### 📋 Ejemplos de Cambios Químicos

| Cambio | ¿Qué ocurre? | ¿Por qué es químico? |
|--------|--------------|----------------------|
| Quemar papel | Se forma CO₂ y H₂O | Ya no es papel |
| Oxidar hierro | Se forma óxido (herrumbre) | Fe₂O₃ no es Fe |
| Digerir alimentos | Se rompen moléculas complejas | Se forman nuevas sustancias |
| Hornear un pastel | Cambian las proteínas y azúcares | No puedes "des-hornear" |
| Explotar fuegos artificiales | Combustión rápida | Se forman gases y luz |
| Fermentar uvas | Se produce alcohol | Azúcar → etanol + CO₂ |

### ⚙️ Ejemplo: La combustión

Cuando quemas madera:
$$
\text{Madera} + \text{O}_2 \rightarrow \text{CO}_2 + \text{H}_2\text{O} + \text{ceniza} + \text{energía}
$$

Los productos (CO₂, H₂O, ceniza) son completamente diferentes a la madera original.

---

## 📖 Evidencias de un Cambio Químico

¿Cómo saber si ocurrió una reacción química? Hay varias señales:

| Evidencia | Descripción | Ejemplo |
|-----------|-------------|---------|
| 🔥 **Cambio de temperatura** | Se libera o absorbe calor (sin fuente externa) | Paquete térmico que se calienta solo |
| 💨 **Producción de gas** | Aparecen burbujas | Vinagre + bicarbonato produce CO₂ |
| 🌈 **Cambio de color** | Color nuevo que no estaba antes | Manzana cortada se oscurece |
| 💎 **Formación de precipitado** | Un sólido aparece en una solución | Mezclar dos líquidos, obtener un sólido |
| 💡 **Emisión de luz** | Se produce luz | Fuegos artificiales, luciérnagas |
| 👃 **Cambio de olor** | Aparece un olor nuevo | Leche que se agria |

### ⚠️ Cuidado con falsas alarmas

No toda burbuja o cambio de color indica reacción química:

| Observación | ¿Es cambio químico? |
|-------------|---------------------|
| Agua hirviendo hace burbujas | No - es evaporación (físico) |
| Mezclar pinturas cambia el color | No - es mezcla (físico) |
| Hielo se derrite | No - cambio de estado (físico) |

**La pregunta clave siempre es:** ¿Se formaron nuevas sustancias?

---

## 📖 Casos Interesantes

### 💡 ¿Disolver sal es cambio físico o químico?

**Físico.** Aunque la sal parece "desaparecer", las moléculas de NaCl siguen existiendo (separadas en iones Na⁺ y Cl⁻). Si evaporas el agua, recuperas la sal.

### 💡 ¿Cocinar un huevo es cambio físico o químico?

**Químico.** Las proteínas de la clara se desnaturalizan (cambian su estructura molecular). No puedes "des-cocinar" el huevo.

### 💡 ¿La fotosíntesis es cambio físico o químico?

**Químico.** Las plantas convierten CO₂ y H₂O en glucosa (C₆H₁₂O₆) y oxígeno:

$$
6\text{CO}_2 + 6\text{H}_2\text{O} \xrightarrow{\text{luz}} \text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2
$$

---

## 📖 Reversibilidad

| Tipo de cambio | ¿Reversible? | Ejemplo |
|----------------|--------------|---------|
| **Físico** | Generalmente sí | Hielo ↔ Agua ↔ Vapor |
| **Químico** | Generalmente difícil | No puedes "desquemar" papel |

### 💡 Excepción: Algunas reacciones químicas son reversibles

En condiciones especiales, algunas reacciones pueden revertirse:
$$
\text{N}_2 + 3\text{H}_2 \rightleftharpoons 2\text{NH}_3
$$

Pero requieren condiciones específicas de temperatura y presión.

---

## 🔑 Resumen

| Concepto | Definición |
|----------|------------|
| **Cambio físico** | Altera forma o estado, pero no la composición |
| **Cambio químico** | Transforma sustancias en otras nuevas (reacción) |
| **Reversibilidad** | Los físicos suelen ser reversibles, los químicos no |
| **Evidencias** | Cambio de color, olor, temperatura, burbujas, precipitado, luz |

---

## 📝 Ejercicios de Práctica

### Ejercicio 1
Clasifica cada situación como **cambio físico (F)** o **cambio químico (Q)**:

a) Hervir agua
b) Oxidar una bicicleta
c) Moler café
d) Digerir pizza
e) Mezclar arena y agua
f) Explotar dinamita

<details>
<summary>Ver solución</summary>

a) **F** - El agua líquida se vuelve vapor, pero sigue siendo H₂O
b) **Q** - El hierro reacciona con oxígeno formando óxido de hierro (Fe₂O₃)
c) **F** - Los granos de café se vuelven más pequeños, pero siguen siendo café
d) **Q** - Las moléculas de alimentos se rompen y forman nuevas sustancias
e) **F** - La arena y el agua no reaccionan, solo se mezclan
f) **Q** - La dinamita se descompone liberando gases, calor y luz

</details>

### Ejercicio 2
Observas que al mezclar dos líquidos transparentes se forma un sólido blanco en el fondo. ¿Es cambio físico o químico? Justifica.

<details>
<summary>Ver solución</summary>

Es un **cambio químico**.

La formación de un **precipitado** (sólido que aparece en una solución) es una evidencia clásica de reacción química.

**Lo que ocurrió:**
1. Los dos líquidos contenían sustancias disueltas
2. Al mezclarse, algunas de esas sustancias reaccionaron
3. El producto de la reacción es insoluble, por eso precipita como sólido

**Ejemplo típico:**
$$
\text{AgNO}_3 + \text{NaCl} \rightarrow \text{AgCl}\downarrow + \text{NaNO}_3
$$

El cloruro de plata (AgCl) es un sólido blanco insoluble.

</details>

### Ejercicio 3
Un estudiante dice que "freír un huevo es un cambio físico porque solo estás calentando el huevo". ¿Estás de acuerdo? Explica.

<details>
<summary>Ver solución</summary>

**No estoy de acuerdo.** Freír un huevo es un **cambio químico**.

Aunque es cierto que se agrega calor, lo que ocurre no es solo un cambio de temperatura. Las **proteínas** de la clara del huevo se **desnaturalizan**:

1. La estructura molecular de las proteínas cambia permanentemente
2. La clara pasa de transparente a blanca
3. La consistencia cambia de líquida a sólida
4. **No puedes revertir el proceso** - no existe forma de "des-freír" el huevo

Si fuera un cambio físico (como derretir mantequilla), podrías regresar al estado original.

</details>

### Ejercicio 4
Completa la tabla indicando si cada evidencia, **por sí sola**, garantiza que hubo reacción química:

| Evidencia | ¿Garantiza reacción química? |
|-----------|------------------------------|
| Cambio de color | |
| Producción de burbujas | |
| Cambio de temperatura | |
| Formación de precipitado | |

<details>
<summary>Ver solución</summary>

| Evidencia | ¿Garantiza reacción química? |
|-----------|------------------------------|
| Cambio de color | **No** (mezclar pinturas es físico) |
| Producción de burbujas | **No** (agua hirviendo es físico) |
| Cambio de temperatura | **No** (disolver sal puede enfriar, pero es físico) |
| Formación de precipitado | **Generalmente sí** (difícil que un sólido se forme sin reacción) |

**Conclusión:** Se deben considerar varias evidencias y determinar si se formaron **nuevas sustancias**.

</details>
