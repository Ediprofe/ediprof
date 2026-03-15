# Laravel Canonical Content Model

## Purpose

This document defines the recommended **long-term content model** for the academic platform when Laravel becomes the source of truth for:

- questions
- shared contexts
- options
- feedback
- related concepts
- assets
- publication to web and mobile

This model is designed to:

- stop depending on `MDX` at runtime
- keep web and mobile aligned
- preserve the current academic domain already built in Laravel
- avoid a rewrite of the assessment engine

Domain scope and module boundaries:

- [Academy Domain Boundaries](/Users/edilbertosuarez/Documents/EDIPROFE.COM/ediprof/docs/new-features/academy-domain-boundaries.md)

## Executive decision

We should **not** replace the current academic domain.

We should **evolve** the current Laravel assessment schema into the canonical content model.

That means:

- keep the existing `assessment_*` tables as the base
- stop treating them as a sync cache only
- grow them into the real content source of truth
- treat `MDX` as an import path during migration

## What already exists and should be preserved

These tables already represent the right academic concepts:

- `assessment_templates`
- `assessment_contexts`
- `assessment_questions`
- `assessment_question_contexts`
- `assessment_assignments`
- `assessment_assignment_questions`
- `assessment_attempts`
- `assessment_attempt_answers`

This is already a strong foundation.

The current weakness is not the domain model itself.
The weakness is that content authoring and render output are still too tied to `MDX` export assumptions.

## Recommended long-term model

### 1. `assessment_templates`

Keep this table.

Role in the final model:

- editorial or curricular collection
- source grouping for questions and contexts
- still useful even after content becomes canonical in Laravel

Examples:

- `Simulacro 11 · Ciencias Naturales · S1`
- `Taller: Átomos y configuración electrónica`

Recommended meaning going forward:

- a template is a curated collection, not the only owner of content forever
- in a later phase, one question may belong to multiple collections if needed
- but we do **not** need to solve multi-collection reuse immediately

### 2. `assessment_contexts`

Keep this table and strengthen it.

Role:

- canonical shared stimulus / shared context unit
- owns the content that multiple questions depend on

This is the correct place for cases like:

- questions 95, 96 and 97 sharing one context

Recommended canonical fields per context:

- `plain_text`
- `html_web`
- `nodes_mobile`
- `asset_refs`
- `metadata`

Incremental mapping from current fields:

- `context_mdx`
  - legacy import/editorial field
- `context_html`
  - keep and rename conceptually to `html_web`
- `context_blocks`
  - transitional fallback only
- `context_assets`
  - keep short term, evolve into canonical `asset_refs`

### 3. `assessment_questions`

Keep this table and make it the canonical question record.

Role:

- question identity
- question order within a template if needed
- stem
- correct option
- feedback
- concepts
- taxonomy

Recommended canonical fields per rich fragment in the question:

- `stem_plain`
- `stem_html`
- `stem_nodes`
- `stem_asset_refs`

- `feedback_plain`
- `feedback_html`
- `feedback_nodes`
- `feedback_asset_refs`

- `concepts_plain`
- `concepts_html`
- `concepts_nodes`
- `concepts_asset_refs`

Current schema already contains most of this pattern, which is good.
The missing piece is to stop treating it as an export cache and start treating it as the real content payload.

### 4. `assessment_question_options`

This is the first important new table I would add.

Current problem:

- options live inside `assessment_questions.options` as JSON
- that is acceptable for sync payloads
- but it is not ideal if Laravel becomes the real editor/source of truth

Recommended new table:

`assessment_question_options`

Suggested columns:

- `id`
- `question_id`
- `option_id`
  - `A`, `B`, `C`, `D`
- `order_base`
- `is_correct`
- `plain_text`
- `html_web`
- `nodes_mobile`
- `asset_refs`
- `metadata`
- `created_at`
- `updated_at`

Why this table matters:

- options are rich content too
- options may contain math, SVG, tables or formatting
- options may need future editorial status or analytics
- mobile and web need a clean contract for them

My recommendation is:

- keep `assessment_questions.options` during transition
- add `assessment_question_options`
- migrate reads gradually
- eventually treat the JSON field as legacy/import-only

