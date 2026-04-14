# OpenClaw Agent Native Kit

> Portable OpenClaw-native specialist agents, governance skills, and autonomous conductor tooling.
>
> 一个可移植的 OpenClaw Agent Native 套件，提供专精 agents、共享 skills、治理能力和可复用安装方式，方便在多台机器上快速落地。

## What it does

This repo gives you a ready-made **agent-native operating layer** for OpenClaw:

- a **specialist roster** instead of vague generalist fan-out
- shared **execution and governance skills**
- a **conductor-centered autonomous execution model**
- reusable **agent templates**, **registration config**, and **install scripts**
- a validation path so the pack is not just prompt files, but actually installable and governable

## Core capabilities

### Specialized agents

- `specialist-stitch-designer`
- `specialist-frontend-fullstack`
- `specialist-backend-systems`
- `specialist-review-architect`
- `specialist-qa-governor`
- `specialist-openclaw-governor`

### Shared skills

- `autonomous-master-plan-executor`
- `stitch`
- `openclaw-agent-governance`

### Operational features

- conductor-led task routing
- staged plan/build/review execution
- specialist-first delegation
- browser-backed frontend and QA lanes
- OpenClaw agent governance and packaging support
- install + validation workflow for multi-machine rollout

## Who this is for

- teams building **multi-agent OpenClaw setups**
- operators who want **specialists instead of one giant generalist agent**
- people doing **agent-native engineering**, where many tasks are really “change the agent” tasks
- anyone who wants to package and reuse OpenClaw specialists across machines

## Included structure

```text
agent-templates/   reusable specialist workspace templates
skills/            shared execution and governance skills
config/            sample registration JSON
scripts/           install + validation helpers
docs/              architecture and routing notes
```

## Why a git repo first

This pack is intentionally a **portable git repo first**, not a plugin first.

Why:

- easier to install across machines
- easier to version and review
- easier to publish and collaborate on
- easier to validate structure before pluginizing
- plugin packaging can come later once the pack stabilizes

## Install

```bash
python3 scripts/install.py --home ~/.openclaw --register
python3 scripts/validate.py --home ~/.openclaw
```

## Routing overview

- Stitch design → `specialist-stitch-designer`
- Frontend design-to-code + browser verification → `specialist-frontend-fullstack`
- Backend / API / automation → `specialist-backend-systems`
- Milestone review / architecture review → `specialist-review-architect`
- Browser QA / regression / accessibility → `specialist-qa-governor`
- Agent governance / skill governance / packaging → `specialist-openclaw-governor`

See also:
- `docs/architecture.md`
- `docs/routing.md`

## Automation

This repo includes GitHub Actions for:

- validation on `push` / `pull_request`
- end-to-end install smoke testing
- tag-driven release packaging from `CHANGELOG.md`

## Source inspirations

- `stitch-skills`
- `gstack`
- `agency-agents`
- OpenClaw multi-agent and agent-workspace docs

## Notes

- This repo intentionally excludes secrets, auth stores, and private memory.
- Fill in environment-specific `TOOLS.md` details locally after install.
- Adjust models, bindings, and channel routing per machine.
- See `CHANGELOG.md` for release history.
