# Ediprofe Academia Repo Extraction Plan

## Decision summary

The academic product should stop living inside the public `ediprofe.com` repo as its long-term home.

Recommended end state:

- `ediprofe-web`:
  - public website
  - Astro
  - editorial/public marketing surface
- `ediprofe-academia`:
  - Laravel backend
  - Filament admin
  - Inertia + React student web app
  - Expo / React Native mobile app
  - canonical content store
  - asset publication pipeline

This is **not** a recommendation to build another backend from scratch.
It is a recommendation to:

- keep the current Laravel backend as the real product nucleus
- stop tying the academic platform to the public site repo
- treat `MDX` as an import path, not as the permanent source of truth

## Recommended domain model

Recommended production domains:

- `ediprofe.com`
  - public site
- `app.ediprofe.com`
  - academic platform
- `app.ediprofe.com/admin`
  - Filament admin / teacher backoffice
- `app.ediprofe.com/api/v1`
  - API for mobile and integrations

Why `app.ediprofe.com` and not `miembros.ediprofe.com`:

- the product is no longer only a "members area"
- it will include student app, teacher workflows, API, and admin
- `app` is more durable and easier to explain

## Why separate the repo

Right now the repo mixes four concerns that should evolve at different speeds:

1. public/editorial website
2. academic backend and operations
3. student web app
4. mobile app

That coupling has already created friction:

- content assets are resolved as if they belonged to the public Astro site
- student UX changes are blocked by public-site assumptions
- mobile needs a cleaner contract than the public site ever needed
- the old Astro members area keeps competing with the new web app

The repo split is recommended so the academic product can evolve as a platform, not as a subsection of the public site.

## What stays in the current public repo

These parts conceptually belong to the public website and should remain in `ediprofe-web`:

- `/src`
  - all public Astro pages
  - public layouts
  - public editorial rendering
- `/astro.config.mjs`
- `/netlify.toml`
- public-site-only scripts that support the editorial web output

These old member pages should be considered legacy and eventually removed from the public repo:

- `/src/pages/miembros/*`

They should not receive new product work.

## What moves to the new academic repo

These parts belong in `ediprofe-academia`:

- `/apps/backend`
- `/apps/mobile`

And the academic/content tooling that supports the platform:

- `/scripts/export-workshops-manifest.mjs`
- `/scripts/export-content-manifest.mjs`
- `/scripts/export-assets-manifest.mjs`
- `/scripts/upload-to-r2.mjs`
- `/scripts/svg-to-png.mjs`
- `/scripts/workshops-preflight.mjs`
- `/scripts/workshops-watch-dev.mjs`
- `/scripts/workshops-autofix-feedback-options.mjs`
- `/scripts/preprocess-markdown.mjs`

Renderer and asset-generation families that are part of academic content production should also move:

- `/scripts/geometry`
- `/scripts/physics`
- `/scripts/diagrams`
- `/scripts/mindmap`
- `/scripts/functions`
- `/scripts/plots` if they are part of academic content generation

Academic docs should move too:

- `/docs/new-features/backend-*`
- `/docs/new-features/content-manifest.md`
- `/docs/new-features/workshops-app-payload-v1.md`
- `/docs/new-features/assessment-authoring-contract.md`
- `/docs/new-features/assets-policy.md`
- `/docs/new-features/members-v2-migration-plan.md`
- this document

## Recommended structure for the new repo

```text
ediprofe-academia/
  apps/
    backend/
    mobile/
  packages/
    content-schema/
    render-contract/
  scripts/
    export/
    assets/
    renderers/
  docs/
  infra/
```

Notes:

- `apps/backend` stays Laravel.
- `apps/mobile` stays Expo.
- `packages/content-schema` should hold shared types and contracts for:
  - content fragments
  - assets
  - assignments
  - attempts
- `packages/render-contract` can hold shared helpers or schema validation if needed.

## What becomes the source of truth

Long-term source of truth should be **Laravel database + storage**, not `MDX`.