### 5. `content_assets`

This is the second table I would definitely add.

Current problem:

- assets are stored mostly as string refs or relative paths
- clients still infer too much about origin and file availability

Recommended table:

`content_assets`

Suggested columns:

- `id`
- `asset_key`
  - stable internal key
- `source_path`
  - original renderer or source path
- `canonical_url`
- `fallback_url`
  - useful for SVG to PNG/WebP fallback
- `mime_type`
- `kind`
  - `svg`, `png`, `jpg`, `webp`, `audio`, etc.
- `width`
- `height`
- `checksum`
- `metadata`
- `created_at`
- `updated_at`

Why this matters:

- assets become portable across web and mobile
- Laravel can serve stable metadata
- clients stop relying on project-relative paths
- generated SVGs are no longer "owned" by one frontend runtime

### 6. `content_asset_usages`

I recommend this table, but it is less urgent than options/assets.

Purpose:

- link assets to contexts, questions, options or collections
- allow queries like:
  - unused assets
  - all assets referenced by one template
  - all assets needed offline for one assignment

Suggested columns:

- `id`
- `asset_id`
- `usable_type`
- `usable_id`
- `role`
  - `stem`, `context`, `option`, `feedback`, `concepts`, `template`
- `order_base`
- `metadata`

This is a clean long-term answer, but we can delay it if needed and keep `asset_refs` JSON during migration.

## Recommended render contract

For every rich content fragment, Laravel should be able to provide:

- `plain_text`
- `html_web`
- `nodes_mobile`
- `asset_refs`

### Web

Web should render:

- `html_web`

### Mobile

Mobile should render:

- `nodes_mobile`

### Legacy fallback

`blocks` can still exist during transition, but they should be considered:

- legacy
- compatibility only
- not the future source contract

## Why not use a generic `content_fragments` table

I would **not** start with a polymorphic table like:

- `content_fragments`
- `fragment_type`
- `owner_type`
- `owner_id`

That sounds elegant, but in this project it would likely slow us down.

Why:

- the domain is already explicit
- questions, contexts and options are meaningful units
- explicit fields are easier to reason about in Filament, API resources and export logic

So my recommendation is:

- use explicit domain tables
- use consistent fragment field naming
- avoid over-abstracting too early

## Recommended source-of-truth strategy

### Stage 1. Today

- `MDX` still authors content
- export sync fills Laravel
- Laravel is the runtime source for clients

### Stage 2. Transition

- Laravel content tables become canonical
- `MDX` becomes import-only
- edits in Laravel become possible for selected mutable fields first

### Stage 3. Final

- Laravel is the only source of truth for academic content
- `MDX` is optional or legacy
- public site, web app and mobile consume Laravel content contracts

## Recommended migration strategy

### Phase A. Do not change the engine yet

Keep:

- assignments
- attempts
- grading
- exports

They are already the strongest part of the product.

### Phase B. Introduce the two critical tables

Add first:

1. `assessment_question_options`
2. `content_assets`

These two give the biggest structural gain with the least conceptual risk.

### Phase C. Normalize reads in backend

Backend services should begin to read:

- options from `assessment_question_options`
- assets from canonical URLs and metadata

while still keeping compatibility with legacy JSON during migration.

### Phase D. Add `nodes_mobile`

Once the web app is stable on `html_web`, formalize `nodes_mobile` in Laravel.

That lets mobile stop depending on weak fallbacks.

### Phase E. Move authoring ownership

Only after the canonical model is stable:

- decide whether to build real authoring UI in Filament or another editor
- import legacy `MDX` into canonical Laravel content

## What I would implement first

If we are serious about making Laravel the content source of truth, the first concrete schema step should be:

1. add `assessment_question_options`
2. add `content_assets`
3. keep everything else stable

That is the most realistic and highest-leverage move.

## Recommended next engineering step

After this design, the next implementation step should be:

- add migrations for `assessment_question_options` and `content_assets`
- update the sync service to populate them
- update API resources to read from them when present

That would be the first real move from `MDX-synced cache` to `Laravel canonical content model`.
