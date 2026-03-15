# Workshops App Payload v1

## Objetivo
Definir un contrato estable para clientes web y móvil, derivado en build-time desde los talleres `MD/MDX`, sin parsear markdown crudo en runtime.

La regla vigente para este payload es:

- `html` es la fuente principal de render
- `blocks` quedan como fallback legado
- los assets relativos del proyecto se normalizan a URLs absolutas desde backend

## Generación
Comando:

```bash
npm run workshops:manifest
```

Salida:
- `/tmp/ediprofe-workshops-manifest.json`

## Contrato de render

Cada payload expone:

```json
{
  "render_contract": {
    "strategy": "html_first",
    "html_primary_fields": [
      "context_html",
      "stem_html",
      "feedback_html",
      "concepts_html",
      "options.text_html"
    ],
    "block_fallback_fields": [
      "context_blocks",
      "stem_blocks",
      "feedback_blocks",
      "concepts_blocks"
    ],
    "asset_url_policy": "absolute_or_data_uri"
  }
}
```

### Regla práctica para clientes
1. Si existe `*_html`, renderiza `*_html`.
2. Si no existe `*_html`, usa `*_blocks`.
3. Si tampoco existe `*_blocks`, cae a texto plano solo como último fallback.

## Estructura por pregunta (v1)

```json
{
  "id": "1",
  "order": 1,
  "stem_mdx": "...",
  "stem_html": "<p>Texto de la pregunta</p>",
  "stem_assets": ["https://ediprofe.com/images/..."],
  "stem_blocks": [
    {
      "type": "paragraph",
      "inlines": [
        { "text": "Texto normal ", "variant": "plain" },
        { "text": "resaltado", "variant": "highlight" }
      ]
    }
  ],
  "context_html": "<p>Contexto compartido</p>",
  "context_assets": ["https://ediprofe.com/images/..."],
  "context_blocks": [],
  "options": [
    {
      "id": "A",
      "text": "Texto plano",
      "text_html": "<span>Texto rico</span>",
      "text_assets": ["https://ediprofe.com/images/..."]
    },
    {
      "id": "B",
      "text": "..."
    }
  ],
  "correct_option_id": "A",
  "feedback_mdx": "...",
  "feedback_html": "<p>Retroalimentación</p>",
  "feedback_assets": ["https://ediprofe.com/images/..."],
  "feedback_blocks": [],
  "concepts_html": "<p>Conceptos relacionados</p>",
  "concepts_assets": [],
  "concepts_blocks": [],
  "app_payload_version": 1
}
```

## Variantes inline soportadas en `blocks`
- `plain`
- `bold`
- `highlight`
- `strike`

## Regla de seguridad en API pública
Cuando `include_answers=false`, el backend debe ocultar:
- `correct_option_id`
- `feedback_mdx`
- `feedback_html`
- `feedback_assets`
- `feedback_blocks`
- `concepts_mdx`
- `concepts_html`
- `concepts_assets`
- `concepts_blocks`

## Modo de entrega para clientes
Consumo recomendado:

```text
GET /api/v1/workshops/{id}?published_only=false&include_answers=false&format=app
```

Con `format=app`, el backend puede omitir campos MDX crudos:
- `stem_mdx`
- `context_mdx`
- `feedback_mdx`
- `concepts_mdx`

Pero debe mantener:
- `stem_html`
- `context_html`
- `feedback_html`
- `concepts_html`
- `options[].text_html`

## Estado actual
- El exportador `scripts/export-workshops-manifest.mjs` ya genera HTML rico y `blocks`.
- Los `blocks` ya no se construyen por heurísticas de líneas; se derivan desde el árbol real de markdown/mdx.
- El sync backend (`workshops:sync-manifest`) persiste HTML, assets y fallback `blocks`.
- El backend normaliza assets relativos a URLs absolutas antes de responder a clientes.
- `members v2` ya consume este contrato en modo `html-first`.
- El frontend viejo de miembros se mantiene compatible, pero debe considerarse legado.

## Implicación para móvil
Para móvil, la recomendación vigente es:
- usar `html` como fuente principal con un renderer serio
- usar `blocks` solo cuando falte `html`
- no depender de parsear `MDX` o markdown crudo en la app
