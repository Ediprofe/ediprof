# PARTE 1: Registro de Problemas y Mejoras Técnicas

## 🚨 Optimización del Build y Peso del Sitio

**Fecha de reporte:** 23 de diciembre de 2025
**Estado:** Pendiente
**Prioridad:** Media/Alta (para escalabilidad futura)

### 📝 Descripción del Problema
Durante el proceso de build (`npm run build`), se detectó que el tamaño total de la carpeta de salida (`dist/`) es desproporcionadamente grande (~700MB+ para ~600 páginas), lo que provocó un error de espacio en disco en el entorno local.

### 🔍 Análisis de Causa
El peso excesivo **no se debe a las imágenes** (que están bien optimizadas, ~11MB en total), sino a la estructura del HTML generado:

1.  **Redundancia del Menú de Navegación:**
    *   El componente `Sidebar` (y `MobileMenu`) carga y renderiza el árbol de navegación **completo** de todas las materias (Matemáticas, Física, Química, Ciencias) en **cada una** de las páginas generadas.
    *   Esto significa que el código HTML de cientos de enlaces se repite idénticamente en más de 600 archivos HTML.
2.  **Peso por Archivo:**
    *   Cada archivo `index.html` pesa entre **700KB y 1MB** (texto plano), lo cual es muy alto para una página de contenido estándar.
    *   Cálculo estimado: ~1MB x 600 páginas = ~600MB de redundancia.

### 💡 Propuestas de Solución

#### 1. Navegación Contextual (Recomendada)
Modificar el `Sidebar` para que solo cargue la estructura de la materia actual.
*   **Ejemplo:** Si el usuario está en `/fisica/...`, el menú solo muestra el árbol de Física.
*   **Beneficio:** Reducción estimada del 60-75% del peso total del HTML.
*   **Impacto UX:** Menos ruido visual para el usuario, navegación más enfocada.

#### 2. Carga Diferida (Client-Side Fetching)
Generar el menú como un archivo JSON estático (`menu.json`) y renderizarlo en el cliente con JavaScript.
*   **Beneficio:** El HTML inicial es muy ligero.
*   **Contra:** Posible "flicker" (parpadeo) al cargar la página mientras aparece el menú. Peor SEO para enlaces internos si los crawlers no ejecutan JS.

#### 3. Islas de Servidor (Astro Server Islands)
Utilizar renderizado dinámico para el menú.
*   **Contra:** Requiere cambiar a modo SSR (Server Side Rendering), lo que podría implicar costos o límites en Vercel (Serverless Functions).

### 🚀 Pasos Siguientes
1.  Implementar la **Navegación Contextual** en `src/components/Navigation/CollapsibleSidebar.astro` y `MobileMenu.astro`.
2.  Verificar la reducción de tamaño en un nuevo build.


# PARTE 2: Opinión de Gemini PRO

Este es un problema clásico en sitios de documentación o educación con **SSG (Static Site Generation)**. Cuando el árbol de navegación crece, el "costo" de repetirlo en cada archivo HTML se vuelve exponencial.

Para mantenerte en los planes gratuitos (como Vercel o Netlify) y que el sitio vuele, la clave es **eliminar la redundancia estructural**. Aquí tienes tres estrategias técnicas para solucionar el problema:

---

## 1. Implementación de Navegación Contextual (La solución más rápida)

Como bien analizaste, no necesitas el árbol de Química si el usuario está leyendo sobre Cinemática en Física. Puedes filtrar los datos del menú antes de renderizarlos.

**En tu componente `Sidebar.astro`:**

```astro
---
// Obtén la ruta actual
const { pathname } = Astro.url;

// Supongamos que tus rutas son /fisica/leccion-1, /quimica/leccion-1
const currentSection = pathname.split('/')[1]; 

// Filtra el JSON o array de navegación
const fullNavigation = await getNavigationData(); // Tu función actual
const contextualNavigation = fullNavigation.filter(item => 
  item.slug.startsWith(`/${currentSection}`) || item.isGlobal
);
---

<nav>
  {contextualNavigation.map(item => (
    <a href={item.href}>{item.label}</a>
  ))}
</nav>

```

* **Resultado:** Si cada materia tiene 150 páginas, pasarás de renderizar 600 enlaces a solo 150 por página.
* **Ahorro:** ~75% de reducción de peso por archivo.

---

## 2. El patrón "Híbrido": SEO en HTML + Detalles en JSON

Si quieres que el usuario pueda saltar de una materia a otra sin recargar el menú completo, usa este enfoque:

1. **HTML Estático (SEO):** Renderiza solo los niveles superiores (Matemáticas, Física, Química) y la lección actual.
2. **JSON para el resto:** Genera un archivo `nav-data.json` en la carpeta `public/`.
3. **Carga bajo demanda:** Solo cuando el usuario haga clic en un botón de "Ver todas las lecciones" o al hacer *hover* sobre el sidebar, cargas el JSON con JavaScript y construyes el resto del menú.

**Beneficio:** El crawler de Google ve los enlaces principales (bueno para el SEO), pero el peso del HTML cae drásticamente.

---

## 3. Evita la "Serialización de Props" (Punto Crítico en Astro)

A veces el peso no está en el HTML visible, sino en un bloque de `<script type="application/json">` que Astro inserta automáticamente si pasas objetos grandes a **componentes de React/Vue/Svelte** (hidratación).

Si estás haciendo esto:
`<Sidebar client:load navigationData={hugeObject} />`

Astro guarda `hugeObject` dentro del HTML de **cada página**.

**Solución:** * Usa componentes de Astro puros (`.astro`) para el sidebar siempre que sea posible.

* Si necesitas interactividad, usa **Custom Elements (Web Components)** nativos o busca el JSON mediante un `fetch` en el cliente en lugar de pasarlo como prop.

---

## Comparativa de Impacto

| Estrategia | Dificultad | Impacto en Peso | SEO |
| --- | --- | --- | --- |
| **Contextual (Filtro)** | Baja | ⭐⭐⭐ (Muy alto) | Excelente |
| **JSON Fetching** | Media | ⭐⭐⭐⭐ (Máximo) | Moderado |
| **Optimizar Props** | Media | ⭐⭐ (Variable) | Excelente |

---

## Mi recomendación para tu caso (https://www.google.com/search?q=ediprofe.com)

Dado que eres docente y buscas que el sitio sea un referente, la **Navegación Contextual** es tu mejor opción porque:

1. **No rompe el SEO:** Google sigue indexando cada materia perfectamente.
2. **Mantiene la velocidad:** Al ser menos HTML, el navegador parsea la página mucho más rápido (mejorando el *Largest Contentful Paint*).
3. **Sigue siendo 100% Gratis:** No necesitas servidores ni funciones dinámicas.
