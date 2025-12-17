# Problemas Aplicados de Cuerpos Geométricos

En esta lección resolvemos problemas que combinan diferentes cuerpos geométricos y aplican los conceptos aprendidos a situaciones del mundo real.

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 12px; padding: 1rem; margin: 1.5rem 0; width: 100%; box-sizing: border-box;">
  <canvas id="roughjs-helado" width="700" height="260" style="width: 100%; height: auto; display: block;"></canvas>
  <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 0.75rem; font-size: 0.9rem; flex-wrap: wrap;">
    <span><strong style="color: #22c55e;">r</strong> = radio (común al cono y semiesfera)</span>
    <span><strong style="color: #ef4444;">h</strong> = altura del cono</span>
    <span><strong>V</strong> = V_cono + V_semiesfera</span>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof rough !== 'undefined' && document.getElementById('roughjs-helado')) {
    var canvas = document.getElementById('roughjs-helado');
    var rc = rough.canvas(canvas);
    var ctx = canvas.getContext('2d');
    
    ctx.font = 'bold 16px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Problema Clásico: Cono de Helado con Semiesfera', 350, 25);
    
    var azul = '#3b82f6';
    var verde = '#22c55e';
    var rojo = '#ef4444';
    var rosa = '#ec4899';
    
    // Cono de helado
    var cx = 200, cy = 240;
    var r = 50;
    var h = 120;
    
    // Cono (barquillo)
    rc.polygon([[cx - r, cy - h + 50], [cx, cy], [cx + r, cy - h + 50]], {fill: '#fef3c7', stroke: '#f59e0b', strokeWidth: 2, roughness: 0.5});
    
    // Semiesfera de helado
    ctx.beginPath();
    ctx.arc(cx, cy - h + 50, r, Math.PI, 0);
    ctx.fillStyle = '#fce7f3';
    ctx.fill();
    ctx.strokeStyle = rosa;
    ctx.lineWidth = 2;
    ctx.stroke();
    
    // Base de la semiesfera (elipse)
    rc.ellipse(cx, cy - h + 50, r * 2, 20, {fill: '#fbcfe8', stroke: rosa, strokeWidth: 2, roughness: 0.5});
    
    // Etiquetas
    ctx.font = 'bold 12px Inter, sans-serif';
    ctx.fillStyle = verde;
    rc.line(cx, cy - h + 50, cx + r, cy - h + 50, {stroke: verde, strokeWidth: 2, roughness: 0.3});
    ctx.fillText('r', cx + r/2, cy - h + 40);
    
    ctx.fillStyle = rojo;
    rc.line(cx + r + 15, cy - h + 50, cx + r + 15, cy, {stroke: rojo, strokeWidth: 2, roughness: 0.3});
    ctx.fillText('h', cx + r + 30, cy - h/2 + 25);
    
    // Fórmulas
    rc.rectangle(350, 60, 320, 190, {fill: '#f1f5f9', stroke: '#cbd5e1', roughness: 0.3});
    ctx.font = 'bold 14px Inter, sans-serif';
    ctx.fillStyle = '#1e293b';
    ctx.textAlign = 'center';
    ctx.fillText('Volumen Total del Helado', 510, 90);
    
    ctx.font = '13px Inter, sans-serif';
    ctx.textAlign = 'left';
    
    ctx.fillStyle = '#f59e0b';
    ctx.fillText('Cono:', 370, 120);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('V_cono = πr²h / 3', 430, 120);
    
    ctx.fillStyle = rosa;
    ctx.fillText('Semiesfera:', 370, 150);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('V_semi = (2/3)πr³', 460, 150);
    
    ctx.fillStyle = azul;
    ctx.font = 'bold 13px Inter, sans-serif';
    ctx.fillText('Total:', 370, 185);
    ctx.fillStyle = '#1e293b';
    ctx.fillText('V = πr²h/3 + (2/3)πr³', 420, 185);
    
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Ejemplo: r=3cm, h=10cm', 370, 215);
    ctx.fillText('V = 30π + 18π = 48π ≈ 150.8 cm³', 370, 235);
  }
});
</script>

---

## 📖 Estrategia general para problemas

1. **Identificar** los cuerpos geométricos involucrados
2. **Extraer** los datos del problema
3. **Seleccionar** las fórmulas apropiadas
4. **Calcular** paso a paso
5. **Verificar** que la respuesta tenga sentido

---

## 📖 Problema 1: Tanque cilíndrico

Un tanque cilíndrico tiene diámetro 2 m y altura 3 m. ¿Cuántos litros de agua puede contener?

### Solución

Radio: $r = 1$ m

$$
V = \pi r^2 h = \pi(1)^2(3) = 3\pi \approx 9.42 \text{ m}^3
$$

Conversión: $1 \text{ m}^3 = 1000 \text{ L}$

$$
V = 9420 \text{ litros}
$$

---

## 📖 Problema 2: Helado en cono

Un cono de helado tiene radio 3 cm y altura 10 cm. Encima tiene una semiesfera de helado del mismo radio. ¿Cuál es el volumen total de helado?

### Solución

