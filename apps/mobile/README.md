# Ediprofe Mobile (Expo MVP)

Esta app consume el backend Laravel de talleres.

## Ejecutar local

1. Inicia backend:

```bash
cd /Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof
npm run backend:serve
```

2. En otra terminal, instala y ejecuta Expo:

```bash
cd /Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/mobile
npm install
npm run start
```

3. En la app, usa `API Base URL`:
- Simulador en misma máquina: `http://127.0.0.1:8080/api/v1`
- Celular físico en red local: `http://<IP_LAN_DE_TU_MAC>:8080/api/v1`

## Flujo MVP

- Login (`/api/v1/auth/login`)
- Catálogo (`/api/v1/workshops`)
- Detalle (`/api/v1/workshops/{id}?include_answers=false`)

## Preview web de apoyo

Para validar datos sin Expo:

`http://127.0.0.1:8080/dev/workshops/preview`

