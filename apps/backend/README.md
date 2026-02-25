# Ediprofe Backend (Laravel)

Backend API para autenticacion, autorizacion y catalogo de contenido (web + app movil).

## Stack base
- Laravel 12
- PHP 8.5
- Laravel Boost instalado (`laravel/boost`)

## Estructura
- `routes/api.php`: endpoints API versionados (`/api/v1/...`).
- `boost.json`: configuracion de Boost.
- `.codex/config.toml`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`: guias para agentes IA.

## Quick start
```bash
cd apps/backend
composer install
cp .env.example .env
php artisan key:generate
php artisan migrate
php artisan serve --host=127.0.0.1 --port=8080
```

Health check:
- `GET http://127.0.0.1:8080/api/v1/health`

Content catalog:
- `GET http://127.0.0.1:8080/api/v1/content`

## Boost
Instalado con:
```bash
composer require laravel/boost --dev
php artisan boost:install --no-interaction
```

## Proximo objetivo funcional
1. Login/API tokens y middleware de autorizacion.
2. Reglas de acceso por suscripcion + grants de colegio.
3. Endpoint de detalle de contenido y progreso por estudiante.

## Sincronizacion de catalogo
Comando disponible:
```bash
php artisan content:sync-manifest /tmp/ediprofe-content-manifest.json
```

Opciones:
- `--dry-run` valida sin escribir en DB.
- `--prune-missing` elimina entradas que no esten en el manifiesto.