Recommended content ownership model:

- Laravel stores canonical question/context/option records
- Laravel stores canonical asset references
- Laravel serves web and mobile from the same backend model

`MDX` should become:

- an import mechanism
- a migration bridge
- an editorial tool for legacy/public content if still useful

But not:

- the permanent source of truth for the academic platform
- the thing web and mobile depend on at runtime

## Canonical content contract

The academic platform should standardize on this model per rich fragment:

- `plain_text`
- `html_web`
- `nodes_mobile`
- `asset_refs`

This applies to:

- context
- stem
- options
- feedback
- related concepts

### Web

Web student app should use:

- `html_web` as primary render source

### Mobile

Mobile should use:

- `nodes_mobile` as primary render source

### Asset strategy

Every rich fragment should reference assets by stable metadata, not by ad hoc relative paths:

- asset id
- canonical URL
- mime type
- width/height if known
- fallback image URL when needed

## SVG and generated assets strategy

The SVG problem is not that the renderers live in your project.
The problem is that the final clients are consuming assets as if they were tied to one website origin.

Recommended strategy:

1. keep the render engines in the academic repo
2. generate SVG assets from those engines during content build/import
3. publish resulting assets to a stable public origin
4. store the published asset reference in Laravel

Recommended public asset origin:

- short term: `https://ediprofe.com/assets/...` if that is already stable
- better long term: `https://cdn.ediprofe.com/...`

The important part is not whether the file started as local SVG.
The important part is:

- clients receive a stable, public, canonical asset URL

## What to stop doing

To avoid losing more time, stop doing these things as product strategy:

- stop improving the old Astro members area
- stop making the public site the runtime source for the academic app
- stop treating relative asset paths as acceptable client contract
- stop relying on lossy/manual fallback formats as the long-term render strategy
- stop adding new core features before the repo/domain/content boundaries are frozen

## Migration order

### Phase 1. Freeze the old surface

- old Astro `miembros` becomes legacy
- bugfixes only if unavoidable
- no new product work there

### Phase 2. Freeze the academic architecture in the current repo

- keep `apps/backend` as the central backend
- keep `apps/mobile`
- keep `members v2` as the only active student web app
- define the final content contract

### Phase 3. Extract to new repo

Create `ediprofe-academia` and move:

- `apps/backend`
- `apps/mobile`
- academic scripts
- academic docs

The current public repo keeps only public-site concerns.

### Phase 4. Move domain boundary

- keep `ediprofe.com` on the public site
- point `app.ediprofe.com` to the Laravel academic app
- keep `/admin` there for Filament

### Phase 5. Migrate content ownership

- import current `MDX` content into Laravel content tables
- make Laravel the source of truth
- keep `MDX` only as migration/editorial legacy if still needed

### Phase 6. Remove remaining legacy paths

- retire the old Astro members pages
- retire fragile compatibility layers once web and mobile use the canonical contract

## Practical recommendation right now

Do **not** start by moving folders around first.

Do this first:

1. finish freezing the architecture
2. define canonical content tables and asset model in Laravel
3. keep `members v2` as the only active student web path
4. then extract to the new repo

This order matters because otherwise we risk moving the same confusion into a second repository.

## Recommended naming

Suggested repo names:

- `ediprofe-web`
- `ediprofe-academia`

Suggested product naming:

- public: `Ediprofe`
- platform: `Ediprofe App`

Suggested deployment surfaces:

- `ediprofe.com`
- `app.ediprofe.com`

## Final recommendation

If we optimize for flexibility, maintainability, and a clean path to mobile, the best move is:

- separate the academic platform from the public site repo
- keep Laravel as the only backend nucleus
- move the student web app to Laravel + Inertia + React
- keep Filament as admin
- keep Expo for mobile
- move the content source of truth into Laravel
- treat `MDX` as migration/editorial legacy, not as the final foundation

That is the route I would choose if this were my product and I wanted it to last.
