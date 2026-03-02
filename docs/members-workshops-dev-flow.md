# Flujo de Desarrollo: Talleres Saber + Zona Miembros

Este flujo sirve para ver rápido en local un taller nuevo generado por el agente.

## 1) Crear o editar el taller

Ejemplo:

`src/content/saber/quimica/02-atomos-y-configuracion-electronica/taller.mdx`

## 2) Refrescar manifiesto y backend (un solo comando)

En la raíz del proyecto:

```bash
npm run workshops:refresh:dev
```

Este comando ejecuta:

1. `npm run workshops:manifest`
2. `php artisan workshops:sync-manifest /tmp/ediprofe-workshops-manifest.json`

## 3) Levantar servidores

Terminal A (Astro):

```bash
npm run dev:all
```

Terminal B (Backend Laravel):

```bash
npm run backend:serve
```

## 4) Verificación rápida

- Revisión técnica rápida (sin login): `http://localhost:4321/dev/talleres`
- Catálogo miembros: `http://localhost:4321/miembros/talleres`
- Práctica de un taller: desde el botón `Practicar` del catálogo
- Vista de impresión (sin login):  
  `http://localhost:4321/print-saber/<slug-limpio>/taller?mode=default`

Ejemplo de slug limpio:

`quimica/atomos-y-configuracion-electronica`

## Si vuelve a salir “No hay talleres disponibles”

1. Revisa sesión: cerrar y volver a entrar en `/miembros/login`
2. Corre de nuevo: `npm run workshops:refresh:dev`
3. Verifica API base en login miembros:
   - local: `http://127.0.0.1:8080/api/v1`
4. Comprueba backend:

```bash
curl -s "http://127.0.0.1:8080/api/v1/workshops?published=false&per_page=60"
```
