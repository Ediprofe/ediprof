# Members v2 Migration Plan

## Decision summary

We will split the product into two clear fronts:

- `ediprofe.com`: public editorial site in Astro, static output.
- `miembros.ediprofe.com`: authenticated student app served by Laravel.

Inside Laravel we keep two surfaces:

- `miembros.ediprofe.com`: student web app with Inertia + React.
- `miembros.ediprofe.com/admin`: Filament admin / teacher backoffice.

We do **not** remove the Laravel API. We keep and strengthen it for mobile and integrations.

This means the final architecture is:

- Astro: public content and editorial publishing.
- Laravel + Filament: academic backend and admin.
- Laravel + Inertia + React: student web app.
- Laravel API + Sanctum / token exchange: mobile app.
- Expo / React Native: mobile client later.

## Why this decision

The current student area in Astro has already crossed the line from "content pages" into "app behavior":

- authenticated dashboard
- assignment states
- attempts and resuming
- review release
- progress navigation
- rich question rendering

That behavior can keep working in Astro, but it becomes increasingly fragile to evolve there. The backend model is in a good place; the frontend surface is where the instability is accumulating.

The goal of this migration is to:

- stop growing `miembros` as a page-oriented Astro frontend
- move the authenticated app to a more appropriate web-app stack
- keep the public site untouched
- keep the mobile path clean

## Current repo reality

### Public site

- Astro is configured as static output in [/astro.config.mjs](/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/astro.config.mjs).
- The public build is published from `dist` in [/netlify.toml](/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/netlify.toml).

### Backend

- Laravel lives in [/apps/backend](/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/backend).
- Filament is already the right admin solution and should stay.
- The current student area consumes JSON API endpoints in [/apps/backend/routes/api.php](/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/backend/routes/api.php).
- Google login currently happens through `POST /api/v1/auth/google/login` in [/apps/backend/app/Http/Controllers/Api/V1/AuthController.php](/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/backend/app/Http/Controllers/Api/V1/AuthController.php).

### Mobile

- There is already an Expo app scaffold in [/apps/mobile](/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/mobile).

## Target architecture

```text
Public editorial site
ediprofe.com
  -> Astro static site

Authenticated academic app
miembros.ediprofe.com
  -> Laravel web routes
  -> Inertia + React pages
  -> Session / cookie auth for web

Teacher/admin backoffice
miembros.ediprofe.com/admin
  -> Filament

API for mobile + integrations
miembros.ediprofe.com/api/v1
  -> Laravel JSON API
  -> Sanctum / token-based auth

Future mobile app
Expo / React Native
  -> consumes Laravel API
```

## Domain strategy

### Recommended

- `ediprofe.com` -> Astro static site
- `miembros.ediprofe.com` -> Laravel app

This is the recommended split for v2 because it gives:

- clear product boundary
- simpler deployment
- cleaner cookies / sessions
- no path-based proxy tricks
- no need to route `/miembros` from the static site to another origin

### What we are not recommending

- `ediprofe.com/miembros` routed to Laravel through Cloudflare Workers / Pages Functions

That can be made to work, but it adds moving parts and quota/billing considerations that are unnecessary for this project right now.

## Cloudflare and cost implications

### Good news

If your domain is already managed as a full zone in Cloudflare, you can point `miembros.ediprofe.com` to your VPS with a proxied `A`, `AAAA`, or `CNAME` record and stay on Cloudflare Free for that DNS/proxy layer.

Cloudflare documents that the proxyable record types are `A`, `AAAA`, and `CNAME`, and recommends proxying those records for web traffic:

- [Cloudflare proxy status docs](https://developers.cloudflare.com/dns/proxy-status/)

### What to avoid

Do not make the public static site forward `/miembros` by path using Workers / Pages Functions unless you truly need that exact URL shape.

Cloudflare documents that:

- Workers Free includes limited daily usage
- Pages Functions count toward the Workers Free quota

Sources:

- [Cloudflare Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/)
- [Cloudflare Pages Functions pricing](https://developers.cloudflare.com/pages/functions/pricing/)

### Practical recommendation

For lowest operational cost and least friction:

- keep public site on the current static hosting flow
- serve `miembros.ediprofe.com` directly from the VPS
- put Cloudflare in front only as proxied DNS / caching / protection

That should not add meaningful cost beyond the VPS you already pay for.

## Authentication strategy

### Web members app

For the web student app, move to:

- Google login with Socialite
- Laravel session / cookie auth
- Sanctum stateful mode only if needed for same-origin API calls
- Google OAuth web client config:
  - `GOOGLE_CLIENT_ID`
  - `GOOGLE_CLIENT_SECRET`
  - `GOOGLE_REDIRECT_URI`

Official references:

- [Laravel Socialite](https://laravel.com/docs/12.x/socialite)
- [Laravel Sanctum](https://laravel.com/docs/12.x/sanctum)

### Mobile

For mobile later, keep a separate auth path:

- native Google sign-in on the device
- backend token exchange endpoint
- Sanctum token auth or equivalent personal access token flow

This means:

- web does not need bearer tokens for the main authenticated experience
- mobile still has a clean token-based API path

### OAuth client recommendation

Use the same Google Cloud project, but separate OAuth clients by platform when possible:

- web OAuth client for `miembros.ediprofe.com`
- existing browser/token-exchange client for the current API-style login if you keep it temporarily
- mobile client later when the native app is ready

This avoids mixing redirect-based web auth with mobile or browser token flows in one credential.

### Current Google flow

The current Google login endpoint should be treated as the **mobile/API-style auth path**, not as the long-term auth mechanism for the web student app.

## Inertia and API can coexist

This is the most important architectural clarification.

We are **not** choosing between:

- "Laravel monolith"
- and "Laravel API"

We are choosing a **hybrid Laravel architecture**:

- Inertia + React for the student web app
- API endpoints for mobile and integrations

Inertia itself explicitly describes the approach as a "modern monolith" for classic server-driven web apps, and it does not require an API for the web surface:

- [Inertia docs](https://inertiajs.com/docs)

Laravel documents the React starter kit around that exact model:

- [Laravel starter kits](https://laravel.com/docs/12.x/starter-kits)

## Why not keep members in Astro with React islands

React islands inside Astro are technically supported, and fine for isolated interactive components.

But they are **not** the architecture we want for the next phase of `miembros`, because we need:

- authenticated layouts
- attempt flow
- navigation state
- page transitions
- richer client-side state
- progressively app-like UX

At that point, patching Astro with more islands would still leave the student app living in the wrong host architecture.

Astro stays excellent for the public editorial site. The student app should move.

## Rendering contract for questions

This migration is also our opportunity to stop depending on ad-hoc parsing in the student app.

### Rule

For the new members web app, question rendering should be based primarily on canonical HTML payloads:

- `context_html`
- `stem_html`
- `feedback_html`
- `concepts_html`
- `options[].text_html`

And use `blocks` only as fallback:

- `context_blocks`
- `stem_blocks`
- `feedback_blocks`
- `concepts_blocks`

### Why

This is the same data contract that best supports:

- web React renderer
- future React Native renderer
- rich content with tables, images, equations and shared contexts

### Important note

We are **not** trying to share the exact same UI components between web and mobile.

We are sharing:

- the backend schema
- the canonical content payload
- the attempt / question / review payload shape

That is the scalable layer to share.

## Phase-by-phase migration

### Phase 0. Freeze scope in Astro members

Goal:

- no more major UX work in Astro members
- only bug fixes and stability patches

Why:

- avoid doubling effort while the new student app is being built

### Phase 1. Prepare Laravel for Inertia + React

Inside [/apps/backend](/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/apps/backend):

- add `inertiajs/inertia-laravel`
- add React frontend dependencies
- wire Vite for React pages
- keep Filament untouched

Suggested frontend stack for members web:

- Inertia
- React
- TypeScript
- Tailwind
- `shadcn/ui` or a similarly restrained design system

### Phase 2. Add web route layer for members

Add a dedicated set of web controllers for student pages, for example:

- `App\Http\Controllers\Web\Members\DashboardController`
- `App\Http\Controllers\Web\Members\EvaluationsController`
- `App\Http\Controllers\Web\Members\EvaluationShowController`
- `App\Http\Controllers\Web\Members\TalleresController`
- `App\Http\Controllers\Web\Members\SimulacrosController`

These controllers return Inertia pages, not JSON.

JSON remains available under `/api/v1` for mobile.

### Phase 3. Add student React app shell

Suggested file layout:

```text
apps/backend/
  resources/
    js/
      app.tsx
      Layouts/
        MembersLayout.tsx
      Pages/
        Members/
          Dashboard.tsx
          Evaluations/
            Index.tsx
            Show.tsx
          Workshops/
            Index.tsx
            Show.tsx
          Simulacros/
            Index.tsx
            Show.tsx
      Components/
        members/
          RouteCard.tsx
          ActivityTable.tsx
          ProgressSummary.tsx
          QuestionNavigator.tsx
          PracticeRenderer/
            BlockRenderer.tsx
            TableBlock.tsx
            ImageBlock.tsx
            ListBlock.tsx
```

### Phase 4. Migrate auth for web members

Implement:

- `/login/google/redirect`
- `/login/google/callback`

using Socialite for the web student app.

Keep the current `POST /api/v1/auth/google/login` flow for API/mobile until the mobile auth layer is migrated cleanly.

### Phase 5. Port the student flows

Migration order:

1. dashboard
2. evaluation list
3. evaluation lobby / detail
4. attempt player
5. feedback / review flow
6. workshops
7. simulacros

That order matters because it closes the most important academic loop first.

### Phase 6. Build the new practice renderer

The React app should not rebuild the current string-based renderer.

Instead:

- render canonical HTML first
- normalize assets and safe wrappers in backend
- keep blocks only as fallback
- progressively upgrade tables, images, equations and lists into components where it adds value

This is the piece that reduces the class of bugs we just fixed.

### Phase 7. Sunset Astro members

When parity is achieved:

- keep `/miembros` public routes in Astro as redirects or informational entrypoints
- point students to `miembros.ediprofe.com`
- leave Astro responsible only for public/editorial surfaces

## Concrete route strategy

### Public site

- `https://ediprofe.com/`
- `https://ediprofe.com/simulacros/...`
- `https://ediprofe.com/...`

### Student app

- `https://miembros.ediprofe.com/`
- `https://miembros.ediprofe.com/evaluaciones`
- `https://miembros.ediprofe.com/evaluaciones/{id}`
- `https://miembros.ediprofe.com/talleres`
- `https://miembros.ediprofe.com/simulacros`

### Admin

- `https://miembros.ediprofe.com/admin`

Optional future refinement:

- move admin to `admin.ediprofe.com` only if you later want operational isolation

For v1 of this migration, that is not necessary.

## Deployment strategy

### Public site

Keep current static deploy flow unchanged.

### Laravel members app

Deploy Laravel on the VPS with:

- PHP-FPM / Nginx
- queue worker
- Vite-built assets
- HTTPS through Cloudflare proxy + origin cert / Let's Encrypt

### DNS

Create:

- `miembros` -> proxied `A` or `CNAME` to the VPS origin

If the zone is already on Cloudflare, this is straightforward on the free plan.

## Risks and tradeoffs

### What this plan improves

- much cleaner student UX foundation
- fewer frontend regressions from string-rendered markup
- better alignment with future mobile
- better auth story for web vs mobile
- public site stays stable

### What this plan does not do immediately

- it does not move question authoring out of MDX
- it does not rebuild teacher/admin
- it does not make web and mobile share UI

### Main migration risk

Running two student fronts in parallel temporarily:

- Astro members
- Laravel members

That is acceptable if Astro members is placed in maintenance-only mode during the migration.

## Recommendation

Proceed with:

- Astro public site unchanged
- Laravel + Inertia + React for `miembros.ediprofe.com`
- Laravel API retained for mobile
- Filament retained for admin
- Socialite for web Google login
- Sanctum / token auth for mobile

This is the cleanest path that protects your public site, your backend work, and the mobile future.
