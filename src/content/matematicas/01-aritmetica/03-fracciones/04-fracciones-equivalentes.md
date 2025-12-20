# ⚖️ Fracciones Equivalentes

En este tema aprenderemos qué son las fracciones equivalentes, cómo obtenerlas y cómo simplificar fracciones.

---

## 📖 ¿Qué son fracciones equivalentes?

Dos fracciones son **equivalentes** si representan la misma cantidad.

$$
\frac{1}{2} = \frac{2}{4} = \frac{3}{6}
$$

Observa cómo las tres fracciones llenan **exactamente la mitad** del círculo:

<div style="background: #e2e8f0; border: 1px solid #cbd5e1; border-radius: 12px; padding: 0.75rem; margin: 1rem auto; width: 100%; box-sizing: border-box;">
  <div style="margin-bottom: 0.5rem; padding-left: 0.25rem;">
    <span style="font-size: 1.1rem;">📊</span>
  </div>
  <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
    <div style="text-align: center;">
      <div style="width: 90px;"><canvas id="chart-equiv-12"></canvas></div>
      <p style="font-size: 12px; color: #374151; margin-top: 0.25rem;">1/2</p>
    </div>
    <div style="text-align: center;">
      <div style="width: 90px;"><canvas id="chart-equiv-24"></canvas></div>
      <p style="font-size: 12px; color: #374151; margin-top: 0.25rem;">2/4</p>
    </div>
    <div style="text-align: center;">
      <div style="width: 90px;"><canvas id="chart-equiv-36"></canvas></div>
      <p style="font-size: 12px; color: #374151; margin-top: 0.25rem;">3/6</p>
    </div>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Chart !== 'undefined') {
    // 1/2
    if (document.getElementById('chart-equiv-12')) {
      new Chart(document.getElementById('chart-equiv-12'), {
        type: 'pie', data: { labels: ['1','2'], datasets: [{ data: [1,1], backgroundColor: ['#3b82f6','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] },
        options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
      });
    }
    // 2/4
    if (document.getElementById('chart-equiv-24')) {
      new Chart(document.getElementById('chart-equiv-24'), {
        type: 'pie', data: { labels: ['1','2','3','4'], datasets: [{ data: [1,1,1,1], backgroundColor: ['#3b82f6','#3b82f6','#e5e7eb','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] },
        options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
      });
    }
    // 3/6
    if (document.getElementById('chart-equiv-36')) {
      new Chart(document.getElementById('chart-equiv-36'), {
        type: 'pie', data: { labels: ['1','2','3','4','5','6'], datasets: [{ data: [1,1,1,1,1,1], backgroundColor: ['#3b82f6','#3b82f6','#3b82f6','#e5e7eb','#e5e7eb','#e5e7eb'], borderColor: '#374151', borderWidth: 2 }] },
        options: { responsive: true, plugins: { legend: { display: false }, tooltip: { enabled: false } } }
      });
    }
  }
});
</script>

Aunque tienen diferente numerador y denominador, **todas representan la mitad**.

---

## 📖 Amplificar fracciones

**Amplificar** significa multiplicar numerador y denominador por el mismo número.

### Ejemplo 1

Amplificar $\frac{2}{3}$ por $4$:

$$
\frac{2}{3} = \frac{2 \times 4}{3 \times 4} = \frac{8}{12}
$$

---

### Ejemplo 2

Amplificar $\frac{3}{5}$ por $6$:

$$
\frac{3}{5} = \frac{3 \times 6}{5 \times 6} = \frac{18}{30}
$$

---

## 📖 Simplificar fracciones

**Simplificar** significa dividir numerador y denominador por un factor común.

### Ejemplo 1

Simplificar $\frac{12}{18}$:

$$
\frac{12}{18} = \frac{12 \div 6}{18 \div 6} = \frac{2}{3}
$$

---

### Ejemplo 2

Simplificar $\frac{24}{36}$:

$$
\frac{24}{36} = \frac{24 \div 12}{36 \div 12} = \frac{2}{3}
$$

---

## 📖 Verificar equivalencia

Para verificar si dos fracciones son equivalentes, usamos el **producto cruzado**:

$$
\frac{a}{b} = \frac{c}{d} \quad \Leftrightarrow \quad a \times d = b \times c
$$

### Ejemplo 1

¿Son equivalentes $\frac{3}{4}$ y $\frac{9}{12}$?

$$
3 \times 12 = 36 \quad \text{y} \quad 4 \times 9 = 36
$$

Como $36 = 36$, **sí son equivalentes** ✓

---

### Ejemplo 2

¿Son equivalentes $\frac{2}{5}$ y $\frac{6}{14}$?

$$
2 \times 14 = 28 \quad \text{y} \quad 5 \times 6 = 30
$$

Como $28 \neq 30$, **no son equivalentes** ✗

---

## 📝 Ejercicios de práctica

**Ejercicio 1:** Amplifica $\frac{4}{7}$ por $5$.

**Ejercicio 2:** Simplifica $\frac{15}{25}$ a su mínima expresión.

**Ejercicio 3:** ¿Son equivalentes $\frac{5}{8}$ y $\frac{20}{32}$?

**Ejercicio 4:** Encuentra $x$ en $\frac{3}{4} = \frac{x}{20}$.

---