**Volumen del cono:**

$$
V_{cono} = \frac{\pi(9)(10)}{3} = 30\pi \text{ cm}^3
$$

**Volumen de la semiesfera:**

$$
V_{semiesfera} = \frac{1}{2} \times \frac{4}{3}\pi(27) = 18\pi \text{ cm}^3
$$

**Total:**

$$
V_{total} = 30\pi + 18\pi = 48\pi \approx 150.8 \text{ cm}^3
$$

---

## 📖 Problema 3: Silo de granos

Un silo tiene forma de cilindro coronado por un hemisferio. El radio es 5 m y la altura del cilindro es 12 m. Calcula su capacidad.

### Solución

**Volumen del cilindro:**

$$
V_{cil} = \pi(25)(12) = 300\pi \text{ m}^3
$$

**Volumen del hemisferio:**

$$
V_{hem} = \frac{2}{3}\pi(125) = \frac{250\pi}{3} \text{ m}^3
$$

**Total:**

$$
V = 300\pi + \frac{250\pi}{3} = \frac{900\pi + 250\pi}{3} = \frac{1150\pi}{3} \approx 1204.28 \text{ m}^3
$$

---

## 📖 Problema 4: Pintura

¿Cuánta pintura se necesita para pintar el exterior de un cilindro de radio 2 m y altura 5 m, incluyendo las tapas? (Asume que 1 litro cubre 10 m²)

### Solución

**Área total:**

$$
A = 2\pi r(h + r) = 2\pi(2)(7) = 28\pi \approx 87.96 \text{ m}^2
$$

**Pintura necesaria:**

$$
\frac{87.96}{10} \approx 8.8 \text{ litros}
$$

---

## 📖 Problema 5: Casa con techo piramidal

Una casa tiene base cuadrada de 10 m de lado y paredes de 3 m. El techo es una pirámide de 4 m de altura. Calcula el volumen total del espacio interior.

### Solución

**Volumen del prisma (paredes):**

$$
V_{prisma} = 100 \times 3 = 300 \text{ m}^3
$$

**Volumen de la pirámide (techo):**

$$
V_{pir} = \frac{100 \times 4}{3} = \frac{400}{3} \approx 133.33 \text{ m}^3
$$

**Total:**

$$
V = 300 + 133.33 = 433.33 \text{ m}^3
$$

---

## 📝 Problemas de práctica

### Problema 1: Lata de refresco

Una lata cilíndrica tiene diámetro 6.6 cm y altura 12.2 cm. Calcula:

1. Su volumen en cm³
2. Su capacidad en ml

<details>
<summary><strong>Ver respuesta</strong></summary>

$r = 3.3$ cm

$$
V = \pi(10.89)(12.2) \approx 417.5 \text{ cm}^3 = 417.5 \text{ ml}
$$

(Aproximadamente una lata de 330 ml tiene un poco menos de altura real)

</details>

---

### Problema 2: Pelota de tenis

Una pelota de tenis tiene diámetro 6.7 cm. Una caja cilíndrica contiene exactamente 3 pelotas apiladas. ¿Cuánto espacio vacío queda en la caja?

<details>
<summary><strong>Ver respuesta</strong></summary>

$r = 3.35$ cm, cada pelota: $V = \frac{4}{3}\pi(3.35)^3 \approx 157.48$ cm³

Caja: $r = 3.35$, $h = 3 \times 6.7 = 20.1$ cm

$$
V_{caja} = \pi(11.22)(20.1) \approx 708.5 \text{ cm}^3
$$

$$
V_{pelotas} = 3 \times 157.48 = 472.44 \text{ cm}^3
$$

$$
V_{vacío} = 708.5 - 472.44 \approx 236 \text{ cm}^3
$$

</details>

---

### Problema 3: Piscina

Una piscina tiene forma de prisma rectangular de 25 m × 10 m × 2 m. ¿Cuántos litros de agua caben?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
V = 25 \times 10 \times 2 = 500 \text{ m}^3 = 500,000 \text{ litros}
$$

</details>

---

### Problema 4: Vela cónica

Una vela cónica tiene radio 4 cm y altura 15 cm. ¿Cuántas velas se pueden hacer con 2 litros de cera? (1 L = 1000 cm³)

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
V_{vela} = \frac{\pi(16)(15)}{3} = 80\pi \approx 251.33 \text{ cm}^3
$$

$$
\text{Velas} = \frac{2000}{251.33} \approx 7.96
$$

Se pueden hacer **7 velas** completas.

</details>

---

### Problema 5: Embudo

Un embudo tiene forma de cono con radio 6 cm y altura 10 cm. Se llena de agua y luego se vierte en un cilindro de radio 3 cm. ¿Hasta qué altura llega el agua?

<details>
<summary><strong>Ver respuesta</strong></summary>

$$
V_{cono} = \frac{\pi(36)(10)}{3} = 120\pi \text{ cm}^3
$$

$$
h_{cilindro} = \frac{V}{\pi r^2} = \frac{120\pi}{\pi(9)} = \frac{120}{9} = 13.33 \text{ cm}
$$

</details>

---
