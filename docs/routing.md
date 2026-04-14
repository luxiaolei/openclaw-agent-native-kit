# Routing Guide

## Core idea

Keep the conductor session responsible for planning, wave control, synthesis, and final user communication.
Route repeated specialist work into explicit specialist agents instead of relying only on generic same-agent subagents.

## Specialist lanes

### `specialist-stitch-designer`
Use for design-system shaping, Stitch prompt refinement, screen flow planning, and baton writing.

### `specialist-frontend-fullstack`
Use for approved frontend implementation, Stitch-to-code work, browser-backed bug reproduction, and UI verification.

### `specialist-backend-systems`
Use for backend code, APIs, scripts, data flow, and implementation-focused bug fixes.

### `specialist-review-architect`
Use for milestone review, architecture review, and high-risk regression review.

### `specialist-qa-governor`
Use for browser QA, regression testing, accessibility verification, and release readiness.

### `specialist-openclaw-governor`
Use for OpenClaw agent governance, skill governance, registration work, and public pack design.

## Routing rules

- If a qualified specialist exists, prefer it over a generic subagent.
- If browser verification matters, require browser-backed evidence.
- If agent governance changes affect runtime reality, update both workspace files and config registration.
- If a task crosses lanes, split it into separate checklist items.
