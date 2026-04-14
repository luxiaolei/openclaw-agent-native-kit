# Specialist routing

Use this file when deciding whether to route a checklist item to a specialist agent, a same-agent subagent, or a persistent specialist session.

## Priority order

1. Use a registered specialist agent when the task clearly matches a domain.
2. Use a same-agent subagent when the task is narrow and no strong specialist exists.
3. Use a persistent specialist session only when long-lived specialist history matters.

## Current registered routing targets

- Stitch design: `specialist-stitch-designer`
- frontend full-stack: `specialist-frontend-fullstack`
- backend systems: `specialist-backend-systems`
- review architect: `specialist-review-architect`
- QA governor: `specialist-qa-governor`
- OpenClaw governance: `specialist-openclaw-governor`

## Routing matrix

### Stitch design specialist

Use for:
- prompt enhancement for Stitch
- design-system normalization
- screen flow definition
- baton preparation for downstream implementation

Recommended target agentId: `specialist-stitch-designer`

### Frontend full-stack specialist

Use for:
- frontend design implementation
- Stitch-based UI generation or iteration that must land in a real app
- browser validation and test-return loops
- Mac mini browser-backed verification
- UI bug reproduction that requires remote browser work

Required global skills:
- `stitch`
- `remote-opencli`

Hard requirement:
- If a frontend specialist does not have both skills, it is not qualified for Stitch-driven frontend execution.
- If browser access or return-path verification depends on Mac mini OpenCLI, route through `remote-opencli`.
- If this capability slot is missing, stop and report the gap instead of silently downgrading to a generic coder.

Recommended target agentId: `specialist-frontend-fullstack`

### Coding / backend specialist

Use for:
- implementation
- refactors
- tests
- scripts
- bug fixing
- APIs and data flow

Required traits:
- strong coding execution
- respects scope boundaries
- produces verification commands

Recommended target agentId: `specialist-backend-systems`

### Review specialist

Use for:
- milestone review
- correctness review
- regression review
- security or architecture review

Rules:
- run at milestone boundaries, not after every tiny task
- prefer an independent child from the builder

Recommended target agentId: `specialist-review-architect`

### QA specialist

Use for:
- browser QA
- regression testing
- accessibility checks
- release-readiness validation

Rules:
- do not sign off from code inspection alone when runtime verification matters
- prefer browser-backed evidence

Recommended target agentId: `specialist-qa-governor`

### OpenClaw governance specialist

Use for:
- agent workspace creation or revision
- AGENTS/SOUL/USER/TOOLS governance changes
- specialist roster design and registration
- reusable pack or install flow design
- OpenClaw skill governance and public distribution structure

Required traits:
- understands OpenClaw runtime structure
- keeps workspace files and config registration aligned
- does not treat agent design as prompt-only writing

Recommended target agentId: `specialist-openclaw-governor`

## Fallback rules

- If a specialist exists, prefer it over a generic same-agent subagent.
- If no specialist exists and the task is small, use a narrow same-agent subagent.
- If no specialist exists and the task is large or safety-critical, stop and report the missing coverage.
- Do not silently reroute governance work to a generic reviewer when runtime registration or packaging is involved.

## Handoff minimums

Every specialist handoff should include:
- task ID
- objective
- scope boundary
- allowed paths or surfaces
- output path or deliverable
- acceptance test
- stop condition
- timeout
