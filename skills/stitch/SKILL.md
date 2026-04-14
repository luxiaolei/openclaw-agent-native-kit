---
name: stitch
description: Unified Stitch design-to-code skill for OpenClaw. Use when work involves Stitch-driven UI generation, design-system normalization, handoff batons, frontend implementation loops, or browser-verified UI iteration.
---

# Stitch

Use this skill when a task needs the real Stitch workflow rather than generic frontend coding.

## Source inspirations

- `stitch-skills`: prompt enhancement, design-system synthesis, design-to-code baton flow
- `gstack`: staged planning and review discipline
- `agency-agents`: clear specialist lanes and deliverables

## Routing

Choose one of two lanes:

1. **Design lane**
   - convert rough intent into Stitch-ready prompt language
   - normalize the design system
   - define screens, flows, and baton files
   - stop after the design handoff is clean

2. **Full-stack lane**
   - generate or refine the Stitch design
   - integrate the slice into the real frontend codebase
   - run browser QA on the integrated result
   - fix issues and retest before calling the slice done

## Hard rules

- A Stitch task is not complete when only the mockup exists.
- If the task requires browser-backed validation, use `remote-opencli` and preferably `agent-browser`.
- Do not downgrade a missing Stitch or browser path into generic guesswork.
- Keep a baton or next-prompt style handoff so the loop can continue cleanly.

## Deliverables

Return:
- the design intent in structured form
- the artifact or code path that changed
- the verification method used
- the next baton if more Stitch work remains

## Read next

- `references/operating-model.md`
