# Academy Domain Boundaries

## Purpose

This document defines the domain boundaries for the academic platform so we do not keep overloading the assessment engine with responsibilities that belong somewhere else.

The goal is simple:

- keep the evaluation engine strong
- keep the platform flexible
- avoid building a fake "one table for everything" system

## Core principle

The academic platform is **not** one single module.

It should be split into:

1. platform core
2. assessment engine
3. future learning modules

These modules should share infrastructure, not collapse into one giant content model.

## 1. Platform core

This is the reusable foundation of the academy.

It should contain:

- users
- roles
- authentication
- member status
- courses
- enrollments
- access grants / subscriptions
- notifications
- progress summaries
- canonical assets
- API contracts

This layer should be reusable by every future module.

Examples:

- a student belongs to a course
- a teacher manages a course
- a user has permission to access a product
- an asset is available to web and mobile

## 2. Assessment engine

This is the module we are actively building now.

It should contain:

- templates
- shared contexts
- questions
- options
- assignments
- attempts
- answers
- scores
- review / feedback release
- exportable results

This engine should answer problems like:

- start an evaluation
- continue a workshop
- submit a simulacro
- release feedback later
- export grades for a course

This maps naturally to the current `assessment_*` tables.

## 3. Future learning modules

These should **not** be forced into the assessment engine unless they are actually question-based.

Possible future modules:

- lesson pages
- video lessons
- downloadable guides
- essay/open responses
- forums
- announcements
- live sessions
- rubric-based projects

These can still reuse:

- users
- courses
- assets
- permissions
- notifications
- API

But they should not be modeled as fake questions if they are not question-based.

## What belongs in `assessment_*`

Belongs there:

- multiple-choice questions
- shared stimulus/context groups
- right/wrong answer logic
- question review
- score calculation
- assignment policies
- timing / attempts / closing windows

Still acceptable there:

- study mode
- simulacro mode
- formal evaluation mode

Does not belong there by default:

- long-form editorial articles
- arbitrary CMS pages
- blog-like content
- institution news
- teacher profile pages
- generic file repositories

## Why this matters

If we make `assessment_*` try to become the whole LMS, two bad things happen:

1. the current engine becomes harder to evolve
2. future modules inherit constraints they never needed

That is exactly how flexible systems become rigid.

## Recommended platform shape

### Platform core

Suggested conceptual namespace:

- `academy_*` or existing non-assessment platform tables

Responsibilities:

- people
- courses
- memberships
- access
- assets
- reporting entry points

### Assessment engine

Suggested conceptual namespace:

- `assessment_*`

Responsibilities:

- interactive evaluable content
- scoring
- attempts
- feedback

### Future modules

Suggested pattern:

- module-specific bounded contexts

Examples:

- `lesson_*`
- `media_*`
- `project_*`

Only add them when they are real needs, not speculative abstractions.

## Practical rule for new features

When a new academic feature appears, ask this first:

### Question 1

Is this fundamentally based on:

- question
- option
- answer
- evaluation
- feedback

If yes, it probably belongs in `assessment_*`.

### Question 2

Is this fundamentally based on:

- publishing
- reading
- media consumption
- open production
- collaboration

If yes, it probably belongs in another module and should only reuse platform core.

## Current recommendation

Right now we should keep the focus narrow:

- strengthen the platform core where needed
- finish the assessment engine properly
- do **not** generalize the assessment engine into the entire academy

That is the most flexible route, not the least.

## Decision summary

The current path is appropriate **if we understand its scope correctly**:

- Laravel remains the backend nucleus
- `assessment_*` remains the interactive evaluation engine
- web and mobile consume canonical content from Laravel
- future academy features should be added as separate modules, not jammed into the assessment model

This is the boundary that keeps the project scalable.
