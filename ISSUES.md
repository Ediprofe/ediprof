# Registro de Problemas y Mejoras Técnicas

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
