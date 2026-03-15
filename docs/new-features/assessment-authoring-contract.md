# Contrato editorial para talleres, simulacros y evaluaciones

Este contrato deja claro qué se autoriza en `MDX`, qué se exporta al backend y qué consume la web de miembros o un futuro cliente móvil.

## Principios
- `Astro/MDX` sigue siendo la fuente editorial principal.
- `Laravel` es la fuente de verdad para preguntas, contextos, asignaciones, intentos y resultados.
- `Filament` administra cursos, asignaciones y resultados; no es el editor rico principal de preguntas.
- El contenido debe ser reutilizable y resistente a reordenamientos.
- La taxonomía mutable (`tema`, `unidad`, `subtema`, `tags`, `origen`, `estado editorial`, `notas docentes`) se administra en backend y no se obliga en `MDX`.

## Componentes de autoría recomendados
Importa siempre estos componentes en `taller.mdx` o `simulacro.mdx`:

```mdx
import Pregunta from '@/components/saber/Pregunta.astro';
import Opciones from '@/components/saber/Opciones.astro';
import Opcion from '@/components/saber/Opcion.astro';
import ContextoCompartido from '@/components/saber/ContextoCompartido.astro';
import Respuesta from '@/components/saber/Respuesta.astro';
import ConceptosRelacionados from '@/components/saber/ConceptosRelacionados.astro';
```

## Contrato de pregunta
Cada pregunta debe tener:
- un encabezado `## N.` o `## N (Sesión X).`
- un `<Pregunta id="...">`
- un bloque `<Opciones>`
- exactamente una `<Opcion correcta>`
- una retroalimentación usando `<Respuesta>` o, por compatibilidad, `<details>`

Ejemplo:

```mdx
## 12 (Sesión 1).
<Pregunta id="S1-12" fuente="ICFES" anio="2026" context="ctx-s1-bio-12">

Enunciado de la pregunta.

<Opciones>
  <Opcion letra="A">Opción A</Opcion>
  <Opcion letra="B" correcta>Opción B</Opcion>
  <Opcion letra="C">Opción C</Opcion>
  <Opcion letra="D">Opción D</Opcion>
</Opciones>

<Respuesta summary="Solución guiada">

Explicación de la respuesta.

**Respuesta: B**

</Respuesta>

<ConceptosRelacionados>

Profundización, imágenes o recordatorios del tema.

</ConceptosRelacionados>

</Pregunta>
```

## Contrato de contexto compartido
Cuando varias preguntas compartan contexto, usa un bloque explícito:

```mdx
<ContextoCompartido id="ctx-s1-bio-12" title="Cadena alimentaria en humedales">

RESPONDA LAS PREGUNTAS 12 A 14 CON BASE EN LA SIGUIENTE INFORMACIÓN.

Texto, imágenes, tablas o ecuaciones del contexto.

</ContextoCompartido>
```

Y referencia ese contexto desde cada pregunta:

```mdx
<Pregunta id="S1-12" context="ctx-s1-bio-12">
```

## Reglas de IDs
- `Pregunta.id` debe ser único dentro del archivo.
- `ContextoCompartido.id` debe ser único dentro del archivo.
- `Pregunta.context` debe referenciar contextos existentes.
- No depender de la posición del contexto para que el vínculo funcione.
- `Pregunta.id` puede repetirse en otro archivo distinto; la identidad global se resuelve en backend con `template + id local`.

## Assets
Se permiten:
- rutas canónicas del proyecto (`/images/...`)
- CDN canónico (`https://cdn.ediprofe.com/...`)

El exportador registra:
- `asset_refs`
- referencias por pregunta
- referencias por contexto

Esto permite que web y móvil consuman el mismo material sin entender Astro.

## Salida canónica para clientes
El backend debe exponer el contenido rico con esta prioridad:

1. `html` como fuente principal de render
2. `blocks` como fallback legado
3. texto plano solo como último recurso

Eso aplica a:
- `context_html`
- `stem_html`
- `feedback_html`
- `concepts_html`
- `options[].text_html`

Y como fallback:
- `context_blocks`
- `stem_blocks`
- `feedback_blocks`
- `concepts_blocks`

Los assets relativos del proyecto deben salir normalizados a URL absoluta canónica desde backend, para que:
- web autenticada
- web pública
- y cliente móvil

consuman el mismo contrato sin asumir mismo origen.

## Compatibilidad actual
El pipeline todavía soporta:
- `<details>` para retroalimentación
- contexto compartido legado por rango (`RESPONDA LAS PREGUNTAS X A Y`)

Pero la recomendación hacia adelante es:
- usar `<Respuesta>`
- usar `<ConceptosRelacionados>`
- usar `<ContextoCompartido id="...">`

## Validación
Antes de sincronizar, ejecuta:

```bash
npm run workshops:preflight
```

Ese preflight valida:
- IDs duplicados
- opción correcta faltante o múltiple
- referencias de assets
- contexto compartido explícito o legado
- contenido exportable al backend
