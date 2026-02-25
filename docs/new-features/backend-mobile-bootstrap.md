# Backend + Mobile Bootstrap (Estado actual)

Fecha: 2026-02-25
Rama: `dev`

## Objetivo de esta fase
Dejar la base tecnica ordenada para avanzar a:
- App movil React Native (Expo).
- Backend Laravel para control de acceso premium/gratuito.
- Reutilizar el contenido existente de Astro sin duplicacion.

## Lo ya implementado

### 1) Backend Laravel aislado
Se creo una nueva app en:
- `/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/backend`

Incluye:
- Laravel 12 inicializado.
- Endpoint inicial `GET /api/v1/health`.
- API routing habilitado en `bootstrap/app.php`.

### 2) Laravel Boost
Instalado y ejecutado en `apps/backend`:
- `composer require laravel/boost --dev`
- `php artisan boost:install --no-interaction`

Archivos clave generados por Boost:
- `/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/backend/boost.json`
- `/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/backend/.codex/config.toml`
- `/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/backend/AGENTS.md`

### 3) Skills instaladas en Codex (global)
Instaladas en `$CODEX_HOME/skills`:
- `astro-pdf-processing` (origen: `FredKSchott/astro-skills`, path `example/skills/pdf-processing`)
- `vercel-react-native-skills` (origen: `vercel-labs/agent-skills`, path `skills/react-native-skills`)

Nota:
- Se uso fallback `--method git` por error SSL en Python (`CERTIFICATE_VERIFY_FAILED`).
- Reinicia Codex para que queden disponibles en nuevas sesiones.

## Contrato de contenido ya disponible
Ya existe exportador en el proyecto Astro:
- Script: `/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/scripts/export-content-manifest.mjs`
- Comando: `npm run content:manifest`
- Salida default: `/tmp/ediprofe-content-manifest.json`

Ese JSON es la base para poblar catalogo en Laravel y para consumir en React Native.

## Siguiente fase recomendada (orden)
1. Crear tablas backend:
- `content_catalog`
- `plans`
- `subscriptions`
- `access_grants` (incluye excepcion estudiantes del colegio)

2. Crear comando Laravel:
- `php artisan content:sync-manifest /tmp/ediprofe-content-manifest.json`

3. Exponer API v1 para app:
- `POST /api/v1/auth/login`
- `GET /api/v1/content`
- `GET /api/v1/content/{id}`

4. Iniciar app Expo consumiendo esos endpoints.

## Comandos operativos
Backend local:
```bash
cd /Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/backend
php artisan serve --host=127.0.0.1 --port=8080
```

Health check:
```bash
curl -s http://127.0.0.1:8080/api/v1/health
```
