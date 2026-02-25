# Workshops App Payload v1

## Objetivo
Definir un contrato nativo para app móvil, derivado en build-time desde los talleres MD/MDX, evitando parsear markdown crudo en runtime.

## Generación
Comando:

```bash
npm run workshops:manifest
```

Salida:
- `/tmp/ediprofe-workshops-manifest.json`

Desde esta versión, cada pregunta incluye bloques listos para UI nativa:
- `stem_blocks`
- `feedback_blocks`
- `app_payload_version`

## Estructura por pregunta (v1)

```json
{
  "id": "1",
  "order": 1,
  "stem_mdx": "...",
  "stem_assets": ["https://cdn..."],
  "stem_blocks": [
    {
      "type": "paragraph",
      "inlines": [
        { "text": "Texto normal ", "variant": "plain" },
        { "text": "resaltado", "variant": "highlight" },
        { "text": " y ", "variant": "plain" },
        { "text": "tachado", "variant": "strike" }
      ]
    },
    { "type": "equation", "latex": "4Fe + 3O_2 \\rightarrow 2Fe_2O_3" },
    { "type": "table", "rows": [["A", "B"], ["1", "2"]] },
    { "type": "image", "src": "https://cdn...", "alt": "Diagrama" }
  ],
  "options": [
    { "id": "A", "text": "..." },
    { "id": "B", "text": "..." }
  ],
  "correct_option_id": "A",
  "feedback_mdx": "...",
  "feedback_assets": ["https://cdn..."],
  "feedback_blocks": [
    {
      "type": "paragraph",
      "inlines": [
        { "text": "Respuesta: ", "variant": "bold" },
        { "text": "A", "variant": "plain" }
      ]
    }
  ],
  "app_payload_version": 1
}
```

## Variantes de inline soportadas (v1)
- `plain`
- `bold`
- `highlight`
- `strike`

## Regla de seguridad en API pública
Cuando `include_answers=false`, el backend debe ocultar:
- `correct_option_id`
- `feedback_mdx`
- `feedback_assets`
- `feedback_blocks`

## Modo de entrega para app nativa
Para clientes móviles, usar:

```text
GET /api/v1/workshops/{id}?published_only=false&include_answers=false&format=app
```

Con `format=app`, cada pregunta omite campos MDX crudos:
- `stem_mdx`
- `feedback_mdx`

El cliente debe renderizar desde `stem_blocks` y `feedback_blocks`.

## Estado actual
- Exportador `scripts/export-workshops-manifest.mjs` ya genera `stem_blocks` y `feedback_blocks`.
- Backend sync (`workshops:sync-manifest`) persiste esos bloques en `questions`.
- App móvil consume bloques cuando están disponibles; si faltan, cae a parser local.
