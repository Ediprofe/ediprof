# Content Manifest (Laravel + React Native)

## Objetivo
Generar un contrato unico de contenido desde `src/content` para que web, backend y app movil consuman la misma fuente.

## Comando
- `npm run content:manifest`
- Salida por defecto: `/tmp/ediprofe-content-manifest.json`

Opciones:
- `--output <ruta>`: cambia la ruta de salida.
- `--published-only`: exporta solo entradas publicadas.

## Campos clave por entrada
- `id`: identificador estable (`content:<collection>:<slug>`).
- `contentType`: `lesson` o `workshop`.
- `accessTier`: `free` o `premium` (por defecto, `saber` es `premium`).
- `route`: ruta web (`/quimica/...` o `/saber/...`).
- `flags.published`: estado calculado por frontmatter/meta (`draft`).
- `assets.refs`: referencias de imagen detectadas para cache/offline.
- `unidad` y `tema`: metadatos listos para filtros en app y backend.

## Uso recomendado
1. Generar manifiesto: `npm run content:manifest`.
2. Backend Laravel importa/lee el JSON para poblar catalogo y reglas de acceso.
3. App React Native consume el mismo JSON para listado, filtros y prefetch de assets.

## Nota de negocio
- Contenido general: `accessTier=free`.
- Talleres Saber: `accessTier=premium`.
- Excepciones (estudiantes del colegio gratis) se aplican en backend con reglas de `access_grants`.
