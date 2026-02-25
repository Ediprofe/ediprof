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

## Boost
Instalado con:
```bash
composer require laravel/boost --dev
php artisan boost:install --no-interaction
```

## Proximo objetivo funcional
1. Catalogo de contenido sincronizado desde `/tmp/ediprofe-content-manifest.json`.
2. Modelo de acceso: `free`, `premium` y excepcion `colegio_gratis`.
3. Endpoints para app movil (Expo/React Native): login, contenido, desbloqueos.
