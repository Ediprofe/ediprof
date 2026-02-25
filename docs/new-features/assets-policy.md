# Politica Canonica de Assets (Web + App)

## Objetivo
Unificar referencias de imagen para que el contenido de Astro, backend Laravel y app movil React Native usen una fuente canónica sin romper rutas legacy durante la transicion.

## URL canónica
- Formato oficial: `https://cdn.ediprofe.com/img/{materia}/{id}-{slug}.{ext}`
- Para talleres Saber: `https://cdn.ediprofe.com/img/saber/{materia}/{id}-{slug}.{ext}`

## Regla operativa
1. Todo asset nuevo se sube con `npm run img`.
2. El indice `images-index.json` conserva `url` canónica y `aliases` legacy cuando aplique.
3. Rutas legacy (`/images`, `/ilustraciones`, `/illustrations`, `cdn.../images`) se mantienen temporalmente por compatibilidad.
4. La migracion de contenido historico es gradual (por lotes), sin frenar publicacion.

## Scripts de apoyo
- `npm run assets:audit`: reporte no bloqueante de referencias canónicas/legacy (salida por defecto en `/tmp`).
- `npm run assets:audit:strict`: modo bloqueante con baseline (`docs/new-features/assets-audit-baseline.json`) para evitar regresiones.
- `npm run assets:migrate`: codemod seguro de referencias legacy (`--write` para aplicar, `--include-local` opcional).
- `npm run assets:manifest`: genera manifiesto de assets para consumo backend/app (salida por defecto en `/tmp`).
- `npm run img --normalize-index`: migra URLs legacy del indice a URL canónica.

## Gate en despliegue
- Netlify ejecuta `npm run assets:audit:strict` antes del build.
- Si una categoría legacy supera la línea base, el build falla.

## Checklist de contenido nuevo
1. Subir imagen a CDN con `npm run img`.
2. Pegar markdown generado por el script.
3. Evitar rutas locales nuevas (`/images`, `/ilustraciones`, `/illustrations`) en contenido nuevo.
