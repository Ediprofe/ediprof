# Backend API Roadmap (Laravel)

## Vision
Backend unico para habilitar:
- Contenido gratuito abierto.
- Talleres Saber premium por suscripcion.
- Excepcion de acceso gratuito para estudiantes del colegio (regla administrable).

## Modelo inicial recomendado

### Tabla `content_catalog`
- `id` (bigint autoincrement)
- `external_id` (string, unique) -> viene de `content:manifest`
- `title` (string)
- `route` (string)
- `content_type` (`lesson|workshop`)
- `access_tier` (`free|premium`)
- `area_slug` (string)
- `unidad_slug` (string, nullable)
- `tema_slug` (string, nullable)
- `is_published` (bool)
- `metadata` (json)
- timestamps

### Tabla `plans`
- `id`
- `code` (`premium_monthly`, etc)
- `name`
- `price_cents`
- `currency`
- `is_active`
- timestamps

### Tabla `subscriptions`
- `id`
- `user_id`
- `plan_id`
- `status` (`active|canceled|past_due|trialing`)
- `starts_at`
- `ends_at`
- `provider` / `provider_subscription_id`
- timestamps

### Tabla `access_grants`
- `id`
- `user_id`
- `scope` (`global|area|content`)
- `scope_ref` (nullable)
- `reason` (`school_whitelist|admin_override|promo`)
- `starts_at`
- `ends_at`
- timestamps

## Comandos artisan
1. `content:sync-manifest {path}` (implementado)
- sincroniza `content_catalog` desde `/tmp/ediprofe-content-manifest.json`

2. `access:grant-school {user}` (pendiente)
- otorga acceso gratuito segun regla del colegio

## API v1 (primer corte)
1. `GET /api/v1/health` (implementado)
2. `GET /api/v1/content` (implementado)
3. `POST /api/v1/auth/login` (pendiente)
4. `GET /api/v1/content/{external_id}` (pendiente)
5. `GET /api/v1/me/access` (pendiente)

## Regla de autorizacion (resumen)
Permitir contenido si:
1. `access_tier=free`, o
2. suscripcion premium activa, o
3. tiene `access_grants` vigente.

## Integracion con app Expo
- La app consume `GET /api/v1/content`.
- Cacha lista + assets para offline basico.
- Antes de abrir un taller premium, verifica autorizacion local + refresh remoto.
