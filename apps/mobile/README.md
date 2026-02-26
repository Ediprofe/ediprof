# Ediprofe Mobile (Expo MVP)

Esta app consume el backend Laravel de talleres.

## Ejecutar local

Requisito recomendado:
- Node `v22.x` (en este entorno, Node `v25` rompía el arranque de Expo Web).

1. Inicia backend:

```bash
cd /Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof
npm run backend:serve
```

Para pruebas en celular, usa backend en LAN:

```bash
cd /Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof
npm run backend:serve:lan
```

2. En otra terminal, instala y ejecuta Expo:

```bash
cd /Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/mobile
npm install
npm run start
```

Para pruebas en celular (recomendado):

```bash
cd /Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/mobile
npm run start:lan
```

Si tu red bloquea LAN:

```bash
npm run start:tunnel
```

3. En la app, usa `API Base URL`:
- Simulador en misma máquina: `http://127.0.0.1:8080/api/v1`
- Celular físico en red local: `http://<IP_LAN_DE_TU_MAC>:8080/api/v1`
- En celular no uses `localhost` ni `127.0.0.1`.

## Prueba real en celular (Expo Go)

1. Instala `Expo Go` en el celular.
2. Conecta celular y Mac a la misma red Wi-Fi.
3. Arranca backend en LAN:

```bash
cd /Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof
npm run backend:serve:lan
```

4. Arranca Expo en LAN:

```bash
cd /Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/mobile
npm run start:lan
```

5. Escanea el QR con Expo Go.
6. En la app móvil, configura `API Base URL` con la IP LAN de tu Mac
   (o toca **Usar detectada** si aparece):
`http://<IP_LAN_DE_TU_MAC>:8080/api/v1`

Ejemplo:
`http://192.168.1.1:8080/api/v1`

Comando útil para ver tu IP LAN (Mac):

```bash
ipconfig getifaddr en0
```

Si no abre desde el celular:
- Verifica que backend esté en `0.0.0.0:8080`.
- Revisa firewall local.
- Prueba `npm run start:tunnel`.

## Si Expo Go muestra "Project is incompatible"

Si ves el error de SDK (por ejemplo Expo Go SDK 54 y proyecto SDK 52), ejecuta migración local:

```bash
cd /Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/mobile
rm -rf node_modules package-lock.json
npm install
npx expo install --fix
npx expo doctor
```

Luego reinicia Metro:

```bash
npm run start:tunnel
```

## Flujo MVP

- Login (`/api/v1/auth/login`)
- Catálogo (`/api/v1/workshops?published=false` en modo demo actual)
- Detalle (`/api/v1/workshops/{id}?include_answers=false`)

## Build real (TestFlight y Play Internal)

Requisitos de cuentas:
- Apple Developer Program activo (USD 99/año).
- Google Play Console activo (pago único).
- Cuenta Expo (gratis) para EAS Build.

Comandos iniciales (una sola vez):

```bash
cd /Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/mobile
npm run eas:login
npm run eas:init
```

Build de prueba interna:

```bash
npm run eas:build:ios:preview
npm run eas:build:android:preview
```

Instalar el último build Android en emulador (requiere AVD encendido):

```bash
npm run eas:run:android:latest
```

Build para tienda:

```bash
npm run eas:build:ios:prod
npm run eas:build:android:prod
```

Publicar (cuando ya tengas metadata/listings listas):

```bash
npm run eas:submit:ios:prod
npm run eas:submit:android:prod
```

Notas:
- iOS usa TestFlight para pruebas reales.
- Android usa Internal testing track de Play Console.
- Si cambias nombre/identificadores (`bundleIdentifier` o `package`), hazlo antes del primer envío a store.

## Preview web de apoyo

Para validar datos sin Expo:

`http://127.0.0.1:8080/dev/workshops/preview`
