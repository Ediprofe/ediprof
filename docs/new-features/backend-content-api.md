# Backend Content API v1

## Endpoints implementados

### GET `/api/v1/content`
Retorna catalogo paginado desde la tabla `content_catalog`.

Query params soportados:
- `per_page` (1-100, default 20)
- `published` (`true|false`)
- `access_tier` (`free|premium`)
- `content_type` (`lesson|workshop`)
- `area_slug` (ej: `quimica`)
- `collection` (ej: `saber`)
- `search` (texto en titulo/descripcion)

Respuesta:
- `ok`
- `data[]`
- `meta` (paginacion)
- `links` (navegacion)

### GET `/api/v1/health`
Health endpoint del backend.

## Sincronizacion de catalogo

Comando:
```bash
cd /Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/backend
php artisan content:sync-manifest /tmp/ediprofe-content-manifest.json
```

Opciones:
- `--dry-run` valida sin escribir.
- `--prune-missing` elimina entradas no presentes en manifiesto.

## Tablas creadas
- `content_catalog`
- `plans`
- `subscriptions`
- `access_grants`

## Siguiente paso natural
Implementar `GET /api/v1/content/{external_id}` y middleware de autorizacion por `access_tier`.
