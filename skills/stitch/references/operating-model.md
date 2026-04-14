# Stitch operating model

This local skill condenses the useful parts of the reference repos into an OpenClaw-native workflow.

## Core pattern

1. Clarify the slice.
2. Produce or refine the Stitch design.
3. Sync the design intent into the app structure.
4. Productionize the code instead of dumping raw exported HTML.
5. Verify in a browser-backed environment.
6. Record the next baton.

## When to route to specialists

- `specialist-stitch-designer` for design-system and prompt work
- `specialist-frontend-fullstack` for implementation and browser-verified UI fixes
- `specialist-qa-governor` for independent QA and release gating
- `specialist-review-architect` for milestone review or difficult regressions

## Baton minimum

A clean baton should include:
- objective
- target page or slice
- design-system constraints
- affected paths
- acceptance check
- stop condition

## Anti-patterns

- stopping at screenshots or exported HTML
- skipping browser QA on integrated frontend changes
- regenerating whole screens when a small targeted edit would do
- claiming design is production-ready without state, error, and responsive handling
