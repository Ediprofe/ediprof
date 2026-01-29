---
description: Especificación técnica para la generación de Talleres tipo ICFES Saber 11
---

# 🎓 Especificación: Talleres Saber 11

Este documento define el formato estricto y las reglas de estructura para generar talleres de preguntas tipo ICFES (Selección Múltiple con Única Respuesta).

La IA debe seguir estas reglas para asegurar compatibilidad con:
1.  **Plataforma Web** (acordeones dinámicos y estilos "Magic CSS").
2.  **PDF Imprimible** (formato limpio de dos columnas).
3.  **PDF Retroalimentación** (incluye claves y explicaciones).

---

## 1. Estructura General del Archivo

- **Formato**: Markdown estándar con extensiones (frontmatter, details/summary, katex).
- **Ubicación**: `src/content/saber/[materia]/[tema]/taller.md`
- **Frontmatter**:
  ```yaml
  ---
  title: Taller: [Nombre del Tema]
  description: Taller de preguntas tipo Saber 11 sobre [Tema]
  ---
  ```

---

## 2. Bloque de Pregunta

Cada pregunta debe seguir este orden estricto:

1.  **Título de Nivel 2**: `## N.` (donde N es el número de pregunta).
2.  **Comentarios de Metadatos** (Opcional): Fuente, año.
3.  **Enunciado**: Texto claro. Puede incluir imágenes o ecuaciones.
4.  **Opciones de Respuesta**: Lista o texto con letras A, B, C, D.
5.  **Bloque de Retroalimentación**: Tag `<details>`.

### Ejemplo de Enunciado:
```markdown
## 1.

Un estudiante observa que...

![Descripción Imagen](url-imagen.webp)

¿Cuál es la conclusión correcta?

A. La opción A...
B. La opción B...
C. La opción C...
D. La opción D...
```

---

## 3. Bloque de Retroalimentación (`<details>`)

Este bloque es CRÍTICO. Contiene la clave de respuesta y la explicación pedagógica.

### Estructura Interna:

```html
<details>
<summary>✅ Respuesta</summary>

<!-- 1. ANÁLISIS DEL ENUNCIADO (Marcadores) -->
Texto con ==resaltado== de pistas clave y ~~tachado~~ de ideas erróneas.

<!-- 2. ANÁLISIS DE OPCIONES -->
A. Opción incorrecta ~~(Error conceptual)~~.
B. ==Opción Correcta== ✅
C. Opción incorrecta.

<!-- 3. CAJA VERDE: RESPUESTA Y EXPLICACIÓN DIRECTA -->
**Respuesta: B**

Explicación detallada...

<!-- 4. LISTAS DENTRO DE EXPLICACIÓN (Regla "Magic CSS") -->
* Item 1
* Item 2

<!-- 5. CAJA AZUL: INFORMACIÓN ADICIONAL (Opcional) -->
Nota pedagógica o curiosidad (texto sin negrita al inicio).

</details>
```

---

## 4. Reglas de Estilo "Magic CSS"

El sistema usa CSS avanzado (`:has()`, `+`) para dar estilo automáticamente según el contenido. **Sigue estas reglas para que funcione:**

### 🟢 Caja Verde (Respuesta Correcta)
*   Cualquier párrafo dentro del `<details>` que empiece con **negrita** (`**Texto:**`) se convertirá en una caja verde con checkmark.
*   **Uso:** Úsalo para decir `**Respuesta: X**` o `**Explicación:**`.

### 🔵 Caja Azul (Información Adicional)
*   El **último párrafo** del `<details>` se convertirá en una caja azul de información, SIEMPRE QUE **NO** empiece con negrita y NO sea una lista.
*   **Uso:** Tips extra, recordatorios o conceptos relacionados.

### 🔗 Fusión de Listas (Listas en Explicación)
*   **Regla:** Si una explicación requiere una lista (`<ul>` o `- items`), coloca la lista **inmediatamente después** del párrafo de la Caja Verde (`**Explicación:** ...`).
*   **Efecto:** El CSS fusionará visualmente la lista con la caja verde, creando un bloque continuo.
*   **NO** dejes texto "suelto" entre el párrafo de explicación y la lista.

---

## 5. Sintaxis de Marcadores de Texto

Ayudan al estudiante a "leer como un experto" (Descarte Activo):

- `==Texto Clave==`: Resalta pistas importantes en el enunciado o la respuesta correcta.
- `~~Texto Erróneo~~`: Tacha conceptos falsos o trampas en las opciones incorrectas.

---

## 6. Ejemplo Maestro

```markdown
## 5.

Un científico mide la temperatura...

A. Aumenta linealmente.
B. Se mantiene constante.
C. Disminuye exponencialmente.
D. Fluctúa al azar.

<details>
<summary>✅ Respuesta</summary>

El enunciado dice que el sistema es ==isotérmico==, lo que significa que la temperatura ==no cambia==.

A. ~~Aumenta~~ (No puede aumentar).
B. ==Se mantiene constante== ✅
C. ~~Disminuye~~ (No puede disminuir).
D. ~~Fluctúa~~.

**Respuesta: B**

Como el proceso es isotérmico ($\Delta T = 0$), la temperatura permanece constante durante todo el experimento. Esto se cumple bajo las siguientes condiciones:
* El sistema está aislado térmicamente.
* O el cambio es muy lento.
* O hay un reservorio térmico infinito.

Recuerda que en procesos adiabáticos la temperatura sí cambia.

</details>
```
